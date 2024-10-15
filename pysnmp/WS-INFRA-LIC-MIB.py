# SNMP MIB module (WS-INFRA-LIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WS-INFRA-LIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:27 2024
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

(wsInfraLic,) = mibBuilder.importSymbols(
    "WS-INFRA-SMI-MIB",
    "wsInfraLic")


# MODULE-IDENTITY

wsInfraLicMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1)
)
wsInfraLicMib.setRevisions(
        ("2007-02-07 11:27",
         "2006-05-24 15:19",
         "2006-05-01 14:36",
         "2006-04-28 14:16",
         "2005-06-27 17:08",
         "2005-06-22 15:10",
         "2005-06-22 11:27")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsInfraAPLicNum_Type = Unsigned32
_WsInfraAPLicNum_Object = MibScalar
wsInfraAPLicNum = _WsInfraAPLicNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 1),
    _WsInfraAPLicNum_Type()
)
wsInfraAPLicNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraAPLicNum.setStatus("current")
_WsInfraLicMgmt_ObjectIdentity = ObjectIdentity
wsInfraLicMgmt = _WsInfraLicMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 2)
)
_WsInfraLicNum_Type = Unsigned32
_WsInfraLicNum_Object = MibScalar
wsInfraLicNum = _WsInfraLicNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 2, 1),
    _WsInfraLicNum_Type()
)
wsInfraLicNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraLicNum.setStatus("current")


class _WsInfraLicActionFeature_Type(OctetString):
    """Custom type wsInfraLicActionFeature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WsInfraLicActionFeature_Type.__name__ = "OctetString"
_WsInfraLicActionFeature_Object = MibScalar
wsInfraLicActionFeature = _WsInfraLicActionFeature_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 2, 2),
    _WsInfraLicActionFeature_Type()
)
wsInfraLicActionFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraLicActionFeature.setStatus("current")


class _WsInfraLicActionKey_Type(OctetString):
    """Custom type wsInfraLicActionKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_WsInfraLicActionKey_Type.__name__ = "OctetString"
_WsInfraLicActionKey_Object = MibScalar
wsInfraLicActionKey = _WsInfraLicActionKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 2, 3),
    _WsInfraLicActionKey_Type()
)
wsInfraLicActionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraLicActionKey.setStatus("current")


class _WsInfraLicAction_Type(Integer32):
    """Custom type wsInfraLicAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsInfraLicAction_Type.__name__ = "Integer32"
_WsInfraLicAction_Object = MibScalar
wsInfraLicAction = _WsInfraLicAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 2, 4),
    _WsInfraLicAction_Type()
)
wsInfraLicAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraLicAction.setStatus("current")
_WsInfraLicTable_Object = MibTable
wsInfraLicTable = _WsInfraLicTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 2, 5)
)
if mibBuilder.loadTexts:
    wsInfraLicTable.setStatus("current")
_WsInfraLicEntry_Object = MibTableRow
wsInfraLicEntry = _WsInfraLicEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 2, 5, 1)
)
wsInfraLicEntry.setIndexNames(
    (0, "WS-INFRA-LIC-MIB", "wsInfraLicIndex"),
)
if mibBuilder.loadTexts:
    wsInfraLicEntry.setStatus("current")


class _WsInfraLicIndex_Type(OctetString):
    """Custom type wsInfraLicIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WsInfraLicIndex_Type.__name__ = "OctetString"
_WsInfraLicIndex_Object = MibTableColumn
wsInfraLicIndex = _WsInfraLicIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 2, 5, 1, 1),
    _WsInfraLicIndex_Type()
)
wsInfraLicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsInfraLicIndex.setStatus("current")


class _WsInfraLicFeature_Type(OctetString):
    """Custom type wsInfraLicFeature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WsInfraLicFeature_Type.__name__ = "OctetString"
_WsInfraLicFeature_Object = MibTableColumn
wsInfraLicFeature = _WsInfraLicFeature_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 2, 5, 1, 2),
    _WsInfraLicFeature_Type()
)
wsInfraLicFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraLicFeature.setStatus("current")


class _WsInfraLicKey_Type(OctetString):
    """Custom type wsInfraLicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_WsInfraLicKey_Type.__name__ = "OctetString"
_WsInfraLicKey_Object = MibTableColumn
wsInfraLicKey = _WsInfraLicKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 2, 5, 1, 3),
    _WsInfraLicKey_Type()
)
wsInfraLicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraLicKey.setStatus("current")


class _WsInfraLicCount_Type(Integer32):
    """Custom type wsInfraLicCount based on Integer32"""
    defaultValue = 0


_WsInfraLicCount_Object = MibTableColumn
wsInfraLicCount = _WsInfraLicCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 2, 5, 1, 4),
    _WsInfraLicCount_Type()
)
wsInfraLicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraLicCount.setStatus("current")


class _WsInfraLicUsage_Type(Integer32):
    """Custom type wsInfraLicUsage based on Integer32"""
    defaultValue = 0


_WsInfraLicUsage_Object = MibTableColumn
wsInfraLicUsage = _WsInfraLicUsage_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 2, 5, 1, 5),
    _WsInfraLicUsage_Type()
)
wsInfraLicUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraLicUsage.setStatus("current")
_WsInfraLicSerialNumber_Type = DisplayString
_WsInfraLicSerialNumber_Object = MibScalar
wsInfraLicSerialNumber = _WsInfraLicSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 2, 6),
    _WsInfraLicSerialNumber_Type()
)
wsInfraLicSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraLicSerialNumber.setStatus("current")
_WsInfraLicMIBConformance_ObjectIdentity = ObjectIdentity
wsInfraLicMIBConformance = _WsInfraLicMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 100)
)
_WsInfraLicMIBCompliances_ObjectIdentity = ObjectIdentity
wsInfraLicMIBCompliances = _WsInfraLicMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 100, 1)
)
_WsInfraLicMIBGroups_ObjectIdentity = ObjectIdentity
wsInfraLicMIBGroups = _WsInfraLicMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 100, 2)
)

# Managed Objects groups

wsInfraLicMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 100, 2, 1)
)
wsInfraLicMIBGroup.setObjects(
    ("WS-INFRA-LIC-MIB", "wsInfraAPLicNum")
)
if mibBuilder.loadTexts:
    wsInfraLicMIBGroup.setStatus("current")

wsInfraLicMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 100, 2, 2)
)
wsInfraLicMgmtGroup.setObjects(
      *(("WS-INFRA-LIC-MIB", "wsInfraLicNum"),
        ("WS-INFRA-LIC-MIB", "wsInfraLicFeature"),
        ("WS-INFRA-LIC-MIB", "wsInfraLicActionKey"),
        ("WS-INFRA-LIC-MIB", "wsInfraLicAction"),
        ("WS-INFRA-LIC-MIB", "wsInfraLicUsage"),
        ("WS-INFRA-LIC-MIB", "wsInfraLicKey"),
        ("WS-INFRA-LIC-MIB", "wsInfraLicSerialNumber"),
        ("WS-INFRA-LIC-MIB", "wsInfraAPLicNum"),
        ("WS-INFRA-LIC-MIB", "wsInfraLicCount"),
        ("WS-INFRA-LIC-MIB", "wsInfraLicActionFeature"))
)
if mibBuilder.loadTexts:
    wsInfraLicMgmtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wsInfraLicMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9, 1, 100, 1, 1)
)
if mibBuilder.loadTexts:
    wsInfraLicMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-INFRA-LIC-MIB",
    **{"wsInfraLicMib": wsInfraLicMib,
       "wsInfraAPLicNum": wsInfraAPLicNum,
       "wsInfraLicMgmt": wsInfraLicMgmt,
       "wsInfraLicNum": wsInfraLicNum,
       "wsInfraLicActionFeature": wsInfraLicActionFeature,
       "wsInfraLicActionKey": wsInfraLicActionKey,
       "wsInfraLicAction": wsInfraLicAction,
       "wsInfraLicTable": wsInfraLicTable,
       "wsInfraLicEntry": wsInfraLicEntry,
       "wsInfraLicIndex": wsInfraLicIndex,
       "wsInfraLicFeature": wsInfraLicFeature,
       "wsInfraLicKey": wsInfraLicKey,
       "wsInfraLicCount": wsInfraLicCount,
       "wsInfraLicUsage": wsInfraLicUsage,
       "wsInfraLicSerialNumber": wsInfraLicSerialNumber,
       "wsInfraLicMIBConformance": wsInfraLicMIBConformance,
       "wsInfraLicMIBCompliances": wsInfraLicMIBCompliances,
       "wsInfraLicMIBCompliance": wsInfraLicMIBCompliance,
       "wsInfraLicMIBGroups": wsInfraLicMIBGroups,
       "wsInfraLicMIBGroup": wsInfraLicMIBGroup,
       "wsInfraLicMgmtGroup": wsInfraLicMgmtGroup}
)
