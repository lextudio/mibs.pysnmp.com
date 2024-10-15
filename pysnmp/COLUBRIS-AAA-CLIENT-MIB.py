# SNMP MIB module (COLUBRIS-AAA-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-AAA-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:10 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

(ColubrisProfileIndex,
 ColubrisServerIndex,
 ColubrisServerIndexOrZero) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisProfileIndex",
    "ColubrisServerIndex",
    "ColubrisServerIndexOrZero")

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

colubrisAAAClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisAAAClientObjects_ObjectIdentity = ObjectIdentity
colubrisAAAClientObjects = _ColubrisAAAClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1)
)
_ColubrisAAAProfileGroup_ObjectIdentity = ObjectIdentity
colubrisAAAProfileGroup = _ColubrisAAAProfileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1)
)
_ColubrisAAAProfileTable_Object = MibTable
colubrisAAAProfileTable = _ColubrisAAAProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisAAAProfileTable.setStatus("current")
_ColubrisAAAProfileEntry_Object = MibTableRow
colubrisAAAProfileEntry = _ColubrisAAAProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1, 1, 1)
)
colubrisAAAProfileEntry.setIndexNames(
    (0, "COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAProfileIndex"),
)
if mibBuilder.loadTexts:
    colubrisAAAProfileEntry.setStatus("current")
_ColubrisAAAProfileIndex_Type = ColubrisProfileIndex
_ColubrisAAAProfileIndex_Object = MibTableColumn
colubrisAAAProfileIndex = _ColubrisAAAProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1, 1, 1, 1),
    _ColubrisAAAProfileIndex_Type()
)
colubrisAAAProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    colubrisAAAProfileIndex.setStatus("current")
_ColubrisAAAProfileName_Type = DisplayString
_ColubrisAAAProfileName_Object = MibTableColumn
colubrisAAAProfileName = _ColubrisAAAProfileName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1, 1, 1, 2),
    _ColubrisAAAProfileName_Type()
)
colubrisAAAProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colubrisAAAProfileName.setStatus("current")
_ColubrisAAAProfilePrimaryServerIndex_Type = ColubrisServerIndexOrZero
_ColubrisAAAProfilePrimaryServerIndex_Object = MibTableColumn
colubrisAAAProfilePrimaryServerIndex = _ColubrisAAAProfilePrimaryServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1, 1, 1, 3),
    _ColubrisAAAProfilePrimaryServerIndex_Type()
)
colubrisAAAProfilePrimaryServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisAAAProfilePrimaryServerIndex.setStatus("current")
_ColubrisAAAProfileSecondaryServerIndex_Type = ColubrisServerIndexOrZero
_ColubrisAAAProfileSecondaryServerIndex_Object = MibTableColumn
colubrisAAAProfileSecondaryServerIndex = _ColubrisAAAProfileSecondaryServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1, 1, 1, 4),
    _ColubrisAAAProfileSecondaryServerIndex_Type()
)
colubrisAAAProfileSecondaryServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisAAAProfileSecondaryServerIndex.setStatus("current")
_ColubrisAAAServerGroup_ObjectIdentity = ObjectIdentity
colubrisAAAServerGroup = _ColubrisAAAServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2)
)
_ColubrisAAAServerTable_Object = MibTable
colubrisAAAServerTable = _ColubrisAAAServerTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    colubrisAAAServerTable.setStatus("current")
_ColubrisAAAServerEntry_Object = MibTableRow
colubrisAAAServerEntry = _ColubrisAAAServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1)
)
colubrisAAAServerEntry.setIndexNames(
    (0, "COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAServerIndex"),
)
if mibBuilder.loadTexts:
    colubrisAAAServerEntry.setStatus("current")
_ColubrisAAAServerIndex_Type = ColubrisServerIndex
_ColubrisAAAServerIndex_Object = MibTableColumn
colubrisAAAServerIndex = _ColubrisAAAServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 1),
    _ColubrisAAAServerIndex_Type()
)
colubrisAAAServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    colubrisAAAServerIndex.setStatus("current")


class _ColubrisAAAAuthenProtocol_Type(Integer32):
    """Custom type colubrisAAAAuthenProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("radius", 1)
    )


_ColubrisAAAAuthenProtocol_Type.__name__ = "Integer32"
_ColubrisAAAAuthenProtocol_Object = MibTableColumn
colubrisAAAAuthenProtocol = _ColubrisAAAAuthenProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 2),
    _ColubrisAAAAuthenProtocol_Type()
)
colubrisAAAAuthenProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisAAAAuthenProtocol.setStatus("current")


class _ColubrisAAAAuthenMethod_Type(Integer32):
    """Custom type colubrisAAAAuthenMethod based on Integer32"""
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


_ColubrisAAAAuthenMethod_Type.__name__ = "Integer32"
_ColubrisAAAAuthenMethod_Object = MibTableColumn
colubrisAAAAuthenMethod = _ColubrisAAAAuthenMethod_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 3),
    _ColubrisAAAAuthenMethod_Type()
)
colubrisAAAAuthenMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisAAAAuthenMethod.setStatus("current")


class _ColubrisAAAServerName_Type(OctetString):
    """Custom type colubrisAAAServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ColubrisAAAServerName_Type.__name__ = "OctetString"
_ColubrisAAAServerName_Object = MibTableColumn
colubrisAAAServerName = _ColubrisAAAServerName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 4),
    _ColubrisAAAServerName_Type()
)
colubrisAAAServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colubrisAAAServerName.setStatus("current")
_ColubrisAAASharedSecret_Type = DisplayString
_ColubrisAAASharedSecret_Object = MibTableColumn
colubrisAAASharedSecret = _ColubrisAAASharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 5),
    _ColubrisAAASharedSecret_Type()
)
colubrisAAASharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colubrisAAASharedSecret.setStatus("current")


class _ColubrisAAAAuthenticationPort_Type(Integer32):
    """Custom type colubrisAAAAuthenticationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ColubrisAAAAuthenticationPort_Type.__name__ = "Integer32"
_ColubrisAAAAuthenticationPort_Object = MibTableColumn
colubrisAAAAuthenticationPort = _ColubrisAAAAuthenticationPort_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 6),
    _ColubrisAAAAuthenticationPort_Type()
)
colubrisAAAAuthenticationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisAAAAuthenticationPort.setStatus("current")


class _ColubrisAAAAccountingPort_Type(Integer32):
    """Custom type colubrisAAAAccountingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ColubrisAAAAccountingPort_Type.__name__ = "Integer32"
_ColubrisAAAAccountingPort_Object = MibTableColumn
colubrisAAAAccountingPort = _ColubrisAAAAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 7),
    _ColubrisAAAAccountingPort_Type()
)
colubrisAAAAccountingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisAAAAccountingPort.setStatus("current")


class _ColubrisAAATimeout_Type(Integer32):
    """Custom type colubrisAAATimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_ColubrisAAATimeout_Type.__name__ = "Integer32"
_ColubrisAAATimeout_Object = MibTableColumn
colubrisAAATimeout = _ColubrisAAATimeout_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 8),
    _ColubrisAAATimeout_Type()
)
colubrisAAATimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisAAATimeout.setStatus("current")
if mibBuilder.loadTexts:
    colubrisAAATimeout.setUnits("seconds")


class _ColubrisAAANASId_Type(OctetString):
    """Custom type colubrisAAANASId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_ColubrisAAANASId_Type.__name__ = "OctetString"
_ColubrisAAANASId_Object = MibTableColumn
colubrisAAANASId = _ColubrisAAANASId_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 9),
    _ColubrisAAANASId_Type()
)
colubrisAAANASId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisAAANASId.setStatus("current")
_ColubrisAAAClientMIBConformance_ObjectIdentity = ObjectIdentity
colubrisAAAClientMIBConformance = _ColubrisAAAClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 2)
)
_ColubrisAAAClientMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisAAAClientMIBCompliances = _ColubrisAAAClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 2, 1)
)
_ColubrisAAAClientMIBGroups_ObjectIdentity = ObjectIdentity
colubrisAAAClientMIBGroups = _ColubrisAAAClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 2, 2)
)

# Managed Objects groups

colubrisAAAProfileMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 2, 2, 1)
)
colubrisAAAProfileMIBGroup.setObjects(
      *(("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAProfileName"),
        ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAProfilePrimaryServerIndex"),
        ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAProfileSecondaryServerIndex"))
)
if mibBuilder.loadTexts:
    colubrisAAAProfileMIBGroup.setStatus("current")

colubrisAAAClientMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 2, 2, 2)
)
colubrisAAAClientMIBGroup.setObjects(
      *(("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAAuthenProtocol"),
        ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAAuthenMethod"),
        ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAServerName"),
        ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAASharedSecret"),
        ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAAuthenticationPort"),
        ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAAccountingPort"),
        ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAATimeout"),
        ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAANASId"))
)
if mibBuilder.loadTexts:
    colubrisAAAClientMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

colubrisAAAClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisAAAClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-AAA-CLIENT-MIB",
    **{"colubrisAAAClientMIB": colubrisAAAClientMIB,
       "colubrisAAAClientObjects": colubrisAAAClientObjects,
       "colubrisAAAProfileGroup": colubrisAAAProfileGroup,
       "colubrisAAAProfileTable": colubrisAAAProfileTable,
       "colubrisAAAProfileEntry": colubrisAAAProfileEntry,
       "colubrisAAAProfileIndex": colubrisAAAProfileIndex,
       "colubrisAAAProfileName": colubrisAAAProfileName,
       "colubrisAAAProfilePrimaryServerIndex": colubrisAAAProfilePrimaryServerIndex,
       "colubrisAAAProfileSecondaryServerIndex": colubrisAAAProfileSecondaryServerIndex,
       "colubrisAAAServerGroup": colubrisAAAServerGroup,
       "colubrisAAAServerTable": colubrisAAAServerTable,
       "colubrisAAAServerEntry": colubrisAAAServerEntry,
       "colubrisAAAServerIndex": colubrisAAAServerIndex,
       "colubrisAAAAuthenProtocol": colubrisAAAAuthenProtocol,
       "colubrisAAAAuthenMethod": colubrisAAAAuthenMethod,
       "colubrisAAAServerName": colubrisAAAServerName,
       "colubrisAAASharedSecret": colubrisAAASharedSecret,
       "colubrisAAAAuthenticationPort": colubrisAAAAuthenticationPort,
       "colubrisAAAAccountingPort": colubrisAAAAccountingPort,
       "colubrisAAATimeout": colubrisAAATimeout,
       "colubrisAAANASId": colubrisAAANASId,
       "colubrisAAAClientMIBConformance": colubrisAAAClientMIBConformance,
       "colubrisAAAClientMIBCompliances": colubrisAAAClientMIBCompliances,
       "colubrisAAAClientMIBCompliance": colubrisAAAClientMIBCompliance,
       "colubrisAAAClientMIBGroups": colubrisAAAClientMIBGroups,
       "colubrisAAAProfileMIBGroup": colubrisAAAProfileMIBGroup,
       "colubrisAAAClientMIBGroup": colubrisAAAClientMIBGroup}
)
