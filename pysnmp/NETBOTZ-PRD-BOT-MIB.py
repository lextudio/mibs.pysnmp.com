# SNMP MIB module (NETBOTZ-PRD-BOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETBOTZ-PRD-BOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:36 2024
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

(netBotz_ismetric,) = mibBuilder.importSymbols(
    "NETBOTZ-DEVICE-MIB",
    "netBotz-ismetric")

(netBotz_products,) = mibBuilder.importSymbols(
    "NETBOTZ-MIB",
    "netBotz-products")

(netBotz_prd_bot,) = mibBuilder.importSymbols(
    "NETBOTZ-PRODUCTS-MIB",
    "netBotz-prd-bot")

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
_NetBotz_prd_bot_doorpic_delay_Type = Integer32
_NetBotz_prd_bot_doorpic_delay_Object = MibScalar
netBotz_prd_bot_doorpic_delay = _NetBotz_prd_bot_doorpic_delay_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 19),
    _NetBotz_prd_bot_doorpic_delay_Type()
)
netBotz_prd_bot_doorpic_delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_doorpic_delay.setStatus("mandatory")
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
_NetBotz_prd_bot_ext_temp4_Type = Integer32
_NetBotz_prd_bot_ext_temp4_Object = MibScalar
netBotz_prd_bot_ext_temp4 = _NetBotz_prd_bot_ext_temp4_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 65),
    _NetBotz_prd_bot_ext_temp4_Type()
)
netBotz_prd_bot_ext_temp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4.setStatus("mandatory")
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
_NetBotz_prd_bot_ext_temp4_enabled_Type = Integer32
_NetBotz_prd_bot_ext_temp4_enabled_Object = MibScalar
netBotz_prd_bot_ext_temp4_enabled = _NetBotz_prd_bot_ext_temp4_enabled_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 75),
    _NetBotz_prd_bot_ext_temp4_enabled_Type()
)
netBotz_prd_bot_ext_temp4_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_enabled.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp4_min_Type = Integer32
_NetBotz_prd_bot_ext_temp4_min_Object = MibScalar
netBotz_prd_bot_ext_temp4_min = _NetBotz_prd_bot_ext_temp4_min_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 76),
    _NetBotz_prd_bot_ext_temp4_min_Type()
)
netBotz_prd_bot_ext_temp4_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_min.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp4_max_Type = Integer32
_NetBotz_prd_bot_ext_temp4_max_Object = MibScalar
netBotz_prd_bot_ext_temp4_max = _NetBotz_prd_bot_ext_temp4_max_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 77),
    _NetBotz_prd_bot_ext_temp4_max_Type()
)
netBotz_prd_bot_ext_temp4_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_max.setStatus("mandatory")
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
_NetBotz_prd_bot_ext_temp4_uV_per_degreeC_Type = Integer32
_NetBotz_prd_bot_ext_temp4_uV_per_degreeC_Object = MibScalar
netBotz_prd_bot_ext_temp4_uV_per_degreeC = _NetBotz_prd_bot_ext_temp4_uV_per_degreeC_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 90),
    _NetBotz_prd_bot_ext_temp4_uV_per_degreeC_Type()
)
netBotz_prd_bot_ext_temp4_uV_per_degreeC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_uV_per_degreeC.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp4_uV_at_0_degreeC_Type = Integer32
_NetBotz_prd_bot_ext_temp4_uV_at_0_degreeC_Object = MibScalar
netBotz_prd_bot_ext_temp4_uV_at_0_degreeC = _NetBotz_prd_bot_ext_temp4_uV_at_0_degreeC_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 91),
    _NetBotz_prd_bot_ext_temp4_uV_at_0_degreeC_Type()
)
netBotz_prd_bot_ext_temp4_uV_at_0_degreeC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_uV_at_0_degreeC.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp4_min_range_Type = Integer32
_NetBotz_prd_bot_ext_temp4_min_range_Object = MibScalar
netBotz_prd_bot_ext_temp4_min_range = _NetBotz_prd_bot_ext_temp4_min_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 92),
    _NetBotz_prd_bot_ext_temp4_min_range_Type()
)
netBotz_prd_bot_ext_temp4_min_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_min_range.setStatus("mandatory")
_NetBotz_prd_bot_ext_temp4_max_range_Type = Integer32
_NetBotz_prd_bot_ext_temp4_max_range_Object = MibScalar
netBotz_prd_bot_ext_temp4_max_range = _NetBotz_prd_bot_ext_temp4_max_range_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 93),
    _NetBotz_prd_bot_ext_temp4_max_range_Type()
)
netBotz_prd_bot_ext_temp4_max_range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_max_range.setStatus("mandatory")
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
_NetBotz_prd_bot_ext_port4_module_id_Type = DisplayString
_NetBotz_prd_bot_ext_port4_module_id_Object = MibScalar
netBotz_prd_bot_ext_port4_module_id = _NetBotz_prd_bot_ext_port4_module_id_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 100),
    _NetBotz_prd_bot_ext_port4_module_id_Type()
)
netBotz_prd_bot_ext_port4_module_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_port4_module_id.setStatus("mandatory")
_NetBotz_prd_bot_ext_port4_module_type_Type = DisplayString
_NetBotz_prd_bot_ext_port4_module_type_Object = MibScalar
netBotz_prd_bot_ext_port4_module_type = _NetBotz_prd_bot_ext_port4_module_type_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 101),
    _NetBotz_prd_bot_ext_port4_module_type_Type()
)
netBotz_prd_bot_ext_port4_module_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_port4_module_type.setStatus("mandatory")
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
_NetBotz_prd_bot_ext_dry4_label_Type = DisplayString
_NetBotz_prd_bot_ext_dry4_label_Object = MibScalar
netBotz_prd_bot_ext_dry4_label = _NetBotz_prd_bot_ext_dry4_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 142),
    _NetBotz_prd_bot_ext_dry4_label_Type()
)
netBotz_prd_bot_ext_dry4_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry4_label.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry4_open_label_Type = DisplayString
_NetBotz_prd_bot_ext_dry4_open_label_Object = MibScalar
netBotz_prd_bot_ext_dry4_open_label = _NetBotz_prd_bot_ext_dry4_open_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 143),
    _NetBotz_prd_bot_ext_dry4_open_label_Type()
)
netBotz_prd_bot_ext_dry4_open_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry4_open_label.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry4_closed_label_Type = DisplayString
_NetBotz_prd_bot_ext_dry4_closed_label_Object = MibScalar
netBotz_prd_bot_ext_dry4_closed_label = _NetBotz_prd_bot_ext_dry4_closed_label_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 144),
    _NetBotz_prd_bot_ext_dry4_closed_label_Type()
)
netBotz_prd_bot_ext_dry4_closed_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry4_closed_label.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry4_open_to_close_millis_Type = Integer32
_NetBotz_prd_bot_ext_dry4_open_to_close_millis_Object = MibScalar
netBotz_prd_bot_ext_dry4_open_to_close_millis = _NetBotz_prd_bot_ext_dry4_open_to_close_millis_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 145),
    _NetBotz_prd_bot_ext_dry4_open_to_close_millis_Type()
)
netBotz_prd_bot_ext_dry4_open_to_close_millis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry4_open_to_close_millis.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry4_close_to_open_millis_Type = Integer32
_NetBotz_prd_bot_ext_dry4_close_to_open_millis_Object = MibScalar
netBotz_prd_bot_ext_dry4_close_to_open_millis = _NetBotz_prd_bot_ext_dry4_close_to_open_millis_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 146),
    _NetBotz_prd_bot_ext_dry4_close_to_open_millis_Type()
)
netBotz_prd_bot_ext_dry4_close_to_open_millis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry4_close_to_open_millis.setStatus("mandatory")
_NetBotz_prd_bot_ext_dry4_response_Type = DisplayString
_NetBotz_prd_bot_ext_dry4_response_Object = MibScalar
netBotz_prd_bot_ext_dry4_response = _NetBotz_prd_bot_ext_dry4_response_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 147),
    _NetBotz_prd_bot_ext_dry4_response_Type()
)
netBotz_prd_bot_ext_dry4_response.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry4_response.setStatus("mandatory")
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

# Managed Objects groups


# Notification objects

netBotz_prd_bot_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 0, 1)
)
netBotz_prd_bot_low_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 0, 2)
)
netBotz_prd_bot_high_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 0, 3)
)
netBotz_prd_bot_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_offline_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 0, 4)
)
netBotz_prd_bot_offline_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_offline_trap.setStatus(
        ""
    )

netBotz_prd_bot_online_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 10, 0, 5)
)
netBotz_prd_bot_online_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_online_trap.setStatus(
        ""
    )

netBotz_prd_bot_temperature_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 1, 0, 1)
)
netBotz_prd_bot_temperature_low_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_temperature_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_temperature_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 1, 0, 2)
)
netBotz_prd_bot_temperature_high_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_temperature_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_temperature_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 1, 0, 3)
)
netBotz_prd_bot_temperature_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_temperature_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_humidity_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 2, 0, 1)
)
netBotz_prd_bot_humidity_low_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_humidity_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_humidity_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 2, 0, 2)
)
netBotz_prd_bot_humidity_high_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_humidity_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_humidity_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 2, 0, 3)
)
netBotz_prd_bot_humidity_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_humidity_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_airflow_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 3, 0, 1)
)
netBotz_prd_bot_airflow_low_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_airflow_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_airflow_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 3, 0, 3)
)
netBotz_prd_bot_airflow_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_airflow_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_audio_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 4, 0, 2)
)
netBotz_prd_bot_audio_high_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_audio_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_audio_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 4, 0, 3)
)
netBotz_prd_bot_audio_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_audio_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_door_trap_tripped = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 5, 0, 2)
)
netBotz_prd_bot_door_trap_tripped.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_door_trap_tripped.setStatus(
        ""
    )

netBotz_prd_bot_door_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 5, 0, 3)
)
netBotz_prd_bot_door_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_door_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp1_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 6, 0, 1)
)
netBotz_prd_bot_amp1_low_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp1_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp1_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 6, 0, 2)
)
netBotz_prd_bot_amp1_high_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp1_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp1_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 6, 0, 3)
)
netBotz_prd_bot_amp1_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp1_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp1_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 6, 0, 6)
)
netBotz_prd_bot_amp1_sensor_unplugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp1_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_amp1_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 6, 0, 7)
)
netBotz_prd_bot_amp1_sensor_replugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp1_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_amp2_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 7, 0, 1)
)
netBotz_prd_bot_amp2_low_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp2_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp2_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 7, 0, 2)
)
netBotz_prd_bot_amp2_high_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp2_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp2_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 7, 0, 3)
)
netBotz_prd_bot_amp2_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp2_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp2_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 7, 0, 6)
)
netBotz_prd_bot_amp2_sensor_unplugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp2_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_amp2_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 7, 0, 7)
)
netBotz_prd_bot_amp2_sensor_replugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp2_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_amp3_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 8, 0, 1)
)
netBotz_prd_bot_amp3_low_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp3_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp3_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 8, 0, 2)
)
netBotz_prd_bot_amp3_high_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp3_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp3_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 8, 0, 3)
)
netBotz_prd_bot_amp3_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp3_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp3_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 8, 0, 6)
)
netBotz_prd_bot_amp3_sensor_unplugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp3_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_amp3_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 8, 0, 7)
)
netBotz_prd_bot_amp3_sensor_replugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp3_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_amp4_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 9, 0, 1)
)
netBotz_prd_bot_amp4_low_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp4_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp4_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 9, 0, 2)
)
netBotz_prd_bot_amp4_high_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp4_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp4_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 9, 0, 3)
)
netBotz_prd_bot_amp4_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp4_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_amp4_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 9, 0, 6)
)
netBotz_prd_bot_amp4_sensor_unplugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp4_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_amp4_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 9, 0, 7)
)
netBotz_prd_bot_amp4_sensor_replugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp4_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_amp_total_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 10, 0, 1)
)
netBotz_prd_bot_amp_total_low_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp_total_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp_total_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 10, 0, 2)
)
netBotz_prd_bot_amp_total_high_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp_total_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_amp_total_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 10, 0, 3)
)
netBotz_prd_bot_amp_total_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_amp_total_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp1_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 11, 0, 1)
)
netBotz_prd_bot_ext_temp1_low_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp1_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 11, 0, 2)
)
netBotz_prd_bot_ext_temp1_high_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp1_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 11, 0, 3)
)
netBotz_prd_bot_ext_temp1_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp1_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 11, 0, 6)
)
netBotz_prd_bot_ext_temp1_sensor_unplugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp1_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 11, 0, 7)
)
netBotz_prd_bot_ext_temp1_sensor_replugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp1_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp2_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 12, 0, 1)
)
netBotz_prd_bot_ext_temp2_low_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp2_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 12, 0, 2)
)
netBotz_prd_bot_ext_temp2_high_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp2_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 12, 0, 3)
)
netBotz_prd_bot_ext_temp2_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp2_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 12, 0, 6)
)
netBotz_prd_bot_ext_temp2_sensor_unplugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp2_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 12, 0, 7)
)
netBotz_prd_bot_ext_temp2_sensor_replugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp2_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp3_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 13, 0, 1)
)
netBotz_prd_bot_ext_temp3_low_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp3_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 13, 0, 2)
)
netBotz_prd_bot_ext_temp3_high_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp3_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 13, 0, 3)
)
netBotz_prd_bot_ext_temp3_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp3_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 13, 0, 6)
)
netBotz_prd_bot_ext_temp3_sensor_unplugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp3_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 13, 0, 7)
)
netBotz_prd_bot_ext_temp3_sensor_replugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp3_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp4_low_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 14, 0, 1)
)
netBotz_prd_bot_ext_temp4_low_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_low_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp4_high_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 14, 0, 2)
)
netBotz_prd_bot_ext_temp4_high_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_high_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp4_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 14, 0, 3)
)
netBotz_prd_bot_ext_temp4_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp4_sensor_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 14, 0, 6)
)
netBotz_prd_bot_ext_temp4_sensor_unplugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_sensor_unplugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_temp4_sensor_replugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 14, 0, 7)
)
netBotz_prd_bot_ext_temp4_sensor_replugged.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_temp4_sensor_replugged.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry1_triggered_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 15, 0, 2)
)
netBotz_prd_bot_ext_dry1_triggered_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry1_triggered_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry1_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 15, 0, 3)
)
netBotz_prd_bot_ext_dry1_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry1_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry2_triggered_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 16, 0, 2)
)
netBotz_prd_bot_ext_dry2_triggered_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry2_triggered_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry2_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 16, 0, 3)
)
netBotz_prd_bot_ext_dry2_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry2_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry3_triggered_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 17, 0, 2)
)
netBotz_prd_bot_ext_dry3_triggered_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry3_triggered_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry3_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 17, 0, 3)
)
netBotz_prd_bot_ext_dry3_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry3_trap_clear.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry4_triggered_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 18, 0, 2)
)
netBotz_prd_bot_ext_dry4_triggered_trap.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry4_triggered_trap.setStatus(
        ""
    )

netBotz_prd_bot_ext_dry4_trap_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 100, 18, 0, 3)
)
netBotz_prd_bot_ext_dry4_trap_clear.setObjects(
      *(("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_index"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_address"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_oid"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_value"),
        ("NETBOTZ-PRD-BOT-MIB", "netBotz_prd_bot_trap_date"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_bot_ext_dry4_trap_clear.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETBOTZ-PRD-BOT-MIB",
    **{"netBotz-prd-bot-low-trap": netBotz_prd_bot_low_trap,
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
       "netBotz-prd-bot-doorpic-delay": netBotz_prd_bot_doorpic_delay,
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
       "netBotz-prd-bot-ext-temp4": netBotz_prd_bot_ext_temp4,
       "netBotz-prd-bot-ext-temp1-enabled": netBotz_prd_bot_ext_temp1_enabled,
       "netBotz-prd-bot-ext-temp1-min": netBotz_prd_bot_ext_temp1_min,
       "netBotz-prd-bot-ext-temp1-max": netBotz_prd_bot_ext_temp1_max,
       "netBotz-prd-bot-ext-temp2-enabled": netBotz_prd_bot_ext_temp2_enabled,
       "netBotz-prd-bot-ext-temp2-min": netBotz_prd_bot_ext_temp2_min,
       "netBotz-prd-bot-ext-temp2-max": netBotz_prd_bot_ext_temp2_max,
       "netBotz-prd-bot-ext-temp3-enabled": netBotz_prd_bot_ext_temp3_enabled,
       "netBotz-prd-bot-ext-temp3-min": netBotz_prd_bot_ext_temp3_min,
       "netBotz-prd-bot-ext-temp3-max": netBotz_prd_bot_ext_temp3_max,
       "netBotz-prd-bot-ext-temp4-enabled": netBotz_prd_bot_ext_temp4_enabled,
       "netBotz-prd-bot-ext-temp4-min": netBotz_prd_bot_ext_temp4_min,
       "netBotz-prd-bot-ext-temp4-max": netBotz_prd_bot_ext_temp4_max,
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
       "netBotz-prd-bot-ext-temp4-uV-per-degreeC": netBotz_prd_bot_ext_temp4_uV_per_degreeC,
       "netBotz-prd-bot-ext-temp4-uV-at-0-degreeC": netBotz_prd_bot_ext_temp4_uV_at_0_degreeC,
       "netBotz-prd-bot-ext-temp4-min-range": netBotz_prd_bot_ext_temp4_min_range,
       "netBotz-prd-bot-ext-temp4-max-range": netBotz_prd_bot_ext_temp4_max_range,
       "netBotz-prd-bot-ext-port1-module-id": netBotz_prd_bot_ext_port1_module_id,
       "netBotz-prd-bot-ext-port1-module-type": netBotz_prd_bot_ext_port1_module_type,
       "netBotz-prd-bot-ext-port2-module-id": netBotz_prd_bot_ext_port2_module_id,
       "netBotz-prd-bot-ext-port2-module-type": netBotz_prd_bot_ext_port2_module_type,
       "netBotz-prd-bot-ext-port3-module-id": netBotz_prd_bot_ext_port3_module_id,
       "netBotz-prd-bot-ext-port3-module-type": netBotz_prd_bot_ext_port3_module_type,
       "netBotz-prd-bot-ext-port4-module-id": netBotz_prd_bot_ext_port4_module_id,
       "netBotz-prd-bot-ext-port4-module-type": netBotz_prd_bot_ext_port4_module_type,
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
       "netBotz-prd-bot-ext-dry4-label": netBotz_prd_bot_ext_dry4_label,
       "netBotz-prd-bot-ext-dry4-open-label": netBotz_prd_bot_ext_dry4_open_label,
       "netBotz-prd-bot-ext-dry4-closed-label": netBotz_prd_bot_ext_dry4_closed_label,
       "netBotz-prd-bot-ext-dry4-open-to-close-millis": netBotz_prd_bot_ext_dry4_open_to_close_millis,
       "netBotz-prd-bot-ext-dry4-close-to-open-millis": netBotz_prd_bot_ext_dry4_close_to_open_millis,
       "netBotz-prd-bot-ext-dry4-response": netBotz_prd_bot_ext_dry4_response,
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
       "netBotz-prd-bot-ext-dry4-trap-clear": netBotz_prd_bot_ext_dry4_trap_clear}
)
