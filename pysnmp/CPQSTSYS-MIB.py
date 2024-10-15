# SNMP MIB module (CPQSTSYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQSTSYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:22 2024
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqSsStorageSys_ObjectIdentity = ObjectIdentity
cpqSsStorageSys = _CpqSsStorageSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 8)
)
_CpqSsMibRev_ObjectIdentity = ObjectIdentity
cpqSsMibRev = _CpqSsMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 8, 1)
)


class _CpqSsMibRevMajor_Type(Integer32):
    """Custom type cpqSsMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqSsMibRevMajor_Type.__name__ = "Integer32"
_CpqSsMibRevMajor_Object = MibScalar
cpqSsMibRevMajor = _CpqSsMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 1, 1),
    _CpqSsMibRevMajor_Type()
)
cpqSsMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsMibRevMajor.setStatus("mandatory")


class _CpqSsMibRevMinor_Type(Integer32):
    """Custom type cpqSsMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSsMibRevMinor_Type.__name__ = "Integer32"
_CpqSsMibRevMinor_Object = MibScalar
cpqSsMibRevMinor = _CpqSsMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 1, 2),
    _CpqSsMibRevMinor_Type()
)
cpqSsMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsMibRevMinor.setStatus("mandatory")


class _CpqSsMibCondition_Type(Integer32):
    """Custom type cpqSsMibCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsMibCondition_Type.__name__ = "Integer32"
_CpqSsMibCondition_Object = MibScalar
cpqSsMibCondition = _CpqSsMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 1, 3),
    _CpqSsMibCondition_Type()
)
cpqSsMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsMibCondition.setStatus("mandatory")
_CpqSsDrvBox_ObjectIdentity = ObjectIdentity
cpqSsDrvBox = _CpqSsDrvBox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 8, 2)
)
_CpqSsDrvBoxTable_Object = MibTable
cpqSsDrvBoxTable = _CpqSsDrvBoxTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1)
)
if mibBuilder.loadTexts:
    cpqSsDrvBoxTable.setStatus("mandatory")
_CpqSsDrvBoxEntry_Object = MibTableRow
cpqSsDrvBoxEntry = _CpqSsDrvBoxEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1)
)
cpqSsDrvBoxEntry.setIndexNames(
    (0, "CPQSTSYS-MIB", "cpqSsBoxCntlrIndex"),
    (0, "CPQSTSYS-MIB", "cpqSsBoxBusIndex"),
)
if mibBuilder.loadTexts:
    cpqSsDrvBoxEntry.setStatus("mandatory")
_CpqSsBoxCntlrIndex_Type = Integer32
_CpqSsBoxCntlrIndex_Object = MibTableColumn
cpqSsBoxCntlrIndex = _CpqSsBoxCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 1),
    _CpqSsBoxCntlrIndex_Type()
)
cpqSsBoxCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxCntlrIndex.setStatus("mandatory")


class _CpqSsBoxBusIndex_Type(Integer32):
    """Custom type cpqSsBoxBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSsBoxBusIndex_Type.__name__ = "Integer32"
_CpqSsBoxBusIndex_Object = MibTableColumn
cpqSsBoxBusIndex = _CpqSsBoxBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 2),
    _CpqSsBoxBusIndex_Type()
)
cpqSsBoxBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxBusIndex.setStatus("mandatory")


class _CpqSsBoxType_Type(Integer32):
    """Custom type cpqSsBoxType based on Integer32"""
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
        *(("other", 1),
          ("proLiant", 2),
          ("proLiant2", 3),
          ("proLiant2DuplexBottom", 6),
          ("proLiant2DuplexTop", 5),
          ("proLiant2Internal", 4),
          ("proLiant2InternalDuplexBottom", 8),
          ("proLiant2InternalDuplexTop", 7))
    )


_CpqSsBoxType_Type.__name__ = "Integer32"
_CpqSsBoxType_Object = MibTableColumn
cpqSsBoxType = _CpqSsBoxType_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 3),
    _CpqSsBoxType_Type()
)
cpqSsBoxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxType.setStatus("deprecated")


class _CpqSsBoxModel_Type(DisplayString):
    """Custom type cpqSsBoxModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CpqSsBoxModel_Type.__name__ = "DisplayString"
_CpqSsBoxModel_Object = MibTableColumn
cpqSsBoxModel = _CpqSsBoxModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 4),
    _CpqSsBoxModel_Type()
)
cpqSsBoxModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxModel.setStatus("mandatory")


class _CpqSsBoxFWRev_Type(DisplayString):
    """Custom type cpqSsBoxFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqSsBoxFWRev_Type.__name__ = "DisplayString"
_CpqSsBoxFWRev_Object = MibTableColumn
cpqSsBoxFWRev = _CpqSsBoxFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 5),
    _CpqSsBoxFWRev_Type()
)
cpqSsBoxFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxFWRev.setStatus("mandatory")


class _CpqSsBoxVendor_Type(DisplayString):
    """Custom type cpqSsBoxVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CpqSsBoxVendor_Type.__name__ = "DisplayString"
_CpqSsBoxVendor_Object = MibTableColumn
cpqSsBoxVendor = _CpqSsBoxVendor_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 6),
    _CpqSsBoxVendor_Type()
)
cpqSsBoxVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxVendor.setStatus("mandatory")


class _CpqSsBoxFanStatus_Type(Integer32):
    """Custom type cpqSsBoxFanStatus based on Integer32"""
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
        *(("degraded", 5),
          ("failed", 3),
          ("noFan", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsBoxFanStatus_Type.__name__ = "Integer32"
_CpqSsBoxFanStatus_Object = MibTableColumn
cpqSsBoxFanStatus = _CpqSsBoxFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 7),
    _CpqSsBoxFanStatus_Type()
)
cpqSsBoxFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxFanStatus.setStatus("mandatory")


class _CpqSsBoxCondition_Type(Integer32):
    """Custom type cpqSsBoxCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsBoxCondition_Type.__name__ = "Integer32"
_CpqSsBoxCondition_Object = MibTableColumn
cpqSsBoxCondition = _CpqSsBoxCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 8),
    _CpqSsBoxCondition_Type()
)
cpqSsBoxCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxCondition.setStatus("mandatory")


class _CpqSsBoxTempStatus_Type(Integer32):
    """Custom type cpqSsBoxTempStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("noTemp", 5),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsBoxTempStatus_Type.__name__ = "Integer32"
_CpqSsBoxTempStatus_Object = MibTableColumn
cpqSsBoxTempStatus = _CpqSsBoxTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 9),
    _CpqSsBoxTempStatus_Type()
)
cpqSsBoxTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxTempStatus.setStatus("mandatory")


class _CpqSsBoxSidePanelStatus_Type(Integer32):
    """Custom type cpqSsBoxSidePanelStatus based on Integer32"""
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
        *(("noSidePanelStatus", 4),
          ("other", 1),
          ("sidePanelInPlace", 2),
          ("sidePanelRemoved", 3))
    )


_CpqSsBoxSidePanelStatus_Type.__name__ = "Integer32"
_CpqSsBoxSidePanelStatus_Object = MibTableColumn
cpqSsBoxSidePanelStatus = _CpqSsBoxSidePanelStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 10),
    _CpqSsBoxSidePanelStatus_Type()
)
cpqSsBoxSidePanelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxSidePanelStatus.setStatus("mandatory")


class _CpqSsBoxFltTolPwrSupplyStatus_Type(Integer32):
    """Custom type cpqSsBoxFltTolPwrSupplyStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("noFltTolPower", 5),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsBoxFltTolPwrSupplyStatus_Type.__name__ = "Integer32"
_CpqSsBoxFltTolPwrSupplyStatus_Object = MibTableColumn
cpqSsBoxFltTolPwrSupplyStatus = _CpqSsBoxFltTolPwrSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 11),
    _CpqSsBoxFltTolPwrSupplyStatus_Type()
)
cpqSsBoxFltTolPwrSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxFltTolPwrSupplyStatus.setStatus("mandatory")


class _CpqSsBoxBackPlaneVersion_Type(Integer32):
    """Custom type cpqSsBoxBackPlaneVersion based on Integer32"""
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
        *(("other", 1),
          ("proLiant", 2),
          ("proLiant2", 3),
          ("proLiant3", 4),
          ("proLiant4", 5),
          ("proLiant5", 6))
    )


_CpqSsBoxBackPlaneVersion_Type.__name__ = "Integer32"
_CpqSsBoxBackPlaneVersion_Object = MibTableColumn
cpqSsBoxBackPlaneVersion = _CpqSsBoxBackPlaneVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 12),
    _CpqSsBoxBackPlaneVersion_Type()
)
cpqSsBoxBackPlaneVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxBackPlaneVersion.setStatus("mandatory")
_CpqSsBoxTotalBays_Type = Integer32
_CpqSsBoxTotalBays_Object = MibTableColumn
cpqSsBoxTotalBays = _CpqSsBoxTotalBays_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 13),
    _CpqSsBoxTotalBays_Type()
)
cpqSsBoxTotalBays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxTotalBays.setStatus("mandatory")


class _CpqSsBoxPlacement_Type(Integer32):
    """Custom type cpqSsBoxPlacement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("other", 1))
    )


_CpqSsBoxPlacement_Type.__name__ = "Integer32"
_CpqSsBoxPlacement_Object = MibTableColumn
cpqSsBoxPlacement = _CpqSsBoxPlacement_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 14),
    _CpqSsBoxPlacement_Type()
)
cpqSsBoxPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxPlacement.setStatus("mandatory")


class _CpqSsBoxDuplexOption_Type(Integer32):
    """Custom type cpqSsBoxDuplexOption based on Integer32"""
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
        *(("duplexBottom", 4),
          ("duplexTop", 3),
          ("notDuplexed", 2),
          ("other", 1))
    )


_CpqSsBoxDuplexOption_Type.__name__ = "Integer32"
_CpqSsBoxDuplexOption_Object = MibTableColumn
cpqSsBoxDuplexOption = _CpqSsBoxDuplexOption_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 15),
    _CpqSsBoxDuplexOption_Type()
)
cpqSsBoxDuplexOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxDuplexOption.setStatus("mandatory")
_CpqSsBoxBoardRevision_Type = Integer32
_CpqSsBoxBoardRevision_Object = MibTableColumn
cpqSsBoxBoardRevision = _CpqSsBoxBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 16),
    _CpqSsBoxBoardRevision_Type()
)
cpqSsBoxBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxBoardRevision.setStatus("mandatory")


class _CpqSsBoxSerialNumber_Type(DisplayString):
    """Custom type cpqSsBoxSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSsBoxSerialNumber_Type.__name__ = "DisplayString"
_CpqSsBoxSerialNumber_Object = MibTableColumn
cpqSsBoxSerialNumber = _CpqSsBoxSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 17),
    _CpqSsBoxSerialNumber_Type()
)
cpqSsBoxSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxSerialNumber.setStatus("mandatory")


class _CpqSsBoxCntlrHwLocation_Type(DisplayString):
    """Custom type cpqSsBoxCntlrHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSsBoxCntlrHwLocation_Type.__name__ = "DisplayString"
_CpqSsBoxCntlrHwLocation_Object = MibTableColumn
cpqSsBoxCntlrHwLocation = _CpqSsBoxCntlrHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 18),
    _CpqSsBoxCntlrHwLocation_Type()
)
cpqSsBoxCntlrHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxCntlrHwLocation.setStatus("mandatory")


class _CpqSsBoxBackplaneSpeed_Type(Integer32):
    """Custom type cpqSsBoxBackplaneSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ultra3", 2),
          ("ultra320", 3))
    )


_CpqSsBoxBackplaneSpeed_Type.__name__ = "Integer32"
_CpqSsBoxBackplaneSpeed_Object = MibTableColumn
cpqSsBoxBackplaneSpeed = _CpqSsBoxBackplaneSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 19),
    _CpqSsBoxBackplaneSpeed_Type()
)
cpqSsBoxBackplaneSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxBackplaneSpeed.setStatus("mandatory")


class _CpqSsBoxConnectionType_Type(Integer32):
    """Custom type cpqSsBoxConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("sasAttached", 3),
          ("scsiAttached", 2))
    )


_CpqSsBoxConnectionType_Type.__name__ = "Integer32"
_CpqSsBoxConnectionType_Object = MibTableColumn
cpqSsBoxConnectionType = _CpqSsBoxConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 20),
    _CpqSsBoxConnectionType_Type()
)
cpqSsBoxConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxConnectionType.setStatus("mandatory")


class _CpqSsBoxHostConnector_Type(DisplayString):
    """Custom type cpqSsBoxHostConnector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CpqSsBoxHostConnector_Type.__name__ = "DisplayString"
_CpqSsBoxHostConnector_Object = MibTableColumn
cpqSsBoxHostConnector = _CpqSsBoxHostConnector_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 21),
    _CpqSsBoxHostConnector_Type()
)
cpqSsBoxHostConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxHostConnector.setStatus("mandatory")
_CpqSsBoxBoxOnConnector_Type = Integer32
_CpqSsBoxBoxOnConnector_Object = MibTableColumn
cpqSsBoxBoxOnConnector = _CpqSsBoxBoxOnConnector_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 22),
    _CpqSsBoxBoxOnConnector_Type()
)
cpqSsBoxBoxOnConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxBoxOnConnector.setStatus("mandatory")


class _CpqSsBoxLocationString_Type(DisplayString):
    """Custom type cpqSsBoxLocationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSsBoxLocationString_Type.__name__ = "DisplayString"
_CpqSsBoxLocationString_Object = MibTableColumn
cpqSsBoxLocationString = _CpqSsBoxLocationString_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 1, 1, 23),
    _CpqSsBoxLocationString_Type()
)
cpqSsBoxLocationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBoxLocationString.setStatus("mandatory")
_CpqSsBoxExtended_ObjectIdentity = ObjectIdentity
cpqSsBoxExtended = _CpqSsBoxExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2)
)
_CpqSsChassisTable_Object = MibTable
cpqSsChassisTable = _CpqSsChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpqSsChassisTable.setStatus("mandatory")
_CpqSsChassisEntry_Object = MibTableRow
cpqSsChassisEntry = _CpqSsChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1)
)
cpqSsChassisEntry.setIndexNames(
    (0, "CPQSTSYS-MIB", "cpqSsChassisIndex"),
)
if mibBuilder.loadTexts:
    cpqSsChassisEntry.setStatus("mandatory")


class _CpqSsChassisIndex_Type(Integer32):
    """Custom type cpqSsChassisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSsChassisIndex_Type.__name__ = "Integer32"
_CpqSsChassisIndex_Object = MibTableColumn
cpqSsChassisIndex = _CpqSsChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 1),
    _CpqSsChassisIndex_Type()
)
cpqSsChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisIndex.setStatus("mandatory")


class _CpqSsChassisConnectionType_Type(Integer32):
    """Custom type cpqSsChassisConnectionType based on Integer32"""
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
        *(("fibreAttached", 2),
          ("iScsiAttached", 4),
          ("other", 1),
          ("sasAttached", 5),
          ("scsiAttached", 3))
    )


_CpqSsChassisConnectionType_Type.__name__ = "Integer32"
_CpqSsChassisConnectionType_Object = MibTableColumn
cpqSsChassisConnectionType = _CpqSsChassisConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 2),
    _CpqSsChassisConnectionType_Type()
)
cpqSsChassisConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisConnectionType.setStatus("mandatory")


class _CpqSsChassisSerialNumber_Type(DisplayString):
    """Custom type cpqSsChassisSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqSsChassisSerialNumber_Type.__name__ = "DisplayString"
_CpqSsChassisSerialNumber_Object = MibTableColumn
cpqSsChassisSerialNumber = _CpqSsChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 3),
    _CpqSsChassisSerialNumber_Type()
)
cpqSsChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisSerialNumber.setStatus("mandatory")


class _CpqSsChassisName_Type(DisplayString):
    """Custom type cpqSsChassisName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqSsChassisName_Type.__name__ = "DisplayString"
_CpqSsChassisName_Object = MibTableColumn
cpqSsChassisName = _CpqSsChassisName_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 4),
    _CpqSsChassisName_Type()
)
cpqSsChassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisName.setStatus("mandatory")


class _CpqSsChassisSystemBoardSerNum_Type(DisplayString):
    """Custom type cpqSsChassisSystemBoardSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSsChassisSystemBoardSerNum_Type.__name__ = "DisplayString"
_CpqSsChassisSystemBoardSerNum_Object = MibTableColumn
cpqSsChassisSystemBoardSerNum = _CpqSsChassisSystemBoardSerNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 5),
    _CpqSsChassisSystemBoardSerNum_Type()
)
cpqSsChassisSystemBoardSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisSystemBoardSerNum.setStatus("mandatory")


class _CpqSsChassisSystemBoardRev_Type(DisplayString):
    """Custom type cpqSsChassisSystemBoardRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqSsChassisSystemBoardRev_Type.__name__ = "DisplayString"
_CpqSsChassisSystemBoardRev_Object = MibTableColumn
cpqSsChassisSystemBoardRev = _CpqSsChassisSystemBoardRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 6),
    _CpqSsChassisSystemBoardRev_Type()
)
cpqSsChassisSystemBoardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisSystemBoardRev.setStatus("mandatory")


class _CpqSsChassisPowerBoardSerNum_Type(DisplayString):
    """Custom type cpqSsChassisPowerBoardSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSsChassisPowerBoardSerNum_Type.__name__ = "DisplayString"
_CpqSsChassisPowerBoardSerNum_Object = MibTableColumn
cpqSsChassisPowerBoardSerNum = _CpqSsChassisPowerBoardSerNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 7),
    _CpqSsChassisPowerBoardSerNum_Type()
)
cpqSsChassisPowerBoardSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisPowerBoardSerNum.setStatus("mandatory")


class _CpqSsChassisPowerBoardRev_Type(DisplayString):
    """Custom type cpqSsChassisPowerBoardRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqSsChassisPowerBoardRev_Type.__name__ = "DisplayString"
_CpqSsChassisPowerBoardRev_Object = MibTableColumn
cpqSsChassisPowerBoardRev = _CpqSsChassisPowerBoardRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 8),
    _CpqSsChassisPowerBoardRev_Type()
)
cpqSsChassisPowerBoardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisPowerBoardRev.setStatus("mandatory")


class _CpqSsChassisScsiBoardSerNum_Type(DisplayString):
    """Custom type cpqSsChassisScsiBoardSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSsChassisScsiBoardSerNum_Type.__name__ = "DisplayString"
_CpqSsChassisScsiBoardSerNum_Object = MibTableColumn
cpqSsChassisScsiBoardSerNum = _CpqSsChassisScsiBoardSerNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 9),
    _CpqSsChassisScsiBoardSerNum_Type()
)
cpqSsChassisScsiBoardSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisScsiBoardSerNum.setStatus("mandatory")


class _CpqSsChassisScsiBoardRev_Type(DisplayString):
    """Custom type cpqSsChassisScsiBoardRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqSsChassisScsiBoardRev_Type.__name__ = "DisplayString"
_CpqSsChassisScsiBoardRev_Object = MibTableColumn
cpqSsChassisScsiBoardRev = _CpqSsChassisScsiBoardRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 10),
    _CpqSsChassisScsiBoardRev_Type()
)
cpqSsChassisScsiBoardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisScsiBoardRev.setStatus("mandatory")


class _CpqSsChassisOverallCondition_Type(Integer32):
    """Custom type cpqSsChassisOverallCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsChassisOverallCondition_Type.__name__ = "Integer32"
_CpqSsChassisOverallCondition_Object = MibTableColumn
cpqSsChassisOverallCondition = _CpqSsChassisOverallCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 11),
    _CpqSsChassisOverallCondition_Type()
)
cpqSsChassisOverallCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisOverallCondition.setStatus("mandatory")


class _CpqSsChassisPowerSupplyCondition_Type(Integer32):
    """Custom type cpqSsChassisPowerSupplyCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsChassisPowerSupplyCondition_Type.__name__ = "Integer32"
_CpqSsChassisPowerSupplyCondition_Object = MibTableColumn
cpqSsChassisPowerSupplyCondition = _CpqSsChassisPowerSupplyCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 12),
    _CpqSsChassisPowerSupplyCondition_Type()
)
cpqSsChassisPowerSupplyCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisPowerSupplyCondition.setStatus("mandatory")


class _CpqSsChassisFanCondition_Type(Integer32):
    """Custom type cpqSsChassisFanCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsChassisFanCondition_Type.__name__ = "Integer32"
_CpqSsChassisFanCondition_Object = MibTableColumn
cpqSsChassisFanCondition = _CpqSsChassisFanCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 13),
    _CpqSsChassisFanCondition_Type()
)
cpqSsChassisFanCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisFanCondition.setStatus("mandatory")


class _CpqSsChassisTemperatureCondition_Type(Integer32):
    """Custom type cpqSsChassisTemperatureCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsChassisTemperatureCondition_Type.__name__ = "Integer32"
_CpqSsChassisTemperatureCondition_Object = MibTableColumn
cpqSsChassisTemperatureCondition = _CpqSsChassisTemperatureCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 14),
    _CpqSsChassisTemperatureCondition_Type()
)
cpqSsChassisTemperatureCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisTemperatureCondition.setStatus("mandatory")


class _CpqSsChassisFcaCntlrCondition_Type(Integer32):
    """Custom type cpqSsChassisFcaCntlrCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsChassisFcaCntlrCondition_Type.__name__ = "Integer32"
_CpqSsChassisFcaCntlrCondition_Object = MibTableColumn
cpqSsChassisFcaCntlrCondition = _CpqSsChassisFcaCntlrCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 15),
    _CpqSsChassisFcaCntlrCondition_Type()
)
cpqSsChassisFcaCntlrCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisFcaCntlrCondition.setStatus("mandatory")


class _CpqSsChassisFcaLogicalDriveCondition_Type(Integer32):
    """Custom type cpqSsChassisFcaLogicalDriveCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsChassisFcaLogicalDriveCondition_Type.__name__ = "Integer32"
_CpqSsChassisFcaLogicalDriveCondition_Object = MibTableColumn
cpqSsChassisFcaLogicalDriveCondition = _CpqSsChassisFcaLogicalDriveCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 16),
    _CpqSsChassisFcaLogicalDriveCondition_Type()
)
cpqSsChassisFcaLogicalDriveCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisFcaLogicalDriveCondition.setStatus("mandatory")


class _CpqSsChassisFcaPhysDrvCondition_Type(Integer32):
    """Custom type cpqSsChassisFcaPhysDrvCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsChassisFcaPhysDrvCondition_Type.__name__ = "Integer32"
_CpqSsChassisFcaPhysDrvCondition_Object = MibTableColumn
cpqSsChassisFcaPhysDrvCondition = _CpqSsChassisFcaPhysDrvCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 17),
    _CpqSsChassisFcaPhysDrvCondition_Type()
)
cpqSsChassisFcaPhysDrvCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisFcaPhysDrvCondition.setStatus("mandatory")
_CpqSsChassisTime_Type = Integer32
_CpqSsChassisTime_Object = MibTableColumn
cpqSsChassisTime = _CpqSsChassisTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 18),
    _CpqSsChassisTime_Type()
)
cpqSsChassisTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisTime.setStatus("mandatory")


class _CpqSsChassisModel_Type(Integer32):
    """Custom type cpqSsChassisModel based on Integer32"""
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
        *(("enterpriseModularArray", 5),
          ("enterpriseVirtualArray", 6),
          ("msa1000", 3),
          ("msa1500cs", 9),
          ("msa1510i", 10),
          ("msa20", 8),
          ("msa500G2", 7),
          ("other", 1),
          ("ra4x00", 2),
          ("smartArrayClusterStorage", 4))
    )


_CpqSsChassisModel_Type.__name__ = "Integer32"
_CpqSsChassisModel_Object = MibTableColumn
cpqSsChassisModel = _CpqSsChassisModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 19),
    _CpqSsChassisModel_Type()
)
cpqSsChassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisModel.setStatus("mandatory")


class _CpqSsChassisBackplaneCondition_Type(Integer32):
    """Custom type cpqSsChassisBackplaneCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsChassisBackplaneCondition_Type.__name__ = "Integer32"
_CpqSsChassisBackplaneCondition_Object = MibTableColumn
cpqSsChassisBackplaneCondition = _CpqSsChassisBackplaneCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 20),
    _CpqSsChassisBackplaneCondition_Type()
)
cpqSsChassisBackplaneCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisBackplaneCondition.setStatus("mandatory")


class _CpqSsChassisFcaTapeDrvCondition_Type(Integer32):
    """Custom type cpqSsChassisFcaTapeDrvCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsChassisFcaTapeDrvCondition_Type.__name__ = "Integer32"
_CpqSsChassisFcaTapeDrvCondition_Object = MibTableColumn
cpqSsChassisFcaTapeDrvCondition = _CpqSsChassisFcaTapeDrvCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 21),
    _CpqSsChassisFcaTapeDrvCondition_Type()
)
cpqSsChassisFcaTapeDrvCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisFcaTapeDrvCondition.setStatus("mandatory")


class _CpqSsChassisRsoStatus_Type(Integer32):
    """Custom type cpqSsChassisRsoStatus based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("daemonDownActive", 7),
          ("daemonDownDisabled", 5),
          ("daemonDownLinkDown", 11),
          ("daemonDownNoSecondary", 9),
          ("disabled", 4),
          ("evTimeoutError", 14),
          ("linkDown", 10),
          ("noSecondary", 8),
          ("notConfigured", 3),
          ("notSupported", 2),
          ("ok", 6),
          ("other", 1),
          ("secondaryRunningAuto", 12),
          ("secondaryRunningUser", 13))
    )


_CpqSsChassisRsoStatus_Type.__name__ = "Integer32"
_CpqSsChassisRsoStatus_Object = MibTableColumn
cpqSsChassisRsoStatus = _CpqSsChassisRsoStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 22),
    _CpqSsChassisRsoStatus_Type()
)
cpqSsChassisRsoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisRsoStatus.setStatus("mandatory")


class _CpqSsChassisRsoCondition_Type(Integer32):
    """Custom type cpqSsChassisRsoCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsChassisRsoCondition_Type.__name__ = "Integer32"
_CpqSsChassisRsoCondition_Object = MibTableColumn
cpqSsChassisRsoCondition = _CpqSsChassisRsoCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 23),
    _CpqSsChassisRsoCondition_Type()
)
cpqSsChassisRsoCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisRsoCondition.setStatus("mandatory")


class _CpqSsChassisScsiIoModuleType_Type(Integer32):
    """Custom type cpqSsChassisScsiIoModuleType based on Integer32"""
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
        *(("io1port320", 7),
          ("io2port", 2),
          ("io2port320", 5),
          ("io4port", 4),
          ("io4port320", 6),
          ("io4portUpgradeFirmware", 3),
          ("other", 1))
    )


_CpqSsChassisScsiIoModuleType_Type.__name__ = "Integer32"
_CpqSsChassisScsiIoModuleType_Object = MibTableColumn
cpqSsChassisScsiIoModuleType = _CpqSsChassisScsiIoModuleType_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 24),
    _CpqSsChassisScsiIoModuleType_Type()
)
cpqSsChassisScsiIoModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisScsiIoModuleType.setStatus("mandatory")


class _CpqSsChassisPreferredPathMode_Type(Integer32):
    """Custom type cpqSsChassisPreferredPathMode based on Integer32"""
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
        *(("automatic", 3),
          ("manual", 4),
          ("notActiveActive", 2),
          ("other", 1))
    )


_CpqSsChassisPreferredPathMode_Type.__name__ = "Integer32"
_CpqSsChassisPreferredPathMode_Object = MibTableColumn
cpqSsChassisPreferredPathMode = _CpqSsChassisPreferredPathMode_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 25),
    _CpqSsChassisPreferredPathMode_Type()
)
cpqSsChassisPreferredPathMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisPreferredPathMode.setStatus("mandatory")


class _CpqSsChassisProductId_Type(DisplayString):
    """Custom type cpqSsChassisProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqSsChassisProductId_Type.__name__ = "DisplayString"
_CpqSsChassisProductId_Object = MibTableColumn
cpqSsChassisProductId = _CpqSsChassisProductId_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 1, 1, 26),
    _CpqSsChassisProductId_Type()
)
cpqSsChassisProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsChassisProductId.setStatus("mandatory")
_CpqSsIoSlotTable_Object = MibTable
cpqSsIoSlotTable = _CpqSsIoSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cpqSsIoSlotTable.setStatus("mandatory")
_CpqSsIoSlotEntry_Object = MibTableRow
cpqSsIoSlotEntry = _CpqSsIoSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 2, 1)
)
cpqSsIoSlotEntry.setIndexNames(
    (0, "CPQSTSYS-MIB", "cpqSsIoSlotChassisIndex"),
    (0, "CPQSTSYS-MIB", "cpqSsIoSlotIndex"),
)
if mibBuilder.loadTexts:
    cpqSsIoSlotEntry.setStatus("mandatory")


class _CpqSsIoSlotChassisIndex_Type(Integer32):
    """Custom type cpqSsIoSlotChassisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSsIoSlotChassisIndex_Type.__name__ = "Integer32"
_CpqSsIoSlotChassisIndex_Object = MibTableColumn
cpqSsIoSlotChassisIndex = _CpqSsIoSlotChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 2, 1, 1),
    _CpqSsIoSlotChassisIndex_Type()
)
cpqSsIoSlotChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsIoSlotChassisIndex.setStatus("mandatory")
_CpqSsIoSlotIndex_Type = Integer32
_CpqSsIoSlotIndex_Object = MibTableColumn
cpqSsIoSlotIndex = _CpqSsIoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 2, 1, 2),
    _CpqSsIoSlotIndex_Type()
)
cpqSsIoSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsIoSlotIndex.setStatus("mandatory")


class _CpqSsIoSlotControllerType_Type(Integer32):
    """Custom type cpqSsIoSlotControllerType based on Integer32"""
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
        *(("fibreArray", 4),
          ("iScsiArray", 7),
          ("noSlot", 6),
          ("notInstalled", 2),
          ("other", 1),
          ("sasArray", 8),
          ("scsiArray", 5),
          ("unknownBoard", 3))
    )


_CpqSsIoSlotControllerType_Type.__name__ = "Integer32"
_CpqSsIoSlotControllerType_Object = MibTableColumn
cpqSsIoSlotControllerType = _CpqSsIoSlotControllerType_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 2, 1, 3),
    _CpqSsIoSlotControllerType_Type()
)
cpqSsIoSlotControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsIoSlotControllerType.setStatus("mandatory")
_CpqSsPowerSupplyTable_Object = MibTable
cpqSsPowerSupplyTable = _CpqSsPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cpqSsPowerSupplyTable.setStatus("mandatory")
_CpqSsPowerSupplyEntry_Object = MibTableRow
cpqSsPowerSupplyEntry = _CpqSsPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 3, 1)
)
cpqSsPowerSupplyEntry.setIndexNames(
    (0, "CPQSTSYS-MIB", "cpqSsPowerSupplyChassisIndex"),
    (0, "CPQSTSYS-MIB", "cpqSsPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    cpqSsPowerSupplyEntry.setStatus("mandatory")


class _CpqSsPowerSupplyChassisIndex_Type(Integer32):
    """Custom type cpqSsPowerSupplyChassisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSsPowerSupplyChassisIndex_Type.__name__ = "Integer32"
_CpqSsPowerSupplyChassisIndex_Object = MibTableColumn
cpqSsPowerSupplyChassisIndex = _CpqSsPowerSupplyChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 3, 1, 1),
    _CpqSsPowerSupplyChassisIndex_Type()
)
cpqSsPowerSupplyChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsPowerSupplyChassisIndex.setStatus("mandatory")
_CpqSsPowerSupplyIndex_Type = Integer32
_CpqSsPowerSupplyIndex_Object = MibTableColumn
cpqSsPowerSupplyIndex = _CpqSsPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 3, 1, 2),
    _CpqSsPowerSupplyIndex_Type()
)
cpqSsPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsPowerSupplyIndex.setStatus("mandatory")


class _CpqSsPowerSupplyBay_Type(Integer32):
    """Custom type cpqSsPowerSupplyBay based on Integer32"""
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
        *(("composite", 4),
          ("other", 1),
          ("powerBay1", 2),
          ("powerBay2", 3))
    )


_CpqSsPowerSupplyBay_Type.__name__ = "Integer32"
_CpqSsPowerSupplyBay_Object = MibTableColumn
cpqSsPowerSupplyBay = _CpqSsPowerSupplyBay_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 3, 1, 3),
    _CpqSsPowerSupplyBay_Type()
)
cpqSsPowerSupplyBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsPowerSupplyBay.setStatus("mandatory")


class _CpqSsPowerSupplyStatus_Type(Integer32):
    """Custom type cpqSsPowerSupplyStatus based on Integer32"""
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
        *(("degraded", 5),
          ("failed", 4),
          ("notInstalled", 2),
          ("ok", 3),
          ("other", 1))
    )


_CpqSsPowerSupplyStatus_Type.__name__ = "Integer32"
_CpqSsPowerSupplyStatus_Object = MibTableColumn
cpqSsPowerSupplyStatus = _CpqSsPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 3, 1, 4),
    _CpqSsPowerSupplyStatus_Type()
)
cpqSsPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsPowerSupplyStatus.setStatus("mandatory")


class _CpqSsPowerSupplyUpsStatus_Type(Integer32):
    """Custom type cpqSsPowerSupplyUpsStatus based on Integer32"""
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
        *(("batteryLow", 5),
          ("noUps", 2),
          ("ok", 3),
          ("other", 1),
          ("powerFailed", 4))
    )


_CpqSsPowerSupplyUpsStatus_Type.__name__ = "Integer32"
_CpqSsPowerSupplyUpsStatus_Object = MibTableColumn
cpqSsPowerSupplyUpsStatus = _CpqSsPowerSupplyUpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 3, 1, 5),
    _CpqSsPowerSupplyUpsStatus_Type()
)
cpqSsPowerSupplyUpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsPowerSupplyUpsStatus.setStatus("mandatory")


class _CpqSsPowerSupplyCondition_Type(Integer32):
    """Custom type cpqSsPowerSupplyCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsPowerSupplyCondition_Type.__name__ = "Integer32"
_CpqSsPowerSupplyCondition_Object = MibTableColumn
cpqSsPowerSupplyCondition = _CpqSsPowerSupplyCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 3, 1, 6),
    _CpqSsPowerSupplyCondition_Type()
)
cpqSsPowerSupplyCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsPowerSupplyCondition.setStatus("mandatory")


class _CpqSsPowerSupplySerialNumber_Type(DisplayString):
    """Custom type cpqSsPowerSupplySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSsPowerSupplySerialNumber_Type.__name__ = "DisplayString"
_CpqSsPowerSupplySerialNumber_Object = MibTableColumn
cpqSsPowerSupplySerialNumber = _CpqSsPowerSupplySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 3, 1, 7),
    _CpqSsPowerSupplySerialNumber_Type()
)
cpqSsPowerSupplySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsPowerSupplySerialNumber.setStatus("mandatory")


class _CpqSsPowerSupplyBoardRevision_Type(DisplayString):
    """Custom type cpqSsPowerSupplyBoardRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqSsPowerSupplyBoardRevision_Type.__name__ = "DisplayString"
_CpqSsPowerSupplyBoardRevision_Object = MibTableColumn
cpqSsPowerSupplyBoardRevision = _CpqSsPowerSupplyBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 3, 1, 8),
    _CpqSsPowerSupplyBoardRevision_Type()
)
cpqSsPowerSupplyBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsPowerSupplyBoardRevision.setStatus("mandatory")


class _CpqSsPowerSupplyFirmwareRevision_Type(DisplayString):
    """Custom type cpqSsPowerSupplyFirmwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqSsPowerSupplyFirmwareRevision_Type.__name__ = "DisplayString"
_CpqSsPowerSupplyFirmwareRevision_Object = MibTableColumn
cpqSsPowerSupplyFirmwareRevision = _CpqSsPowerSupplyFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 3, 1, 9),
    _CpqSsPowerSupplyFirmwareRevision_Type()
)
cpqSsPowerSupplyFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsPowerSupplyFirmwareRevision.setStatus("mandatory")
_CpqSsFanModuleTable_Object = MibTable
cpqSsFanModuleTable = _CpqSsFanModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 4)
)
if mibBuilder.loadTexts:
    cpqSsFanModuleTable.setStatus("mandatory")
_CpqSsFanModuleEntry_Object = MibTableRow
cpqSsFanModuleEntry = _CpqSsFanModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 4, 1)
)
cpqSsFanModuleEntry.setIndexNames(
    (0, "CPQSTSYS-MIB", "cpqSsFanModuleChassisIndex"),
    (0, "CPQSTSYS-MIB", "cpqSsFanModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqSsFanModuleEntry.setStatus("mandatory")


class _CpqSsFanModuleChassisIndex_Type(Integer32):
    """Custom type cpqSsFanModuleChassisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSsFanModuleChassisIndex_Type.__name__ = "Integer32"
_CpqSsFanModuleChassisIndex_Object = MibTableColumn
cpqSsFanModuleChassisIndex = _CpqSsFanModuleChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 4, 1, 1),
    _CpqSsFanModuleChassisIndex_Type()
)
cpqSsFanModuleChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsFanModuleChassisIndex.setStatus("mandatory")
_CpqSsFanModuleIndex_Type = Integer32
_CpqSsFanModuleIndex_Object = MibTableColumn
cpqSsFanModuleIndex = _CpqSsFanModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 4, 1, 2),
    _CpqSsFanModuleIndex_Type()
)
cpqSsFanModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsFanModuleIndex.setStatus("mandatory")


class _CpqSsFanModuleStatus_Type(Integer32):
    """Custom type cpqSsFanModuleStatus based on Integer32"""
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
        *(("degraded", 4),
          ("failed", 5),
          ("notInstalled", 2),
          ("ok", 3),
          ("other", 1))
    )


_CpqSsFanModuleStatus_Type.__name__ = "Integer32"
_CpqSsFanModuleStatus_Object = MibTableColumn
cpqSsFanModuleStatus = _CpqSsFanModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 4, 1, 3),
    _CpqSsFanModuleStatus_Type()
)
cpqSsFanModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsFanModuleStatus.setStatus("mandatory")


class _CpqSsFanModuleCondition_Type(Integer32):
    """Custom type cpqSsFanModuleCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsFanModuleCondition_Type.__name__ = "Integer32"
_CpqSsFanModuleCondition_Object = MibTableColumn
cpqSsFanModuleCondition = _CpqSsFanModuleCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 4, 1, 4),
    _CpqSsFanModuleCondition_Type()
)
cpqSsFanModuleCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsFanModuleCondition.setStatus("mandatory")


class _CpqSsFanModuleLocation_Type(Integer32):
    """Custom type cpqSsFanModuleLocation based on Integer32"""
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
        *(("composite", 3),
          ("fanBay", 2),
          ("fanBay2", 4),
          ("other", 1))
    )


_CpqSsFanModuleLocation_Type.__name__ = "Integer32"
_CpqSsFanModuleLocation_Object = MibTableColumn
cpqSsFanModuleLocation = _CpqSsFanModuleLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 4, 1, 5),
    _CpqSsFanModuleLocation_Type()
)
cpqSsFanModuleLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsFanModuleLocation.setStatus("mandatory")


class _CpqSsFanModuleSerialNumber_Type(DisplayString):
    """Custom type cpqSsFanModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSsFanModuleSerialNumber_Type.__name__ = "DisplayString"
_CpqSsFanModuleSerialNumber_Object = MibTableColumn
cpqSsFanModuleSerialNumber = _CpqSsFanModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 4, 1, 6),
    _CpqSsFanModuleSerialNumber_Type()
)
cpqSsFanModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsFanModuleSerialNumber.setStatus("mandatory")


class _CpqSsFanModuleBoardRevision_Type(DisplayString):
    """Custom type cpqSsFanModuleBoardRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqSsFanModuleBoardRevision_Type.__name__ = "DisplayString"
_CpqSsFanModuleBoardRevision_Object = MibTableColumn
cpqSsFanModuleBoardRevision = _CpqSsFanModuleBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 4, 1, 7),
    _CpqSsFanModuleBoardRevision_Type()
)
cpqSsFanModuleBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsFanModuleBoardRevision.setStatus("mandatory")
_CpqSsTempSensorTable_Object = MibTable
cpqSsTempSensorTable = _CpqSsTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 5)
)
if mibBuilder.loadTexts:
    cpqSsTempSensorTable.setStatus("mandatory")
_CpqSsTempSensorEntry_Object = MibTableRow
cpqSsTempSensorEntry = _CpqSsTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 5, 1)
)
cpqSsTempSensorEntry.setIndexNames(
    (0, "CPQSTSYS-MIB", "cpqSsTempSensorChassisIndex"),
    (0, "CPQSTSYS-MIB", "cpqSsTempSensorIndex"),
)
if mibBuilder.loadTexts:
    cpqSsTempSensorEntry.setStatus("mandatory")


class _CpqSsTempSensorChassisIndex_Type(Integer32):
    """Custom type cpqSsTempSensorChassisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSsTempSensorChassisIndex_Type.__name__ = "Integer32"
_CpqSsTempSensorChassisIndex_Object = MibTableColumn
cpqSsTempSensorChassisIndex = _CpqSsTempSensorChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 5, 1, 1),
    _CpqSsTempSensorChassisIndex_Type()
)
cpqSsTempSensorChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsTempSensorChassisIndex.setStatus("mandatory")
_CpqSsTempSensorIndex_Type = Integer32
_CpqSsTempSensorIndex_Object = MibTableColumn
cpqSsTempSensorIndex = _CpqSsTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 5, 1, 2),
    _CpqSsTempSensorIndex_Type()
)
cpqSsTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsTempSensorIndex.setStatus("mandatory")


class _CpqSsTempSensorStatus_Type(Integer32):
    """Custom type cpqSsTempSensorStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsTempSensorStatus_Type.__name__ = "Integer32"
_CpqSsTempSensorStatus_Object = MibTableColumn
cpqSsTempSensorStatus = _CpqSsTempSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 5, 1, 3),
    _CpqSsTempSensorStatus_Type()
)
cpqSsTempSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsTempSensorStatus.setStatus("mandatory")


class _CpqSsTempSensorCondition_Type(Integer32):
    """Custom type cpqSsTempSensorCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsTempSensorCondition_Type.__name__ = "Integer32"
_CpqSsTempSensorCondition_Object = MibTableColumn
cpqSsTempSensorCondition = _CpqSsTempSensorCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 5, 1, 4),
    _CpqSsTempSensorCondition_Type()
)
cpqSsTempSensorCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsTempSensorCondition.setStatus("mandatory")


class _CpqSsTempSensorLocation_Type(Integer32):
    """Custom type cpqSsTempSensorLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 3),
          ("fanBay", 2),
          ("other", 1))
    )


_CpqSsTempSensorLocation_Type.__name__ = "Integer32"
_CpqSsTempSensorLocation_Object = MibTableColumn
cpqSsTempSensorLocation = _CpqSsTempSensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 5, 1, 5),
    _CpqSsTempSensorLocation_Type()
)
cpqSsTempSensorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsTempSensorLocation.setStatus("mandatory")
_CpqSsTempSensorCurrentValue_Type = Integer32
_CpqSsTempSensorCurrentValue_Object = MibTableColumn
cpqSsTempSensorCurrentValue = _CpqSsTempSensorCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 5, 1, 6),
    _CpqSsTempSensorCurrentValue_Type()
)
cpqSsTempSensorCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsTempSensorCurrentValue.setStatus("mandatory")
_CpqSsTempSensorLimitValue_Type = Integer32
_CpqSsTempSensorLimitValue_Object = MibTableColumn
cpqSsTempSensorLimitValue = _CpqSsTempSensorLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 5, 1, 7),
    _CpqSsTempSensorLimitValue_Type()
)
cpqSsTempSensorLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsTempSensorLimitValue.setStatus("mandatory")
_CpqSsTempSensorHysteresisValue_Type = Integer32
_CpqSsTempSensorHysteresisValue_Object = MibTableColumn
cpqSsTempSensorHysteresisValue = _CpqSsTempSensorHysteresisValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 5, 1, 8),
    _CpqSsTempSensorHysteresisValue_Type()
)
cpqSsTempSensorHysteresisValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsTempSensorHysteresisValue.setStatus("mandatory")
_CpqSsBackplaneTable_Object = MibTable
cpqSsBackplaneTable = _CpqSsBackplaneTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6)
)
if mibBuilder.loadTexts:
    cpqSsBackplaneTable.setStatus("mandatory")
_CpqSsBackplaneEntry_Object = MibTableRow
cpqSsBackplaneEntry = _CpqSsBackplaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1)
)
cpqSsBackplaneEntry.setIndexNames(
    (0, "CPQSTSYS-MIB", "cpqSsBackplaneChassisIndex"),
    (0, "CPQSTSYS-MIB", "cpqSsBackplaneIndex"),
)
if mibBuilder.loadTexts:
    cpqSsBackplaneEntry.setStatus("mandatory")


class _CpqSsBackplaneChassisIndex_Type(Integer32):
    """Custom type cpqSsBackplaneChassisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSsBackplaneChassisIndex_Type.__name__ = "Integer32"
_CpqSsBackplaneChassisIndex_Object = MibTableColumn
cpqSsBackplaneChassisIndex = _CpqSsBackplaneChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 1),
    _CpqSsBackplaneChassisIndex_Type()
)
cpqSsBackplaneChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneChassisIndex.setStatus("mandatory")


class _CpqSsBackplaneIndex_Type(Integer32):
    """Custom type cpqSsBackplaneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSsBackplaneIndex_Type.__name__ = "Integer32"
_CpqSsBackplaneIndex_Object = MibTableColumn
cpqSsBackplaneIndex = _CpqSsBackplaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 2),
    _CpqSsBackplaneIndex_Type()
)
cpqSsBackplaneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneIndex.setStatus("mandatory")


class _CpqSsBackplaneFWRev_Type(DisplayString):
    """Custom type cpqSsBackplaneFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqSsBackplaneFWRev_Type.__name__ = "DisplayString"
_CpqSsBackplaneFWRev_Object = MibTableColumn
cpqSsBackplaneFWRev = _CpqSsBackplaneFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 3),
    _CpqSsBackplaneFWRev_Type()
)
cpqSsBackplaneFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneFWRev.setStatus("mandatory")


class _CpqSsBackplaneDriveBays_Type(Integer32):
    """Custom type cpqSsBackplaneDriveBays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSsBackplaneDriveBays_Type.__name__ = "Integer32"
_CpqSsBackplaneDriveBays_Object = MibTableColumn
cpqSsBackplaneDriveBays = _CpqSsBackplaneDriveBays_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 4),
    _CpqSsBackplaneDriveBays_Type()
)
cpqSsBackplaneDriveBays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneDriveBays.setStatus("mandatory")


class _CpqSsBackplaneDuplexOption_Type(Integer32):
    """Custom type cpqSsBackplaneDuplexOption based on Integer32"""
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
        *(("duplexBottom", 4),
          ("duplexTop", 3),
          ("notDuplexed", 2),
          ("other", 1))
    )


_CpqSsBackplaneDuplexOption_Type.__name__ = "Integer32"
_CpqSsBackplaneDuplexOption_Object = MibTableColumn
cpqSsBackplaneDuplexOption = _CpqSsBackplaneDuplexOption_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 5),
    _CpqSsBackplaneDuplexOption_Type()
)
cpqSsBackplaneDuplexOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneDuplexOption.setStatus("mandatory")


class _CpqSsBackplaneCondition_Type(Integer32):
    """Custom type cpqSsBackplaneCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsBackplaneCondition_Type.__name__ = "Integer32"
_CpqSsBackplaneCondition_Object = MibTableColumn
cpqSsBackplaneCondition = _CpqSsBackplaneCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 6),
    _CpqSsBackplaneCondition_Type()
)
cpqSsBackplaneCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneCondition.setStatus("mandatory")
_CpqSsBackplaneVersion_Type = Integer32
_CpqSsBackplaneVersion_Object = MibTableColumn
cpqSsBackplaneVersion = _CpqSsBackplaneVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 7),
    _CpqSsBackplaneVersion_Type()
)
cpqSsBackplaneVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneVersion.setStatus("mandatory")


class _CpqSsBackplaneVendor_Type(DisplayString):
    """Custom type cpqSsBackplaneVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CpqSsBackplaneVendor_Type.__name__ = "DisplayString"
_CpqSsBackplaneVendor_Object = MibTableColumn
cpqSsBackplaneVendor = _CpqSsBackplaneVendor_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 8),
    _CpqSsBackplaneVendor_Type()
)
cpqSsBackplaneVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneVendor.setStatus("mandatory")


class _CpqSsBackplaneModel_Type(DisplayString):
    """Custom type cpqSsBackplaneModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CpqSsBackplaneModel_Type.__name__ = "DisplayString"
_CpqSsBackplaneModel_Object = MibTableColumn
cpqSsBackplaneModel = _CpqSsBackplaneModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 9),
    _CpqSsBackplaneModel_Type()
)
cpqSsBackplaneModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneModel.setStatus("mandatory")


class _CpqSsBackplaneFanStatus_Type(Integer32):
    """Custom type cpqSsBackplaneFanStatus based on Integer32"""
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
        *(("degraded", 4),
          ("degraded-Fan1Failed", 7),
          ("degraded-Fan2Failed", 8),
          ("failed", 5),
          ("notInstalled", 2),
          ("notSupported", 6),
          ("ok", 3),
          ("other", 1))
    )


_CpqSsBackplaneFanStatus_Type.__name__ = "Integer32"
_CpqSsBackplaneFanStatus_Object = MibTableColumn
cpqSsBackplaneFanStatus = _CpqSsBackplaneFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 10),
    _CpqSsBackplaneFanStatus_Type()
)
cpqSsBackplaneFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneFanStatus.setStatus("mandatory")


class _CpqSsBackplaneTempStatus_Type(Integer32):
    """Custom type cpqSsBackplaneTempStatus based on Integer32"""
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
        *(("degraded", 4),
          ("failed", 5),
          ("noTemp", 2),
          ("notSupported", 6),
          ("ok", 3),
          ("other", 1))
    )


_CpqSsBackplaneTempStatus_Type.__name__ = "Integer32"
_CpqSsBackplaneTempStatus_Object = MibTableColumn
cpqSsBackplaneTempStatus = _CpqSsBackplaneTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 11),
    _CpqSsBackplaneTempStatus_Type()
)
cpqSsBackplaneTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneTempStatus.setStatus("mandatory")


class _CpqSsBackplaneFtpsStatus_Type(Integer32):
    """Custom type cpqSsBackplaneFtpsStatus based on Integer32"""
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
        *(("degraded", 4),
          ("failed", 5),
          ("noFltTolPower", 2),
          ("noFltTolPower-Bay1Missing", 7),
          ("noFltTolPower-Bay2Missing", 8),
          ("notSupported", 6),
          ("ok", 3),
          ("other", 1))
    )


_CpqSsBackplaneFtpsStatus_Type.__name__ = "Integer32"
_CpqSsBackplaneFtpsStatus_Object = MibTableColumn
cpqSsBackplaneFtpsStatus = _CpqSsBackplaneFtpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 12),
    _CpqSsBackplaneFtpsStatus_Type()
)
cpqSsBackplaneFtpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneFtpsStatus.setStatus("mandatory")


class _CpqSsBackplaneSerialNumber_Type(DisplayString):
    """Custom type cpqSsBackplaneSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSsBackplaneSerialNumber_Type.__name__ = "DisplayString"
_CpqSsBackplaneSerialNumber_Object = MibTableColumn
cpqSsBackplaneSerialNumber = _CpqSsBackplaneSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 13),
    _CpqSsBackplaneSerialNumber_Type()
)
cpqSsBackplaneSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneSerialNumber.setStatus("mandatory")


class _CpqSsBackplanePlacement_Type(Integer32):
    """Custom type cpqSsBackplanePlacement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("other", 1))
    )


_CpqSsBackplanePlacement_Type.__name__ = "Integer32"
_CpqSsBackplanePlacement_Object = MibTableColumn
cpqSsBackplanePlacement = _CpqSsBackplanePlacement_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 14),
    _CpqSsBackplanePlacement_Type()
)
cpqSsBackplanePlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplanePlacement.setStatus("mandatory")
_CpqSsBackplaneBoardRevision_Type = Integer32
_CpqSsBackplaneBoardRevision_Object = MibTableColumn
cpqSsBackplaneBoardRevision = _CpqSsBackplaneBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 15),
    _CpqSsBackplaneBoardRevision_Type()
)
cpqSsBackplaneBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneBoardRevision.setStatus("mandatory")


class _CpqSsBackplaneSpeed_Type(Integer32):
    """Custom type cpqSsBackplaneSpeed based on Integer32"""
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
        *(("other", 1),
          ("sata", 4),
          ("ultra3", 2),
          ("ultra320", 3))
    )


_CpqSsBackplaneSpeed_Type.__name__ = "Integer32"
_CpqSsBackplaneSpeed_Object = MibTableColumn
cpqSsBackplaneSpeed = _CpqSsBackplaneSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 16),
    _CpqSsBackplaneSpeed_Type()
)
cpqSsBackplaneSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneSpeed.setStatus("mandatory")


class _CpqSsBackplaneConnectionType_Type(Integer32):
    """Custom type cpqSsBackplaneConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("sasAttached", 3),
          ("scsiAttached", 2))
    )


_CpqSsBackplaneConnectionType_Type.__name__ = "Integer32"
_CpqSsBackplaneConnectionType_Object = MibTableColumn
cpqSsBackplaneConnectionType = _CpqSsBackplaneConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 17),
    _CpqSsBackplaneConnectionType_Type()
)
cpqSsBackplaneConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneConnectionType.setStatus("mandatory")


class _CpqSsBackplaneConnector_Type(DisplayString):
    """Custom type cpqSsBackplaneConnector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CpqSsBackplaneConnector_Type.__name__ = "DisplayString"
_CpqSsBackplaneConnector_Object = MibTableColumn
cpqSsBackplaneConnector = _CpqSsBackplaneConnector_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 18),
    _CpqSsBackplaneConnector_Type()
)
cpqSsBackplaneConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneConnector.setStatus("mandatory")
_CpqSsBackplaneOnConnector_Type = Integer32
_CpqSsBackplaneOnConnector_Object = MibTableColumn
cpqSsBackplaneOnConnector = _CpqSsBackplaneOnConnector_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 19),
    _CpqSsBackplaneOnConnector_Type()
)
cpqSsBackplaneOnConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneOnConnector.setStatus("mandatory")


class _CpqSsBackplaneLocationString_Type(DisplayString):
    """Custom type cpqSsBackplaneLocationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSsBackplaneLocationString_Type.__name__ = "DisplayString"
_CpqSsBackplaneLocationString_Object = MibTableColumn
cpqSsBackplaneLocationString = _CpqSsBackplaneLocationString_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 6, 1, 20),
    _CpqSsBackplaneLocationString_Type()
)
cpqSsBackplaneLocationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsBackplaneLocationString.setStatus("mandatory")
_CpqSsFibreAttachmentTable_Object = MibTable
cpqSsFibreAttachmentTable = _CpqSsFibreAttachmentTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 7)
)
if mibBuilder.loadTexts:
    cpqSsFibreAttachmentTable.setStatus("mandatory")
_CpqSsFibreAttachmentEntry_Object = MibTableRow
cpqSsFibreAttachmentEntry = _CpqSsFibreAttachmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 7, 1)
)
cpqSsFibreAttachmentEntry.setIndexNames(
    (0, "CPQSTSYS-MIB", "cpqSsFibreAttachmentIndex"),
)
if mibBuilder.loadTexts:
    cpqSsFibreAttachmentEntry.setStatus("mandatory")
_CpqSsFibreAttachmentIndex_Type = Integer32
_CpqSsFibreAttachmentIndex_Object = MibTableColumn
cpqSsFibreAttachmentIndex = _CpqSsFibreAttachmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 7, 1, 1),
    _CpqSsFibreAttachmentIndex_Type()
)
cpqSsFibreAttachmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsFibreAttachmentIndex.setStatus("mandatory")
_CpqSsFibreAttachmentHostControllerIndex_Type = Integer32
_CpqSsFibreAttachmentHostControllerIndex_Object = MibTableColumn
cpqSsFibreAttachmentHostControllerIndex = _CpqSsFibreAttachmentHostControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 7, 1, 2),
    _CpqSsFibreAttachmentHostControllerIndex_Type()
)
cpqSsFibreAttachmentHostControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsFibreAttachmentHostControllerIndex.setStatus("mandatory")


class _CpqSsFibreAttachmentHostControllerPort_Type(Integer32):
    """Custom type cpqSsFibreAttachmentHostControllerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSsFibreAttachmentHostControllerPort_Type.__name__ = "Integer32"
_CpqSsFibreAttachmentHostControllerPort_Object = MibTableColumn
cpqSsFibreAttachmentHostControllerPort = _CpqSsFibreAttachmentHostControllerPort_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 7, 1, 3),
    _CpqSsFibreAttachmentHostControllerPort_Type()
)
cpqSsFibreAttachmentHostControllerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsFibreAttachmentHostControllerPort.setStatus("mandatory")


class _CpqSsFibreAttachmentDeviceType_Type(Integer32):
    """Custom type cpqSsFibreAttachmentDeviceType based on Integer32"""
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
        *(("fibreChannelSwitch", 4),
          ("other", 1),
          ("storageBox", 2),
          ("tapeController", 3))
    )


_CpqSsFibreAttachmentDeviceType_Type.__name__ = "Integer32"
_CpqSsFibreAttachmentDeviceType_Object = MibTableColumn
cpqSsFibreAttachmentDeviceType = _CpqSsFibreAttachmentDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 7, 1, 4),
    _CpqSsFibreAttachmentDeviceType_Type()
)
cpqSsFibreAttachmentDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsFibreAttachmentDeviceType.setStatus("mandatory")


class _CpqSsFibreAttachmentDeviceIndex_Type(Integer32):
    """Custom type cpqSsFibreAttachmentDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSsFibreAttachmentDeviceIndex_Type.__name__ = "Integer32"
_CpqSsFibreAttachmentDeviceIndex_Object = MibTableColumn
cpqSsFibreAttachmentDeviceIndex = _CpqSsFibreAttachmentDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 7, 1, 5),
    _CpqSsFibreAttachmentDeviceIndex_Type()
)
cpqSsFibreAttachmentDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsFibreAttachmentDeviceIndex.setStatus("mandatory")


class _CpqSsFibreAttachmentDevicePort_Type(Integer32):
    """Custom type cpqSsFibreAttachmentDevicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSsFibreAttachmentDevicePort_Type.__name__ = "Integer32"
_CpqSsFibreAttachmentDevicePort_Object = MibTableColumn
cpqSsFibreAttachmentDevicePort = _CpqSsFibreAttachmentDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 7, 1, 6),
    _CpqSsFibreAttachmentDevicePort_Type()
)
cpqSsFibreAttachmentDevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsFibreAttachmentDevicePort.setStatus("mandatory")
_CpqSsScsiAttachmentTable_Object = MibTable
cpqSsScsiAttachmentTable = _CpqSsScsiAttachmentTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 8)
)
if mibBuilder.loadTexts:
    cpqSsScsiAttachmentTable.setStatus("mandatory")
_CpqSsScsiAttachmentEntry_Object = MibTableRow
cpqSsScsiAttachmentEntry = _CpqSsScsiAttachmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 8, 1)
)
cpqSsScsiAttachmentEntry.setIndexNames(
    (0, "CPQSTSYS-MIB", "cpqSsScsiAttachmentIndex"),
)
if mibBuilder.loadTexts:
    cpqSsScsiAttachmentEntry.setStatus("mandatory")
_CpqSsScsiAttachmentIndex_Type = Integer32
_CpqSsScsiAttachmentIndex_Object = MibTableColumn
cpqSsScsiAttachmentIndex = _CpqSsScsiAttachmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 8, 1, 1),
    _CpqSsScsiAttachmentIndex_Type()
)
cpqSsScsiAttachmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsScsiAttachmentIndex.setStatus("mandatory")


class _CpqSsScsiAttachmentControllerIndex_Type(Integer32):
    """Custom type cpqSsScsiAttachmentControllerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSsScsiAttachmentControllerIndex_Type.__name__ = "Integer32"
_CpqSsScsiAttachmentControllerIndex_Object = MibTableColumn
cpqSsScsiAttachmentControllerIndex = _CpqSsScsiAttachmentControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 8, 1, 2),
    _CpqSsScsiAttachmentControllerIndex_Type()
)
cpqSsScsiAttachmentControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsScsiAttachmentControllerIndex.setStatus("mandatory")


class _CpqSsScsiAttachmentControllerPort_Type(Integer32):
    """Custom type cpqSsScsiAttachmentControllerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSsScsiAttachmentControllerPort_Type.__name__ = "Integer32"
_CpqSsScsiAttachmentControllerPort_Object = MibTableColumn
cpqSsScsiAttachmentControllerPort = _CpqSsScsiAttachmentControllerPort_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 8, 1, 3),
    _CpqSsScsiAttachmentControllerPort_Type()
)
cpqSsScsiAttachmentControllerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsScsiAttachmentControllerPort.setStatus("mandatory")


class _CpqSsScsiAttachmentControllerTarget_Type(Integer32):
    """Custom type cpqSsScsiAttachmentControllerTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSsScsiAttachmentControllerTarget_Type.__name__ = "Integer32"
_CpqSsScsiAttachmentControllerTarget_Object = MibTableColumn
cpqSsScsiAttachmentControllerTarget = _CpqSsScsiAttachmentControllerTarget_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 8, 1, 4),
    _CpqSsScsiAttachmentControllerTarget_Type()
)
cpqSsScsiAttachmentControllerTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsScsiAttachmentControllerTarget.setStatus("mandatory")


class _CpqSsScsiAttachmentControllerLun_Type(Integer32):
    """Custom type cpqSsScsiAttachmentControllerLun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSsScsiAttachmentControllerLun_Type.__name__ = "Integer32"
_CpqSsScsiAttachmentControllerLun_Object = MibTableColumn
cpqSsScsiAttachmentControllerLun = _CpqSsScsiAttachmentControllerLun_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 8, 1, 5),
    _CpqSsScsiAttachmentControllerLun_Type()
)
cpqSsScsiAttachmentControllerLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsScsiAttachmentControllerLun.setStatus("mandatory")


class _CpqSsScsiAttachmentChassisIndex_Type(Integer32):
    """Custom type cpqSsScsiAttachmentChassisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSsScsiAttachmentChassisIndex_Type.__name__ = "Integer32"
_CpqSsScsiAttachmentChassisIndex_Object = MibTableColumn
cpqSsScsiAttachmentChassisIndex = _CpqSsScsiAttachmentChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 8, 1, 6),
    _CpqSsScsiAttachmentChassisIndex_Type()
)
cpqSsScsiAttachmentChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsScsiAttachmentChassisIndex.setStatus("mandatory")


class _CpqSsScsiAttachmentChassisIoSlot_Type(Integer32):
    """Custom type cpqSsScsiAttachmentChassisIoSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSsScsiAttachmentChassisIoSlot_Type.__name__ = "Integer32"
_CpqSsScsiAttachmentChassisIoSlot_Object = MibTableColumn
cpqSsScsiAttachmentChassisIoSlot = _CpqSsScsiAttachmentChassisIoSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 8, 1, 7),
    _CpqSsScsiAttachmentChassisIoSlot_Type()
)
cpqSsScsiAttachmentChassisIoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsScsiAttachmentChassisIoSlot.setStatus("mandatory")


class _CpqSsScsiAttachmentPathStatus_Type(Integer32):
    """Custom type cpqSsScsiAttachmentPathStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsScsiAttachmentPathStatus_Type.__name__ = "Integer32"
_CpqSsScsiAttachmentPathStatus_Object = MibTableColumn
cpqSsScsiAttachmentPathStatus = _CpqSsScsiAttachmentPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 8, 1, 8),
    _CpqSsScsiAttachmentPathStatus_Type()
)
cpqSsScsiAttachmentPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsScsiAttachmentPathStatus.setStatus("mandatory")


class _CpqSsScsiAttachmentPathCondition_Type(Integer32):
    """Custom type cpqSsScsiAttachmentPathCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsScsiAttachmentPathCondition_Type.__name__ = "Integer32"
_CpqSsScsiAttachmentPathCondition_Object = MibTableColumn
cpqSsScsiAttachmentPathCondition = _CpqSsScsiAttachmentPathCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 2, 8, 1, 9),
    _CpqSsScsiAttachmentPathCondition_Type()
)
cpqSsScsiAttachmentPathCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsScsiAttachmentPathCondition.setStatus("mandatory")
_CpqSsDrvBoxPathTable_Object = MibTable
cpqSsDrvBoxPathTable = _CpqSsDrvBoxPathTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 3)
)
if mibBuilder.loadTexts:
    cpqSsDrvBoxPathTable.setStatus("mandatory")
_CpqSsDrvBoxPathEntry_Object = MibTableRow
cpqSsDrvBoxPathEntry = _CpqSsDrvBoxPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 3, 1)
)
cpqSsDrvBoxPathEntry.setIndexNames(
    (0, "CPQSTSYS-MIB", "cpqSsDrvBoxPathCntlrIndex"),
    (0, "CPQSTSYS-MIB", "cpqSsDrvBoxPathBoxIndex"),
    (0, "CPQSTSYS-MIB", "cpqSsDrvBoxPathIndex"),
)
if mibBuilder.loadTexts:
    cpqSsDrvBoxPathEntry.setStatus("mandatory")
_CpqSsDrvBoxPathCntlrIndex_Type = Integer32
_CpqSsDrvBoxPathCntlrIndex_Object = MibTableColumn
cpqSsDrvBoxPathCntlrIndex = _CpqSsDrvBoxPathCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 3, 1, 1),
    _CpqSsDrvBoxPathCntlrIndex_Type()
)
cpqSsDrvBoxPathCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsDrvBoxPathCntlrIndex.setStatus("mandatory")
_CpqSsDrvBoxPathBoxIndex_Type = Integer32
_CpqSsDrvBoxPathBoxIndex_Object = MibTableColumn
cpqSsDrvBoxPathBoxIndex = _CpqSsDrvBoxPathBoxIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 3, 1, 2),
    _CpqSsDrvBoxPathBoxIndex_Type()
)
cpqSsDrvBoxPathBoxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsDrvBoxPathBoxIndex.setStatus("mandatory")
_CpqSsDrvBoxPathIndex_Type = Integer32
_CpqSsDrvBoxPathIndex_Object = MibTableColumn
cpqSsDrvBoxPathIndex = _CpqSsDrvBoxPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 3, 1, 3),
    _CpqSsDrvBoxPathIndex_Type()
)
cpqSsDrvBoxPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsDrvBoxPathIndex.setStatus("mandatory")


class _CpqSsDrvBoxPathStatus_Type(Integer32):
    """Custom type cpqSsDrvBoxPathStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsDrvBoxPathStatus_Type.__name__ = "Integer32"
_CpqSsDrvBoxPathStatus_Object = MibTableColumn
cpqSsDrvBoxPathStatus = _CpqSsDrvBoxPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 3, 1, 4),
    _CpqSsDrvBoxPathStatus_Type()
)
cpqSsDrvBoxPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsDrvBoxPathStatus.setStatus("mandatory")


class _CpqSsDrvBoxPathCurrentRole_Type(Integer32):
    """Custom type cpqSsDrvBoxPathCurrentRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("alternate", 3),
          ("other", 1))
    )


_CpqSsDrvBoxPathCurrentRole_Type.__name__ = "Integer32"
_CpqSsDrvBoxPathCurrentRole_Object = MibTableColumn
cpqSsDrvBoxPathCurrentRole = _CpqSsDrvBoxPathCurrentRole_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 3, 1, 5),
    _CpqSsDrvBoxPathCurrentRole_Type()
)
cpqSsDrvBoxPathCurrentRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsDrvBoxPathCurrentRole.setStatus("mandatory")


class _CpqSsDrvBoxPathHostConnector_Type(DisplayString):
    """Custom type cpqSsDrvBoxPathHostConnector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CpqSsDrvBoxPathHostConnector_Type.__name__ = "DisplayString"
_CpqSsDrvBoxPathHostConnector_Object = MibTableColumn
cpqSsDrvBoxPathHostConnector = _CpqSsDrvBoxPathHostConnector_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 3, 1, 6),
    _CpqSsDrvBoxPathHostConnector_Type()
)
cpqSsDrvBoxPathHostConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsDrvBoxPathHostConnector.setStatus("mandatory")
_CpqSsDrvBoxPathBoxOnConnector_Type = Integer32
_CpqSsDrvBoxPathBoxOnConnector_Object = MibTableColumn
cpqSsDrvBoxPathBoxOnConnector = _CpqSsDrvBoxPathBoxOnConnector_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 3, 1, 7),
    _CpqSsDrvBoxPathBoxOnConnector_Type()
)
cpqSsDrvBoxPathBoxOnConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsDrvBoxPathBoxOnConnector.setStatus("mandatory")


class _CpqSsDrvBoxPathLocationString_Type(DisplayString):
    """Custom type cpqSsDrvBoxPathLocationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSsDrvBoxPathLocationString_Type.__name__ = "DisplayString"
_CpqSsDrvBoxPathLocationString_Object = MibTableColumn
cpqSsDrvBoxPathLocationString = _CpqSsDrvBoxPathLocationString_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 2, 3, 1, 8),
    _CpqSsDrvBoxPathLocationString_Type()
)
cpqSsDrvBoxPathLocationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsDrvBoxPathLocationString.setStatus("mandatory")
_CpqSsTrap_ObjectIdentity = ObjectIdentity
cpqSsTrap = _CpqSsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 8, 3)
)
_CpqSsTrapPkts_Type = Counter32
_CpqSsTrapPkts_Object = MibScalar
cpqSsTrapPkts = _CpqSsTrapPkts_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 3, 1),
    _CpqSsTrapPkts_Type()
)
cpqSsTrapPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsTrapPkts.setStatus("deprecated")


class _CpqSsTrapLogMaxSize_Type(Integer32):
    """Custom type cpqSsTrapLogMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSsTrapLogMaxSize_Type.__name__ = "Integer32"
_CpqSsTrapLogMaxSize_Object = MibScalar
cpqSsTrapLogMaxSize = _CpqSsTrapLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 3, 2),
    _CpqSsTrapLogMaxSize_Type()
)
cpqSsTrapLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsTrapLogMaxSize.setStatus("deprecated")
_CpqSsTrapLogTable_Object = MibTable
cpqSsTrapLogTable = _CpqSsTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 3, 3)
)
if mibBuilder.loadTexts:
    cpqSsTrapLogTable.setStatus("deprecated")
_CpqSsTrapLogEntry_Object = MibTableRow
cpqSsTrapLogEntry = _CpqSsTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 3, 3, 1)
)
cpqSsTrapLogEntry.setIndexNames(
    (0, "CPQSTSYS-MIB", "cpqSsTrapLogIndex"),
)
if mibBuilder.loadTexts:
    cpqSsTrapLogEntry.setStatus("deprecated")


class _CpqSsTrapLogIndex_Type(Integer32):
    """Custom type cpqSsTrapLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSsTrapLogIndex_Type.__name__ = "Integer32"
_CpqSsTrapLogIndex_Object = MibTableColumn
cpqSsTrapLogIndex = _CpqSsTrapLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 3, 3, 1, 1),
    _CpqSsTrapLogIndex_Type()
)
cpqSsTrapLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsTrapLogIndex.setStatus("deprecated")


class _CpqSsTrapType_Type(Integer32):
    """Custom type cpqSsTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8001,
              8002,
              8003,
              8004,
              8005,
              8006)
        )
    )
    namedValues = NamedValues(
        *(("cpqSs2FanStatusChange", 8001),
          ("cpqSsFanStatusChange", 1),
          ("cpqSsSidePanelInPlace", 8005),
          ("cpqSsSidePanelRemoved", 8006),
          ("cpqSsTempDegraded", 8003),
          ("cpqSsTempFailed", 8002),
          ("cpqSsTempOk", 8004))
    )


_CpqSsTrapType_Type.__name__ = "Integer32"
_CpqSsTrapType_Object = MibTableColumn
cpqSsTrapType = _CpqSsTrapType_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 3, 3, 1, 2),
    _CpqSsTrapType_Type()
)
cpqSsTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsTrapType.setStatus("deprecated")


class _CpqSsTrapTime_Type(OctetString):
    """Custom type cpqSsTrapTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CpqSsTrapTime_Type.__name__ = "OctetString"
_CpqSsTrapTime_Object = MibTableColumn
cpqSsTrapTime = _CpqSsTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 3, 3, 1, 3),
    _CpqSsTrapTime_Type()
)
cpqSsTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsTrapTime.setStatus("deprecated")
_CpqSsRaidSystem_ObjectIdentity = ObjectIdentity
cpqSsRaidSystem = _CpqSsRaidSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 8, 4)
)
_CpqSsRaidSystemTable_Object = MibTable
cpqSsRaidSystemTable = _CpqSsRaidSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 4, 1)
)
if mibBuilder.loadTexts:
    cpqSsRaidSystemTable.setStatus("mandatory")
_CpqSsRaidSystemEntry_Object = MibTableRow
cpqSsRaidSystemEntry = _CpqSsRaidSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 4, 1, 1)
)
cpqSsRaidSystemEntry.setIndexNames(
    (0, "CPQSTSYS-MIB", "cpqSsRaidSystemIndex"),
)
if mibBuilder.loadTexts:
    cpqSsRaidSystemEntry.setStatus("mandatory")


class _CpqSsRaidSystemIndex_Type(Integer32):
    """Custom type cpqSsRaidSystemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSsRaidSystemIndex_Type.__name__ = "Integer32"
_CpqSsRaidSystemIndex_Object = MibTableColumn
cpqSsRaidSystemIndex = _CpqSsRaidSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 4, 1, 1, 1),
    _CpqSsRaidSystemIndex_Type()
)
cpqSsRaidSystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsRaidSystemIndex.setStatus("mandatory")


class _CpqSsRaidSystemName_Type(DisplayString):
    """Custom type cpqSsRaidSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSsRaidSystemName_Type.__name__ = "DisplayString"
_CpqSsRaidSystemName_Object = MibTableColumn
cpqSsRaidSystemName = _CpqSsRaidSystemName_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 4, 1, 1, 2),
    _CpqSsRaidSystemName_Type()
)
cpqSsRaidSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsRaidSystemName.setStatus("mandatory")


class _CpqSsRaidSystemStatus_Type(Integer32):
    """Custom type cpqSsRaidSystemStatus based on Integer32"""
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
        *(("agentNotRunning", 2),
          ("communicationLoss", 5),
          ("good", 3),
          ("other", 1),
          ("warning", 4))
    )


_CpqSsRaidSystemStatus_Type.__name__ = "Integer32"
_CpqSsRaidSystemStatus_Object = MibTableColumn
cpqSsRaidSystemStatus = _CpqSsRaidSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 4, 1, 1, 3),
    _CpqSsRaidSystemStatus_Type()
)
cpqSsRaidSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsRaidSystemStatus.setStatus("mandatory")


class _CpqSsRaidSystemCondition_Type(Integer32):
    """Custom type cpqSsRaidSystemCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSsRaidSystemCondition_Type.__name__ = "Integer32"
_CpqSsRaidSystemCondition_Object = MibTableColumn
cpqSsRaidSystemCondition = _CpqSsRaidSystemCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 4, 1, 1, 4),
    _CpqSsRaidSystemCondition_Type()
)
cpqSsRaidSystemCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsRaidSystemCondition.setStatus("mandatory")


class _CpqSsRaidSystemCntlr1SerialNumber_Type(DisplayString):
    """Custom type cpqSsRaidSystemCntlr1SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSsRaidSystemCntlr1SerialNumber_Type.__name__ = "DisplayString"
_CpqSsRaidSystemCntlr1SerialNumber_Object = MibTableColumn
cpqSsRaidSystemCntlr1SerialNumber = _CpqSsRaidSystemCntlr1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 4, 1, 1, 5),
    _CpqSsRaidSystemCntlr1SerialNumber_Type()
)
cpqSsRaidSystemCntlr1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsRaidSystemCntlr1SerialNumber.setStatus("mandatory")


class _CpqSsRaidSystemCntlr2SerialNumber_Type(DisplayString):
    """Custom type cpqSsRaidSystemCntlr2SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSsRaidSystemCntlr2SerialNumber_Type.__name__ = "DisplayString"
_CpqSsRaidSystemCntlr2SerialNumber_Object = MibTableColumn
cpqSsRaidSystemCntlr2SerialNumber = _CpqSsRaidSystemCntlr2SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 8, 4, 1, 1, 6),
    _CpqSsRaidSystemCntlr2SerialNumber_Type()
)
cpqSsRaidSystemCntlr2SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSsRaidSystemCntlr2SerialNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqSs2FanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8001)
)
cpqSs2FanStatusChange.setObjects(
    ("CPQSTSYS-MIB", "cpqSsBoxFanStatus")
)
if mibBuilder.loadTexts:
    cpqSs2FanStatusChange.setStatus(
        ""
    )

cpqSsTempFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8002)
)
cpqSsTempFailed.setObjects(
    ("CPQSTSYS-MIB", "cpqSsBoxTempStatus")
)
if mibBuilder.loadTexts:
    cpqSsTempFailed.setStatus(
        ""
    )

cpqSsTempDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8003)
)
cpqSsTempDegraded.setObjects(
    ("CPQSTSYS-MIB", "cpqSsBoxTempStatus")
)
if mibBuilder.loadTexts:
    cpqSsTempDegraded.setStatus(
        ""
    )

cpqSsTempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8004)
)
cpqSsTempOk.setObjects(
    ("CPQSTSYS-MIB", "cpqSsBoxTempStatus")
)
if mibBuilder.loadTexts:
    cpqSsTempOk.setStatus(
        ""
    )

cpqSsSidePanelInPlace = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8005)
)
cpqSsSidePanelInPlace.setObjects(
    ("CPQSTSYS-MIB", "cpqSsBoxSidePanelStatus")
)
if mibBuilder.loadTexts:
    cpqSsSidePanelInPlace.setStatus(
        ""
    )

cpqSsSidePanelRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8006)
)
cpqSsSidePanelRemoved.setObjects(
    ("CPQSTSYS-MIB", "cpqSsBoxSidePanelStatus")
)
if mibBuilder.loadTexts:
    cpqSsSidePanelRemoved.setStatus(
        ""
    )

cpqSsPwrSupplyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8007)
)
if mibBuilder.loadTexts:
    cpqSsPwrSupplyDegraded.setStatus(
        ""
    )

cpqSs3FanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8008)
)
cpqSs3FanStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxFanStatus"))
)
if mibBuilder.loadTexts:
    cpqSs3FanStatusChange.setStatus(
        ""
    )

cpqSs3TempFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8009)
)
cpqSs3TempFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxTempStatus"))
)
if mibBuilder.loadTexts:
    cpqSs3TempFailed.setStatus(
        ""
    )

cpqSs3TempDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8010)
)
cpqSs3TempDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxTempStatus"))
)
if mibBuilder.loadTexts:
    cpqSs3TempDegraded.setStatus(
        ""
    )

cpqSs3TempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8011)
)
cpqSs3TempOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxTempStatus"))
)
if mibBuilder.loadTexts:
    cpqSs3TempOk.setStatus(
        ""
    )

cpqSs3SidePanelInPlace = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8012)
)
cpqSs3SidePanelInPlace.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxSidePanelStatus"))
)
if mibBuilder.loadTexts:
    cpqSs3SidePanelInPlace.setStatus(
        ""
    )

cpqSs3SidePanelRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8013)
)
cpqSs3SidePanelRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxSidePanelStatus"))
)
if mibBuilder.loadTexts:
    cpqSs3SidePanelRemoved.setStatus(
        ""
    )

cpqSs3PwrSupplyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8014)
)
cpqSs3PwrSupplyDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSs3PwrSupplyDegraded.setStatus(
        ""
    )

cpqSs4PwrSupplyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8015)
)
cpqSs4PwrSupplyDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxFltTolPwrSupplyStatus"))
)
if mibBuilder.loadTexts:
    cpqSs4PwrSupplyDegraded.setStatus(
        ""
    )

cpqSsExFanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8016)
)
cpqSsExFanStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQSTSYS-MIB", "cpqSsFanModuleLocation"),
        ("CPQSTSYS-MIB", "cpqSsFanModuleStatus"))
)
if mibBuilder.loadTexts:
    cpqSsExFanStatusChange.setStatus(
        ""
    )

cpqSsExPowerSupplyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8017)
)
cpqSsExPowerSupplyStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQSTSYS-MIB", "cpqSsPowerSupplyBay"),
        ("CPQSTSYS-MIB", "cpqSsPowerSupplyStatus"))
)
if mibBuilder.loadTexts:
    cpqSsExPowerSupplyStatusChange.setStatus(
        ""
    )

cpqSsExPowerSupplyUpsStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8018)
)
cpqSsExPowerSupplyUpsStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQSTSYS-MIB", "cpqSsPowerSupplyBay"),
        ("CPQSTSYS-MIB", "cpqSsPowerSupplyUpsStatus"))
)
if mibBuilder.loadTexts:
    cpqSsExPowerSupplyUpsStatusChange.setStatus(
        ""
    )

cpqSsExTempSensorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8019)
)
cpqSsExTempSensorStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQSTSYS-MIB", "cpqSsTempSensorLocation"),
        ("CPQSTSYS-MIB", "cpqSsTempSensorStatus"),
        ("CPQSTSYS-MIB", "cpqSsTempSensorCurrentValue"))
)
if mibBuilder.loadTexts:
    cpqSsExTempSensorStatusChange.setStatus(
        ""
    )

cpqSsEx2FanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8020)
)
cpqSsEx2FanStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQSTSYS-MIB", "cpqSsFanModuleLocation"),
        ("CPQSTSYS-MIB", "cpqSsFanModuleStatus"),
        ("CPQSTSYS-MIB", "cpqSsFanModuleSerialNumber"),
        ("CPQSTSYS-MIB", "cpqSsFanModuleBoardRevision"))
)
if mibBuilder.loadTexts:
    cpqSsEx2FanStatusChange.setStatus(
        ""
    )

cpqSsEx2PowerSupplyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8021)
)
cpqSsEx2PowerSupplyStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQSTSYS-MIB", "cpqSsPowerSupplyBay"),
        ("CPQSTSYS-MIB", "cpqSsPowerSupplyStatus"),
        ("CPQSTSYS-MIB", "cpqSsPowerSupplySerialNumber"),
        ("CPQSTSYS-MIB", "cpqSsPowerSupplyBoardRevision"),
        ("CPQSTSYS-MIB", "cpqSsPowerSupplyFirmwareRevision"))
)
if mibBuilder.loadTexts:
    cpqSsEx2PowerSupplyStatusChange.setStatus(
        ""
    )

cpqSsExBackplaneFanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8022)
)
cpqSsExBackplaneFanStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneIndex"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneVendor"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneModel"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneSerialNumber"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneFanStatus"))
)
if mibBuilder.loadTexts:
    cpqSsExBackplaneFanStatusChange.setStatus(
        ""
    )

cpqSsExBackplaneTempStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8023)
)
cpqSsExBackplaneTempStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneIndex"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneVendor"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneModel"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneSerialNumber"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneTempStatus"))
)
if mibBuilder.loadTexts:
    cpqSsExBackplaneTempStatusChange.setStatus(
        ""
    )

cpqSsExBackplanePowerSupplyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8024)
)
cpqSsExBackplanePowerSupplyStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneIndex"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneVendor"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneModel"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneSerialNumber"),
        ("CPQSTSYS-MIB", "cpqSsBackplaneFtpsStatus"))
)
if mibBuilder.loadTexts:
    cpqSsExBackplanePowerSupplyStatusChange.setStatus(
        ""
    )

cpqSsExRecoveryServerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8025)
)
cpqSsExRecoveryServerStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQSTSYS-MIB", "cpqSsChassisRsoStatus"),
        ("CPQSTSYS-MIB", "cpqSsChassisIndex"))
)
if mibBuilder.loadTexts:
    cpqSsExRecoveryServerStatusChange.setStatus(
        ""
    )

cpqSs5FanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8026)
)
cpqSs5FanStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrHwLocation"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxBusIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxVendor"),
        ("CPQSTSYS-MIB", "cpqSsBoxModel"),
        ("CPQSTSYS-MIB", "cpqSsBoxSerialNumber"),
        ("CPQSTSYS-MIB", "cpqSsBoxFanStatus"))
)
if mibBuilder.loadTexts:
    cpqSs5FanStatusChange.setStatus(
        ""
    )

cpqSs5TempStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8027)
)
cpqSs5TempStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrHwLocation"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxBusIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxVendor"),
        ("CPQSTSYS-MIB", "cpqSsBoxModel"),
        ("CPQSTSYS-MIB", "cpqSsBoxSerialNumber"),
        ("CPQSTSYS-MIB", "cpqSsBoxTempStatus"))
)
if mibBuilder.loadTexts:
    cpqSs5TempStatusChange.setStatus(
        ""
    )

cpqSs5PwrSupplyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8028)
)
cpqSs5PwrSupplyStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrHwLocation"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxBusIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxVendor"),
        ("CPQSTSYS-MIB", "cpqSsBoxModel"),
        ("CPQSTSYS-MIB", "cpqSsBoxSerialNumber"),
        ("CPQSTSYS-MIB", "cpqSsBoxFltTolPwrSupplyStatus"))
)
if mibBuilder.loadTexts:
    cpqSs5PwrSupplyStatusChange.setStatus(
        ""
    )

cpqSs6FanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8029)
)
cpqSs6FanStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrHwLocation"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxBusIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxVendor"),
        ("CPQSTSYS-MIB", "cpqSsBoxModel"),
        ("CPQSTSYS-MIB", "cpqSsBoxSerialNumber"),
        ("CPQSTSYS-MIB", "cpqSsBoxFanStatus"),
        ("CPQSTSYS-MIB", "cpqSsBoxLocationString"))
)
if mibBuilder.loadTexts:
    cpqSs6FanStatusChange.setStatus(
        ""
    )

cpqSs6TempStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8030)
)
cpqSs6TempStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrHwLocation"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxBusIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxVendor"),
        ("CPQSTSYS-MIB", "cpqSsBoxModel"),
        ("CPQSTSYS-MIB", "cpqSsBoxSerialNumber"),
        ("CPQSTSYS-MIB", "cpqSsBoxTempStatus"),
        ("CPQSTSYS-MIB", "cpqSsBoxLocationString"))
)
if mibBuilder.loadTexts:
    cpqSs6TempStatusChange.setStatus(
        ""
    )

cpqSs6PwrSupplyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 8031)
)
cpqSs6PwrSupplyStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrHwLocation"),
        ("CPQSTSYS-MIB", "cpqSsBoxCntlrIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxBusIndex"),
        ("CPQSTSYS-MIB", "cpqSsBoxVendor"),
        ("CPQSTSYS-MIB", "cpqSsBoxModel"),
        ("CPQSTSYS-MIB", "cpqSsBoxSerialNumber"),
        ("CPQSTSYS-MIB", "cpqSsBoxFltTolPwrSupplyStatus"),
        ("CPQSTSYS-MIB", "cpqSsBoxLocationString"))
)
if mibBuilder.loadTexts:
    cpqSs6PwrSupplyStatusChange.setStatus(
        ""
    )

cpqSsFanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 8, 0, 1)
)
cpqSsFanStatusChange.setObjects(
    ("CPQSTSYS-MIB", "cpqSsBoxFanStatus")
)
if mibBuilder.loadTexts:
    cpqSsFanStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQSTSYS-MIB",
    **{"cpqSs2FanStatusChange": cpqSs2FanStatusChange,
       "cpqSsTempFailed": cpqSsTempFailed,
       "cpqSsTempDegraded": cpqSsTempDegraded,
       "cpqSsTempOk": cpqSsTempOk,
       "cpqSsSidePanelInPlace": cpqSsSidePanelInPlace,
       "cpqSsSidePanelRemoved": cpqSsSidePanelRemoved,
       "cpqSsPwrSupplyDegraded": cpqSsPwrSupplyDegraded,
       "cpqSs3FanStatusChange": cpqSs3FanStatusChange,
       "cpqSs3TempFailed": cpqSs3TempFailed,
       "cpqSs3TempDegraded": cpqSs3TempDegraded,
       "cpqSs3TempOk": cpqSs3TempOk,
       "cpqSs3SidePanelInPlace": cpqSs3SidePanelInPlace,
       "cpqSs3SidePanelRemoved": cpqSs3SidePanelRemoved,
       "cpqSs3PwrSupplyDegraded": cpqSs3PwrSupplyDegraded,
       "cpqSs4PwrSupplyDegraded": cpqSs4PwrSupplyDegraded,
       "cpqSsExFanStatusChange": cpqSsExFanStatusChange,
       "cpqSsExPowerSupplyStatusChange": cpqSsExPowerSupplyStatusChange,
       "cpqSsExPowerSupplyUpsStatusChange": cpqSsExPowerSupplyUpsStatusChange,
       "cpqSsExTempSensorStatusChange": cpqSsExTempSensorStatusChange,
       "cpqSsEx2FanStatusChange": cpqSsEx2FanStatusChange,
       "cpqSsEx2PowerSupplyStatusChange": cpqSsEx2PowerSupplyStatusChange,
       "cpqSsExBackplaneFanStatusChange": cpqSsExBackplaneFanStatusChange,
       "cpqSsExBackplaneTempStatusChange": cpqSsExBackplaneTempStatusChange,
       "cpqSsExBackplanePowerSupplyStatusChange": cpqSsExBackplanePowerSupplyStatusChange,
       "cpqSsExRecoveryServerStatusChange": cpqSsExRecoveryServerStatusChange,
       "cpqSs5FanStatusChange": cpqSs5FanStatusChange,
       "cpqSs5TempStatusChange": cpqSs5TempStatusChange,
       "cpqSs5PwrSupplyStatusChange": cpqSs5PwrSupplyStatusChange,
       "cpqSs6FanStatusChange": cpqSs6FanStatusChange,
       "cpqSs6TempStatusChange": cpqSs6TempStatusChange,
       "cpqSs6PwrSupplyStatusChange": cpqSs6PwrSupplyStatusChange,
       "cpqSsStorageSys": cpqSsStorageSys,
       "cpqSsFanStatusChange": cpqSsFanStatusChange,
       "cpqSsMibRev": cpqSsMibRev,
       "cpqSsMibRevMajor": cpqSsMibRevMajor,
       "cpqSsMibRevMinor": cpqSsMibRevMinor,
       "cpqSsMibCondition": cpqSsMibCondition,
       "cpqSsDrvBox": cpqSsDrvBox,
       "cpqSsDrvBoxTable": cpqSsDrvBoxTable,
       "cpqSsDrvBoxEntry": cpqSsDrvBoxEntry,
       "cpqSsBoxCntlrIndex": cpqSsBoxCntlrIndex,
       "cpqSsBoxBusIndex": cpqSsBoxBusIndex,
       "cpqSsBoxType": cpqSsBoxType,
       "cpqSsBoxModel": cpqSsBoxModel,
       "cpqSsBoxFWRev": cpqSsBoxFWRev,
       "cpqSsBoxVendor": cpqSsBoxVendor,
       "cpqSsBoxFanStatus": cpqSsBoxFanStatus,
       "cpqSsBoxCondition": cpqSsBoxCondition,
       "cpqSsBoxTempStatus": cpqSsBoxTempStatus,
       "cpqSsBoxSidePanelStatus": cpqSsBoxSidePanelStatus,
       "cpqSsBoxFltTolPwrSupplyStatus": cpqSsBoxFltTolPwrSupplyStatus,
       "cpqSsBoxBackPlaneVersion": cpqSsBoxBackPlaneVersion,
       "cpqSsBoxTotalBays": cpqSsBoxTotalBays,
       "cpqSsBoxPlacement": cpqSsBoxPlacement,
       "cpqSsBoxDuplexOption": cpqSsBoxDuplexOption,
       "cpqSsBoxBoardRevision": cpqSsBoxBoardRevision,
       "cpqSsBoxSerialNumber": cpqSsBoxSerialNumber,
       "cpqSsBoxCntlrHwLocation": cpqSsBoxCntlrHwLocation,
       "cpqSsBoxBackplaneSpeed": cpqSsBoxBackplaneSpeed,
       "cpqSsBoxConnectionType": cpqSsBoxConnectionType,
       "cpqSsBoxHostConnector": cpqSsBoxHostConnector,
       "cpqSsBoxBoxOnConnector": cpqSsBoxBoxOnConnector,
       "cpqSsBoxLocationString": cpqSsBoxLocationString,
       "cpqSsBoxExtended": cpqSsBoxExtended,
       "cpqSsChassisTable": cpqSsChassisTable,
       "cpqSsChassisEntry": cpqSsChassisEntry,
       "cpqSsChassisIndex": cpqSsChassisIndex,
       "cpqSsChassisConnectionType": cpqSsChassisConnectionType,
       "cpqSsChassisSerialNumber": cpqSsChassisSerialNumber,
       "cpqSsChassisName": cpqSsChassisName,
       "cpqSsChassisSystemBoardSerNum": cpqSsChassisSystemBoardSerNum,
       "cpqSsChassisSystemBoardRev": cpqSsChassisSystemBoardRev,
       "cpqSsChassisPowerBoardSerNum": cpqSsChassisPowerBoardSerNum,
       "cpqSsChassisPowerBoardRev": cpqSsChassisPowerBoardRev,
       "cpqSsChassisScsiBoardSerNum": cpqSsChassisScsiBoardSerNum,
       "cpqSsChassisScsiBoardRev": cpqSsChassisScsiBoardRev,
       "cpqSsChassisOverallCondition": cpqSsChassisOverallCondition,
       "cpqSsChassisPowerSupplyCondition": cpqSsChassisPowerSupplyCondition,
       "cpqSsChassisFanCondition": cpqSsChassisFanCondition,
       "cpqSsChassisTemperatureCondition": cpqSsChassisTemperatureCondition,
       "cpqSsChassisFcaCntlrCondition": cpqSsChassisFcaCntlrCondition,
       "cpqSsChassisFcaLogicalDriveCondition": cpqSsChassisFcaLogicalDriveCondition,
       "cpqSsChassisFcaPhysDrvCondition": cpqSsChassisFcaPhysDrvCondition,
       "cpqSsChassisTime": cpqSsChassisTime,
       "cpqSsChassisModel": cpqSsChassisModel,
       "cpqSsChassisBackplaneCondition": cpqSsChassisBackplaneCondition,
       "cpqSsChassisFcaTapeDrvCondition": cpqSsChassisFcaTapeDrvCondition,
       "cpqSsChassisRsoStatus": cpqSsChassisRsoStatus,
       "cpqSsChassisRsoCondition": cpqSsChassisRsoCondition,
       "cpqSsChassisScsiIoModuleType": cpqSsChassisScsiIoModuleType,
       "cpqSsChassisPreferredPathMode": cpqSsChassisPreferredPathMode,
       "cpqSsChassisProductId": cpqSsChassisProductId,
       "cpqSsIoSlotTable": cpqSsIoSlotTable,
       "cpqSsIoSlotEntry": cpqSsIoSlotEntry,
       "cpqSsIoSlotChassisIndex": cpqSsIoSlotChassisIndex,
       "cpqSsIoSlotIndex": cpqSsIoSlotIndex,
       "cpqSsIoSlotControllerType": cpqSsIoSlotControllerType,
       "cpqSsPowerSupplyTable": cpqSsPowerSupplyTable,
       "cpqSsPowerSupplyEntry": cpqSsPowerSupplyEntry,
       "cpqSsPowerSupplyChassisIndex": cpqSsPowerSupplyChassisIndex,
       "cpqSsPowerSupplyIndex": cpqSsPowerSupplyIndex,
       "cpqSsPowerSupplyBay": cpqSsPowerSupplyBay,
       "cpqSsPowerSupplyStatus": cpqSsPowerSupplyStatus,
       "cpqSsPowerSupplyUpsStatus": cpqSsPowerSupplyUpsStatus,
       "cpqSsPowerSupplyCondition": cpqSsPowerSupplyCondition,
       "cpqSsPowerSupplySerialNumber": cpqSsPowerSupplySerialNumber,
       "cpqSsPowerSupplyBoardRevision": cpqSsPowerSupplyBoardRevision,
       "cpqSsPowerSupplyFirmwareRevision": cpqSsPowerSupplyFirmwareRevision,
       "cpqSsFanModuleTable": cpqSsFanModuleTable,
       "cpqSsFanModuleEntry": cpqSsFanModuleEntry,
       "cpqSsFanModuleChassisIndex": cpqSsFanModuleChassisIndex,
       "cpqSsFanModuleIndex": cpqSsFanModuleIndex,
       "cpqSsFanModuleStatus": cpqSsFanModuleStatus,
       "cpqSsFanModuleCondition": cpqSsFanModuleCondition,
       "cpqSsFanModuleLocation": cpqSsFanModuleLocation,
       "cpqSsFanModuleSerialNumber": cpqSsFanModuleSerialNumber,
       "cpqSsFanModuleBoardRevision": cpqSsFanModuleBoardRevision,
       "cpqSsTempSensorTable": cpqSsTempSensorTable,
       "cpqSsTempSensorEntry": cpqSsTempSensorEntry,
       "cpqSsTempSensorChassisIndex": cpqSsTempSensorChassisIndex,
       "cpqSsTempSensorIndex": cpqSsTempSensorIndex,
       "cpqSsTempSensorStatus": cpqSsTempSensorStatus,
       "cpqSsTempSensorCondition": cpqSsTempSensorCondition,
       "cpqSsTempSensorLocation": cpqSsTempSensorLocation,
       "cpqSsTempSensorCurrentValue": cpqSsTempSensorCurrentValue,
       "cpqSsTempSensorLimitValue": cpqSsTempSensorLimitValue,
       "cpqSsTempSensorHysteresisValue": cpqSsTempSensorHysteresisValue,
       "cpqSsBackplaneTable": cpqSsBackplaneTable,
       "cpqSsBackplaneEntry": cpqSsBackplaneEntry,
       "cpqSsBackplaneChassisIndex": cpqSsBackplaneChassisIndex,
       "cpqSsBackplaneIndex": cpqSsBackplaneIndex,
       "cpqSsBackplaneFWRev": cpqSsBackplaneFWRev,
       "cpqSsBackplaneDriveBays": cpqSsBackplaneDriveBays,
       "cpqSsBackplaneDuplexOption": cpqSsBackplaneDuplexOption,
       "cpqSsBackplaneCondition": cpqSsBackplaneCondition,
       "cpqSsBackplaneVersion": cpqSsBackplaneVersion,
       "cpqSsBackplaneVendor": cpqSsBackplaneVendor,
       "cpqSsBackplaneModel": cpqSsBackplaneModel,
       "cpqSsBackplaneFanStatus": cpqSsBackplaneFanStatus,
       "cpqSsBackplaneTempStatus": cpqSsBackplaneTempStatus,
       "cpqSsBackplaneFtpsStatus": cpqSsBackplaneFtpsStatus,
       "cpqSsBackplaneSerialNumber": cpqSsBackplaneSerialNumber,
       "cpqSsBackplanePlacement": cpqSsBackplanePlacement,
       "cpqSsBackplaneBoardRevision": cpqSsBackplaneBoardRevision,
       "cpqSsBackplaneSpeed": cpqSsBackplaneSpeed,
       "cpqSsBackplaneConnectionType": cpqSsBackplaneConnectionType,
       "cpqSsBackplaneConnector": cpqSsBackplaneConnector,
       "cpqSsBackplaneOnConnector": cpqSsBackplaneOnConnector,
       "cpqSsBackplaneLocationString": cpqSsBackplaneLocationString,
       "cpqSsFibreAttachmentTable": cpqSsFibreAttachmentTable,
       "cpqSsFibreAttachmentEntry": cpqSsFibreAttachmentEntry,
       "cpqSsFibreAttachmentIndex": cpqSsFibreAttachmentIndex,
       "cpqSsFibreAttachmentHostControllerIndex": cpqSsFibreAttachmentHostControllerIndex,
       "cpqSsFibreAttachmentHostControllerPort": cpqSsFibreAttachmentHostControllerPort,
       "cpqSsFibreAttachmentDeviceType": cpqSsFibreAttachmentDeviceType,
       "cpqSsFibreAttachmentDeviceIndex": cpqSsFibreAttachmentDeviceIndex,
       "cpqSsFibreAttachmentDevicePort": cpqSsFibreAttachmentDevicePort,
       "cpqSsScsiAttachmentTable": cpqSsScsiAttachmentTable,
       "cpqSsScsiAttachmentEntry": cpqSsScsiAttachmentEntry,
       "cpqSsScsiAttachmentIndex": cpqSsScsiAttachmentIndex,
       "cpqSsScsiAttachmentControllerIndex": cpqSsScsiAttachmentControllerIndex,
       "cpqSsScsiAttachmentControllerPort": cpqSsScsiAttachmentControllerPort,
       "cpqSsScsiAttachmentControllerTarget": cpqSsScsiAttachmentControllerTarget,
       "cpqSsScsiAttachmentControllerLun": cpqSsScsiAttachmentControllerLun,
       "cpqSsScsiAttachmentChassisIndex": cpqSsScsiAttachmentChassisIndex,
       "cpqSsScsiAttachmentChassisIoSlot": cpqSsScsiAttachmentChassisIoSlot,
       "cpqSsScsiAttachmentPathStatus": cpqSsScsiAttachmentPathStatus,
       "cpqSsScsiAttachmentPathCondition": cpqSsScsiAttachmentPathCondition,
       "cpqSsDrvBoxPathTable": cpqSsDrvBoxPathTable,
       "cpqSsDrvBoxPathEntry": cpqSsDrvBoxPathEntry,
       "cpqSsDrvBoxPathCntlrIndex": cpqSsDrvBoxPathCntlrIndex,
       "cpqSsDrvBoxPathBoxIndex": cpqSsDrvBoxPathBoxIndex,
       "cpqSsDrvBoxPathIndex": cpqSsDrvBoxPathIndex,
       "cpqSsDrvBoxPathStatus": cpqSsDrvBoxPathStatus,
       "cpqSsDrvBoxPathCurrentRole": cpqSsDrvBoxPathCurrentRole,
       "cpqSsDrvBoxPathHostConnector": cpqSsDrvBoxPathHostConnector,
       "cpqSsDrvBoxPathBoxOnConnector": cpqSsDrvBoxPathBoxOnConnector,
       "cpqSsDrvBoxPathLocationString": cpqSsDrvBoxPathLocationString,
       "cpqSsTrap": cpqSsTrap,
       "cpqSsTrapPkts": cpqSsTrapPkts,
       "cpqSsTrapLogMaxSize": cpqSsTrapLogMaxSize,
       "cpqSsTrapLogTable": cpqSsTrapLogTable,
       "cpqSsTrapLogEntry": cpqSsTrapLogEntry,
       "cpqSsTrapLogIndex": cpqSsTrapLogIndex,
       "cpqSsTrapType": cpqSsTrapType,
       "cpqSsTrapTime": cpqSsTrapTime,
       "cpqSsRaidSystem": cpqSsRaidSystem,
       "cpqSsRaidSystemTable": cpqSsRaidSystemTable,
       "cpqSsRaidSystemEntry": cpqSsRaidSystemEntry,
       "cpqSsRaidSystemIndex": cpqSsRaidSystemIndex,
       "cpqSsRaidSystemName": cpqSsRaidSystemName,
       "cpqSsRaidSystemStatus": cpqSsRaidSystemStatus,
       "cpqSsRaidSystemCondition": cpqSsRaidSystemCondition,
       "cpqSsRaidSystemCntlr1SerialNumber": cpqSsRaidSystemCntlr1SerialNumber,
       "cpqSsRaidSystemCntlr2SerialNumber": cpqSsRaidSystemCntlr2SerialNumber}
)
