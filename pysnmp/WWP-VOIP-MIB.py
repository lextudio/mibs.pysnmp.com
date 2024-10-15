# SNMP MIB module (WWP-VOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-VOIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:27 2024
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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpVoipMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15)
)
wwpVoipMIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpVoipMIBObjects_ObjectIdentity = ObjectIdentity
wwpVoipMIBObjects = _WwpVoipMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 1)
)
_WwpVoip_ObjectIdentity = ObjectIdentity
wwpVoip = _WwpVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1)
)
_WwpVoipTable_Object = MibTable
wwpVoipTable = _WwpVoipTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpVoipTable.setStatus("current")
_WwpVoipEntry_Object = MibTableRow
wwpVoipEntry = _WwpVoipEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1)
)
wwpVoipEntry.setIndexNames(
    (0, "WWP-VOIP-MIB", "wwpVoipIndex"),
)
if mibBuilder.loadTexts:
    wwpVoipEntry.setStatus("current")


class _WwpVoipIndex_Type(Integer32):
    """Custom type wwpVoipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpVoipIndex_Type.__name__ = "Integer32"
_WwpVoipIndex_Object = MibTableColumn
wwpVoipIndex = _WwpVoipIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 1),
    _WwpVoipIndex_Type()
)
wwpVoipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoipIndex.setStatus("current")
_WwpVoipDownLoaderVersion_Type = DisplayString
_WwpVoipDownLoaderVersion_Object = MibTableColumn
wwpVoipDownLoaderVersion = _WwpVoipDownLoaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 2),
    _WwpVoipDownLoaderVersion_Type()
)
wwpVoipDownLoaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoipDownLoaderVersion.setStatus("current")
_WwpVoipApplicationVersion_Type = DisplayString
_WwpVoipApplicationVersion_Object = MibTableColumn
wwpVoipApplicationVersion = _WwpVoipApplicationVersion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 3),
    _WwpVoipApplicationVersion_Type()
)
wwpVoipApplicationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoipApplicationVersion.setStatus("current")


class _WwpVoipPortNum_Type(Integer32):
    """Custom type wwpVoipPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpVoipPortNum_Type.__name__ = "Integer32"
_WwpVoipPortNum_Object = MibTableColumn
wwpVoipPortNum = _WwpVoipPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 4),
    _WwpVoipPortNum_Type()
)
wwpVoipPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoipPortNum.setStatus("current")
_WwpVoipIpAddr_Type = IpAddress
_WwpVoipIpAddr_Object = MibTableColumn
wwpVoipIpAddr = _WwpVoipIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 5),
    _WwpVoipIpAddr_Type()
)
wwpVoipIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoipIpAddr.setStatus("current")


class _WwpVoipNumResets_Type(Integer32):
    """Custom type wwpVoipNumResets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpVoipNumResets_Type.__name__ = "Integer32"
_WwpVoipNumResets_Object = MibTableColumn
wwpVoipNumResets = _WwpVoipNumResets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 6),
    _WwpVoipNumResets_Type()
)
wwpVoipNumResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoipNumResets.setStatus("current")
_WwpVoipCallAgentAddr_Type = IpAddress
_WwpVoipCallAgentAddr_Object = MibTableColumn
wwpVoipCallAgentAddr = _WwpVoipCallAgentAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 7),
    _WwpVoipCallAgentAddr_Type()
)
wwpVoipCallAgentAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoipCallAgentAddr.setStatus("current")


class _WwpVoipResetOp_Type(Integer32):
    """Custom type wwpVoipResetOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_WwpVoipResetOp_Type.__name__ = "Integer32"
_WwpVoipResetOp_Object = MibTableColumn
wwpVoipResetOp = _WwpVoipResetOp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 8),
    _WwpVoipResetOp_Type()
)
wwpVoipResetOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoipResetOp.setStatus("current")
_WwpVoipMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpVoipMIBNotificationPrefix = _WwpVoipMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 2)
)
_WwpVoipMIBNotifications_ObjectIdentity = ObjectIdentity
wwpVoipMIBNotifications = _WwpVoipMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 2, 0)
)
_WwpVoipMIBConformance_ObjectIdentity = ObjectIdentity
wwpVoipMIBConformance = _WwpVoipMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 3)
)
_WwpVoipMIBCompliances_ObjectIdentity = ObjectIdentity
wwpVoipMIBCompliances = _WwpVoipMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 3, 1)
)
_WwpVoipMIBGroups_ObjectIdentity = ObjectIdentity
wwpVoipMIBGroups = _WwpVoipMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpVoipDiagFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 15, 2, 0, 1)
)
if mibBuilder.loadTexts:
    wwpVoipDiagFailNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-VOIP-MIB",
    **{"wwpVoipMIB": wwpVoipMIB,
       "wwpVoipMIBObjects": wwpVoipMIBObjects,
       "wwpVoip": wwpVoip,
       "wwpVoipTable": wwpVoipTable,
       "wwpVoipEntry": wwpVoipEntry,
       "wwpVoipIndex": wwpVoipIndex,
       "wwpVoipDownLoaderVersion": wwpVoipDownLoaderVersion,
       "wwpVoipApplicationVersion": wwpVoipApplicationVersion,
       "wwpVoipPortNum": wwpVoipPortNum,
       "wwpVoipIpAddr": wwpVoipIpAddr,
       "wwpVoipNumResets": wwpVoipNumResets,
       "wwpVoipCallAgentAddr": wwpVoipCallAgentAddr,
       "wwpVoipResetOp": wwpVoipResetOp,
       "wwpVoipMIBNotificationPrefix": wwpVoipMIBNotificationPrefix,
       "wwpVoipMIBNotifications": wwpVoipMIBNotifications,
       "wwpVoipDiagFailNotification": wwpVoipDiagFailNotification,
       "wwpVoipMIBConformance": wwpVoipMIBConformance,
       "wwpVoipMIBCompliances": wwpVoipMIBCompliances,
       "wwpVoipMIBGroups": wwpVoipMIBGroups}
)
