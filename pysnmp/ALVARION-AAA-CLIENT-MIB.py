# SNMP MIB module (ALVARION-AAA-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-AAA-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:29 2024
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

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

(AlvarionProfileIndex,
 AlvarionServerIndex,
 AlvarionServerIndexOrZero) = mibBuilder.importSymbols(
    "ALVARION-TC",
    "AlvarionProfileIndex",
    "AlvarionServerIndex",
    "AlvarionServerIndexOrZero")

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

alvarionAAAClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionAAAClientObjects_ObjectIdentity = ObjectIdentity
alvarionAAAClientObjects = _AlvarionAAAClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1)
)
_AlvarionAAAProfileGroup_ObjectIdentity = ObjectIdentity
alvarionAAAProfileGroup = _AlvarionAAAProfileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1)
)
_AlvarionAAAProfileTable_Object = MibTable
alvarionAAAProfileTable = _AlvarionAAAProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alvarionAAAProfileTable.setStatus("current")
_AlvarionAAAProfileEntry_Object = MibTableRow
alvarionAAAProfileEntry = _AlvarionAAAProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1, 1, 1)
)
alvarionAAAProfileEntry.setIndexNames(
    (0, "ALVARION-AAA-CLIENT-MIB", "alvarionAAAProfileIndex"),
)
if mibBuilder.loadTexts:
    alvarionAAAProfileEntry.setStatus("current")
_AlvarionAAAProfileIndex_Type = AlvarionProfileIndex
_AlvarionAAAProfileIndex_Object = MibTableColumn
alvarionAAAProfileIndex = _AlvarionAAAProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1, 1, 1, 1),
    _AlvarionAAAProfileIndex_Type()
)
alvarionAAAProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alvarionAAAProfileIndex.setStatus("current")
_AlvarionAAAProfileName_Type = DisplayString
_AlvarionAAAProfileName_Object = MibTableColumn
alvarionAAAProfileName = _AlvarionAAAProfileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1, 1, 1, 2),
    _AlvarionAAAProfileName_Type()
)
alvarionAAAProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alvarionAAAProfileName.setStatus("current")
_AlvarionAAAProfilePrimaryServerIndex_Type = AlvarionServerIndexOrZero
_AlvarionAAAProfilePrimaryServerIndex_Object = MibTableColumn
alvarionAAAProfilePrimaryServerIndex = _AlvarionAAAProfilePrimaryServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1, 1, 1, 3),
    _AlvarionAAAProfilePrimaryServerIndex_Type()
)
alvarionAAAProfilePrimaryServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alvarionAAAProfilePrimaryServerIndex.setStatus("current")
_AlvarionAAAProfileSecondaryServerIndex_Type = AlvarionServerIndexOrZero
_AlvarionAAAProfileSecondaryServerIndex_Object = MibTableColumn
alvarionAAAProfileSecondaryServerIndex = _AlvarionAAAProfileSecondaryServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1, 1, 1, 4),
    _AlvarionAAAProfileSecondaryServerIndex_Type()
)
alvarionAAAProfileSecondaryServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alvarionAAAProfileSecondaryServerIndex.setStatus("current")
_AlvarionAAAServerGroup_ObjectIdentity = ObjectIdentity
alvarionAAAServerGroup = _AlvarionAAAServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2)
)
_AlvarionAAAServerTable_Object = MibTable
alvarionAAAServerTable = _AlvarionAAAServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alvarionAAAServerTable.setStatus("current")
_AlvarionAAAServerEntry_Object = MibTableRow
alvarionAAAServerEntry = _AlvarionAAAServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1)
)
alvarionAAAServerEntry.setIndexNames(
    (0, "ALVARION-AAA-CLIENT-MIB", "alvarionAAAServerIndex"),
)
if mibBuilder.loadTexts:
    alvarionAAAServerEntry.setStatus("current")
_AlvarionAAAServerIndex_Type = AlvarionServerIndex
_AlvarionAAAServerIndex_Object = MibTableColumn
alvarionAAAServerIndex = _AlvarionAAAServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 1),
    _AlvarionAAAServerIndex_Type()
)
alvarionAAAServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alvarionAAAServerIndex.setStatus("current")


class _AlvarionAAAAuthenProtocol_Type(Integer32):
    """Custom type alvarionAAAAuthenProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("radius", 1)
    )


_AlvarionAAAAuthenProtocol_Type.__name__ = "Integer32"
_AlvarionAAAAuthenProtocol_Object = MibTableColumn
alvarionAAAAuthenProtocol = _AlvarionAAAAuthenProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 2),
    _AlvarionAAAAuthenProtocol_Type()
)
alvarionAAAAuthenProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alvarionAAAAuthenProtocol.setStatus("current")


class _AlvarionAAAAuthenMethod_Type(Integer32):
    """Custom type alvarionAAAAuthenMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("eapMd5", 5),
          ("mschap", 3),
          ("mschapv2", 4),
          ("pap", 1))
    )


_AlvarionAAAAuthenMethod_Type.__name__ = "Integer32"
_AlvarionAAAAuthenMethod_Object = MibTableColumn
alvarionAAAAuthenMethod = _AlvarionAAAAuthenMethod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 3),
    _AlvarionAAAAuthenMethod_Type()
)
alvarionAAAAuthenMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alvarionAAAAuthenMethod.setStatus("current")


class _AlvarionAAAServerName_Type(OctetString):
    """Custom type alvarionAAAServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AlvarionAAAServerName_Type.__name__ = "OctetString"
_AlvarionAAAServerName_Object = MibTableColumn
alvarionAAAServerName = _AlvarionAAAServerName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 4),
    _AlvarionAAAServerName_Type()
)
alvarionAAAServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alvarionAAAServerName.setStatus("current")
_AlvarionAAASharedSecret_Type = DisplayString
_AlvarionAAASharedSecret_Object = MibTableColumn
alvarionAAASharedSecret = _AlvarionAAASharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 5),
    _AlvarionAAASharedSecret_Type()
)
alvarionAAASharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alvarionAAASharedSecret.setStatus("current")


class _AlvarionAAAAuthenticationPort_Type(Integer32):
    """Custom type alvarionAAAAuthenticationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlvarionAAAAuthenticationPort_Type.__name__ = "Integer32"
_AlvarionAAAAuthenticationPort_Object = MibTableColumn
alvarionAAAAuthenticationPort = _AlvarionAAAAuthenticationPort_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 6),
    _AlvarionAAAAuthenticationPort_Type()
)
alvarionAAAAuthenticationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alvarionAAAAuthenticationPort.setStatus("current")


class _AlvarionAAAAccountingPort_Type(Integer32):
    """Custom type alvarionAAAAccountingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlvarionAAAAccountingPort_Type.__name__ = "Integer32"
_AlvarionAAAAccountingPort_Object = MibTableColumn
alvarionAAAAccountingPort = _AlvarionAAAAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 7),
    _AlvarionAAAAccountingPort_Type()
)
alvarionAAAAccountingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alvarionAAAAccountingPort.setStatus("current")


class _AlvarionAAATimeout_Type(Integer32):
    """Custom type alvarionAAATimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_AlvarionAAATimeout_Type.__name__ = "Integer32"
_AlvarionAAATimeout_Object = MibTableColumn
alvarionAAATimeout = _AlvarionAAATimeout_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 8),
    _AlvarionAAATimeout_Type()
)
alvarionAAATimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alvarionAAATimeout.setStatus("current")
if mibBuilder.loadTexts:
    alvarionAAATimeout.setUnits("seconds")


class _AlvarionAAANASId_Type(OctetString):
    """Custom type alvarionAAANASId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_AlvarionAAANASId_Type.__name__ = "OctetString"
_AlvarionAAANASId_Object = MibTableColumn
alvarionAAANASId = _AlvarionAAANASId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 9),
    _AlvarionAAANASId_Type()
)
alvarionAAANASId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alvarionAAANASId.setStatus("current")
_AlvarionAAAClientMIBConformance_ObjectIdentity = ObjectIdentity
alvarionAAAClientMIBConformance = _AlvarionAAAClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 2)
)
_AlvarionAAAClientMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionAAAClientMIBCompliances = _AlvarionAAAClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 2, 1)
)
_AlvarionAAAClientMIBGroups_ObjectIdentity = ObjectIdentity
alvarionAAAClientMIBGroups = _AlvarionAAAClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 2, 2)
)

# Managed Objects groups

alvarionAAAProfileMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 2, 2, 1)
)
alvarionAAAProfileMIBGroup.setObjects(
      *(("ALVARION-AAA-CLIENT-MIB", "alvarionAAAProfileName"),
        ("ALVARION-AAA-CLIENT-MIB", "alvarionAAAProfilePrimaryServerIndex"),
        ("ALVARION-AAA-CLIENT-MIB", "alvarionAAAProfileSecondaryServerIndex"))
)
if mibBuilder.loadTexts:
    alvarionAAAProfileMIBGroup.setStatus("current")

alvarionAAAClientMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 2, 2, 2)
)
alvarionAAAClientMIBGroup.setObjects(
      *(("ALVARION-AAA-CLIENT-MIB", "alvarionAAAAuthenProtocol"),
        ("ALVARION-AAA-CLIENT-MIB", "alvarionAAAAuthenMethod"),
        ("ALVARION-AAA-CLIENT-MIB", "alvarionAAAServerName"),
        ("ALVARION-AAA-CLIENT-MIB", "alvarionAAASharedSecret"),
        ("ALVARION-AAA-CLIENT-MIB", "alvarionAAAAuthenticationPort"),
        ("ALVARION-AAA-CLIENT-MIB", "alvarionAAAAccountingPort"),
        ("ALVARION-AAA-CLIENT-MIB", "alvarionAAATimeout"),
        ("ALVARION-AAA-CLIENT-MIB", "alvarionAAANASId"))
)
if mibBuilder.loadTexts:
    alvarionAAAClientMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alvarionAAAClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alvarionAAAClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-AAA-CLIENT-MIB",
    **{"alvarionAAAClientMIB": alvarionAAAClientMIB,
       "alvarionAAAClientObjects": alvarionAAAClientObjects,
       "alvarionAAAProfileGroup": alvarionAAAProfileGroup,
       "alvarionAAAProfileTable": alvarionAAAProfileTable,
       "alvarionAAAProfileEntry": alvarionAAAProfileEntry,
       "alvarionAAAProfileIndex": alvarionAAAProfileIndex,
       "alvarionAAAProfileName": alvarionAAAProfileName,
       "alvarionAAAProfilePrimaryServerIndex": alvarionAAAProfilePrimaryServerIndex,
       "alvarionAAAProfileSecondaryServerIndex": alvarionAAAProfileSecondaryServerIndex,
       "alvarionAAAServerGroup": alvarionAAAServerGroup,
       "alvarionAAAServerTable": alvarionAAAServerTable,
       "alvarionAAAServerEntry": alvarionAAAServerEntry,
       "alvarionAAAServerIndex": alvarionAAAServerIndex,
       "alvarionAAAAuthenProtocol": alvarionAAAAuthenProtocol,
       "alvarionAAAAuthenMethod": alvarionAAAAuthenMethod,
       "alvarionAAAServerName": alvarionAAAServerName,
       "alvarionAAASharedSecret": alvarionAAASharedSecret,
       "alvarionAAAAuthenticationPort": alvarionAAAAuthenticationPort,
       "alvarionAAAAccountingPort": alvarionAAAAccountingPort,
       "alvarionAAATimeout": alvarionAAATimeout,
       "alvarionAAANASId": alvarionAAANASId,
       "alvarionAAAClientMIBConformance": alvarionAAAClientMIBConformance,
       "alvarionAAAClientMIBCompliances": alvarionAAAClientMIBCompliances,
       "alvarionAAAClientMIBCompliance": alvarionAAAClientMIBCompliance,
       "alvarionAAAClientMIBGroups": alvarionAAAClientMIBGroups,
       "alvarionAAAProfileMIBGroup": alvarionAAAProfileMIBGroup,
       "alvarionAAAClientMIBGroup": alvarionAAAClientMIBGroup}
)
