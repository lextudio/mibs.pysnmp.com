# SNMP MIB module (CISCO-WAN-FR-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-FR-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:04 2024
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

(frPort,
 frPortCnf,
 frPortCnt,
 frPortServiceQueGrp) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "frPort",
    "frPortCnf",
    "frPortCnt",
    "frPortServiceQueGrp")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoWanFrPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 44)
)
ciscoWanFrPortMIB.setRevisions(
        ("2002-10-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrPortCnfPortGrp_ObjectIdentity = ObjectIdentity
frPortCnfPortGrp = _FrPortCnfPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1)
)
_FrPortCnfPortGrpTable_Object = MibTable
frPortCnfPortGrpTable = _FrPortCnfPortGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    frPortCnfPortGrpTable.setStatus("current")
_FrPortCnfPortGrpEntry_Object = MibTableRow
frPortCnfPortGrpEntry = _FrPortCnfPortGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1)
)
frPortCnfPortGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-PORT-MIB", "portNum"),
)
if mibBuilder.loadTexts:
    frPortCnfPortGrpEntry.setStatus("current")


class _PortNum_Type(Integer32):
    """Custom type portNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortNum_Type.__name__ = "Integer32"
_PortNum_Object = MibTableColumn
portNum = _PortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 1),
    _PortNum_Type()
)
portNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNum.setStatus("current")


class _PortLineNum_Type(Integer32):
    """Custom type portLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortLineNum_Type.__name__ = "Integer32"
_PortLineNum_Object = MibTableColumn
portLineNum = _PortLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 2),
    _PortLineNum_Type()
)
portLineNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLineNum.setStatus("current")


class _PortRowStatus_Type(Integer32):
    """Custom type portRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2),
          ("mod", 3))
    )


_PortRowStatus_Type.__name__ = "Integer32"
_PortRowStatus_Object = MibTableColumn
portRowStatus = _PortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 3),
    _PortRowStatus_Type()
)
portRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portRowStatus.setStatus("current")


class _PortDs0ConfigBitMap_Type(Integer32):
    """Custom type portDs0ConfigBitMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_PortDs0ConfigBitMap_Type.__name__ = "Integer32"
_PortDs0ConfigBitMap_Object = MibTableColumn
portDs0ConfigBitMap = _PortDs0ConfigBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 4),
    _PortDs0ConfigBitMap_Type()
)
portDs0ConfigBitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDs0ConfigBitMap.setStatus("current")


class _PortDs0Speed_Type(Integer32):
    """Custom type portDs0Speed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed56k", 1),
          ("speed64k", 2),
          ("unUsed", 3))
    )


_PortDs0Speed_Type.__name__ = "Integer32"
_PortDs0Speed_Object = MibTableColumn
portDs0Speed = _PortDs0Speed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 5),
    _PortDs0Speed_Type()
)
portDs0Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDs0Speed.setStatus("current")


class _PortFlagsBetweenFrames_Type(Integer32):
    """Custom type portFlagsBetweenFrames based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PortFlagsBetweenFrames_Type.__name__ = "Integer32"
_PortFlagsBetweenFrames_Object = MibTableColumn
portFlagsBetweenFrames = _PortFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 6),
    _PortFlagsBetweenFrames_Type()
)
portFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFlagsBetweenFrames.setStatus("current")


class _PortEqueueServiceRatio_Type(Integer32):
    """Custom type portEqueueServiceRatio based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PortEqueueServiceRatio_Type.__name__ = "Integer32"
_PortEqueueServiceRatio_Object = MibTableColumn
portEqueueServiceRatio = _PortEqueueServiceRatio_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 7),
    _PortEqueueServiceRatio_Type()
)
portEqueueServiceRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEqueueServiceRatio.setStatus("current")
_PortSpeed_Type = Integer32
_PortSpeed_Object = MibTableColumn
portSpeed = _PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 8),
    _PortSpeed_Type()
)
portSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpeed.setStatus("current")
if mibBuilder.loadTexts:
    portSpeed.setUnits("kbps")


class _PortAdmin_Type(Integer32):
    """Custom type portAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1),
          ("write-Only", 3))
    )


_PortAdmin_Type.__name__ = "Integer32"
_PortAdmin_Object = MibTableColumn
portAdmin = _PortAdmin_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 9),
    _PortAdmin_Type()
)
portAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdmin.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frFUNI", 2),
          ("frame-forward", 3),
          ("frame-relay", 1))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 10),
    _PortType_Type()
)
portType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _PortSvcStatus_Type(Integer32):
    """Custom type portSvcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PortSvcStatus_Type.__name__ = "Integer32"
_PortSvcStatus_Object = MibTableColumn
portSvcStatus = _PortSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 11),
    _PortSvcStatus_Type()
)
portSvcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSvcStatus.setStatus("current")


class _PortSvcInUse_Type(Integer32):
    """Custom type portSvcInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-use", 2),
          ("not-use", 1))
    )


_PortSvcInUse_Type.__name__ = "Integer32"
_PortSvcInUse_Object = MibTableColumn
portSvcInUse = _PortSvcInUse_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 12),
    _PortSvcInUse_Type()
)
portSvcInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSvcInUse.setStatus("current")


class _PortSvcShareLcn_Type(Integer32):
    """Custom type portSvcShareLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("card-based", 2),
          ("port-based", 1))
    )


_PortSvcShareLcn_Type.__name__ = "Integer32"
_PortSvcShareLcn_Object = MibTableColumn
portSvcShareLcn = _PortSvcShareLcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 13),
    _PortSvcShareLcn_Type()
)
portSvcShareLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSvcShareLcn.setStatus("current")


class _PortSvcLcnLow_Type(Integer32):
    """Custom type portSvcLcnLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4015),
    )


_PortSvcLcnLow_Type.__name__ = "Integer32"
_PortSvcLcnLow_Object = MibTableColumn
portSvcLcnLow = _PortSvcLcnLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 14),
    _PortSvcLcnLow_Type()
)
portSvcLcnLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSvcLcnLow.setStatus("current")


class _PortSvcLcnHigh_Type(Integer32):
    """Custom type portSvcLcnHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4015),
    )


_PortSvcLcnHigh_Type.__name__ = "Integer32"
_PortSvcLcnHigh_Object = MibTableColumn
portSvcLcnHigh = _PortSvcLcnHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 15),
    _PortSvcLcnHigh_Type()
)
portSvcLcnHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSvcLcnHigh.setStatus("current")


class _PortSvcDlciLow_Type(Integer32):
    """Custom type portSvcDlciLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_PortSvcDlciLow_Type.__name__ = "Integer32"
_PortSvcDlciLow_Object = MibTableColumn
portSvcDlciLow = _PortSvcDlciLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 16),
    _PortSvcDlciLow_Type()
)
portSvcDlciLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSvcDlciLow.setStatus("current")


class _PortSvcDlciHigh_Type(Integer32):
    """Custom type portSvcDlciHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_PortSvcDlciHigh_Type.__name__ = "Integer32"
_PortSvcDlciHigh_Object = MibTableColumn
portSvcDlciHigh = _PortSvcDlciHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 17),
    _PortSvcDlciHigh_Type()
)
portSvcDlciHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSvcDlciHigh.setStatus("current")


class _PortDeleteSvcs_Type(Integer32):
    """Custom type portDeleteSvcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("other", 2))
    )


_PortDeleteSvcs_Type.__name__ = "Integer32"
_PortDeleteSvcs_Object = MibTableColumn
portDeleteSvcs = _PortDeleteSvcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 18),
    _PortDeleteSvcs_Type()
)
portDeleteSvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDeleteSvcs.setStatus("current")
_PortIngrSvcBandW_Type = Integer32
_PortIngrSvcBandW_Object = MibTableColumn
portIngrSvcBandW = _PortIngrSvcBandW_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 19),
    _PortIngrSvcBandW_Type()
)
portIngrSvcBandW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIngrSvcBandW.setStatus("current")
_PortEgrSvcBandW_Type = Integer32
_PortEgrSvcBandW_Object = MibTableColumn
portEgrSvcBandW = _PortEgrSvcBandW_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 20),
    _PortEgrSvcBandW_Type()
)
portEgrSvcBandW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portEgrSvcBandW.setStatus("current")


class _PortBERTEnable_Type(Integer32):
    """Custom type portBERTEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PortBERTEnable_Type.__name__ = "Integer32"
_PortBERTEnable_Object = MibTableColumn
portBERTEnable = _PortBERTEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 21),
    _PortBERTEnable_Type()
)
portBERTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBERTEnable.setStatus("current")


class _PortEnhancedSIW_Type(Integer32):
    """Custom type portEnhancedSIW based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PortEnhancedSIW_Type.__name__ = "Integer32"
_PortEnhancedSIW_Object = MibTableColumn
portEnhancedSIW = _PortEnhancedSIW_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 22),
    _PortEnhancedSIW_Type()
)
portEnhancedSIW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEnhancedSIW.setStatus("current")


class _PortM32EgrQueueThresh_Type(Integer32):
    """Custom type portM32EgrQueueThresh based on Integer32"""
    defaultValue = 6000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_PortM32EgrQueueThresh_Type.__name__ = "Integer32"
_PortM32EgrQueueThresh_Object = MibTableColumn
portM32EgrQueueThresh = _PortM32EgrQueueThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 23),
    _PortM32EgrQueueThresh_Type()
)
portM32EgrQueueThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portM32EgrQueueThresh.setStatus("current")
if mibBuilder.loadTexts:
    portM32EgrQueueThresh.setUnits("bytes")


class _PortHeaderLen_Type(Integer32):
    """Custom type portHeaderLen based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourOctets", 2),
          ("twoOctets", 1))
    )


_PortHeaderLen_Type.__name__ = "Integer32"
_PortHeaderLen_Object = MibTableColumn
portHeaderLen = _PortHeaderLen_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 24),
    _PortHeaderLen_Type()
)
portHeaderLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portHeaderLen.setStatus("current")
if mibBuilder.loadTexts:
    portHeaderLen.setUnits("Octets")


class _PortFrameChkSumType_Type(Integer32):
    """Custom type portFrameChkSumType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_PortFrameChkSumType_Type.__name__ = "Integer32"
_PortFrameChkSumType_Object = MibTableColumn
portFrameChkSumType = _PortFrameChkSumType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 25),
    _PortFrameChkSumType_Type()
)
portFrameChkSumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFrameChkSumType.setStatus("current")


class _PortFileId_Type(Integer32):
    """Custom type portFileId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortFileId_Type.__name__ = "Integer32"
_PortFileId_Object = MibTableColumn
portFileId = _PortFileId_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 26),
    _PortFileId_Type()
)
portFileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFileId.setStatus("current")


class _PortOverSubEnable_Type(Integer32):
    """Custom type portOverSubEnable based on Integer32"""
    defaultValue = 2

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


_PortOverSubEnable_Type.__name__ = "Integer32"
_PortOverSubEnable_Object = MibTableColumn
portOverSubEnable = _PortOverSubEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 1, 1, 27),
    _PortOverSubEnable_Type()
)
portOverSubEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOverSubEnable.setStatus("current")


class _PortsUsedLine1_Type(Integer32):
    """Custom type portsUsedLine1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_PortsUsedLine1_Type.__name__ = "Integer32"
_PortsUsedLine1_Object = MibScalar
portsUsedLine1 = _PortsUsedLine1_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 2),
    _PortsUsedLine1_Type()
)
portsUsedLine1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsUsedLine1.setStatus("current")


class _PortsUsedLine2_Type(Integer32):
    """Custom type portsUsedLine2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_PortsUsedLine2_Type.__name__ = "Integer32"
_PortsUsedLine2_Object = MibScalar
portsUsedLine2 = _PortsUsedLine2_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 3),
    _PortsUsedLine2_Type()
)
portsUsedLine2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsUsedLine2.setStatus("current")


class _PortsUsedLine3_Type(Integer32):
    """Custom type portsUsedLine3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_PortsUsedLine3_Type.__name__ = "Integer32"
_PortsUsedLine3_Object = MibScalar
portsUsedLine3 = _PortsUsedLine3_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 4),
    _PortsUsedLine3_Type()
)
portsUsedLine3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsUsedLine3.setStatus("current")


class _PortsUsedLine4_Type(Integer32):
    """Custom type portsUsedLine4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_PortsUsedLine4_Type.__name__ = "Integer32"
_PortsUsedLine4_Object = MibScalar
portsUsedLine4 = _PortsUsedLine4_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 5),
    _PortsUsedLine4_Type()
)
portsUsedLine4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsUsedLine4.setStatus("current")


class _PortNextAvailable_Type(Integer32):
    """Custom type portNextAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PortNextAvailable_Type.__name__ = "Integer32"
_PortNextAvailable_Object = MibScalar
portNextAvailable = _PortNextAvailable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 6),
    _PortNextAvailable_Type()
)
portNextAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNextAvailable.setStatus("current")


class _PortsUsedLine5_Type(Integer32):
    """Custom type portsUsedLine5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_PortsUsedLine5_Type.__name__ = "Integer32"
_PortsUsedLine5_Object = MibScalar
portsUsedLine5 = _PortsUsedLine5_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 7),
    _PortsUsedLine5_Type()
)
portsUsedLine5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsUsedLine5.setStatus("current")


class _PortsUsedLine6_Type(Integer32):
    """Custom type portsUsedLine6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_PortsUsedLine6_Type.__name__ = "Integer32"
_PortsUsedLine6_Object = MibScalar
portsUsedLine6 = _PortsUsedLine6_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 8),
    _PortsUsedLine6_Type()
)
portsUsedLine6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsUsedLine6.setStatus("current")


class _PortsUsedLine7_Type(Integer32):
    """Custom type portsUsedLine7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_PortsUsedLine7_Type.__name__ = "Integer32"
_PortsUsedLine7_Object = MibScalar
portsUsedLine7 = _PortsUsedLine7_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 9),
    _PortsUsedLine7_Type()
)
portsUsedLine7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsUsedLine7.setStatus("current")


class _PortsUsedLine8_Type(Integer32):
    """Custom type portsUsedLine8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_PortsUsedLine8_Type.__name__ = "Integer32"
_PortsUsedLine8_Object = MibScalar
portsUsedLine8 = _PortsUsedLine8_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 10),
    _PortsUsedLine8_Type()
)
portsUsedLine8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsUsedLine8.setStatus("current")
_FrPortsUsedLineGrpTable_Object = MibTable
frPortsUsedLineGrpTable = _FrPortsUsedLineGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    frPortsUsedLineGrpTable.setStatus("current")
_FrPortsUsedLineGrpEntry_Object = MibTableRow
frPortsUsedLineGrpEntry = _FrPortsUsedLineGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 11, 1)
)
frPortsUsedLineGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-PORT-MIB", "frPortsUsedLineIndex"),
)
if mibBuilder.loadTexts:
    frPortsUsedLineGrpEntry.setStatus("current")


class _FrPortsUsedLineIndex_Type(Integer32):
    """Custom type frPortsUsedLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 56),
    )


_FrPortsUsedLineIndex_Type.__name__ = "Integer32"
_FrPortsUsedLineIndex_Object = MibTableColumn
frPortsUsedLineIndex = _FrPortsUsedLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 11, 1, 1),
    _FrPortsUsedLineIndex_Type()
)
frPortsUsedLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPortsUsedLineIndex.setStatus("current")


class _FrPortsUsedLine_Type(Integer32):
    """Custom type frPortsUsedLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrPortsUsedLine_Type.__name__ = "Integer32"
_FrPortsUsedLine_Object = MibTableColumn
frPortsUsedLine = _FrPortsUsedLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 1, 11, 1, 2),
    _FrPortsUsedLine_Type()
)
frPortsUsedLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPortsUsedLine.setStatus("current")
_FrPortServiceQueGrpTable_Object = MibTable
frPortServiceQueGrpTable = _FrPortServiceQueGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    frPortServiceQueGrpTable.setStatus("current")
_FrPortServiceQueGrpEntry_Object = MibTableRow
frPortServiceQueGrpEntry = _FrPortServiceQueGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 4, 1, 1)
)
frPortServiceQueGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-PORT-MIB", "frServPortNum"),
    (0, "CISCO-WAN-FR-PORT-MIB", "portServiceQueueNo"),
)
if mibBuilder.loadTexts:
    frPortServiceQueGrpEntry.setStatus("current")


class _FrServPortNum_Type(Integer32):
    """Custom type frServPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrServPortNum_Type.__name__ = "Integer32"
_FrServPortNum_Object = MibTableColumn
frServPortNum = _FrServPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 4, 1, 1, 1),
    _FrServPortNum_Type()
)
frServPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frServPortNum.setStatus("current")


class _PortServiceQueueNo_Type(Integer32):
    """Custom type portServiceQueueNo based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("highpriorityQ", 1),
          ("nrtVBRandABRQ", 3),
          ("queue5", 5),
          ("queue6", 6),
          ("queue7", 7),
          ("queue8", 8),
          ("rtVBRQ", 2),
          ("uBRQ", 4))
    )


_PortServiceQueueNo_Type.__name__ = "Integer32"
_PortServiceQueueNo_Object = MibTableColumn
portServiceQueueNo = _PortServiceQueueNo_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 4, 1, 1, 2),
    _PortServiceQueueNo_Type()
)
portServiceQueueNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portServiceQueueNo.setStatus("current")


class _PortEgresQDepth_Type(Integer32):
    """Custom type portEgresQDepth based on Integer32"""
    defaultValue = 1048575

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_PortEgresQDepth_Type.__name__ = "Integer32"
_PortEgresQDepth_Object = MibTableColumn
portEgresQDepth = _PortEgresQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 4, 1, 1, 3),
    _PortEgresQDepth_Type()
)
portEgresQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEgresQDepth.setStatus("current")


class _PortEgresECNThresh_Type(Integer32):
    """Custom type portEgresECNThresh based on Integer32"""
    defaultValue = 104857

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_PortEgresECNThresh_Type.__name__ = "Integer32"
_PortEgresECNThresh_Object = MibTableColumn
portEgresECNThresh = _PortEgresECNThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 4, 1, 1, 4),
    _PortEgresECNThresh_Type()
)
portEgresECNThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEgresECNThresh.setStatus("current")


class _PortEgresDEThresh_Type(Integer32):
    """Custom type portEgresDEThresh based on Integer32"""
    defaultValue = 524287

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_PortEgresDEThresh_Type.__name__ = "Integer32"
_PortEgresDEThresh_Object = MibTableColumn
portEgresDEThresh = _PortEgresDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 4, 1, 1, 5),
    _PortEgresDEThresh_Type()
)
portEgresDEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEgresDEThresh.setStatus("current")


class _PortQBwInc_Type(Integer32):
    """Custom type portQBwInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_PortQBwInc_Type.__name__ = "Integer32"
_PortQBwInc_Object = MibTableColumn
portQBwInc = _PortQBwInc_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 4, 1, 1, 6),
    _PortQBwInc_Type()
)
portQBwInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portQBwInc.setStatus("current")
_PortBytesDiscXceedQueFull_Type = Counter32
_PortBytesDiscXceedQueFull_Object = MibTableColumn
portBytesDiscXceedQueFull = _PortBytesDiscXceedQueFull_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 4, 1, 1, 7),
    _PortBytesDiscXceedQueFull_Type()
)
portBytesDiscXceedQueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBytesDiscXceedQueFull.setStatus("current")
if mibBuilder.loadTexts:
    portBytesDiscXceedQueFull.setUnits("Bytes")
_PortBytesDiscXceedDEThresh_Type = Counter32
_PortBytesDiscXceedDEThresh_Object = MibTableColumn
portBytesDiscXceedDEThresh = _PortBytesDiscXceedDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 4, 1, 1, 8),
    _PortBytesDiscXceedDEThresh_Type()
)
portBytesDiscXceedDEThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBytesDiscXceedDEThresh.setStatus("current")
if mibBuilder.loadTexts:
    portBytesDiscXceedDEThresh.setUnits("Bytes")
_FrPortCntPortGrp_ObjectIdentity = ObjectIdentity
frPortCntPortGrp = _FrPortCntPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1)
)
_FrPortCntPortGrpTable_Object = MibTable
frPortCntPortGrpTable = _FrPortCntPortGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    frPortCntPortGrpTable.setStatus("current")
_FrPortCntPortGrpEntry_Object = MibTableRow
frPortCntPortGrpEntry = _FrPortCntPortGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1)
)
frPortCntPortGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-PORT-MIB", "cntPortNum"),
)
if mibBuilder.loadTexts:
    frPortCntPortGrpEntry.setStatus("current")


class _CntPortNum_Type(Integer32):
    """Custom type cntPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CntPortNum_Type.__name__ = "Integer32"
_CntPortNum_Object = MibTableColumn
cntPortNum = _CntPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 1),
    _CntPortNum_Type()
)
cntPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntPortNum.setStatus("current")
_RcvPortFrames_Type = Counter32
_RcvPortFrames_Object = MibTableColumn
rcvPortFrames = _RcvPortFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 2),
    _RcvPortFrames_Type()
)
rcvPortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvPortFrames.setStatus("current")
if mibBuilder.loadTexts:
    rcvPortFrames.setUnits("Frames")
_RcvPortBytes_Type = Counter32
_RcvPortBytes_Object = MibTableColumn
rcvPortBytes = _RcvPortBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 3),
    _RcvPortBytes_Type()
)
rcvPortBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvPortBytes.setStatus("current")
if mibBuilder.loadTexts:
    rcvPortBytes.setUnits("Bytes")
_RcvPortFramesDE_Type = Counter32
_RcvPortFramesDE_Object = MibTableColumn
rcvPortFramesDE = _RcvPortFramesDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 4),
    _RcvPortFramesDE_Type()
)
rcvPortFramesDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvPortFramesDE.setStatus("current")
if mibBuilder.loadTexts:
    rcvPortFramesDE.setUnits("Frames")
_RcvPortFramesFECN_Type = Counter32
_RcvPortFramesFECN_Object = MibTableColumn
rcvPortFramesFECN = _RcvPortFramesFECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 5),
    _RcvPortFramesFECN_Type()
)
rcvPortFramesFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvPortFramesFECN.setStatus("current")
if mibBuilder.loadTexts:
    rcvPortFramesFECN.setUnits("Frames")
_RcvPortFramesBECN_Type = Counter32
_RcvPortFramesBECN_Object = MibTableColumn
rcvPortFramesBECN = _RcvPortFramesBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 6),
    _RcvPortFramesBECN_Type()
)
rcvPortFramesBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvPortFramesBECN.setStatus("current")
if mibBuilder.loadTexts:
    rcvPortFramesBECN.setUnits("Frames")
_RcvFramesDiscCRCError_Type = Counter32
_RcvFramesDiscCRCError_Object = MibTableColumn
rcvFramesDiscCRCError = _RcvFramesDiscCRCError_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 7),
    _RcvFramesDiscCRCError_Type()
)
rcvFramesDiscCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesDiscCRCError.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesDiscCRCError.setUnits("Frames")
_RcvFramesDiscAlignmentError_Type = Counter32
_RcvFramesDiscAlignmentError_Object = MibTableColumn
rcvFramesDiscAlignmentError = _RcvFramesDiscAlignmentError_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 8),
    _RcvFramesDiscAlignmentError_Type()
)
rcvFramesDiscAlignmentError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesDiscAlignmentError.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesDiscAlignmentError.setUnits("Frames")
_RcvFramesDiscIllegalLen_Type = Counter32
_RcvFramesDiscIllegalLen_Object = MibTableColumn
rcvFramesDiscIllegalLen = _RcvFramesDiscIllegalLen_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 9),
    _RcvFramesDiscIllegalLen_Type()
)
rcvFramesDiscIllegalLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesDiscIllegalLen.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesDiscIllegalLen.setUnits("Frames")
_RcvFramesDiscIllegalHeader_Type = Counter32
_RcvFramesDiscIllegalHeader_Object = MibTableColumn
rcvFramesDiscIllegalHeader = _RcvFramesDiscIllegalHeader_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 10),
    _RcvFramesDiscIllegalHeader_Type()
)
rcvFramesDiscIllegalHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesDiscIllegalHeader.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesDiscIllegalHeader.setUnits("Frames")
_RcvFramesAbort_Type = Counter32
_RcvFramesAbort_Object = MibTableColumn
rcvFramesAbort = _RcvFramesAbort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 11),
    _RcvFramesAbort_Type()
)
rcvFramesAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesAbort.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesAbort.setUnits("Frames")
_RcvFramesUnknownDLCI_Type = Counter32
_RcvFramesUnknownDLCI_Object = MibTableColumn
rcvFramesUnknownDLCI = _RcvFramesUnknownDLCI_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 12),
    _RcvFramesUnknownDLCI_Type()
)
rcvFramesUnknownDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesUnknownDLCI.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesUnknownDLCI.setUnits("Frames")
_RcvLastUnknownDLCI_Type = Integer32
_RcvLastUnknownDLCI_Object = MibTableColumn
rcvLastUnknownDLCI = _RcvLastUnknownDLCI_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 13),
    _RcvLastUnknownDLCI_Type()
)
rcvLastUnknownDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvLastUnknownDLCI.setStatus("current")
_RcvPortFramesTaggedFECN_Type = Counter32
_RcvPortFramesTaggedFECN_Object = MibTableColumn
rcvPortFramesTaggedFECN = _RcvPortFramesTaggedFECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 14),
    _RcvPortFramesTaggedFECN_Type()
)
rcvPortFramesTaggedFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvPortFramesTaggedFECN.setStatus("current")
if mibBuilder.loadTexts:
    rcvPortFramesTaggedFECN.setUnits("Frames")
_RcvPortFramesTaggedBECN_Type = Counter32
_RcvPortFramesTaggedBECN_Object = MibTableColumn
rcvPortFramesTaggedBECN = _RcvPortFramesTaggedBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 15),
    _RcvPortFramesTaggedBECN_Type()
)
rcvPortFramesTaggedBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvPortFramesTaggedBECN.setStatus("current")
if mibBuilder.loadTexts:
    rcvPortFramesTaggedBECN.setUnits("Frames")
_RcvPortFramesTaggedDE_Type = Counter32
_RcvPortFramesTaggedDE_Object = MibTableColumn
rcvPortFramesTaggedDE = _RcvPortFramesTaggedDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 16),
    _RcvPortFramesTaggedDE_Type()
)
rcvPortFramesTaggedDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvPortFramesTaggedDE.setStatus("current")
if mibBuilder.loadTexts:
    rcvPortFramesTaggedDE.setUnits("Frames")
_RcvPortFramesDiscXceedDEThresh_Type = Counter32
_RcvPortFramesDiscXceedDEThresh_Object = MibTableColumn
rcvPortFramesDiscXceedDEThresh = _RcvPortFramesDiscXceedDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 17),
    _RcvPortFramesDiscXceedDEThresh_Type()
)
rcvPortFramesDiscXceedDEThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvPortFramesDiscXceedDEThresh.setStatus("current")
if mibBuilder.loadTexts:
    rcvPortFramesDiscXceedDEThresh.setUnits("Frames")
_RcvPortKbpsAIR_Type = Integer32
_RcvPortKbpsAIR_Object = MibTableColumn
rcvPortKbpsAIR = _RcvPortKbpsAIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 18),
    _RcvPortKbpsAIR_Type()
)
rcvPortKbpsAIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvPortKbpsAIR.setStatus("current")
if mibBuilder.loadTexts:
    rcvPortKbpsAIR.setUnits("kbps")
_RcvBufNotAvailable_Type = Counter32
_RcvBufNotAvailable_Object = MibTableColumn
rcvBufNotAvailable = _RcvBufNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 19),
    _RcvBufNotAvailable_Type()
)
rcvBufNotAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvBufNotAvailable.setStatus("current")
_XmtPortFrames_Type = Counter32
_XmtPortFrames_Object = MibTableColumn
xmtPortFrames = _XmtPortFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 20),
    _XmtPortFrames_Type()
)
xmtPortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtPortFrames.setStatus("current")
if mibBuilder.loadTexts:
    xmtPortFrames.setUnits("Frames")
_XmtPortBytes_Type = Counter32
_XmtPortBytes_Object = MibTableColumn
xmtPortBytes = _XmtPortBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 21),
    _XmtPortBytes_Type()
)
xmtPortBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtPortBytes.setStatus("current")
if mibBuilder.loadTexts:
    xmtPortBytes.setUnits("Bytes")
_XmtPortFramesFECN_Type = Counter32
_XmtPortFramesFECN_Object = MibTableColumn
xmtPortFramesFECN = _XmtPortFramesFECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 22),
    _XmtPortFramesFECN_Type()
)
xmtPortFramesFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtPortFramesFECN.setStatus("current")
if mibBuilder.loadTexts:
    xmtPortFramesFECN.setUnits("Frames")
_XmtPortFramesBECN_Type = Counter32
_XmtPortFramesBECN_Object = MibTableColumn
xmtPortFramesBECN = _XmtPortFramesBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 23),
    _XmtPortFramesBECN_Type()
)
xmtPortFramesBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtPortFramesBECN.setStatus("current")
if mibBuilder.loadTexts:
    xmtPortFramesBECN.setUnits("Frames")
_XmtPortFramesDiscXceedQDepth_Type = Counter32
_XmtPortFramesDiscXceedQDepth_Object = MibTableColumn
xmtPortFramesDiscXceedQDepth = _XmtPortFramesDiscXceedQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 24),
    _XmtPortFramesDiscXceedQDepth_Type()
)
xmtPortFramesDiscXceedQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtPortFramesDiscXceedQDepth.setStatus("current")
if mibBuilder.loadTexts:
    xmtPortFramesDiscXceedQDepth.setUnits("Frames")
_XmtPortBytesDiscXceedQDepth_Type = Counter32
_XmtPortBytesDiscXceedQDepth_Object = MibTableColumn
xmtPortBytesDiscXceedQDepth = _XmtPortBytesDiscXceedQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 25),
    _XmtPortBytesDiscXceedQDepth_Type()
)
xmtPortBytesDiscXceedQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtPortBytesDiscXceedQDepth.setStatus("current")
if mibBuilder.loadTexts:
    xmtPortBytesDiscXceedQDepth.setUnits("Bytes")
_XmtPortFramesDuringLMIAlarm_Type = Counter32
_XmtPortFramesDuringLMIAlarm_Object = MibTableColumn
xmtPortFramesDuringLMIAlarm = _XmtPortFramesDuringLMIAlarm_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 26),
    _XmtPortFramesDuringLMIAlarm_Type()
)
xmtPortFramesDuringLMIAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtPortFramesDuringLMIAlarm.setStatus("current")
if mibBuilder.loadTexts:
    xmtPortFramesDuringLMIAlarm.setUnits("Frames")
_XmtPortBytesDuringLMIAlarm_Type = Counter32
_XmtPortBytesDuringLMIAlarm_Object = MibTableColumn
xmtPortBytesDuringLMIAlarm = _XmtPortBytesDuringLMIAlarm_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 27),
    _XmtPortBytesDuringLMIAlarm_Type()
)
xmtPortBytesDuringLMIAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtPortBytesDuringLMIAlarm.setStatus("current")
if mibBuilder.loadTexts:
    xmtPortBytesDuringLMIAlarm.setUnits("Bytes")
_XmtFramesAbort_Type = Counter32
_XmtFramesAbort_Object = MibTableColumn
xmtFramesAbort = _XmtFramesAbort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 28),
    _XmtFramesAbort_Type()
)
xmtFramesAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesAbort.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesAbort.setUnits("Frames")
_XmtFramesUnderrun_Type = Counter32
_XmtFramesUnderrun_Object = MibTableColumn
xmtFramesUnderrun = _XmtFramesUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 29),
    _XmtFramesUnderrun_Type()
)
xmtFramesUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesUnderrun.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesUnderrun.setUnits("Frames")
_XmtPortKbpsAIR_Type = Integer32
_XmtPortKbpsAIR_Object = MibTableColumn
xmtPortKbpsAIR = _XmtPortKbpsAIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 30),
    _XmtPortKbpsAIR_Type()
)
xmtPortKbpsAIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtPortKbpsAIR.setStatus("current")
if mibBuilder.loadTexts:
    xmtPortKbpsAIR.setUnits("Kbps")
_XmtBufNotAvailable_Type = Counter32
_XmtBufNotAvailable_Object = MibTableColumn
xmtBufNotAvailable = _XmtBufNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 31),
    _XmtBufNotAvailable_Type()
)
xmtBufNotAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtBufNotAvailable.setStatus("current")


class _PortClrButton_Type(Integer32):
    """Custom type portClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_PortClrButton_Type.__name__ = "Integer32"
_PortClrButton_Object = MibTableColumn
portClrButton = _PortClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 32),
    _PortClrButton_Type()
)
portClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portClrButton.setStatus("current")
_RcvFramesDiscNoChan_Type = Counter32
_RcvFramesDiscNoChan_Object = MibTableColumn
rcvFramesDiscNoChan = _RcvFramesDiscNoChan_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 33),
    _RcvFramesDiscNoChan_Type()
)
rcvFramesDiscNoChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesDiscNoChan.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesDiscNoChan.setUnits("Frames")
_RcvFramesDiscOverrun_Type = Counter32
_RcvFramesDiscOverrun_Object = MibTableColumn
rcvFramesDiscOverrun = _RcvFramesDiscOverrun_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 34),
    _RcvFramesDiscOverrun_Type()
)
rcvFramesDiscOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesDiscOverrun.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesDiscOverrun.setUnits("Frames")
_RcvPortFramesDiscard_Type = Counter32
_RcvPortFramesDiscard_Object = MibTableColumn
rcvPortFramesDiscard = _RcvPortFramesDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 35),
    _RcvPortFramesDiscard_Type()
)
rcvPortFramesDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvPortFramesDiscard.setStatus("current")
_XmtPortFramesDE_Type = Counter32
_XmtPortFramesDE_Object = MibTableColumn
xmtPortFramesDE = _XmtPortFramesDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 36),
    _XmtPortFramesDE_Type()
)
xmtPortFramesDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtPortFramesDE.setStatus("current")
_XmtPortBytesDE_Type = Counter32
_XmtPortBytesDE_Object = MibTableColumn
xmtPortBytesDE = _XmtPortBytesDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 37),
    _XmtPortBytesDE_Type()
)
xmtPortBytesDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtPortBytesDE.setStatus("current")
_RcvPortBytesDE_Type = Counter32
_RcvPortBytesDE_Object = MibTableColumn
rcvPortBytesDE = _RcvPortBytesDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 38),
    _RcvPortBytesDE_Type()
)
rcvPortBytesDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvPortBytesDE.setStatus("current")
_XmtPortFramesDiscXceedDEThresh_Type = Counter32
_XmtPortFramesDiscXceedDEThresh_Object = MibTableColumn
xmtPortFramesDiscXceedDEThresh = _XmtPortFramesDiscXceedDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 39),
    _XmtPortFramesDiscXceedDEThresh_Type()
)
xmtPortFramesDiscXceedDEThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtPortFramesDiscXceedDEThresh.setStatus("current")
_XmtPortBytesDiscXceedDEThresh_Type = Counter32
_XmtPortBytesDiscXceedDEThresh_Object = MibTableColumn
xmtPortBytesDiscXceedDEThresh = _XmtPortBytesDiscXceedDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 40),
    _XmtPortBytesDiscXceedDEThresh_Type()
)
xmtPortBytesDiscXceedDEThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtPortBytesDiscXceedDEThresh.setStatus("current")
_RcvPortBytesDiscXceedDEThresh_Type = Counter32
_RcvPortBytesDiscXceedDEThresh_Object = MibTableColumn
rcvPortBytesDiscXceedDEThresh = _RcvPortBytesDiscXceedDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 1, 1, 1, 41),
    _RcvPortBytesDiscXceedDEThresh_Type()
)
rcvPortBytesDiscXceedDEThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvPortBytesDiscXceedDEThresh.setStatus("current")
_FrPortStateGrp_ObjectIdentity = ObjectIdentity
frPortStateGrp = _FrPortStateGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 3)
)
_FrPortStateGrpTable_Object = MibTable
frPortStateGrpTable = _FrPortStateGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    frPortStateGrpTable.setStatus("current")
_FrPortStateGrpEntry_Object = MibTableRow
frPortStateGrpEntry = _FrPortStateGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 3, 1, 1)
)
frPortStateGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-PORT-MIB", "statePortNum"),
)
if mibBuilder.loadTexts:
    frPortStateGrpEntry.setStatus("current")


class _StatePortNum_Type(Integer32):
    """Custom type statePortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_StatePortNum_Type.__name__ = "Integer32"
_StatePortNum_Object = MibTableColumn
statePortNum = _StatePortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 3, 1, 1, 1),
    _StatePortNum_Type()
)
statePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statePortNum.setStatus("current")


class _PortState_Type(Integer32):
    """Custom type portState based on Integer32"""
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("failedDueToLine", 4),
          ("failedDueToSignalling", 5),
          ("farEndRemoteLoopback", 8),
          ("inBert", 7),
          ("inactive", 6),
          ("latchCsuFeLoop", 12),
          ("latchDS0DropFeLoop", 9),
          ("latchDS0LineFeLoop", 10),
          ("latchDsuFeLoop", 13),
          ("latchHL96FeLoop", 14),
          ("latchOcuFeLoop", 11),
          ("notConfigured", 1),
          ("remoteLoopback", 3),
          ("v54PolynomialFeLoop", 15))
    )


_PortState_Type.__name__ = "Integer32"
_PortState_Object = MibTableColumn
portState = _PortState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 3, 1, 1, 2),
    _PortState_Type()
)
portState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portState.setStatus("current")


class _PortSignallingState_Type(Integer32):
    """Custom type portSignallingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_PortSignallingState_Type.__name__ = "Integer32"
_PortSignallingState_Object = MibTableColumn
portSignallingState = _PortSignallingState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 3, 1, 1, 3),
    _PortSignallingState_Type()
)
portSignallingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSignallingState.setStatus("current")


class _PortOversubscribed_Type(Integer32):
    """Custom type portOversubscribed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_PortOversubscribed_Type.__name__ = "Integer32"
_PortOversubscribed_Object = MibTableColumn
portOversubscribed = _PortOversubscribed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 3, 1, 1, 4),
    _PortOversubscribed_Type()
)
portOversubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOversubscribed.setStatus("current")


class _PortIngrPercentUtil_Type(Integer32):
    """Custom type portIngrPercentUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PortIngrPercentUtil_Type.__name__ = "Integer32"
_PortIngrPercentUtil_Object = MibTableColumn
portIngrPercentUtil = _PortIngrPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 3, 1, 1, 5),
    _PortIngrPercentUtil_Type()
)
portIngrPercentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIngrPercentUtil.setStatus("current")


class _PortEgrPercentUtil_Type(Integer32):
    """Custom type portEgrPercentUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PortEgrPercentUtil_Type.__name__ = "Integer32"
_PortEgrPercentUtil_Object = MibTableColumn
portEgrPercentUtil = _PortEgrPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 3, 1, 1, 6),
    _PortEgrPercentUtil_Type()
)
portEgrPercentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portEgrPercentUtil.setStatus("current")
_CiscoWanFrPortMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanFrPortMIBConformance = _CiscoWanFrPortMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 44, 2)
)
_CiscoWanFrPortMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanFrPortMIBGroups = _CiscoWanFrPortMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 44, 2, 1)
)
_CiscoWanFrPortMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanFrPortMIBCompliances = _CiscoWanFrPortMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 44, 2, 2)
)

# Managed Objects groups

ciscoWanFrPortConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 44, 2, 1, 1)
)
ciscoWanFrPortConfGroup.setObjects(
      *(("CISCO-WAN-FR-PORT-MIB", "portNum"),
        ("CISCO-WAN-FR-PORT-MIB", "portLineNum"),
        ("CISCO-WAN-FR-PORT-MIB", "portRowStatus"),
        ("CISCO-WAN-FR-PORT-MIB", "portDs0ConfigBitMap"),
        ("CISCO-WAN-FR-PORT-MIB", "portDs0Speed"),
        ("CISCO-WAN-FR-PORT-MIB", "portFlagsBetweenFrames"),
        ("CISCO-WAN-FR-PORT-MIB", "portEqueueServiceRatio"),
        ("CISCO-WAN-FR-PORT-MIB", "portSpeed"),
        ("CISCO-WAN-FR-PORT-MIB", "portAdmin"),
        ("CISCO-WAN-FR-PORT-MIB", "portType"),
        ("CISCO-WAN-FR-PORT-MIB", "portBERTEnable"),
        ("CISCO-WAN-FR-PORT-MIB", "portEnhancedSIW"),
        ("CISCO-WAN-FR-PORT-MIB", "portM32EgrQueueThresh"),
        ("CISCO-WAN-FR-PORT-MIB", "portHeaderLen"),
        ("CISCO-WAN-FR-PORT-MIB", "portFrameChkSumType"),
        ("CISCO-WAN-FR-PORT-MIB", "portFileId"),
        ("CISCO-WAN-FR-PORT-MIB", "portOverSubEnable"))
)
if mibBuilder.loadTexts:
    ciscoWanFrPortConfGroup.setStatus("current")

ciscoWanFrPortSvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 44, 2, 1, 2)
)
ciscoWanFrPortSvcGroup.setObjects(
      *(("CISCO-WAN-FR-PORT-MIB", "portSvcStatus"),
        ("CISCO-WAN-FR-PORT-MIB", "portSvcInUse"),
        ("CISCO-WAN-FR-PORT-MIB", "portSvcShareLcn"),
        ("CISCO-WAN-FR-PORT-MIB", "portSvcLcnLow"),
        ("CISCO-WAN-FR-PORT-MIB", "portSvcLcnHigh"),
        ("CISCO-WAN-FR-PORT-MIB", "portSvcDlciLow"),
        ("CISCO-WAN-FR-PORT-MIB", "portSvcDlciHigh"),
        ("CISCO-WAN-FR-PORT-MIB", "portDeleteSvcs"),
        ("CISCO-WAN-FR-PORT-MIB", "portIngrSvcBandW"),
        ("CISCO-WAN-FR-PORT-MIB", "portEgrSvcBandW"))
)
if mibBuilder.loadTexts:
    ciscoWanFrPortSvcGroup.setStatus("current")

ciscoWanFrPortDs0InDs1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 44, 2, 1, 3)
)
ciscoWanFrPortDs0InDs1Group.setObjects(
      *(("CISCO-WAN-FR-PORT-MIB", "portsUsedLine1"),
        ("CISCO-WAN-FR-PORT-MIB", "portsUsedLine2"),
        ("CISCO-WAN-FR-PORT-MIB", "portsUsedLine3"),
        ("CISCO-WAN-FR-PORT-MIB", "portsUsedLine4"),
        ("CISCO-WAN-FR-PORT-MIB", "portsUsedLine5"),
        ("CISCO-WAN-FR-PORT-MIB", "portsUsedLine6"),
        ("CISCO-WAN-FR-PORT-MIB", "portsUsedLine7"),
        ("CISCO-WAN-FR-PORT-MIB", "portsUsedLine8"),
        ("CISCO-WAN-FR-PORT-MIB", "portNextAvailable"))
)
if mibBuilder.loadTexts:
    ciscoWanFrPortDs0InDs1Group.setStatus("current")

ciscoWanFrPortStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 44, 2, 1, 4)
)
ciscoWanFrPortStateGroup.setObjects(
      *(("CISCO-WAN-FR-PORT-MIB", "statePortNum"),
        ("CISCO-WAN-FR-PORT-MIB", "portState"),
        ("CISCO-WAN-FR-PORT-MIB", "portSignallingState"),
        ("CISCO-WAN-FR-PORT-MIB", "portOversubscribed"),
        ("CISCO-WAN-FR-PORT-MIB", "portIngrPercentUtil"),
        ("CISCO-WAN-FR-PORT-MIB", "portEgrPercentUtil"))
)
if mibBuilder.loadTexts:
    ciscoWanFrPortStateGroup.setStatus("current")

ciscoWanFrPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 44, 2, 1, 5)
)
ciscoWanFrPortStatsGroup.setObjects(
      *(("CISCO-WAN-FR-PORT-MIB", "cntPortNum"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvPortFrames"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvPortBytes"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvPortFramesDE"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvPortFramesFECN"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvPortFramesBECN"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvFramesDiscCRCError"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvFramesDiscAlignmentError"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvFramesDiscIllegalLen"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvFramesDiscIllegalHeader"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvFramesAbort"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvFramesUnknownDLCI"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvLastUnknownDLCI"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvPortFramesTaggedFECN"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvPortFramesTaggedBECN"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvPortFramesTaggedDE"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvPortFramesDiscXceedDEThresh"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvPortKbpsAIR"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvBufNotAvailable"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtPortFrames"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtPortBytes"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtPortFramesFECN"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtPortFramesBECN"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtPortFramesDiscXceedQDepth"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtPortBytesDiscXceedQDepth"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtPortFramesDuringLMIAlarm"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtPortBytesDuringLMIAlarm"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtFramesAbort"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtFramesUnderrun"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtPortKbpsAIR"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtBufNotAvailable"),
        ("CISCO-WAN-FR-PORT-MIB", "portClrButton"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvFramesDiscNoChan"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvFramesDiscOverrun"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvPortFramesDiscard"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtPortFramesDE"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtPortBytesDE"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvPortBytesDE"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtPortFramesDiscXceedDEThresh"),
        ("CISCO-WAN-FR-PORT-MIB", "xmtPortBytesDiscXceedDEThresh"),
        ("CISCO-WAN-FR-PORT-MIB", "rcvPortBytesDiscXceedDEThresh"))
)
if mibBuilder.loadTexts:
    ciscoWanFrPortStatsGroup.setStatus("current")

ciscoWanFrPortServiceQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 44, 2, 1, 6)
)
ciscoWanFrPortServiceQueueGroup.setObjects(
      *(("CISCO-WAN-FR-PORT-MIB", "frServPortNum"),
        ("CISCO-WAN-FR-PORT-MIB", "portServiceQueueNo"),
        ("CISCO-WAN-FR-PORT-MIB", "portEgresQDepth"),
        ("CISCO-WAN-FR-PORT-MIB", "portEgresECNThresh"),
        ("CISCO-WAN-FR-PORT-MIB", "portEgresDEThresh"),
        ("CISCO-WAN-FR-PORT-MIB", "portQBwInc"),
        ("CISCO-WAN-FR-PORT-MIB", "portBytesDiscXceedQueFull"),
        ("CISCO-WAN-FR-PORT-MIB", "portBytesDiscXceedDEThresh"))
)
if mibBuilder.loadTexts:
    ciscoWanFrPortServiceQueueGroup.setStatus("current")

ciscoWanFrPortsUsedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 44, 2, 1, 7)
)
ciscoWanFrPortsUsedGroup.setObjects(
      *(("CISCO-WAN-FR-PORT-MIB", "frPortsUsedLineIndex"),
        ("CISCO-WAN-FR-PORT-MIB", "frPortsUsedLine"))
)
if mibBuilder.loadTexts:
    ciscoWanFrPortsUsedGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanFrPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 44, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoWanFrPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-FR-PORT-MIB",
    **{"frPortCnfPortGrp": frPortCnfPortGrp,
       "frPortCnfPortGrpTable": frPortCnfPortGrpTable,
       "frPortCnfPortGrpEntry": frPortCnfPortGrpEntry,
       "portNum": portNum,
       "portLineNum": portLineNum,
       "portRowStatus": portRowStatus,
       "portDs0ConfigBitMap": portDs0ConfigBitMap,
       "portDs0Speed": portDs0Speed,
       "portFlagsBetweenFrames": portFlagsBetweenFrames,
       "portEqueueServiceRatio": portEqueueServiceRatio,
       "portSpeed": portSpeed,
       "portAdmin": portAdmin,
       "portType": portType,
       "portSvcStatus": portSvcStatus,
       "portSvcInUse": portSvcInUse,
       "portSvcShareLcn": portSvcShareLcn,
       "portSvcLcnLow": portSvcLcnLow,
       "portSvcLcnHigh": portSvcLcnHigh,
       "portSvcDlciLow": portSvcDlciLow,
       "portSvcDlciHigh": portSvcDlciHigh,
       "portDeleteSvcs": portDeleteSvcs,
       "portIngrSvcBandW": portIngrSvcBandW,
       "portEgrSvcBandW": portEgrSvcBandW,
       "portBERTEnable": portBERTEnable,
       "portEnhancedSIW": portEnhancedSIW,
       "portM32EgrQueueThresh": portM32EgrQueueThresh,
       "portHeaderLen": portHeaderLen,
       "portFrameChkSumType": portFrameChkSumType,
       "portFileId": portFileId,
       "portOverSubEnable": portOverSubEnable,
       "portsUsedLine1": portsUsedLine1,
       "portsUsedLine2": portsUsedLine2,
       "portsUsedLine3": portsUsedLine3,
       "portsUsedLine4": portsUsedLine4,
       "portNextAvailable": portNextAvailable,
       "portsUsedLine5": portsUsedLine5,
       "portsUsedLine6": portsUsedLine6,
       "portsUsedLine7": portsUsedLine7,
       "portsUsedLine8": portsUsedLine8,
       "frPortsUsedLineGrpTable": frPortsUsedLineGrpTable,
       "frPortsUsedLineGrpEntry": frPortsUsedLineGrpEntry,
       "frPortsUsedLineIndex": frPortsUsedLineIndex,
       "frPortsUsedLine": frPortsUsedLine,
       "frPortServiceQueGrpTable": frPortServiceQueGrpTable,
       "frPortServiceQueGrpEntry": frPortServiceQueGrpEntry,
       "frServPortNum": frServPortNum,
       "portServiceQueueNo": portServiceQueueNo,
       "portEgresQDepth": portEgresQDepth,
       "portEgresECNThresh": portEgresECNThresh,
       "portEgresDEThresh": portEgresDEThresh,
       "portQBwInc": portQBwInc,
       "portBytesDiscXceedQueFull": portBytesDiscXceedQueFull,
       "portBytesDiscXceedDEThresh": portBytesDiscXceedDEThresh,
       "frPortCntPortGrp": frPortCntPortGrp,
       "frPortCntPortGrpTable": frPortCntPortGrpTable,
       "frPortCntPortGrpEntry": frPortCntPortGrpEntry,
       "cntPortNum": cntPortNum,
       "rcvPortFrames": rcvPortFrames,
       "rcvPortBytes": rcvPortBytes,
       "rcvPortFramesDE": rcvPortFramesDE,
       "rcvPortFramesFECN": rcvPortFramesFECN,
       "rcvPortFramesBECN": rcvPortFramesBECN,
       "rcvFramesDiscCRCError": rcvFramesDiscCRCError,
       "rcvFramesDiscAlignmentError": rcvFramesDiscAlignmentError,
       "rcvFramesDiscIllegalLen": rcvFramesDiscIllegalLen,
       "rcvFramesDiscIllegalHeader": rcvFramesDiscIllegalHeader,
       "rcvFramesAbort": rcvFramesAbort,
       "rcvFramesUnknownDLCI": rcvFramesUnknownDLCI,
       "rcvLastUnknownDLCI": rcvLastUnknownDLCI,
       "rcvPortFramesTaggedFECN": rcvPortFramesTaggedFECN,
       "rcvPortFramesTaggedBECN": rcvPortFramesTaggedBECN,
       "rcvPortFramesTaggedDE": rcvPortFramesTaggedDE,
       "rcvPortFramesDiscXceedDEThresh": rcvPortFramesDiscXceedDEThresh,
       "rcvPortKbpsAIR": rcvPortKbpsAIR,
       "rcvBufNotAvailable": rcvBufNotAvailable,
       "xmtPortFrames": xmtPortFrames,
       "xmtPortBytes": xmtPortBytes,
       "xmtPortFramesFECN": xmtPortFramesFECN,
       "xmtPortFramesBECN": xmtPortFramesBECN,
       "xmtPortFramesDiscXceedQDepth": xmtPortFramesDiscXceedQDepth,
       "xmtPortBytesDiscXceedQDepth": xmtPortBytesDiscXceedQDepth,
       "xmtPortFramesDuringLMIAlarm": xmtPortFramesDuringLMIAlarm,
       "xmtPortBytesDuringLMIAlarm": xmtPortBytesDuringLMIAlarm,
       "xmtFramesAbort": xmtFramesAbort,
       "xmtFramesUnderrun": xmtFramesUnderrun,
       "xmtPortKbpsAIR": xmtPortKbpsAIR,
       "xmtBufNotAvailable": xmtBufNotAvailable,
       "portClrButton": portClrButton,
       "rcvFramesDiscNoChan": rcvFramesDiscNoChan,
       "rcvFramesDiscOverrun": rcvFramesDiscOverrun,
       "rcvPortFramesDiscard": rcvPortFramesDiscard,
       "xmtPortFramesDE": xmtPortFramesDE,
       "xmtPortBytesDE": xmtPortBytesDE,
       "rcvPortBytesDE": rcvPortBytesDE,
       "xmtPortFramesDiscXceedDEThresh": xmtPortFramesDiscXceedDEThresh,
       "xmtPortBytesDiscXceedDEThresh": xmtPortBytesDiscXceedDEThresh,
       "rcvPortBytesDiscXceedDEThresh": rcvPortBytesDiscXceedDEThresh,
       "frPortStateGrp": frPortStateGrp,
       "frPortStateGrpTable": frPortStateGrpTable,
       "frPortStateGrpEntry": frPortStateGrpEntry,
       "statePortNum": statePortNum,
       "portState": portState,
       "portSignallingState": portSignallingState,
       "portOversubscribed": portOversubscribed,
       "portIngrPercentUtil": portIngrPercentUtil,
       "portEgrPercentUtil": portEgrPercentUtil,
       "ciscoWanFrPortMIB": ciscoWanFrPortMIB,
       "ciscoWanFrPortMIBConformance": ciscoWanFrPortMIBConformance,
       "ciscoWanFrPortMIBGroups": ciscoWanFrPortMIBGroups,
       "ciscoWanFrPortConfGroup": ciscoWanFrPortConfGroup,
       "ciscoWanFrPortSvcGroup": ciscoWanFrPortSvcGroup,
       "ciscoWanFrPortDs0InDs1Group": ciscoWanFrPortDs0InDs1Group,
       "ciscoWanFrPortStateGroup": ciscoWanFrPortStateGroup,
       "ciscoWanFrPortStatsGroup": ciscoWanFrPortStatsGroup,
       "ciscoWanFrPortServiceQueueGroup": ciscoWanFrPortServiceQueueGroup,
       "ciscoWanFrPortsUsedGroup": ciscoWanFrPortsUsedGroup,
       "ciscoWanFrPortMIBCompliances": ciscoWanFrPortMIBCompliances,
       "ciscoWanFrPortCompliance": ciscoWanFrPortCompliance}
)
