# SNMP MIB module (ELS100-S24TX2M-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELS100-S24TX2M-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:54 2024
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
 internet,
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
    "internet",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

tpELS100S24TX2M = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7)
)
tpELS100S24TX2M.setRevisions(
        ("2002-08-05 17:53",
         "2002-02-20 22:02",
         "1999-10-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwitchInfo_ObjectIdentity = ObjectIdentity
switchInfo = _SwitchInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1)
)
_SwitchNumber_Type = Integer32
_SwitchNumber_Object = MibScalar
switchNumber = _SwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 1),
    _SwitchNumber_Type()
)
switchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchNumber.setStatus("current")
_SwitchInfoTable_Object = MibTable
switchInfoTable = _SwitchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2)
)
if mibBuilder.loadTexts:
    switchInfoTable.setStatus("current")
_SwitchInfoEntry_Object = MibTableRow
switchInfoEntry = _SwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1)
)
switchInfoEntry.setIndexNames(
    (0, "ELS100-S24TX2M-MIB", "swUnitIndex"),
)
if mibBuilder.loadTexts:
    switchInfoEntry.setStatus("current")
_SwUnitIndex_Type = Integer32
_SwUnitIndex_Object = MibTableColumn
swUnitIndex = _SwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 1),
    _SwUnitIndex_Type()
)
swUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swUnitIndex.setStatus("current")


class _SwMainBoardHwVer_Type(DisplayString):
    """Custom type swMainBoardHwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwMainBoardHwVer_Type.__name__ = "DisplayString"
_SwMainBoardHwVer_Object = MibTableColumn
swMainBoardHwVer = _SwMainBoardHwVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 2),
    _SwMainBoardHwVer_Type()
)
swMainBoardHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMainBoardHwVer.setStatus("current")


class _SwMainBoardFwVer_Type(DisplayString):
    """Custom type swMainBoardFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwMainBoardFwVer_Type.__name__ = "DisplayString"
_SwMainBoardFwVer_Object = MibTableColumn
swMainBoardFwVer = _SwMainBoardFwVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 3),
    _SwMainBoardFwVer_Type()
)
swMainBoardFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMainBoardFwVer.setStatus("current")


class _SwAgentBoardHwVer_Type(DisplayString):
    """Custom type swAgentBoardHwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwAgentBoardHwVer_Type.__name__ = "DisplayString"
_SwAgentBoardHwVer_Object = MibTableColumn
swAgentBoardHwVer = _SwAgentBoardHwVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 4),
    _SwAgentBoardHwVer_Type()
)
swAgentBoardHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAgentBoardHwVer.setStatus("current")


class _SwAgentBoardFwVer_Type(DisplayString):
    """Custom type swAgentBoardFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwAgentBoardFwVer_Type.__name__ = "DisplayString"
_SwAgentBoardFwVer_Object = MibTableColumn
swAgentBoardFwVer = _SwAgentBoardFwVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 5),
    _SwAgentBoardFwVer_Type()
)
swAgentBoardFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAgentBoardFwVer.setStatus("current")


class _SwAgentBoardPOSTCodeVer_Type(DisplayString):
    """Custom type swAgentBoardPOSTCodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwAgentBoardPOSTCodeVer_Type.__name__ = "DisplayString"
_SwAgentBoardPOSTCodeVer_Object = MibTableColumn
swAgentBoardPOSTCodeVer = _SwAgentBoardPOSTCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 6),
    _SwAgentBoardPOSTCodeVer_Type()
)
swAgentBoardPOSTCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAgentBoardPOSTCodeVer.setStatus("current")
_SwPortNumber_Type = Integer32
_SwPortNumber_Object = MibTableColumn
swPortNumber = _SwPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 7),
    _SwPortNumber_Type()
)
swPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortNumber.setStatus("current")


class _SwPowerStatus_Type(Integer32):
    """Custom type swPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internalAndRedundantPower", 3),
          ("internalPower", 1),
          ("redundantPower", 2))
    )


_SwPowerStatus_Type.__name__ = "Integer32"
_SwPowerStatus_Object = MibTableColumn
swPowerStatus = _SwPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 8),
    _SwPowerStatus_Type()
)
swPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPowerStatus.setStatus("current")


class _SwExpansionSlot1_Type(Integer32):
    """Custom type swExpansionSlot1 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("hundredBaseFX1Port", 4),
          ("hundredBaseFX2Port", 1),
          ("notPresent", 10),
          ("other", 9),
          ("stackingModule2GB", 8),
          ("stackingModule4GB", 3),
          ("thousandBaseGBIC", 7),
          ("thousandBaseLX", 5),
          ("thousandBaseSX", 2),
          ("thousandBaseT", 6))
    )


_SwExpansionSlot1_Type.__name__ = "Integer32"
_SwExpansionSlot1_Object = MibTableColumn
swExpansionSlot1 = _SwExpansionSlot1_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 9),
    _SwExpansionSlot1_Type()
)
swExpansionSlot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swExpansionSlot1.setStatus("current")


class _SwExpansionSlot2_Type(Integer32):
    """Custom type swExpansionSlot2 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("hundredBaseFX1Port", 4),
          ("hundredBaseFX2Port", 1),
          ("notPresent", 10),
          ("other", 9),
          ("stackingModule2GB", 8),
          ("stackingModule4GB", 3),
          ("thousandBaseGBIC", 7),
          ("thousandBaseLX", 5),
          ("thousandBaseSX", 2),
          ("thousandBaseT", 6))
    )


_SwExpansionSlot2_Type.__name__ = "Integer32"
_SwExpansionSlot2_Object = MibTableColumn
swExpansionSlot2 = _SwExpansionSlot2_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 10),
    _SwExpansionSlot2_Type()
)
swExpansionSlot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swExpansionSlot2.setStatus("current")


class _SwRoleInSystem_Type(Integer32):
    """Custom type swRoleInSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupMaster", 2),
          ("master", 1),
          ("slave", 3))
    )


_SwRoleInSystem_Type.__name__ = "Integer32"
_SwRoleInSystem_Object = MibTableColumn
swRoleInSystem = _SwRoleInSystem_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 11),
    _SwRoleInSystem_Type()
)
swRoleInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRoleInSystem.setStatus("current")
_SwitchOIDTable_Object = MibTable
switchOIDTable = _SwitchOIDTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 3)
)
if mibBuilder.loadTexts:
    switchOIDTable.setStatus("current")
_SwitchOIDEntry_Object = MibTableRow
switchOIDEntry = _SwitchOIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 3, 1)
)
switchOIDEntry.setIndexNames(
    (0, "ELS100-S24TX2M-MIB", "switchOIDIndex"),
)
if mibBuilder.loadTexts:
    switchOIDEntry.setStatus("current")


class _SwitchOIDIndex_Type(Integer32):
    """Custom type switchOIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwitchOIDIndex_Type.__name__ = "Integer32"
_SwitchOIDIndex_Object = MibTableColumn
switchOIDIndex = _SwitchOIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 3, 1, 1),
    _SwitchOIDIndex_Type()
)
switchOIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchOIDIndex.setStatus("current")
_SwitchOIDValue_Type = ObjectIdentifier
_SwitchOIDValue_Object = MibTableColumn
switchOIDValue = _SwitchOIDValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 3, 1, 2),
    _SwitchOIDValue_Type()
)
switchOIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchOIDValue.setStatus("current")
_SwitchPortMgt_ObjectIdentity = ObjectIdentity
switchPortMgt = _SwitchPortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2)
)
_SwitchPortMgtTable_Object = MibTable
switchPortMgtTable = _SwitchPortMgtTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1)
)
if mibBuilder.loadTexts:
    switchPortMgtTable.setStatus("current")
_SwitchPortMgtEntry_Object = MibTableRow
switchPortMgtEntry = _SwitchPortMgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1)
)
switchPortMgtEntry.setIndexNames(
    (0, "ELS100-S24TX2M-MIB", "swUnitIndex"),
    (0, "ELS100-S24TX2M-MIB", "swPortMgtIndex"),
)
if mibBuilder.loadTexts:
    switchPortMgtEntry.setStatus("current")
_SwPortMgtIndex_Type = Integer32
_SwPortMgtIndex_Object = MibTableColumn
swPortMgtIndex = _SwPortMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1, 1),
    _SwPortMgtIndex_Type()
)
swPortMgtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPortMgtIndex.setStatus("current")


class _SwPortMgtPortType_Type(Integer32):
    """Custom type swPortMgtPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hundredBaseFX", 2),
          ("hundredBaseTX", 1),
          ("thousandBaseSX", 3))
    )


_SwPortMgtPortType_Type.__name__ = "Integer32"
_SwPortMgtPortType_Object = MibTableColumn
swPortMgtPortType = _SwPortMgtPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1, 2),
    _SwPortMgtPortType_Type()
)
swPortMgtPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortMgtPortType.setStatus("current")


class _SwPortMgtSpeedDpxAdmin_Type(Integer32):
    """Custom type swPortMgtSpeedDpxAdmin based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiation", 7),
          ("fullDuplex10", 2),
          ("fullDuplex100", 4),
          ("fullDuplex1000", 6),
          ("halfDuplex10", 1),
          ("halfDuplex100", 3),
          ("halfDuplex1000", 5))
    )


_SwPortMgtSpeedDpxAdmin_Type.__name__ = "Integer32"
_SwPortMgtSpeedDpxAdmin_Object = MibTableColumn
swPortMgtSpeedDpxAdmin = _SwPortMgtSpeedDpxAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1, 3),
    _SwPortMgtSpeedDpxAdmin_Type()
)
swPortMgtSpeedDpxAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMgtSpeedDpxAdmin.setStatus("current")


class _SwPortMgtSpeedDpxInUse_Type(Integer32):
    """Custom type swPortMgtSpeedDpxInUse based on Integer32"""
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
        *(("fullDuplex10", 2),
          ("fullDuplex100", 4),
          ("fullDuplex1000", 6),
          ("halfDuplex10", 1),
          ("halfDuplex100", 3),
          ("halfDuplex1000", 5))
    )


_SwPortMgtSpeedDpxInUse_Type.__name__ = "Integer32"
_SwPortMgtSpeedDpxInUse_Object = MibTableColumn
swPortMgtSpeedDpxInUse = _SwPortMgtSpeedDpxInUse_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1, 4),
    _SwPortMgtSpeedDpxInUse_Type()
)
swPortMgtSpeedDpxInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortMgtSpeedDpxInUse.setStatus("current")


class _SwPortMgtFlowCtrlAdmin_Type(Integer32):
    """Custom type swPortMgtFlowCtrlAdmin based on Integer32"""
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
        *(("backPressure", 3),
          ("disabled", 2),
          ("dot3xFlowControl", 4),
          ("enabled", 1))
    )


_SwPortMgtFlowCtrlAdmin_Type.__name__ = "Integer32"
_SwPortMgtFlowCtrlAdmin_Object = MibTableColumn
swPortMgtFlowCtrlAdmin = _SwPortMgtFlowCtrlAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1, 5),
    _SwPortMgtFlowCtrlAdmin_Type()
)
swPortMgtFlowCtrlAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMgtFlowCtrlAdmin.setStatus("current")


class _SwPortMgtFlowCtrlInUse_Type(Integer32):
    """Custom type swPortMgtFlowCtrlInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backPressure", 1),
          ("dot3xFlowControl", 2),
          ("none", 3))
    )


_SwPortMgtFlowCtrlInUse_Type.__name__ = "Integer32"
_SwPortMgtFlowCtrlInUse_Object = MibTableColumn
swPortMgtFlowCtrlInUse = _SwPortMgtFlowCtrlInUse_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1, 6),
    _SwPortMgtFlowCtrlInUse_Type()
)
swPortMgtFlowCtrlInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortMgtFlowCtrlInUse.setStatus("current")
_SystemSTAMgt_ObjectIdentity = ObjectIdentity
systemSTAMgt = _SystemSTAMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 3)
)


class _SystemSTAStatus_Type(Integer32):
    """Custom type systemSTAStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SystemSTAStatus_Type.__name__ = "Integer32"
_SystemSTAStatus_Object = MibScalar
systemSTAStatus = _SystemSTAStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 3, 1),
    _SystemSTAStatus_Type()
)
systemSTAStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSTAStatus.setStatus("current")
_TftpDownloadMgt_ObjectIdentity = ObjectIdentity
tftpDownloadMgt = _TftpDownloadMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 4)
)


class _TftpDownloadServerIP_Type(IpAddress):
    """Custom type tftpDownloadServerIP based on IpAddress"""
    defaultHexValue = "00000000"


_TftpDownloadServerIP_Object = MibScalar
tftpDownloadServerIP = _TftpDownloadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 4, 1),
    _TftpDownloadServerIP_Type()
)
tftpDownloadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDownloadServerIP.setStatus("current")


class _TftpDownloadAgentBoardFwFileName_Type(DisplayString):
    """Custom type tftpDownloadAgentBoardFwFileName based on DisplayString"""
    defaultValue = OctetString("es3526f.bin")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TftpDownloadAgentBoardFwFileName_Type.__name__ = "DisplayString"
_TftpDownloadAgentBoardFwFileName_Object = MibScalar
tftpDownloadAgentBoardFwFileName = _TftpDownloadAgentBoardFwFileName_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 4, 2),
    _TftpDownloadAgentBoardFwFileName_Type()
)
tftpDownloadAgentBoardFwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDownloadAgentBoardFwFileName.setStatus("current")


class _TftpDownloadAgentBoardFwDownloadNode_Type(Integer32):
    """Custom type tftpDownloadAgentBoardFwDownloadNode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 1),
          ("temporary", 2))
    )


_TftpDownloadAgentBoardFwDownloadNode_Type.__name__ = "Integer32"
_TftpDownloadAgentBoardFwDownloadNode_Object = MibScalar
tftpDownloadAgentBoardFwDownloadNode = _TftpDownloadAgentBoardFwDownloadNode_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 4, 3),
    _TftpDownloadAgentBoardFwDownloadNode_Type()
)
tftpDownloadAgentBoardFwDownloadNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDownloadAgentBoardFwDownloadNode.setStatus("current")


class _TftpDownloadStatus_Type(Integer32):
    """Custom type tftpDownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_TftpDownloadStatus_Type.__name__ = "Integer32"
_TftpDownloadStatus_Object = MibScalar
tftpDownloadStatus = _TftpDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 4, 4),
    _TftpDownloadStatus_Type()
)
tftpDownloadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDownloadStatus.setStatus("current")
_RestartMgt_ObjectIdentity = ObjectIdentity
restartMgt = _RestartMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 5)
)


class _RestartOptionPOST_Type(Integer32):
    """Custom type restartOptionPOST based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RestartOptionPOST_Type.__name__ = "Integer32"
_RestartOptionPOST_Object = MibScalar
restartOptionPOST = _RestartOptionPOST_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 5, 1),
    _RestartOptionPOST_Type()
)
restartOptionPOST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartOptionPOST.setStatus("current")


class _RestartOptionReloadFactoryDefault_Type(Integer32):
    """Custom type restartOptionReloadFactoryDefault based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RestartOptionReloadFactoryDefault_Type.__name__ = "Integer32"
_RestartOptionReloadFactoryDefault_Object = MibScalar
restartOptionReloadFactoryDefault = _RestartOptionReloadFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 5, 2),
    _RestartOptionReloadFactoryDefault_Type()
)
restartOptionReloadFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartOptionReloadFactoryDefault.setStatus("current")


class _RestartOptionKeepIpSetting_Type(Integer32):
    """Custom type restartOptionKeepIpSetting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RestartOptionKeepIpSetting_Type.__name__ = "Integer32"
_RestartOptionKeepIpSetting_Object = MibScalar
restartOptionKeepIpSetting = _RestartOptionKeepIpSetting_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 5, 3),
    _RestartOptionKeepIpSetting_Type()
)
restartOptionKeepIpSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartOptionKeepIpSetting.setStatus("current")


class _RestartOptionKeepUserAuthentication_Type(Integer32):
    """Custom type restartOptionKeepUserAuthentication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RestartOptionKeepUserAuthentication_Type.__name__ = "Integer32"
_RestartOptionKeepUserAuthentication_Object = MibScalar
restartOptionKeepUserAuthentication = _RestartOptionKeepUserAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 5, 4),
    _RestartOptionKeepUserAuthentication_Type()
)
restartOptionKeepUserAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartOptionKeepUserAuthentication.setStatus("current")


class _RestartAction_Type(Integer32):
    """Custom type restartAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_RestartAction_Type.__name__ = "Integer32"
_RestartAction_Object = MibScalar
restartAction = _RestartAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 5, 5),
    _RestartAction_Type()
)
restartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartAction.setStatus("current")
_PortMirrorMgt_ObjectIdentity = ObjectIdentity
portMirrorMgt = _PortMirrorMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 6)
)


class _PortMirrorStatus_Type(Integer32):
    """Custom type portMirrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PortMirrorStatus_Type.__name__ = "Integer32"
_PortMirrorStatus_Object = MibScalar
portMirrorStatus = _PortMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 6, 1),
    _PortMirrorStatus_Type()
)
portMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMirrorStatus.setStatus("current")
_PortMirrorSnifferPort_Type = Integer32
_PortMirrorSnifferPort_Object = MibScalar
portMirrorSnifferPort = _PortMirrorSnifferPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 6, 2),
    _PortMirrorSnifferPort_Type()
)
portMirrorSnifferPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMirrorSnifferPort.setStatus("current")
_PortMirrorMirroredPort_Type = Integer32
_PortMirrorMirroredPort_Object = MibScalar
portMirrorMirroredPort = _PortMirrorMirroredPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 6, 3),
    _PortMirrorMirroredPort_Type()
)
portMirrorMirroredPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMirrorMirroredPort.setStatus("current")
_IgmpMgt_ObjectIdentity = ObjectIdentity
igmpMgt = _IgmpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 7)
)


class _IgmpStatus_Type(Integer32):
    """Custom type igmpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IgmpStatus_Type.__name__ = "Integer32"
_IgmpStatus_Object = MibScalar
igmpStatus = _IgmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 7, 1),
    _IgmpStatus_Type()
)
igmpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpStatus.setStatus("current")


class _IgmpQueryCount_Type(Integer32):
    """Custom type igmpQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_IgmpQueryCount_Type.__name__ = "Integer32"
_IgmpQueryCount_Object = MibScalar
igmpQueryCount = _IgmpQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 7, 2),
    _IgmpQueryCount_Type()
)
igmpQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpQueryCount.setStatus("current")


class _IgmpReportDelay_Type(Integer32):
    """Custom type igmpReportDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_IgmpReportDelay_Type.__name__ = "Integer32"
_IgmpReportDelay_Object = MibScalar
igmpReportDelay = _IgmpReportDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 7, 3),
    _IgmpReportDelay_Type()
)
igmpReportDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpReportDelay.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELS100-S24TX2M-MIB",
    **{"tpELS100S24TX2M": tpELS100S24TX2M,
       "switchInfo": switchInfo,
       "switchNumber": switchNumber,
       "switchInfoTable": switchInfoTable,
       "switchInfoEntry": switchInfoEntry,
       "swUnitIndex": swUnitIndex,
       "swMainBoardHwVer": swMainBoardHwVer,
       "swMainBoardFwVer": swMainBoardFwVer,
       "swAgentBoardHwVer": swAgentBoardHwVer,
       "swAgentBoardFwVer": swAgentBoardFwVer,
       "swAgentBoardPOSTCodeVer": swAgentBoardPOSTCodeVer,
       "swPortNumber": swPortNumber,
       "swPowerStatus": swPowerStatus,
       "swExpansionSlot1": swExpansionSlot1,
       "swExpansionSlot2": swExpansionSlot2,
       "swRoleInSystem": swRoleInSystem,
       "switchOIDTable": switchOIDTable,
       "switchOIDEntry": switchOIDEntry,
       "switchOIDIndex": switchOIDIndex,
       "switchOIDValue": switchOIDValue,
       "switchPortMgt": switchPortMgt,
       "switchPortMgtTable": switchPortMgtTable,
       "switchPortMgtEntry": switchPortMgtEntry,
       "swPortMgtIndex": swPortMgtIndex,
       "swPortMgtPortType": swPortMgtPortType,
       "swPortMgtSpeedDpxAdmin": swPortMgtSpeedDpxAdmin,
       "swPortMgtSpeedDpxInUse": swPortMgtSpeedDpxInUse,
       "swPortMgtFlowCtrlAdmin": swPortMgtFlowCtrlAdmin,
       "swPortMgtFlowCtrlInUse": swPortMgtFlowCtrlInUse,
       "systemSTAMgt": systemSTAMgt,
       "systemSTAStatus": systemSTAStatus,
       "tftpDownloadMgt": tftpDownloadMgt,
       "tftpDownloadServerIP": tftpDownloadServerIP,
       "tftpDownloadAgentBoardFwFileName": tftpDownloadAgentBoardFwFileName,
       "tftpDownloadAgentBoardFwDownloadNode": tftpDownloadAgentBoardFwDownloadNode,
       "tftpDownloadStatus": tftpDownloadStatus,
       "restartMgt": restartMgt,
       "restartOptionPOST": restartOptionPOST,
       "restartOptionReloadFactoryDefault": restartOptionReloadFactoryDefault,
       "restartOptionKeepIpSetting": restartOptionKeepIpSetting,
       "restartOptionKeepUserAuthentication": restartOptionKeepUserAuthentication,
       "restartAction": restartAction,
       "portMirrorMgt": portMirrorMgt,
       "portMirrorStatus": portMirrorStatus,
       "portMirrorSnifferPort": portMirrorSnifferPort,
       "portMirrorMirroredPort": portMirrorMirroredPort,
       "igmpMgt": igmpMgt,
       "igmpStatus": igmpStatus,
       "igmpQueryCount": igmpQueryCount,
       "igmpReportDelay": igmpReportDelay}
)
