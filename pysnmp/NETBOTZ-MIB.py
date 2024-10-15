# SNMP MIB module (NETBOTZ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETBOTZ-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:34 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetBotz_ObjectIdentity = ObjectIdentity
netBotz = _NetBotz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528)
)
_NetBotz_reg_ObjectIdentity = ObjectIdentity
netBotz_reg = _NetBotz_reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 10)
)
_NetBotz_generic_ObjectIdentity = ObjectIdentity
netBotz_generic = _NetBotz_generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 20)
)
_NetBotz_products_ObjectIdentity = ObjectIdentity
netBotz_products = _NetBotz_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30)
)
_NetBotz_prd_bot_ObjectIdentity = ObjectIdentity
netBotz_prd_bot = _NetBotz_prd_bot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10)
)
_NetBotz_prd_bot_temp_Type = Integer32
_NetBotz_prd_bot_temp_Object = MibScalar
netBotz_prd_bot_temp = _NetBotz_prd_bot_temp_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 1),
    _NetBotz_prd_bot_temp_Type()
)
netBotz_prd_bot_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_temp.setStatus("mandatory")
_NetBotz_prd_bot_humidity_Type = Integer32
_NetBotz_prd_bot_humidity_Object = MibScalar
netBotz_prd_bot_humidity = _NetBotz_prd_bot_humidity_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 2),
    _NetBotz_prd_bot_humidity_Type()
)
netBotz_prd_bot_humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_humidity.setStatus("mandatory")
_NetBotz_prd_bot_airflow_Type = Integer32
_NetBotz_prd_bot_airflow_Object = MibScalar
netBotz_prd_bot_airflow = _NetBotz_prd_bot_airflow_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 3),
    _NetBotz_prd_bot_airflow_Type()
)
netBotz_prd_bot_airflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_airflow.setStatus("mandatory")
_NetBotz_prd_bot_audio_Type = Integer32
_NetBotz_prd_bot_audio_Object = MibScalar
netBotz_prd_bot_audio = _NetBotz_prd_bot_audio_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 4),
    _NetBotz_prd_bot_audio_Type()
)
netBotz_prd_bot_audio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_audio.setStatus("mandatory")
_NetBotz_prd_bot_doorajar_Type = Integer32
_NetBotz_prd_bot_doorajar_Object = MibScalar
netBotz_prd_bot_doorajar = _NetBotz_prd_bot_doorajar_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 5),
    _NetBotz_prd_bot_doorajar_Type()
)
netBotz_prd_bot_doorajar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_doorajar.setStatus("mandatory")
_NetBotz_prd_bot_temp_min_Type = Integer32
_NetBotz_prd_bot_temp_min_Object = MibScalar
netBotz_prd_bot_temp_min = _NetBotz_prd_bot_temp_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 6),
    _NetBotz_prd_bot_temp_min_Type()
)
netBotz_prd_bot_temp_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_temp_min.setStatus("mandatory")
_NetBotz_prd_bot_temp_max_Type = Integer32
_NetBotz_prd_bot_temp_max_Object = MibScalar
netBotz_prd_bot_temp_max = _NetBotz_prd_bot_temp_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 7),
    _NetBotz_prd_bot_temp_max_Type()
)
netBotz_prd_bot_temp_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_temp_max.setStatus("mandatory")
_NetBotz_prd_bot_humidity_min_Type = Integer32
_NetBotz_prd_bot_humidity_min_Object = MibScalar
netBotz_prd_bot_humidity_min = _NetBotz_prd_bot_humidity_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 8),
    _NetBotz_prd_bot_humidity_min_Type()
)
netBotz_prd_bot_humidity_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_humidity_min.setStatus("mandatory")
_NetBotz_prd_bot_humidity_max_Type = Integer32
_NetBotz_prd_bot_humidity_max_Object = MibScalar
netBotz_prd_bot_humidity_max = _NetBotz_prd_bot_humidity_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 9),
    _NetBotz_prd_bot_humidity_max_Type()
)
netBotz_prd_bot_humidity_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_humidity_max.setStatus("mandatory")
_NetBotz_prd_bot_airflow_mins_Type = Integer32
_NetBotz_prd_bot_airflow_mins_Object = MibScalar
netBotz_prd_bot_airflow_mins = _NetBotz_prd_bot_airflow_mins_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 10),
    _NetBotz_prd_bot_airflow_mins_Type()
)
netBotz_prd_bot_airflow_mins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_airflow_mins.setStatus("mandatory")
_NetBotz_prd_bot_audio_secs_Type = Integer32
_NetBotz_prd_bot_audio_secs_Object = MibScalar
netBotz_prd_bot_audio_secs = _NetBotz_prd_bot_audio_secs_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 11),
    _NetBotz_prd_bot_audio_secs_Type()
)
netBotz_prd_bot_audio_secs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_audio_secs.setStatus("mandatory")
_NetBotz_prd_bot_temp_enabled_Type = Integer32
_NetBotz_prd_bot_temp_enabled_Object = MibScalar
netBotz_prd_bot_temp_enabled = _NetBotz_prd_bot_temp_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 12),
    _NetBotz_prd_bot_temp_enabled_Type()
)
netBotz_prd_bot_temp_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_temp_enabled.setStatus("mandatory")
_NetBotz_prd_bot_hum_enabled_Type = Integer32
_NetBotz_prd_bot_hum_enabled_Object = MibScalar
netBotz_prd_bot_hum_enabled = _NetBotz_prd_bot_hum_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 13),
    _NetBotz_prd_bot_hum_enabled_Type()
)
netBotz_prd_bot_hum_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_hum_enabled.setStatus("mandatory")
_NetBotz_prd_bot_air_enabled_Type = Integer32
_NetBotz_prd_bot_air_enabled_Object = MibScalar
netBotz_prd_bot_air_enabled = _NetBotz_prd_bot_air_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 14),
    _NetBotz_prd_bot_air_enabled_Type()
)
netBotz_prd_bot_air_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_air_enabled.setStatus("mandatory")
_NetBotz_prd_bot_audio_enabled_Type = Integer32
_NetBotz_prd_bot_audio_enabled_Object = MibScalar
netBotz_prd_bot_audio_enabled = _NetBotz_prd_bot_audio_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 15),
    _NetBotz_prd_bot_audio_enabled_Type()
)
netBotz_prd_bot_audio_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_audio_enabled.setStatus("mandatory")
_NetBotz_prd_bot_switch_state_Type = Integer32
_NetBotz_prd_bot_switch_state_Object = MibScalar
netBotz_prd_bot_switch_state = _NetBotz_prd_bot_switch_state_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 16),
    _NetBotz_prd_bot_switch_state_Type()
)
netBotz_prd_bot_switch_state.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_switch_state.setStatus("mandatory")
_NetBotz_prd_bot_switch_enabled_Type = Integer32
_NetBotz_prd_bot_switch_enabled_Object = MibScalar
netBotz_prd_bot_switch_enabled = _NetBotz_prd_bot_switch_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 17),
    _NetBotz_prd_bot_switch_enabled_Type()
)
netBotz_prd_bot_switch_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_switch_enabled.setStatus("mandatory")
_NetBotz_prd_bot_audio_level_Type = Integer32
_NetBotz_prd_bot_audio_level_Object = MibScalar
netBotz_prd_bot_audio_level = _NetBotz_prd_bot_audio_level_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 18),
    _NetBotz_prd_bot_audio_level_Type()
)
netBotz_prd_bot_audio_level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_audio_level.setStatus("mandatory")
_NetBotz_prd_bot_trap_index_Type = Integer32
_NetBotz_prd_bot_trap_index_Object = MibScalar
netBotz_prd_bot_trap_index = _NetBotz_prd_bot_trap_index_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 20),
    _NetBotz_prd_bot_trap_index_Type()
)
netBotz_prd_bot_trap_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_trap_index.setStatus("mandatory")
_NetBotz_prd_bot_trap_address_Type = IpAddress
_NetBotz_prd_bot_trap_address_Object = MibScalar
netBotz_prd_bot_trap_address = _NetBotz_prd_bot_trap_address_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 21),
    _NetBotz_prd_bot_trap_address_Type()
)
netBotz_prd_bot_trap_address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_trap_address.setStatus("mandatory")
_NetBotz_prd_bot_trap_oid_Type = ObjectIdentifier
_NetBotz_prd_bot_trap_oid_Object = MibScalar
netBotz_prd_bot_trap_oid = _NetBotz_prd_bot_trap_oid_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 22),
    _NetBotz_prd_bot_trap_oid_Type()
)
netBotz_prd_bot_trap_oid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_trap_oid.setStatus("mandatory")
_NetBotz_prd_bot_trap_value_Type = Integer32
_NetBotz_prd_bot_trap_value_Object = MibScalar
netBotz_prd_bot_trap_value = _NetBotz_prd_bot_trap_value_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 23),
    _NetBotz_prd_bot_trap_value_Type()
)
netBotz_prd_bot_trap_value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_trap_value.setStatus("mandatory")
_NetBotz_prd_bot_trap_date_Type = Integer32
_NetBotz_prd_bot_trap_date_Object = MibScalar
netBotz_prd_bot_trap_date = _NetBotz_prd_bot_trap_date_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 24),
    _NetBotz_prd_bot_trap_date_Type()
)
netBotz_prd_bot_trap_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_trap_date.setStatus("mandatory")
_NetBotz_prd_bot_refresh_Type = Integer32
_NetBotz_prd_bot_refresh_Object = MibScalar
netBotz_prd_bot_refresh = _NetBotz_prd_bot_refresh_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 26),
    _NetBotz_prd_bot_refresh_Type()
)
netBotz_prd_bot_refresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_refresh.setStatus("mandatory")
_NetBotz_prd_bot_airflow_level_Type = Integer32
_NetBotz_prd_bot_airflow_level_Object = MibScalar
netBotz_prd_bot_airflow_level = _NetBotz_prd_bot_airflow_level_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 27),
    _NetBotz_prd_bot_airflow_level_Type()
)
netBotz_prd_bot_airflow_level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_airflow_level.setStatus("mandatory")
_NetBotz_prd_bot_doorpic_count_Type = Integer32
_NetBotz_prd_bot_doorpic_count_Object = MibScalar
netBotz_prd_bot_doorpic_count = _NetBotz_prd_bot_doorpic_count_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 28),
    _NetBotz_prd_bot_doorpic_count_Type()
)
netBotz_prd_bot_doorpic_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_doorpic_count.setStatus("mandatory")
_NetBotz_prd_bot_amps1_Type = Integer32
_NetBotz_prd_bot_amps1_Object = MibScalar
netBotz_prd_bot_amps1 = _NetBotz_prd_bot_amps1_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 29),
    _NetBotz_prd_bot_amps1_Type()
)
netBotz_prd_bot_amps1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps1.setStatus("mandatory")
_NetBotz_prd_bot_amps1_enabled_Type = Integer32
_NetBotz_prd_bot_amps1_enabled_Object = MibScalar
netBotz_prd_bot_amps1_enabled = _NetBotz_prd_bot_amps1_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 30),
    _NetBotz_prd_bot_amps1_enabled_Type()
)
netBotz_prd_bot_amps1_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps1_enabled.setStatus("mandatory")
_NetBotz_prd_bot_amps1_min_Type = Integer32
_NetBotz_prd_bot_amps1_min_Object = MibScalar
netBotz_prd_bot_amps1_min = _NetBotz_prd_bot_amps1_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 31),
    _NetBotz_prd_bot_amps1_min_Type()
)
netBotz_prd_bot_amps1_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps1_min.setStatus("mandatory")
_NetBotz_prd_bot_amps1_max_Type = Integer32
_NetBotz_prd_bot_amps1_max_Object = MibScalar
netBotz_prd_bot_amps1_max = _NetBotz_prd_bot_amps1_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 32),
    _NetBotz_prd_bot_amps1_max_Type()
)
netBotz_prd_bot_amps1_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps1_max.setStatus("mandatory")
_NetBotz_prd_bot_amps2_Type = Integer32
_NetBotz_prd_bot_amps2_Object = MibScalar
netBotz_prd_bot_amps2 = _NetBotz_prd_bot_amps2_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 34),
    _NetBotz_prd_bot_amps2_Type()
)
netBotz_prd_bot_amps2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps2.setStatus("mandatory")
_NetBotz_prd_bot_amps2_enabled_Type = Integer32
_NetBotz_prd_bot_amps2_enabled_Object = MibScalar
netBotz_prd_bot_amps2_enabled = _NetBotz_prd_bot_amps2_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 35),
    _NetBotz_prd_bot_amps2_enabled_Type()
)
netBotz_prd_bot_amps2_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps2_enabled.setStatus("mandatory")
_NetBotz_prd_bot_amps2_min_Type = Integer32
_NetBotz_prd_bot_amps2_min_Object = MibScalar
netBotz_prd_bot_amps2_min = _NetBotz_prd_bot_amps2_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 36),
    _NetBotz_prd_bot_amps2_min_Type()
)
netBotz_prd_bot_amps2_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps2_min.setStatus("mandatory")
_NetBotz_prd_bot_amps2_max_Type = Integer32
_NetBotz_prd_bot_amps2_max_Object = MibScalar
netBotz_prd_bot_amps2_max = _NetBotz_prd_bot_amps2_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 37),
    _NetBotz_prd_bot_amps2_max_Type()
)
netBotz_prd_bot_amps2_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps2_max.setStatus("mandatory")
_NetBotz_prd_bot_amps3_Type = Integer32
_NetBotz_prd_bot_amps3_Object = MibScalar
netBotz_prd_bot_amps3 = _NetBotz_prd_bot_amps3_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 39),
    _NetBotz_prd_bot_amps3_Type()
)
netBotz_prd_bot_amps3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps3.setStatus("mandatory")
_NetBotz_prd_bot_amps3_enabled_Type = Integer32
_NetBotz_prd_bot_amps3_enabled_Object = MibScalar
netBotz_prd_bot_amps3_enabled = _NetBotz_prd_bot_amps3_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 40),
    _NetBotz_prd_bot_amps3_enabled_Type()
)
netBotz_prd_bot_amps3_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps3_enabled.setStatus("mandatory")
_NetBotz_prd_bot_amps3_min_Type = Integer32
_NetBotz_prd_bot_amps3_min_Object = MibScalar
netBotz_prd_bot_amps3_min = _NetBotz_prd_bot_amps3_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 41),
    _NetBotz_prd_bot_amps3_min_Type()
)
netBotz_prd_bot_amps3_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps3_min.setStatus("mandatory")
_NetBotz_prd_bot_amps3_max_Type = Integer32
_NetBotz_prd_bot_amps3_max_Object = MibScalar
netBotz_prd_bot_amps3_max = _NetBotz_prd_bot_amps3_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 42),
    _NetBotz_prd_bot_amps3_max_Type()
)
netBotz_prd_bot_amps3_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps3_max.setStatus("mandatory")
_NetBotz_prd_bot_amps_total_Type = Integer32
_NetBotz_prd_bot_amps_total_Object = MibScalar
netBotz_prd_bot_amps_total = _NetBotz_prd_bot_amps_total_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 44),
    _NetBotz_prd_bot_amps_total_Type()
)
netBotz_prd_bot_amps_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps_total.setStatus("mandatory")
_NetBotz_prd_bot_amps_total_enabled_Type = Integer32
_NetBotz_prd_bot_amps_total_enabled_Object = MibScalar
netBotz_prd_bot_amps_total_enabled = _NetBotz_prd_bot_amps_total_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 45),
    _NetBotz_prd_bot_amps_total_enabled_Type()
)
netBotz_prd_bot_amps_total_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps_total_enabled.setStatus("mandatory")
_NetBotz_prd_bot_amps_total_min_Type = Integer32
_NetBotz_prd_bot_amps_total_min_Object = MibScalar
netBotz_prd_bot_amps_total_min = _NetBotz_prd_bot_amps_total_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 46),
    _NetBotz_prd_bot_amps_total_min_Type()
)
netBotz_prd_bot_amps_total_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps_total_min.setStatus("mandatory")
_NetBotz_prd_bot_amps_total_max_Type = Integer32
_NetBotz_prd_bot_amps_total_max_Object = MibScalar
netBotz_prd_bot_amps_total_max = _NetBotz_prd_bot_amps_total_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 47),
    _NetBotz_prd_bot_amps_total_max_Type()
)
netBotz_prd_bot_amps_total_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps_total_max.setStatus("mandatory")
_NetBotz_prd_bot_amps_total_support_enabled_Type = DisplayString
_NetBotz_prd_bot_amps_total_support_enabled_Object = MibScalar
netBotz_prd_bot_amps_total_support_enabled = _NetBotz_prd_bot_amps_total_support_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 48),
    _NetBotz_prd_bot_amps_total_support_enabled_Type()
)
netBotz_prd_bot_amps_total_support_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps_total_support_enabled.setStatus("mandatory")
_NetBotz_prd_bot_amps1_uV_per_10mA_Type = Integer32
_NetBotz_prd_bot_amps1_uV_per_10mA_Object = MibScalar
netBotz_prd_bot_amps1_uV_per_10mA = _NetBotz_prd_bot_amps1_uV_per_10mA_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 49),
    _NetBotz_prd_bot_amps1_uV_per_10mA_Type()
)
netBotz_prd_bot_amps1_uV_per_10mA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps1_uV_per_10mA.setStatus("mandatory")
_NetBotz_prd_bot_amps2_uV_per_10mA_Type = Integer32
_NetBotz_prd_bot_amps2_uV_per_10mA_Object = MibScalar
netBotz_prd_bot_amps2_uV_per_10mA = _NetBotz_prd_bot_amps2_uV_per_10mA_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 50),
    _NetBotz_prd_bot_amps2_uV_per_10mA_Type()
)
netBotz_prd_bot_amps2_uV_per_10mA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps2_uV_per_10mA.setStatus("mandatory")
_NetBotz_prd_bot_amps3_uV_per_mA_Type = Integer32
_NetBotz_prd_bot_amps3_uV_per_mA_Object = MibScalar
netBotz_prd_bot_amps3_uV_per_mA = _NetBotz_prd_bot_amps3_uV_per_mA_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 51),
    _NetBotz_prd_bot_amps3_uV_per_mA_Type()
)
netBotz_prd_bot_amps3_uV_per_mA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps3_uV_per_mA.setStatus("mandatory")
_NetBotz_prd_bot_amps1_max_range_Type = Integer32
_NetBotz_prd_bot_amps1_max_range_Object = MibScalar
netBotz_prd_bot_amps1_max_range = _NetBotz_prd_bot_amps1_max_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 52),
    _NetBotz_prd_bot_amps1_max_range_Type()
)
netBotz_prd_bot_amps1_max_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps1_max_range.setStatus("mandatory")
_NetBotz_prd_bot_amps2_max_range_Type = Integer32
_NetBotz_prd_bot_amps2_max_range_Object = MibScalar
netBotz_prd_bot_amps2_max_range = _NetBotz_prd_bot_amps2_max_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 53),
    _NetBotz_prd_bot_amps2_max_range_Type()
)
netBotz_prd_bot_amps2_max_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps2_max_range.setStatus("mandatory")
_NetBotz_prd_bot_amps3_max_range_Type = Integer32
_NetBotz_prd_bot_amps3_max_range_Object = MibScalar
netBotz_prd_bot_amps3_max_range = _NetBotz_prd_bot_amps3_max_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 54),
    _NetBotz_prd_bot_amps3_max_range_Type()
)
netBotz_prd_bot_amps3_max_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps3_max_range.setStatus("mandatory")
_NetBotz_prd_bot_amps4_Type = Integer32
_NetBotz_prd_bot_amps4_Object = MibScalar
netBotz_prd_bot_amps4 = _NetBotz_prd_bot_amps4_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 55),
    _NetBotz_prd_bot_amps4_Type()
)
netBotz_prd_bot_amps4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps4.setStatus("mandatory")
_NetBotz_prd_bot_amps4_enabled_Type = Integer32
_NetBotz_prd_bot_amps4_enabled_Object = MibScalar
netBotz_prd_bot_amps4_enabled = _NetBotz_prd_bot_amps4_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 56),
    _NetBotz_prd_bot_amps4_enabled_Type()
)
netBotz_prd_bot_amps4_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps4_enabled.setStatus("mandatory")
_NetBotz_prd_bot_amps4_min_Type = Integer32
_NetBotz_prd_bot_amps4_min_Object = MibScalar
netBotz_prd_bot_amps4_min = _NetBotz_prd_bot_amps4_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 57),
    _NetBotz_prd_bot_amps4_min_Type()
)
netBotz_prd_bot_amps4_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps4_min.setStatus("mandatory")
_NetBotz_prd_bot_amps4_max_Type = Integer32
_NetBotz_prd_bot_amps4_max_Object = MibScalar
netBotz_prd_bot_amps4_max = _NetBotz_prd_bot_amps4_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 58),
    _NetBotz_prd_bot_amps4_max_Type()
)
netBotz_prd_bot_amps4_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps4_max.setStatus("mandatory")
_NetBotz_prd_bot_amps4_uV_per_10mA_Type = Integer32
_NetBotz_prd_bot_amps4_uV_per_10mA_Object = MibScalar
netBotz_prd_bot_amps4_uV_per_10mA = _NetBotz_prd_bot_amps4_uV_per_10mA_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 60),
    _NetBotz_prd_bot_amps4_uV_per_10mA_Type()
)
netBotz_prd_bot_amps4_uV_per_10mA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps4_uV_per_10mA.setStatus("mandatory")
_NetBotz_prd_bot_amps4_max_range_Type = Integer32
_NetBotz_prd_bot_amps4_max_range_Object = MibScalar
netBotz_prd_bot_amps4_max_range = _NetBotz_prd_bot_amps4_max_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 61),
    _NetBotz_prd_bot_amps4_max_range_Type()
)
netBotz_prd_bot_amps4_max_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amps4_max_range.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp1_Type = Integer32
_NetBotz_prd_bot_ext_temp1_Object = MibScalar
netBotz_prd_bot_ext_temp1 = _NetBotz_prd_bot_ext_temp1_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 62),
    _NetBotz_prd_bot_ext_temp1_Type()
)
netBotz_prd_bot_ext_temp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp2_Type = Integer32
_NetBotz_prd_bot_ext_temp2_Object = MibScalar
netBotz_prd_bot_ext_temp2 = _NetBotz_prd_bot_ext_temp2_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 63),
    _NetBotz_prd_bot_ext_temp2_Type()
)
netBotz_prd_bot_ext_temp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp3_Type = Integer32
_NetBotz_prd_bot_ext_temp3_Object = MibScalar
netBotz_prd_bot_ext_temp3 = _NetBotz_prd_bot_ext_temp3_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 64),
    _NetBotz_prd_bot_ext_temp3_Type()
)
netBotz_prd_bot_ext_temp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp1_enabled_Type = Integer32
_NetBotz_prd_bot_ext_temp1_enabled_Object = MibScalar
netBotz_prd_bot_ext_temp1_enabled = _NetBotz_prd_bot_ext_temp1_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 66),
    _NetBotz_prd_bot_ext_temp1_enabled_Type()
)
netBotz_prd_bot_ext_temp1_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_enabled.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp1_min_Type = Integer32
_NetBotz_prd_bot_ext_temp1_min_Object = MibScalar
netBotz_prd_bot_ext_temp1_min = _NetBotz_prd_bot_ext_temp1_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 67),
    _NetBotz_prd_bot_ext_temp1_min_Type()
)
netBotz_prd_bot_ext_temp1_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_min.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp1_max_Type = Integer32
_NetBotz_prd_bot_ext_temp1_max_Object = MibScalar
netBotz_prd_bot_ext_temp1_max = _NetBotz_prd_bot_ext_temp1_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 68),
    _NetBotz_prd_bot_ext_temp1_max_Type()
)
netBotz_prd_bot_ext_temp1_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_max.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp2_enabled_Type = Integer32
_NetBotz_prd_bot_ext_temp2_enabled_Object = MibScalar
netBotz_prd_bot_ext_temp2_enabled = _NetBotz_prd_bot_ext_temp2_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 69),
    _NetBotz_prd_bot_ext_temp2_enabled_Type()
)
netBotz_prd_bot_ext_temp2_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_enabled.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp2_min_Type = Integer32
_NetBotz_prd_bot_ext_temp2_min_Object = MibScalar
netBotz_prd_bot_ext_temp2_min = _NetBotz_prd_bot_ext_temp2_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 70),
    _NetBotz_prd_bot_ext_temp2_min_Type()
)
netBotz_prd_bot_ext_temp2_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_min.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp2_max_Type = Integer32
_NetBotz_prd_bot_ext_temp2_max_Object = MibScalar
netBotz_prd_bot_ext_temp2_max = _NetBotz_prd_bot_ext_temp2_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 71),
    _NetBotz_prd_bot_ext_temp2_max_Type()
)
netBotz_prd_bot_ext_temp2_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_max.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp3_enabled_Type = Integer32
_NetBotz_prd_bot_ext_temp3_enabled_Object = MibScalar
netBotz_prd_bot_ext_temp3_enabled = _NetBotz_prd_bot_ext_temp3_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 72),
    _NetBotz_prd_bot_ext_temp3_enabled_Type()
)
netBotz_prd_bot_ext_temp3_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_enabled.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp3_min_Type = Integer32
_NetBotz_prd_bot_ext_temp3_min_Object = MibScalar
netBotz_prd_bot_ext_temp3_min = _NetBotz_prd_bot_ext_temp3_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 73),
    _NetBotz_prd_bot_ext_temp3_min_Type()
)
netBotz_prd_bot_ext_temp3_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_min.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp3_max_Type = Integer32
_NetBotz_prd_bot_ext_temp3_max_Object = MibScalar
netBotz_prd_bot_ext_temp3_max = _NetBotz_prd_bot_ext_temp3_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 74),
    _NetBotz_prd_bot_ext_temp3_max_Type()
)
netBotz_prd_bot_ext_temp3_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_max.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp1_uV_per_degreeC_Type = Integer32
_NetBotz_prd_bot_ext_temp1_uV_per_degreeC_Object = MibScalar
netBotz_prd_bot_ext_temp1_uV_per_degreeC = _NetBotz_prd_bot_ext_temp1_uV_per_degreeC_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 78),
    _NetBotz_prd_bot_ext_temp1_uV_per_degreeC_Type()
)
netBotz_prd_bot_ext_temp1_uV_per_degreeC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_uV_per_degreeC.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp1_uV_at_0_degreeC_Type = Integer32
_NetBotz_prd_bot_ext_temp1_uV_at_0_degreeC_Object = MibScalar
netBotz_prd_bot_ext_temp1_uV_at_0_degreeC = _NetBotz_prd_bot_ext_temp1_uV_at_0_degreeC_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 79),
    _NetBotz_prd_bot_ext_temp1_uV_at_0_degreeC_Type()
)
netBotz_prd_bot_ext_temp1_uV_at_0_degreeC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_uV_at_0_degreeC.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp1_min_range_Type = Integer32
_NetBotz_prd_bot_ext_temp1_min_range_Object = MibScalar
netBotz_prd_bot_ext_temp1_min_range = _NetBotz_prd_bot_ext_temp1_min_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 80),
    _NetBotz_prd_bot_ext_temp1_min_range_Type()
)
netBotz_prd_bot_ext_temp1_min_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_min_range.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp1_max_range_Type = Integer32
_NetBotz_prd_bot_ext_temp1_max_range_Object = MibScalar
netBotz_prd_bot_ext_temp1_max_range = _NetBotz_prd_bot_ext_temp1_max_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 81),
    _NetBotz_prd_bot_ext_temp1_max_range_Type()
)
netBotz_prd_bot_ext_temp1_max_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_max_range.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp2_uV_per_degreeC_Type = Integer32
_NetBotz_prd_bot_ext_temp2_uV_per_degreeC_Object = MibScalar
netBotz_prd_bot_ext_temp2_uV_per_degreeC = _NetBotz_prd_bot_ext_temp2_uV_per_degreeC_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 82),
    _NetBotz_prd_bot_ext_temp2_uV_per_degreeC_Type()
)
netBotz_prd_bot_ext_temp2_uV_per_degreeC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_uV_per_degreeC.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp2_uV_at_0_degreeC_Type = Integer32
_NetBotz_prd_bot_ext_temp2_uV_at_0_degreeC_Object = MibScalar
netBotz_prd_bot_ext_temp2_uV_at_0_degreeC = _NetBotz_prd_bot_ext_temp2_uV_at_0_degreeC_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 83),
    _NetBotz_prd_bot_ext_temp2_uV_at_0_degreeC_Type()
)
netBotz_prd_bot_ext_temp2_uV_at_0_degreeC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_uV_at_0_degreeC.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp2_min_range_Type = Integer32
_NetBotz_prd_bot_ext_temp2_min_range_Object = MibScalar
netBotz_prd_bot_ext_temp2_min_range = _NetBotz_prd_bot_ext_temp2_min_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 84),
    _NetBotz_prd_bot_ext_temp2_min_range_Type()
)
netBotz_prd_bot_ext_temp2_min_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_min_range.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp2_max_range_Type = Integer32
_NetBotz_prd_bot_ext_temp2_max_range_Object = MibScalar
netBotz_prd_bot_ext_temp2_max_range = _NetBotz_prd_bot_ext_temp2_max_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 85),
    _NetBotz_prd_bot_ext_temp2_max_range_Type()
)
netBotz_prd_bot_ext_temp2_max_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_max_range.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp3_uV_per_degreeC_Type = Integer32
_NetBotz_prd_bot_ext_temp3_uV_per_degreeC_Object = MibScalar
netBotz_prd_bot_ext_temp3_uV_per_degreeC = _NetBotz_prd_bot_ext_temp3_uV_per_degreeC_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 86),
    _NetBotz_prd_bot_ext_temp3_uV_per_degreeC_Type()
)
netBotz_prd_bot_ext_temp3_uV_per_degreeC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_uV_per_degreeC.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp3_uV_at_0_degreeC_Type = Integer32
_NetBotz_prd_bot_ext_temp3_uV_at_0_degreeC_Object = MibScalar
netBotz_prd_bot_ext_temp3_uV_at_0_degreeC = _NetBotz_prd_bot_ext_temp3_uV_at_0_degreeC_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 87),
    _NetBotz_prd_bot_ext_temp3_uV_at_0_degreeC_Type()
)
netBotz_prd_bot_ext_temp3_uV_at_0_degreeC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_uV_at_0_degreeC.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp3_min_range_Type = Integer32
_NetBotz_prd_bot_ext_temp3_min_range_Object = MibScalar
netBotz_prd_bot_ext_temp3_min_range = _NetBotz_prd_bot_ext_temp3_min_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 88),
    _NetBotz_prd_bot_ext_temp3_min_range_Type()
)
netBotz_prd_bot_ext_temp3_min_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_min_range.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp3_max_range_Type = Integer32
_NetBotz_prd_bot_ext_temp3_max_range_Object = MibScalar
netBotz_prd_bot_ext_temp3_max_range = _NetBotz_prd_bot_ext_temp3_max_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 89),
    _NetBotz_prd_bot_ext_temp3_max_range_Type()
)
netBotz_prd_bot_ext_temp3_max_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_max_range.setStatus("mandatory")
_NetBotz_prd_bot_ext_port1_module_id_Type = DisplayString
_NetBotz_prd_bot_ext_port1_module_id_Object = MibScalar
netBotz_prd_bot_ext_port1_module_id = _NetBotz_prd_bot_ext_port1_module_id_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 94),
    _NetBotz_prd_bot_ext_port1_module_id_Type()
)
netBotz_prd_bot_ext_port1_module_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_port1_module_id.setStatus("mandatory")
_NetBotz_prd_bot_ext_port1_module_type_Type = DisplayString
_NetBotz_prd_bot_ext_port1_module_type_Object = MibScalar
netBotz_prd_bot_ext_port1_module_type = _NetBotz_prd_bot_ext_port1_module_type_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 95),
    _NetBotz_prd_bot_ext_port1_module_type_Type()
)
netBotz_prd_bot_ext_port1_module_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_port1_module_type.setStatus("mandatory")
_NetBotz_prd_bot_ext_port2_module_id_Type = DisplayString
_NetBotz_prd_bot_ext_port2_module_id_Object = MibScalar
netBotz_prd_bot_ext_port2_module_id = _NetBotz_prd_bot_ext_port2_module_id_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 96),
    _NetBotz_prd_bot_ext_port2_module_id_Type()
)
netBotz_prd_bot_ext_port2_module_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_port2_module_id.setStatus("mandatory")
_NetBotz_prd_bot_ext_port2_module_type_Type = DisplayString
_NetBotz_prd_bot_ext_port2_module_type_Object = MibScalar
netBotz_prd_bot_ext_port2_module_type = _NetBotz_prd_bot_ext_port2_module_type_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 97),
    _NetBotz_prd_bot_ext_port2_module_type_Type()
)
netBotz_prd_bot_ext_port2_module_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_port2_module_type.setStatus("mandatory")
_NetBotz_prd_bot_ext_port3_module_id_Type = DisplayString
_NetBotz_prd_bot_ext_port3_module_id_Object = MibScalar
netBotz_prd_bot_ext_port3_module_id = _NetBotz_prd_bot_ext_port3_module_id_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 98),
    _NetBotz_prd_bot_ext_port3_module_id_Type()
)
netBotz_prd_bot_ext_port3_module_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_port3_module_id.setStatus("mandatory")
_NetBotz_prd_bot_ext_port3_module_type_Type = DisplayString
_NetBotz_prd_bot_ext_port3_module_type_Object = MibScalar
netBotz_prd_bot_ext_port3_module_type = _NetBotz_prd_bot_ext_port3_module_type_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 99),
    _NetBotz_prd_bot_ext_port3_module_type_Type()
)
netBotz_prd_bot_ext_port3_module_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_port3_module_type.setStatus("mandatory")
_NetBotz_prd_bot_amp1_total_amp_seconds_Type = Integer32
_NetBotz_prd_bot_amp1_total_amp_seconds_Object = MibScalar
netBotz_prd_bot_amp1_total_amp_seconds = _NetBotz_prd_bot_amp1_total_amp_seconds_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 102),
    _NetBotz_prd_bot_amp1_total_amp_seconds_Type()
)
netBotz_prd_bot_amp1_total_amp_seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp1_total_amp_seconds.setStatus("mandatory")
_NetBotz_prd_bot_amp1_total_amp_seconds_since_time_Type = Integer32
_NetBotz_prd_bot_amp1_total_amp_seconds_since_time_Object = MibScalar
netBotz_prd_bot_amp1_total_amp_seconds_since_time = _NetBotz_prd_bot_amp1_total_amp_seconds_since_time_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 103),
    _NetBotz_prd_bot_amp1_total_amp_seconds_since_time_Type()
)
netBotz_prd_bot_amp1_total_amp_seconds_since_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp1_total_amp_seconds_since_time.setStatus("mandatory")
_NetBotz_prd_bot_amp2_total_amp_seconds_Type = Integer32
_NetBotz_prd_bot_amp2_total_amp_seconds_Object = MibScalar
netBotz_prd_bot_amp2_total_amp_seconds = _NetBotz_prd_bot_amp2_total_amp_seconds_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 104),
    _NetBotz_prd_bot_amp2_total_amp_seconds_Type()
)
netBotz_prd_bot_amp2_total_amp_seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp2_total_amp_seconds.setStatus("mandatory")
_NetBotz_prd_bot_amp2_total_amp_seconds_since_time_Type = Integer32
_NetBotz_prd_bot_amp2_total_amp_seconds_since_time_Object = MibScalar
netBotz_prd_bot_amp2_total_amp_seconds_since_time = _NetBotz_prd_bot_amp2_total_amp_seconds_since_time_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 105),
    _NetBotz_prd_bot_amp2_total_amp_seconds_since_time_Type()
)
netBotz_prd_bot_amp2_total_amp_seconds_since_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp2_total_amp_seconds_since_time.setStatus("mandatory")
_NetBotz_prd_bot_amp3_total_amp_seconds_Type = Integer32
_NetBotz_prd_bot_amp3_total_amp_seconds_Object = MibScalar
netBotz_prd_bot_amp3_total_amp_seconds = _NetBotz_prd_bot_amp3_total_amp_seconds_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 106),
    _NetBotz_prd_bot_amp3_total_amp_seconds_Type()
)
netBotz_prd_bot_amp3_total_amp_seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp3_total_amp_seconds.setStatus("mandatory")
_NetBotz_prd_bot_amp3_total_amp_seconds_since_time_Type = Integer32
_NetBotz_prd_bot_amp3_total_amp_seconds_since_time_Object = MibScalar
netBotz_prd_bot_amp3_total_amp_seconds_since_time = _NetBotz_prd_bot_amp3_total_amp_seconds_since_time_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 107),
    _NetBotz_prd_bot_amp3_total_amp_seconds_since_time_Type()
)
netBotz_prd_bot_amp3_total_amp_seconds_since_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp3_total_amp_seconds_since_time.setStatus("mandatory")
_NetBotz_prd_bot_amp4_total_amp_seconds_Type = Integer32
_NetBotz_prd_bot_amp4_total_amp_seconds_Object = MibScalar
netBotz_prd_bot_amp4_total_amp_seconds = _NetBotz_prd_bot_amp4_total_amp_seconds_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 108),
    _NetBotz_prd_bot_amp4_total_amp_seconds_Type()
)
netBotz_prd_bot_amp4_total_amp_seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp4_total_amp_seconds.setStatus("mandatory")
_NetBotz_prd_bot_amp4_total_amp_seconds_since_time_Type = Integer32
_NetBotz_prd_bot_amp4_total_amp_seconds_since_time_Object = MibScalar
netBotz_prd_bot_amp4_total_amp_seconds_since_time = _NetBotz_prd_bot_amp4_total_amp_seconds_since_time_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 109),
    _NetBotz_prd_bot_amp4_total_amp_seconds_since_time_Type()
)
netBotz_prd_bot_amp4_total_amp_seconds_since_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp4_total_amp_seconds_since_time.setStatus("mandatory")
_NetBotz_prd_bot_amptotal_total_amp_seconds_Type = Integer32
_NetBotz_prd_bot_amptotal_total_amp_seconds_Object = MibScalar
netBotz_prd_bot_amptotal_total_amp_seconds = _NetBotz_prd_bot_amptotal_total_amp_seconds_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 110),
    _NetBotz_prd_bot_amptotal_total_amp_seconds_Type()
)
netBotz_prd_bot_amptotal_total_amp_seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amptotal_total_amp_seconds.setStatus("mandatory")
_NetBotz_prd_bot_amptotal_total_amp_seconds_since_time_Type = Integer32
_NetBotz_prd_bot_amptotal_total_amp_seconds_since_time_Object = MibScalar
netBotz_prd_bot_amptotal_total_amp_seconds_since_time = _NetBotz_prd_bot_amptotal_total_amp_seconds_since_time_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 111),
    _NetBotz_prd_bot_amptotal_total_amp_seconds_since_time_Type()
)
netBotz_prd_bot_amptotal_total_amp_seconds_since_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_amptotal_total_amp_seconds_since_time.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry1_Type = Integer32
_NetBotz_prd_bot_ext_dry1_Object = MibScalar
netBotz_prd_bot_ext_dry1 = _NetBotz_prd_bot_ext_dry1_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 112),
    _NetBotz_prd_bot_ext_dry1_Type()
)
netBotz_prd_bot_ext_dry1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry1.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry2_Type = Integer32
_NetBotz_prd_bot_ext_dry2_Object = MibScalar
netBotz_prd_bot_ext_dry2 = _NetBotz_prd_bot_ext_dry2_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 113),
    _NetBotz_prd_bot_ext_dry2_Type()
)
netBotz_prd_bot_ext_dry2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry2.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry3_Type = Integer32
_NetBotz_prd_bot_ext_dry3_Object = MibScalar
netBotz_prd_bot_ext_dry3 = _NetBotz_prd_bot_ext_dry3_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 114),
    _NetBotz_prd_bot_ext_dry3_Type()
)
netBotz_prd_bot_ext_dry3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry3.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry4_Type = Integer32
_NetBotz_prd_bot_ext_dry4_Object = MibScalar
netBotz_prd_bot_ext_dry4 = _NetBotz_prd_bot_ext_dry4_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 115),
    _NetBotz_prd_bot_ext_dry4_Type()
)
netBotz_prd_bot_ext_dry4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry4.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry1_alarm_value_Type = Integer32
_NetBotz_prd_bot_ext_dry1_alarm_value_Object = MibScalar
netBotz_prd_bot_ext_dry1_alarm_value = _NetBotz_prd_bot_ext_dry1_alarm_value_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 116),
    _NetBotz_prd_bot_ext_dry1_alarm_value_Type()
)
netBotz_prd_bot_ext_dry1_alarm_value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry1_alarm_value.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry1_enabled_Type = Integer32
_NetBotz_prd_bot_ext_dry1_enabled_Object = MibScalar
netBotz_prd_bot_ext_dry1_enabled = _NetBotz_prd_bot_ext_dry1_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 117),
    _NetBotz_prd_bot_ext_dry1_enabled_Type()
)
netBotz_prd_bot_ext_dry1_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry1_enabled.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry2_alarm_value_Type = Integer32
_NetBotz_prd_bot_ext_dry2_alarm_value_Object = MibScalar
netBotz_prd_bot_ext_dry2_alarm_value = _NetBotz_prd_bot_ext_dry2_alarm_value_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 118),
    _NetBotz_prd_bot_ext_dry2_alarm_value_Type()
)
netBotz_prd_bot_ext_dry2_alarm_value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry2_alarm_value.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry2_enabled_Type = Integer32
_NetBotz_prd_bot_ext_dry2_enabled_Object = MibScalar
netBotz_prd_bot_ext_dry2_enabled = _NetBotz_prd_bot_ext_dry2_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 119),
    _NetBotz_prd_bot_ext_dry2_enabled_Type()
)
netBotz_prd_bot_ext_dry2_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry2_enabled.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry3_alarm_value_Type = Integer32
_NetBotz_prd_bot_ext_dry3_alarm_value_Object = MibScalar
netBotz_prd_bot_ext_dry3_alarm_value = _NetBotz_prd_bot_ext_dry3_alarm_value_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 120),
    _NetBotz_prd_bot_ext_dry3_alarm_value_Type()
)
netBotz_prd_bot_ext_dry3_alarm_value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry3_alarm_value.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry3_enabled_Type = Integer32
_NetBotz_prd_bot_ext_dry3_enabled_Object = MibScalar
netBotz_prd_bot_ext_dry3_enabled = _NetBotz_prd_bot_ext_dry3_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 121),
    _NetBotz_prd_bot_ext_dry3_enabled_Type()
)
netBotz_prd_bot_ext_dry3_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry3_enabled.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry4_alarm_value_Type = Integer32
_NetBotz_prd_bot_ext_dry4_alarm_value_Object = MibScalar
netBotz_prd_bot_ext_dry4_alarm_value = _NetBotz_prd_bot_ext_dry4_alarm_value_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 122),
    _NetBotz_prd_bot_ext_dry4_alarm_value_Type()
)
netBotz_prd_bot_ext_dry4_alarm_value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry4_alarm_value.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry4_enabled_Type = Integer32
_NetBotz_prd_bot_ext_dry4_enabled_Object = MibScalar
netBotz_prd_bot_ext_dry4_enabled = _NetBotz_prd_bot_ext_dry4_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 123),
    _NetBotz_prd_bot_ext_dry4_enabled_Type()
)
netBotz_prd_bot_ext_dry4_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry4_enabled.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry1_label_Type = DisplayString
_NetBotz_prd_bot_ext_dry1_label_Object = MibScalar
netBotz_prd_bot_ext_dry1_label = _NetBotz_prd_bot_ext_dry1_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 124),
    _NetBotz_prd_bot_ext_dry1_label_Type()
)
netBotz_prd_bot_ext_dry1_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry1_label.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry1_open_label_Type = DisplayString
_NetBotz_prd_bot_ext_dry1_open_label_Object = MibScalar
netBotz_prd_bot_ext_dry1_open_label = _NetBotz_prd_bot_ext_dry1_open_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 125),
    _NetBotz_prd_bot_ext_dry1_open_label_Type()
)
netBotz_prd_bot_ext_dry1_open_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry1_open_label.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry1_closed_label_Type = DisplayString
_NetBotz_prd_bot_ext_dry1_closed_label_Object = MibScalar
netBotz_prd_bot_ext_dry1_closed_label = _NetBotz_prd_bot_ext_dry1_closed_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 126),
    _NetBotz_prd_bot_ext_dry1_closed_label_Type()
)
netBotz_prd_bot_ext_dry1_closed_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry1_closed_label.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry1_open_to_close_millis_Type = Integer32
_NetBotz_prd_bot_ext_dry1_open_to_close_millis_Object = MibScalar
netBotz_prd_bot_ext_dry1_open_to_close_millis = _NetBotz_prd_bot_ext_dry1_open_to_close_millis_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 127),
    _NetBotz_prd_bot_ext_dry1_open_to_close_millis_Type()
)
netBotz_prd_bot_ext_dry1_open_to_close_millis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry1_open_to_close_millis.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry1_close_to_open_millis_Type = Integer32
_NetBotz_prd_bot_ext_dry1_close_to_open_millis_Object = MibScalar
netBotz_prd_bot_ext_dry1_close_to_open_millis = _NetBotz_prd_bot_ext_dry1_close_to_open_millis_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 128),
    _NetBotz_prd_bot_ext_dry1_close_to_open_millis_Type()
)
netBotz_prd_bot_ext_dry1_close_to_open_millis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry1_close_to_open_millis.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry1_response_Type = DisplayString
_NetBotz_prd_bot_ext_dry1_response_Object = MibScalar
netBotz_prd_bot_ext_dry1_response = _NetBotz_prd_bot_ext_dry1_response_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 129),
    _NetBotz_prd_bot_ext_dry1_response_Type()
)
netBotz_prd_bot_ext_dry1_response.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry1_response.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry2_label_Type = DisplayString
_NetBotz_prd_bot_ext_dry2_label_Object = MibScalar
netBotz_prd_bot_ext_dry2_label = _NetBotz_prd_bot_ext_dry2_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 130),
    _NetBotz_prd_bot_ext_dry2_label_Type()
)
netBotz_prd_bot_ext_dry2_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry2_label.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry2_open_label_Type = DisplayString
_NetBotz_prd_bot_ext_dry2_open_label_Object = MibScalar
netBotz_prd_bot_ext_dry2_open_label = _NetBotz_prd_bot_ext_dry2_open_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 131),
    _NetBotz_prd_bot_ext_dry2_open_label_Type()
)
netBotz_prd_bot_ext_dry2_open_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry2_open_label.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry2_closed_label_Type = DisplayString
_NetBotz_prd_bot_ext_dry2_closed_label_Object = MibScalar
netBotz_prd_bot_ext_dry2_closed_label = _NetBotz_prd_bot_ext_dry2_closed_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 132),
    _NetBotz_prd_bot_ext_dry2_closed_label_Type()
)
netBotz_prd_bot_ext_dry2_closed_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry2_closed_label.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry2_open_to_close_millis_Type = Integer32
_NetBotz_prd_bot_ext_dry2_open_to_close_millis_Object = MibScalar
netBotz_prd_bot_ext_dry2_open_to_close_millis = _NetBotz_prd_bot_ext_dry2_open_to_close_millis_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 133),
    _NetBotz_prd_bot_ext_dry2_open_to_close_millis_Type()
)
netBotz_prd_bot_ext_dry2_open_to_close_millis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry2_open_to_close_millis.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry2_close_to_open_millis_Type = Integer32
_NetBotz_prd_bot_ext_dry2_close_to_open_millis_Object = MibScalar
netBotz_prd_bot_ext_dry2_close_to_open_millis = _NetBotz_prd_bot_ext_dry2_close_to_open_millis_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 134),
    _NetBotz_prd_bot_ext_dry2_close_to_open_millis_Type()
)
netBotz_prd_bot_ext_dry2_close_to_open_millis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry2_close_to_open_millis.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry2_response_Type = DisplayString
_NetBotz_prd_bot_ext_dry2_response_Object = MibScalar
netBotz_prd_bot_ext_dry2_response = _NetBotz_prd_bot_ext_dry2_response_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 135),
    _NetBotz_prd_bot_ext_dry2_response_Type()
)
netBotz_prd_bot_ext_dry2_response.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry2_response.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry3_label_Type = DisplayString
_NetBotz_prd_bot_ext_dry3_label_Object = MibScalar
netBotz_prd_bot_ext_dry3_label = _NetBotz_prd_bot_ext_dry3_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 136),
    _NetBotz_prd_bot_ext_dry3_label_Type()
)
netBotz_prd_bot_ext_dry3_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry3_label.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry3_open_label_Type = DisplayString
_NetBotz_prd_bot_ext_dry3_open_label_Object = MibScalar
netBotz_prd_bot_ext_dry3_open_label = _NetBotz_prd_bot_ext_dry3_open_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 137),
    _NetBotz_prd_bot_ext_dry3_open_label_Type()
)
netBotz_prd_bot_ext_dry3_open_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry3_open_label.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry3_closed_label_Type = DisplayString
_NetBotz_prd_bot_ext_dry3_closed_label_Object = MibScalar
netBotz_prd_bot_ext_dry3_closed_label = _NetBotz_prd_bot_ext_dry3_closed_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 138),
    _NetBotz_prd_bot_ext_dry3_closed_label_Type()
)
netBotz_prd_bot_ext_dry3_closed_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry3_closed_label.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry3_open_to_close_millis_Type = Integer32
_NetBotz_prd_bot_ext_dry3_open_to_close_millis_Object = MibScalar
netBotz_prd_bot_ext_dry3_open_to_close_millis = _NetBotz_prd_bot_ext_dry3_open_to_close_millis_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 139),
    _NetBotz_prd_bot_ext_dry3_open_to_close_millis_Type()
)
netBotz_prd_bot_ext_dry3_open_to_close_millis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry3_open_to_close_millis.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry3_close_to_open_millis_Type = Integer32
_NetBotz_prd_bot_ext_dry3_close_to_open_millis_Object = MibScalar
netBotz_prd_bot_ext_dry3_close_to_open_millis = _NetBotz_prd_bot_ext_dry3_close_to_open_millis_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 140),
    _NetBotz_prd_bot_ext_dry3_close_to_open_millis_Type()
)
netBotz_prd_bot_ext_dry3_close_to_open_millis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry3_close_to_open_millis.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry3_response_Type = DisplayString
_NetBotz_prd_bot_ext_dry3_response_Object = MibScalar
netBotz_prd_bot_ext_dry3_response = _NetBotz_prd_bot_ext_dry3_response_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 141),
    _NetBotz_prd_bot_ext_dry3_response_Type()
)
netBotz_prd_bot_ext_dry3_response.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry3_response.setStatus("mandatory")
_NetBotz_prd_bot_cam_motion_Type = Integer32
_NetBotz_prd_bot_cam_motion_Object = MibScalar
netBotz_prd_bot_cam_motion = _NetBotz_prd_bot_cam_motion_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 148),
    _NetBotz_prd_bot_cam_motion_Type()
)
netBotz_prd_bot_cam_motion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_cam_motion.setStatus("mandatory")
_NetBotz_prd_bot_cam_motion_enabled_Type = Integer32
_NetBotz_prd_bot_cam_motion_enabled_Object = MibScalar
netBotz_prd_bot_cam_motion_enabled = _NetBotz_prd_bot_cam_motion_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 149),
    _NetBotz_prd_bot_cam_motion_enabled_Type()
)
netBotz_prd_bot_cam_motion_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_cam_motion_enabled.setStatus("mandatory")
_NetBotz_prd_bot_cam_motion_sensitivity_Type = Integer32
_NetBotz_prd_bot_cam_motion_sensitivity_Object = MibScalar
netBotz_prd_bot_cam_motion_sensitivity = _NetBotz_prd_bot_cam_motion_sensitivity_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 150),
    _NetBotz_prd_bot_cam_motion_sensitivity_Type()
)
netBotz_prd_bot_cam_motion_sensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_cam_motion_sensitivity.setStatus("mandatory")
_NetBotz_prd_bot_cam_motion_delay_Type = Integer32
_NetBotz_prd_bot_cam_motion_delay_Object = MibScalar
netBotz_prd_bot_cam_motion_delay = _NetBotz_prd_bot_cam_motion_delay_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 151),
    _NetBotz_prd_bot_cam_motion_delay_Type()
)
netBotz_prd_bot_cam_motion_delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_cam_motion_delay.setStatus("mandatory")
_NetBotz_prd_bot_camera_event_autocycle_Type = Integer32
_NetBotz_prd_bot_camera_event_autocycle_Object = MibScalar
netBotz_prd_bot_camera_event_autocycle = _NetBotz_prd_bot_camera_event_autocycle_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 152),
    _NetBotz_prd_bot_camera_event_autocycle_Type()
)
netBotz_prd_bot_camera_event_autocycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_camera_event_autocycle.setStatus("mandatory")
_NetBotz_prd_bot_num_pix_before_alarm_Type = Integer32
_NetBotz_prd_bot_num_pix_before_alarm_Object = MibScalar
netBotz_prd_bot_num_pix_before_alarm = _NetBotz_prd_bot_num_pix_before_alarm_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 153),
    _NetBotz_prd_bot_num_pix_before_alarm_Type()
)
netBotz_prd_bot_num_pix_before_alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_num_pix_before_alarm.setStatus("mandatory")
_NetBotz_prd_bot_delay_before_event_pix_Type = Integer32
_NetBotz_prd_bot_delay_before_event_pix_Object = MibScalar
netBotz_prd_bot_delay_before_event_pix = _NetBotz_prd_bot_delay_before_event_pix_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 154),
    _NetBotz_prd_bot_delay_before_event_pix_Type()
)
netBotz_prd_bot_delay_before_event_pix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_delay_before_event_pix.setStatus("mandatory")
_NetBotz_prd_bot_delay_between_event_pix_Type = Integer32
_NetBotz_prd_bot_delay_between_event_pix_Object = MibScalar
netBotz_prd_bot_delay_between_event_pix = _NetBotz_prd_bot_delay_between_event_pix_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 155),
    _NetBotz_prd_bot_delay_between_event_pix_Type()
)
netBotz_prd_bot_delay_between_event_pix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_delay_between_event_pix.setStatus("mandatory")
_NetBotz_prd_bot_cam_motion_area_of_motion_Type = Integer32
_NetBotz_prd_bot_cam_motion_area_of_motion_Object = MibScalar
netBotz_prd_bot_cam_motion_area_of_motion = _NetBotz_prd_bot_cam_motion_area_of_motion_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 156),
    _NetBotz_prd_bot_cam_motion_area_of_motion_Type()
)
netBotz_prd_bot_cam_motion_area_of_motion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_cam_motion_area_of_motion.setStatus("mandatory")
_NetBotz_prd_bot_cam_pix_for_duration_of_alerts_Type = Integer32
_NetBotz_prd_bot_cam_pix_for_duration_of_alerts_Object = MibScalar
netBotz_prd_bot_cam_pix_for_duration_of_alerts = _NetBotz_prd_bot_cam_pix_for_duration_of_alerts_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 157),
    _NetBotz_prd_bot_cam_pix_for_duration_of_alerts_Type()
)
netBotz_prd_bot_cam_pix_for_duration_of_alerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_cam_pix_for_duration_of_alerts.setStatus("mandatory")
_NetBotz_prd_bot_camera_enabled_Type = Integer32
_NetBotz_prd_bot_camera_enabled_Object = MibScalar
netBotz_prd_bot_camera_enabled = _NetBotz_prd_bot_camera_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 158),
    _NetBotz_prd_bot_camera_enabled_Type()
)
netBotz_prd_bot_camera_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_camera_enabled.setStatus("mandatory")
_NetBotz_prd_bot_camera_is_flipped_Type = Integer32
_NetBotz_prd_bot_camera_is_flipped_Object = MibScalar
netBotz_prd_bot_camera_is_flipped = _NetBotz_prd_bot_camera_is_flipped_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 159),
    _NetBotz_prd_bot_camera_is_flipped_Type()
)
netBotz_prd_bot_camera_is_flipped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_camera_is_flipped.setStatus("mandatory")
_NetBotz_prd_bot_camera_brightness_Type = Integer32
_NetBotz_prd_bot_camera_brightness_Object = MibScalar
netBotz_prd_bot_camera_brightness = _NetBotz_prd_bot_camera_brightness_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 160),
    _NetBotz_prd_bot_camera_brightness_Type()
)
netBotz_prd_bot_camera_brightness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_camera_brightness.setStatus("mandatory")
_NetBotz_prd_crawlers_ObjectIdentity = ObjectIdentity
netBotz_prd_crawlers = _NetBotz_prd_crawlers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20)
)
_Netbotz_crawlers_ObjectIdentity = ObjectIdentity
netbotz_crawlers = _Netbotz_crawlers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528)
)
_NetBotz_prd_crl_mib2_ObjectIdentity = ObjectIdentity
netBotz_prd_crl_mib2 = _NetBotz_prd_crl_mib2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1)
)
_NetBotz_prd_crl_mib2_ping_Type = Integer32
_NetBotz_prd_crl_mib2_ping_Object = MibScalar
netBotz_prd_crl_mib2_ping = _NetBotz_prd_crl_mib2_ping_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 3),
    _NetBotz_prd_crl_mib2_ping_Type()
)
netBotz_prd_crl_mib2_ping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_mib2_ping.setStatus("mandatory")
_NetBotz_prd_crl_mib2_uptime_Type = TimeTicks
_NetBotz_prd_crl_mib2_uptime_Object = MibScalar
netBotz_prd_crl_mib2_uptime = _NetBotz_prd_crl_mib2_uptime_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 8),
    _NetBotz_prd_crl_mib2_uptime_Type()
)
netBotz_prd_crl_mib2_uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_mib2_uptime.setStatus("mandatory")
_NetBotz_prd_crl_mib2_snmpstatus_Type = DisplayString
_NetBotz_prd_crl_mib2_snmpstatus_Object = MibScalar
netBotz_prd_crl_mib2_snmpstatus = _NetBotz_prd_crl_mib2_snmpstatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 9),
    _NetBotz_prd_crl_mib2_snmpstatus_Type()
)
netBotz_prd_crl_mib2_snmpstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_mib2_snmpstatus.setStatus("mandatory")
_NetBotz_prd_crl_mib2if_ObjectIdentity = ObjectIdentity
netBotz_prd_crl_mib2if = _NetBotz_prd_crl_mib2if_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2)
)
_NetBotz_prd_crl_mib2if_opstatus_Type = Integer32
_NetBotz_prd_crl_mib2if_opstatus_Object = MibScalar
netBotz_prd_crl_mib2if_opstatus = _NetBotz_prd_crl_mib2if_opstatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2, 6),
    _NetBotz_prd_crl_mib2if_opstatus_Type()
)
netBotz_prd_crl_mib2if_opstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_mib2if_opstatus.setStatus("mandatory")
_NetBotz_prd_crltrap_ObjectIdentity = ObjectIdentity
netBotz_prd_crltrap = _NetBotz_prd_crltrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21)
)
_NetBotz_prd_crl_trap_index_Type = Integer32
_NetBotz_prd_crl_trap_index_Object = MibScalar
netBotz_prd_crl_trap_index = _NetBotz_prd_crl_trap_index_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 20),
    _NetBotz_prd_crl_trap_index_Type()
)
netBotz_prd_crl_trap_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_index.setStatus("mandatory")
_NetBotz_prd_crl_trap_address_Type = IpAddress
_NetBotz_prd_crl_trap_address_Object = MibScalar
netBotz_prd_crl_trap_address = _NetBotz_prd_crl_trap_address_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 21),
    _NetBotz_prd_crl_trap_address_Type()
)
netBotz_prd_crl_trap_address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_address.setStatus("mandatory")
_NetBotz_prd_crl_trap_oid_Type = ObjectIdentifier
_NetBotz_prd_crl_trap_oid_Object = MibScalar
netBotz_prd_crl_trap_oid = _NetBotz_prd_crl_trap_oid_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 22),
    _NetBotz_prd_crl_trap_oid_Type()
)
netBotz_prd_crl_trap_oid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_oid.setStatus("mandatory")
_NetBotz_prd_crl_trap_botoid_Type = ObjectIdentifier
_NetBotz_prd_crl_trap_botoid_Object = MibScalar
netBotz_prd_crl_trap_botoid = _NetBotz_prd_crl_trap_botoid_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 23),
    _NetBotz_prd_crl_trap_botoid_Type()
)
netBotz_prd_crl_trap_botoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_botoid.setStatus("mandatory")
_NetBotz_prd_crl_trap_value_Type = Integer32
_NetBotz_prd_crl_trap_value_Object = MibScalar
netBotz_prd_crl_trap_value = _NetBotz_prd_crl_trap_value_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 24),
    _NetBotz_prd_crl_trap_value_Type()
)
netBotz_prd_crl_trap_value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_value.setStatus("mandatory")
_NetBotz_prd_crl_trap_date_Type = Integer32
_NetBotz_prd_crl_trap_date_Object = MibScalar
netBotz_prd_crl_trap_date = _NetBotz_prd_crl_trap_date_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 25),
    _NetBotz_prd_crl_trap_date_Type()
)
netBotz_prd_crl_trap_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_date.setStatus("mandatory")
_NetBotz_prd_crl_trap_attrib_Type = Integer32
_NetBotz_prd_crl_trap_attrib_Object = MibScalar
netBotz_prd_crl_trap_attrib = _NetBotz_prd_crl_trap_attrib_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 26),
    _NetBotz_prd_crl_trap_attrib_Type()
)
netBotz_prd_crl_trap_attrib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_attrib.setStatus("mandatory")
_NetBotz_prd_crl_trap_desc_Type = DisplayString
_NetBotz_prd_crl_trap_desc_Object = MibScalar
netBotz_prd_crl_trap_desc = _NetBotz_prd_crl_trap_desc_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 27),
    _NetBotz_prd_crl_trap_desc_Type()
)
netBotz_prd_crl_trap_desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_desc.setStatus("mandatory")
_NetBotz_prd_bot_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_traps = _NetBotz_prd_bot_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100)
)
_NetBotz_prd_bot_temperature_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_temperature_traps = _NetBotz_prd_bot_temperature_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 1)
)
_NetBotz_prd_bot_humidity_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_humidity_traps = _NetBotz_prd_bot_humidity_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 2)
)
_NetBotz_prd_bot_airflow_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_airflow_traps = _NetBotz_prd_bot_airflow_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 3)
)
_NetBotz_prd_bot_audio_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_audio_traps = _NetBotz_prd_bot_audio_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 4)
)
_NetBotz_prd_bot_door_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_door_traps = _NetBotz_prd_bot_door_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 5)
)
_NetBotz_prd_bot_amp1_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_amp1_traps = _NetBotz_prd_bot_amp1_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 6)
)
_NetBotz_prd_bot_amp2_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_amp2_traps = _NetBotz_prd_bot_amp2_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 7)
)
_NetBotz_prd_bot_amp3_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_amp3_traps = _NetBotz_prd_bot_amp3_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 8)
)
_NetBotz_prd_bot_amp4_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_amp4_traps = _NetBotz_prd_bot_amp4_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 9)
)
_NetBotz_prd_bot_amp_total_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_amp_total_traps = _NetBotz_prd_bot_amp_total_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 10)
)
_NetBotz_prd_bot_ext_temp1_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_temp1_traps = _NetBotz_prd_bot_ext_temp1_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 11)
)
_NetBotz_prd_bot_ext_temp2_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_temp2_traps = _NetBotz_prd_bot_ext_temp2_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 12)
)
_NetBotz_prd_bot_ext_temp3_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_temp3_traps = _NetBotz_prd_bot_ext_temp3_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 13)
)
_NetBotz_prd_bot_ext_temp4_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_temp4_traps = _NetBotz_prd_bot_ext_temp4_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 14)
)
_NetBotz_prd_bot_ext_dry1_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_dry1_traps = _NetBotz_prd_bot_ext_dry1_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 15)
)
_NetBotz_prd_bot_ext_dry2_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_dry2_traps = _NetBotz_prd_bot_ext_dry2_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 16)
)
_NetBotz_prd_bot_ext_dry3_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_dry3_traps = _NetBotz_prd_bot_ext_dry3_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 17)
)
_NetBotz_prd_bot_ext_dry4_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_dry4_traps = _NetBotz_prd_bot_ext_dry4_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 18)
)
_NetBotz_prd_bot_amp5_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_amp5_traps = _NetBotz_prd_bot_amp5_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 19)
)
_NetBotz_prd_bot_amp6_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_amp6_traps = _NetBotz_prd_bot_amp6_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 20)
)
_NetBotz_prd_bot_amp7_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_amp7_traps = _NetBotz_prd_bot_amp7_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 21)
)
_NetBotz_prd_bot_ext_temp5_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_temp5_traps = _NetBotz_prd_bot_ext_temp5_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 22)
)
_NetBotz_prd_bot_ext_temp6_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_temp6_traps = _NetBotz_prd_bot_ext_temp6_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 23)
)
_NetBotz_prd_bot_ext_temp7_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_temp7_traps = _NetBotz_prd_bot_ext_temp7_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 24)
)
_NetBotz_prd_bot_ext_dry5_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_dry5_traps = _NetBotz_prd_bot_ext_dry5_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 25)
)
_NetBotz_prd_bot_ext_dry6_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_dry6_traps = _NetBotz_prd_bot_ext_dry6_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 26)
)
_NetBotz_prd_bot_ext_dry7_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_dry7_traps = _NetBotz_prd_bot_ext_dry7_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 27)
)
_NetBotz_prd_bot_camera_motion_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_camera_motion_traps = _NetBotz_prd_bot_camera_motion_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 28)
)
_NetBotz_prd_bot_ext_humi1_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_humi1_traps = _NetBotz_prd_bot_ext_humi1_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 29)
)
_NetBotz_prd_bot_ext_humi2_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_humi2_traps = _NetBotz_prd_bot_ext_humi2_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 30)
)
_NetBotz_prd_bot_ext_humi3_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_humi3_traps = _NetBotz_prd_bot_ext_humi3_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 31)
)
_NetBotz_prd_bot_ext_humi4_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_humi4_traps = _NetBotz_prd_bot_ext_humi4_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 32)
)
_NetBotz_prd_bot_ext_humi5_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_humi5_traps = _NetBotz_prd_bot_ext_humi5_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 33)
)
_NetBotz_prd_bot_ext_humi6_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_humi6_traps = _NetBotz_prd_bot_ext_humi6_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 34)
)
_NetBotz_prd_bot_ext_humi7_traps_ObjectIdentity = ObjectIdentity
netBotz_prd_bot_ext_humi7_traps = _NetBotz_prd_bot_ext_humi7_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 35)
)
_NetBotz_prd_WallBotz_300_ObjectIdentity = ObjectIdentity
netBotz_prd_WallBotz_300 = _NetBotz_prd_WallBotz_300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1000)
)
_NetBotz_prd_RackBotz_300_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_300 = _NetBotz_prd_RackBotz_300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1001)
)
_NetBotz_prd_RackBotz_300U_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_300U = _NetBotz_prd_RackBotz_300U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1002)
)
_NetBotz_prd_WallBotz_400_ObjectIdentity = ObjectIdentity
netBotz_prd_WallBotz_400 = _NetBotz_prd_WallBotz_400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1003)
)
_NetBotz_prd_RackBotz_400_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_400 = _NetBotz_prd_RackBotz_400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1004)
)
_NetBotz_prd_RackBotz_303_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_303 = _NetBotz_prd_RackBotz_303_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1006)
)
_NetBotz_prd_WallBotz_310_ObjectIdentity = ObjectIdentity
netBotz_prd_WallBotz_310 = _NetBotz_prd_WallBotz_310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1007)
)
_NetBotz_prd_RackBotz_310_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_310 = _NetBotz_prd_RackBotz_310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1008)
)
_NetBotz_prd_WallBotz_300B_ObjectIdentity = ObjectIdentity
netBotz_prd_WallBotz_300B = _NetBotz_prd_WallBotz_300B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1009)
)
_NetBotz_prd_WallBotz_300C_ObjectIdentity = ObjectIdentity
netBotz_prd_WallBotz_300C = _NetBotz_prd_WallBotz_300C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1100)
)
_NetBotz_prd_RackBotz_300C_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_300C = _NetBotz_prd_RackBotz_300C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1101)
)
_NetBotz_prd_RackBotz_300UC_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_300UC = _NetBotz_prd_RackBotz_300UC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1102)
)
_NetBotz_prd_WallBotz_400C_ObjectIdentity = ObjectIdentity
netBotz_prd_WallBotz_400C = _NetBotz_prd_WallBotz_400C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1103)
)
_NetBotz_prd_RackBotz_400C_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_400C = _NetBotz_prd_RackBotz_400C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1104)
)
_NetBotz_prd_RackBotz_303C_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_303C = _NetBotz_prd_RackBotz_303C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1106)
)
_NetBotz_prd_WallBotz_310C_ObjectIdentity = ObjectIdentity
netBotz_prd_WallBotz_310C = _NetBotz_prd_WallBotz_310C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1107)
)
_NetBotz_prd_RackBotz_310C_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_310C = _NetBotz_prd_RackBotz_310C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1108)
)
_NetBotz_prd_WallBotz_300BC_ObjectIdentity = ObjectIdentity
netBotz_prd_WallBotz_300BC = _NetBotz_prd_WallBotz_300BC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1109)
)
_NetBotz_prd_WallBotz_300E_ObjectIdentity = ObjectIdentity
netBotz_prd_WallBotz_300E = _NetBotz_prd_WallBotz_300E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1200)
)
_NetBotz_prd_RackBotz_300E_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_300E = _NetBotz_prd_RackBotz_300E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1201)
)
_NetBotz_prd_RackBotz_300UE_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_300UE = _NetBotz_prd_RackBotz_300UE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1202)
)
_NetBotz_prd_WallBotz_400E_ObjectIdentity = ObjectIdentity
netBotz_prd_WallBotz_400E = _NetBotz_prd_WallBotz_400E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1203)
)
_NetBotz_prd_RackBotz_400E_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_400E = _NetBotz_prd_RackBotz_400E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1204)
)
_NetBotz_prd_RackBotz_303E_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_303E = _NetBotz_prd_RackBotz_303E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1206)
)
_NetBotz_prd_WallBotz_310E_ObjectIdentity = ObjectIdentity
netBotz_prd_WallBotz_310E = _NetBotz_prd_WallBotz_310E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1207)
)
_NetBotz_prd_RackBotz_310E_ObjectIdentity = ObjectIdentity
netBotz_prd_RackBotz_310E = _NetBotz_prd_RackBotz_310E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1208)
)
_NetBotz_prd_WallBotz_300BE_ObjectIdentity = ObjectIdentity
netBotz_prd_WallBotz_300BE = _NetBotz_prd_WallBotz_300BE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 1209)
)
_ExpPortTable_Object = MibTable
expPortTable = _ExpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31)
)
if mibBuilder.loadTexts:
    expPortTable.setStatus("mandatory")
_ExpPortEntry_Object = MibTableRow
expPortEntry = _ExpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1)
)
if mibBuilder.loadTexts:
    expPortEntry.setStatus("mandatory")
_ExpPort_module_id_Type = DisplayString
_ExpPort_module_id_Object = MibScalar
expPort_module_id = _ExpPort_module_id_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 1),
    _ExpPort_module_id_Type()
)
expPort_module_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_module_id.setStatus("mandatory")
_ExpPort_module_type_Type = DisplayString
_ExpPort_module_type_Object = MibScalar
expPort_module_type = _ExpPort_module_type_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 2),
    _ExpPort_module_type_Type()
)
expPort_module_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_module_type.setStatus("mandatory")
_ExpPort_label_Type = DisplayString
_ExpPort_label_Object = MibScalar
expPort_label = _ExpPort_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 3),
    _ExpPort_label_Type()
)
expPort_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_label.setStatus("mandatory")
_ExpPort_amps_Type = Integer32
_ExpPort_amps_Object = MibScalar
expPort_amps = _ExpPort_amps_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 20),
    _ExpPort_amps_Type()
)
expPort_amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expPort_amps.setStatus("mandatory")
_ExpPort_total_amp_seconds_Type = Integer32
_ExpPort_total_amp_seconds_Object = MibScalar
expPort_total_amp_seconds = _ExpPort_total_amp_seconds_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 21),
    _ExpPort_total_amp_seconds_Type()
)
expPort_total_amp_seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expPort_total_amp_seconds.setStatus("mandatory")
_ExpPort_total_amp_seconds_since_time_Type = Integer32
_ExpPort_total_amp_seconds_since_time_Object = MibScalar
expPort_total_amp_seconds_since_time = _ExpPort_total_amp_seconds_since_time_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 22),
    _ExpPort_total_amp_seconds_since_time_Type()
)
expPort_total_amp_seconds_since_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_total_amp_seconds_since_time.setStatus("mandatory")
_ExpPort_amps_enabled_Type = Integer32
_ExpPort_amps_enabled_Object = MibScalar
expPort_amps_enabled = _ExpPort_amps_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 23),
    _ExpPort_amps_enabled_Type()
)
expPort_amps_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_amps_enabled.setStatus("mandatory")
_ExpPort_amps_min_Type = Integer32
_ExpPort_amps_min_Object = MibScalar
expPort_amps_min = _ExpPort_amps_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 24),
    _ExpPort_amps_min_Type()
)
expPort_amps_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_amps_min.setStatus("mandatory")
_ExpPort_amps_max_Type = Integer32
_ExpPort_amps_max_Object = MibScalar
expPort_amps_max = _ExpPort_amps_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 25),
    _ExpPort_amps_max_Type()
)
expPort_amps_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_amps_max.setStatus("mandatory")
_ExpPort_amps_uV_per_10mA_Type = Integer32
_ExpPort_amps_uV_per_10mA_Object = MibScalar
expPort_amps_uV_per_10mA = _ExpPort_amps_uV_per_10mA_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 26),
    _ExpPort_amps_uV_per_10mA_Type()
)
expPort_amps_uV_per_10mA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_amps_uV_per_10mA.setStatus("mandatory")
_ExpPort_amps_max_range_Type = Integer32
_ExpPort_amps_max_range_Object = MibScalar
expPort_amps_max_range = _ExpPort_amps_max_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 27),
    _ExpPort_amps_max_range_Type()
)
expPort_amps_max_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_amps_max_range.setStatus("mandatory")
_ExpPort_ext_temp_Type = Integer32
_ExpPort_ext_temp_Object = MibScalar
expPort_ext_temp = _ExpPort_ext_temp_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 40),
    _ExpPort_ext_temp_Type()
)
expPort_ext_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expPort_ext_temp.setStatus("mandatory")
_ExpPort_ext_temp_enabled_Type = Integer32
_ExpPort_ext_temp_enabled_Object = MibScalar
expPort_ext_temp_enabled = _ExpPort_ext_temp_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 41),
    _ExpPort_ext_temp_enabled_Type()
)
expPort_ext_temp_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_temp_enabled.setStatus("mandatory")
_ExpPort_ext_temp_min_Type = Integer32
_ExpPort_ext_temp_min_Object = MibScalar
expPort_ext_temp_min = _ExpPort_ext_temp_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 42),
    _ExpPort_ext_temp_min_Type()
)
expPort_ext_temp_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_temp_min.setStatus("mandatory")
_ExpPort_ext_temp_max_Type = Integer32
_ExpPort_ext_temp_max_Object = MibScalar
expPort_ext_temp_max = _ExpPort_ext_temp_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 43),
    _ExpPort_ext_temp_max_Type()
)
expPort_ext_temp_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_temp_max.setStatus("mandatory")
_ExpPort_ext_temp_uV_per_degreeC_Type = Integer32
_ExpPort_ext_temp_uV_per_degreeC_Object = MibScalar
expPort_ext_temp_uV_per_degreeC = _ExpPort_ext_temp_uV_per_degreeC_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 44),
    _ExpPort_ext_temp_uV_per_degreeC_Type()
)
expPort_ext_temp_uV_per_degreeC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_temp_uV_per_degreeC.setStatus("mandatory")
_ExpPort_ext_temp_uV_at_0_degreeC_Type = Integer32
_ExpPort_ext_temp_uV_at_0_degreeC_Object = MibScalar
expPort_ext_temp_uV_at_0_degreeC = _ExpPort_ext_temp_uV_at_0_degreeC_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 45),
    _ExpPort_ext_temp_uV_at_0_degreeC_Type()
)
expPort_ext_temp_uV_at_0_degreeC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_temp_uV_at_0_degreeC.setStatus("mandatory")
_ExpPort_ext_temp_min_range_Type = Integer32
_ExpPort_ext_temp_min_range_Object = MibScalar
expPort_ext_temp_min_range = _ExpPort_ext_temp_min_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 46),
    _ExpPort_ext_temp_min_range_Type()
)
expPort_ext_temp_min_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_temp_min_range.setStatus("mandatory")
_ExpPort_ext_temp_max_range_Type = Integer32
_ExpPort_ext_temp_max_range_Object = MibScalar
expPort_ext_temp_max_range = _ExpPort_ext_temp_max_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 47),
    _ExpPort_ext_temp_max_range_Type()
)
expPort_ext_temp_max_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_temp_max_range.setStatus("mandatory")
_ExpPort_ext_dry_Type = Integer32
_ExpPort_ext_dry_Object = MibScalar
expPort_ext_dry = _ExpPort_ext_dry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 60),
    _ExpPort_ext_dry_Type()
)
expPort_ext_dry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expPort_ext_dry.setStatus("mandatory")
_ExpPort_ext_dry_alarm_value_Type = Integer32
_ExpPort_ext_dry_alarm_value_Object = MibScalar
expPort_ext_dry_alarm_value = _ExpPort_ext_dry_alarm_value_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 61),
    _ExpPort_ext_dry_alarm_value_Type()
)
expPort_ext_dry_alarm_value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_dry_alarm_value.setStatus("mandatory")
_ExpPort_ext_dry_enabled_Type = Integer32
_ExpPort_ext_dry_enabled_Object = MibScalar
expPort_ext_dry_enabled = _ExpPort_ext_dry_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 62),
    _ExpPort_ext_dry_enabled_Type()
)
expPort_ext_dry_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_dry_enabled.setStatus("mandatory")
_ExpPort_ext_dry_label_Type = DisplayString
_ExpPort_ext_dry_label_Object = MibScalar
expPort_ext_dry_label = _ExpPort_ext_dry_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 63),
    _ExpPort_ext_dry_label_Type()
)
expPort_ext_dry_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_dry_label.setStatus("mandatory")
_ExpPort_ext_dry_open_label_Type = DisplayString
_ExpPort_ext_dry_open_label_Object = MibScalar
expPort_ext_dry_open_label = _ExpPort_ext_dry_open_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 64),
    _ExpPort_ext_dry_open_label_Type()
)
expPort_ext_dry_open_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_dry_open_label.setStatus("mandatory")
_ExpPort_ext_dry_closed_label_Type = DisplayString
_ExpPort_ext_dry_closed_label_Object = MibScalar
expPort_ext_dry_closed_label = _ExpPort_ext_dry_closed_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 65),
    _ExpPort_ext_dry_closed_label_Type()
)
expPort_ext_dry_closed_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_dry_closed_label.setStatus("mandatory")
_ExpPort_ext_dry_open_to_close_millis_Type = Integer32
_ExpPort_ext_dry_open_to_close_millis_Object = MibScalar
expPort_ext_dry_open_to_close_millis = _ExpPort_ext_dry_open_to_close_millis_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 66),
    _ExpPort_ext_dry_open_to_close_millis_Type()
)
expPort_ext_dry_open_to_close_millis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_dry_open_to_close_millis.setStatus("mandatory")
_ExpPort_ext_dry_close_to_open_millis_Type = Integer32
_ExpPort_ext_dry_close_to_open_millis_Object = MibScalar
expPort_ext_dry_close_to_open_millis = _ExpPort_ext_dry_close_to_open_millis_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 67),
    _ExpPort_ext_dry_close_to_open_millis_Type()
)
expPort_ext_dry_close_to_open_millis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_dry_close_to_open_millis.setStatus("mandatory")
_ExpPort_ext_dry_response_Type = DisplayString
_ExpPort_ext_dry_response_Object = MibScalar
expPort_ext_dry_response = _ExpPort_ext_dry_response_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 68),
    _ExpPort_ext_dry_response_Type()
)
expPort_ext_dry_response.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_dry_response.setStatus("mandatory")
_ExpPort_ext_humi_Type = Integer32
_ExpPort_ext_humi_Object = MibScalar
expPort_ext_humi = _ExpPort_ext_humi_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 80),
    _ExpPort_ext_humi_Type()
)
expPort_ext_humi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expPort_ext_humi.setStatus("mandatory")
_ExpPort_ext_humi_enabled_Type = Integer32
_ExpPort_ext_humi_enabled_Object = MibScalar
expPort_ext_humi_enabled = _ExpPort_ext_humi_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 81),
    _ExpPort_ext_humi_enabled_Type()
)
expPort_ext_humi_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_humi_enabled.setStatus("mandatory")
_ExpPort_ext_humi_min_Type = Integer32
_ExpPort_ext_humi_min_Object = MibScalar
expPort_ext_humi_min = _ExpPort_ext_humi_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 82),
    _ExpPort_ext_humi_min_Type()
)
expPort_ext_humi_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_humi_min.setStatus("mandatory")
_ExpPort_ext_humi_max_Type = Integer32
_ExpPort_ext_humi_max_Object = MibScalar
expPort_ext_humi_max = _ExpPort_ext_humi_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 83),
    _ExpPort_ext_humi_max_Type()
)
expPort_ext_humi_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_humi_max.setStatus("mandatory")
_ExpPort_ext_humi_uV_per_percent_Type = Integer32
_ExpPort_ext_humi_uV_per_percent_Object = MibScalar
expPort_ext_humi_uV_per_percent = _ExpPort_ext_humi_uV_per_percent_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 84),
    _ExpPort_ext_humi_uV_per_percent_Type()
)
expPort_ext_humi_uV_per_percent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_humi_uV_per_percent.setStatus("mandatory")
_ExpPort_ext_humi_uV_at_0_percent_Type = Integer32
_ExpPort_ext_humi_uV_at_0_percent_Object = MibScalar
expPort_ext_humi_uV_at_0_percent = _ExpPort_ext_humi_uV_at_0_percent_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 85),
    _ExpPort_ext_humi_uV_at_0_percent_Type()
)
expPort_ext_humi_uV_at_0_percent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_humi_uV_at_0_percent.setStatus("mandatory")
_ExpPort_ext_humi_min_range_Type = Integer32
_ExpPort_ext_humi_min_range_Object = MibScalar
expPort_ext_humi_min_range = _ExpPort_ext_humi_min_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 86),
    _ExpPort_ext_humi_min_range_Type()
)
expPort_ext_humi_min_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_humi_min_range.setStatus("mandatory")
_ExpPort_ext_humi_max_range_Type = Integer32
_ExpPort_ext_humi_max_range_Object = MibScalar
expPort_ext_humi_max_range = _ExpPort_ext_humi_max_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 31, 1, 87),
    _ExpPort_ext_humi_max_range_Type()
)
expPort_ext_humi_max_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expPort_ext_humi_max_range.setStatus("mandatory")
_NetBotz_metric_ObjectIdentity = ObjectIdentity
netBotz_metric = _NetBotz_metric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 32)
)
_NetBotz_metric_onboard_ObjectIdentity = ObjectIdentity
netBotz_metric_onboard = _NetBotz_metric_onboard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10)
)
_NetBotz_metric_onboard_model_Type = DisplayString
_NetBotz_metric_onboard_model_Object = MibScalar
netBotz_metric_onboard_model = _NetBotz_metric_onboard_model_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 1),
    _NetBotz_metric_onboard_model_Type()
)
netBotz_metric_onboard_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_model.setStatus("mandatory")
_NetBotz_metric_onboard_temp_Type = Integer32
_NetBotz_metric_onboard_temp_Object = MibScalar
netBotz_metric_onboard_temp = _NetBotz_metric_onboard_temp_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 2),
    _NetBotz_metric_onboard_temp_Type()
)
netBotz_metric_onboard_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_temp.setStatus("mandatory")
_NetBotz_metric_onboard_humidity_Type = Integer32
_NetBotz_metric_onboard_humidity_Object = MibScalar
netBotz_metric_onboard_humidity = _NetBotz_metric_onboard_humidity_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 3),
    _NetBotz_metric_onboard_humidity_Type()
)
netBotz_metric_onboard_humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_humidity.setStatus("mandatory")
_NetBotz_metric_onboard_airflow_Type = Integer32
_NetBotz_metric_onboard_airflow_Object = MibScalar
netBotz_metric_onboard_airflow = _NetBotz_metric_onboard_airflow_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 4),
    _NetBotz_metric_onboard_airflow_Type()
)
netBotz_metric_onboard_airflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_airflow.setStatus("mandatory")
_NetBotz_metric_onboard_audio_Type = Integer32
_NetBotz_metric_onboard_audio_Object = MibScalar
netBotz_metric_onboard_audio = _NetBotz_metric_onboard_audio_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 5),
    _NetBotz_metric_onboard_audio_Type()
)
netBotz_metric_onboard_audio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_audio.setStatus("mandatory")
_NetBotz_metric_onboard_doorajar_Type = Integer32
_NetBotz_metric_onboard_doorajar_Object = MibScalar
netBotz_metric_onboard_doorajar = _NetBotz_metric_onboard_doorajar_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 6),
    _NetBotz_metric_onboard_doorajar_Type()
)
netBotz_metric_onboard_doorajar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_doorajar.setStatus("mandatory")
_NetBotz_metric_onboard_temp_min_Type = Integer32
_NetBotz_metric_onboard_temp_min_Object = MibScalar
netBotz_metric_onboard_temp_min = _NetBotz_metric_onboard_temp_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 7),
    _NetBotz_metric_onboard_temp_min_Type()
)
netBotz_metric_onboard_temp_min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_temp_min.setStatus("mandatory")
_NetBotz_metric_onboard_temp_max_Type = Integer32
_NetBotz_metric_onboard_temp_max_Object = MibScalar
netBotz_metric_onboard_temp_max = _NetBotz_metric_onboard_temp_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 8),
    _NetBotz_metric_onboard_temp_max_Type()
)
netBotz_metric_onboard_temp_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_temp_max.setStatus("mandatory")
_NetBotz_metric_onboard_humidity_min_Type = Integer32
_NetBotz_metric_onboard_humidity_min_Object = MibScalar
netBotz_metric_onboard_humidity_min = _NetBotz_metric_onboard_humidity_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 9),
    _NetBotz_metric_onboard_humidity_min_Type()
)
netBotz_metric_onboard_humidity_min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_humidity_min.setStatus("mandatory")
_NetBotz_metric_onboard_humidity_max_Type = Integer32
_NetBotz_metric_onboard_humidity_max_Object = MibScalar
netBotz_metric_onboard_humidity_max = _NetBotz_metric_onboard_humidity_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 10),
    _NetBotz_metric_onboard_humidity_max_Type()
)
netBotz_metric_onboard_humidity_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_humidity_max.setStatus("mandatory")
_NetBotz_metric_onboard_airflow_mins_Type = Integer32
_NetBotz_metric_onboard_airflow_mins_Object = MibScalar
netBotz_metric_onboard_airflow_mins = _NetBotz_metric_onboard_airflow_mins_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 11),
    _NetBotz_metric_onboard_airflow_mins_Type()
)
netBotz_metric_onboard_airflow_mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_airflow_mins.setStatus("mandatory")
_NetBotz_metric_onboard_audio_secs_Type = Integer32
_NetBotz_metric_onboard_audio_secs_Object = MibScalar
netBotz_metric_onboard_audio_secs = _NetBotz_metric_onboard_audio_secs_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 12),
    _NetBotz_metric_onboard_audio_secs_Type()
)
netBotz_metric_onboard_audio_secs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_audio_secs.setStatus("mandatory")
_NetBotz_metric_onboard_switch_state_Type = Integer32
_NetBotz_metric_onboard_switch_state_Object = MibScalar
netBotz_metric_onboard_switch_state = _NetBotz_metric_onboard_switch_state_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 13),
    _NetBotz_metric_onboard_switch_state_Type()
)
netBotz_metric_onboard_switch_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_switch_state.setStatus("mandatory")
_NetBotz_metric_onboard_audio_level_Type = Integer32
_NetBotz_metric_onboard_audio_level_Object = MibScalar
netBotz_metric_onboard_audio_level = _NetBotz_metric_onboard_audio_level_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 14),
    _NetBotz_metric_onboard_audio_level_Type()
)
netBotz_metric_onboard_audio_level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_audio_level.setStatus("mandatory")
_NetBotz_metric_onboard_airflow_level_Type = Integer32
_NetBotz_metric_onboard_airflow_level_Object = MibScalar
netBotz_metric_onboard_airflow_level = _NetBotz_metric_onboard_airflow_level_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 15),
    _NetBotz_metric_onboard_airflow_level_Type()
)
netBotz_metric_onboard_airflow_level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_airflow_level.setStatus("mandatory")
_NetBotz_metric_onboard_cam_motion_Type = Integer32
_NetBotz_metric_onboard_cam_motion_Object = MibScalar
netBotz_metric_onboard_cam_motion = _NetBotz_metric_onboard_cam_motion_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 16),
    _NetBotz_metric_onboard_cam_motion_Type()
)
netBotz_metric_onboard_cam_motion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_cam_motion.setStatus("mandatory")
_NetBotz_metric_onboard_cam_motion_sensitivity_Type = Integer32
_NetBotz_metric_onboard_cam_motion_sensitivity_Object = MibScalar
netBotz_metric_onboard_cam_motion_sensitivity = _NetBotz_metric_onboard_cam_motion_sensitivity_Object(
    (1, 3, 6, 1, 4, 1, 5528, 32, 10, 17),
    _NetBotz_metric_onboard_cam_motion_sensitivity_Type()
)
netBotz_metric_onboard_cam_motion_sensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_metric_onboard_cam_motion_sensitivity.setStatus("mandatory")
_NetBotz_snmp_ObjectIdentity = ObjectIdentity
netBotz_snmp = _NetBotz_snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 40)
)
_NetBotz_snmp_traptarget_Type = IpAddress
_NetBotz_snmp_traptarget_Object = MibScalar
netBotz_snmp_traptarget = _NetBotz_snmp_traptarget_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 1),
    _NetBotz_snmp_traptarget_Type()
)
netBotz_snmp_traptarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_snmp_traptarget.setStatus("mandatory")
_NetBotz_snmp_community_Type = DisplayString
_NetBotz_snmp_community_Object = MibScalar
netBotz_snmp_community = _NetBotz_snmp_community_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 2),
    _NetBotz_snmp_community_Type()
)
netBotz_snmp_community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_snmp_community.setStatus("mandatory")
_NetBotz_snmp_timeout_Type = Integer32
_NetBotz_snmp_timeout_Object = MibScalar
netBotz_snmp_timeout = _NetBotz_snmp_timeout_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 3),
    _NetBotz_snmp_timeout_Type()
)
netBotz_snmp_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_snmp_timeout.setStatus("mandatory")
_NetBotz_snmp_retries_Type = Integer32
_NetBotz_snmp_retries_Object = MibScalar
netBotz_snmp_retries = _NetBotz_snmp_retries_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 4),
    _NetBotz_snmp_retries_Type()
)
netBotz_snmp_retries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_snmp_retries.setStatus("mandatory")
_NetBotz_userid_1_Type = DisplayString
_NetBotz_userid_1_Object = MibScalar
netBotz_userid_1 = _NetBotz_userid_1_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 5),
    _NetBotz_userid_1_Type()
)
netBotz_userid_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_userid_1.setStatus("mandatory")
_NetBotz_password_1_Type = DisplayString
_NetBotz_password_1_Object = MibScalar
netBotz_password_1 = _NetBotz_password_1_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 6),
    _NetBotz_password_1_Type()
)
netBotz_password_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_password_1.setStatus("mandatory")
_NetBotz_userid_2_Type = DisplayString
_NetBotz_userid_2_Object = MibScalar
netBotz_userid_2 = _NetBotz_userid_2_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 7),
    _NetBotz_userid_2_Type()
)
netBotz_userid_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_userid_2.setStatus("mandatory")
_NetBotz_password_2_Type = DisplayString
_NetBotz_password_2_Object = MibScalar
netBotz_password_2 = _NetBotz_password_2_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 8),
    _NetBotz_password_2_Type()
)
netBotz_password_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_password_2.setStatus("mandatory")
_NetBotz_userid_3_Type = DisplayString
_NetBotz_userid_3_Object = MibScalar
netBotz_userid_3 = _NetBotz_userid_3_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 9),
    _NetBotz_userid_3_Type()
)
netBotz_userid_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_userid_3.setStatus("mandatory")
_NetBotz_password_3_Type = DisplayString
_NetBotz_password_3_Object = MibScalar
netBotz_password_3 = _NetBotz_password_3_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 10),
    _NetBotz_password_3_Type()
)
netBotz_password_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_password_3.setStatus("mandatory")
_NetBotz_snmp_traptarget2_Type = IpAddress
_NetBotz_snmp_traptarget2_Object = MibScalar
netBotz_snmp_traptarget2 = _NetBotz_snmp_traptarget2_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 11),
    _NetBotz_snmp_traptarget2_Type()
)
netBotz_snmp_traptarget2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_snmp_traptarget2.setStatus("mandatory")
_NetBotz_snmp_read_community_Type = DisplayString
_NetBotz_snmp_read_community_Object = MibScalar
netBotz_snmp_read_community = _NetBotz_snmp_read_community_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 12),
    _NetBotz_snmp_read_community_Type()
)
netBotz_snmp_read_community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_snmp_read_community.setStatus("mandatory")
_NetBotz_device_ObjectIdentity = ObjectIdentity
netBotz_device = _NetBotz_device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 50)
)
_NetBotz_dev_host_Type = DisplayString
_NetBotz_dev_host_Object = MibScalar
netBotz_dev_host = _NetBotz_dev_host_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 1),
    _NetBotz_dev_host_Type()
)
netBotz_dev_host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_host.setStatus("mandatory")
_NetBotz_dev_domain_Type = DisplayString
_NetBotz_dev_domain_Object = MibScalar
netBotz_dev_domain = _NetBotz_dev_domain_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 2),
    _NetBotz_dev_domain_Type()
)
netBotz_dev_domain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_domain.setStatus("mandatory")
_NetBotz_dev_ip_Type = IpAddress
_NetBotz_dev_ip_Object = MibScalar
netBotz_dev_ip = _NetBotz_dev_ip_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 3),
    _NetBotz_dev_ip_Type()
)
netBotz_dev_ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_ip.setStatus("mandatory")
_NetBotz_dev_netmask_Type = IpAddress
_NetBotz_dev_netmask_Object = MibScalar
netBotz_dev_netmask = _NetBotz_dev_netmask_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 4),
    _NetBotz_dev_netmask_Type()
)
netBotz_dev_netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_netmask.setStatus("mandatory")
_NetBotz_dev_gateway_Type = IpAddress
_NetBotz_dev_gateway_Object = MibScalar
netBotz_dev_gateway = _NetBotz_dev_gateway_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 5),
    _NetBotz_dev_gateway_Type()
)
netBotz_dev_gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_gateway.setStatus("mandatory")
_NetBotz_dev_primarydns_Type = IpAddress
_NetBotz_dev_primarydns_Object = MibScalar
netBotz_dev_primarydns = _NetBotz_dev_primarydns_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 6),
    _NetBotz_dev_primarydns_Type()
)
netBotz_dev_primarydns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_primarydns.setStatus("mandatory")
_NetBotz_dev_secondarydns_Type = IpAddress
_NetBotz_dev_secondarydns_Object = MibScalar
netBotz_dev_secondarydns = _NetBotz_dev_secondarydns_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 7),
    _NetBotz_dev_secondarydns_Type()
)
netBotz_dev_secondarydns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_secondarydns.setStatus("mandatory")
_NetBotz_dev_smtp_Type = DisplayString
_NetBotz_dev_smtp_Object = MibScalar
netBotz_dev_smtp = _NetBotz_dev_smtp_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 8),
    _NetBotz_dev_smtp_Type()
)
netBotz_dev_smtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_smtp.setStatus("mandatory")
_NetBotz_dev_smtpport_Type = Integer32
_NetBotz_dev_smtpport_Object = MibScalar
netBotz_dev_smtpport = _NetBotz_dev_smtpport_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 9),
    _NetBotz_dev_smtpport_Type()
)
netBotz_dev_smtpport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_smtpport.setStatus("mandatory")
_NetBotz_dev_popport_Type = Integer32
_NetBotz_dev_popport_Object = MibScalar
netBotz_dev_popport = _NetBotz_dev_popport_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 10),
    _NetBotz_dev_popport_Type()
)
netBotz_dev_popport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_popport.setStatus("mandatory")
_NetBotz_dev_loglevel_Type = Integer32
_NetBotz_dev_loglevel_Object = MibScalar
netBotz_dev_loglevel = _NetBotz_dev_loglevel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 11),
    _NetBotz_dev_loglevel_Type()
)
netBotz_dev_loglevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_loglevel.setStatus("mandatory")
_NetBotz_dev_primaryemail_Type = DisplayString
_NetBotz_dev_primaryemail_Object = MibScalar
netBotz_dev_primaryemail = _NetBotz_dev_primaryemail_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 14),
    _NetBotz_dev_primaryemail_Type()
)
netBotz_dev_primaryemail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_primaryemail.setStatus("mandatory")
_NetBotz_dev_secondaryemail_Type = DisplayString
_NetBotz_dev_secondaryemail_Object = MibScalar
netBotz_dev_secondaryemail = _NetBotz_dev_secondaryemail_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 15),
    _NetBotz_dev_secondaryemail_Type()
)
netBotz_dev_secondaryemail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_secondaryemail.setStatus("mandatory")
_NetBotz_dev_serialno_Type = DisplayString
_NetBotz_dev_serialno_Object = MibScalar
netBotz_dev_serialno = _NetBotz_dev_serialno_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 17),
    _NetBotz_dev_serialno_Type()
)
netBotz_dev_serialno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_dev_serialno.setStatus("mandatory")
_NetBotz_dev_pop_Type = DisplayString
_NetBotz_dev_pop_Object = MibScalar
netBotz_dev_pop = _NetBotz_dev_pop_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 18),
    _NetBotz_dev_pop_Type()
)
netBotz_dev_pop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_pop.setStatus("mandatory")
_NetBotz_dev_version_Type = DisplayString
_NetBotz_dev_version_Object = MibScalar
netBotz_dev_version = _NetBotz_dev_version_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 19),
    _NetBotz_dev_version_Type()
)
netBotz_dev_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_dev_version.setStatus("mandatory")
_NetBotz_dev_registered_Type = Integer32
_NetBotz_dev_registered_Object = MibScalar
netBotz_dev_registered = _NetBotz_dev_registered_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 20),
    _NetBotz_dev_registered_Type()
)
netBotz_dev_registered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_dev_registered.setStatus("mandatory")
_NetBotz_default_applet_Type = Integer32
_NetBotz_default_applet_Object = MibScalar
netBotz_default_applet = _NetBotz_default_applet_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 21),
    _NetBotz_default_applet_Type()
)
netBotz_default_applet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_default_applet.setStatus("mandatory")
_NetBotz_guibar_color_Type = Integer32
_NetBotz_guibar_color_Object = MibScalar
netBotz_guibar_color = _NetBotz_guibar_color_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 22),
    _NetBotz_guibar_color_Type()
)
netBotz_guibar_color.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_guibar_color.setStatus("mandatory")
_NetBotz_locale_Type = DisplayString
_NetBotz_locale_Object = MibScalar
netBotz_locale = _NetBotz_locale_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 23),
    _NetBotz_locale_Type()
)
netBotz_locale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_locale.setStatus("mandatory")
_NetBotz_timezone_Type = DisplayString
_NetBotz_timezone_Object = MibScalar
netBotz_timezone = _NetBotz_timezone_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 24),
    _NetBotz_timezone_Type()
)
netBotz_timezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_timezone.setStatus("mandatory")
_NetBotz_24hourpreferred_Type = Integer32
_NetBotz_24hourpreferred_Object = MibScalar
netBotz_24hourpreferred = _NetBotz_24hourpreferred_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 25),
    _NetBotz_24hourpreferred_Type()
)
netBotz_24hourpreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_24hourpreferred.setStatus("mandatory")
_NetBotz_utc_clock_Type = Integer32
_NetBotz_utc_clock_Object = MibScalar
netBotz_utc_clock = _NetBotz_utc_clock_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 26),
    _NetBotz_utc_clock_Type()
)
netBotz_utc_clock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_utc_clock.setStatus("mandatory")
_NetBotz_ismetric_Type = Integer32
_NetBotz_ismetric_Object = MibScalar
netBotz_ismetric = _NetBotz_ismetric_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 27),
    _NetBotz_ismetric_Type()
)
netBotz_ismetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_ismetric.setStatus("mandatory")
_NetBotz_alert_url_Type = DisplayString
_NetBotz_alert_url_Object = MibScalar
netBotz_alert_url = _NetBotz_alert_url_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 28),
    _NetBotz_alert_url_Type()
)
netBotz_alert_url.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_alert_url.setStatus("mandatory")
_NetBotz_picture_alert_url_Type = DisplayString
_NetBotz_picture_alert_url_Object = MibScalar
netBotz_picture_alert_url = _NetBotz_picture_alert_url_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 29),
    _NetBotz_picture_alert_url_Type()
)
netBotz_picture_alert_url.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_picture_alert_url.setStatus("mandatory")
_NetBotz_sensor_data_url_Type = DisplayString
_NetBotz_sensor_data_url_Object = MibScalar
netBotz_sensor_data_url = _NetBotz_sensor_data_url_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 30),
    _NetBotz_sensor_data_url_Type()
)
netBotz_sensor_data_url.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_sensor_data_url.setStatus("mandatory")
_NetBotz_alert_url_logon_Type = DisplayString
_NetBotz_alert_url_logon_Object = MibScalar
netBotz_alert_url_logon = _NetBotz_alert_url_logon_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 31),
    _NetBotz_alert_url_logon_Type()
)
netBotz_alert_url_logon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_alert_url_logon.setStatus("mandatory")
_NetBotz_picture_alert_url_logon_Type = DisplayString
_NetBotz_picture_alert_url_logon_Object = MibScalar
netBotz_picture_alert_url_logon = _NetBotz_picture_alert_url_logon_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 32),
    _NetBotz_picture_alert_url_logon_Type()
)
netBotz_picture_alert_url_logon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_picture_alert_url_logon.setStatus("mandatory")
_NetBotz_sensor_data_url_logon_Type = DisplayString
_NetBotz_sensor_data_url_logon_Object = MibScalar
netBotz_sensor_data_url_logon = _NetBotz_sensor_data_url_logon_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 33),
    _NetBotz_sensor_data_url_logon_Type()
)
netBotz_sensor_data_url_logon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_sensor_data_url_logon.setStatus("mandatory")
_NetBotz_sensor_data_url_period_Type = Integer32
_NetBotz_sensor_data_url_period_Object = MibScalar
netBotz_sensor_data_url_period = _NetBotz_sensor_data_url_period_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 34),
    _NetBotz_sensor_data_url_period_Type()
)
netBotz_sensor_data_url_period.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_sensor_data_url_period.setStatus("mandatory")
_NetBotz_sensor_data_url_flags_Type = Integer32
_NetBotz_sensor_data_url_flags_Object = MibScalar
netBotz_sensor_data_url_flags = _NetBotz_sensor_data_url_flags_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 35),
    _NetBotz_sensor_data_url_flags_Type()
)
netBotz_sensor_data_url_flags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_sensor_data_url_flags.setStatus("mandatory")
_NetBotz_dev_backup_smtp_Type = DisplayString
_NetBotz_dev_backup_smtp_Object = MibScalar
netBotz_dev_backup_smtp = _NetBotz_dev_backup_smtp_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 36),
    _NetBotz_dev_backup_smtp_Type()
)
netBotz_dev_backup_smtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_backup_smtp.setStatus("mandatory")
_NetBotz_dev_tertiarydns_Type = IpAddress
_NetBotz_dev_tertiarydns_Object = MibScalar
netBotz_dev_tertiarydns = _NetBotz_dev_tertiarydns_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 37),
    _NetBotz_dev_tertiarydns_Type()
)
netBotz_dev_tertiarydns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_tertiarydns.setStatus("mandatory")
_NetBotz_dev_ntp_server_Type = DisplayString
_NetBotz_dev_ntp_server_Object = MibScalar
netBotz_dev_ntp_server = _NetBotz_dev_ntp_server_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 38),
    _NetBotz_dev_ntp_server_Type()
)
netBotz_dev_ntp_server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_ntp_server.setStatus("mandatory")
_NetBotz_dev_ntp_period_Type = Integer32
_NetBotz_dev_ntp_period_Object = MibScalar
netBotz_dev_ntp_period = _NetBotz_dev_ntp_period_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 39),
    _NetBotz_dev_ntp_period_Type()
)
netBotz_dev_ntp_period.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_ntp_period.setStatus("mandatory")
_NetBotz_dev_socks_server_Type = DisplayString
_NetBotz_dev_socks_server_Object = MibScalar
netBotz_dev_socks_server = _NetBotz_dev_socks_server_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 40),
    _NetBotz_dev_socks_server_Type()
)
netBotz_dev_socks_server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_socks_server.setStatus("mandatory")
_NetBotz_dev_socks_portnum_Type = Integer32
_NetBotz_dev_socks_portnum_Object = MibScalar
netBotz_dev_socks_portnum = _NetBotz_dev_socks_portnum_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 41),
    _NetBotz_dev_socks_portnum_Type()
)
netBotz_dev_socks_portnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_socks_portnum.setStatus("mandatory")
_NetBotz_dev_socks_user_id_Type = DisplayString
_NetBotz_dev_socks_user_id_Object = MibScalar
netBotz_dev_socks_user_id = _NetBotz_dev_socks_user_id_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 42),
    _NetBotz_dev_socks_user_id_Type()
)
netBotz_dev_socks_user_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_socks_user_id.setStatus("mandatory")
_NetBotz_dev_socks_password_Type = DisplayString
_NetBotz_dev_socks_password_Object = MibScalar
netBotz_dev_socks_password = _NetBotz_dev_socks_password_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 43),
    _NetBotz_dev_socks_password_Type()
)
netBotz_dev_socks_password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_socks_password.setStatus("mandatory")
_NetBotz_alert_ftp_site_Type = DisplayString
_NetBotz_alert_ftp_site_Object = MibScalar
netBotz_alert_ftp_site = _NetBotz_alert_ftp_site_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 44),
    _NetBotz_alert_ftp_site_Type()
)
netBotz_alert_ftp_site.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_alert_ftp_site.setStatus("mandatory")
_NetBotz_alert_ftp_path_Type = DisplayString
_NetBotz_alert_ftp_path_Object = MibScalar
netBotz_alert_ftp_path = _NetBotz_alert_ftp_path_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 45),
    _NetBotz_alert_ftp_path_Type()
)
netBotz_alert_ftp_path.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_alert_ftp_path.setStatus("mandatory")
_NetBotz_alert_ftp_filename_Type = DisplayString
_NetBotz_alert_ftp_filename_Object = MibScalar
netBotz_alert_ftp_filename = _NetBotz_alert_ftp_filename_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 46),
    _NetBotz_alert_ftp_filename_Type()
)
netBotz_alert_ftp_filename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_alert_ftp_filename.setStatus("mandatory")
_NetBotz_alert_ftp_logon_Type = DisplayString
_NetBotz_alert_ftp_logon_Object = MibScalar
netBotz_alert_ftp_logon = _NetBotz_alert_ftp_logon_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 47),
    _NetBotz_alert_ftp_logon_Type()
)
netBotz_alert_ftp_logon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_alert_ftp_logon.setStatus("mandatory")
_NetBotz_sensor_ftp_site_Type = DisplayString
_NetBotz_sensor_ftp_site_Object = MibScalar
netBotz_sensor_ftp_site = _NetBotz_sensor_ftp_site_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 48),
    _NetBotz_sensor_ftp_site_Type()
)
netBotz_sensor_ftp_site.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_sensor_ftp_site.setStatus("mandatory")
_NetBotz_sensor_ftp_path_Type = DisplayString
_NetBotz_sensor_ftp_path_Object = MibScalar
netBotz_sensor_ftp_path = _NetBotz_sensor_ftp_path_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 49),
    _NetBotz_sensor_ftp_path_Type()
)
netBotz_sensor_ftp_path.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_sensor_ftp_path.setStatus("mandatory")
_NetBotz_sensor_ftp_filename_Type = DisplayString
_NetBotz_sensor_ftp_filename_Object = MibScalar
netBotz_sensor_ftp_filename = _NetBotz_sensor_ftp_filename_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 50),
    _NetBotz_sensor_ftp_filename_Type()
)
netBotz_sensor_ftp_filename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_sensor_ftp_filename.setStatus("mandatory")
_NetBotz_sensor_ftp_logon_Type = DisplayString
_NetBotz_sensor_ftp_logon_Object = MibScalar
netBotz_sensor_ftp_logon = _NetBotz_sensor_ftp_logon_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 51),
    _NetBotz_sensor_ftp_logon_Type()
)
netBotz_sensor_ftp_logon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_sensor_ftp_logon.setStatus("mandatory")
_NetBotz_sensor_ftp_period_Type = Integer32
_NetBotz_sensor_ftp_period_Object = MibScalar
netBotz_sensor_ftp_period = _NetBotz_sensor_ftp_period_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 52),
    _NetBotz_sensor_ftp_period_Type()
)
netBotz_sensor_ftp_period.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_sensor_ftp_period.setStatus("mandatory")
_NetBotz_use_syslog_Type = Integer32
_NetBotz_use_syslog_Object = MibScalar
netBotz_use_syslog = _NetBotz_use_syslog_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 53),
    _NetBotz_use_syslog_Type()
)
netBotz_use_syslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_use_syslog.setStatus("mandatory")
_NetBotz_syslog_address_Type = DisplayString
_NetBotz_syslog_address_Object = MibScalar
netBotz_syslog_address = _NetBotz_syslog_address_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 54),
    _NetBotz_syslog_address_Type()
)
netBotz_syslog_address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_syslog_address.setStatus("mandatory")
_NetBotz_syslog_facility_Type = Integer32
_NetBotz_syslog_facility_Object = MibScalar
netBotz_syslog_facility = _NetBotz_syslog_facility_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 55),
    _NetBotz_syslog_facility_Type()
)
netBotz_syslog_facility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_syslog_facility.setStatus("mandatory")
_NetBotz_color_balance_Type = DisplayString
_NetBotz_color_balance_Object = MibScalar
netBotz_color_balance = _NetBotz_color_balance_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 56),
    _NetBotz_color_balance_Type()
)
netBotz_color_balance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_color_balance.setStatus("mandatory")
_NetBotz_addonapp_ObjectIdentity = ObjectIdentity
netBotz_addonapp = _NetBotz_addonapp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 60)
)
_Device_crawlers_trap_target_index_ObjectIdentity = ObjectIdentity
device_crawlers_trap_target_index = _Device_crawlers_trap_target_index_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 60, 2)
)
_Branch_checker_trap_target_index_ObjectIdentity = ObjectIdentity
branch_checker_trap_target_index = _Branch_checker_trap_target_index_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 60, 3)
)
_Vendor_netBotz_ObjectIdentity = ObjectIdentity
vendor_netBotz = _Vendor_netBotz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 60, 5528)
)
_Device_crawlers_trap_ObjectIdentity = ObjectIdentity
device_crawlers_trap = _Device_crawlers_trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 60, 5528, 2)
)
_Branch_checker_trap_ObjectIdentity = ObjectIdentity
branch_checker_trap = _Branch_checker_trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 60, 5528, 3)
)
_NetBotz_addonapp_trap_ObjectIdentity = ObjectIdentity
netBotz_addonapp_trap = _NetBotz_addonapp_trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 61)
)
_Device_crawlers_trap_attrib_ObjectIdentity = ObjectIdentity
device_crawlers_trap_attrib = _Device_crawlers_trap_attrib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 61, 2)
)
_Device_crawlers_trap_index_Type = Integer32
_Device_crawlers_trap_index_Object = MibScalar
device_crawlers_trap_index = _Device_crawlers_trap_index_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 2, 20),
    _Device_crawlers_trap_index_Type()
)
device_crawlers_trap_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_crawlers_trap_index.setStatus("mandatory")
_Device_crawlers_trap_address_Type = IpAddress
_Device_crawlers_trap_address_Object = MibScalar
device_crawlers_trap_address = _Device_crawlers_trap_address_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 2, 21),
    _Device_crawlers_trap_address_Type()
)
device_crawlers_trap_address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_crawlers_trap_address.setStatus("mandatory")
_Device_crawlers_trap_oid_Type = ObjectIdentifier
_Device_crawlers_trap_oid_Object = MibScalar
device_crawlers_trap_oid = _Device_crawlers_trap_oid_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 2, 22),
    _Device_crawlers_trap_oid_Type()
)
device_crawlers_trap_oid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_crawlers_trap_oid.setStatus("mandatory")
_Device_crawlers_trap_botoid_Type = ObjectIdentifier
_Device_crawlers_trap_botoid_Object = MibScalar
device_crawlers_trap_botoid = _Device_crawlers_trap_botoid_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 2, 23),
    _Device_crawlers_trap_botoid_Type()
)
device_crawlers_trap_botoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_crawlers_trap_botoid.setStatus("mandatory")
_Device_crawlers_trap_value_Type = Integer32
_Device_crawlers_trap_value_Object = MibScalar
device_crawlers_trap_value = _Device_crawlers_trap_value_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 2, 24),
    _Device_crawlers_trap_value_Type()
)
device_crawlers_trap_value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_crawlers_trap_value.setStatus("mandatory")
_Device_crawlers_trap_stringvalue_Type = DisplayString
_Device_crawlers_trap_stringvalue_Object = MibScalar
device_crawlers_trap_stringvalue = _Device_crawlers_trap_stringvalue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 2, 25),
    _Device_crawlers_trap_stringvalue_Type()
)
device_crawlers_trap_stringvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_crawlers_trap_stringvalue.setStatus("mandatory")
_Device_crawlers_trap_date_Type = Integer32
_Device_crawlers_trap_date_Object = MibScalar
device_crawlers_trap_date = _Device_crawlers_trap_date_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 2, 26),
    _Device_crawlers_trap_date_Type()
)
device_crawlers_trap_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_crawlers_trap_date.setStatus("mandatory")
_Device_crawlers_trap_attrib_index_Type = Integer32
_Device_crawlers_trap_attrib_index_Object = MibScalar
device_crawlers_trap_attrib_index = _Device_crawlers_trap_attrib_index_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 2, 27),
    _Device_crawlers_trap_attrib_index_Type()
)
device_crawlers_trap_attrib_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_crawlers_trap_attrib_index.setStatus("mandatory")
_Device_crawlers_crawlers_trap_desc_Type = DisplayString
_Device_crawlers_crawlers_trap_desc_Object = MibScalar
device_crawlers_crawlers_trap_desc = _Device_crawlers_crawlers_trap_desc_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 2, 28),
    _Device_crawlers_crawlers_trap_desc_Type()
)
device_crawlers_crawlers_trap_desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_crawlers_crawlers_trap_desc.setStatus("mandatory")
_Branch_checker_trap_attrib_ObjectIdentity = ObjectIdentity
branch_checker_trap_attrib = _Branch_checker_trap_attrib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 61, 3)
)
_Branch_checker_trap_index_Type = Integer32
_Branch_checker_trap_index_Object = MibScalar
branch_checker_trap_index = _Branch_checker_trap_index_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 3, 20),
    _Branch_checker_trap_index_Type()
)
branch_checker_trap_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branch_checker_trap_index.setStatus("mandatory")
_Branch_checker_trap_address_Type = IpAddress
_Branch_checker_trap_address_Object = MibScalar
branch_checker_trap_address = _Branch_checker_trap_address_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 3, 21),
    _Branch_checker_trap_address_Type()
)
branch_checker_trap_address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branch_checker_trap_address.setStatus("mandatory")
_Branch_checker_trap_oid_Type = ObjectIdentifier
_Branch_checker_trap_oid_Object = MibScalar
branch_checker_trap_oid = _Branch_checker_trap_oid_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 3, 22),
    _Branch_checker_trap_oid_Type()
)
branch_checker_trap_oid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branch_checker_trap_oid.setStatus("mandatory")
_Branch_checker_trap_botoid_Type = ObjectIdentifier
_Branch_checker_trap_botoid_Object = MibScalar
branch_checker_trap_botoid = _Branch_checker_trap_botoid_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 3, 23),
    _Branch_checker_trap_botoid_Type()
)
branch_checker_trap_botoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branch_checker_trap_botoid.setStatus("mandatory")
_Branch_checker_trap_value_Type = Integer32
_Branch_checker_trap_value_Object = MibScalar
branch_checker_trap_value = _Branch_checker_trap_value_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 3, 24),
    _Branch_checker_trap_value_Type()
)
branch_checker_trap_value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branch_checker_trap_value.setStatus("mandatory")
_Branch_checker_trap_stringvalue_Type = DisplayString
_Branch_checker_trap_stringvalue_Object = MibScalar
branch_checker_trap_stringvalue = _Branch_checker_trap_stringvalue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 3, 25),
    _Branch_checker_trap_stringvalue_Type()
)
branch_checker_trap_stringvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branch_checker_trap_stringvalue.setStatus("mandatory")
_Branch_checker_trap_date_Type = Integer32
_Branch_checker_trap_date_Object = MibScalar
branch_checker_trap_date = _Branch_checker_trap_date_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 3, 26),
    _Branch_checker_trap_date_Type()
)
branch_checker_trap_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branch_checker_trap_date.setStatus("mandatory")
_Branch_checker_trap_attrib_index_Type = Integer32
_Branch_checker_trap_attrib_index_Object = MibScalar
branch_checker_trap_attrib_index = _Branch_checker_trap_attrib_index_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 3, 27),
    _Branch_checker_trap_attrib_index_Type()
)
branch_checker_trap_attrib_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branch_checker_trap_attrib_index.setStatus("mandatory")
_Branch_checker_trap_desc_Type = DisplayString
_Branch_checker_trap_desc_Object = MibScalar
branch_checker_trap_desc = _Branch_checker_trap_desc_Object(
    (1, 3, 6, 1, 4, 1, 5528, 61, 3, 28),
    _Branch_checker_trap_desc_Type()
)
branch_checker_trap_desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branch_checker_trap_desc.setStatus("mandatory")

# Managed Objects groups


# Notification objects

netBotz_prd_bot_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 0, 1)
)
netBotz_prd_bot_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 0, 2)
)
netBotz_prd_bot_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 0, 3)
)
netBotz_prd_bot_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_offline_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 0, 4)
)
netBotz_prd_bot_offline_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_offline_trap.setStatus(
        ""
    )

netBotz_prd_bot_online_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 0, 5)
)
netBotz_prd_bot_online_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_online_trap.setStatus(
        ""
    )

netBotz_prd_crl_ping_offline_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 3, 0, 4)
)
netBotz_prd_crl_ping_offline_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_ping_offline_trap.setStatus(
        ""
    )

netBotz_prd_crl_ping_online_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 3, 0, 5)
)
netBotz_prd_crl_ping_online_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_ping_online_trap.setStatus(
        ""
    )

netBotz_prd_crl_uptime_online_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 8, 0, 5)
)
netBotz_prd_crl_uptime_online_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_uptime_online_trap.setStatus(
        ""
    )

netBotz_prd_crl_snmp_offline_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 9, 0, 4)
)
netBotz_prd_crl_snmp_offline_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_snmp_offline_trap.setStatus(
        ""
    )

netBotz_prd_crl_snmp_online_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 9, 0, 5)
)
netBotz_prd_crl_snmp_online_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_snmp_online_trap.setStatus(
        ""
    )

netBotz_prd_crl_opstatus_mismatch_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2, 6, 0, 1)
)
netBotz_prd_crl_opstatus_mismatch_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_opstatus_mismatch_trap.setStatus(
        ""
    )

netBotz_prd_crl_opstatus_match_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2, 6, 0, 2)
)
netBotz_prd_crl_opstatus_match_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_opstatus_match_trap.setStatus(
        ""
    )

netBotz_prd_crl_opstatus_offline_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2, 6, 0, 4)
)
netBotz_prd_crl_opstatus_offline_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_opstatus_offline_trap.setStatus(
        ""
    )

netBotz_prd_bot_temperature_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 1, 0, 1)
)
netBotz_prd_bot_temperature_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_temperature_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_temperature_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 1, 0, 2)
)
netBotz_prd_bot_temperature_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_temperature_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_temperature_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 1, 0, 3)
)
netBotz_prd_bot_temperature_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_temperature_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_humidity_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 2, 0, 1)
)
netBotz_prd_bot_humidity_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_humidity_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_humidity_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 2, 0, 2)
)
netBotz_prd_bot_humidity_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_humidity_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_humidity_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 2, 0, 3)
)
netBotz_prd_bot_humidity_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_humidity_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_airflow_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 3, 0, 1)
)
netBotz_prd_bot_airflow_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_airflow_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_airflow_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 3, 0, 3)
)
netBotz_prd_bot_airflow_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_airflow_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_audio_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 4, 0, 2)
)
netBotz_prd_bot_audio_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_audio_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_audio_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 4, 0, 3)
)
netBotz_prd_bot_audio_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_audio_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_door_trap_tripped = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 5, 0, 2)
)
netBotz_prd_bot_door_trap_tripped.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_door_trap_tripped.setStatus(
        ""
    )

netBotz_prd_bot_door_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 5, 0, 3)
)
netBotz_prd_bot_door_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_door_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp1_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 6, 0, 1)
)
netBotz_prd_bot_amp1_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp1_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp1_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 6, 0, 2)
)
netBotz_prd_bot_amp1_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp1_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp1_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 6, 0, 3)
)
netBotz_prd_bot_amp1_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp1_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp1_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 6, 0, 6)
)
netBotz_prd_bot_amp1_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp1_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_amp1_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 6, 0, 7)
)
netBotz_prd_bot_amp1_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp1_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_amp2_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 7, 0, 1)
)
netBotz_prd_bot_amp2_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp2_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp2_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 7, 0, 2)
)
netBotz_prd_bot_amp2_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp2_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp2_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 7, 0, 3)
)
netBotz_prd_bot_amp2_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp2_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp2_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 7, 0, 6)
)
netBotz_prd_bot_amp2_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp2_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_amp2_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 7, 0, 7)
)
netBotz_prd_bot_amp2_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp2_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_amp3_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 8, 0, 1)
)
netBotz_prd_bot_amp3_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp3_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp3_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 8, 0, 2)
)
netBotz_prd_bot_amp3_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp3_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp3_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 8, 0, 3)
)
netBotz_prd_bot_amp3_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp3_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp3_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 8, 0, 6)
)
netBotz_prd_bot_amp3_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp3_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_amp3_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 8, 0, 7)
)
netBotz_prd_bot_amp3_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp3_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_amp4_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 9, 0, 1)
)
netBotz_prd_bot_amp4_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp4_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp4_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 9, 0, 2)
)
netBotz_prd_bot_amp4_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp4_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp4_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 9, 0, 3)
)
netBotz_prd_bot_amp4_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp4_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp4_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 9, 0, 6)
)
netBotz_prd_bot_amp4_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp4_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_amp4_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 9, 0, 7)
)
netBotz_prd_bot_amp4_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp4_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_amp_total_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 10, 0, 1)
)
netBotz_prd_bot_amp_total_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp_total_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp_total_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 10, 0, 2)
)
netBotz_prd_bot_amp_total_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp_total_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp_total_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 10, 0, 3)
)
netBotz_prd_bot_amp_total_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp_total_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp1_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 11, 0, 1)
)
netBotz_prd_bot_ext_temp1_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp1_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 11, 0, 2)
)
netBotz_prd_bot_ext_temp1_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp1_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 11, 0, 3)
)
netBotz_prd_bot_ext_temp1_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp1_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 11, 0, 6)
)
netBotz_prd_bot_ext_temp1_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp1_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 11, 0, 7)
)
netBotz_prd_bot_ext_temp1_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp2_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 12, 0, 1)
)
netBotz_prd_bot_ext_temp2_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp2_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 12, 0, 2)
)
netBotz_prd_bot_ext_temp2_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp2_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 12, 0, 3)
)
netBotz_prd_bot_ext_temp2_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp2_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 12, 0, 6)
)
netBotz_prd_bot_ext_temp2_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp2_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 12, 0, 7)
)
netBotz_prd_bot_ext_temp2_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp3_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 13, 0, 1)
)
netBotz_prd_bot_ext_temp3_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp3_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 13, 0, 2)
)
netBotz_prd_bot_ext_temp3_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp3_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 13, 0, 3)
)
netBotz_prd_bot_ext_temp3_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp3_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 13, 0, 6)
)
netBotz_prd_bot_ext_temp3_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp3_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 13, 0, 7)
)
netBotz_prd_bot_ext_temp3_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp4_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 14, 0, 1)
)
netBotz_prd_bot_ext_temp4_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp4_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 14, 0, 2)
)
netBotz_prd_bot_ext_temp4_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp4_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 14, 0, 3)
)
netBotz_prd_bot_ext_temp4_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp4_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 14, 0, 6)
)
netBotz_prd_bot_ext_temp4_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp4_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 14, 0, 7)
)
netBotz_prd_bot_ext_temp4_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry1_triggered_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 15, 0, 2)
)
netBotz_prd_bot_ext_dry1_triggered_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry1_triggered_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry1_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 15, 0, 3)
)
netBotz_prd_bot_ext_dry1_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry1_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry2_triggered_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 16, 0, 2)
)
netBotz_prd_bot_ext_dry2_triggered_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry2_triggered_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry2_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 16, 0, 3)
)
netBotz_prd_bot_ext_dry2_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry2_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry3_triggered_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 17, 0, 2)
)
netBotz_prd_bot_ext_dry3_triggered_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry3_triggered_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry3_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 17, 0, 3)
)
netBotz_prd_bot_ext_dry3_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry3_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry4_triggered_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 18, 0, 2)
)
netBotz_prd_bot_ext_dry4_triggered_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry4_triggered_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry4_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 18, 0, 3)
)
netBotz_prd_bot_ext_dry4_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry4_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp5_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 19, 0, 1)
)
netBotz_prd_bot_amp5_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp5_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp5_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 19, 0, 2)
)
netBotz_prd_bot_amp5_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp5_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp5_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 19, 0, 3)
)
netBotz_prd_bot_amp5_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp5_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp5_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 19, 0, 6)
)
netBotz_prd_bot_amp5_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp5_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_amp5_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 19, 0, 7)
)
netBotz_prd_bot_amp5_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp5_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_amp6_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 20, 0, 1)
)
netBotz_prd_bot_amp6_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp6_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp6_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 20, 0, 2)
)
netBotz_prd_bot_amp6_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp6_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp6_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 20, 0, 3)
)
netBotz_prd_bot_amp6_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp6_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp6_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 20, 0, 6)
)
netBotz_prd_bot_amp6_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp6_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_amp6_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 20, 0, 7)
)
netBotz_prd_bot_amp6_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp6_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_amp7_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 21, 0, 1)
)
netBotz_prd_bot_amp7_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp7_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp7_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 21, 0, 2)
)
netBotz_prd_bot_amp7_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp7_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp7_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 21, 0, 3)
)
netBotz_prd_bot_amp7_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp7_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp7_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 21, 0, 6)
)
netBotz_prd_bot_amp7_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp7_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_amp7_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 21, 0, 7)
)
netBotz_prd_bot_amp7_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp7_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp5_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 22, 0, 1)
)
netBotz_prd_bot_ext_temp5_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp5_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp5_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 22, 0, 2)
)
netBotz_prd_bot_ext_temp5_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp5_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp5_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 22, 0, 3)
)
netBotz_prd_bot_ext_temp5_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp5_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp5_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 22, 0, 6)
)
netBotz_prd_bot_ext_temp5_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp5_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp5_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 22, 0, 7)
)
netBotz_prd_bot_ext_temp5_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp5_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp6_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 23, 0, 1)
)
netBotz_prd_bot_ext_temp6_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp6_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp6_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 23, 0, 2)
)
netBotz_prd_bot_ext_temp6_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp6_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp6_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 23, 0, 3)
)
netBotz_prd_bot_ext_temp6_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp6_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp6_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 23, 0, 6)
)
netBotz_prd_bot_ext_temp6_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp6_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp6_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 23, 0, 7)
)
netBotz_prd_bot_ext_temp6_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp6_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp7_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 24, 0, 1)
)
netBotz_prd_bot_ext_temp7_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp7_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp7_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 24, 0, 2)
)
netBotz_prd_bot_ext_temp7_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp7_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp7_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 24, 0, 3)
)
netBotz_prd_bot_ext_temp7_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp7_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp7_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 24, 0, 6)
)
netBotz_prd_bot_ext_temp7_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp7_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp7_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 24, 0, 7)
)
netBotz_prd_bot_ext_temp7_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp7_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry5_triggered_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 25, 0, 2)
)
netBotz_prd_bot_ext_dry5_triggered_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry5_triggered_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry5_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 25, 0, 3)
)
netBotz_prd_bot_ext_dry5_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry5_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry6_triggered_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 26, 0, 2)
)
netBotz_prd_bot_ext_dry6_triggered_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry6_triggered_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry6_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 26, 0, 3)
)
netBotz_prd_bot_ext_dry6_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry6_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry7_triggered_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 27, 0, 2)
)
netBotz_prd_bot_ext_dry7_triggered_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry7_triggered_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry7_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 27, 0, 3)
)
netBotz_prd_bot_ext_dry7_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry7_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_camera_motion_trap_tripped = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 28, 0, 2)
)
netBotz_prd_bot_camera_motion_trap_tripped.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_camera_motion_trap_tripped.setStatus(
        ""
    )

netBotz_prd_bot_camera_motion_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 28, 0, 3)
)
netBotz_prd_bot_camera_motion_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_camera_motion_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi1_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 29, 0, 1)
)
netBotz_prd_bot_ext_humi1_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi1_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi1_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 29, 0, 2)
)
netBotz_prd_bot_ext_humi1_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi1_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi1_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 29, 0, 3)
)
netBotz_prd_bot_ext_humi1_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi1_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi1_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 29, 0, 6)
)
netBotz_prd_bot_ext_humi1_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi1_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi1_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 29, 0, 7)
)
netBotz_prd_bot_ext_humi1_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi1_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi2_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 30, 0, 1)
)
netBotz_prd_bot_ext_humi2_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi2_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi2_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 30, 0, 2)
)
netBotz_prd_bot_ext_humi2_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi2_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi2_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 30, 0, 3)
)
netBotz_prd_bot_ext_humi2_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi2_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi2_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 30, 0, 6)
)
netBotz_prd_bot_ext_humi2_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi2_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi2_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 30, 0, 7)
)
netBotz_prd_bot_ext_humi2_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi2_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi3_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 31, 0, 1)
)
netBotz_prd_bot_ext_humi3_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi3_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi3_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 31, 0, 2)
)
netBotz_prd_bot_ext_humi3_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi3_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi3_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 31, 0, 3)
)
netBotz_prd_bot_ext_humi3_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi3_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi3_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 31, 0, 6)
)
netBotz_prd_bot_ext_humi3_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi3_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi3_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 31, 0, 7)
)
netBotz_prd_bot_ext_humi3_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi3_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi4_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 32, 0, 1)
)
netBotz_prd_bot_ext_humi4_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi4_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi4_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 32, 0, 2)
)
netBotz_prd_bot_ext_humi4_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi4_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi4_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 32, 0, 3)
)
netBotz_prd_bot_ext_humi4_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi4_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi4_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 32, 0, 6)
)
netBotz_prd_bot_ext_humi4_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi4_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi4_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 32, 0, 7)
)
netBotz_prd_bot_ext_humi4_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi4_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi5_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 33, 0, 1)
)
netBotz_prd_bot_ext_humi5_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi5_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi5_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 33, 0, 2)
)
netBotz_prd_bot_ext_humi5_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi5_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi5_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 33, 0, 3)
)
netBotz_prd_bot_ext_humi5_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi5_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi5_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 33, 0, 6)
)
netBotz_prd_bot_ext_humi5_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi5_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi5_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 33, 0, 7)
)
netBotz_prd_bot_ext_humi5_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi5_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi6_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 34, 0, 1)
)
netBotz_prd_bot_ext_humi6_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi6_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi6_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 34, 0, 2)
)
netBotz_prd_bot_ext_humi6_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi6_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi6_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 34, 0, 3)
)
netBotz_prd_bot_ext_humi6_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi6_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi6_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 34, 0, 6)
)
netBotz_prd_bot_ext_humi6_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi6_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi6_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 34, 0, 7)
)
netBotz_prd_bot_ext_humi6_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi6_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi7_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 35, 0, 1)
)
netBotz_prd_bot_ext_humi7_low_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi7_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi7_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 35, 0, 2)
)
netBotz_prd_bot_ext_humi7_high_trap.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi7_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi7_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 35, 0, 3)
)
netBotz_prd_bot_ext_humi7_trap_clear.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi7_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi7_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 35, 0, 6)
)
netBotz_prd_bot_ext_humi7_sensor_unplugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi7_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_humi7_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 35, 0, 7)
)
netBotz_prd_bot_ext_humi7_sensor_replugged.setObjects(
      *(("NETBOTZ-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_humi7_sensor_replugged.setStatus(
        ""
    )

netBotz_device_crawlers_value_low_alert_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 60, 5528, 2, 0, 1)
)
netBotz_device_crawlers_value_low_alert_trap.setObjects(
      *(("NETBOTZ-MIB", "device_crawlers_trap_index"),
        ("NETBOTZ-MIB", "device_crawlers_trap_address"),
        ("NETBOTZ-MIB", "device_crawlers_trap_oid"),
        ("NETBOTZ-MIB", "device_crawlers_trap_botoid"),
        ("NETBOTZ-MIB", "device_crawlers_trap_value"),
        ("NETBOTZ-MIB", "device_crawlers_trap_stringvalue"),
        ("NETBOTZ-MIB", "device_crawlers_trap_date"),
        ("NETBOTZ-MIB", "device_crawlers_trap_attrib"),
        ("NETBOTZ-MIB", "device_crawlers_trap_desc"))
)
if mibBuilder.loadTexts:
    netBotz_device_crawlers_value_low_alert_trap.setStatus(
        ""
    )

netBotz_device_crawlers_value_high_alert_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 60, 5528, 2, 0, 2)
)
netBotz_device_crawlers_value_high_alert_trap.setObjects(
      *(("NETBOTZ-MIB", "device_crawlers_trap_index"),
        ("NETBOTZ-MIB", "device_crawlers_trap_address"),
        ("NETBOTZ-MIB", "device_crawlers_trap_oid"),
        ("NETBOTZ-MIB", "device_crawlers_trap_botoid"),
        ("NETBOTZ-MIB", "device_crawlers_trap_value"),
        ("NETBOTZ-MIB", "device_crawlers_trap_stringvalue"),
        ("NETBOTZ-MIB", "device_crawlers_trap_date"),
        ("NETBOTZ-MIB", "device_crawlers_trap_attrib"),
        ("NETBOTZ-MIB", "device_crawlers_trap_desc"))
)
if mibBuilder.loadTexts:
    netBotz_device_crawlers_value_high_alert_trap.setStatus(
        ""
    )

netBotz_device_crawlers_clear_alert_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 60, 5528, 2, 0, 3)
)
netBotz_device_crawlers_clear_alert_trap.setObjects(
      *(("NETBOTZ-MIB", "device_crawlers_trap_index"),
        ("NETBOTZ-MIB", "device_crawlers_trap_address"),
        ("NETBOTZ-MIB", "device_crawlers_trap_oid"),
        ("NETBOTZ-MIB", "device_crawlers_trap_botoid"),
        ("NETBOTZ-MIB", "device_crawlers_trap_value"),
        ("NETBOTZ-MIB", "device_crawlers_trap_stringvalue"),
        ("NETBOTZ-MIB", "device_crawlers_trap_date"),
        ("NETBOTZ-MIB", "device_crawlers_trap_attrib"),
        ("NETBOTZ-MIB", "device_crawlers_trap_desc"))
)
if mibBuilder.loadTexts:
    netBotz_device_crawlers_clear_alert_trap.setStatus(
        ""
    )

netBotz_device_crawlers_offline_alert_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 60, 5528, 2, 0, 4)
)
netBotz_device_crawlers_offline_alert_trap.setObjects(
      *(("NETBOTZ-MIB", "device_crawlers_trap_index"),
        ("NETBOTZ-MIB", "device_crawlers_trap_address"),
        ("NETBOTZ-MIB", "device_crawlers_trap_oid"),
        ("NETBOTZ-MIB", "device_crawlers_trap_botoid"),
        ("NETBOTZ-MIB", "device_crawlers_trap_value"),
        ("NETBOTZ-MIB", "device_crawlers_trap_stringvalue"),
        ("NETBOTZ-MIB", "device_crawlers_trap_date"),
        ("NETBOTZ-MIB", "device_crawlers_trap_attrib"),
        ("NETBOTZ-MIB", "device_crawlers_trap_desc"))
)
if mibBuilder.loadTexts:
    netBotz_device_crawlers_offline_alert_trap.setStatus(
        ""
    )

netBotz_device_crawlers_online_alert_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 60, 5528, 2, 0, 5)
)
netBotz_device_crawlers_online_alert_trap.setObjects(
      *(("NETBOTZ-MIB", "device_crawlers_trap_index"),
        ("NETBOTZ-MIB", "device_crawlers_trap_address"),
        ("NETBOTZ-MIB", "device_crawlers_trap_oid"),
        ("NETBOTZ-MIB", "device_crawlers_trap_botoid"),
        ("NETBOTZ-MIB", "device_crawlers_trap_value"),
        ("NETBOTZ-MIB", "device_crawlers_trap_stringvalue"),
        ("NETBOTZ-MIB", "device_crawlers_trap_date"),
        ("NETBOTZ-MIB", "device_crawlers_trap_attrib"),
        ("NETBOTZ-MIB", "device_crawlers_trap_desc"))
)
if mibBuilder.loadTexts:
    netBotz_device_crawlers_online_alert_trap.setStatus(
        ""
    )

netBotz_device_crawlers_ifopstatus_alert_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 60, 5528, 2, 0, 8)
)
netBotz_device_crawlers_ifopstatus_alert_trap.setObjects(
      *(("NETBOTZ-MIB", "device_crawlers_trap_index"),
        ("NETBOTZ-MIB", "device_crawlers_trap_address"),
        ("NETBOTZ-MIB", "device_crawlers_trap_oid"),
        ("NETBOTZ-MIB", "device_crawlers_trap_botoid"),
        ("NETBOTZ-MIB", "device_crawlers_trap_value"),
        ("NETBOTZ-MIB", "device_crawlers_trap_stringvalue"),
        ("NETBOTZ-MIB", "device_crawlers_trap_date"),
        ("NETBOTZ-MIB", "device_crawlers_trap_attrib"),
        ("NETBOTZ-MIB", "device_crawlers_trap_desc"))
)
if mibBuilder.loadTexts:
    netBotz_device_crawlers_ifopstatus_alert_trap.setStatus(
        ""
    )

netBotz_branch_checker_clear_alert_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 60, 5528, 3, 0, 3)
)
netBotz_branch_checker_clear_alert_trap.setObjects(
      *(("NETBOTZ-MIB", "branch_checker_trap_index"),
        ("NETBOTZ-MIB", "branch_checker_trap_address"),
        ("NETBOTZ-MIB", "branch_checker_trap_oid"),
        ("NETBOTZ-MIB", "branch_checker_trap_botoid"),
        ("NETBOTZ-MIB", "branch_checker_trap_value"),
        ("NETBOTZ-MIB", "branch_checker_trap_stringvalue"),
        ("NETBOTZ-MIB", "branch_checker_trap_date"),
        ("NETBOTZ-MIB", "branch_checker_trap_attrib"),
        ("NETBOTZ-MIB", "branch_checker_trap_desc"))
)
if mibBuilder.loadTexts:
    netBotz_branch_checker_clear_alert_trap.setStatus(
        ""
    )

netBotz_branch_checker_offline_alert_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 60, 5528, 3, 0, 4)
)
netBotz_branch_checker_offline_alert_trap.setObjects(
      *(("NETBOTZ-MIB", "branch_checker_trap_index"),
        ("NETBOTZ-MIB", "branch_checker_trap_address"),
        ("NETBOTZ-MIB", "branch_checker_trap_oid"),
        ("NETBOTZ-MIB", "branch_checker_trap_botoid"),
        ("NETBOTZ-MIB", "branch_checker_trap_value"),
        ("NETBOTZ-MIB", "branch_checker_trap_stringvalue"),
        ("NETBOTZ-MIB", "branch_checker_trap_date"),
        ("NETBOTZ-MIB", "branch_checker_trap_attrib"),
        ("NETBOTZ-MIB", "branch_checker_trap_desc"))
)
if mibBuilder.loadTexts:
    netBotz_branch_checker_offline_alert_trap.setStatus(
        ""
    )

netBotz_branch_checker_online_alert_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 60, 5528, 3, 0, 5)
)
netBotz_branch_checker_online_alert_trap.setObjects(
      *(("NETBOTZ-MIB", "branch_checker_trap_index"),
        ("NETBOTZ-MIB", "branch_checker_trap_address"),
        ("NETBOTZ-MIB", "branch_checker_trap_oid"),
        ("NETBOTZ-MIB", "branch_checker_trap_botoid"),
        ("NETBOTZ-MIB", "branch_checker_trap_value"),
        ("NETBOTZ-MIB", "branch_checker_trap_stringvalue"),
        ("NETBOTZ-MIB", "branch_checker_trap_date"),
        ("NETBOTZ-MIB", "branch_checker_trap_attrib"),
        ("NETBOTZ-MIB", "branch_checker_trap_desc"))
)
if mibBuilder.loadTexts:
    netBotz_branch_checker_online_alert_trap.setStatus(
        ""
    )

netBotz_branch_checker_target_error_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 60, 5528, 3, 0, 12)
)
netBotz_branch_checker_target_error_trap.setObjects(
      *(("NETBOTZ-MIB", "branch_checker_trap_index"),
        ("NETBOTZ-MIB", "branch_checker_trap_address"),
        ("NETBOTZ-MIB", "branch_checker_trap_oid"),
        ("NETBOTZ-MIB", "branch_checker_trap_botoid"),
        ("NETBOTZ-MIB", "branch_checker_trap_value"),
        ("NETBOTZ-MIB", "branch_checker_trap_stringvalue"),
        ("NETBOTZ-MIB", "branch_checker_trap_date"),
        ("NETBOTZ-MIB", "branch_checker_trap_attrib"),
        ("NETBOTZ-MIB", "branch_checker_trap_desc"))
)
if mibBuilder.loadTexts:
    netBotz_branch_checker_target_error_trap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETBOTZ-MIB",
    **{"netBotz": netBotz,
       "netBotz-reg": netBotz_reg,
       "netBotz-generic": netBotz_generic,
       "netBotz-products": netBotz_products,
       "netBotz-prd-bot": netBotz_prd_bot,
       "netBotz-prd-bot-low-trap": netBotz_prd_bot_low_trap,
       "netBotz-prd-bot-high-trap": netBotz_prd_bot_high_trap,
       "netBotz-prd-bot-trap-clear": netBotz_prd_bot_trap_clear,
       "netBotz-prd-bot-offline-trap": netBotz_prd_bot_offline_trap,
       "netBotz-prd-bot-online-trap": netBotz_prd_bot_online_trap,
       "netBotz-prd-bot-temp": netBotz_prd_bot_temp,
       "netBotz-prd-bot-humidity": netBotz_prd_bot_humidity,
       "netBotz-prd-bot-airflow": netBotz_prd_bot_airflow,
       "netBotz-prd-bot-audio": netBotz_prd_bot_audio,
       "netBotz-prd-bot-doorajar": netBotz_prd_bot_doorajar,
       "netBotz-prd-bot-temp-min": netBotz_prd_bot_temp_min,
       "netBotz-prd-bot-temp-max": netBotz_prd_bot_temp_max,
       "netBotz-prd-bot-humidity-min": netBotz_prd_bot_humidity_min,
       "netBotz-prd-bot-humidity-max": netBotz_prd_bot_humidity_max,
       "netBotz-prd-bot-airflow-mins": netBotz_prd_bot_airflow_mins,
       "netBotz-prd-bot-audio-secs": netBotz_prd_bot_audio_secs,
       "netBotz-prd-bot-temp-enabled": netBotz_prd_bot_temp_enabled,
       "netBotz-prd-bot-hum-enabled": netBotz_prd_bot_hum_enabled,
       "netBotz-prd-bot-air-enabled": netBotz_prd_bot_air_enabled,
       "netBotz-prd-bot-audio-enabled": netBotz_prd_bot_audio_enabled,
       "netBotz-prd-bot-switch-state": netBotz_prd_bot_switch_state,
       "netBotz-prd-bot-switch-enabled": netBotz_prd_bot_switch_enabled,
       "netBotz-prd-bot-audio-level": netBotz_prd_bot_audio_level,
       "netBotz-prd-bot-trap-index": netBotz_prd_bot_trap_index,
       "netBotz-prd-bot-trap-address": netBotz_prd_bot_trap_address,
       "netBotz-prd-bot-trap-oid": netBotz_prd_bot_trap_oid,
       "netBotz-prd-bot-trap-value": netBotz_prd_bot_trap_value,
       "netBotz-prd-bot-trap-date": netBotz_prd_bot_trap_date,
       "netBotz-prd-bot-refresh": netBotz_prd_bot_refresh,
       "netBotz-prd-bot-airflow-level": netBotz_prd_bot_airflow_level,
       "netBotz-prd-bot-doorpic-count": netBotz_prd_bot_doorpic_count,
       "netBotz-prd-bot-amps1": netBotz_prd_bot_amps1,
       "netBotz-prd-bot-amps1-enabled": netBotz_prd_bot_amps1_enabled,
       "netBotz-prd-bot-amps1-min": netBotz_prd_bot_amps1_min,
       "netBotz-prd-bot-amps1-max": netBotz_prd_bot_amps1_max,
       "netBotz-prd-bot-amps2": netBotz_prd_bot_amps2,
       "netBotz-prd-bot-amps2-enabled": netBotz_prd_bot_amps2_enabled,
       "netBotz-prd-bot-amps2-min": netBotz_prd_bot_amps2_min,
       "netBotz-prd-bot-amps2-max": netBotz_prd_bot_amps2_max,
       "netBotz-prd-bot-amps3": netBotz_prd_bot_amps3,
       "netBotz-prd-bot-amps3-enabled": netBotz_prd_bot_amps3_enabled,
       "netBotz-prd-bot-amps3-min": netBotz_prd_bot_amps3_min,
       "netBotz-prd-bot-amps3-max": netBotz_prd_bot_amps3_max,
       "netBotz-prd-bot-amps-total": netBotz_prd_bot_amps_total,
       "netBotz-prd-bot-amps-total-enabled": netBotz_prd_bot_amps_total_enabled,
       "netBotz-prd-bot-amps-total-min": netBotz_prd_bot_amps_total_min,
       "netBotz-prd-bot-amps-total-max": netBotz_prd_bot_amps_total_max,
       "netBotz-prd-bot-amps-total-support-enabled": netBotz_prd_bot_amps_total_support_enabled,
       "netBotz-prd-bot-amps1-uV-per-10mA": netBotz_prd_bot_amps1_uV_per_10mA,
       "netBotz-prd-bot-amps2-uV-per-10mA": netBotz_prd_bot_amps2_uV_per_10mA,
       "netBotz-prd-bot-amps3-uV-per-mA": netBotz_prd_bot_amps3_uV_per_mA,
       "netBotz-prd-bot-amps1-max-range": netBotz_prd_bot_amps1_max_range,
       "netBotz-prd-bot-amps2-max-range": netBotz_prd_bot_amps2_max_range,
       "netBotz-prd-bot-amps3-max-range": netBotz_prd_bot_amps3_max_range,
       "netBotz-prd-bot-amps4": netBotz_prd_bot_amps4,
       "netBotz-prd-bot-amps4-enabled": netBotz_prd_bot_amps4_enabled,
       "netBotz-prd-bot-amps4-min": netBotz_prd_bot_amps4_min,
       "netBotz-prd-bot-amps4-max": netBotz_prd_bot_amps4_max,
       "netBotz-prd-bot-amps4-uV-per-10mA": netBotz_prd_bot_amps4_uV_per_10mA,
       "netBotz-prd-bot-amps4-max-range": netBotz_prd_bot_amps4_max_range,
       "netBotz-prd-bot-ext-temp1": netBotz_prd_bot_ext_temp1,
       "netBotz-prd-bot-ext-temp2": netBotz_prd_bot_ext_temp2,
       "netBotz-prd-bot-ext-temp3": netBotz_prd_bot_ext_temp3,
       "netBotz-prd-bot-ext-temp1-enabled": netBotz_prd_bot_ext_temp1_enabled,
       "netBotz-prd-bot-ext-temp1-min": netBotz_prd_bot_ext_temp1_min,
       "netBotz-prd-bot-ext-temp1-max": netBotz_prd_bot_ext_temp1_max,
       "netBotz-prd-bot-ext-temp2-enabled": netBotz_prd_bot_ext_temp2_enabled,
       "netBotz-prd-bot-ext-temp2-min": netBotz_prd_bot_ext_temp2_min,
       "netBotz-prd-bot-ext-temp2-max": netBotz_prd_bot_ext_temp2_max,
       "netBotz-prd-bot-ext-temp3-enabled": netBotz_prd_bot_ext_temp3_enabled,
       "netBotz-prd-bot-ext-temp3-min": netBotz_prd_bot_ext_temp3_min,
       "netBotz-prd-bot-ext-temp3-max": netBotz_prd_bot_ext_temp3_max,
       "netBotz-prd-bot-ext-temp1-uV-per-degreeC": netBotz_prd_bot_ext_temp1_uV_per_degreeC,
       "netBotz-prd-bot-ext-temp1-uV-at-0-degreeC": netBotz_prd_bot_ext_temp1_uV_at_0_degreeC,
       "netBotz-prd-bot-ext-temp1-min-range": netBotz_prd_bot_ext_temp1_min_range,
       "netBotz-prd-bot-ext-temp1-max-range": netBotz_prd_bot_ext_temp1_max_range,
       "netBotz-prd-bot-ext-temp2-uV-per-degreeC": netBotz_prd_bot_ext_temp2_uV_per_degreeC,
       "netBotz-prd-bot-ext-temp2-uV-at-0-degreeC": netBotz_prd_bot_ext_temp2_uV_at_0_degreeC,
       "netBotz-prd-bot-ext-temp2-min-range": netBotz_prd_bot_ext_temp2_min_range,
       "netBotz-prd-bot-ext-temp2-max-range": netBotz_prd_bot_ext_temp2_max_range,
       "netBotz-prd-bot-ext-temp3-uV-per-degreeC": netBotz_prd_bot_ext_temp3_uV_per_degreeC,
       "netBotz-prd-bot-ext-temp3-uV-at-0-degreeC": netBotz_prd_bot_ext_temp3_uV_at_0_degreeC,
       "netBotz-prd-bot-ext-temp3-min-range": netBotz_prd_bot_ext_temp3_min_range,
       "netBotz-prd-bot-ext-temp3-max-range": netBotz_prd_bot_ext_temp3_max_range,
       "netBotz-prd-bot-ext-port1-module-id": netBotz_prd_bot_ext_port1_module_id,
       "netBotz-prd-bot-ext-port1-module-type": netBotz_prd_bot_ext_port1_module_type,
       "netBotz-prd-bot-ext-port2-module-id": netBotz_prd_bot_ext_port2_module_id,
       "netBotz-prd-bot-ext-port2-module-type": netBotz_prd_bot_ext_port2_module_type,
       "netBotz-prd-bot-ext-port3-module-id": netBotz_prd_bot_ext_port3_module_id,
       "netBotz-prd-bot-ext-port3-module-type": netBotz_prd_bot_ext_port3_module_type,
       "netBotz-prd-bot-amp1-total-amp-seconds": netBotz_prd_bot_amp1_total_amp_seconds,
       "netBotz-prd-bot-amp1-total-amp-seconds-since-time": netBotz_prd_bot_amp1_total_amp_seconds_since_time,
       "netBotz-prd-bot-amp2-total-amp-seconds": netBotz_prd_bot_amp2_total_amp_seconds,
       "netBotz-prd-bot-amp2-total-amp-seconds-since-time": netBotz_prd_bot_amp2_total_amp_seconds_since_time,
       "netBotz-prd-bot-amp3-total-amp-seconds": netBotz_prd_bot_amp3_total_amp_seconds,
       "netBotz-prd-bot-amp3-total-amp-seconds-since-time": netBotz_prd_bot_amp3_total_amp_seconds_since_time,
       "netBotz-prd-bot-amp4-total-amp-seconds": netBotz_prd_bot_amp4_total_amp_seconds,
       "netBotz-prd-bot-amp4-total-amp-seconds-since-time": netBotz_prd_bot_amp4_total_amp_seconds_since_time,
       "netBotz-prd-bot-amptotal-total-amp-seconds": netBotz_prd_bot_amptotal_total_amp_seconds,
       "netBotz-prd-bot-amptotal-total-amp-seconds-since-time": netBotz_prd_bot_amptotal_total_amp_seconds_since_time,
       "netBotz-prd-bot-ext-dry1": netBotz_prd_bot_ext_dry1,
       "netBotz-prd-bot-ext-dry2": netBotz_prd_bot_ext_dry2,
       "netBotz-prd-bot-ext-dry3": netBotz_prd_bot_ext_dry3,
       "netBotz-prd-bot-ext-dry4": netBotz_prd_bot_ext_dry4,
       "netBotz-prd-bot-ext-dry1-alarm-value": netBotz_prd_bot_ext_dry1_alarm_value,
       "netBotz-prd-bot-ext-dry1-enabled": netBotz_prd_bot_ext_dry1_enabled,
       "netBotz-prd-bot-ext-dry2-alarm-value": netBotz_prd_bot_ext_dry2_alarm_value,
       "netBotz-prd-bot-ext-dry2-enabled": netBotz_prd_bot_ext_dry2_enabled,
       "netBotz-prd-bot-ext-dry3-alarm-value": netBotz_prd_bot_ext_dry3_alarm_value,
       "netBotz-prd-bot-ext-dry3-enabled": netBotz_prd_bot_ext_dry3_enabled,
       "netBotz-prd-bot-ext-dry4-alarm-value": netBotz_prd_bot_ext_dry4_alarm_value,
       "netBotz-prd-bot-ext-dry4-enabled": netBotz_prd_bot_ext_dry4_enabled,
       "netBotz-prd-bot-ext-dry1-label": netBotz_prd_bot_ext_dry1_label,
       "netBotz-prd-bot-ext-dry1-open-label": netBotz_prd_bot_ext_dry1_open_label,
       "netBotz-prd-bot-ext-dry1-closed-label": netBotz_prd_bot_ext_dry1_closed_label,
       "netBotz-prd-bot-ext-dry1-open-to-close-millis": netBotz_prd_bot_ext_dry1_open_to_close_millis,
       "netBotz-prd-bot-ext-dry1-close-to-open-millis": netBotz_prd_bot_ext_dry1_close_to_open_millis,
       "netBotz-prd-bot-ext-dry1-response": netBotz_prd_bot_ext_dry1_response,
       "netBotz-prd-bot-ext-dry2-label": netBotz_prd_bot_ext_dry2_label,
       "netBotz-prd-bot-ext-dry2-open-label": netBotz_prd_bot_ext_dry2_open_label,
       "netBotz-prd-bot-ext-dry2-closed-label": netBotz_prd_bot_ext_dry2_closed_label,
       "netBotz-prd-bot-ext-dry2-open-to-close-millis": netBotz_prd_bot_ext_dry2_open_to_close_millis,
       "netBotz-prd-bot-ext-dry2-close-to-open-millis": netBotz_prd_bot_ext_dry2_close_to_open_millis,
       "netBotz-prd-bot-ext-dry2-response": netBotz_prd_bot_ext_dry2_response,
       "netBotz-prd-bot-ext-dry3-label": netBotz_prd_bot_ext_dry3_label,
       "netBotz-prd-bot-ext-dry3-open-label": netBotz_prd_bot_ext_dry3_open_label,
       "netBotz-prd-bot-ext-dry3-closed-label": netBotz_prd_bot_ext_dry3_closed_label,
       "netBotz-prd-bot-ext-dry3-open-to-close-millis": netBotz_prd_bot_ext_dry3_open_to_close_millis,
       "netBotz-prd-bot-ext-dry3-close-to-open-millis": netBotz_prd_bot_ext_dry3_close_to_open_millis,
       "netBotz-prd-bot-ext-dry3-response": netBotz_prd_bot_ext_dry3_response,
       "netBotz-prd-bot-cam-motion": netBotz_prd_bot_cam_motion,
       "netBotz-prd-bot-cam-motion-enabled": netBotz_prd_bot_cam_motion_enabled,
       "netBotz-prd-bot-cam-motion-sensitivity": netBotz_prd_bot_cam_motion_sensitivity,
       "netBotz-prd-bot-cam-motion-delay": netBotz_prd_bot_cam_motion_delay,
       "netBotz-prd-bot-camera-event-autocycle": netBotz_prd_bot_camera_event_autocycle,
       "netBotz-prd-bot-num-pix-before-alarm": netBotz_prd_bot_num_pix_before_alarm,
       "netBotz-prd-bot-delay-before-event-pix": netBotz_prd_bot_delay_before_event_pix,
       "netBotz-prd-bot-delay-between-event-pix": netBotz_prd_bot_delay_between_event_pix,
       "netBotz-prd-bot-cam-motion-area-of-motion": netBotz_prd_bot_cam_motion_area_of_motion,
       "netBotz-prd-bot-cam-pix-for-duration-of-alerts": netBotz_prd_bot_cam_pix_for_duration_of_alerts,
       "netBotz-prd-bot-camera-enabled": netBotz_prd_bot_camera_enabled,
       "netBotz-prd-bot-camera-is-flipped": netBotz_prd_bot_camera_is_flipped,
       "netBotz-prd-bot-camera-brightness": netBotz_prd_bot_camera_brightness,
       "netBotz-prd-crawlers": netBotz_prd_crawlers,
       "netbotz-crawlers": netbotz_crawlers,
       "netBotz-prd-crl-mib2": netBotz_prd_crl_mib2,
       "netBotz-prd-crl-mib2-ping": netBotz_prd_crl_mib2_ping,
       "netBotz-prd-crl-ping-offline-trap": netBotz_prd_crl_ping_offline_trap,
       "netBotz-prd-crl-ping-online-trap": netBotz_prd_crl_ping_online_trap,
       "netBotz-prd-crl-mib2-uptime": netBotz_prd_crl_mib2_uptime,
       "netBotz-prd-crl-uptime-online-trap": netBotz_prd_crl_uptime_online_trap,
       "netBotz-prd-crl-mib2-snmpstatus": netBotz_prd_crl_mib2_snmpstatus,
       "netBotz-prd-crl-snmp-offline-trap": netBotz_prd_crl_snmp_offline_trap,
       "netBotz-prd-crl-snmp-online-trap": netBotz_prd_crl_snmp_online_trap,
       "netBotz-prd-crl-mib2if": netBotz_prd_crl_mib2if,
       "netBotz-prd-crl-mib2if-opstatus": netBotz_prd_crl_mib2if_opstatus,
       "netBotz-prd-crl-opstatus-mismatch-trap": netBotz_prd_crl_opstatus_mismatch_trap,
       "netBotz-prd-crl-opstatus-match-trap": netBotz_prd_crl_opstatus_match_trap,
       "netBotz-prd-crl-opstatus-offline-trap": netBotz_prd_crl_opstatus_offline_trap,
       "netBotz-prd-crltrap": netBotz_prd_crltrap,
       "netBotz-prd-crl-trap-index": netBotz_prd_crl_trap_index,
       "netBotz-prd-crl-trap-address": netBotz_prd_crl_trap_address,
       "netBotz-prd-crl-trap-oid": netBotz_prd_crl_trap_oid,
       "netBotz-prd-crl-trap-botoid": netBotz_prd_crl_trap_botoid,
       "netBotz-prd-crl-trap-value": netBotz_prd_crl_trap_value,
       "netBotz-prd-crl-trap-date": netBotz_prd_crl_trap_date,
       "netBotz-prd-crl-trap-attrib": netBotz_prd_crl_trap_attrib,
       "netBotz-prd-crl-trap-desc": netBotz_prd_crl_trap_desc,
       "netBotz-prd-bot-traps": netBotz_prd_bot_traps,
       "netBotz-prd-bot-temperature-traps": netBotz_prd_bot_temperature_traps,
       "netBotz-prd-bot-temperature-low-trap": netBotz_prd_bot_temperature_low_trap,
       "netBotz-prd-bot-temperature-high-trap": netBotz_prd_bot_temperature_high_trap,
       "netBotz-prd-bot-temperature-trap-clear": netBotz_prd_bot_temperature_trap_clear,
       "netBotz-prd-bot-humidity-traps": netBotz_prd_bot_humidity_traps,
       "netBotz-prd-bot-humidity-low-trap": netBotz_prd_bot_humidity_low_trap,
       "netBotz-prd-bot-humidity-high-trap": netBotz_prd_bot_humidity_high_trap,
       "netBotz-prd-bot-humidity-trap-clear": netBotz_prd_bot_humidity_trap_clear,
       "netBotz-prd-bot-airflow-traps": netBotz_prd_bot_airflow_traps,
       "netBotz-prd-bot-airflow-low-trap": netBotz_prd_bot_airflow_low_trap,
       "netBotz-prd-bot-airflow-trap-clear": netBotz_prd_bot_airflow_trap_clear,
       "netBotz-prd-bot-audio-traps": netBotz_prd_bot_audio_traps,
       "netBotz-prd-bot-audio-high-trap": netBotz_prd_bot_audio_high_trap,
       "netBotz-prd-bot-audio-trap-clear": netBotz_prd_bot_audio_trap_clear,
       "netBotz-prd-bot-door-traps": netBotz_prd_bot_door_traps,
       "netBotz-prd-bot-door-trap-tripped": netBotz_prd_bot_door_trap_tripped,
       "netBotz-prd-bot-door-trap-clear": netBotz_prd_bot_door_trap_clear,
       "netBotz-prd-bot-amp1-traps": netBotz_prd_bot_amp1_traps,
       "netBotz-prd-bot-amp1-low-trap": netBotz_prd_bot_amp1_low_trap,
       "netBotz-prd-bot-amp1-high-trap": netBotz_prd_bot_amp1_high_trap,
       "netBotz-prd-bot-amp1-trap-clear": netBotz_prd_bot_amp1_trap_clear,
       "netBotz-prd-bot-amp1-sensor-unplugged": netBotz_prd_bot_amp1_sensor_unplugged,
       "netBotz-prd-bot-amp1-sensor-replugged": netBotz_prd_bot_amp1_sensor_replugged,
       "netBotz-prd-bot-amp2-traps": netBotz_prd_bot_amp2_traps,
       "netBotz-prd-bot-amp2-low-trap": netBotz_prd_bot_amp2_low_trap,
       "netBotz-prd-bot-amp2-high-trap": netBotz_prd_bot_amp2_high_trap,
       "netBotz-prd-bot-amp2-trap-clear": netBotz_prd_bot_amp2_trap_clear,
       "netBotz-prd-bot-amp2-sensor-unplugged": netBotz_prd_bot_amp2_sensor_unplugged,
       "netBotz-prd-bot-amp2-sensor-replugged": netBotz_prd_bot_amp2_sensor_replugged,
       "netBotz-prd-bot-amp3-traps": netBotz_prd_bot_amp3_traps,
       "netBotz-prd-bot-amp3-low-trap": netBotz_prd_bot_amp3_low_trap,
       "netBotz-prd-bot-amp3-high-trap": netBotz_prd_bot_amp3_high_trap,
       "netBotz-prd-bot-amp3-trap-clear": netBotz_prd_bot_amp3_trap_clear,
       "netBotz-prd-bot-amp3-sensor-unplugged": netBotz_prd_bot_amp3_sensor_unplugged,
       "netBotz-prd-bot-amp3-sensor-replugged": netBotz_prd_bot_amp3_sensor_replugged,
       "netBotz-prd-bot-amp4-traps": netBotz_prd_bot_amp4_traps,
       "netBotz-prd-bot-amp4-low-trap": netBotz_prd_bot_amp4_low_trap,
       "netBotz-prd-bot-amp4-high-trap": netBotz_prd_bot_amp4_high_trap,
       "netBotz-prd-bot-amp4-trap-clear": netBotz_prd_bot_amp4_trap_clear,
       "netBotz-prd-bot-amp4-sensor-unplugged": netBotz_prd_bot_amp4_sensor_unplugged,
       "netBotz-prd-bot-amp4-sensor-replugged": netBotz_prd_bot_amp4_sensor_replugged,
       "netBotz-prd-bot-amp-total-traps": netBotz_prd_bot_amp_total_traps,
       "netBotz-prd-bot-amp-total-low-trap": netBotz_prd_bot_amp_total_low_trap,
       "netBotz-prd-bot-amp-total-high-trap": netBotz_prd_bot_amp_total_high_trap,
       "netBotz-prd-bot-amp-total-trap-clear": netBotz_prd_bot_amp_total_trap_clear,
       "netBotz-prd-bot-ext-temp1-traps": netBotz_prd_bot_ext_temp1_traps,
       "netBotz-prd-bot-ext-temp1-low-trap": netBotz_prd_bot_ext_temp1_low_trap,
       "netBotz-prd-bot-ext-temp1-high-trap": netBotz_prd_bot_ext_temp1_high_trap,
       "netBotz-prd-bot-ext-temp1-trap-clear": netBotz_prd_bot_ext_temp1_trap_clear,
       "netBotz-prd-bot-ext-temp1-sensor-unplugged": netBotz_prd_bot_ext_temp1_sensor_unplugged,
       "netBotz-prd-bot-ext-temp1-sensor-replugged": netBotz_prd_bot_ext_temp1_sensor_replugged,
       "netBotz-prd-bot-ext-temp2-traps": netBotz_prd_bot_ext_temp2_traps,
       "netBotz-prd-bot-ext-temp2-low-trap": netBotz_prd_bot_ext_temp2_low_trap,
       "netBotz-prd-bot-ext-temp2-high-trap": netBotz_prd_bot_ext_temp2_high_trap,
       "netBotz-prd-bot-ext-temp2-trap-clear": netBotz_prd_bot_ext_temp2_trap_clear,
       "netBotz-prd-bot-ext-temp2-sensor-unplugged": netBotz_prd_bot_ext_temp2_sensor_unplugged,
       "netBotz-prd-bot-ext-temp2-sensor-replugged": netBotz_prd_bot_ext_temp2_sensor_replugged,
       "netBotz-prd-bot-ext-temp3-traps": netBotz_prd_bot_ext_temp3_traps,
       "netBotz-prd-bot-ext-temp3-low-trap": netBotz_prd_bot_ext_temp3_low_trap,
       "netBotz-prd-bot-ext-temp3-high-trap": netBotz_prd_bot_ext_temp3_high_trap,
       "netBotz-prd-bot-ext-temp3-trap-clear": netBotz_prd_bot_ext_temp3_trap_clear,
       "netBotz-prd-bot-ext-temp3-sensor-unplugged": netBotz_prd_bot_ext_temp3_sensor_unplugged,
       "netBotz-prd-bot-ext-temp3-sensor-replugged": netBotz_prd_bot_ext_temp3_sensor_replugged,
       "netBotz-prd-bot-ext-temp4-traps": netBotz_prd_bot_ext_temp4_traps,
       "netBotz-prd-bot-ext-temp4-low-trap": netBotz_prd_bot_ext_temp4_low_trap,
       "netBotz-prd-bot-ext-temp4-high-trap": netBotz_prd_bot_ext_temp4_high_trap,
       "netBotz-prd-bot-ext-temp4-trap-clear": netBotz_prd_bot_ext_temp4_trap_clear,
       "netBotz-prd-bot-ext-temp4-sensor-unplugged": netBotz_prd_bot_ext_temp4_sensor_unplugged,
       "netBotz-prd-bot-ext-temp4-sensor-replugged": netBotz_prd_bot_ext_temp4_sensor_replugged,
       "netBotz-prd-bot-ext-dry1-traps": netBotz_prd_bot_ext_dry1_traps,
       "netBotz-prd-bot-ext-dry1-triggered-trap": netBotz_prd_bot_ext_dry1_triggered_trap,
       "netBotz-prd-bot-ext-dry1-trap-clear": netBotz_prd_bot_ext_dry1_trap_clear,
       "netBotz-prd-bot-ext-dry2-traps": netBotz_prd_bot_ext_dry2_traps,
       "netBotz-prd-bot-ext-dry2-triggered-trap": netBotz_prd_bot_ext_dry2_triggered_trap,
       "netBotz-prd-bot-ext-dry2-trap-clear": netBotz_prd_bot_ext_dry2_trap_clear,
       "netBotz-prd-bot-ext-dry3-traps": netBotz_prd_bot_ext_dry3_traps,
       "netBotz-prd-bot-ext-dry3-triggered-trap": netBotz_prd_bot_ext_dry3_triggered_trap,
       "netBotz-prd-bot-ext-dry3-trap-clear": netBotz_prd_bot_ext_dry3_trap_clear,
       "netBotz-prd-bot-ext-dry4-traps": netBotz_prd_bot_ext_dry4_traps,
       "netBotz-prd-bot-ext-dry4-triggered-trap": netBotz_prd_bot_ext_dry4_triggered_trap,
       "netBotz-prd-bot-ext-dry4-trap-clear": netBotz_prd_bot_ext_dry4_trap_clear,
       "netBotz-prd-bot-amp5-traps": netBotz_prd_bot_amp5_traps,
       "netBotz-prd-bot-amp5-low-trap": netBotz_prd_bot_amp5_low_trap,
       "netBotz-prd-bot-amp5-high-trap": netBotz_prd_bot_amp5_high_trap,
       "netBotz-prd-bot-amp5-trap-clear": netBotz_prd_bot_amp5_trap_clear,
       "netBotz-prd-bot-amp5-sensor-unplugged": netBotz_prd_bot_amp5_sensor_unplugged,
       "netBotz-prd-bot-amp5-sensor-replugged": netBotz_prd_bot_amp5_sensor_replugged,
       "netBotz-prd-bot-amp6-traps": netBotz_prd_bot_amp6_traps,
       "netBotz-prd-bot-amp6-low-trap": netBotz_prd_bot_amp6_low_trap,
       "netBotz-prd-bot-amp6-high-trap": netBotz_prd_bot_amp6_high_trap,
       "netBotz-prd-bot-amp6-trap-clear": netBotz_prd_bot_amp6_trap_clear,
       "netBotz-prd-bot-amp6-sensor-unplugged": netBotz_prd_bot_amp6_sensor_unplugged,
       "netBotz-prd-bot-amp6-sensor-replugged": netBotz_prd_bot_amp6_sensor_replugged,
       "netBotz-prd-bot-amp7-traps": netBotz_prd_bot_amp7_traps,
       "netBotz-prd-bot-amp7-low-trap": netBotz_prd_bot_amp7_low_trap,
       "netBotz-prd-bot-amp7-high-trap": netBotz_prd_bot_amp7_high_trap,
       "netBotz-prd-bot-amp7-trap-clear": netBotz_prd_bot_amp7_trap_clear,
       "netBotz-prd-bot-amp7-sensor-unplugged": netBotz_prd_bot_amp7_sensor_unplugged,
       "netBotz-prd-bot-amp7-sensor-replugged": netBotz_prd_bot_amp7_sensor_replugged,
       "netBotz-prd-bot-ext-temp5-traps": netBotz_prd_bot_ext_temp5_traps,
       "netBotz-prd-bot-ext-temp5-low-trap": netBotz_prd_bot_ext_temp5_low_trap,
       "netBotz-prd-bot-ext-temp5-high-trap": netBotz_prd_bot_ext_temp5_high_trap,
       "netBotz-prd-bot-ext-temp5-trap-clear": netBotz_prd_bot_ext_temp5_trap_clear,
       "netBotz-prd-bot-ext-temp5-sensor-unplugged": netBotz_prd_bot_ext_temp5_sensor_unplugged,
       "netBotz-prd-bot-ext-temp5-sensor-replugged": netBotz_prd_bot_ext_temp5_sensor_replugged,
       "netBotz-prd-bot-ext-temp6-traps": netBotz_prd_bot_ext_temp6_traps,
       "netBotz-prd-bot-ext-temp6-low-trap": netBotz_prd_bot_ext_temp6_low_trap,
       "netBotz-prd-bot-ext-temp6-high-trap": netBotz_prd_bot_ext_temp6_high_trap,
       "netBotz-prd-bot-ext-temp6-trap-clear": netBotz_prd_bot_ext_temp6_trap_clear,
       "netBotz-prd-bot-ext-temp6-sensor-unplugged": netBotz_prd_bot_ext_temp6_sensor_unplugged,
       "netBotz-prd-bot-ext-temp6-sensor-replugged": netBotz_prd_bot_ext_temp6_sensor_replugged,
       "netBotz-prd-bot-ext-temp7-traps": netBotz_prd_bot_ext_temp7_traps,
       "netBotz-prd-bot-ext-temp7-low-trap": netBotz_prd_bot_ext_temp7_low_trap,
       "netBotz-prd-bot-ext-temp7-high-trap": netBotz_prd_bot_ext_temp7_high_trap,
       "netBotz-prd-bot-ext-temp7-trap-clear": netBotz_prd_bot_ext_temp7_trap_clear,
       "netBotz-prd-bot-ext-temp7-sensor-unplugged": netBotz_prd_bot_ext_temp7_sensor_unplugged,
       "netBotz-prd-bot-ext-temp7-sensor-replugged": netBotz_prd_bot_ext_temp7_sensor_replugged,
       "netBotz-prd-bot-ext-dry5-traps": netBotz_prd_bot_ext_dry5_traps,
       "netBotz-prd-bot-ext-dry5-triggered-trap": netBotz_prd_bot_ext_dry5_triggered_trap,
       "netBotz-prd-bot-ext-dry5-trap-clear": netBotz_prd_bot_ext_dry5_trap_clear,
       "netBotz-prd-bot-ext-dry6-traps": netBotz_prd_bot_ext_dry6_traps,
       "netBotz-prd-bot-ext-dry6-triggered-trap": netBotz_prd_bot_ext_dry6_triggered_trap,
       "netBotz-prd-bot-ext-dry6-trap-clear": netBotz_prd_bot_ext_dry6_trap_clear,
       "netBotz-prd-bot-ext-dry7-traps": netBotz_prd_bot_ext_dry7_traps,
       "netBotz-prd-bot-ext-dry7-triggered-trap": netBotz_prd_bot_ext_dry7_triggered_trap,
       "netBotz-prd-bot-ext-dry7-trap-clear": netBotz_prd_bot_ext_dry7_trap_clear,
       "netBotz-prd-bot-camera-motion-traps": netBotz_prd_bot_camera_motion_traps,
       "netBotz-prd-bot-camera-motion-trap-tripped": netBotz_prd_bot_camera_motion_trap_tripped,
       "netBotz-prd-bot-camera-motion-trap-clear": netBotz_prd_bot_camera_motion_trap_clear,
       "netBotz-prd-bot-ext-humi1-traps": netBotz_prd_bot_ext_humi1_traps,
       "netBotz-prd-bot-ext-humi1-low-trap": netBotz_prd_bot_ext_humi1_low_trap,
       "netBotz-prd-bot-ext-humi1-high-trap": netBotz_prd_bot_ext_humi1_high_trap,
       "netBotz-prd-bot-ext-humi1-trap-clear": netBotz_prd_bot_ext_humi1_trap_clear,
       "netBotz-prd-bot-ext-humi1-sensor-unplugged": netBotz_prd_bot_ext_humi1_sensor_unplugged,
       "netBotz-prd-bot-ext-humi1-sensor-replugged": netBotz_prd_bot_ext_humi1_sensor_replugged,
       "netBotz-prd-bot-ext-humi2-traps": netBotz_prd_bot_ext_humi2_traps,
       "netBotz-prd-bot-ext-humi2-low-trap": netBotz_prd_bot_ext_humi2_low_trap,
       "netBotz-prd-bot-ext-humi2-high-trap": netBotz_prd_bot_ext_humi2_high_trap,
       "netBotz-prd-bot-ext-humi2-trap-clear": netBotz_prd_bot_ext_humi2_trap_clear,
       "netBotz-prd-bot-ext-humi2-sensor-unplugged": netBotz_prd_bot_ext_humi2_sensor_unplugged,
       "netBotz-prd-bot-ext-humi2-sensor-replugged": netBotz_prd_bot_ext_humi2_sensor_replugged,
       "netBotz-prd-bot-ext-humi3-traps": netBotz_prd_bot_ext_humi3_traps,
       "netBotz-prd-bot-ext-humi3-low-trap": netBotz_prd_bot_ext_humi3_low_trap,
       "netBotz-prd-bot-ext-humi3-high-trap": netBotz_prd_bot_ext_humi3_high_trap,
       "netBotz-prd-bot-ext-humi3-trap-clear": netBotz_prd_bot_ext_humi3_trap_clear,
       "netBotz-prd-bot-ext-humi3-sensor-unplugged": netBotz_prd_bot_ext_humi3_sensor_unplugged,
       "netBotz-prd-bot-ext-humi3-sensor-replugged": netBotz_prd_bot_ext_humi3_sensor_replugged,
       "netBotz-prd-bot-ext-humi4-traps": netBotz_prd_bot_ext_humi4_traps,
       "netBotz-prd-bot-ext-humi4-low-trap": netBotz_prd_bot_ext_humi4_low_trap,
       "netBotz-prd-bot-ext-humi4-high-trap": netBotz_prd_bot_ext_humi4_high_trap,
       "netBotz-prd-bot-ext-humi4-trap-clear": netBotz_prd_bot_ext_humi4_trap_clear,
       "netBotz-prd-bot-ext-humi4-sensor-unplugged": netBotz_prd_bot_ext_humi4_sensor_unplugged,
       "netBotz-prd-bot-ext-humi4-sensor-replugged": netBotz_prd_bot_ext_humi4_sensor_replugged,
       "netBotz-prd-bot-ext-humi5-traps": netBotz_prd_bot_ext_humi5_traps,
       "netBotz-prd-bot-ext-humi5-low-trap": netBotz_prd_bot_ext_humi5_low_trap,
       "netBotz-prd-bot-ext-humi5-high-trap": netBotz_prd_bot_ext_humi5_high_trap,
       "netBotz-prd-bot-ext-humi5-trap-clear": netBotz_prd_bot_ext_humi5_trap_clear,
       "netBotz-prd-bot-ext-humi5-sensor-unplugged": netBotz_prd_bot_ext_humi5_sensor_unplugged,
       "netBotz-prd-bot-ext-humi5-sensor-replugged": netBotz_prd_bot_ext_humi5_sensor_replugged,
       "netBotz-prd-bot-ext-humi6-traps": netBotz_prd_bot_ext_humi6_traps,
       "netBotz-prd-bot-ext-humi6-low-trap": netBotz_prd_bot_ext_humi6_low_trap,
       "netBotz-prd-bot-ext-humi6-high-trap": netBotz_prd_bot_ext_humi6_high_trap,
       "netBotz-prd-bot-ext-humi6-trap-clear": netBotz_prd_bot_ext_humi6_trap_clear,
       "netBotz-prd-bot-ext-humi6-sensor-unplugged": netBotz_prd_bot_ext_humi6_sensor_unplugged,
       "netBotz-prd-bot-ext-humi6-sensor-replugged": netBotz_prd_bot_ext_humi6_sensor_replugged,
       "netBotz-prd-bot-ext-humi7-traps": netBotz_prd_bot_ext_humi7_traps,
       "netBotz-prd-bot-ext-humi7-low-trap": netBotz_prd_bot_ext_humi7_low_trap,
       "netBotz-prd-bot-ext-humi7-high-trap": netBotz_prd_bot_ext_humi7_high_trap,
       "netBotz-prd-bot-ext-humi7-trap-clear": netBotz_prd_bot_ext_humi7_trap_clear,
       "netBotz-prd-bot-ext-humi7-sensor-unplugged": netBotz_prd_bot_ext_humi7_sensor_unplugged,
       "netBotz-prd-bot-ext-humi7-sensor-replugged": netBotz_prd_bot_ext_humi7_sensor_replugged,
       "netBotz-prd-WallBotz-300": netBotz_prd_WallBotz_300,
       "netBotz-prd-RackBotz-300": netBotz_prd_RackBotz_300,
       "netBotz-prd-RackBotz-300U": netBotz_prd_RackBotz_300U,
       "netBotz-prd-WallBotz-400": netBotz_prd_WallBotz_400,
       "netBotz-prd-RackBotz-400": netBotz_prd_RackBotz_400,
       "netBotz-prd-RackBotz-303": netBotz_prd_RackBotz_303,
       "netBotz-prd-WallBotz-310": netBotz_prd_WallBotz_310,
       "netBotz-prd-RackBotz-310": netBotz_prd_RackBotz_310,
       "netBotz-prd-WallBotz-300B": netBotz_prd_WallBotz_300B,
       "netBotz-prd-WallBotz-300C": netBotz_prd_WallBotz_300C,
       "netBotz-prd-RackBotz-300C": netBotz_prd_RackBotz_300C,
       "netBotz-prd-RackBotz-300UC": netBotz_prd_RackBotz_300UC,
       "netBotz-prd-WallBotz-400C": netBotz_prd_WallBotz_400C,
       "netBotz-prd-RackBotz-400C": netBotz_prd_RackBotz_400C,
       "netBotz-prd-RackBotz-303C": netBotz_prd_RackBotz_303C,
       "netBotz-prd-WallBotz-310C": netBotz_prd_WallBotz_310C,
       "netBotz-prd-RackBotz-310C": netBotz_prd_RackBotz_310C,
       "netBotz-prd-WallBotz-300BC": netBotz_prd_WallBotz_300BC,
       "netBotz-prd-WallBotz-300E": netBotz_prd_WallBotz_300E,
       "netBotz-prd-RackBotz-300E": netBotz_prd_RackBotz_300E,
       "netBotz-prd-RackBotz-300UE": netBotz_prd_RackBotz_300UE,
       "netBotz-prd-WallBotz-400E": netBotz_prd_WallBotz_400E,
       "netBotz-prd-RackBotz-400E": netBotz_prd_RackBotz_400E,
       "netBotz-prd-RackBotz-303E": netBotz_prd_RackBotz_303E,
       "netBotz-prd-WallBotz-310E": netBotz_prd_WallBotz_310E,
       "netBotz-prd-RackBotz-310E": netBotz_prd_RackBotz_310E,
       "netBotz-prd-WallBotz-300BE": netBotz_prd_WallBotz_300BE,
       "expPortTable": expPortTable,
       "expPortEntry": expPortEntry,
       "expPort-module-id": expPort_module_id,
       "expPort-module-type": expPort_module_type,
       "expPort-label": expPort_label,
       "expPort-amps": expPort_amps,
       "expPort-total-amp-seconds": expPort_total_amp_seconds,
       "expPort-total-amp-seconds-since-time": expPort_total_amp_seconds_since_time,
       "expPort-amps-enabled": expPort_amps_enabled,
       "expPort-amps-min": expPort_amps_min,
       "expPort-amps-max": expPort_amps_max,
       "expPort-amps-uV-per-10mA": expPort_amps_uV_per_10mA,
       "expPort-amps-max-range": expPort_amps_max_range,
       "expPort-ext-temp": expPort_ext_temp,
       "expPort-ext-temp-enabled": expPort_ext_temp_enabled,
       "expPort-ext-temp-min": expPort_ext_temp_min,
       "expPort-ext-temp-max": expPort_ext_temp_max,
       "expPort-ext-temp-uV-per-degreeC": expPort_ext_temp_uV_per_degreeC,
       "expPort-ext-temp-uV-at-0-degreeC": expPort_ext_temp_uV_at_0_degreeC,
       "expPort-ext-temp-min-range": expPort_ext_temp_min_range,
       "expPort-ext-temp-max-range": expPort_ext_temp_max_range,
       "expPort-ext-dry": expPort_ext_dry,
       "expPort-ext-dry-alarm-value": expPort_ext_dry_alarm_value,
       "expPort-ext-dry-enabled": expPort_ext_dry_enabled,
       "expPort-ext-dry-label": expPort_ext_dry_label,
       "expPort-ext-dry-open-label": expPort_ext_dry_open_label,
       "expPort-ext-dry-closed-label": expPort_ext_dry_closed_label,
       "expPort-ext-dry-open-to-close-millis": expPort_ext_dry_open_to_close_millis,
       "expPort-ext-dry-close-to-open-millis": expPort_ext_dry_close_to_open_millis,
       "expPort-ext-dry-response": expPort_ext_dry_response,
       "expPort-ext-humi": expPort_ext_humi,
       "expPort-ext-humi-enabled": expPort_ext_humi_enabled,
       "expPort-ext-humi-min": expPort_ext_humi_min,
       "expPort-ext-humi-max": expPort_ext_humi_max,
       "expPort-ext-humi-uV-per-percent": expPort_ext_humi_uV_per_percent,
       "expPort-ext-humi-uV-at-0-percent": expPort_ext_humi_uV_at_0_percent,
       "expPort-ext-humi-min-range": expPort_ext_humi_min_range,
       "expPort-ext-humi-max-range": expPort_ext_humi_max_range,
       "netBotz-metric": netBotz_metric,
       "netBotz-metric-onboard": netBotz_metric_onboard,
       "netBotz-metric-onboard-model": netBotz_metric_onboard_model,
       "netBotz-metric-onboard-temp": netBotz_metric_onboard_temp,
       "netBotz-metric-onboard-humidity": netBotz_metric_onboard_humidity,
       "netBotz-metric-onboard-airflow": netBotz_metric_onboard_airflow,
       "netBotz-metric-onboard-audio": netBotz_metric_onboard_audio,
       "netBotz-metric-onboard-doorajar": netBotz_metric_onboard_doorajar,
       "netBotz-metric-onboard-temp-min": netBotz_metric_onboard_temp_min,
       "netBotz-metric-onboard-temp-max": netBotz_metric_onboard_temp_max,
       "netBotz-metric-onboard-humidity-min": netBotz_metric_onboard_humidity_min,
       "netBotz-metric-onboard-humidity-max": netBotz_metric_onboard_humidity_max,
       "netBotz-metric-onboard-airflow-mins": netBotz_metric_onboard_airflow_mins,
       "netBotz-metric-onboard-audio-secs": netBotz_metric_onboard_audio_secs,
       "netBotz-metric-onboard-switch-state": netBotz_metric_onboard_switch_state,
       "netBotz-metric-onboard-audio-level": netBotz_metric_onboard_audio_level,
       "netBotz-metric-onboard-airflow-level": netBotz_metric_onboard_airflow_level,
       "netBotz-metric-onboard-cam-motion": netBotz_metric_onboard_cam_motion,
       "netBotz-metric-onboard-cam-motion-sensitivity": netBotz_metric_onboard_cam_motion_sensitivity,
       "netBotz-snmp": netBotz_snmp,
       "netBotz-snmp-traptarget": netBotz_snmp_traptarget,
       "netBotz-snmp-community": netBotz_snmp_community,
       "netBotz-snmp-timeout": netBotz_snmp_timeout,
       "netBotz-snmp-retries": netBotz_snmp_retries,
       "netBotz-userid-1": netBotz_userid_1,
       "netBotz-password-1": netBotz_password_1,
       "netBotz-userid-2": netBotz_userid_2,
       "netBotz-password-2": netBotz_password_2,
       "netBotz-userid-3": netBotz_userid_3,
       "netBotz-password-3": netBotz_password_3,
       "netBotz-snmp-traptarget2": netBotz_snmp_traptarget2,
       "netBotz-snmp-read-community": netBotz_snmp_read_community,
       "netBotz-device": netBotz_device,
       "netBotz-dev-host": netBotz_dev_host,
       "netBotz-dev-domain": netBotz_dev_domain,
       "netBotz-dev-ip": netBotz_dev_ip,
       "netBotz-dev-netmask": netBotz_dev_netmask,
       "netBotz-dev-gateway": netBotz_dev_gateway,
       "netBotz-dev-primarydns": netBotz_dev_primarydns,
       "netBotz-dev-secondarydns": netBotz_dev_secondarydns,
       "netBotz-dev-smtp": netBotz_dev_smtp,
       "netBotz-dev-smtpport": netBotz_dev_smtpport,
       "netBotz-dev-popport": netBotz_dev_popport,
       "netBotz-dev-loglevel": netBotz_dev_loglevel,
       "netBotz-dev-primaryemail": netBotz_dev_primaryemail,
       "netBotz-dev-secondaryemail": netBotz_dev_secondaryemail,
       "netBotz-dev-serialno": netBotz_dev_serialno,
       "netBotz-dev-pop": netBotz_dev_pop,
       "netBotz-dev-version": netBotz_dev_version,
       "netBotz-dev-registered": netBotz_dev_registered,
       "netBotz-default-applet": netBotz_default_applet,
       "netBotz-guibar-color": netBotz_guibar_color,
       "netBotz-locale": netBotz_locale,
       "netBotz-timezone": netBotz_timezone,
       "netBotz-24hourpreferred": netBotz_24hourpreferred,
       "netBotz-utc-clock": netBotz_utc_clock,
       "netBotz-ismetric": netBotz_ismetric,
       "netBotz-alert-url": netBotz_alert_url,
       "netBotz-picture-alert-url": netBotz_picture_alert_url,
       "netBotz-sensor-data-url": netBotz_sensor_data_url,
       "netBotz-alert-url-logon": netBotz_alert_url_logon,
       "netBotz-picture-alert-url-logon": netBotz_picture_alert_url_logon,
       "netBotz-sensor-data-url-logon": netBotz_sensor_data_url_logon,
       "netBotz-sensor-data-url-period": netBotz_sensor_data_url_period,
       "netBotz-sensor-data-url-flags": netBotz_sensor_data_url_flags,
       "netBotz-dev-backup-smtp": netBotz_dev_backup_smtp,
       "netBotz-dev-tertiarydns": netBotz_dev_tertiarydns,
       "netBotz-dev-ntp-server": netBotz_dev_ntp_server,
       "netBotz-dev-ntp-period": netBotz_dev_ntp_period,
       "netBotz-dev-socks-server": netBotz_dev_socks_server,
       "netBotz-dev-socks-portnum": netBotz_dev_socks_portnum,
       "netBotz-dev-socks-user-id": netBotz_dev_socks_user_id,
       "netBotz-dev-socks-password": netBotz_dev_socks_password,
       "netBotz-alert-ftp-site": netBotz_alert_ftp_site,
       "netBotz-alert-ftp-path": netBotz_alert_ftp_path,
       "netBotz-alert-ftp-filename": netBotz_alert_ftp_filename,
       "netBotz-alert-ftp-logon": netBotz_alert_ftp_logon,
       "netBotz-sensor-ftp-site": netBotz_sensor_ftp_site,
       "netBotz-sensor-ftp-path": netBotz_sensor_ftp_path,
       "netBotz-sensor-ftp-filename": netBotz_sensor_ftp_filename,
       "netBotz-sensor-ftp-logon": netBotz_sensor_ftp_logon,
       "netBotz-sensor-ftp-period": netBotz_sensor_ftp_period,
       "netBotz-use-syslog": netBotz_use_syslog,
       "netBotz-syslog-address": netBotz_syslog_address,
       "netBotz-syslog-facility": netBotz_syslog_facility,
       "netBotz-color-balance": netBotz_color_balance,
       "netBotz-addonapp": netBotz_addonapp,
       "device-crawlers-trap-target-index": device_crawlers_trap_target_index,
       "branch-checker-trap-target-index": branch_checker_trap_target_index,
       "vendor-netBotz": vendor_netBotz,
       "device-crawlers-trap": device_crawlers_trap,
       "netBotz-device-crawlers-value-low-alert-trap": netBotz_device_crawlers_value_low_alert_trap,
       "netBotz-device-crawlers-value-high-alert-trap": netBotz_device_crawlers_value_high_alert_trap,
       "netBotz-device-crawlers-clear-alert-trap": netBotz_device_crawlers_clear_alert_trap,
       "netBotz-device-crawlers-offline-alert-trap": netBotz_device_crawlers_offline_alert_trap,
       "netBotz-device-crawlers-online-alert-trap": netBotz_device_crawlers_online_alert_trap,
       "netBotz-device-crawlers-ifopstatus-alert-trap": netBotz_device_crawlers_ifopstatus_alert_trap,
       "branch-checker-trap": branch_checker_trap,
       "netBotz-branch-checker-clear-alert-trap": netBotz_branch_checker_clear_alert_trap,
       "netBotz-branch-checker-offline-alert-trap": netBotz_branch_checker_offline_alert_trap,
       "netBotz-branch-checker-online-alert-trap": netBotz_branch_checker_online_alert_trap,
       "netBotz-branch-checker-target-error-trap": netBotz_branch_checker_target_error_trap,
       "netBotz-addonapp-trap": netBotz_addonapp_trap,
       "device-crawlers-trap-attrib": device_crawlers_trap_attrib,
       "device-crawlers-trap-index": device_crawlers_trap_index,
       "device-crawlers-trap-address": device_crawlers_trap_address,
       "device-crawlers-trap-oid": device_crawlers_trap_oid,
       "device-crawlers-trap-botoid": device_crawlers_trap_botoid,
       "device-crawlers-trap-value": device_crawlers_trap_value,
       "device-crawlers-trap-stringvalue": device_crawlers_trap_stringvalue,
       "device-crawlers-trap-date": device_crawlers_trap_date,
       "device-crawlers-trap-attrib-index": device_crawlers_trap_attrib_index,
       "device-crawlers-crawlers-trap-desc": device_crawlers_crawlers_trap_desc,
       "branch-checker-trap-attrib": branch_checker_trap_attrib,
       "branch-checker-trap-index": branch_checker_trap_index,
       "branch-checker-trap-address": branch_checker_trap_address,
       "branch-checker-trap-oid": branch_checker_trap_oid,
       "branch-checker-trap-botoid": branch_checker_trap_botoid,
       "branch-checker-trap-value": branch_checker_trap_value,
       "branch-checker-trap-stringvalue": branch_checker_trap_stringvalue,
       "branch-checker-trap-date": branch_checker_trap_date,
       "branch-checker-trap-attrib-index": branch_checker_trap_attrib_index,
       "branch-checker-trap-desc": branch_checker_trap_desc}
)
