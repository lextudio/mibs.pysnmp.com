# SNMP MIB module (BIANCA-BRICK-HDSL2SHDSL2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-HDSL2SHDSL2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:27 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "enterprises",
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

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Hdsl2shdsl_ObjectIdentity = ObjectIdentity
hdsl2shdsl = _Hdsl2shdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 35)
)
_Hdsl2ShdslLineMib_ObjectIdentity = ObjectIdentity
hdsl2ShdslLineMib = _Hdsl2ShdslLineMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1)
)
_Hdsl2ShdslMibObjects_ObjectIdentity = ObjectIdentity
hdsl2ShdslMibObjects = _Hdsl2ShdslMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1)
)
_Hdsl2ShdslInventoryTable_Object = MibTable
hdsl2ShdslInventoryTable = _Hdsl2ShdslInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hdsl2ShdslInventoryTable.setStatus("mandatory")
_Hdsl2ShdslInventoryEntry_Object = MibTableRow
hdsl2ShdslInventoryEntry = _Hdsl2ShdslInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1)
)
hdsl2ShdslInventoryEntry.setIndexNames(
    (0, "BIANCA-BRICK-HDSL2SHDSL2-MIB", "hdsl2ShdslInvIfIndex"),
)
if mibBuilder.loadTexts:
    hdsl2ShdslInventoryEntry.setStatus("mandatory")
_Hdsl2ShdslInvIfIndex_Type = Integer32
_Hdsl2ShdslInvIfIndex_Object = MibTableColumn
hdsl2ShdslInvIfIndex = _Hdsl2ShdslInvIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1, 1),
    _Hdsl2ShdslInvIfIndex_Type()
)
hdsl2ShdslInvIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvIfIndex.setStatus("mandatory")


class _Hdsl2ShdslInvIndex_Type(Integer32):
    """Custom type hdsl2ShdslInvIndex based on Integer32"""
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
        *(("xru1", 3),
          ("xru2", 4),
          ("xru3", 5),
          ("xru4", 6),
          ("xru5", 7),
          ("xru6", 8),
          ("xru7", 9),
          ("xru8", 10),
          ("xtuC", 1),
          ("xtuR", 2))
    )


_Hdsl2ShdslInvIndex_Type.__name__ = "Integer32"
_Hdsl2ShdslInvIndex_Object = MibTableColumn
hdsl2ShdslInvIndex = _Hdsl2ShdslInvIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1, 2),
    _Hdsl2ShdslInvIndex_Type()
)
hdsl2ShdslInvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvIndex.setStatus("mandatory")


class _Hdsl2ShdslInvVendorID_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hdsl2ShdslInvVendorID_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorID_Object = MibTableColumn
hdsl2ShdslInvVendorID = _Hdsl2ShdslInvVendorID_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1, 3),
    _Hdsl2ShdslInvVendorID_Type()
)
hdsl2ShdslInvVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorID.setStatus("mandatory")


class _Hdsl2ShdslInvVendorModelNumber_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorModelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Hdsl2ShdslInvVendorModelNumber_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorModelNumber_Object = MibTableColumn
hdsl2ShdslInvVendorModelNumber = _Hdsl2ShdslInvVendorModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1, 4),
    _Hdsl2ShdslInvVendorModelNumber_Type()
)
hdsl2ShdslInvVendorModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorModelNumber.setStatus("mandatory")


class _Hdsl2ShdslInvVendorSerialNumber_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Hdsl2ShdslInvVendorSerialNumber_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorSerialNumber_Object = MibTableColumn
hdsl2ShdslInvVendorSerialNumber = _Hdsl2ShdslInvVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1, 5),
    _Hdsl2ShdslInvVendorSerialNumber_Type()
)
hdsl2ShdslInvVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorSerialNumber.setStatus("mandatory")
_Hdsl2ShdslInvVendorEOCSoftwareVersion_Type = Integer32
_Hdsl2ShdslInvVendorEOCSoftwareVersion_Object = MibTableColumn
hdsl2ShdslInvVendorEOCSoftwareVersion = _Hdsl2ShdslInvVendorEOCSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1, 6),
    _Hdsl2ShdslInvVendorEOCSoftwareVersion_Type()
)
hdsl2ShdslInvVendorEOCSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorEOCSoftwareVersion.setStatus("mandatory")
_Hdsl2ShdslInvStandardVersion_Type = Integer32
_Hdsl2ShdslInvStandardVersion_Object = MibTableColumn
hdsl2ShdslInvStandardVersion = _Hdsl2ShdslInvStandardVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1, 7),
    _Hdsl2ShdslInvStandardVersion_Type()
)
hdsl2ShdslInvStandardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvStandardVersion.setStatus("mandatory")


class _Hdsl2ShdslInvVendorListNumber_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorListNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Hdsl2ShdslInvVendorListNumber_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorListNumber_Object = MibTableColumn
hdsl2ShdslInvVendorListNumber = _Hdsl2ShdslInvVendorListNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1, 8),
    _Hdsl2ShdslInvVendorListNumber_Type()
)
hdsl2ShdslInvVendorListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorListNumber.setStatus("mandatory")


class _Hdsl2ShdslInvVendorIssueNumber_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorIssueNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hdsl2ShdslInvVendorIssueNumber_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorIssueNumber_Object = MibTableColumn
hdsl2ShdslInvVendorIssueNumber = _Hdsl2ShdslInvVendorIssueNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1, 9),
    _Hdsl2ShdslInvVendorIssueNumber_Type()
)
hdsl2ShdslInvVendorIssueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorIssueNumber.setStatus("mandatory")


class _Hdsl2ShdslInvVendorSoftwareVersion_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Hdsl2ShdslInvVendorSoftwareVersion_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorSoftwareVersion_Object = MibTableColumn
hdsl2ShdslInvVendorSoftwareVersion = _Hdsl2ShdslInvVendorSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1, 10),
    _Hdsl2ShdslInvVendorSoftwareVersion_Type()
)
hdsl2ShdslInvVendorSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorSoftwareVersion.setStatus("mandatory")


class _Hdsl2ShdslInvEquipmentCode_Type(OctetString):
    """Custom type hdsl2ShdslInvEquipmentCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Hdsl2ShdslInvEquipmentCode_Type.__name__ = "OctetString"
_Hdsl2ShdslInvEquipmentCode_Object = MibTableColumn
hdsl2ShdslInvEquipmentCode = _Hdsl2ShdslInvEquipmentCode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1, 11),
    _Hdsl2ShdslInvEquipmentCode_Type()
)
hdsl2ShdslInvEquipmentCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvEquipmentCode.setStatus("mandatory")


class _Hdsl2ShdslInvVendorOther_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorOther based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Hdsl2ShdslInvVendorOther_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorOther_Object = MibTableColumn
hdsl2ShdslInvVendorOther = _Hdsl2ShdslInvVendorOther_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1, 12),
    _Hdsl2ShdslInvVendorOther_Type()
)
hdsl2ShdslInvVendorOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorOther.setStatus("mandatory")


class _Hdsl2ShdslInvTransmissionModeCapability_Type(Integer32):
    """Custom type hdsl2ShdslInvTransmissionModeCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("region1", 1),
          ("region2", 2))
    )


_Hdsl2ShdslInvTransmissionModeCapability_Type.__name__ = "Integer32"
_Hdsl2ShdslInvTransmissionModeCapability_Object = MibTableColumn
hdsl2ShdslInvTransmissionModeCapability = _Hdsl2ShdslInvTransmissionModeCapability_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 3, 1, 13),
    _Hdsl2ShdslInvTransmissionModeCapability_Type()
)
hdsl2ShdslInvTransmissionModeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvTransmissionModeCapability.setStatus("mandatory")
_Hdsl2ShdslEndpointConfTable_Object = MibTable
hdsl2ShdslEndpointConfTable = _Hdsl2ShdslEndpointConfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfTable.setStatus("mandatory")
_Hdsl2ShdslEndpointConfEntry_Object = MibTableRow
hdsl2ShdslEndpointConfEntry = _Hdsl2ShdslEndpointConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1)
)
hdsl2ShdslEndpointConfEntry.setIndexNames(
    (0, "BIANCA-BRICK-HDSL2SHDSL2-MIB", "hdsl2ShdslEndpointConfIfIndex"),
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfEntry.setStatus("mandatory")
_Hdsl2ShdslEndpointConfIfIndex_Type = Integer32
_Hdsl2ShdslEndpointConfIfIndex_Object = MibTableColumn
hdsl2ShdslEndpointConfIfIndex = _Hdsl2ShdslEndpointConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 1),
    _Hdsl2ShdslEndpointConfIfIndex_Type()
)
hdsl2ShdslEndpointConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfIfIndex.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfSide_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfSide based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("customerSide", 2),
          ("networkSide", 1))
    )


_Hdsl2ShdslEndpointConfSide_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfSide_Object = MibTableColumn
hdsl2ShdslEndpointConfSide = _Hdsl2ShdslEndpointConfSide_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 2),
    _Hdsl2ShdslEndpointConfSide_Type()
)
hdsl2ShdslEndpointConfSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfSide.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfWireInterface_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfWireInterface based on Integer32"""
    defaultValue = 1

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
        *(("eightWire", 7),
          ("eightWireEFM", 14),
          ("eightWireIMA", 8),
          ("fourWire", 2),
          ("fourWireEFM", 12),
          ("fourWireIMA", 4),
          ("fourWireStandard", 3),
          ("groupMember", 10),
          ("not-used", 9),
          ("sixWire", 5),
          ("sixWireEFM", 13),
          ("sixWireIMA", 6),
          ("twoWire", 1),
          ("twoWireEFM", 11))
    )


_Hdsl2ShdslEndpointConfWireInterface_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfWireInterface_Object = MibTableColumn
hdsl2ShdslEndpointConfWireInterface = _Hdsl2ShdslEndpointConfWireInterface_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 5),
    _Hdsl2ShdslEndpointConfWireInterface_Type()
)
hdsl2ShdslEndpointConfWireInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfWireInterface.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfMinLineRate_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfMinLineRate based on Integer32"""
    defaultValue = 1552000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 22784000),
    )


_Hdsl2ShdslEndpointConfMinLineRate_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfMinLineRate_Object = MibTableColumn
hdsl2ShdslEndpointConfMinLineRate = _Hdsl2ShdslEndpointConfMinLineRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 6),
    _Hdsl2ShdslEndpointConfMinLineRate_Type()
)
hdsl2ShdslEndpointConfMinLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfMinLineRate.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfMaxLineRate_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfMaxLineRate based on Integer32"""
    defaultValue = 1552000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 22784000),
    )


_Hdsl2ShdslEndpointConfMaxLineRate_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfMaxLineRate_Object = MibTableColumn
hdsl2ShdslEndpointConfMaxLineRate = _Hdsl2ShdslEndpointConfMaxLineRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 7),
    _Hdsl2ShdslEndpointConfMaxLineRate_Type()
)
hdsl2ShdslEndpointConfMaxLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfMaxLineRate.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfTransmissionMode_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfTransmissionMode based on Integer32"""
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
        *(("region1", 1),
          ("region1or2", 3),
          ("region2", 2))
    )


_Hdsl2ShdslEndpointConfTransmissionMode_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfTransmissionMode_Object = MibTableColumn
hdsl2ShdslEndpointConfTransmissionMode = _Hdsl2ShdslEndpointConfTransmissionMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 8),
    _Hdsl2ShdslEndpointConfTransmissionMode_Type()
)
hdsl2ShdslEndpointConfTransmissionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfTransmissionMode.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfWorstCaseTargetMarginDown_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfWorstCaseTargetMarginDown based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hdsl2ShdslEndpointConfWorstCaseTargetMarginDown_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfWorstCaseTargetMarginDown_Object = MibTableColumn
hdsl2ShdslEndpointConfWorstCaseTargetMarginDown = _Hdsl2ShdslEndpointConfWorstCaseTargetMarginDown_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 11),
    _Hdsl2ShdslEndpointConfWorstCaseTargetMarginDown_Type()
)
hdsl2ShdslEndpointConfWorstCaseTargetMarginDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfWorstCaseTargetMarginDown.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfWorstCaseTargetMarginUp_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfWorstCaseTargetMarginUp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 21),
    )


_Hdsl2ShdslEndpointConfWorstCaseTargetMarginUp_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfWorstCaseTargetMarginUp_Object = MibTableColumn
hdsl2ShdslEndpointConfWorstCaseTargetMarginUp = _Hdsl2ShdslEndpointConfWorstCaseTargetMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 13),
    _Hdsl2ShdslEndpointConfWorstCaseTargetMarginUp_Type()
)
hdsl2ShdslEndpointConfWorstCaseTargetMarginUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfWorstCaseTargetMarginUp.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfGroupId_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfGroupId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hdsl2ShdslEndpointConfGroupId_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfGroupId_Object = MibTableColumn
hdsl2ShdslEndpointConfGroupId = _Hdsl2ShdslEndpointConfGroupId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 14),
    _Hdsl2ShdslEndpointConfGroupId_Type()
)
hdsl2ShdslEndpointConfGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfGroupId.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfLineProbeEnable_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfLineProbeEnable based on Integer32"""
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
        *(("auto", 1),
          ("disable", 2),
          ("enable", 3),
          ("enable-std", 4))
    )


_Hdsl2ShdslEndpointConfLineProbeEnable_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfLineProbeEnable_Object = MibTableColumn
hdsl2ShdslEndpointConfLineProbeEnable = _Hdsl2ShdslEndpointConfLineProbeEnable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 15),
    _Hdsl2ShdslEndpointConfLineProbeEnable_Type()
)
hdsl2ShdslEndpointConfLineProbeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfLineProbeEnable.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfLicenseUsage_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfLicenseUsage based on Integer32"""
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
        *(("missing", 2),
          ("none", 1),
          ("shdsl", 3))
    )


_Hdsl2ShdslEndpointConfLicenseUsage_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfLicenseUsage_Object = MibTableColumn
hdsl2ShdslEndpointConfLicenseUsage = _Hdsl2ShdslEndpointConfLicenseUsage_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 16),
    _Hdsl2ShdslEndpointConfLicenseUsage_Type()
)
hdsl2ShdslEndpointConfLicenseUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfLicenseUsage.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfPamMode_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfPamMode based on Integer32"""
    defaultValue = 48

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 252),
    )


_Hdsl2ShdslEndpointConfPamMode_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfPamMode_Object = MibTableColumn
hdsl2ShdslEndpointConfPamMode = _Hdsl2ShdslEndpointConfPamMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 17),
    _Hdsl2ShdslEndpointConfPamMode_Type()
)
hdsl2ShdslEndpointConfPamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfPamMode.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfTotalMinLineRate_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfTotalMinLineRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50000000),
    )


_Hdsl2ShdslEndpointConfTotalMinLineRate_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfTotalMinLineRate_Object = MibTableColumn
hdsl2ShdslEndpointConfTotalMinLineRate = _Hdsl2ShdslEndpointConfTotalMinLineRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 18),
    _Hdsl2ShdslEndpointConfTotalMinLineRate_Type()
)
hdsl2ShdslEndpointConfTotalMinLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfTotalMinLineRate.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfMinWirePairs_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfMinWirePairs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hdsl2ShdslEndpointConfMinWirePairs_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfMinWirePairs_Object = MibTableColumn
hdsl2ShdslEndpointConfMinWirePairs = _Hdsl2ShdslEndpointConfMinWirePairs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 19),
    _Hdsl2ShdslEndpointConfMinWirePairs_Type()
)
hdsl2ShdslEndpointConfMinWirePairs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfMinWirePairs.setStatus("mandatory")


class _Hdsl2ShdslEndpointConfCapListStyle_Type(Integer32):
    """Custom type hdsl2ShdslEndpointConfCapListStyle based on Integer32"""
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
        *(("auto", 1),
          ("new", 3),
          ("old", 2))
    )


_Hdsl2ShdslEndpointConfCapListStyle_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointConfCapListStyle_Object = MibTableColumn
hdsl2ShdslEndpointConfCapListStyle = _Hdsl2ShdslEndpointConfCapListStyle_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 4, 1, 20),
    _Hdsl2ShdslEndpointConfCapListStyle_Type()
)
hdsl2ShdslEndpointConfCapListStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfCapListStyle.setStatus("mandatory")
_Hdsl2ShdslEndpointCurrTable_Object = MibTable
hdsl2ShdslEndpointCurrTable = _Hdsl2ShdslEndpointCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrTable.setStatus("mandatory")
_Hdsl2ShdslEndpointCurrEntry_Object = MibTableRow
hdsl2ShdslEndpointCurrEntry = _Hdsl2ShdslEndpointCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1)
)
hdsl2ShdslEndpointCurrEntry.setIndexNames(
    (0, "BIANCA-BRICK-HDSL2SHDSL2-MIB", "hdsl2ShdslEndpointCurrIfIndex"),
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrEntry.setStatus("mandatory")
_Hdsl2ShdslEndpointCurrIfIndex_Type = Integer32
_Hdsl2ShdslEndpointCurrIfIndex_Object = MibTableColumn
hdsl2ShdslEndpointCurrIfIndex = _Hdsl2ShdslEndpointCurrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 1),
    _Hdsl2ShdslEndpointCurrIfIndex_Type()
)
hdsl2ShdslEndpointCurrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrIfIndex.setStatus("mandatory")
_Hdsl2ShdslEndpointCurrReceivedBlks_Type = Integer32
_Hdsl2ShdslEndpointCurrReceivedBlks_Object = MibTableColumn
hdsl2ShdslEndpointCurrReceivedBlks = _Hdsl2ShdslEndpointCurrReceivedBlks_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 2),
    _Hdsl2ShdslEndpointCurrReceivedBlks_Type()
)
hdsl2ShdslEndpointCurrReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrReceivedBlks.setStatus("mandatory")
_Hdsl2ShdslEndpointCurrTransmittedBlks_Type = Integer32
_Hdsl2ShdslEndpointCurrTransmittedBlks_Object = MibTableColumn
hdsl2ShdslEndpointCurrTransmittedBlks = _Hdsl2ShdslEndpointCurrTransmittedBlks_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 3),
    _Hdsl2ShdslEndpointCurrTransmittedBlks_Type()
)
hdsl2ShdslEndpointCurrTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrTransmittedBlks.setStatus("mandatory")
_Hdsl2ShdslEndpointCurrCorrectedBlks_Type = Integer32
_Hdsl2ShdslEndpointCurrCorrectedBlks_Object = MibTableColumn
hdsl2ShdslEndpointCurrCorrectedBlks = _Hdsl2ShdslEndpointCurrCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 4),
    _Hdsl2ShdslEndpointCurrCorrectedBlks_Type()
)
hdsl2ShdslEndpointCurrCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrCorrectedBlks.setStatus("mandatory")
_Hdsl2ShdslEndpointCurrUncorrectBlks_Type = Integer32
_Hdsl2ShdslEndpointCurrUncorrectBlks_Object = MibTableColumn
hdsl2ShdslEndpointCurrUncorrectBlks = _Hdsl2ShdslEndpointCurrUncorrectBlks_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 5),
    _Hdsl2ShdslEndpointCurrUncorrectBlks_Type()
)
hdsl2ShdslEndpointCurrUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrUncorrectBlks.setStatus("mandatory")


class _Hdsl2ShdslEndpointCurrAtn_Type(Integer32):
    """Custom type hdsl2ShdslEndpointCurrAtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_Hdsl2ShdslEndpointCurrAtn_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointCurrAtn_Object = MibTableColumn
hdsl2ShdslEndpointCurrAtn = _Hdsl2ShdslEndpointCurrAtn_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 6),
    _Hdsl2ShdslEndpointCurrAtn_Type()
)
hdsl2ShdslEndpointCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrAtn.setStatus("mandatory")


class _Hdsl2ShdslEndpointCurrSnrMgn_Type(Integer32):
    """Custom type hdsl2ShdslEndpointCurrSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_Hdsl2ShdslEndpointCurrSnrMgn_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointCurrSnrMgn_Object = MibTableColumn
hdsl2ShdslEndpointCurrSnrMgn = _Hdsl2ShdslEndpointCurrSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 7),
    _Hdsl2ShdslEndpointCurrSnrMgn_Type()
)
hdsl2ShdslEndpointCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrSnrMgn.setStatus("mandatory")


class _Hdsl2ShdslEndpointCurrStatus_Type(Integer32):
    """Custom type hdsl2ShdslEndpointCurrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("configInitFailure", 8),
          ("dcContinuityFault", 4),
          ("deviceFault", 3),
          ("loopbackActive", 11),
          ("loswFailureAlarm", 7),
          ("noDefect", 1),
          ("noNeighborPresent", 10),
          ("powerBackoff", 2),
          ("protocolInitFailure", 9),
          ("snrMarginAlarm", 5))
    )


_Hdsl2ShdslEndpointCurrStatus_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointCurrStatus_Object = MibTableColumn
hdsl2ShdslEndpointCurrStatus = _Hdsl2ShdslEndpointCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 8),
    _Hdsl2ShdslEndpointCurrStatus_Type()
)
hdsl2ShdslEndpointCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrStatus.setStatus("mandatory")
_Hdsl2ShdslEndpointES_Type = Counter32
_Hdsl2ShdslEndpointES_Object = MibTableColumn
hdsl2ShdslEndpointES = _Hdsl2ShdslEndpointES_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 9),
    _Hdsl2ShdslEndpointES_Type()
)
hdsl2ShdslEndpointES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointES.setStatus("mandatory")
_Hdsl2ShdslEndpointSES_Type = Counter32
_Hdsl2ShdslEndpointSES_Object = MibTableColumn
hdsl2ShdslEndpointSES = _Hdsl2ShdslEndpointSES_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 10),
    _Hdsl2ShdslEndpointSES_Type()
)
hdsl2ShdslEndpointSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointSES.setStatus("mandatory")
_Hdsl2ShdslEndpointCRCanomalies_Type = Counter32
_Hdsl2ShdslEndpointCRCanomalies_Object = MibTableColumn
hdsl2ShdslEndpointCRCanomalies = _Hdsl2ShdslEndpointCRCanomalies_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 11),
    _Hdsl2ShdslEndpointCRCanomalies_Type()
)
hdsl2ShdslEndpointCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCRCanomalies.setStatus("mandatory")
_Hdsl2ShdslEndpointLOSWS_Type = Counter32
_Hdsl2ShdslEndpointLOSWS_Object = MibTableColumn
hdsl2ShdslEndpointLOSWS = _Hdsl2ShdslEndpointLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 12),
    _Hdsl2ShdslEndpointLOSWS_Type()
)
hdsl2ShdslEndpointLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointLOSWS.setStatus("mandatory")
_Hdsl2ShdslEndpointUAS_Type = Counter32
_Hdsl2ShdslEndpointUAS_Object = MibTableColumn
hdsl2ShdslEndpointUAS = _Hdsl2ShdslEndpointUAS_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 13),
    _Hdsl2ShdslEndpointUAS_Type()
)
hdsl2ShdslEndpointUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointUAS.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr15MinReceivedBlks_Type = Integer32
_Hdsl2ShdslEndpointCurr15MinReceivedBlks_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinReceivedBlks = _Hdsl2ShdslEndpointCurr15MinReceivedBlks_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 14),
    _Hdsl2ShdslEndpointCurr15MinReceivedBlks_Type()
)
hdsl2ShdslEndpointCurr15MinReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinReceivedBlks.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr15MinTransmittedBlks_Type = Integer32
_Hdsl2ShdslEndpointCurr15MinTransmittedBlks_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinTransmittedBlks = _Hdsl2ShdslEndpointCurr15MinTransmittedBlks_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 15),
    _Hdsl2ShdslEndpointCurr15MinTransmittedBlks_Type()
)
hdsl2ShdslEndpointCurr15MinTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinTransmittedBlks.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr15MinCorrectedBlks_Type = Integer32
_Hdsl2ShdslEndpointCurr15MinCorrectedBlks_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinCorrectedBlks = _Hdsl2ShdslEndpointCurr15MinCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 16),
    _Hdsl2ShdslEndpointCurr15MinCorrectedBlks_Type()
)
hdsl2ShdslEndpointCurr15MinCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinCorrectedBlks.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr15MinUncorrectBlks_Type = Integer32
_Hdsl2ShdslEndpointCurr15MinUncorrectBlks_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinUncorrectBlks = _Hdsl2ShdslEndpointCurr15MinUncorrectBlks_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 17),
    _Hdsl2ShdslEndpointCurr15MinUncorrectBlks_Type()
)
hdsl2ShdslEndpointCurr15MinUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinUncorrectBlks.setStatus("mandatory")


class _Hdsl2ShdslEndpointCurr15MinTimeElapsed_Type(Integer32):
    """Custom type hdsl2ShdslEndpointCurr15MinTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_Hdsl2ShdslEndpointCurr15MinTimeElapsed_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointCurr15MinTimeElapsed_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinTimeElapsed = _Hdsl2ShdslEndpointCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 18),
    _Hdsl2ShdslEndpointCurr15MinTimeElapsed_Type()
)
hdsl2ShdslEndpointCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinTimeElapsed.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr15MinES_Type = Integer32
_Hdsl2ShdslEndpointCurr15MinES_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinES = _Hdsl2ShdslEndpointCurr15MinES_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 19),
    _Hdsl2ShdslEndpointCurr15MinES_Type()
)
hdsl2ShdslEndpointCurr15MinES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinES.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr15MinSES_Type = Integer32
_Hdsl2ShdslEndpointCurr15MinSES_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinSES = _Hdsl2ShdslEndpointCurr15MinSES_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 20),
    _Hdsl2ShdslEndpointCurr15MinSES_Type()
)
hdsl2ShdslEndpointCurr15MinSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinSES.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr15MinCRCanomalies_Type = Integer32
_Hdsl2ShdslEndpointCurr15MinCRCanomalies_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinCRCanomalies = _Hdsl2ShdslEndpointCurr15MinCRCanomalies_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 21),
    _Hdsl2ShdslEndpointCurr15MinCRCanomalies_Type()
)
hdsl2ShdslEndpointCurr15MinCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinCRCanomalies.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr15MinLOSWS_Type = Integer32
_Hdsl2ShdslEndpointCurr15MinLOSWS_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinLOSWS = _Hdsl2ShdslEndpointCurr15MinLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 22),
    _Hdsl2ShdslEndpointCurr15MinLOSWS_Type()
)
hdsl2ShdslEndpointCurr15MinLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinLOSWS.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr15MinUAS_Type = Integer32
_Hdsl2ShdslEndpointCurr15MinUAS_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinUAS = _Hdsl2ShdslEndpointCurr15MinUAS_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 23),
    _Hdsl2ShdslEndpointCurr15MinUAS_Type()
)
hdsl2ShdslEndpointCurr15MinUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinUAS.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr1DayReceivedBlks_Type = Integer32
_Hdsl2ShdslEndpointCurr1DayReceivedBlks_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayReceivedBlks = _Hdsl2ShdslEndpointCurr1DayReceivedBlks_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 24),
    _Hdsl2ShdslEndpointCurr1DayReceivedBlks_Type()
)
hdsl2ShdslEndpointCurr1DayReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayReceivedBlks.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr1DayTransmittedBlks_Type = Integer32
_Hdsl2ShdslEndpointCurr1DayTransmittedBlks_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayTransmittedBlks = _Hdsl2ShdslEndpointCurr1DayTransmittedBlks_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 25),
    _Hdsl2ShdslEndpointCurr1DayTransmittedBlks_Type()
)
hdsl2ShdslEndpointCurr1DayTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayTransmittedBlks.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr1DayCorrectedBlks_Type = Integer32
_Hdsl2ShdslEndpointCurr1DayCorrectedBlks_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayCorrectedBlks = _Hdsl2ShdslEndpointCurr1DayCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 26),
    _Hdsl2ShdslEndpointCurr1DayCorrectedBlks_Type()
)
hdsl2ShdslEndpointCurr1DayCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayCorrectedBlks.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr1DayUncorrectBlks_Type = Integer32
_Hdsl2ShdslEndpointCurr1DayUncorrectBlks_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayUncorrectBlks = _Hdsl2ShdslEndpointCurr1DayUncorrectBlks_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 27),
    _Hdsl2ShdslEndpointCurr1DayUncorrectBlks_Type()
)
hdsl2ShdslEndpointCurr1DayUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayUncorrectBlks.setStatus("mandatory")


class _Hdsl2ShdslEndpointCurr1DayTimeElapsed_Type(Integer32):
    """Custom type hdsl2ShdslEndpointCurr1DayTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_Hdsl2ShdslEndpointCurr1DayTimeElapsed_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointCurr1DayTimeElapsed_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayTimeElapsed = _Hdsl2ShdslEndpointCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 28),
    _Hdsl2ShdslEndpointCurr1DayTimeElapsed_Type()
)
hdsl2ShdslEndpointCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayTimeElapsed.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr1DayES_Type = Integer32
_Hdsl2ShdslEndpointCurr1DayES_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayES = _Hdsl2ShdslEndpointCurr1DayES_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 29),
    _Hdsl2ShdslEndpointCurr1DayES_Type()
)
hdsl2ShdslEndpointCurr1DayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayES.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr1DaySES_Type = Integer32
_Hdsl2ShdslEndpointCurr1DaySES_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DaySES = _Hdsl2ShdslEndpointCurr1DaySES_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 30),
    _Hdsl2ShdslEndpointCurr1DaySES_Type()
)
hdsl2ShdslEndpointCurr1DaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DaySES.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr1DayCRCanomalies_Type = Integer32
_Hdsl2ShdslEndpointCurr1DayCRCanomalies_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayCRCanomalies = _Hdsl2ShdslEndpointCurr1DayCRCanomalies_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 31),
    _Hdsl2ShdslEndpointCurr1DayCRCanomalies_Type()
)
hdsl2ShdslEndpointCurr1DayCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayCRCanomalies.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr1DayLOSWS_Type = Integer32
_Hdsl2ShdslEndpointCurr1DayLOSWS_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayLOSWS = _Hdsl2ShdslEndpointCurr1DayLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 32),
    _Hdsl2ShdslEndpointCurr1DayLOSWS_Type()
)
hdsl2ShdslEndpointCurr1DayLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayLOSWS.setStatus("mandatory")
_Hdsl2ShdslEndpointCurr1DayUAS_Type = Integer32
_Hdsl2ShdslEndpointCurr1DayUAS_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayUAS = _Hdsl2ShdslEndpointCurr1DayUAS_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 5, 1, 33),
    _Hdsl2ShdslEndpointCurr1DayUAS_Type()
)
hdsl2ShdslEndpointCurr1DayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayUAS.setStatus("mandatory")
_Hdsl2ShdslSpanConfProfileTable_Object = MibTable
hdsl2ShdslSpanConfProfileTable = _Hdsl2ShdslSpanConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfProfileTable.setStatus("mandatory")
_Hdsl2ShdslSpanConfProfileEntry_Object = MibTableRow
hdsl2ShdslSpanConfProfileEntry = _Hdsl2ShdslSpanConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 10, 1)
)
hdsl2ShdslSpanConfProfileEntry.setIndexNames(
    (0, "BIANCA-BRICK-HDSL2SHDSL2-MIB", "hdsl2ShdslSpanConfProfileName"),
)
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfProfileEntry.setStatus("mandatory")


class _Hdsl2ShdslSpanConfProfileName_Type(DisplayString):
    """Custom type hdsl2ShdslSpanConfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hdsl2ShdslSpanConfProfileName_Type.__name__ = "DisplayString"
_Hdsl2ShdslSpanConfProfileName_Object = MibTableColumn
hdsl2ShdslSpanConfProfileName = _Hdsl2ShdslSpanConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 10, 1, 1),
    _Hdsl2ShdslSpanConfProfileName_Type()
)
hdsl2ShdslSpanConfProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfProfileName.setStatus("mandatory")


class _Hdsl2ShdslSpanConfWireInterface_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfWireInterface based on Integer32"""
    defaultValue = 1

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
        *(("eightWire", 7),
          ("eightWireEFM", 14),
          ("eightWireIMA", 8),
          ("fourWire", 2),
          ("fourWireEFM", 12),
          ("fourWireIMA", 4),
          ("fourWireStandard", 3),
          ("groupMember", 10),
          ("not-used", 9),
          ("sixWire", 5),
          ("sixWireEFM", 13),
          ("sixWireIMA", 6),
          ("twoWire", 1),
          ("twoWireEFM", 11))
    )


_Hdsl2ShdslSpanConfWireInterface_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfWireInterface_Object = MibTableColumn
hdsl2ShdslSpanConfWireInterface = _Hdsl2ShdslSpanConfWireInterface_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 10, 1, 2),
    _Hdsl2ShdslSpanConfWireInterface_Type()
)
hdsl2ShdslSpanConfWireInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfWireInterface.setStatus("mandatory")


class _Hdsl2ShdslSpanConfMinLineRate_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfMinLineRate based on Integer32"""
    defaultValue = 1552000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 22784000),
    )


_Hdsl2ShdslSpanConfMinLineRate_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfMinLineRate_Object = MibTableColumn
hdsl2ShdslSpanConfMinLineRate = _Hdsl2ShdslSpanConfMinLineRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 10, 1, 3),
    _Hdsl2ShdslSpanConfMinLineRate_Type()
)
hdsl2ShdslSpanConfMinLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfMinLineRate.setStatus("mandatory")


class _Hdsl2ShdslSpanConfMaxLineRate_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfMaxLineRate based on Integer32"""
    defaultValue = 1552000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 22784000),
    )


_Hdsl2ShdslSpanConfMaxLineRate_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfMaxLineRate_Object = MibTableColumn
hdsl2ShdslSpanConfMaxLineRate = _Hdsl2ShdslSpanConfMaxLineRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 10, 1, 4),
    _Hdsl2ShdslSpanConfMaxLineRate_Type()
)
hdsl2ShdslSpanConfMaxLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfMaxLineRate.setStatus("mandatory")


class _Hdsl2ShdslSpanConfTransmissionMode_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfTransmissionMode based on Integer32"""
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
        *(("region1", 1),
          ("region1or2", 3),
          ("region2", 2))
    )


_Hdsl2ShdslSpanConfTransmissionMode_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfTransmissionMode_Object = MibTableColumn
hdsl2ShdslSpanConfTransmissionMode = _Hdsl2ShdslSpanConfTransmissionMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 10, 1, 6),
    _Hdsl2ShdslSpanConfTransmissionMode_Type()
)
hdsl2ShdslSpanConfTransmissionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfTransmissionMode.setStatus("mandatory")


class _Hdsl2ShdslSpanConfWorstCaseTargetMarginDown_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfWorstCaseTargetMarginDown based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hdsl2ShdslSpanConfWorstCaseTargetMarginDown_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfWorstCaseTargetMarginDown_Object = MibTableColumn
hdsl2ShdslSpanConfWorstCaseTargetMarginDown = _Hdsl2ShdslSpanConfWorstCaseTargetMarginDown_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 10, 1, 10),
    _Hdsl2ShdslSpanConfWorstCaseTargetMarginDown_Type()
)
hdsl2ShdslSpanConfWorstCaseTargetMarginDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfWorstCaseTargetMarginDown.setStatus("mandatory")


class _Hdsl2ShdslSpanConfWorstCaseTargetMarginUp_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfWorstCaseTargetMarginUp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 21),
    )


_Hdsl2ShdslSpanConfWorstCaseTargetMarginUp_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfWorstCaseTargetMarginUp_Object = MibTableColumn
hdsl2ShdslSpanConfWorstCaseTargetMarginUp = _Hdsl2ShdslSpanConfWorstCaseTargetMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 35, 1, 1, 10, 1, 12),
    _Hdsl2ShdslSpanConfWorstCaseTargetMarginUp_Type()
)
hdsl2ShdslSpanConfWorstCaseTargetMarginUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfWorstCaseTargetMarginUp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-HDSL2SHDSL2-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "hdsl2shdsl": hdsl2shdsl,
       "hdsl2ShdslLineMib": hdsl2ShdslLineMib,
       "hdsl2ShdslMibObjects": hdsl2ShdslMibObjects,
       "hdsl2ShdslInventoryTable": hdsl2ShdslInventoryTable,
       "hdsl2ShdslInventoryEntry": hdsl2ShdslInventoryEntry,
       "hdsl2ShdslInvIfIndex": hdsl2ShdslInvIfIndex,
       "hdsl2ShdslInvIndex": hdsl2ShdslInvIndex,
       "hdsl2ShdslInvVendorID": hdsl2ShdslInvVendorID,
       "hdsl2ShdslInvVendorModelNumber": hdsl2ShdslInvVendorModelNumber,
       "hdsl2ShdslInvVendorSerialNumber": hdsl2ShdslInvVendorSerialNumber,
       "hdsl2ShdslInvVendorEOCSoftwareVersion": hdsl2ShdslInvVendorEOCSoftwareVersion,
       "hdsl2ShdslInvStandardVersion": hdsl2ShdslInvStandardVersion,
       "hdsl2ShdslInvVendorListNumber": hdsl2ShdslInvVendorListNumber,
       "hdsl2ShdslInvVendorIssueNumber": hdsl2ShdslInvVendorIssueNumber,
       "hdsl2ShdslInvVendorSoftwareVersion": hdsl2ShdslInvVendorSoftwareVersion,
       "hdsl2ShdslInvEquipmentCode": hdsl2ShdslInvEquipmentCode,
       "hdsl2ShdslInvVendorOther": hdsl2ShdslInvVendorOther,
       "hdsl2ShdslInvTransmissionModeCapability": hdsl2ShdslInvTransmissionModeCapability,
       "hdsl2ShdslEndpointConfTable": hdsl2ShdslEndpointConfTable,
       "hdsl2ShdslEndpointConfEntry": hdsl2ShdslEndpointConfEntry,
       "hdsl2ShdslEndpointConfIfIndex": hdsl2ShdslEndpointConfIfIndex,
       "hdsl2ShdslEndpointConfSide": hdsl2ShdslEndpointConfSide,
       "hdsl2ShdslEndpointConfWireInterface": hdsl2ShdslEndpointConfWireInterface,
       "hdsl2ShdslEndpointConfMinLineRate": hdsl2ShdslEndpointConfMinLineRate,
       "hdsl2ShdslEndpointConfMaxLineRate": hdsl2ShdslEndpointConfMaxLineRate,
       "hdsl2ShdslEndpointConfTransmissionMode": hdsl2ShdslEndpointConfTransmissionMode,
       "hdsl2ShdslEndpointConfWorstCaseTargetMarginDown": hdsl2ShdslEndpointConfWorstCaseTargetMarginDown,
       "hdsl2ShdslEndpointConfWorstCaseTargetMarginUp": hdsl2ShdslEndpointConfWorstCaseTargetMarginUp,
       "hdsl2ShdslEndpointConfGroupId": hdsl2ShdslEndpointConfGroupId,
       "hdsl2ShdslEndpointConfLineProbeEnable": hdsl2ShdslEndpointConfLineProbeEnable,
       "hdsl2ShdslEndpointConfLicenseUsage": hdsl2ShdslEndpointConfLicenseUsage,
       "hdsl2ShdslEndpointConfPamMode": hdsl2ShdslEndpointConfPamMode,
       "hdsl2ShdslEndpointConfTotalMinLineRate": hdsl2ShdslEndpointConfTotalMinLineRate,
       "hdsl2ShdslEndpointConfMinWirePairs": hdsl2ShdslEndpointConfMinWirePairs,
       "hdsl2ShdslEndpointConfCapListStyle": hdsl2ShdslEndpointConfCapListStyle,
       "hdsl2ShdslEndpointCurrTable": hdsl2ShdslEndpointCurrTable,
       "hdsl2ShdslEndpointCurrEntry": hdsl2ShdslEndpointCurrEntry,
       "hdsl2ShdslEndpointCurrIfIndex": hdsl2ShdslEndpointCurrIfIndex,
       "hdsl2ShdslEndpointCurrReceivedBlks": hdsl2ShdslEndpointCurrReceivedBlks,
       "hdsl2ShdslEndpointCurrTransmittedBlks": hdsl2ShdslEndpointCurrTransmittedBlks,
       "hdsl2ShdslEndpointCurrCorrectedBlks": hdsl2ShdslEndpointCurrCorrectedBlks,
       "hdsl2ShdslEndpointCurrUncorrectBlks": hdsl2ShdslEndpointCurrUncorrectBlks,
       "hdsl2ShdslEndpointCurrAtn": hdsl2ShdslEndpointCurrAtn,
       "hdsl2ShdslEndpointCurrSnrMgn": hdsl2ShdslEndpointCurrSnrMgn,
       "hdsl2ShdslEndpointCurrStatus": hdsl2ShdslEndpointCurrStatus,
       "hdsl2ShdslEndpointES": hdsl2ShdslEndpointES,
       "hdsl2ShdslEndpointSES": hdsl2ShdslEndpointSES,
       "hdsl2ShdslEndpointCRCanomalies": hdsl2ShdslEndpointCRCanomalies,
       "hdsl2ShdslEndpointLOSWS": hdsl2ShdslEndpointLOSWS,
       "hdsl2ShdslEndpointUAS": hdsl2ShdslEndpointUAS,
       "hdsl2ShdslEndpointCurr15MinReceivedBlks": hdsl2ShdslEndpointCurr15MinReceivedBlks,
       "hdsl2ShdslEndpointCurr15MinTransmittedBlks": hdsl2ShdslEndpointCurr15MinTransmittedBlks,
       "hdsl2ShdslEndpointCurr15MinCorrectedBlks": hdsl2ShdslEndpointCurr15MinCorrectedBlks,
       "hdsl2ShdslEndpointCurr15MinUncorrectBlks": hdsl2ShdslEndpointCurr15MinUncorrectBlks,
       "hdsl2ShdslEndpointCurr15MinTimeElapsed": hdsl2ShdslEndpointCurr15MinTimeElapsed,
       "hdsl2ShdslEndpointCurr15MinES": hdsl2ShdslEndpointCurr15MinES,
       "hdsl2ShdslEndpointCurr15MinSES": hdsl2ShdslEndpointCurr15MinSES,
       "hdsl2ShdslEndpointCurr15MinCRCanomalies": hdsl2ShdslEndpointCurr15MinCRCanomalies,
       "hdsl2ShdslEndpointCurr15MinLOSWS": hdsl2ShdslEndpointCurr15MinLOSWS,
       "hdsl2ShdslEndpointCurr15MinUAS": hdsl2ShdslEndpointCurr15MinUAS,
       "hdsl2ShdslEndpointCurr1DayReceivedBlks": hdsl2ShdslEndpointCurr1DayReceivedBlks,
       "hdsl2ShdslEndpointCurr1DayTransmittedBlks": hdsl2ShdslEndpointCurr1DayTransmittedBlks,
       "hdsl2ShdslEndpointCurr1DayCorrectedBlks": hdsl2ShdslEndpointCurr1DayCorrectedBlks,
       "hdsl2ShdslEndpointCurr1DayUncorrectBlks": hdsl2ShdslEndpointCurr1DayUncorrectBlks,
       "hdsl2ShdslEndpointCurr1DayTimeElapsed": hdsl2ShdslEndpointCurr1DayTimeElapsed,
       "hdsl2ShdslEndpointCurr1DayES": hdsl2ShdslEndpointCurr1DayES,
       "hdsl2ShdslEndpointCurr1DaySES": hdsl2ShdslEndpointCurr1DaySES,
       "hdsl2ShdslEndpointCurr1DayCRCanomalies": hdsl2ShdslEndpointCurr1DayCRCanomalies,
       "hdsl2ShdslEndpointCurr1DayLOSWS": hdsl2ShdslEndpointCurr1DayLOSWS,
       "hdsl2ShdslEndpointCurr1DayUAS": hdsl2ShdslEndpointCurr1DayUAS,
       "hdsl2ShdslSpanConfProfileTable": hdsl2ShdslSpanConfProfileTable,
       "hdsl2ShdslSpanConfProfileEntry": hdsl2ShdslSpanConfProfileEntry,
       "hdsl2ShdslSpanConfProfileName": hdsl2ShdslSpanConfProfileName,
       "hdsl2ShdslSpanConfWireInterface": hdsl2ShdslSpanConfWireInterface,
       "hdsl2ShdslSpanConfMinLineRate": hdsl2ShdslSpanConfMinLineRate,
       "hdsl2ShdslSpanConfMaxLineRate": hdsl2ShdslSpanConfMaxLineRate,
       "hdsl2ShdslSpanConfTransmissionMode": hdsl2ShdslSpanConfTransmissionMode,
       "hdsl2ShdslSpanConfWorstCaseTargetMarginDown": hdsl2ShdslSpanConfWorstCaseTargetMarginDown,
       "hdsl2ShdslSpanConfWorstCaseTargetMarginUp": hdsl2ShdslSpanConfWorstCaseTargetMarginUp}
)
