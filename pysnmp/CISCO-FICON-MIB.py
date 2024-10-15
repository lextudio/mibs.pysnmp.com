# SNMP MIB module (CISCO-FICON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FICON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:31 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(FcAddressId,) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcAddressId")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoFiconMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 375)
)
ciscoFiconMIB.setRevisions(
        ("2006-04-07 00:00",
         "2006-03-14 00:00",
         "2005-10-21 00:00",
         "2005-10-06 00:00",
         "2005-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CficonPortNumOrAddr(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFiconMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoFiconMIBNotifications = _CiscoFiconMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 0)
)
_CiscoFiconMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFiconMIBObjects = _CiscoFiconMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1)
)
_CiscoFiconConfig_ObjectIdentity = ObjectIdentity
ciscoFiconConfig = _CiscoFiconConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1)
)
_CficonPortSwapTable_Object = MibTable
cficonPortSwapTable = _CficonPortSwapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cficonPortSwapTable.setStatus("current")
_CficonPortSwapEntry_Object = MibTableRow
cficonPortSwapEntry = _CficonPortSwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 1, 1)
)
cficonPortSwapEntry.setIndexNames(
    (0, "CISCO-FICON-MIB", "cficonPortSwapIndex"),
)
if mibBuilder.loadTexts:
    cficonPortSwapEntry.setStatus("current")


class _CficonPortSwapIndex_Type(Integer32):
    """Custom type cficonPortSwapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CficonPortSwapIndex_Type.__name__ = "Integer32"
_CficonPortSwapIndex_Object = MibTableColumn
cficonPortSwapIndex = _CficonPortSwapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 1, 1, 1),
    _CficonPortSwapIndex_Type()
)
cficonPortSwapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cficonPortSwapIndex.setStatus("current")
_CficonSwapPortNumberFirst_Type = CficonPortNumOrAddr
_CficonSwapPortNumberFirst_Object = MibTableColumn
cficonSwapPortNumberFirst = _CficonSwapPortNumberFirst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 1, 1, 2),
    _CficonSwapPortNumberFirst_Type()
)
cficonSwapPortNumberFirst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonSwapPortNumberFirst.setStatus("current")
_CficonSwapPortNumberSecond_Type = CficonPortNumOrAddr
_CficonSwapPortNumberSecond_Object = MibTableColumn
cficonSwapPortNumberSecond = _CficonSwapPortNumberSecond_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 1, 1, 3),
    _CficonSwapPortNumberSecond_Type()
)
cficonSwapPortNumberSecond.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonSwapPortNumberSecond.setStatus("current")
_CficonSwapPortEntryStatus_Type = RowStatus
_CficonSwapPortEntryStatus_Object = MibTableColumn
cficonSwapPortEntryStatus = _CficonSwapPortEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 1, 1, 4),
    _CficonSwapPortEntryStatus_Type()
)
cficonSwapPortEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonSwapPortEntryStatus.setStatus("current")
_CficonVsanTable_Object = MibTable
cficonVsanTable = _CficonVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cficonVsanTable.setStatus("current")
_CficonVsanEntry_Object = MibTableRow
cficonVsanEntry = _CficonVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1)
)
cficonVsanEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    cficonVsanEntry.setStatus("current")


class _CficonVsanHostControl_Type(TruthValue):
    """Custom type cficonVsanHostControl based on TruthValue"""


_CficonVsanHostControl_Object = MibTableColumn
cficonVsanHostControl = _CficonVsanHostControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 1),
    _CficonVsanHostControl_Type()
)
cficonVsanHostControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonVsanHostControl.setStatus("current")


class _CficonVsanHostControlSwOffline_Type(TruthValue):
    """Custom type cficonVsanHostControlSwOffline based on TruthValue"""


_CficonVsanHostControlSwOffline_Object = MibTableColumn
cficonVsanHostControlSwOffline = _CficonVsanHostControlSwOffline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 2),
    _CficonVsanHostControlSwOffline_Type()
)
cficonVsanHostControlSwOffline.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonVsanHostControlSwOffline.setStatus("current")


class _CficonVsanHostControlClkAlrtMode_Type(TruthValue):
    """Custom type cficonVsanHostControlClkAlrtMode based on TruthValue"""


_CficonVsanHostControlClkAlrtMode_Object = MibTableColumn
cficonVsanHostControlClkAlrtMode = _CficonVsanHostControlClkAlrtMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 3),
    _CficonVsanHostControlClkAlrtMode_Type()
)
cficonVsanHostControlClkAlrtMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonVsanHostControlClkAlrtMode.setStatus("current")


class _CficonVsanSnmpControl_Type(TruthValue):
    """Custom type cficonVsanSnmpControl based on TruthValue"""


_CficonVsanSnmpControl_Object = MibTableColumn
cficonVsanSnmpControl = _CficonVsanSnmpControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 4),
    _CficonVsanSnmpControl_Type()
)
cficonVsanSnmpControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonVsanSnmpControl.setStatus("current")


class _CficonVsanAutoSavePortAddrCfg_Type(TruthValue):
    """Custom type cficonVsanAutoSavePortAddrCfg based on TruthValue"""


_CficonVsanAutoSavePortAddrCfg_Object = MibTableColumn
cficonVsanAutoSavePortAddrCfg = _CficonVsanAutoSavePortAddrCfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 5),
    _CficonVsanAutoSavePortAddrCfg_Type()
)
cficonVsanAutoSavePortAddrCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonVsanAutoSavePortAddrCfg.setStatus("current")


class _CficonVsanEnableCup_Type(TruthValue):
    """Custom type cficonVsanEnableCup based on TruthValue"""


_CficonVsanEnableCup_Object = MibTableColumn
cficonVsanEnableCup = _CficonVsanEnableCup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 6),
    _CficonVsanEnableCup_Type()
)
cficonVsanEnableCup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonVsanEnableCup.setStatus("current")


class _CficonVsanCodePage_Type(Integer32):
    """Custom type cficonVsanCodePage based on Integer32"""
    defaultValue = 37

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(37,
              273,
              275,
              280,
              281,
              284,
              285,
              297,
              500)
        )
    )
    namedValues = NamedValues(
        *(("brazil", 275),
          ("france", 297),
          ("germany", 273),
          ("interNational", 500),
          ("italy", 280),
          ("japan", 281),
          ("spain", 284),
          ("uk", 285),
          ("usa", 37))
    )


_CficonVsanCodePage_Type.__name__ = "Integer32"
_CficonVsanCodePage_Object = MibTableColumn
cficonVsanCodePage = _CficonVsanCodePage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 7),
    _CficonVsanCodePage_Type()
)
cficonVsanCodePage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonVsanCodePage.setStatus("current")


class _CficonVsanCharSet_Type(Integer32):
    """Custom type cficonVsanCharSet based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("charSet697", 1)
    )


_CficonVsanCharSet_Type.__name__ = "Integer32"
_CficonVsanCharSet_Object = MibTableColumn
cficonVsanCharSet = _CficonVsanCharSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 8),
    _CficonVsanCharSet_Type()
)
cficonVsanCharSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonVsanCharSet.setStatus("current")


class _CficonVsanKeyCounter_Type(Integer32):
    """Custom type cficonVsanKeyCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CficonVsanKeyCounter_Type.__name__ = "Integer32"
_CficonVsanKeyCounter_Object = MibTableColumn
cficonVsanKeyCounter = _CficonVsanKeyCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 9),
    _CficonVsanKeyCounter_Type()
)
cficonVsanKeyCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonVsanKeyCounter.setStatus("current")


class _CficonVsanUserAlertMode_Type(TruthValue):
    """Custom type cficonVsanUserAlertMode based on TruthValue"""


_CficonVsanUserAlertMode_Object = MibTableColumn
cficonVsanUserAlertMode = _CficonVsanUserAlertMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 10),
    _CficonVsanUserAlertMode_Type()
)
cficonVsanUserAlertMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonVsanUserAlertMode.setStatus("current")


class _CficonVsanDeviceAllegience_Type(Integer32):
    """Custom type cficonVsanDeviceAllegience based on Integer32"""
    defaultValue = 4

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
        *(("lockedByCLI", 1),
          ("lockedByHost", 3),
          ("lockedBySnmp", 2),
          ("unlocked", 4))
    )


_CficonVsanDeviceAllegience_Type.__name__ = "Integer32"
_CficonVsanDeviceAllegience_Object = MibTableColumn
cficonVsanDeviceAllegience = _CficonVsanDeviceAllegience_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 11),
    _CficonVsanDeviceAllegience_Type()
)
cficonVsanDeviceAllegience.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonVsanDeviceAllegience.setStatus("current")
_CficonVsanTime_Type = DisplayString
_CficonVsanTime_Object = MibTableColumn
cficonVsanTime = _CficonVsanTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 12),
    _CficonVsanTime_Type()
)
cficonVsanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonVsanTime.setStatus("current")


class _CficonVsanHostOrDefaultTime_Type(TruthValue):
    """Custom type cficonVsanHostOrDefaultTime based on TruthValue"""


_CficonVsanHostOrDefaultTime_Object = MibTableColumn
cficonVsanHostOrDefaultTime = _CficonVsanHostOrDefaultTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 13),
    _CficonVsanHostOrDefaultTime_Type()
)
cficonVsanHostOrDefaultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonVsanHostOrDefaultTime.setStatus("current")
_CficonVsanCupName_Type = SnmpAdminString
_CficonVsanCupName_Object = MibTableColumn
cficonVsanCupName = _CficonVsanCupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 14),
    _CficonVsanCupName_Type()
)
cficonVsanCupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonVsanCupName.setStatus("current")


class _CficonSetHostTimeControl_Type(TruthValue):
    """Custom type cficonSetHostTimeControl based on TruthValue"""


_CficonSetHostTimeControl_Object = MibTableColumn
cficonSetHostTimeControl = _CficonSetHostTimeControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 15),
    _CficonSetHostTimeControl_Type()
)
cficonSetHostTimeControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonSetHostTimeControl.setStatus("current")


class _CficonVsanClearAllegience_Type(Integer32):
    """Custom type cficonVsanClearAllegience based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_CficonVsanClearAllegience_Type.__name__ = "Integer32"
_CficonVsanClearAllegience_Object = MibTableColumn
cficonVsanClearAllegience = _CficonVsanClearAllegience_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 16),
    _CficonVsanClearAllegience_Type()
)
cficonVsanClearAllegience.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonVsanClearAllegience.setStatus("current")
_CficonVsanEntryStatus_Type = RowStatus
_CficonVsanEntryStatus_Object = MibTableColumn
cficonVsanEntryStatus = _CficonVsanEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 17),
    _CficonVsanEntryStatus_Type()
)
cficonVsanEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonVsanEntryStatus.setStatus("current")


class _CficonVsanFiconState_Type(Integer32):
    """Custom type cficonVsanFiconState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )


_CficonVsanFiconState_Type.__name__ = "Integer32"
_CficonVsanFiconState_Object = MibTableColumn
cficonVsanFiconState = _CficonVsanFiconState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 18),
    _CficonVsanFiconState_Type()
)
cficonVsanFiconState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonVsanFiconState.setStatus("current")
_CficonVsanSerialNum_Type = SnmpAdminString
_CficonVsanSerialNum_Object = MibTableColumn
cficonVsanSerialNum = _CficonVsanSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 2, 1, 19),
    _CficonVsanSerialNum_Type()
)
cficonVsanSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonVsanSerialNum.setStatus("current")
_CficonPortTable_Object = MibTable
cficonPortTable = _CficonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cficonPortTable.setStatus("current")
_CficonPortEntry_Object = MibTableRow
cficonPortEntry = _CficonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 3, 1)
)
cficonPortEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FICON-MIB", "cficonCfgFilename"),
    (0, "CISCO-FICON-MIB", "cficonPortAddr"),
)
if mibBuilder.loadTexts:
    cficonPortEntry.setStatus("current")
_CficonPortAddr_Type = CficonPortNumOrAddr
_CficonPortAddr_Object = MibTableColumn
cficonPortAddr = _CficonPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 3, 1, 1),
    _CficonPortAddr_Type()
)
cficonPortAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cficonPortAddr.setStatus("current")
_CficonPortBlock_Type = TruthValue
_CficonPortBlock_Object = MibTableColumn
cficonPortBlock = _CficonPortBlock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 3, 1, 2),
    _CficonPortBlock_Type()
)
cficonPortBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonPortBlock.setStatus("current")
_CficonPortName_Type = SnmpAdminString
_CficonPortName_Object = MibTableColumn
cficonPortName = _CficonPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 3, 1, 3),
    _CficonPortName_Type()
)
cficonPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonPortName.setStatus("current")


class _CficonProhibitPortNumbers_Type(OctetString):
    """Custom type cficonProhibitPortNumbers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CficonProhibitPortNumbers_Type.__name__ = "OctetString"
_CficonProhibitPortNumbers_Object = MibTableColumn
cficonProhibitPortNumbers = _CficonProhibitPortNumbers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 3, 1, 4),
    _CficonProhibitPortNumbers_Type()
)
cficonProhibitPortNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonProhibitPortNumbers.setStatus("current")
_CficonPortRunCfgTable_Object = MibTable
cficonPortRunCfgTable = _CficonPortRunCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cficonPortRunCfgTable.setStatus("current")
_CficonPortRunCfgEntry_Object = MibTableRow
cficonPortRunCfgEntry = _CficonPortRunCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4, 1)
)
cficonPortRunCfgEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FICON-MIB", "cficonPortRunCfgAddr"),
)
if mibBuilder.loadTexts:
    cficonPortRunCfgEntry.setStatus("current")
_CficonPortRunCfgAddr_Type = CficonPortNumOrAddr
_CficonPortRunCfgAddr_Object = MibTableColumn
cficonPortRunCfgAddr = _CficonPortRunCfgAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4, 1, 1),
    _CficonPortRunCfgAddr_Type()
)
cficonPortRunCfgAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cficonPortRunCfgAddr.setStatus("current")
_CficonPortRunCfgBlock_Type = TruthValue
_CficonPortRunCfgBlock_Object = MibTableColumn
cficonPortRunCfgBlock = _CficonPortRunCfgBlock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4, 1, 2),
    _CficonPortRunCfgBlock_Type()
)
cficonPortRunCfgBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonPortRunCfgBlock.setStatus("current")
_CficonPortRunCfgName_Type = SnmpAdminString
_CficonPortRunCfgName_Object = MibTableColumn
cficonPortRunCfgName = _CficonPortRunCfgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4, 1, 3),
    _CficonPortRunCfgName_Type()
)
cficonPortRunCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonPortRunCfgName.setStatus("current")


class _CficonRunCfgProhibitPrtNums_Type(OctetString):
    """Custom type cficonRunCfgProhibitPrtNums based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_CficonRunCfgProhibitPrtNums_Type.__name__ = "OctetString"
_CficonRunCfgProhibitPrtNums_Object = MibTableColumn
cficonRunCfgProhibitPrtNums = _CficonRunCfgProhibitPrtNums_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4, 1, 4),
    _CficonRunCfgProhibitPrtNums_Type()
)
cficonRunCfgProhibitPrtNums.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonRunCfgProhibitPrtNums.setStatus("current")


class _CficonRunCfgTypeNumber_Type(DisplayString):
    """Custom type cficonRunCfgTypeNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CficonRunCfgTypeNumber_Type.__name__ = "DisplayString"
_CficonRunCfgTypeNumber_Object = MibTableColumn
cficonRunCfgTypeNumber = _CficonRunCfgTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4, 1, 5),
    _CficonRunCfgTypeNumber_Type()
)
cficonRunCfgTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonRunCfgTypeNumber.setStatus("current")


class _CficonRunCfgModelNumber_Type(DisplayString):
    """Custom type cficonRunCfgModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CficonRunCfgModelNumber_Type.__name__ = "DisplayString"
_CficonRunCfgModelNumber_Object = MibTableColumn
cficonRunCfgModelNumber = _CficonRunCfgModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4, 1, 6),
    _CficonRunCfgModelNumber_Type()
)
cficonRunCfgModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonRunCfgModelNumber.setStatus("current")


class _CficonRunCfgManufacturer_Type(DisplayString):
    """Custom type cficonRunCfgManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CficonRunCfgManufacturer_Type.__name__ = "DisplayString"
_CficonRunCfgManufacturer_Object = MibTableColumn
cficonRunCfgManufacturer = _CficonRunCfgManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4, 1, 7),
    _CficonRunCfgManufacturer_Type()
)
cficonRunCfgManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonRunCfgManufacturer.setStatus("current")


class _CficonRunCfgPlantOfMfg_Type(DisplayString):
    """Custom type cficonRunCfgPlantOfMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CficonRunCfgPlantOfMfg_Type.__name__ = "DisplayString"
_CficonRunCfgPlantOfMfg_Object = MibTableColumn
cficonRunCfgPlantOfMfg = _CficonRunCfgPlantOfMfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4, 1, 8),
    _CficonRunCfgPlantOfMfg_Type()
)
cficonRunCfgPlantOfMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonRunCfgPlantOfMfg.setStatus("current")


class _CficonRunCfgSerialNumber_Type(DisplayString):
    """Custom type cficonRunCfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CficonRunCfgSerialNumber_Type.__name__ = "DisplayString"
_CficonRunCfgSerialNumber_Object = MibTableColumn
cficonRunCfgSerialNumber = _CficonRunCfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4, 1, 9),
    _CficonRunCfgSerialNumber_Type()
)
cficonRunCfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonRunCfgSerialNumber.setStatus("current")


class _CficonRunCfgUnitType_Type(Integer32):
    """Custom type cficonRunCfgUnitType based on Integer32"""
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
        *(("channel", 1),
          ("controlUnit", 2),
          ("fabric", 3),
          ("unknown", 4))
    )


_CficonRunCfgUnitType_Type.__name__ = "Integer32"
_CficonRunCfgUnitType_Object = MibTableColumn
cficonRunCfgUnitType = _CficonRunCfgUnitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4, 1, 10),
    _CficonRunCfgUnitType_Type()
)
cficonRunCfgUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonRunCfgUnitType.setStatus("current")


class _CficonRunCfgPortId_Type(Integer32):
    """Custom type cficonRunCfgPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CficonRunCfgPortId_Type.__name__ = "Integer32"
_CficonRunCfgPortId_Object = MibTableColumn
cficonRunCfgPortId = _CficonRunCfgPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4, 1, 11),
    _CficonRunCfgPortId_Type()
)
cficonRunCfgPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonRunCfgPortId.setStatus("current")


class _CficonRunCfgStatus_Type(Integer32):
    """Custom type cficonRunCfgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("old", 3),
          ("valid", 1))
    )


_CficonRunCfgStatus_Type.__name__ = "Integer32"
_CficonRunCfgStatus_Object = MibTableColumn
cficonRunCfgStatus = _CficonRunCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 4, 1, 12),
    _CficonRunCfgStatus_Type()
)
cficonRunCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonRunCfgStatus.setStatus("current")
_CficonCfgFileTable_Object = MibTable
cficonCfgFileTable = _CficonCfgFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cficonCfgFileTable.setStatus("current")
_CficonCfgFileEntry_Object = MibTableRow
cficonCfgFileEntry = _CficonCfgFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 5, 1)
)
cficonCfgFileEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FICON-MIB", "cficonCfgFilename"),
)
if mibBuilder.loadTexts:
    cficonCfgFileEntry.setStatus("current")


class _CficonCfgFilename_Type(SnmpAdminString):
    """Custom type cficonCfgFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CficonCfgFilename_Type.__name__ = "SnmpAdminString"
_CficonCfgFilename_Object = MibTableColumn
cficonCfgFilename = _CficonCfgFilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 5, 1, 1),
    _CficonCfgFilename_Type()
)
cficonCfgFilename.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cficonCfgFilename.setStatus("current")


class _CficonCfgFileDescr_Type(SnmpAdminString):
    """Custom type cficonCfgFileDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CficonCfgFileDescr_Type.__name__ = "SnmpAdminString"
_CficonCfgFileDescr_Object = MibTableColumn
cficonCfgFileDescr = _CficonCfgFileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 5, 1, 2),
    _CficonCfgFileDescr_Type()
)
cficonCfgFileDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonCfgFileDescr.setStatus("current")


class _CficonCfgFileStatus_Type(Integer32):
    """Custom type cficonCfgFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_CficonCfgFileStatus_Type.__name__ = "Integer32"
_CficonCfgFileStatus_Object = MibTableColumn
cficonCfgFileStatus = _CficonCfgFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 5, 1, 3),
    _CficonCfgFileStatus_Type()
)
cficonCfgFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonCfgFileStatus.setStatus("current")
_CficonCfgFileLastUpdated_Type = SnmpAdminString
_CficonCfgFileLastUpdated_Object = MibTableColumn
cficonCfgFileLastUpdated = _CficonCfgFileLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 5, 1, 4),
    _CficonCfgFileLastUpdated_Type()
)
cficonCfgFileLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonCfgFileLastUpdated.setStatus("current")


class _CficonCfgFileCmd_Type(Integer32):
    """Custom type cficonCfgFileCmd based on Integer32"""
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
        *(("apply", 1),
          ("close", 4),
          ("noOp", 2),
          ("open", 3))
    )


_CficonCfgFileCmd_Type.__name__ = "Integer32"
_CficonCfgFileCmd_Object = MibTableColumn
cficonCfgFileCmd = _CficonCfgFileCmd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 5, 1, 5),
    _CficonCfgFileCmd_Type()
)
cficonCfgFileCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonCfgFileCmd.setStatus("current")
_CficonCfgFileRowStatus_Type = RowStatus
_CficonCfgFileRowStatus_Object = MibTableColumn
cficonCfgFileRowStatus = _CficonCfgFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 5, 1, 6),
    _CficonCfgFileRowStatus_Type()
)
cficonCfgFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonCfgFileRowStatus.setStatus("current")


class _CficonCfgFileCmdStatus_Type(Integer32):
    """Custom type cficonCfgFileCmdStatus based on Integer32"""
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
        *(("failed", 3),
          ("inProgress", 2),
          ("notApplicable", 4),
          ("success", 1))
    )


_CficonCfgFileCmdStatus_Type.__name__ = "Integer32"
_CficonCfgFileCmdStatus_Object = MibTableColumn
cficonCfgFileCmdStatus = _CficonCfgFileCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 5, 1, 7),
    _CficonCfgFileCmdStatus_Type()
)
cficonCfgFileCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonCfgFileCmdStatus.setStatus("current")


class _CficonCfgFileCmdErrorString_Type(SnmpAdminString):
    """Custom type cficonCfgFileCmdErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CficonCfgFileCmdErrorString_Type.__name__ = "SnmpAdminString"
_CficonCfgFileCmdErrorString_Object = MibTableColumn
cficonCfgFileCmdErrorString = _CficonCfgFileCmdErrorString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 5, 1, 8),
    _CficonCfgFileCmdErrorString_Type()
)
cficonCfgFileCmdErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonCfgFileCmdErrorString.setStatus("current")
_CficonPortNumIfTable_Object = MibTable
cficonPortNumIfTable = _CficonPortNumIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cficonPortNumIfTable.setStatus("current")
_CficonPortNumIfEntry_Object = MibTableRow
cficonPortNumIfEntry = _CficonPortNumIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 6, 1)
)
cficonPortNumIfEntry.setIndexNames(
    (0, "CISCO-FICON-MIB", "cficonPortNumber"),
)
if mibBuilder.loadTexts:
    cficonPortNumIfEntry.setStatus("current")
_CficonPortNumber_Type = CficonPortNumOrAddr
_CficonPortNumber_Object = MibTableColumn
cficonPortNumber = _CficonPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 6, 1, 1),
    _CficonPortNumber_Type()
)
cficonPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cficonPortNumber.setStatus("current")
_CficonPortIfIndex_Type = InterfaceIndex
_CficonPortIfIndex_Object = MibTableColumn
cficonPortIfIndex = _CficonPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 6, 1, 2),
    _CficonPortIfIndex_Type()
)
cficonPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonPortIfIndex.setStatus("current")
_CficonPortAddrNumTable_Object = MibTable
cficonPortAddrNumTable = _CficonPortAddrNumTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cficonPortAddrNumTable.setStatus("current")
_CficonPortAddrNumEntry_Object = MibTableRow
cficonPortAddrNumEntry = _CficonPortAddrNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 7, 1)
)
cficonPortAddrNumEntry.setIndexNames(
    (0, "CISCO-FICON-MIB", "cficonPortAddrPortAddr"),
)
if mibBuilder.loadTexts:
    cficonPortAddrNumEntry.setStatus("current")
_CficonPortAddrPortAddr_Type = CficonPortNumOrAddr
_CficonPortAddrPortAddr_Object = MibTableColumn
cficonPortAddrPortAddr = _CficonPortAddrPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 7, 1, 1),
    _CficonPortAddrPortAddr_Type()
)
cficonPortAddrPortAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cficonPortAddrPortAddr.setStatus("current")
_CficonPortAddrPortNumber_Type = CficonPortNumOrAddr
_CficonPortAddrPortNumber_Object = MibTableColumn
cficonPortAddrPortNumber = _CficonPortAddrPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 7, 1, 2),
    _CficonPortAddrPortNumber_Type()
)
cficonPortAddrPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonPortAddrPortNumber.setStatus("current")
_CficonPortNumAddrTable_Object = MibTable
cficonPortNumAddrTable = _CficonPortNumAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cficonPortNumAddrTable.setStatus("current")
_CficonPortNumAddrEntry_Object = MibTableRow
cficonPortNumAddrEntry = _CficonPortNumAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 8, 1)
)
cficonPortNumAddrEntry.setIndexNames(
    (0, "CISCO-FICON-MIB", "portAddrPortNumber"),
)
if mibBuilder.loadTexts:
    cficonPortNumAddrEntry.setStatus("current")
_PortAddrPortNumber_Type = CficonPortNumOrAddr
_PortAddrPortNumber_Object = MibTableColumn
portAddrPortNumber = _PortAddrPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 8, 1, 1),
    _PortAddrPortNumber_Type()
)
portAddrPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portAddrPortNumber.setStatus("current")
_PortAddress_Type = CficonPortNumOrAddr
_PortAddress_Object = MibTableColumn
portAddress = _PortAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 8, 1, 2),
    _PortAddress_Type()
)
portAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAddress.setStatus("current")
_CficonDirHistTable_Object = MibTable
cficonDirHistTable = _CficonDirHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cficonDirHistTable.setStatus("current")
_CficonDirHistEntry_Object = MibTableRow
cficonDirHistEntry = _CficonDirHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 9, 1)
)
cficonDirHistEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FICON-MIB", "cficonDirHistKeyCounter"),
)
if mibBuilder.loadTexts:
    cficonDirHistEntry.setStatus("current")


class _CficonDirHistKeyCounter_Type(Integer32):
    """Custom type cficonDirHistKeyCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CficonDirHistKeyCounter_Type.__name__ = "Integer32"
_CficonDirHistKeyCounter_Object = MibTableColumn
cficonDirHistKeyCounter = _CficonDirHistKeyCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 9, 1, 1),
    _CficonDirHistKeyCounter_Type()
)
cficonDirHistKeyCounter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cficonDirHistKeyCounter.setStatus("current")


class _CficonDirHistPortNumbers_Type(OctetString):
    """Custom type cficonDirHistPortNumbers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CficonDirHistPortNumbers_Type.__name__ = "OctetString"
_CficonDirHistPortNumbers_Object = MibTableColumn
cficonDirHistPortNumbers = _CficonDirHistPortNumbers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 9, 1, 2),
    _CficonDirHistPortNumbers_Type()
)
cficonDirHistPortNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonDirHistPortNumbers.setStatus("current")
_CficonStatsTable_Object = MibTable
cficonStatsTable = _CficonStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cficonStatsTable.setStatus("current")
_CficonStatsEntry_Object = MibTableRow
cficonStatsEntry = _CficonStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 10, 1)
)
cficonStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cficonStatsEntry.setStatus("current")
_CfStatsFramePacingTime_Type = Counter32
_CfStatsFramePacingTime_Object = MibTableColumn
cfStatsFramePacingTime = _CfStatsFramePacingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 10, 1, 1),
    _CfStatsFramePacingTime_Type()
)
cfStatsFramePacingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfStatsFramePacingTime.setStatus("current")
_CfStatsDispErrorsInFrame_Type = Counter32
_CfStatsDispErrorsInFrame_Object = MibTableColumn
cfStatsDispErrorsInFrame = _CfStatsDispErrorsInFrame_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 10, 1, 2),
    _CfStatsDispErrorsInFrame_Type()
)
cfStatsDispErrorsInFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfStatsDispErrorsInFrame.setStatus("current")
_CfStatsEOFErrs_Type = Counter32
_CfStatsEOFErrs_Object = MibTableColumn
cfStatsEOFErrs = _CfStatsEOFErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 10, 1, 3),
    _CfStatsEOFErrs_Type()
)
cfStatsEOFErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfStatsEOFErrs.setStatus("current")
_CfStatsDispErrsOutOfFrame_Type = Counter32
_CfStatsDispErrsOutOfFrame_Object = MibTableColumn
cfStatsDispErrsOutOfFrame = _CfStatsDispErrsOutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 10, 1, 4),
    _CfStatsDispErrsOutOfFrame_Type()
)
cfStatsDispErrsOutOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfStatsDispErrsOutOfFrame.setStatus("current")
_CfStatsInvalidOrderSets_Type = Counter32
_CfStatsInvalidOrderSets_Object = MibTableColumn
cfStatsInvalidOrderSets = _CfStatsInvalidOrderSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 10, 1, 5),
    _CfStatsInvalidOrderSets_Type()
)
cfStatsInvalidOrderSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfStatsInvalidOrderSets.setStatus("current")
_CfStatsErrorSummary_Type = Counter32
_CfStatsErrorSummary_Object = MibTableColumn
cfStatsErrorSummary = _CfStatsErrorSummary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 10, 1, 6),
    _CfStatsErrorSummary_Type()
)
cfStatsErrorSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfStatsErrorSummary.setStatus("current")


class _CficonShowPorts_Type(Integer32):
    """Custom type cficonShowPorts based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("installed", 2))
    )


_CficonShowPorts_Type.__name__ = "Integer32"
_CficonShowPorts_Object = MibScalar
cficonShowPorts = _CficonShowPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 11),
    _CficonShowPorts_Type()
)
cficonShowPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonShowPorts.setStatus("current")
_CficonLinkIncidentTable_Object = MibTable
cficonLinkIncidentTable = _CficonLinkIncidentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cficonLinkIncidentTable.setStatus("current")
_CficonLinkIncidentEntry_Object = MibTableRow
cficonLinkIncidentEntry = _CficonLinkIncidentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 12, 1)
)
cficonLinkIncidentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cficonLinkIncidentEntry.setStatus("current")


class _CficonLinkIncident_Type(Integer32):
    """Custom type cficonLinkIncident based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bitErrThreshExceeded", 2),
          ("invalidPrimitiveSeq", 6),
          ("lossOfSignalOrSync", 3),
          ("none", 1),
          ("nosReceived", 4),
          ("primitiveSeqTimeOut", 5))
    )


_CficonLinkIncident_Type.__name__ = "Integer32"
_CficonLinkIncident_Object = MibTableColumn
cficonLinkIncident = _CficonLinkIncident_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 12, 1, 1),
    _CficonLinkIncident_Type()
)
cficonLinkIncident.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonLinkIncident.setStatus("current")


class _CficonLinkIncidentTime_Type(DisplayString):
    """Custom type cficonLinkIncidentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CficonLinkIncidentTime_Type.__name__ = "DisplayString"
_CficonLinkIncidentTime_Object = MibTableColumn
cficonLinkIncidentTime = _CficonLinkIncidentTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 12, 1, 2),
    _CficonLinkIncidentTime_Type()
)
cficonLinkIncidentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonLinkIncidentTime.setStatus("current")


class _CficonLinkIncidentClear_Type(Integer32):
    """Custom type cficonLinkIncidentClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_CficonLinkIncidentClear_Type.__name__ = "Integer32"
_CficonLinkIncidentClear_Object = MibTableColumn
cficonLinkIncidentClear = _CficonLinkIncidentClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 12, 1, 3),
    _CficonLinkIncidentClear_Type()
)
cficonLinkIncidentClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonLinkIncidentClear.setStatus("current")
_CficonCfgFileCupNameTable_Object = MibTable
cficonCfgFileCupNameTable = _CficonCfgFileCupNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cficonCfgFileCupNameTable.setStatus("current")
_CficonCfgFileCupNameEntry_Object = MibTableRow
cficonCfgFileCupNameEntry = _CficonCfgFileCupNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 13, 1)
)
cficonCfgFileCupNameEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FICON-MIB", "cficonCfgFilename"),
)
if mibBuilder.loadTexts:
    cficonCfgFileCupNameEntry.setStatus("current")


class _CficonCfgFileCupName_Type(SnmpAdminString):
    """Custom type cficonCfgFileCupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_CficonCfgFileCupName_Type.__name__ = "SnmpAdminString"
_CficonCfgFileCupName_Object = MibTableColumn
cficonCfgFileCupName = _CficonCfgFileCupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 13, 1, 1),
    _CficonCfgFileCupName_Type()
)
cficonCfgFileCupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonCfgFileCupName.setStatus("current")
_CficonConfigCopyTable_Object = MibTable
cficonConfigCopyTable = _CficonConfigCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 14)
)
if mibBuilder.loadTexts:
    cficonConfigCopyTable.setStatus("current")
_CficonConfigCopyEntry_Object = MibTableRow
cficonConfigCopyEntry = _CficonConfigCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 14, 1)
)
cficonConfigCopyEntry.setIndexNames(
    (0, "CISCO-FICON-MIB", "cficonConfigCopyIndex"),
)
if mibBuilder.loadTexts:
    cficonConfigCopyEntry.setStatus("current")


class _CficonConfigCopyIndex_Type(Unsigned32):
    """Custom type cficonConfigCopyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CficonConfigCopyIndex_Type.__name__ = "Unsigned32"
_CficonConfigCopyIndex_Object = MibTableColumn
cficonConfigCopyIndex = _CficonConfigCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 14, 1, 1),
    _CficonConfigCopyIndex_Type()
)
cficonConfigCopyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cficonConfigCopyIndex.setStatus("current")


class _CficonCopyState_Type(Integer32):
    """Custom type cficonCopyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("inProgress", 1),
          ("success", 2))
    )


_CficonCopyState_Type.__name__ = "Integer32"
_CficonCopyState_Object = MibTableColumn
cficonCopyState = _CficonCopyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 14, 1, 2),
    _CficonCopyState_Type()
)
cficonCopyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonCopyState.setStatus("current")
_CficonCopyFailReason_Type = SnmpAdminString
_CficonCopyFailReason_Object = MibTableColumn
cficonCopyFailReason = _CficonCopyFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 14, 1, 3),
    _CficonCopyFailReason_Type()
)
cficonCopyFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonCopyFailReason.setStatus("current")
_CficonCopyEntryRowStatus_Type = RowStatus
_CficonCopyEntryRowStatus_Object = MibTableColumn
cficonCopyEntryRowStatus = _CficonCopyEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 14, 1, 4),
    _CficonCopyEntryRowStatus_Type()
)
cficonCopyEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonCopyEntryRowStatus.setStatus("current")


class _CficonAutoSaveState_Type(TruthValue):
    """Custom type cficonAutoSaveState based on TruthValue"""


_CficonAutoSaveState_Object = MibScalar
cficonAutoSaveState = _CficonAutoSaveState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 15),
    _CficonAutoSaveState_Type()
)
cficonAutoSaveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonAutoSaveState.setStatus("current")
_CiscoFiconPortMap_ObjectIdentity = ObjectIdentity
ciscoFiconPortMap = _CiscoFiconPortMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 16)
)


class _CficonPortMap1_Type(OctetString):
    """Custom type cficonPortMap1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CficonPortMap1_Type.__name__ = "OctetString"
_CficonPortMap1_Object = MibScalar
cficonPortMap1 = _CficonPortMap1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 16, 1),
    _CficonPortMap1_Type()
)
cficonPortMap1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonPortMap1.setStatus("deprecated")


class _CficonPortMap2_Type(OctetString):
    """Custom type cficonPortMap2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CficonPortMap2_Type.__name__ = "OctetString"
_CficonPortMap2_Object = MibScalar
cficonPortMap2 = _CficonPortMap2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 16, 2),
    _CficonPortMap2_Type()
)
cficonPortMap2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonPortMap2.setStatus("deprecated")


class _CficonPortMap3_Type(OctetString):
    """Custom type cficonPortMap3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CficonPortMap3_Type.__name__ = "OctetString"
_CficonPortMap3_Object = MibScalar
cficonPortMap3 = _CficonPortMap3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 16, 3),
    _CficonPortMap3_Type()
)
cficonPortMap3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonPortMap3.setStatus("deprecated")


class _CficonPortMap4_Type(OctetString):
    """Custom type cficonPortMap4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CficonPortMap4_Type.__name__ = "OctetString"
_CficonPortMap4_Object = MibScalar
cficonPortMap4 = _CficonPortMap4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 16, 4),
    _CficonPortMap4_Type()
)
cficonPortMap4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonPortMap4.setStatus("deprecated")


class _CficonPortMap5_Type(OctetString):
    """Custom type cficonPortMap5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CficonPortMap5_Type.__name__ = "OctetString"
_CficonPortMap5_Object = MibScalar
cficonPortMap5 = _CficonPortMap5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 16, 5),
    _CficonPortMap5_Type()
)
cficonPortMap5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonPortMap5.setStatus("deprecated")


class _CficonPortMap6_Type(OctetString):
    """Custom type cficonPortMap6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CficonPortMap6_Type.__name__ = "OctetString"
_CficonPortMap6_Object = MibScalar
cficonPortMap6 = _CficonPortMap6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 16, 6),
    _CficonPortMap6_Type()
)
cficonPortMap6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonPortMap6.setStatus("deprecated")


class _CficonPortMapMax_Type(Integer32):
    """Custom type cficonPortMapMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CficonPortMapMax_Type.__name__ = "Integer32"
_CficonPortMapMax_Object = MibScalar
cficonPortMapMax = _CficonPortMapMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 16, 7),
    _CficonPortMapMax_Type()
)
cficonPortMapMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonPortMapMax.setStatus("current")
_CficonPortMapTable_Object = MibTable
cficonPortMapTable = _CficonPortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 16, 8)
)
if mibBuilder.loadTexts:
    cficonPortMapTable.setStatus("current")
_CficonPortMapEntry_Object = MibTableRow
cficonPortMapEntry = _CficonPortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 16, 8, 1)
)
cficonPortMapEntry.setIndexNames(
    (0, "CISCO-FICON-MIB", "cficonPortMapIndex"),
)
if mibBuilder.loadTexts:
    cficonPortMapEntry.setStatus("current")


class _CficonPortMapIndex_Type(Integer32):
    """Custom type cficonPortMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CficonPortMapIndex_Type.__name__ = "Integer32"
_CficonPortMapIndex_Object = MibTableColumn
cficonPortMapIndex = _CficonPortMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 16, 8, 1, 1),
    _CficonPortMapIndex_Type()
)
cficonPortMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cficonPortMapIndex.setStatus("current")


class _CficonPortMapObj_Type(OctetString):
    """Custom type cficonPortMapObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CficonPortMapObj_Type.__name__ = "OctetString"
_CficonPortMapObj_Object = MibTableColumn
cficonPortMapObj = _CficonPortMapObj_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 16, 8, 1, 2),
    _CficonPortMapObj_Type()
)
cficonPortMapObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonPortMapObj.setStatus("current")
_CficonSlotPortNumTable_Object = MibTable
cficonSlotPortNumTable = _CficonSlotPortNumTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 17)
)
if mibBuilder.loadTexts:
    cficonSlotPortNumTable.setStatus("current")
_CficonSlotPortNumEntry_Object = MibTableRow
cficonSlotPortNumEntry = _CficonSlotPortNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 17, 1)
)
cficonSlotPortNumEntry.setIndexNames(
    (0, "CISCO-FICON-MIB", "cficonSlotIndex"),
)
if mibBuilder.loadTexts:
    cficonSlotPortNumEntry.setStatus("current")


class _CficonSlotIndex_Type(Integer32):
    """Custom type cficonSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CficonSlotIndex_Type.__name__ = "Integer32"
_CficonSlotIndex_Object = MibTableColumn
cficonSlotIndex = _CficonSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 17, 1, 1),
    _CficonSlotIndex_Type()
)
cficonSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cficonSlotIndex.setStatus("current")


class _CficonSlotReservedPN_Type(OctetString):
    """Custom type cficonSlotReservedPN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CficonSlotReservedPN_Type.__name__ = "OctetString"
_CficonSlotReservedPN_Object = MibTableColumn
cficonSlotReservedPN = _CficonSlotReservedPN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 17, 1, 2),
    _CficonSlotReservedPN_Type()
)
cficonSlotReservedPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonSlotReservedPN.setStatus("current")


class _CficonLogicReservedPN_Type(OctetString):
    """Custom type cficonLogicReservedPN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CficonLogicReservedPN_Type.__name__ = "OctetString"
_CficonLogicReservedPN_Object = MibScalar
cficonLogicReservedPN = _CficonLogicReservedPN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 18),
    _CficonLogicReservedPN_Type()
)
cficonLogicReservedPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonLogicReservedPN.setStatus("current")
_CficonRlirErlTable_Object = MibTable
cficonRlirErlTable = _CficonRlirErlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 19)
)
if mibBuilder.loadTexts:
    cficonRlirErlTable.setStatus("current")
_CficonRlirErlEntry_Object = MibTableRow
cficonRlirErlEntry = _CficonRlirErlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 19, 1)
)
cficonRlirErlEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FICON-MIB", "cficonRlirErlFcId"),
    (0, "CISCO-FICON-MIB", "cficonRlirErlFormat"),
)
if mibBuilder.loadTexts:
    cficonRlirErlEntry.setStatus("current")
_CficonRlirErlFcId_Type = FcAddressId
_CficonRlirErlFcId_Object = MibTableColumn
cficonRlirErlFcId = _CficonRlirErlFcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 19, 1, 1),
    _CficonRlirErlFcId_Type()
)
cficonRlirErlFcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cficonRlirErlFcId.setStatus("current")


class _CficonRlirErlFormat_Type(Unsigned32):
    """Custom type cficonRlirErlFormat based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CficonRlirErlFormat_Type.__name__ = "Unsigned32"
_CficonRlirErlFormat_Object = MibTableColumn
cficonRlirErlFormat = _CficonRlirErlFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 19, 1, 2),
    _CficonRlirErlFormat_Type()
)
cficonRlirErlFormat.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cficonRlirErlFormat.setStatus("current")


class _CficonRlirErlRegType_Type(Integer32):
    """Custom type cficonRlirErlRegType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwaysRx", 2),
          ("conditionalRx", 1))
    )


_CficonRlirErlRegType_Type.__name__ = "Integer32"
_CficonRlirErlRegType_Object = MibTableColumn
cficonRlirErlRegType = _CficonRlirErlRegType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 19, 1, 3),
    _CficonRlirErlRegType_Type()
)
cficonRlirErlRegType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonRlirErlRegType.setStatus("current")
_CficonInterfaceSwapTable_Object = MibTable
cficonInterfaceSwapTable = _CficonInterfaceSwapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 20)
)
if mibBuilder.loadTexts:
    cficonInterfaceSwapTable.setStatus("current")
_CficonInterfaceSwapEntry_Object = MibTableRow
cficonInterfaceSwapEntry = _CficonInterfaceSwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 20, 1)
)
cficonInterfaceSwapEntry.setIndexNames(
    (0, "CISCO-FICON-MIB", "cficonInterfaceSwapIndex"),
)
if mibBuilder.loadTexts:
    cficonInterfaceSwapEntry.setStatus("current")


class _CficonInterfaceSwapIndex_Type(Integer32):
    """Custom type cficonInterfaceSwapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CficonInterfaceSwapIndex_Type.__name__ = "Integer32"
_CficonInterfaceSwapIndex_Object = MibTableColumn
cficonInterfaceSwapIndex = _CficonInterfaceSwapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 20, 1, 1),
    _CficonInterfaceSwapIndex_Type()
)
cficonInterfaceSwapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cficonInterfaceSwapIndex.setStatus("current")
_CficonSwapInterfaceIndexFirst_Type = InterfaceIndex
_CficonSwapInterfaceIndexFirst_Object = MibTableColumn
cficonSwapInterfaceIndexFirst = _CficonSwapInterfaceIndexFirst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 20, 1, 2),
    _CficonSwapInterfaceIndexFirst_Type()
)
cficonSwapInterfaceIndexFirst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonSwapInterfaceIndexFirst.setStatus("current")
_CficonSwapInterfaceIndexSecond_Type = InterfaceIndex
_CficonSwapInterfaceIndexSecond_Object = MibTableColumn
cficonSwapInterfaceIndexSecond = _CficonSwapInterfaceIndexSecond_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 20, 1, 3),
    _CficonSwapInterfaceIndexSecond_Type()
)
cficonSwapInterfaceIndexSecond.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonSwapInterfaceIndexSecond.setStatus("current")


class _CficonSwapInterfaceActionStatus_Type(Integer32):
    """Custom type cficonSwapInterfaceActionStatus based on Integer32"""
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
        *(("executing", 2),
          ("failure", 4),
          ("pending", 1),
          ("success", 3))
    )


_CficonSwapInterfaceActionStatus_Type.__name__ = "Integer32"
_CficonSwapInterfaceActionStatus_Object = MibTableColumn
cficonSwapInterfaceActionStatus = _CficonSwapInterfaceActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 20, 1, 4),
    _CficonSwapInterfaceActionStatus_Type()
)
cficonSwapInterfaceActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonSwapInterfaceActionStatus.setStatus("current")


class _CficonSwapInterfaceFailReason_Type(Integer32):
    """Custom type cficonSwapInterfaceFailReason based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("dmFailure", 3),
          ("ficonFailure", 4),
          ("none", 2),
          ("other", 1),
          ("pmFailure", 5),
          ("psmFailure", 6),
          ("qosFailure", 7),
          ("spanFailure", 8),
          ("zsFailure", 9))
    )


_CficonSwapInterfaceFailReason_Type.__name__ = "Integer32"
_CficonSwapInterfaceFailReason_Object = MibTableColumn
cficonSwapInterfaceFailReason = _CficonSwapInterfaceFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 20, 1, 5),
    _CficonSwapInterfaceFailReason_Type()
)
cficonSwapInterfaceFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonSwapInterfaceFailReason.setStatus("current")
_CficonSwapInterfaceSystemError_Type = SnmpAdminString
_CficonSwapInterfaceSystemError_Object = MibTableColumn
cficonSwapInterfaceSystemError = _CficonSwapInterfaceSystemError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 20, 1, 6),
    _CficonSwapInterfaceSystemError_Type()
)
cficonSwapInterfaceSystemError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonSwapInterfaceSystemError.setStatus("current")
_CficonSwapInterfaceEntryStatus_Type = RowStatus
_CficonSwapInterfaceEntryStatus_Object = MibTableColumn
cficonSwapInterfaceEntryStatus = _CficonSwapInterfaceEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 20, 1, 7),
    _CficonSwapInterfaceEntryStatus_Type()
)
cficonSwapInterfaceEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cficonSwapInterfaceEntryStatus.setStatus("current")


class _CficonInterfaceSwapNextIndex_Type(Integer32):
    """Custom type cficonInterfaceSwapNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CficonInterfaceSwapNextIndex_Type.__name__ = "Integer32"
_CficonInterfaceSwapNextIndex_Object = MibScalar
cficonInterfaceSwapNextIndex = _CficonInterfaceSwapNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 1, 21),
    _CficonInterfaceSwapNextIndex_Type()
)
cficonInterfaceSwapNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cficonInterfaceSwapNextIndex.setStatus("current")
_CiscoFiconGlobal_ObjectIdentity = ObjectIdentity
ciscoFiconGlobal = _CiscoFiconGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 2)
)
_CficonDefaultPortBlock_Type = TruthValue
_CficonDefaultPortBlock_Object = MibScalar
cficonDefaultPortBlock = _CficonDefaultPortBlock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 1, 2, 1),
    _CficonDefaultPortBlock_Type()
)
cficonDefaultPortBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cficonDefaultPortBlock.setStatus("current")
_CiscoFiconMIBConform_ObjectIdentity = ObjectIdentity
ciscoFiconMIBConform = _CiscoFiconMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2)
)
_CiscoFiconCompliances_ObjectIdentity = ObjectIdentity
ciscoFiconCompliances = _CiscoFiconCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 1)
)
_CiscoFiconGroups_ObjectIdentity = ObjectIdentity
ciscoFiconGroups = _CiscoFiconGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2)
)

# Managed Objects groups

cficonPortSwapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 1)
)
cficonPortSwapGroup.setObjects(
      *(("CISCO-FICON-MIB", "cficonSwapPortNumberFirst"),
        ("CISCO-FICON-MIB", "cficonSwapPortNumberSecond"),
        ("CISCO-FICON-MIB", "cficonSwapPortEntryStatus"))
)
if mibBuilder.loadTexts:
    cficonPortSwapGroup.setStatus("current")

cficonVsanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 2)
)
cficonVsanGroup.setObjects(
      *(("CISCO-FICON-MIB", "cficonVsanHostControl"),
        ("CISCO-FICON-MIB", "cficonVsanHostControlSwOffline"),
        ("CISCO-FICON-MIB", "cficonVsanHostControlClkAlrtMode"),
        ("CISCO-FICON-MIB", "cficonVsanSnmpControl"),
        ("CISCO-FICON-MIB", "cficonVsanAutoSavePortAddrCfg"),
        ("CISCO-FICON-MIB", "cficonVsanEnableCup"),
        ("CISCO-FICON-MIB", "cficonVsanCodePage"),
        ("CISCO-FICON-MIB", "cficonVsanCharSet"),
        ("CISCO-FICON-MIB", "cficonVsanKeyCounter"),
        ("CISCO-FICON-MIB", "cficonVsanUserAlertMode"),
        ("CISCO-FICON-MIB", "cficonVsanDeviceAllegience"),
        ("CISCO-FICON-MIB", "cficonVsanTime"),
        ("CISCO-FICON-MIB", "cficonVsanHostOrDefaultTime"),
        ("CISCO-FICON-MIB", "cficonVsanCupName"),
        ("CISCO-FICON-MIB", "cficonSetHostTimeControl"),
        ("CISCO-FICON-MIB", "cficonVsanClearAllegience"),
        ("CISCO-FICON-MIB", "cficonVsanEntryStatus"),
        ("CISCO-FICON-MIB", "cficonVsanFiconState"),
        ("CISCO-FICON-MIB", "cficonVsanSerialNum"))
)
if mibBuilder.loadTexts:
    cficonVsanGroup.setStatus("current")

cficonPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 3)
)
cficonPortGroup.setObjects(
      *(("CISCO-FICON-MIB", "cficonPortBlock"),
        ("CISCO-FICON-MIB", "cficonPortName"),
        ("CISCO-FICON-MIB", "cficonProhibitPortNumbers"))
)
if mibBuilder.loadTexts:
    cficonPortGroup.setStatus("current")

cficonPortRunCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 4)
)
cficonPortRunCfgGroup.setObjects(
      *(("CISCO-FICON-MIB", "cficonPortRunCfgBlock"),
        ("CISCO-FICON-MIB", "cficonPortRunCfgName"),
        ("CISCO-FICON-MIB", "cficonRunCfgProhibitPrtNums"),
        ("CISCO-FICON-MIB", "cficonRunCfgTypeNumber"),
        ("CISCO-FICON-MIB", "cficonRunCfgModelNumber"),
        ("CISCO-FICON-MIB", "cficonRunCfgManufacturer"),
        ("CISCO-FICON-MIB", "cficonRunCfgPlantOfMfg"),
        ("CISCO-FICON-MIB", "cficonRunCfgSerialNumber"),
        ("CISCO-FICON-MIB", "cficonRunCfgUnitType"),
        ("CISCO-FICON-MIB", "cficonRunCfgPortId"),
        ("CISCO-FICON-MIB", "cficonRunCfgStatus"))
)
if mibBuilder.loadTexts:
    cficonPortRunCfgGroup.setStatus("current")

cficonCfgFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 5)
)
cficonCfgFileGroup.setObjects(
      *(("CISCO-FICON-MIB", "cficonCfgFileDescr"),
        ("CISCO-FICON-MIB", "cficonCfgFileStatus"),
        ("CISCO-FICON-MIB", "cficonCfgFileLastUpdated"),
        ("CISCO-FICON-MIB", "cficonCfgFileCmd"),
        ("CISCO-FICON-MIB", "cficonCfgFileRowStatus"),
        ("CISCO-FICON-MIB", "cficonCfgFileCmdStatus"),
        ("CISCO-FICON-MIB", "cficonCfgFileCmdErrorString"))
)
if mibBuilder.loadTexts:
    cficonCfgFileGroup.setStatus("current")

cficonPortNumIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 6)
)
cficonPortNumIfGroup.setObjects(
    ("CISCO-FICON-MIB", "cficonPortIfIndex")
)
if mibBuilder.loadTexts:
    cficonPortNumIfGroup.setStatus("current")

cficonPortAddrNumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 7)
)
cficonPortAddrNumGroup.setObjects(
    ("CISCO-FICON-MIB", "cficonPortAddrPortNumber")
)
if mibBuilder.loadTexts:
    cficonPortAddrNumGroup.setStatus("current")

cficonPortNumAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 8)
)
cficonPortNumAddrGroup.setObjects(
    ("CISCO-FICON-MIB", "portAddress")
)
if mibBuilder.loadTexts:
    cficonPortNumAddrGroup.setStatus("current")

cficonDirHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 9)
)
cficonDirHistGroup.setObjects(
    ("CISCO-FICON-MIB", "cficonDirHistPortNumbers")
)
if mibBuilder.loadTexts:
    cficonDirHistGroup.setStatus("current")

cficonStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 10)
)
cficonStatsGroup.setObjects(
      *(("CISCO-FICON-MIB", "cfStatsFramePacingTime"),
        ("CISCO-FICON-MIB", "cfStatsDispErrorsInFrame"),
        ("CISCO-FICON-MIB", "cfStatsEOFErrs"),
        ("CISCO-FICON-MIB", "cfStatsDispErrsOutOfFrame"),
        ("CISCO-FICON-MIB", "cfStatsInvalidOrderSets"),
        ("CISCO-FICON-MIB", "cfStatsErrorSummary"))
)
if mibBuilder.loadTexts:
    cficonStatsGroup.setStatus("current")

cifconShowPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 11)
)
cifconShowPortGroup.setObjects(
    ("CISCO-FICON-MIB", "cficonShowPorts")
)
if mibBuilder.loadTexts:
    cifconShowPortGroup.setStatus("current")

cficonLinkIncidentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 12)
)
cficonLinkIncidentGroup.setObjects(
      *(("CISCO-FICON-MIB", "cficonLinkIncident"),
        ("CISCO-FICON-MIB", "cficonLinkIncidentTime"),
        ("CISCO-FICON-MIB", "cficonLinkIncidentClear"))
)
if mibBuilder.loadTexts:
    cficonLinkIncidentGroup.setStatus("current")

cficonCfgFileCupNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 13)
)
cficonCfgFileCupNameGroup.setObjects(
    ("CISCO-FICON-MIB", "cficonCfgFileCupName")
)
if mibBuilder.loadTexts:
    cficonCfgFileCupNameGroup.setStatus("current")

cficonConfigCopyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 14)
)
cficonConfigCopyGroup.setObjects(
      *(("CISCO-FICON-MIB", "cficonCopyState"),
        ("CISCO-FICON-MIB", "cficonCopyFailReason"),
        ("CISCO-FICON-MIB", "cficonCopyEntryRowStatus"))
)
if mibBuilder.loadTexts:
    cficonConfigCopyGroup.setStatus("current")

cficonAutoSaveStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 15)
)
cficonAutoSaveStateGroup.setObjects(
    ("CISCO-FICON-MIB", "cficonAutoSaveState")
)
if mibBuilder.loadTexts:
    cficonAutoSaveStateGroup.setStatus("current")

cficonPortMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 16)
)
cficonPortMapGroup.setObjects(
      *(("CISCO-FICON-MIB", "cficonPortMap1"),
        ("CISCO-FICON-MIB", "cficonPortMap2"),
        ("CISCO-FICON-MIB", "cficonPortMap3"),
        ("CISCO-FICON-MIB", "cficonPortMap4"),
        ("CISCO-FICON-MIB", "cficonPortMap5"),
        ("CISCO-FICON-MIB", "cficonPortMap6"))
)
if mibBuilder.loadTexts:
    cficonPortMapGroup.setStatus("deprecated")

cficonPortMapGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 18)
)
cficonPortMapGroupRev1.setObjects(
      *(("CISCO-FICON-MIB", "cficonPortMapMax"),
        ("CISCO-FICON-MIB", "cficonPortMapObj"))
)
if mibBuilder.loadTexts:
    cficonPortMapGroupRev1.setStatus("current")

cficonReservedPortNumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 19)
)
cficonReservedPortNumGroup.setObjects(
      *(("CISCO-FICON-MIB", "cficonSlotReservedPN"),
        ("CISCO-FICON-MIB", "cficonLogicReservedPN"))
)
if mibBuilder.loadTexts:
    cficonReservedPortNumGroup.setStatus("current")

cficonRlirErlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 20)
)
cficonRlirErlGroup.setObjects(
    ("CISCO-FICON-MIB", "cficonRlirErlRegType")
)
if mibBuilder.loadTexts:
    cficonRlirErlGroup.setStatus("current")

cficonInterfaceSwapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 21)
)
cficonInterfaceSwapGroup.setObjects(
      *(("CISCO-FICON-MIB", "cficonSwapInterfaceIndexFirst"),
        ("CISCO-FICON-MIB", "cficonSwapInterfaceIndexSecond"),
        ("CISCO-FICON-MIB", "cficonSwapInterfaceActionStatus"),
        ("CISCO-FICON-MIB", "cficonSwapInterfaceFailReason"),
        ("CISCO-FICON-MIB", "cficonSwapInterfaceSystemError"),
        ("CISCO-FICON-MIB", "cficonSwapInterfaceEntryStatus"),
        ("CISCO-FICON-MIB", "cficonInterfaceSwapNextIndex"))
)
if mibBuilder.loadTexts:
    cficonInterfaceSwapGroup.setStatus("current")

cficonDefaultPortBlockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 22)
)
cficonDefaultPortBlockGroup.setObjects(
    ("CISCO-FICON-MIB", "cficonDefaultPortBlock")
)
if mibBuilder.loadTexts:
    cficonDefaultPortBlockGroup.setStatus("current")


# Notification objects

cficonPortInfoChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 0, 1)
)
cficonPortInfoChange.setObjects(
      *(("CISCO-FICON-MIB", "cficonRunCfgUnitType"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    cficonPortInfoChange.setStatus(
        "current"
    )


# Notifications groups

cficonNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 2, 17)
)
cficonNotificationGroup.setObjects(
    ("CISCO-FICON-MIB", "cficonPortInfoChange")
)
if mibBuilder.loadTexts:
    cficonNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoFiconCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFiconCompliance.setStatus(
        "deprecated"
    )

ciscoFiconComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoFiconComplianceRev1.setStatus(
        "deprecated"
    )

ciscoFiconComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoFiconComplianceRev2.setStatus(
        "deprecated"
    )

ciscoFiconComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 375, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoFiconComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FICON-MIB",
    **{"CficonPortNumOrAddr": CficonPortNumOrAddr,
       "ciscoFiconMIB": ciscoFiconMIB,
       "ciscoFiconMIBNotifications": ciscoFiconMIBNotifications,
       "cficonPortInfoChange": cficonPortInfoChange,
       "ciscoFiconMIBObjects": ciscoFiconMIBObjects,
       "ciscoFiconConfig": ciscoFiconConfig,
       "cficonPortSwapTable": cficonPortSwapTable,
       "cficonPortSwapEntry": cficonPortSwapEntry,
       "cficonPortSwapIndex": cficonPortSwapIndex,
       "cficonSwapPortNumberFirst": cficonSwapPortNumberFirst,
       "cficonSwapPortNumberSecond": cficonSwapPortNumberSecond,
       "cficonSwapPortEntryStatus": cficonSwapPortEntryStatus,
       "cficonVsanTable": cficonVsanTable,
       "cficonVsanEntry": cficonVsanEntry,
       "cficonVsanHostControl": cficonVsanHostControl,
       "cficonVsanHostControlSwOffline": cficonVsanHostControlSwOffline,
       "cficonVsanHostControlClkAlrtMode": cficonVsanHostControlClkAlrtMode,
       "cficonVsanSnmpControl": cficonVsanSnmpControl,
       "cficonVsanAutoSavePortAddrCfg": cficonVsanAutoSavePortAddrCfg,
       "cficonVsanEnableCup": cficonVsanEnableCup,
       "cficonVsanCodePage": cficonVsanCodePage,
       "cficonVsanCharSet": cficonVsanCharSet,
       "cficonVsanKeyCounter": cficonVsanKeyCounter,
       "cficonVsanUserAlertMode": cficonVsanUserAlertMode,
       "cficonVsanDeviceAllegience": cficonVsanDeviceAllegience,
       "cficonVsanTime": cficonVsanTime,
       "cficonVsanHostOrDefaultTime": cficonVsanHostOrDefaultTime,
       "cficonVsanCupName": cficonVsanCupName,
       "cficonSetHostTimeControl": cficonSetHostTimeControl,
       "cficonVsanClearAllegience": cficonVsanClearAllegience,
       "cficonVsanEntryStatus": cficonVsanEntryStatus,
       "cficonVsanFiconState": cficonVsanFiconState,
       "cficonVsanSerialNum": cficonVsanSerialNum,
       "cficonPortTable": cficonPortTable,
       "cficonPortEntry": cficonPortEntry,
       "cficonPortAddr": cficonPortAddr,
       "cficonPortBlock": cficonPortBlock,
       "cficonPortName": cficonPortName,
       "cficonProhibitPortNumbers": cficonProhibitPortNumbers,
       "cficonPortRunCfgTable": cficonPortRunCfgTable,
       "cficonPortRunCfgEntry": cficonPortRunCfgEntry,
       "cficonPortRunCfgAddr": cficonPortRunCfgAddr,
       "cficonPortRunCfgBlock": cficonPortRunCfgBlock,
       "cficonPortRunCfgName": cficonPortRunCfgName,
       "cficonRunCfgProhibitPrtNums": cficonRunCfgProhibitPrtNums,
       "cficonRunCfgTypeNumber": cficonRunCfgTypeNumber,
       "cficonRunCfgModelNumber": cficonRunCfgModelNumber,
       "cficonRunCfgManufacturer": cficonRunCfgManufacturer,
       "cficonRunCfgPlantOfMfg": cficonRunCfgPlantOfMfg,
       "cficonRunCfgSerialNumber": cficonRunCfgSerialNumber,
       "cficonRunCfgUnitType": cficonRunCfgUnitType,
       "cficonRunCfgPortId": cficonRunCfgPortId,
       "cficonRunCfgStatus": cficonRunCfgStatus,
       "cficonCfgFileTable": cficonCfgFileTable,
       "cficonCfgFileEntry": cficonCfgFileEntry,
       "cficonCfgFilename": cficonCfgFilename,
       "cficonCfgFileDescr": cficonCfgFileDescr,
       "cficonCfgFileStatus": cficonCfgFileStatus,
       "cficonCfgFileLastUpdated": cficonCfgFileLastUpdated,
       "cficonCfgFileCmd": cficonCfgFileCmd,
       "cficonCfgFileRowStatus": cficonCfgFileRowStatus,
       "cficonCfgFileCmdStatus": cficonCfgFileCmdStatus,
       "cficonCfgFileCmdErrorString": cficonCfgFileCmdErrorString,
       "cficonPortNumIfTable": cficonPortNumIfTable,
       "cficonPortNumIfEntry": cficonPortNumIfEntry,
       "cficonPortNumber": cficonPortNumber,
       "cficonPortIfIndex": cficonPortIfIndex,
       "cficonPortAddrNumTable": cficonPortAddrNumTable,
       "cficonPortAddrNumEntry": cficonPortAddrNumEntry,
       "cficonPortAddrPortAddr": cficonPortAddrPortAddr,
       "cficonPortAddrPortNumber": cficonPortAddrPortNumber,
       "cficonPortNumAddrTable": cficonPortNumAddrTable,
       "cficonPortNumAddrEntry": cficonPortNumAddrEntry,
       "portAddrPortNumber": portAddrPortNumber,
       "portAddress": portAddress,
       "cficonDirHistTable": cficonDirHistTable,
       "cficonDirHistEntry": cficonDirHistEntry,
       "cficonDirHistKeyCounter": cficonDirHistKeyCounter,
       "cficonDirHistPortNumbers": cficonDirHistPortNumbers,
       "cficonStatsTable": cficonStatsTable,
       "cficonStatsEntry": cficonStatsEntry,
       "cfStatsFramePacingTime": cfStatsFramePacingTime,
       "cfStatsDispErrorsInFrame": cfStatsDispErrorsInFrame,
       "cfStatsEOFErrs": cfStatsEOFErrs,
       "cfStatsDispErrsOutOfFrame": cfStatsDispErrsOutOfFrame,
       "cfStatsInvalidOrderSets": cfStatsInvalidOrderSets,
       "cfStatsErrorSummary": cfStatsErrorSummary,
       "cficonShowPorts": cficonShowPorts,
       "cficonLinkIncidentTable": cficonLinkIncidentTable,
       "cficonLinkIncidentEntry": cficonLinkIncidentEntry,
       "cficonLinkIncident": cficonLinkIncident,
       "cficonLinkIncidentTime": cficonLinkIncidentTime,
       "cficonLinkIncidentClear": cficonLinkIncidentClear,
       "cficonCfgFileCupNameTable": cficonCfgFileCupNameTable,
       "cficonCfgFileCupNameEntry": cficonCfgFileCupNameEntry,
       "cficonCfgFileCupName": cficonCfgFileCupName,
       "cficonConfigCopyTable": cficonConfigCopyTable,
       "cficonConfigCopyEntry": cficonConfigCopyEntry,
       "cficonConfigCopyIndex": cficonConfigCopyIndex,
       "cficonCopyState": cficonCopyState,
       "cficonCopyFailReason": cficonCopyFailReason,
       "cficonCopyEntryRowStatus": cficonCopyEntryRowStatus,
       "cficonAutoSaveState": cficonAutoSaveState,
       "ciscoFiconPortMap": ciscoFiconPortMap,
       "cficonPortMap1": cficonPortMap1,
       "cficonPortMap2": cficonPortMap2,
       "cficonPortMap3": cficonPortMap3,
       "cficonPortMap4": cficonPortMap4,
       "cficonPortMap5": cficonPortMap5,
       "cficonPortMap6": cficonPortMap6,
       "cficonPortMapMax": cficonPortMapMax,
       "cficonPortMapTable": cficonPortMapTable,
       "cficonPortMapEntry": cficonPortMapEntry,
       "cficonPortMapIndex": cficonPortMapIndex,
       "cficonPortMapObj": cficonPortMapObj,
       "cficonSlotPortNumTable": cficonSlotPortNumTable,
       "cficonSlotPortNumEntry": cficonSlotPortNumEntry,
       "cficonSlotIndex": cficonSlotIndex,
       "cficonSlotReservedPN": cficonSlotReservedPN,
       "cficonLogicReservedPN": cficonLogicReservedPN,
       "cficonRlirErlTable": cficonRlirErlTable,
       "cficonRlirErlEntry": cficonRlirErlEntry,
       "cficonRlirErlFcId": cficonRlirErlFcId,
       "cficonRlirErlFormat": cficonRlirErlFormat,
       "cficonRlirErlRegType": cficonRlirErlRegType,
       "cficonInterfaceSwapTable": cficonInterfaceSwapTable,
       "cficonInterfaceSwapEntry": cficonInterfaceSwapEntry,
       "cficonInterfaceSwapIndex": cficonInterfaceSwapIndex,
       "cficonSwapInterfaceIndexFirst": cficonSwapInterfaceIndexFirst,
       "cficonSwapInterfaceIndexSecond": cficonSwapInterfaceIndexSecond,
       "cficonSwapInterfaceActionStatus": cficonSwapInterfaceActionStatus,
       "cficonSwapInterfaceFailReason": cficonSwapInterfaceFailReason,
       "cficonSwapInterfaceSystemError": cficonSwapInterfaceSystemError,
       "cficonSwapInterfaceEntryStatus": cficonSwapInterfaceEntryStatus,
       "cficonInterfaceSwapNextIndex": cficonInterfaceSwapNextIndex,
       "ciscoFiconGlobal": ciscoFiconGlobal,
       "cficonDefaultPortBlock": cficonDefaultPortBlock,
       "ciscoFiconMIBConform": ciscoFiconMIBConform,
       "ciscoFiconCompliances": ciscoFiconCompliances,
       "ciscoFiconCompliance": ciscoFiconCompliance,
       "ciscoFiconComplianceRev1": ciscoFiconComplianceRev1,
       "ciscoFiconComplianceRev2": ciscoFiconComplianceRev2,
       "ciscoFiconComplianceRev3": ciscoFiconComplianceRev3,
       "ciscoFiconGroups": ciscoFiconGroups,
       "cficonPortSwapGroup": cficonPortSwapGroup,
       "cficonVsanGroup": cficonVsanGroup,
       "cficonPortGroup": cficonPortGroup,
       "cficonPortRunCfgGroup": cficonPortRunCfgGroup,
       "cficonCfgFileGroup": cficonCfgFileGroup,
       "cficonPortNumIfGroup": cficonPortNumIfGroup,
       "cficonPortAddrNumGroup": cficonPortAddrNumGroup,
       "cficonPortNumAddrGroup": cficonPortNumAddrGroup,
       "cficonDirHistGroup": cficonDirHistGroup,
       "cficonStatsGroup": cficonStatsGroup,
       "cifconShowPortGroup": cifconShowPortGroup,
       "cficonLinkIncidentGroup": cficonLinkIncidentGroup,
       "cficonCfgFileCupNameGroup": cficonCfgFileCupNameGroup,
       "cficonConfigCopyGroup": cficonConfigCopyGroup,
       "cficonAutoSaveStateGroup": cficonAutoSaveStateGroup,
       "cficonPortMapGroup": cficonPortMapGroup,
       "cficonNotificationGroup": cficonNotificationGroup,
       "cficonPortMapGroupRev1": cficonPortMapGroupRev1,
       "cficonReservedPortNumGroup": cficonReservedPortNumGroup,
       "cficonRlirErlGroup": cficonRlirErlGroup,
       "cficonInterfaceSwapGroup": cficonInterfaceSwapGroup,
       "cficonDefaultPortBlockGroup": cficonDefaultPortBlockGroup}
)
