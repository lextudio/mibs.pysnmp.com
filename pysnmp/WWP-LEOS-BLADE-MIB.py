# SNMP MIB module (WWP-LEOS-BLADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-BLADE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:45 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosBladeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1)
)
wwpLeosBladeMIB.setRevisions(
        ("2011-10-19 00:00",
         "2002-03-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosBladeMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosBladeMIBObjects = _WwpLeosBladeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1)
)
_WwpLeosBlade_ObjectIdentity = ObjectIdentity
wwpLeosBlade = _WwpLeosBlade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1)
)
_WwpLeosBladeTable_Object = MibTable
wwpLeosBladeTable = _WwpLeosBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosBladeTable.setStatus("current")
_WwpLeosBladeEntry_Object = MibTableRow
wwpLeosBladeEntry = _WwpLeosBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1)
)
wwpLeosBladeEntry.setIndexNames(
    (0, "WWP-LEOS-BLADE-MIB", "wwpLeosBladeId"),
)
if mibBuilder.loadTexts:
    wwpLeosBladeEntry.setStatus("current")


class _WwpLeosBladeId_Type(Integer32):
    """Custom type wwpLeosBladeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosBladeId_Type.__name__ = "Integer32"
_WwpLeosBladeId_Object = MibTableColumn
wwpLeosBladeId = _WwpLeosBladeId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 1),
    _WwpLeosBladeId_Type()
)
wwpLeosBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBladeId.setStatus("current")


class _WwpLeosBladeType_Type(Integer32):
    """Custom type wwpLeosBladeType based on Integer32"""
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
        *(("control", 1),
          ("fabric", 3),
          ("io", 2),
          ("single", 4))
    )


_WwpLeosBladeType_Type.__name__ = "Integer32"
_WwpLeosBladeType_Object = MibTableColumn
wwpLeosBladeType = _WwpLeosBladeType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 2),
    _WwpLeosBladeType_Type()
)
wwpLeosBladeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBladeType.setStatus("current")
_WwpLeosBladeCapFilename_Type = DisplayString
_WwpLeosBladeCapFilename_Object = MibTableColumn
wwpLeosBladeCapFilename = _WwpLeosBladeCapFilename_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 3),
    _WwpLeosBladeCapFilename_Type()
)
wwpLeosBladeCapFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBladeCapFilename.setStatus("current")


class _WwpLeosBladeAdminState_Type(Integer32):
    """Custom type wwpLeosBladeAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpLeosBladeAdminState_Type.__name__ = "Integer32"
_WwpLeosBladeAdminState_Object = MibTableColumn
wwpLeosBladeAdminState = _WwpLeosBladeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 4),
    _WwpLeosBladeAdminState_Type()
)
wwpLeosBladeAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBladeAdminState.setStatus("current")


class _WwpLeosBladeOperState_Type(Integer32):
    """Custom type wwpLeosBladeOperState based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 2),
          ("faulted", 4),
          ("init", 1),
          ("unequipped", 5))
    )


_WwpLeosBladeOperState_Type.__name__ = "Integer32"
_WwpLeosBladeOperState_Object = MibTableColumn
wwpLeosBladeOperState = _WwpLeosBladeOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 5),
    _WwpLeosBladeOperState_Type()
)
wwpLeosBladeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBladeOperState.setStatus("current")
_WwpLeosBladeStartMacAddr_Type = MacAddress
_WwpLeosBladeStartMacAddr_Object = MibTableColumn
wwpLeosBladeStartMacAddr = _WwpLeosBladeStartMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 6),
    _WwpLeosBladeStartMacAddr_Type()
)
wwpLeosBladeStartMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBladeStartMacAddr.setStatus("current")


class _WwpLeosBladeNumPorts_Type(Integer32):
    """Custom type wwpLeosBladeNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosBladeNumPorts_Type.__name__ = "Integer32"
_WwpLeosBladeNumPorts_Object = MibTableColumn
wwpLeosBladeNumPorts = _WwpLeosBladeNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 7),
    _WwpLeosBladeNumPorts_Type()
)
wwpLeosBladeNumPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosBladeNumPorts.setStatus("current")
_WwpLeosBladeStatus_Type = RowStatus
_WwpLeosBladeStatus_Object = MibTableColumn
wwpLeosBladeStatus = _WwpLeosBladeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 1, 1, 8),
    _WwpLeosBladeStatus_Type()
)
wwpLeosBladeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosBladeStatus.setStatus("current")
_WwpLeosPhyBladeTable_Object = MibTable
wwpLeosPhyBladeTable = _WwpLeosPhyBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosPhyBladeTable.setStatus("current")
_WwpLeosPhyBladeEntry_Object = MibTableRow
wwpLeosPhyBladeEntry = _WwpLeosPhyBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1)
)
wwpLeosPhyBladeEntry.setIndexNames(
    (0, "WWP-LEOS-BLADE-MIB", "wwpLeosBladeId"),
)
if mibBuilder.loadTexts:
    wwpLeosPhyBladeEntry.setStatus("current")
_WwpLeosPhyBladeSysUpTime_Type = TimeTicks
_WwpLeosPhyBladeSysUpTime_Object = MibTableColumn
wwpLeosPhyBladeSysUpTime = _WwpLeosPhyBladeSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 1),
    _WwpLeosPhyBladeSysUpTime_Type()
)
wwpLeosPhyBladeSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPhyBladeSysUpTime.setStatus("current")


class _WwpLeosPhyBladeSerialNum_Type(DisplayString):
    """Custom type wwpLeosPhyBladeSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WwpLeosPhyBladeSerialNum_Type.__name__ = "DisplayString"
_WwpLeosPhyBladeSerialNum_Object = MibTableColumn
wwpLeosPhyBladeSerialNum = _WwpLeosPhyBladeSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 2),
    _WwpLeosPhyBladeSerialNum_Type()
)
wwpLeosPhyBladeSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPhyBladeSerialNum.setStatus("current")


class _WwpLeosPhyBladeBoardRevision_Type(DisplayString):
    """Custom type wwpLeosPhyBladeBoardRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WwpLeosPhyBladeBoardRevision_Type.__name__ = "DisplayString"
_WwpLeosPhyBladeBoardRevision_Object = MibTableColumn
wwpLeosPhyBladeBoardRevision = _WwpLeosPhyBladeBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 3),
    _WwpLeosPhyBladeBoardRevision_Type()
)
wwpLeosPhyBladeBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPhyBladeBoardRevision.setStatus("current")
_WwpLeosPhyBladePostResults_Type = DisplayString
_WwpLeosPhyBladePostResults_Object = MibTableColumn
wwpLeosPhyBladePostResults = _WwpLeosPhyBladePostResults_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 4),
    _WwpLeosPhyBladePostResults_Type()
)
wwpLeosPhyBladePostResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPhyBladePostResults.setStatus("current")
_WwpLeosPhyBladePostCode_Type = Unsigned32
_WwpLeosPhyBladePostCode_Object = MibTableColumn
wwpLeosPhyBladePostCode = _WwpLeosPhyBladePostCode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 5),
    _WwpLeosPhyBladePostCode_Type()
)
wwpLeosPhyBladePostCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPhyBladePostCode.setStatus("current")
_WwpLeosPhyBladeMfgDate_Type = DateAndTime
_WwpLeosPhyBladeMfgDate_Object = MibTableColumn
wwpLeosPhyBladeMfgDate = _WwpLeosPhyBladeMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 6),
    _WwpLeosPhyBladeMfgDate_Type()
)
wwpLeosPhyBladeMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPhyBladeMfgDate.setStatus("current")
_WwpLeosPhyBladeBoardDesc_Type = DisplayString
_WwpLeosPhyBladeBoardDesc_Object = MibTableColumn
wwpLeosPhyBladeBoardDesc = _WwpLeosPhyBladeBoardDesc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 7),
    _WwpLeosPhyBladeBoardDesc_Type()
)
wwpLeosPhyBladeBoardDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPhyBladeBoardDesc.setStatus("current")
_WwpLeosPhyBladeNumResets_Type = Unsigned32
_WwpLeosPhyBladeNumResets_Object = MibTableColumn
wwpLeosPhyBladeNumResets = _WwpLeosPhyBladeNumResets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 8),
    _WwpLeosPhyBladeNumResets_Type()
)
wwpLeosPhyBladeNumResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPhyBladeNumResets.setStatus("current")


class _WwpLeosPhyBladeLastRebootReason_Type(Integer32):
    """Custom type wwpLeosPhyBladeLastRebootReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("appLoad", 4),
          ("cli", 8),
          ("errorHandler", 5),
          ("guardianReboot", 11),
          ("guardianSaosRestart", 12),
          ("pwrFail", 3),
          ("resetButton", 9),
          ("serviceModeChange", 10),
          ("snmp", 2),
          ("unknown", 1),
          ("upgrade", 7),
          ("watchdog", 6))
    )


_WwpLeosPhyBladeLastRebootReason_Type.__name__ = "Integer32"
_WwpLeosPhyBladeLastRebootReason_Object = MibTableColumn
wwpLeosPhyBladeLastRebootReason = _WwpLeosPhyBladeLastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 9),
    _WwpLeosPhyBladeLastRebootReason_Type()
)
wwpLeosPhyBladeLastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPhyBladeLastRebootReason.setStatus("current")


class _WwpLeosPhyBladeRebootOperation_Type(Integer32):
    """Custom type wwpLeosPhyBladeRebootOperation based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("reboot", 2),
          ("rebootCustReinit", 4),
          ("rebootReinit", 3))
    )


_WwpLeosPhyBladeRebootOperation_Type.__name__ = "Integer32"
_WwpLeosPhyBladeRebootOperation_Object = MibTableColumn
wwpLeosPhyBladeRebootOperation = _WwpLeosPhyBladeRebootOperation_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 1, 1, 2, 1, 10),
    _WwpLeosPhyBladeRebootOperation_Type()
)
wwpLeosPhyBladeRebootOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPhyBladeRebootOperation.setStatus("current")
_WwpLeosBladeMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosBladeMIBNotificationPrefix = _WwpLeosBladeMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 2)
)
_WwpLeosBladeMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosBladeMIBNotifications = _WwpLeosBladeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 2, 0)
)
_WwpLeosBladeMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosBladeMIBConformance = _WwpLeosBladeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 3)
)
_WwpLeosBladeMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosBladeMIBCompliances = _WwpLeosBladeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 3, 1)
)
_WwpLeosBladeMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosBladeMIBGroups = _WwpLeosBladeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosBladeStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 2, 0, 1)
)
wwpLeosBladeStateChange.setObjects(
      *(("WWP-LEOS-BLADE-MIB", "wwpLeosBladeId"),
        ("WWP-LEOS-BLADE-MIB", "wwpLeosBladeOperState"))
)
if mibBuilder.loadTexts:
    wwpLeosBladeStateChange.setStatus(
        "current"
    )

wwpLeosBladePostFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 1, 2, 0, 2)
)
wwpLeosBladePostFail.setObjects(
      *(("WWP-LEOS-BLADE-MIB", "wwpLeosBladeId"),
        ("WWP-LEOS-BLADE-MIB", "wwpLeosPhyBladePostCode"))
)
if mibBuilder.loadTexts:
    wwpLeosBladePostFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-BLADE-MIB",
    **{"wwpLeosBladeMIB": wwpLeosBladeMIB,
       "wwpLeosBladeMIBObjects": wwpLeosBladeMIBObjects,
       "wwpLeosBlade": wwpLeosBlade,
       "wwpLeosBladeTable": wwpLeosBladeTable,
       "wwpLeosBladeEntry": wwpLeosBladeEntry,
       "wwpLeosBladeId": wwpLeosBladeId,
       "wwpLeosBladeType": wwpLeosBladeType,
       "wwpLeosBladeCapFilename": wwpLeosBladeCapFilename,
       "wwpLeosBladeAdminState": wwpLeosBladeAdminState,
       "wwpLeosBladeOperState": wwpLeosBladeOperState,
       "wwpLeosBladeStartMacAddr": wwpLeosBladeStartMacAddr,
       "wwpLeosBladeNumPorts": wwpLeosBladeNumPorts,
       "wwpLeosBladeStatus": wwpLeosBladeStatus,
       "wwpLeosPhyBladeTable": wwpLeosPhyBladeTable,
       "wwpLeosPhyBladeEntry": wwpLeosPhyBladeEntry,
       "wwpLeosPhyBladeSysUpTime": wwpLeosPhyBladeSysUpTime,
       "wwpLeosPhyBladeSerialNum": wwpLeosPhyBladeSerialNum,
       "wwpLeosPhyBladeBoardRevision": wwpLeosPhyBladeBoardRevision,
       "wwpLeosPhyBladePostResults": wwpLeosPhyBladePostResults,
       "wwpLeosPhyBladePostCode": wwpLeosPhyBladePostCode,
       "wwpLeosPhyBladeMfgDate": wwpLeosPhyBladeMfgDate,
       "wwpLeosPhyBladeBoardDesc": wwpLeosPhyBladeBoardDesc,
       "wwpLeosPhyBladeNumResets": wwpLeosPhyBladeNumResets,
       "wwpLeosPhyBladeLastRebootReason": wwpLeosPhyBladeLastRebootReason,
       "wwpLeosPhyBladeRebootOperation": wwpLeosPhyBladeRebootOperation,
       "wwpLeosBladeMIBNotificationPrefix": wwpLeosBladeMIBNotificationPrefix,
       "wwpLeosBladeMIBNotifications": wwpLeosBladeMIBNotifications,
       "wwpLeosBladeStateChange": wwpLeosBladeStateChange,
       "wwpLeosBladePostFail": wwpLeosBladePostFail,
       "wwpLeosBladeMIBConformance": wwpLeosBladeMIBConformance,
       "wwpLeosBladeMIBCompliances": wwpLeosBladeMIBCompliances,
       "wwpLeosBladeMIBGroups": wwpLeosBladeMIBGroups}
)
