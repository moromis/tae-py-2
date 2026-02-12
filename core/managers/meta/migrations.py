from core.helpers.fprint import fprint
from core.managers.meta import meta_manager


class Migrator:

    @classmethod
    def set_json(cls, json):
        cls.json = json

    @classmethod
    def _migration_noop(cls, *args, **kwargs):
        return cls.json

    @classmethod
    def _set_new_version(cls):
        cls.json["meta"][
            meta_manager.META_KEYS.SCHEMA.value
        ] = meta_manager.CURRENT_SCHEMA_VERSION.value

    @classmethod
    def _migrate_to_0_0_3(cls):
        json = cls.json
        if json:
            if (
                json["meta"][meta_manager.META_KEYS.SCHEMA.value]
                == meta_manager.SCHEMA_VERSIONS._0_0_2.value
            ):
                for o in json["objects"]:
                    json["objects"][o]["properties"] = {}
                json["meta"][
                    meta_manager.META_KEYS.SCHEMA.value
                ] = meta_manager.SCHEMA_VERSIONS._0_0_3.value
            return json

    @classmethod
    def needs_migration(cls) -> bool:
        current_schema = meta_manager.CURRENT_SCHEMA_VERSION.value
        json_schema = cls.json["meta"][meta_manager.META_KEYS.SCHEMA.value]
        if current_schema == json_schema:
            return False
        else:
            return True

    @classmethod
    def migrate(cls):
        MIGRATIONS = [
            cls._migration_noop,  # v0.0.0 -> v0.0.1
            cls._migration_noop,  # v0.0.1 -> v0.0.2
            cls._migrate_to_0_0_3,  # v0.0.2 -> v0.0.3
        ]

        current_schema = meta_manager.CURRENT_SCHEMA_VERSION.value
        json_schema = cls.json["meta"][meta_manager.META_KEYS.SCHEMA.value]
        if not cls.needs_migration():
            return cls.json
        versions = [s.value for s in meta_manager.SCHEMA_VERSIONS]
        current_index = -1
        json_index = -1
        for i, schema in enumerate(versions):
            if schema == current_schema:
                current_index = i
            if schema == json_schema:
                json_index = i

        # migrate
        fprint("MIGRATING...\n0%")
        total_steps = current_index - json_index + 1
        if json_index < current_index:
            for migration_index in range(json_index + 1, current_index + 1):
                cls.json = MIGRATIONS[migration_index]()
                fprint(f"Successfully migrated game to v{versions[migration_index]}")
                fprint(f"{round((migration_index / total_steps) * 100, 2)}%")

        # validate
        pass

        # set new version
        cls._set_new_version()

        return cls.json
