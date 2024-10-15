# SNMP MIB module (WWP-PHYSICAL-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-PHYSICAL-MODULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:18 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpPhyModuleMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3)
)
wwpPhyModuleMIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpPhyModuleMIBObjects_ObjectIdentity = ObjectIdentity
wwpPhyModuleMIBObjects = _WwpPhyModuleMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1)
)
_WwpPhyModuleInfo_ObjectIdentity = ObjectIdentity
wwpPhyModuleInfo = _WwpPhyModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 1)
)


class _WwpPhyModSerialNum_Type(DisplayString):
    """Custom type wwpPhyModSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WwpPhyModSerialNum_Type.__name__ = "DisplayString"
_WwpPhyModSerialNum_Object = MibScalar
wwpPhyModSerialNum = _WwpPhyModSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 1, 1),
    _WwpPhyModSerialNum_Type()
)
wwpPhyModSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPhyModSerialNum.setStatus("current")


class _WwpPhyModBoardRevision_Type(DisplayString):
    """Custom type wwpPhyModBoardRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WwpPhyModBoardRevision_Type.__name__ = "DisplayString"
_WwpPhyModBoardRevision_Object = MibScalar
wwpPhyModBoardRevision = _WwpPhyModBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 1, 2),
    _WwpPhyModBoardRevision_Type()
)
wwpPhyModBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPhyModBoardRevision.setStatus("current")


class _WwpPhyModNumResets_Type(Unsigned32):
    """Custom type wwpPhyModNumResets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpPhyModNumResets_Type.__name__ = "Unsigned32"
_WwpPhyModNumResets_Object = MibScalar
wwpPhyModNumResets = _WwpPhyModNumResets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 1, 3),
    _WwpPhyModNumResets_Type()
)
wwpPhyModNumResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPhyModNumResets.setStatus("current")
_WwpPhyModFwVer_Type = DisplayString
_WwpPhyModFwVer_Object = MibScalar
wwpPhyModFwVer = _WwpPhyModFwVer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 1, 4),
    _WwpPhyModFwVer_Type()
)
wwpPhyModFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPhyModFwVer.setStatus("current")


class _WwpPhyModAppVer_Type(DisplayString):
    """Custom type wwpPhyModAppVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WwpPhyModAppVer_Type.__name__ = "DisplayString"
_WwpPhyModAppVer_Object = MibScalar
wwpPhyModAppVer = _WwpPhyModAppVer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 1, 5),
    _WwpPhyModAppVer_Type()
)
wwpPhyModAppVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPhyModAppVer.setStatus("current")
_WwpPhyModPostResults_Type = DisplayString
_WwpPhyModPostResults_Object = MibScalar
wwpPhyModPostResults = _WwpPhyModPostResults_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 1, 6),
    _WwpPhyModPostResults_Type()
)
wwpPhyModPostResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPhyModPostResults.setStatus("current")


class _WwpPhyModPostCode_Type(Unsigned32):
    """Custom type wwpPhyModPostCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpPhyModPostCode_Type.__name__ = "Unsigned32"
_WwpPhyModPostCode_Object = MibScalar
wwpPhyModPostCode = _WwpPhyModPostCode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 1, 7),
    _WwpPhyModPostCode_Type()
)
wwpPhyModPostCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPhyModPostCode.setStatus("current")
_WwpPhyModBootLoaderVer_Type = DisplayString
_WwpPhyModBootLoaderVer_Object = MibScalar
wwpPhyModBootLoaderVer = _WwpPhyModBootLoaderVer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 1, 8),
    _WwpPhyModBootLoaderVer_Type()
)
wwpPhyModBootLoaderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPhyModBootLoaderVer.setStatus("current")
_WwpPhyModMfgDate_Type = DateAndTime
_WwpPhyModMfgDate_Object = MibScalar
wwpPhyModMfgDate = _WwpPhyModMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 1, 9),
    _WwpPhyModMfgDate_Type()
)
wwpPhyModMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPhyModMfgDate.setStatus("current")
_WwpPhyModBoardType_Type = DisplayString
_WwpPhyModBoardType_Object = MibScalar
wwpPhyModBoardType = _WwpPhyModBoardType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 1, 10),
    _WwpPhyModBoardType_Type()
)
wwpPhyModBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPhyModBoardType.setStatus("current")


class _WwpPhyModMktDesc_Type(OctetString):
    """Custom type wwpPhyModMktDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WwpPhyModMktDesc_Type.__name__ = "OctetString"
_WwpPhyModMktDesc_Object = MibScalar
wwpPhyModMktDesc = _WwpPhyModMktDesc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 1, 11),
    _WwpPhyModMktDesc_Type()
)
wwpPhyModMktDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPhyModMktDesc.setStatus("current")
_WwpPhyModuleRebootAttr_ObjectIdentity = ObjectIdentity
wwpPhyModuleRebootAttr = _WwpPhyModuleRebootAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 2)
)


class _WwpPhyModRebootOperation_Type(Integer32):
    """Custom type wwpPhyModRebootOperation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reboot", 1),
          ("rebootDefault", 3),
          ("rebootReinit", 2))
    )


_WwpPhyModRebootOperation_Type.__name__ = "Integer32"
_WwpPhyModRebootOperation_Object = MibScalar
wwpPhyModRebootOperation = _WwpPhyModRebootOperation_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 2, 1),
    _WwpPhyModRebootOperation_Type()
)
wwpPhyModRebootOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPhyModRebootOperation.setStatus("current")
_WwpPhyModLastRebootTime_Type = DateAndTime
_WwpPhyModLastRebootTime_Object = MibScalar
wwpPhyModLastRebootTime = _WwpPhyModLastRebootTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 2, 2),
    _WwpPhyModLastRebootTime_Type()
)
wwpPhyModLastRebootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPhyModLastRebootTime.setStatus("current")


class _WwpPhyModLastRebootReason_Type(Integer32):
    """Custom type wwpPhyModLastRebootReason based on Integer32"""
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
        *(("hostRequest", 1),
          ("pwrFail", 2),
          ("softwareForced", 4),
          ("unknown", 3))
    )


_WwpPhyModLastRebootReason_Type.__name__ = "Integer32"
_WwpPhyModLastRebootReason_Object = MibScalar
wwpPhyModLastRebootReason = _WwpPhyModLastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 1, 2, 3),
    _WwpPhyModLastRebootReason_Type()
)
wwpPhyModLastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPhyModLastRebootReason.setStatus("current")
_WwpPhyModuleMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpPhyModuleMIBNotificationPrefix = _WwpPhyModuleMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 2)
)
_WwpPhyModuleMIBNotifications_ObjectIdentity = ObjectIdentity
wwpPhyModuleMIBNotifications = _WwpPhyModuleMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 2, 0)
)
_WwpPhyModuleMIBConformance_ObjectIdentity = ObjectIdentity
wwpPhyModuleMIBConformance = _WwpPhyModuleMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 3)
)
_WwpPhyModuleMIBCompliances_ObjectIdentity = ObjectIdentity
wwpPhyModuleMIBCompliances = _WwpPhyModuleMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 3, 1)
)
_WwpPhyModuleMIBGroups_ObjectIdentity = ObjectIdentity
wwpPhyModuleMIBGroups = _WwpPhyModuleMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 3, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-PHYSICAL-MODULE-MIB",
    **{"wwpPhyModuleMIB": wwpPhyModuleMIB,
       "wwpPhyModuleMIBObjects": wwpPhyModuleMIBObjects,
       "wwpPhyModuleInfo": wwpPhyModuleInfo,
       "wwpPhyModSerialNum": wwpPhyModSerialNum,
       "wwpPhyModBoardRevision": wwpPhyModBoardRevision,
       "wwpPhyModNumResets": wwpPhyModNumResets,
       "wwpPhyModFwVer": wwpPhyModFwVer,
       "wwpPhyModAppVer": wwpPhyModAppVer,
       "wwpPhyModPostResults": wwpPhyModPostResults,
       "wwpPhyModPostCode": wwpPhyModPostCode,
       "wwpPhyModBootLoaderVer": wwpPhyModBootLoaderVer,
       "wwpPhyModMfgDate": wwpPhyModMfgDate,
       "wwpPhyModBoardType": wwpPhyModBoardType,
       "wwpPhyModMktDesc": wwpPhyModMktDesc,
       "wwpPhyModuleRebootAttr": wwpPhyModuleRebootAttr,
       "wwpPhyModRebootOperation": wwpPhyModRebootOperation,
       "wwpPhyModLastRebootTime": wwpPhyModLastRebootTime,
       "wwpPhyModLastRebootReason": wwpPhyModLastRebootReason,
       "wwpPhyModuleMIBNotificationPrefix": wwpPhyModuleMIBNotificationPrefix,
       "wwpPhyModuleMIBNotifications": wwpPhyModuleMIBNotifications,
       "wwpPhyModuleMIBConformance": wwpPhyModuleMIBConformance,
       "wwpPhyModuleMIBCompliances": wwpPhyModuleMIBCompliances,
       "wwpPhyModuleMIBGroups": wwpPhyModuleMIBGroups}
)
