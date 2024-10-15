# SNMP MIB module (EATON-EMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EATON-EMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:18 2024
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

(xupsEnvironment,) = mibBuilder.importSymbols(
    "EATON-OIDS",
    "xupsEnvironment")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

eatonEMPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 0)
)
eatonEMPMIB.setRevisions(
        ("2007-03-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EatonEMPConformance_ObjectIdentity = ObjectIdentity
eatonEMPConformance = _EatonEMPConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 0, 2)
)


class _XupsEnvRemoteTemp_Type(Integer32):
    """Custom type xupsEnvRemoteTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_XupsEnvRemoteTemp_Type.__name__ = "Integer32"
_XupsEnvRemoteTemp_Object = MibScalar
xupsEnvRemoteTemp = _XupsEnvRemoteTemp_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 5),
    _XupsEnvRemoteTemp_Type()
)
xupsEnvRemoteTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsEnvRemoteTemp.setStatus("current")
if mibBuilder.loadTexts:
    xupsEnvRemoteTemp.setUnits("degrees Centigrade")


class _XupsEnvRemoteHumidity_Type(Integer32):
    """Custom type xupsEnvRemoteHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XupsEnvRemoteHumidity_Type.__name__ = "Integer32"
_XupsEnvRemoteHumidity_Object = MibScalar
xupsEnvRemoteHumidity = _XupsEnvRemoteHumidity_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 6),
    _XupsEnvRemoteHumidity_Type()
)
xupsEnvRemoteHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsEnvRemoteHumidity.setStatus("current")
if mibBuilder.loadTexts:
    xupsEnvRemoteHumidity.setUnits("percent")


class _XupsEnvNumContacts_Type(Integer32):
    """Custom type xupsEnvNumContacts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_XupsEnvNumContacts_Type.__name__ = "Integer32"
_XupsEnvNumContacts_Object = MibScalar
xupsEnvNumContacts = _XupsEnvNumContacts_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 7),
    _XupsEnvNumContacts_Type()
)
xupsEnvNumContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsEnvNumContacts.setStatus("current")
_XupsContactSenseTable_Object = MibTable
xupsContactSenseTable = _XupsContactSenseTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 8)
)
if mibBuilder.loadTexts:
    xupsContactSenseTable.setStatus("current")
_XupsContactsTableEntry_Object = MibTableRow
xupsContactsTableEntry = _XupsContactsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1)
)
xupsContactsTableEntry.setIndexNames(
    (0, "EATON-EMP-MIB", "xupsContactIndex"),
)
if mibBuilder.loadTexts:
    xupsContactsTableEntry.setStatus("current")


class _XupsContactIndex_Type(Integer32):
    """Custom type xupsContactIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_XupsContactIndex_Type.__name__ = "Integer32"
_XupsContactIndex_Object = MibTableColumn
xupsContactIndex = _XupsContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 1),
    _XupsContactIndex_Type()
)
xupsContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsContactIndex.setStatus("current")


class _XupsContactType_Type(Integer32):
    """Custom type xupsContactType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("anyChange", 3),
          ("normallyClosed", 2),
          ("normallyOpen", 1),
          ("notUsed", 4))
    )


_XupsContactType_Type.__name__ = "Integer32"
_XupsContactType_Object = MibTableColumn
xupsContactType = _XupsContactType_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 2),
    _XupsContactType_Type()
)
xupsContactType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsContactType.setStatus("current")


class _XupsContactState_Type(Integer32):
    """Custom type xupsContactState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("closedWithNotice", 4),
          ("open", 1),
          ("openWithNotice", 3))
    )


_XupsContactState_Type.__name__ = "Integer32"
_XupsContactState_Object = MibTableColumn
xupsContactState = _XupsContactState_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 3),
    _XupsContactState_Type()
)
xupsContactState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsContactState.setStatus("current")


class _XupsContactDescr_Type(DisplayString):
    """Custom type xupsContactDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_XupsContactDescr_Type.__name__ = "DisplayString"
_XupsContactDescr_Object = MibTableColumn
xupsContactDescr = _XupsContactDescr_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 4),
    _XupsContactDescr_Type()
)
xupsContactDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsContactDescr.setStatus("current")


class _XupsEnvRemoteTempLowerLimit_Type(Integer32):
    """Custom type xupsEnvRemoteTempLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_XupsEnvRemoteTempLowerLimit_Type.__name__ = "Integer32"
_XupsEnvRemoteTempLowerLimit_Object = MibScalar
xupsEnvRemoteTempLowerLimit = _XupsEnvRemoteTempLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 9),
    _XupsEnvRemoteTempLowerLimit_Type()
)
xupsEnvRemoteTempLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsEnvRemoteTempLowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    xupsEnvRemoteTempLowerLimit.setUnits("degrees Centigrade")


class _XupsEnvRemoteTempUpperLimit_Type(Integer32):
    """Custom type xupsEnvRemoteTempUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_XupsEnvRemoteTempUpperLimit_Type.__name__ = "Integer32"
_XupsEnvRemoteTempUpperLimit_Object = MibScalar
xupsEnvRemoteTempUpperLimit = _XupsEnvRemoteTempUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 10),
    _XupsEnvRemoteTempUpperLimit_Type()
)
xupsEnvRemoteTempUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsEnvRemoteTempUpperLimit.setStatus("current")
if mibBuilder.loadTexts:
    xupsEnvRemoteTempUpperLimit.setUnits("degrees Centigrade")


class _XupsEnvRemoteHumidityLowerLimit_Type(Integer32):
    """Custom type xupsEnvRemoteHumidityLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XupsEnvRemoteHumidityLowerLimit_Type.__name__ = "Integer32"
_XupsEnvRemoteHumidityLowerLimit_Object = MibScalar
xupsEnvRemoteHumidityLowerLimit = _XupsEnvRemoteHumidityLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 11),
    _XupsEnvRemoteHumidityLowerLimit_Type()
)
xupsEnvRemoteHumidityLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsEnvRemoteHumidityLowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    xupsEnvRemoteHumidityLowerLimit.setUnits("percent")


class _XupsEnvRemoteHumidityUpperLimit_Type(Integer32):
    """Custom type xupsEnvRemoteHumidityUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XupsEnvRemoteHumidityUpperLimit_Type.__name__ = "Integer32"
_XupsEnvRemoteHumidityUpperLimit_Object = MibScalar
xupsEnvRemoteHumidityUpperLimit = _XupsEnvRemoteHumidityUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 12),
    _XupsEnvRemoteHumidityUpperLimit_Type()
)
xupsEnvRemoteHumidityUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsEnvRemoteHumidityUpperLimit.setStatus("current")
if mibBuilder.loadTexts:
    xupsEnvRemoteHumidityUpperLimit.setUnits("percent")

# Managed Objects groups

eatonEMPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 0, 2, 1)
)
eatonEMPGroup.setObjects(
      *(("EATON-EMP-MIB", "xupsEnvRemoteTemp"),
        ("EATON-EMP-MIB", "xupsEnvRemoteHumidity"),
        ("EATON-EMP-MIB", "xupsEnvRemoteTempLowerLimit"),
        ("EATON-EMP-MIB", "xupsEnvRemoteTempUpperLimit"),
        ("EATON-EMP-MIB", "xupsEnvRemoteHumidityLowerLimit"),
        ("EATON-EMP-MIB", "xupsEnvRemoteHumidityUpperLimit"))
)
if mibBuilder.loadTexts:
    eatonEMPGroup.setStatus("current")

eatonEMPTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 0, 2, 2)
)
eatonEMPTableGroup.setObjects(
      *(("EATON-EMP-MIB", "xupsEnvNumContacts"),
        ("EATON-EMP-MIB", "xupsContactIndex"),
        ("EATON-EMP-MIB", "xupsContactType"),
        ("EATON-EMP-MIB", "xupsContactState"),
        ("EATON-EMP-MIB", "xupsContactDescr"))
)
if mibBuilder.loadTexts:
    eatonEMPTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

eatonEMPSimpleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 0, 2, 4)
)
if mibBuilder.loadTexts:
    eatonEMPSimpleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EATON-EMP-MIB",
    **{"eatonEMPMIB": eatonEMPMIB,
       "eatonEMPConformance": eatonEMPConformance,
       "eatonEMPGroup": eatonEMPGroup,
       "eatonEMPTableGroup": eatonEMPTableGroup,
       "eatonEMPSimpleCompliance": eatonEMPSimpleCompliance,
       "xupsEnvRemoteTemp": xupsEnvRemoteTemp,
       "xupsEnvRemoteHumidity": xupsEnvRemoteHumidity,
       "xupsEnvNumContacts": xupsEnvNumContacts,
       "xupsContactSenseTable": xupsContactSenseTable,
       "xupsContactsTableEntry": xupsContactsTableEntry,
       "xupsContactIndex": xupsContactIndex,
       "xupsContactType": xupsContactType,
       "xupsContactState": xupsContactState,
       "xupsContactDescr": xupsContactDescr,
       "xupsEnvRemoteTempLowerLimit": xupsEnvRemoteTempLowerLimit,
       "xupsEnvRemoteTempUpperLimit": xupsEnvRemoteTempUpperLimit,
       "xupsEnvRemoteHumidityLowerLimit": xupsEnvRemoteHumidityLowerLimit,
       "xupsEnvRemoteHumidityUpperLimit": xupsEnvRemoteHumidityUpperLimit}
)
