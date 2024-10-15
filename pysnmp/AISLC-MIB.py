# SNMP MIB module (AISLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:18 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aiSLC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSLCSystem_ObjectIdentity = ObjectIdentity
aiSLCSystem = _AiSLCSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 10, 1)
)


class _AislcAdminStatus_Type(Integer32):
    """Custom type aislcAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 2),
          ("up", 1))
    )


_AislcAdminStatus_Type.__name__ = "Integer32"
_AislcAdminStatus_Object = MibScalar
aislcAdminStatus = _AislcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 10, 1, 1),
    _AislcAdminStatus_Type()
)
aislcAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcAdminStatus.setStatus("current")


class _AislcAdminPush_Type(Integer32):
    """Custom type aislcAdminPush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("push", 2),
          ("ready", 1))
    )


_AislcAdminPush_Type.__name__ = "Integer32"
_AislcAdminPush_Object = MibScalar
aislcAdminPush = _AislcAdminPush_Object(
    (1, 3, 6, 1, 4, 1, 539, 10, 1, 2),
    _AislcAdminPush_Type()
)
aislcAdminPush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcAdminPush.setStatus("current")


class _AislcOperBaseport_Type(Integer32):
    """Custom type aislcOperBaseport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AislcOperBaseport_Type.__name__ = "Integer32"
_AislcOperBaseport_Object = MibScalar
aislcOperBaseport = _AislcOperBaseport_Object(
    (1, 3, 6, 1, 4, 1, 539, 10, 1, 3),
    _AislcOperBaseport_Type()
)
aislcOperBaseport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcOperBaseport.setStatus("current")
_AislcLastConfigTime_Type = TimeTicks
_AislcLastConfigTime_Object = MibScalar
aislcLastConfigTime = _AislcLastConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 539, 10, 1, 4),
    _AislcLastConfigTime_Type()
)
aislcLastConfigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcLastConfigTime.setStatus("current")


class _AislcAdminResetAlarm_Type(Integer32):
    """Custom type aislcAdminResetAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 3),
          ("normal", 1),
          ("reset", 2))
    )


_AislcAdminResetAlarm_Type.__name__ = "Integer32"
_AislcAdminResetAlarm_Object = MibScalar
aislcAdminResetAlarm = _AislcAdminResetAlarm_Object(
    (1, 3, 6, 1, 4, 1, 539, 10, 1, 5),
    _AislcAdminResetAlarm_Type()
)
aislcAdminResetAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcAdminResetAlarm.setStatus("current")


class _AislcFirmwareVersion_Type(DisplayString):
    """Custom type aislcFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 11),
    )


_AislcFirmwareVersion_Type.__name__ = "DisplayString"
_AislcFirmwareVersion_Object = MibScalar
aislcFirmwareVersion = _AislcFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 539, 10, 1, 6),
    _AislcFirmwareVersion_Type()
)
aislcFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcFirmwareVersion.setStatus("current")


class _AislcProductName_Type(DisplayString):
    """Custom type aislcProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 40),
    )


_AislcProductName_Type.__name__ = "DisplayString"
_AislcProductName_Object = MibScalar
aislcProductName = _AislcProductName_Object(
    (1, 3, 6, 1, 4, 1, 539, 10, 1, 7),
    _AislcProductName_Type()
)
aislcProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcProductName.setStatus("current")


class _AislcRomIdImageId_Type(DisplayString):
    """Custom type aislcRomIdImageId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AislcRomIdImageId_Type.__name__ = "DisplayString"
_AislcRomIdImageId_Object = MibScalar
aislcRomIdImageId = _AislcRomIdImageId_Object(
    (1, 3, 6, 1, 4, 1, 539, 10, 1, 8),
    _AislcRomIdImageId_Type()
)
aislcRomIdImageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcRomIdImageId.setStatus("current")
_AislcRomIdTimeDate_Type = DateAndTime
_AislcRomIdTimeDate_Object = MibScalar
aislcRomIdTimeDate = _AislcRomIdTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 539, 10, 1, 9),
    _AislcRomIdTimeDate_Type()
)
aislcRomIdTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcRomIdTimeDate.setStatus("current")
_AislcRomIdSelFeatTable_Object = MibTable
aislcRomIdSelFeatTable = _AislcRomIdSelFeatTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 10, 1, 10)
)
if mibBuilder.loadTexts:
    aislcRomIdSelFeatTable.setStatus("current")
_AislcRomIdSelFeatTableEntry_Object = MibTableRow
aislcRomIdSelFeatTableEntry = _AislcRomIdSelFeatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 10, 1, 10, 1)
)
aislcRomIdSelFeatTableEntry.setIndexNames(
    (0, "AISLC-MIB", "aislcRomIdSelFeatName"),
)
if mibBuilder.loadTexts:
    aislcRomIdSelFeatTableEntry.setStatus("current")
_AislcRomIdSelFeatName_Type = DisplayString
_AislcRomIdSelFeatName_Object = MibTableColumn
aislcRomIdSelFeatName = _AislcRomIdSelFeatName_Object(
    (1, 3, 6, 1, 4, 1, 539, 10, 1, 10, 1, 1),
    _AislcRomIdSelFeatName_Type()
)
aislcRomIdSelFeatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcRomIdSelFeatName.setStatus("current")
_AislcRomIdSelFeatEnabled_Type = TruthValue
_AislcRomIdSelFeatEnabled_Object = MibTableColumn
aislcRomIdSelFeatEnabled = _AislcRomIdSelFeatEnabled_Object(
    (1, 3, 6, 1, 4, 1, 539, 10, 1, 10, 1, 2),
    _AislcRomIdSelFeatEnabled_Type()
)
aislcRomIdSelFeatEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcRomIdSelFeatEnabled.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISLC-MIB",
    **{"aii": aii,
       "aiSLC": aiSLC,
       "aiSLCSystem": aiSLCSystem,
       "aislcAdminStatus": aislcAdminStatus,
       "aislcAdminPush": aislcAdminPush,
       "aislcOperBaseport": aislcOperBaseport,
       "aislcLastConfigTime": aislcLastConfigTime,
       "aislcAdminResetAlarm": aislcAdminResetAlarm,
       "aislcFirmwareVersion": aislcFirmwareVersion,
       "aislcProductName": aislcProductName,
       "aislcRomIdImageId": aislcRomIdImageId,
       "aislcRomIdTimeDate": aislcRomIdTimeDate,
       "aislcRomIdSelFeatTable": aislcRomIdSelFeatTable,
       "aislcRomIdSelFeatTableEntry": aislcRomIdSelFeatTableEntry,
       "aislcRomIdSelFeatName": aislcRomIdSelFeatName,
       "aislcRomIdSelFeatEnabled": aislcRomIdSelFeatEnabled}
)
