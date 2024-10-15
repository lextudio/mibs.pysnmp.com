# SNMP MIB module (FSS-SYSTEM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FSS-SYSTEM
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:41 2024
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

(fssCommon,) = mibBuilder.importSymbols(
    "FSS-COMMON-SMI",
    "fssCommon")

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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fssSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100)
)
fssSystem.setRevisions(
        ("2016-06-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class String(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class ADT_value(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("adt-ten", 1),
          ("adt-zero", 0))
    )



class RestartLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cold", 0),
          ("warm", 1))
    )



class AAT_value(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aat-twoPointFive", 1),
          ("aat-zero", 0))
    )



# MIB Managed Objects in the order of their OIDs

_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1)
)
_SystemVendor_Type = String
_SystemVendor_Object = MibScalar
systemVendor = _SystemVendor_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 1),
    _SystemVendor_Type()
)
systemVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVendor.setStatus("current")


class _SystemName_Type(String):
    """Custom type systemName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 20),
    )


_SystemName_Type.__name__ = "String"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 2),
    _SystemName_Type()
)
systemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemName.setStatus("current")
_SystemLocation_Type = String
_SystemLocation_Object = MibScalar
systemLocation = _SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 3),
    _SystemLocation_Type()
)
systemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLocation.setStatus("current")
_SystemContact_Type = String
_SystemContact_Object = MibScalar
systemContact = _SystemContact_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 4),
    _SystemContact_Type()
)
systemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemContact.setStatus("current")
_SystemNeType_Type = String
_SystemNeType_Object = MibScalar
systemNeType = _SystemNeType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 5),
    _SystemNeType_Type()
)
systemNeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNeType.setStatus("current")
_SystemSoftwareVersion_Type = String
_SystemSoftwareVersion_Object = MibScalar
systemSoftwareVersion = _SystemSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 6),
    _SystemSoftwareVersion_Type()
)
systemSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSoftwareVersion.setStatus("current")
_SystemUpTime_Type = Unsigned32
_SystemUpTime_Object = MibScalar
systemUpTime = _SystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 7),
    _SystemUpTime_Type()
)
systemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpTime.setStatus("current")
_SystemAutoP_Type = TruthValue
_SystemAutoP_Object = MibScalar
systemAutoP = _SystemAutoP_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 8),
    _SystemAutoP_Type()
)
systemAutoP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAutoP.setStatus("current")
_SystemAAT_Type = AAT_value
_SystemAAT_Object = MibScalar
systemAAT = _SystemAAT_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 9),
    _SystemAAT_Type()
)
systemAAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAAT.setStatus("current")
_SystemADT_Type = ADT_value
_SystemADT_Object = MibScalar
systemADT = _SystemADT_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 10),
    _SystemADT_Type()
)
systemADT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemADT.setStatus("current")
_SystemClock_ObjectIdentity = ObjectIdentity
systemClock = _SystemClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 11)
)
_SystemClockTimezone_name_Type = String
_SystemClockTimezone_name_Object = MibScalar
systemClockTimezone_name = _SystemClockTimezone_name_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 11, 1),
    _SystemClockTimezone_name_Type()
)
systemClockTimezone_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemClockTimezone_name.setStatus("current")
_SystemNtp_Type = TruthValue
_SystemNtp_Object = MibScalar
systemNtp = _SystemNtp_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 12),
    _SystemNtp_Type()
)
systemNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNtp.setStatus("current")
_SystemNtpEnabled_Type = TruthValue
_SystemNtpEnabled_Object = MibScalar
systemNtpEnabled = _SystemNtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 13),
    _SystemNtpEnabled_Type()
)
systemNtpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNtpEnabled.setStatus("current")
_SystemNtp_cfg_Type = TruthValue
_SystemNtp_cfg_Object = MibScalar
systemNtp_cfg = _SystemNtp_cfg_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 14),
    _SystemNtp_cfg_Type()
)
systemNtp_cfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNtp_cfg.setStatus("current")
_SystemNtp_cfgNtp_enabled_Type = TruthValue
_SystemNtp_cfgNtp_enabled_Object = MibScalar
systemNtp_cfgNtp_enabled = _SystemNtp_cfgNtp_enabled_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 15),
    _SystemNtp_cfgNtp_enabled_Type()
)
systemNtp_cfgNtp_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNtp_cfgNtp_enabled.setStatus("current")
_System_state_ObjectIdentity = ObjectIdentity
system_state = _System_state_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 2)
)
_System_stateClock_ObjectIdentity = ObjectIdentity
system_stateClock = _System_stateClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 2, 1)
)
_System_stateClockDatetime_Type = String
_System_stateClockDatetime_Object = MibScalar
system_stateClockDatetime = _System_stateClockDatetime_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 2, 1, 1),
    _System_stateClockDatetime_Type()
)
system_stateClockDatetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    system_stateClockDatetime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSS-SYSTEM",
    **{"String": String,
       "ADT-value": ADT_value,
       "RestartLevel": RestartLevel,
       "AAT-value": AAT_value,
       "fssSystem": fssSystem,
       "system": system,
       "systemVendor": systemVendor,
       "systemName": systemName,
       "systemLocation": systemLocation,
       "systemContact": systemContact,
       "systemNeType": systemNeType,
       "systemSoftwareVersion": systemSoftwareVersion,
       "systemUpTime": systemUpTime,
       "systemAutoP": systemAutoP,
       "systemAAT": systemAAT,
       "systemADT": systemADT,
       "systemClock": systemClock,
       "systemClockTimezone-name": systemClockTimezone_name,
       "systemNtp": systemNtp,
       "systemNtpEnabled": systemNtpEnabled,
       "systemNtp-cfg": systemNtp_cfg,
       "systemNtp-cfgNtp-enabled": systemNtp_cfgNtp_enabled,
       "system-state": system_state,
       "system-stateClock": system_stateClock,
       "system-stateClockDatetime": system_stateClockDatetime}
)
