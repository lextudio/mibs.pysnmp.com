# SNMP MIB module (BTI-OL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BTI-OL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:53 2024
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

(condCodeType,
 condDateAndTime,
 condDescription,
 condObjectType,
 condReportType,
 condServiceAffecting,
 condSeverity,
 evtCodeType,
 evtDateAndTime,
 evtDescription,
 evtObjectType,
 olCondNotifications,
 olEvtNotifications,
 opticalLayer,
 tcaDateAndTime,
 tcaIntervalType,
 tcaMontype,
 tcaThreshold,
 tcaValue,
 trapSeqNum) = mibBuilder.importSymbols(
    "BTI-7000-MIB",
    "condCodeType",
    "condDateAndTime",
    "condDescription",
    "condObjectType",
    "condReportType",
    "condServiceAffecting",
    "condSeverity",
    "evtCodeType",
    "evtDateAndTime",
    "evtDescription",
    "evtObjectType",
    "olCondNotifications",
    "olEvtNotifications",
    "opticalLayer",
    "tcaDateAndTime",
    "tcaIntervalType",
    "tcaMontype",
    "tcaThreshold",
    "tcaValue",
    "trapSeqNum")

(btiModules,) = mibBuilder.importSymbols(
    "BTI-MIB",
    "btiModules")

(AdminStatus,
 BERType,
 CpType,
 FiberType,
 FixedX10,
 FixedX100,
 HoursAndMinutes,
 InitializeCmd,
 OperStatQlfr,
 OperStatus,
 PMIntervalType,
 PMValidity) = mibBuilder.importSymbols(
    "BTI-TC-MIB",
    "AdminStatus",
    "BERType",
    "CpType",
    "FiberType",
    "FixedX10",
    "FixedX100",
    "HoursAndMinutes",
    "InitializeCmd",
    "OperStatQlfr",
    "OperStatus",
    "PMIntervalType",
    "PMValidity")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

olMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 1, 6)
)
olMib.setRevisions(
        ("2012-08-17 12:00",
         "2012-02-10 12:00",
         "2011-09-26 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OlGroupType(Integer32, TextualConvention):
    status = "current"
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
        *(("eqlzLine", 5),
          ("eqlzTerm", 3),
          ("noEqlzLine", 4),
          ("noEqlzTerm", 2),
          ("none", 1),
          ("roadm", 6))
    )



class OlPortType(Integer32, TextualConvention):
    status = "current"
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
        *(("channel", 4),
          ("client", 2),
          ("dcm", 3),
          ("expansion", 5),
          ("line", 1))
    )



# MIB Managed Objects in the order of their OIDs

_OlGroupTable_Object = MibTable
olGroupTable = _OlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 1)
)
if mibBuilder.loadTexts:
    olGroupTable.setStatus("current")
_OlGroupEntry_Object = MibTableRow
olGroupEntry = _OlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 1, 1)
)
olGroupEntry.setIndexNames(
    (0, "BTI-OL-MIB", "olGroupIdx"),
)
if mibBuilder.loadTexts:
    olGroupEntry.setStatus("current")


class _OlGroupIdx_Type(Integer32):
    """Custom type olGroupIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OlGroupIdx_Type.__name__ = "Integer32"
_OlGroupIdx_Object = MibTableColumn
olGroupIdx = _OlGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 1, 1, 1),
    _OlGroupIdx_Type()
)
olGroupIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olGroupIdx.setStatus("current")
_OlGroupType_Type = OlGroupType
_OlGroupType_Object = MibTableColumn
olGroupType = _OlGroupType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 1, 1, 2),
    _OlGroupType_Type()
)
olGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olGroupType.setStatus("current")


class _OlGroupId_Type(DisplayString):
    """Custom type olGroupId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlGroupId_Type.__name__ = "DisplayString"
_OlGroupId_Object = MibTableColumn
olGroupId = _OlGroupId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 1, 1, 3),
    _OlGroupId_Type()
)
olGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olGroupId.setStatus("current")
_OlGroupCustom1_Type = DisplayString
_OlGroupCustom1_Object = MibTableColumn
olGroupCustom1 = _OlGroupCustom1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 1, 1, 4),
    _OlGroupCustom1_Type()
)
olGroupCustom1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olGroupCustom1.setStatus("current")
_OlGroupCustom2_Type = DisplayString
_OlGroupCustom2_Object = MibTableColumn
olGroupCustom2 = _OlGroupCustom2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 1, 1, 5),
    _OlGroupCustom2_Type()
)
olGroupCustom2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olGroupCustom2.setStatus("current")
_OlGroupCustom3_Type = DisplayString
_OlGroupCustom3_Object = MibTableColumn
olGroupCustom3 = _OlGroupCustom3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 1, 1, 6),
    _OlGroupCustom3_Type()
)
olGroupCustom3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olGroupCustom3.setStatus("current")
_OlGroupRowStatus_Type = RowStatus
_OlGroupRowStatus_Object = MibTableColumn
olGroupRowStatus = _OlGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 1, 1, 100),
    _OlGroupRowStatus_Type()
)
olGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olGroupRowStatus.setStatus("current")
_OlEqptTable_Object = MibTable
olEqptTable = _OlEqptTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 3)
)
if mibBuilder.loadTexts:
    olEqptTable.setStatus("current")
_OlEqptEntry_Object = MibTableRow
olEqptEntry = _OlEqptEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 3, 1)
)
olEqptEntry.setIndexNames(
    (0, "BTI-OL-MIB", "olEqptCpTypeIdx"),
    (0, "BTI-OL-MIB", "olEqptShelfIdx"),
    (0, "BTI-OL-MIB", "olEqptSlotIdx"),
)
if mibBuilder.loadTexts:
    olEqptEntry.setStatus("current")
_OlEqptCpTypeIdx_Type = CpType
_OlEqptCpTypeIdx_Object = MibTableColumn
olEqptCpTypeIdx = _OlEqptCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 3, 1, 1),
    _OlEqptCpTypeIdx_Type()
)
olEqptCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olEqptCpTypeIdx.setStatus("current")


class _OlEqptShelfIdx_Type(Integer32):
    """Custom type olEqptShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_OlEqptShelfIdx_Type.__name__ = "Integer32"
_OlEqptShelfIdx_Object = MibTableColumn
olEqptShelfIdx = _OlEqptShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 3, 1, 2),
    _OlEqptShelfIdx_Type()
)
olEqptShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olEqptShelfIdx.setStatus("current")


class _OlEqptSlotIdx_Type(Integer32):
    """Custom type olEqptSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OlEqptSlotIdx_Type.__name__ = "Integer32"
_OlEqptSlotIdx_Object = MibTableColumn
olEqptSlotIdx = _OlEqptSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 3, 1, 3),
    _OlEqptSlotIdx_Type()
)
olEqptSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olEqptSlotIdx.setStatus("current")


class _OlEqptGroupNum_Type(Integer32):
    """Custom type olEqptGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OlEqptGroupNum_Type.__name__ = "Integer32"
_OlEqptGroupNum_Object = MibTableColumn
olEqptGroupNum = _OlEqptGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 3, 1, 4),
    _OlEqptGroupNum_Type()
)
olEqptGroupNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olEqptGroupNum.setStatus("current")


class _OlEqptDegreeNum_Type(Integer32):
    """Custom type olEqptDegreeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_OlEqptDegreeNum_Type.__name__ = "Integer32"
_OlEqptDegreeNum_Object = MibTableColumn
olEqptDegreeNum = _OlEqptDegreeNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 3, 1, 5),
    _OlEqptDegreeNum_Type()
)
olEqptDegreeNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olEqptDegreeNum.setStatus("current")
_OlEqptRowStatus_Type = RowStatus
_OlEqptRowStatus_Object = MibTableColumn
olEqptRowStatus = _OlEqptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 3, 1, 100),
    _OlEqptRowStatus_Type()
)
olEqptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olEqptRowStatus.setStatus("current")
_OlPortTable_Object = MibTable
olPortTable = _OlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4)
)
if mibBuilder.loadTexts:
    olPortTable.setStatus("current")
_OlPortEntry_Object = MibTableRow
olPortEntry = _OlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1)
)
olPortEntry.setIndexNames(
    (0, "BTI-OL-MIB", "olPortCpTypeIdx"),
    (0, "BTI-OL-MIB", "olPortShelfIdx"),
    (0, "BTI-OL-MIB", "olPortSlotIdx"),
    (0, "BTI-OL-MIB", "olPortTypeIdx"),
    (0, "BTI-OL-MIB", "olPortIdx"),
)
if mibBuilder.loadTexts:
    olPortEntry.setStatus("current")
_OlPortCpTypeIdx_Type = CpType
_OlPortCpTypeIdx_Object = MibTableColumn
olPortCpTypeIdx = _OlPortCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 1),
    _OlPortCpTypeIdx_Type()
)
olPortCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortCpTypeIdx.setStatus("current")


class _OlPortShelfIdx_Type(Integer32):
    """Custom type olPortShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_OlPortShelfIdx_Type.__name__ = "Integer32"
_OlPortShelfIdx_Object = MibTableColumn
olPortShelfIdx = _OlPortShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 2),
    _OlPortShelfIdx_Type()
)
olPortShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortShelfIdx.setStatus("current")


class _OlPortSlotIdx_Type(Integer32):
    """Custom type olPortSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OlPortSlotIdx_Type.__name__ = "Integer32"
_OlPortSlotIdx_Object = MibTableColumn
olPortSlotIdx = _OlPortSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 3),
    _OlPortSlotIdx_Type()
)
olPortSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortSlotIdx.setStatus("current")
_OlPortTypeIdx_Type = OlPortType
_OlPortTypeIdx_Object = MibTableColumn
olPortTypeIdx = _OlPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 4),
    _OlPortTypeIdx_Type()
)
olPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortTypeIdx.setStatus("current")


class _OlPortIdx_Type(Integer32):
    """Custom type olPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_OlPortIdx_Type.__name__ = "Integer32"
_OlPortIdx_Object = MibTableColumn
olPortIdx = _OlPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 5),
    _OlPortIdx_Type()
)
olPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortIdx.setStatus("current")


class _OlPortId_Type(DisplayString):
    """Custom type olPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlPortId_Type.__name__ = "DisplayString"
_OlPortId_Object = MibTableColumn
olPortId = _OlPortId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 6),
    _OlPortId_Type()
)
olPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olPortId.setStatus("current")
_OlPortCustom1_Type = DisplayString
_OlPortCustom1_Object = MibTableColumn
olPortCustom1 = _OlPortCustom1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 7),
    _OlPortCustom1_Type()
)
olPortCustom1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olPortCustom1.setStatus("current")
_OlPortCustom2_Type = DisplayString
_OlPortCustom2_Object = MibTableColumn
olPortCustom2 = _OlPortCustom2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 8),
    _OlPortCustom2_Type()
)
olPortCustom2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olPortCustom2.setStatus("current")
_OlPortCustom3_Type = DisplayString
_OlPortCustom3_Object = MibTableColumn
olPortCustom3 = _OlPortCustom3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 9),
    _OlPortCustom3_Type()
)
olPortCustom3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olPortCustom3.setStatus("current")


class _OlPortDWDMType_Type(Integer32):
    """Custom type olPortDWDMType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alien", 2),
          ("native", 1))
    )


_OlPortDWDMType_Type.__name__ = "Integer32"
_OlPortDWDMType_Object = MibTableColumn
olPortDWDMType = _OlPortDWDMType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 10),
    _OlPortDWDMType_Type()
)
olPortDWDMType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olPortDWDMType.setStatus("current")


class _OlPortGrid_Type(Integer32):
    """Custom type olPortGrid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ghz100", 1),
          ("ghz50", 2))
    )


_OlPortGrid_Type.__name__ = "Integer32"
_OlPortGrid_Object = MibTableColumn
olPortGrid = _OlPortGrid_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 11),
    _OlPortGrid_Type()
)
olPortGrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olPortGrid.setStatus("current")
_OlPortWavelength_Type = FixedX100
_OlPortWavelength_Object = MibTableColumn
olPortWavelength = _OlPortWavelength_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 12),
    _OlPortWavelength_Type()
)
olPortWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortWavelength.setStatus("current")
if mibBuilder.loadTexts:
    olPortWavelength.setUnits("nanometers/100")
_OlPortFrequency_Type = FixedX100
_OlPortFrequency_Object = MibTableColumn
olPortFrequency = _OlPortFrequency_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 13),
    _OlPortFrequency_Type()
)
olPortFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortFrequency.setStatus("current")
if mibBuilder.loadTexts:
    olPortFrequency.setUnits("terahertz/100")
_OlPortOperStatus_Type = OperStatus
_OlPortOperStatus_Object = MibTableColumn
olPortOperStatus = _OlPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 14),
    _OlPortOperStatus_Type()
)
olPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortOperStatus.setStatus("current")
_OlPortOperStatQlfr_Type = OperStatQlfr
_OlPortOperStatQlfr_Object = MibTableColumn
olPortOperStatQlfr = _OlPortOperStatQlfr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 15),
    _OlPortOperStatQlfr_Type()
)
olPortOperStatQlfr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortOperStatQlfr.setStatus("current")
_OlPortRemoteId_Type = DisplayString
_OlPortRemoteId_Object = MibTableColumn
olPortRemoteId = _OlPortRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 16),
    _OlPortRemoteId_Type()
)
olPortRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olPortRemoteId.setStatus("current")


class _OlPortExpCnxDegree_Type(Integer32):
    """Custom type olPortExpCnxDegree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_OlPortExpCnxDegree_Type.__name__ = "Integer32"
_OlPortExpCnxDegree_Object = MibTableColumn
olPortExpCnxDegree = _OlPortExpCnxDegree_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 17),
    _OlPortExpCnxDegree_Type()
)
olPortExpCnxDegree.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    olPortExpCnxDegree.setStatus("current")


class _OlPortActCnxDegree_Type(Integer32):
    """Custom type olPortActCnxDegree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_OlPortActCnxDegree_Type.__name__ = "Integer32"
_OlPortActCnxDegree_Object = MibTableColumn
olPortActCnxDegree = _OlPortActCnxDegree_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 18),
    _OlPortActCnxDegree_Type()
)
olPortActCnxDegree.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    olPortActCnxDegree.setStatus("current")
_OlPortRowStatus_Type = RowStatus
_OlPortRowStatus_Object = MibTableColumn
olPortRowStatus = _OlPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 4, 1, 100),
    _OlPortRowStatus_Type()
)
olPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olPortRowStatus.setStatus("current")
_EqptConnTable_Object = MibTable
eqptConnTable = _EqptConnTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5)
)
if mibBuilder.loadTexts:
    eqptConnTable.setStatus("current")
_EqptConnEntry_Object = MibTableRow
eqptConnEntry = _EqptConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5, 1)
)
eqptConnEntry.setIndexNames(
    (0, "BTI-OL-MIB", "eqptConnSrcCpTypeIdx"),
    (0, "BTI-OL-MIB", "eqptConnSrcShelfIdx"),
    (0, "BTI-OL-MIB", "eqptConnSrcSlotIdx"),
    (0, "BTI-OL-MIB", "eqptConnSrcPortTypeIdx"),
    (0, "BTI-OL-MIB", "eqptConnSrcIdx"),
    (0, "BTI-OL-MIB", "eqptConnDstCpTypeIdx"),
    (0, "BTI-OL-MIB", "eqptConnDstShelfIdx"),
    (0, "BTI-OL-MIB", "eqptConnDstSlotIdx"),
    (0, "BTI-OL-MIB", "eqptConnDstPortTypeIdx"),
    (0, "BTI-OL-MIB", "eqptConnDstIdx"),
)
if mibBuilder.loadTexts:
    eqptConnEntry.setStatus("current")
_EqptConnSrcCpTypeIdx_Type = CpType
_EqptConnSrcCpTypeIdx_Object = MibTableColumn
eqptConnSrcCpTypeIdx = _EqptConnSrcCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5, 1, 1),
    _EqptConnSrcCpTypeIdx_Type()
)
eqptConnSrcCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqptConnSrcCpTypeIdx.setStatus("current")


class _EqptConnSrcShelfIdx_Type(Integer32):
    """Custom type eqptConnSrcShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_EqptConnSrcShelfIdx_Type.__name__ = "Integer32"
_EqptConnSrcShelfIdx_Object = MibTableColumn
eqptConnSrcShelfIdx = _EqptConnSrcShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5, 1, 2),
    _EqptConnSrcShelfIdx_Type()
)
eqptConnSrcShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqptConnSrcShelfIdx.setStatus("current")


class _EqptConnSrcSlotIdx_Type(Integer32):
    """Custom type eqptConnSrcSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EqptConnSrcSlotIdx_Type.__name__ = "Integer32"
_EqptConnSrcSlotIdx_Object = MibTableColumn
eqptConnSrcSlotIdx = _EqptConnSrcSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5, 1, 3),
    _EqptConnSrcSlotIdx_Type()
)
eqptConnSrcSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqptConnSrcSlotIdx.setStatus("current")
_EqptConnSrcPortTypeIdx_Type = OlPortType
_EqptConnSrcPortTypeIdx_Object = MibTableColumn
eqptConnSrcPortTypeIdx = _EqptConnSrcPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5, 1, 4),
    _EqptConnSrcPortTypeIdx_Type()
)
eqptConnSrcPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqptConnSrcPortTypeIdx.setStatus("current")


class _EqptConnSrcIdx_Type(Integer32):
    """Custom type eqptConnSrcIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_EqptConnSrcIdx_Type.__name__ = "Integer32"
_EqptConnSrcIdx_Object = MibTableColumn
eqptConnSrcIdx = _EqptConnSrcIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5, 1, 5),
    _EqptConnSrcIdx_Type()
)
eqptConnSrcIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqptConnSrcIdx.setStatus("current")
_EqptConnDstCpTypeIdx_Type = CpType
_EqptConnDstCpTypeIdx_Object = MibTableColumn
eqptConnDstCpTypeIdx = _EqptConnDstCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5, 1, 6),
    _EqptConnDstCpTypeIdx_Type()
)
eqptConnDstCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqptConnDstCpTypeIdx.setStatus("current")


class _EqptConnDstShelfIdx_Type(Integer32):
    """Custom type eqptConnDstShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_EqptConnDstShelfIdx_Type.__name__ = "Integer32"
_EqptConnDstShelfIdx_Object = MibTableColumn
eqptConnDstShelfIdx = _EqptConnDstShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5, 1, 7),
    _EqptConnDstShelfIdx_Type()
)
eqptConnDstShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqptConnDstShelfIdx.setStatus("current")


class _EqptConnDstSlotIdx_Type(Integer32):
    """Custom type eqptConnDstSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EqptConnDstSlotIdx_Type.__name__ = "Integer32"
_EqptConnDstSlotIdx_Object = MibTableColumn
eqptConnDstSlotIdx = _EqptConnDstSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5, 1, 8),
    _EqptConnDstSlotIdx_Type()
)
eqptConnDstSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqptConnDstSlotIdx.setStatus("current")
_EqptConnDstPortTypeIdx_Type = OlPortType
_EqptConnDstPortTypeIdx_Object = MibTableColumn
eqptConnDstPortTypeIdx = _EqptConnDstPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5, 1, 9),
    _EqptConnDstPortTypeIdx_Type()
)
eqptConnDstPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqptConnDstPortTypeIdx.setStatus("current")


class _EqptConnDstIdx_Type(Integer32):
    """Custom type eqptConnDstIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_EqptConnDstIdx_Type.__name__ = "Integer32"
_EqptConnDstIdx_Object = MibTableColumn
eqptConnDstIdx = _EqptConnDstIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5, 1, 10),
    _EqptConnDstIdx_Type()
)
eqptConnDstIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqptConnDstIdx.setStatus("current")


class _EqptConnType_Type(Integer32):
    """Custom type eqptConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("duplex", 1),
          ("loopback", 2))
    )


_EqptConnType_Type.__name__ = "Integer32"
_EqptConnType_Object = MibTableColumn
eqptConnType = _EqptConnType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5, 1, 11),
    _EqptConnType_Type()
)
eqptConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptConnType.setStatus("current")
_EqptConnRowStatus_Type = RowStatus
_EqptConnRowStatus_Object = MibTableColumn
eqptConnRowStatus = _EqptConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 5, 1, 100),
    _EqptConnRowStatus_Type()
)
eqptConnRowStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eqptConnRowStatus.setStatus("current")
_OlOSCTable_Object = MibTable
olOSCTable = _OlOSCTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6)
)
if mibBuilder.loadTexts:
    olOSCTable.setStatus("current")
_OlOSCEntry_Object = MibTableRow
olOSCEntry = _OlOSCEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1)
)
olOSCEntry.setIndexNames(
    (0, "BTI-OL-MIB", "olOSCCpTypeIdx"),
    (0, "BTI-OL-MIB", "olOSCShelfIdx"),
    (0, "BTI-OL-MIB", "olOSCSlotIdx"),
    (0, "BTI-OL-MIB", "olOSCLineIdx"),
)
if mibBuilder.loadTexts:
    olOSCEntry.setStatus("current")
_OlOSCCpTypeIdx_Type = CpType
_OlOSCCpTypeIdx_Object = MibTableColumn
olOSCCpTypeIdx = _OlOSCCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 1),
    _OlOSCCpTypeIdx_Type()
)
olOSCCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCCpTypeIdx.setStatus("current")


class _OlOSCShelfIdx_Type(Integer32):
    """Custom type olOSCShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_OlOSCShelfIdx_Type.__name__ = "Integer32"
_OlOSCShelfIdx_Object = MibTableColumn
olOSCShelfIdx = _OlOSCShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 2),
    _OlOSCShelfIdx_Type()
)
olOSCShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCShelfIdx.setStatus("current")


class _OlOSCSlotIdx_Type(Integer32):
    """Custom type olOSCSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OlOSCSlotIdx_Type.__name__ = "Integer32"
_OlOSCSlotIdx_Object = MibTableColumn
olOSCSlotIdx = _OlOSCSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 3),
    _OlOSCSlotIdx_Type()
)
olOSCSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCSlotIdx.setStatus("current")


class _OlOSCLineIdx_Type(Integer32):
    """Custom type olOSCLineIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_OlOSCLineIdx_Type.__name__ = "Integer32"
_OlOSCLineIdx_Object = MibTableColumn
olOSCLineIdx = _OlOSCLineIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 4),
    _OlOSCLineIdx_Type()
)
olOSCLineIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCLineIdx.setStatus("current")
_OlOSCAdminStatus_Type = AdminStatus
_OlOSCAdminStatus_Object = MibTableColumn
olOSCAdminStatus = _OlOSCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 5),
    _OlOSCAdminStatus_Type()
)
olOSCAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCAdminStatus.setStatus("current")
_OlOSCOperStatus_Type = OperStatus
_OlOSCOperStatus_Object = MibTableColumn
olOSCOperStatus = _OlOSCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 6),
    _OlOSCOperStatus_Type()
)
olOSCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCOperStatus.setStatus("current")
_OlOSCOperStatQlfr_Type = OperStatQlfr
_OlOSCOperStatQlfr_Object = MibTableColumn
olOSCOperStatQlfr = _OlOSCOperStatQlfr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 7),
    _OlOSCOperStatQlfr_Type()
)
olOSCOperStatQlfr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCOperStatQlfr.setStatus("current")
_OlOSCAutoEnableTimer_Type = HoursAndMinutes
_OlOSCAutoEnableTimer_Object = MibTableColumn
olOSCAutoEnableTimer = _OlOSCAutoEnableTimer_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 8),
    _OlOSCAutoEnableTimer_Type()
)
olOSCAutoEnableTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCAutoEnableTimer.setStatus("current")
_OlOSCActAutoEnableTimer_Type = HoursAndMinutes
_OlOSCActAutoEnableTimer_Object = MibTableColumn
olOSCActAutoEnableTimer = _OlOSCActAutoEnableTimer_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 9),
    _OlOSCActAutoEnableTimer_Type()
)
olOSCActAutoEnableTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCActAutoEnableTimer.setStatus("current")


class _OlOSCId_Type(DisplayString):
    """Custom type olOSCId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlOSCId_Type.__name__ = "DisplayString"
_OlOSCId_Object = MibTableColumn
olOSCId = _OlOSCId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 10),
    _OlOSCId_Type()
)
olOSCId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCId.setStatus("current")
_OlOSCCustom1_Type = DisplayString
_OlOSCCustom1_Object = MibTableColumn
olOSCCustom1 = _OlOSCCustom1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 11),
    _OlOSCCustom1_Type()
)
olOSCCustom1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCCustom1.setStatus("current")
_OlOSCCustom2_Type = DisplayString
_OlOSCCustom2_Object = MibTableColumn
olOSCCustom2 = _OlOSCCustom2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 12),
    _OlOSCCustom2_Type()
)
olOSCCustom2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCCustom2.setStatus("current")
_OlOSCCustom3_Type = DisplayString
_OlOSCCustom3_Object = MibTableColumn
olOSCCustom3 = _OlOSCCustom3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 13),
    _OlOSCCustom3_Type()
)
olOSCCustom3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCCustom3.setStatus("current")


class _OlOSCFEIMMon_Type(Integer32):
    """Custom type olOSCFEIMMon based on Integer32"""
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


_OlOSCFEIMMon_Type.__name__ = "Integer32"
_OlOSCFEIMMon_Object = MibTableColumn
olOSCFEIMMon = _OlOSCFEIMMon_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 14),
    _OlOSCFEIMMon_Type()
)
olOSCFEIMMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCFEIMMon.setStatus("current")


class _OlOSCExpFESysName_Type(DisplayString):
    """Custom type olOSCExpFESysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OlOSCExpFESysName_Type.__name__ = "DisplayString"
_OlOSCExpFESysName_Object = MibTableColumn
olOSCExpFESysName = _OlOSCExpFESysName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 15),
    _OlOSCExpFESysName_Type()
)
olOSCExpFESysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCExpFESysName.setStatus("current")


class _OlOSCExpFEIPAddr_Type(IpAddress):
    """Custom type olOSCExpFEIPAddr based on IpAddress"""
    defaultValue = 0


_OlOSCExpFEIPAddr_Object = MibTableColumn
olOSCExpFEIPAddr = _OlOSCExpFEIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 16),
    _OlOSCExpFEIPAddr_Type()
)
olOSCExpFEIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCExpFEIPAddr.setStatus("current")


class _OlOSCExpFEGrp_Type(Integer32):
    """Custom type olOSCExpFEGrp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OlOSCExpFEGrp_Type.__name__ = "Integer32"
_OlOSCExpFEGrp_Object = MibTableColumn
olOSCExpFEGrp = _OlOSCExpFEGrp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 17),
    _OlOSCExpFEGrp_Type()
)
olOSCExpFEGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCExpFEGrp.setStatus("current")


class _OlOSCExpFEDegr_Type(Integer32):
    """Custom type olOSCExpFEDegr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_OlOSCExpFEDegr_Type.__name__ = "Integer32"
_OlOSCExpFEDegr_Object = MibTableColumn
olOSCExpFEDegr = _OlOSCExpFEDegr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 18),
    _OlOSCExpFEDegr_Type()
)
olOSCExpFEDegr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCExpFEDegr.setStatus("current")


class _OlOSCFESysName_Type(DisplayString):
    """Custom type olOSCFESysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OlOSCFESysName_Type.__name__ = "DisplayString"
_OlOSCFESysName_Object = MibTableColumn
olOSCFESysName = _OlOSCFESysName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 19),
    _OlOSCFESysName_Type()
)
olOSCFESysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCFESysName.setStatus("current")
_OlOSCFEIPAddr_Type = IpAddress
_OlOSCFEIPAddr_Object = MibTableColumn
olOSCFEIPAddr = _OlOSCFEIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 20),
    _OlOSCFEIPAddr_Type()
)
olOSCFEIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCFEIPAddr.setStatus("current")


class _OlOSCFEGrp_Type(Integer32):
    """Custom type olOSCFEGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OlOSCFEGrp_Type.__name__ = "Integer32"
_OlOSCFEGrp_Object = MibTableColumn
olOSCFEGrp = _OlOSCFEGrp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 21),
    _OlOSCFEGrp_Type()
)
olOSCFEGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCFEGrp.setStatus("current")


class _OlOSCFEDegr_Type(Integer32):
    """Custom type olOSCFEDegr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_OlOSCFEDegr_Type.__name__ = "Integer32"
_OlOSCFEDegr_Object = MibTableColumn
olOSCFEDegr = _OlOSCFEDegr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 22),
    _OlOSCFEDegr_Type()
)
olOSCFEDegr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCFEDegr.setStatus("current")
_OlOSCFEGrpType_Type = OlGroupType
_OlOSCFEGrpType_Object = MibTableColumn
olOSCFEGrpType = _OlOSCFEGrpType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 23),
    _OlOSCFEGrpType_Type()
)
olOSCFEGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCFEGrpType.setStatus("current")
_OlOSCRowStatus_Type = RowStatus
_OlOSCRowStatus_Object = MibTableColumn
olOSCRowStatus = _OlOSCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 6, 1, 100),
    _OlOSCRowStatus_Type()
)
olOSCRowStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    olOSCRowStatus.setStatus("current")
_OdccTable_Object = MibTable
odccTable = _OdccTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 7)
)
if mibBuilder.loadTexts:
    odccTable.setStatus("current")
_OdccEntry_Object = MibTableRow
odccEntry = _OdccEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 7, 1)
)
odccEntry.setIndexNames(
    (0, "BTI-OL-MIB", "odccCpTypeIdx"),
    (0, "BTI-OL-MIB", "odccShelfIdx"),
    (0, "BTI-OL-MIB", "odccSlotIdx"),
    (0, "BTI-OL-MIB", "odccLineIdx"),
)
if mibBuilder.loadTexts:
    odccEntry.setStatus("current")
_OdccCpTypeIdx_Type = CpType
_OdccCpTypeIdx_Object = MibTableColumn
odccCpTypeIdx = _OdccCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 7, 1, 1),
    _OdccCpTypeIdx_Type()
)
odccCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    odccCpTypeIdx.setStatus("current")


class _OdccShelfIdx_Type(Integer32):
    """Custom type odccShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_OdccShelfIdx_Type.__name__ = "Integer32"
_OdccShelfIdx_Object = MibTableColumn
odccShelfIdx = _OdccShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 7, 1, 2),
    _OdccShelfIdx_Type()
)
odccShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    odccShelfIdx.setStatus("current")


class _OdccSlotIdx_Type(Integer32):
    """Custom type odccSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OdccSlotIdx_Type.__name__ = "Integer32"
_OdccSlotIdx_Object = MibTableColumn
odccSlotIdx = _OdccSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 7, 1, 3),
    _OdccSlotIdx_Type()
)
odccSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    odccSlotIdx.setStatus("current")


class _OdccLineIdx_Type(Integer32):
    """Custom type odccLineIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_OdccLineIdx_Type.__name__ = "Integer32"
_OdccLineIdx_Object = MibTableColumn
odccLineIdx = _OdccLineIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 7, 1, 4),
    _OdccLineIdx_Type()
)
odccLineIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    odccLineIdx.setStatus("current")
_OdccAdminStatus_Type = AdminStatus
_OdccAdminStatus_Object = MibTableColumn
odccAdminStatus = _OdccAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 7, 1, 5),
    _OdccAdminStatus_Type()
)
odccAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    odccAdminStatus.setStatus("current")
_OdccRowStatus_Type = RowStatus
_OdccRowStatus_Object = MibTableColumn
odccRowStatus = _OdccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 7, 1, 100),
    _OdccRowStatus_Type()
)
odccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    odccRowStatus.setStatus("current")
_WdmTable_Object = MibTable
wdmTable = _WdmTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8)
)
if mibBuilder.loadTexts:
    wdmTable.setStatus("current")
_WdmEntry_Object = MibTableRow
wdmEntry = _WdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1)
)
wdmEntry.setIndexNames(
    (0, "BTI-OL-MIB", "wdmCpTypeIdx"),
    (0, "BTI-OL-MIB", "wdmShelfIdx"),
    (0, "BTI-OL-MIB", "wdmSlotIdx"),
    (0, "BTI-OL-MIB", "wdmLineIdx"),
)
if mibBuilder.loadTexts:
    wdmEntry.setStatus("current")
_WdmCpTypeIdx_Type = CpType
_WdmCpTypeIdx_Object = MibTableColumn
wdmCpTypeIdx = _WdmCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 1),
    _WdmCpTypeIdx_Type()
)
wdmCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wdmCpTypeIdx.setStatus("current")


class _WdmShelfIdx_Type(Integer32):
    """Custom type wdmShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_WdmShelfIdx_Type.__name__ = "Integer32"
_WdmShelfIdx_Object = MibTableColumn
wdmShelfIdx = _WdmShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 2),
    _WdmShelfIdx_Type()
)
wdmShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wdmShelfIdx.setStatus("current")


class _WdmSlotIdx_Type(Integer32):
    """Custom type wdmSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WdmSlotIdx_Type.__name__ = "Integer32"
_WdmSlotIdx_Object = MibTableColumn
wdmSlotIdx = _WdmSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 3),
    _WdmSlotIdx_Type()
)
wdmSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wdmSlotIdx.setStatus("current")


class _WdmLineIdx_Type(Integer32):
    """Custom type wdmLineIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WdmLineIdx_Type.__name__ = "Integer32"
_WdmLineIdx_Object = MibTableColumn
wdmLineIdx = _WdmLineIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 4),
    _WdmLineIdx_Type()
)
wdmLineIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wdmLineIdx.setStatus("current")
_WdmAdminStatus_Type = AdminStatus
_WdmAdminStatus_Object = MibTableColumn
wdmAdminStatus = _WdmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 5),
    _WdmAdminStatus_Type()
)
wdmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmAdminStatus.setStatus("current")
_WdmOperStatus_Type = OperStatus
_WdmOperStatus_Object = MibTableColumn
wdmOperStatus = _WdmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 6),
    _WdmOperStatus_Type()
)
wdmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmOperStatus.setStatus("current")
_WdmOperStatQlfr_Type = OperStatQlfr
_WdmOperStatQlfr_Object = MibTableColumn
wdmOperStatQlfr = _WdmOperStatQlfr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 7),
    _WdmOperStatQlfr_Type()
)
wdmOperStatQlfr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmOperStatQlfr.setStatus("current")
_WdmAutoEnableTimer_Type = HoursAndMinutes
_WdmAutoEnableTimer_Object = MibTableColumn
wdmAutoEnableTimer = _WdmAutoEnableTimer_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 8),
    _WdmAutoEnableTimer_Type()
)
wdmAutoEnableTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmAutoEnableTimer.setStatus("current")
_WdmActAutoEnableTimer_Type = HoursAndMinutes
_WdmActAutoEnableTimer_Object = MibTableColumn
wdmActAutoEnableTimer = _WdmActAutoEnableTimer_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 9),
    _WdmActAutoEnableTimer_Type()
)
wdmActAutoEnableTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmActAutoEnableTimer.setStatus("current")


class _WdmId_Type(DisplayString):
    """Custom type wdmId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WdmId_Type.__name__ = "DisplayString"
_WdmId_Object = MibTableColumn
wdmId = _WdmId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 10),
    _WdmId_Type()
)
wdmId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmId.setStatus("current")
_WdmCustom1_Type = DisplayString
_WdmCustom1_Object = MibTableColumn
wdmCustom1 = _WdmCustom1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 11),
    _WdmCustom1_Type()
)
wdmCustom1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmCustom1.setStatus("current")
_WdmCustom2_Type = DisplayString
_WdmCustom2_Object = MibTableColumn
wdmCustom2 = _WdmCustom2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 12),
    _WdmCustom2_Type()
)
wdmCustom2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmCustom2.setStatus("current")
_WdmCustom3_Type = DisplayString
_WdmCustom3_Object = MibTableColumn
wdmCustom3 = _WdmCustom3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 13),
    _WdmCustom3_Type()
)
wdmCustom3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmCustom3.setStatus("current")


class _WdmFiberType_Type(Integer32):
    """Custom type wdmFiberType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("smf", 1)
    )


_WdmFiberType_Type.__name__ = "Integer32"
_WdmFiberType_Object = MibTableColumn
wdmFiberType = _WdmFiberType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 14),
    _WdmFiberType_Type()
)
wdmFiberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmFiberType.setStatus("current")
_WdmSpanLength_Type = Unsigned32
_WdmSpanLength_Object = MibTableColumn
wdmSpanLength = _WdmSpanLength_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 15),
    _WdmSpanLength_Type()
)
wdmSpanLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmSpanLength.setStatus("current")
if mibBuilder.loadTexts:
    wdmSpanLength.setUnits("kilometers")
_WdmSpanLossRxHighTh_Type = FixedX10
_WdmSpanLossRxHighTh_Object = MibTableColumn
wdmSpanLossRxHighTh = _WdmSpanLossRxHighTh_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 16),
    _WdmSpanLossRxHighTh_Type()
)
wdmSpanLossRxHighTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmSpanLossRxHighTh.setStatus("current")
if mibBuilder.loadTexts:
    wdmSpanLossRxHighTh.setUnits("dB/10")
_WdmSpanLossSpecMax_Type = FixedX10
_WdmSpanLossSpecMax_Object = MibTableColumn
wdmSpanLossSpecMax = _WdmSpanLossSpecMax_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 17),
    _WdmSpanLossSpecMax_Type()
)
wdmSpanLossSpecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmSpanLossSpecMax.setStatus("current")
if mibBuilder.loadTexts:
    wdmSpanLossSpecMax.setUnits("dB/10")


class _WdmNumChannels_Type(Integer32):
    """Custom type wdmNumChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44),
    )


_WdmNumChannels_Type.__name__ = "Integer32"
_WdmNumChannels_Object = MibTableColumn
wdmNumChannels = _WdmNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 18),
    _WdmNumChannels_Type()
)
wdmNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmNumChannels.setStatus("current")
_WdmRowStatus_Type = RowStatus
_WdmRowStatus_Object = MibTableColumn
wdmRowStatus = _WdmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 8, 1, 100),
    _WdmRowStatus_Type()
)
wdmRowStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wdmRowStatus.setStatus("current")
_WchXCTable_Object = MibTable
wchXCTable = _WchXCTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9)
)
if mibBuilder.loadTexts:
    wchXCTable.setStatus("current")
_WchXCEntry_Object = MibTableRow
wchXCEntry = _WchXCEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1)
)
wchXCEntry.setIndexNames(
    (0, "BTI-OL-MIB", "wchXCSrcCpTypeIdx"),
    (0, "BTI-OL-MIB", "wchXCSrcShelfIdx"),
    (0, "BTI-OL-MIB", "wchXCSrcSlotIdx"),
    (0, "BTI-OL-MIB", "wchXCSrcPortTypeIdx"),
    (0, "BTI-OL-MIB", "wchXCSrcPortIdx"),
    (0, "BTI-OL-MIB", "wchXCSrcChannelIdx"),
    (0, "BTI-OL-MIB", "wchXCDstCpTypeIdx"),
    (0, "BTI-OL-MIB", "wchXCDstShelfIdx"),
    (0, "BTI-OL-MIB", "wchXCDstSlotIdx"),
    (0, "BTI-OL-MIB", "wchXCDstPortTypeIdx"),
    (0, "BTI-OL-MIB", "wchXCDstPortIdx"),
    (0, "BTI-OL-MIB", "wchXCDstChannelIdx"),
)
if mibBuilder.loadTexts:
    wchXCEntry.setStatus("current")
_WchXCSrcCpTypeIdx_Type = CpType
_WchXCSrcCpTypeIdx_Object = MibTableColumn
wchXCSrcCpTypeIdx = _WchXCSrcCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 1),
    _WchXCSrcCpTypeIdx_Type()
)
wchXCSrcCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchXCSrcCpTypeIdx.setStatus("current")


class _WchXCSrcShelfIdx_Type(Integer32):
    """Custom type wchXCSrcShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_WchXCSrcShelfIdx_Type.__name__ = "Integer32"
_WchXCSrcShelfIdx_Object = MibTableColumn
wchXCSrcShelfIdx = _WchXCSrcShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 2),
    _WchXCSrcShelfIdx_Type()
)
wchXCSrcShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchXCSrcShelfIdx.setStatus("current")


class _WchXCSrcSlotIdx_Type(Integer32):
    """Custom type wchXCSrcSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WchXCSrcSlotIdx_Type.__name__ = "Integer32"
_WchXCSrcSlotIdx_Object = MibTableColumn
wchXCSrcSlotIdx = _WchXCSrcSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 3),
    _WchXCSrcSlotIdx_Type()
)
wchXCSrcSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchXCSrcSlotIdx.setStatus("current")
_WchXCSrcPortTypeIdx_Type = OlPortType
_WchXCSrcPortTypeIdx_Object = MibTableColumn
wchXCSrcPortTypeIdx = _WchXCSrcPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 4),
    _WchXCSrcPortTypeIdx_Type()
)
wchXCSrcPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchXCSrcPortTypeIdx.setStatus("current")


class _WchXCSrcPortIdx_Type(Integer32):
    """Custom type wchXCSrcPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_WchXCSrcPortIdx_Type.__name__ = "Integer32"
_WchXCSrcPortIdx_Object = MibTableColumn
wchXCSrcPortIdx = _WchXCSrcPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 5),
    _WchXCSrcPortIdx_Type()
)
wchXCSrcPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchXCSrcPortIdx.setStatus("current")


class _WchXCSrcChannelIdx_Type(Integer32):
    """Custom type wchXCSrcChannelIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(135, 610),
    )


_WchXCSrcChannelIdx_Type.__name__ = "Integer32"
_WchXCSrcChannelIdx_Object = MibTableColumn
wchXCSrcChannelIdx = _WchXCSrcChannelIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 6),
    _WchXCSrcChannelIdx_Type()
)
wchXCSrcChannelIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchXCSrcChannelIdx.setStatus("current")
_WchXCDstCpTypeIdx_Type = CpType
_WchXCDstCpTypeIdx_Object = MibTableColumn
wchXCDstCpTypeIdx = _WchXCDstCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 7),
    _WchXCDstCpTypeIdx_Type()
)
wchXCDstCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchXCDstCpTypeIdx.setStatus("current")


class _WchXCDstShelfIdx_Type(Integer32):
    """Custom type wchXCDstShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_WchXCDstShelfIdx_Type.__name__ = "Integer32"
_WchXCDstShelfIdx_Object = MibTableColumn
wchXCDstShelfIdx = _WchXCDstShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 8),
    _WchXCDstShelfIdx_Type()
)
wchXCDstShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchXCDstShelfIdx.setStatus("current")


class _WchXCDstSlotIdx_Type(Integer32):
    """Custom type wchXCDstSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WchXCDstSlotIdx_Type.__name__ = "Integer32"
_WchXCDstSlotIdx_Object = MibTableColumn
wchXCDstSlotIdx = _WchXCDstSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 9),
    _WchXCDstSlotIdx_Type()
)
wchXCDstSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchXCDstSlotIdx.setStatus("current")
_WchXCDstPortTypeIdx_Type = OlPortType
_WchXCDstPortTypeIdx_Object = MibTableColumn
wchXCDstPortTypeIdx = _WchXCDstPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 10),
    _WchXCDstPortTypeIdx_Type()
)
wchXCDstPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchXCDstPortTypeIdx.setStatus("current")


class _WchXCDstPortIdx_Type(Integer32):
    """Custom type wchXCDstPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_WchXCDstPortIdx_Type.__name__ = "Integer32"
_WchXCDstPortIdx_Object = MibTableColumn
wchXCDstPortIdx = _WchXCDstPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 11),
    _WchXCDstPortIdx_Type()
)
wchXCDstPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchXCDstPortIdx.setStatus("current")


class _WchXCDstChannelIdx_Type(Integer32):
    """Custom type wchXCDstChannelIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(135, 610),
    )


_WchXCDstChannelIdx_Type.__name__ = "Integer32"
_WchXCDstChannelIdx_Object = MibTableColumn
wchXCDstChannelIdx = _WchXCDstChannelIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 12),
    _WchXCDstChannelIdx_Type()
)
wchXCDstChannelIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchXCDstChannelIdx.setStatus("current")


class _WchXCServiceName_Type(DisplayString):
    """Custom type wchXCServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WchXCServiceName_Type.__name__ = "DisplayString"
_WchXCServiceName_Object = MibTableColumn
wchXCServiceName = _WchXCServiceName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 13),
    _WchXCServiceName_Type()
)
wchXCServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wchXCServiceName.setStatus("current")
_WchXCRowStatus_Type = RowStatus
_WchXCRowStatus_Object = MibTableColumn
wchXCRowStatus = _WchXCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 9, 1, 100),
    _WchXCRowStatus_Type()
)
wchXCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wchXCRowStatus.setStatus("current")
_WchTable_Object = MibTable
wchTable = _WchTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10)
)
if mibBuilder.loadTexts:
    wchTable.setStatus("current")
_WchEntry_Object = MibTableRow
wchEntry = _WchEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1)
)
wchEntry.setIndexNames(
    (0, "BTI-OL-MIB", "wchCpTypeIdx"),
    (0, "BTI-OL-MIB", "wchShelfIdx"),
    (0, "BTI-OL-MIB", "wchSlotIdx"),
    (0, "BTI-OL-MIB", "wchPortTypeIdx"),
    (0, "BTI-OL-MIB", "wchPortIdx"),
    (0, "BTI-OL-MIB", "wchIdx"),
)
if mibBuilder.loadTexts:
    wchEntry.setStatus("current")
_WchCpTypeIdx_Type = CpType
_WchCpTypeIdx_Object = MibTableColumn
wchCpTypeIdx = _WchCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 1),
    _WchCpTypeIdx_Type()
)
wchCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchCpTypeIdx.setStatus("current")


class _WchShelfIdx_Type(Integer32):
    """Custom type wchShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_WchShelfIdx_Type.__name__ = "Integer32"
_WchShelfIdx_Object = MibTableColumn
wchShelfIdx = _WchShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 2),
    _WchShelfIdx_Type()
)
wchShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchShelfIdx.setStatus("current")


class _WchSlotIdx_Type(Integer32):
    """Custom type wchSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WchSlotIdx_Type.__name__ = "Integer32"
_WchSlotIdx_Object = MibTableColumn
wchSlotIdx = _WchSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 3),
    _WchSlotIdx_Type()
)
wchSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchSlotIdx.setStatus("current")
_WchPortTypeIdx_Type = OlPortType
_WchPortTypeIdx_Object = MibTableColumn
wchPortTypeIdx = _WchPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 4),
    _WchPortTypeIdx_Type()
)
wchPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchPortTypeIdx.setStatus("current")


class _WchPortIdx_Type(Integer32):
    """Custom type wchPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WchPortIdx_Type.__name__ = "Integer32"
_WchPortIdx_Object = MibTableColumn
wchPortIdx = _WchPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 5),
    _WchPortIdx_Type()
)
wchPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchPortIdx.setStatus("current")


class _WchIdx_Type(Integer32):
    """Custom type wchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(135, 610),
    )


_WchIdx_Type.__name__ = "Integer32"
_WchIdx_Object = MibTableColumn
wchIdx = _WchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 6),
    _WchIdx_Type()
)
wchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchIdx.setStatus("current")
_WchAdminStatus_Type = AdminStatus
_WchAdminStatus_Object = MibTableColumn
wchAdminStatus = _WchAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 7),
    _WchAdminStatus_Type()
)
wchAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchAdminStatus.setStatus("current")
_WchOperStatus_Type = OperStatus
_WchOperStatus_Object = MibTableColumn
wchOperStatus = _WchOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 8),
    _WchOperStatus_Type()
)
wchOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchOperStatus.setStatus("current")
_WchOperStatQlfr_Type = OperStatQlfr
_WchOperStatQlfr_Object = MibTableColumn
wchOperStatQlfr = _WchOperStatQlfr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 9),
    _WchOperStatQlfr_Type()
)
wchOperStatQlfr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchOperStatQlfr.setStatus("current")
_WchAutoEnableTimer_Type = HoursAndMinutes
_WchAutoEnableTimer_Object = MibTableColumn
wchAutoEnableTimer = _WchAutoEnableTimer_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 10),
    _WchAutoEnableTimer_Type()
)
wchAutoEnableTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchAutoEnableTimer.setStatus("current")
_WchActAutoEnableTimer_Type = HoursAndMinutes
_WchActAutoEnableTimer_Object = MibTableColumn
wchActAutoEnableTimer = _WchActAutoEnableTimer_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 11),
    _WchActAutoEnableTimer_Type()
)
wchActAutoEnableTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchActAutoEnableTimer.setStatus("current")


class _WchId_Type(DisplayString):
    """Custom type wchId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WchId_Type.__name__ = "DisplayString"
_WchId_Object = MibTableColumn
wchId = _WchId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 12),
    _WchId_Type()
)
wchId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchId.setStatus("current")
_WchCustom1_Type = DisplayString
_WchCustom1_Object = MibTableColumn
wchCustom1 = _WchCustom1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 13),
    _WchCustom1_Type()
)
wchCustom1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchCustom1.setStatus("current")
_WchCustom2_Type = DisplayString
_WchCustom2_Object = MibTableColumn
wchCustom2 = _WchCustom2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 14),
    _WchCustom2_Type()
)
wchCustom2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchCustom2.setStatus("current")
_WchCustom3_Type = DisplayString
_WchCustom3_Object = MibTableColumn
wchCustom3 = _WchCustom3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 15),
    _WchCustom3_Type()
)
wchCustom3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchCustom3.setStatus("current")


class _WchBitrate_Type(Integer32):
    """Custom type wchBitrate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tenGig", 1)
    )


_WchBitrate_Type.__name__ = "Integer32"
_WchBitrate_Object = MibTableColumn
wchBitrate = _WchBitrate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 16),
    _WchBitrate_Type()
)
wchBitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchBitrate.setStatus("current")


class _WchGrid_Type(Integer32):
    """Custom type wchGrid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ghz100", 1),
          ("ghz50", 2))
    )


_WchGrid_Type.__name__ = "Integer32"
_WchGrid_Object = MibTableColumn
wchGrid = _WchGrid_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 17),
    _WchGrid_Type()
)
wchGrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchGrid.setStatus("current")
_WchWavelength_Type = FixedX100
_WchWavelength_Object = MibTableColumn
wchWavelength = _WchWavelength_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 18),
    _WchWavelength_Type()
)
wchWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchWavelength.setStatus("current")
if mibBuilder.loadTexts:
    wchWavelength.setUnits("nanometers/100")
_WchFrequency_Type = FixedX100
_WchFrequency_Object = MibTableColumn
wchFrequency = _WchFrequency_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 19),
    _WchFrequency_Type()
)
wchFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchFrequency.setStatus("current")
if mibBuilder.loadTexts:
    wchFrequency.setUnits("terahertz/100")
_WchRowStatus_Type = RowStatus
_WchRowStatus_Object = MibTableColumn
wchRowStatus = _WchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 10, 1, 100),
    _WchRowStatus_Type()
)
wchRowStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wchRowStatus.setStatus("current")
_OlGroupMerge_ObjectIdentity = ObjectIdentity
olGroupMerge = _OlGroupMerge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 11)
)


class _OlGroupMergeCmd_Type(Integer32):
    """Custom type olGroupMergeCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("invoke", 2))
    )


_OlGroupMergeCmd_Type.__name__ = "Integer32"
_OlGroupMergeCmd_Object = MibScalar
olGroupMergeCmd = _OlGroupMergeCmd_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 11, 1),
    _OlGroupMergeCmd_Type()
)
olGroupMergeCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olGroupMergeCmd.setStatus("current")


class _OlGroupMergePrimary_Type(Integer32):
    """Custom type olGroupMergePrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OlGroupMergePrimary_Type.__name__ = "Integer32"
_OlGroupMergePrimary_Object = MibScalar
olGroupMergePrimary = _OlGroupMergePrimary_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 11, 2),
    _OlGroupMergePrimary_Type()
)
olGroupMergePrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olGroupMergePrimary.setStatus("current")


class _OlGroupMergeSecondary_Type(Integer32):
    """Custom type olGroupMergeSecondary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OlGroupMergeSecondary_Type.__name__ = "Integer32"
_OlGroupMergeSecondary_Object = MibScalar
olGroupMergeSecondary = _OlGroupMergeSecondary_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 11, 3),
    _OlGroupMergeSecondary_Type()
)
olGroupMergeSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olGroupMergeSecondary.setStatus("current")
_OlPerformance_ObjectIdentity = ObjectIdentity
olPerformance = _OlPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12)
)
_OlOSCCrntPMTable_Object = MibTable
olOSCCrntPMTable = _OlOSCCrntPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1)
)
if mibBuilder.loadTexts:
    olOSCCrntPMTable.setStatus("current")
_OlOSCCrntPMEntry_Object = MibTableRow
olOSCCrntPMEntry = _OlOSCCrntPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1)
)
olOSCCrntPMEntry.setIndexNames(
    (0, "BTI-OL-MIB", "olOSCCrntPMCpTypeIdx"),
    (0, "BTI-OL-MIB", "olOSCCrntPMShelfIdx"),
    (0, "BTI-OL-MIB", "olOSCCrntPMSlotIdx"),
    (0, "BTI-OL-MIB", "olOSCCrntPMLineIdx"),
    (0, "BTI-OL-MIB", "olOSCCrntPMIntervalTypeIdx"),
)
if mibBuilder.loadTexts:
    olOSCCrntPMEntry.setStatus("current")
_OlOSCCrntPMCpTypeIdx_Type = CpType
_OlOSCCrntPMCpTypeIdx_Object = MibTableColumn
olOSCCrntPMCpTypeIdx = _OlOSCCrntPMCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 1),
    _OlOSCCrntPMCpTypeIdx_Type()
)
olOSCCrntPMCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCCrntPMCpTypeIdx.setStatus("current")


class _OlOSCCrntPMShelfIdx_Type(Integer32):
    """Custom type olOSCCrntPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_OlOSCCrntPMShelfIdx_Type.__name__ = "Integer32"
_OlOSCCrntPMShelfIdx_Object = MibTableColumn
olOSCCrntPMShelfIdx = _OlOSCCrntPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 2),
    _OlOSCCrntPMShelfIdx_Type()
)
olOSCCrntPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCCrntPMShelfIdx.setStatus("current")


class _OlOSCCrntPMSlotIdx_Type(Integer32):
    """Custom type olOSCCrntPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OlOSCCrntPMSlotIdx_Type.__name__ = "Integer32"
_OlOSCCrntPMSlotIdx_Object = MibTableColumn
olOSCCrntPMSlotIdx = _OlOSCCrntPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 3),
    _OlOSCCrntPMSlotIdx_Type()
)
olOSCCrntPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCCrntPMSlotIdx.setStatus("current")


class _OlOSCCrntPMLineIdx_Type(Integer32):
    """Custom type olOSCCrntPMLineIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_OlOSCCrntPMLineIdx_Type.__name__ = "Integer32"
_OlOSCCrntPMLineIdx_Object = MibTableColumn
olOSCCrntPMLineIdx = _OlOSCCrntPMLineIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 4),
    _OlOSCCrntPMLineIdx_Type()
)
olOSCCrntPMLineIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCCrntPMLineIdx.setStatus("current")
_OlOSCCrntPMIntervalTypeIdx_Type = PMIntervalType
_OlOSCCrntPMIntervalTypeIdx_Object = MibTableColumn
olOSCCrntPMIntervalTypeIdx = _OlOSCCrntPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 5),
    _OlOSCCrntPMIntervalTypeIdx_Type()
)
olOSCCrntPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCCrntPMIntervalTypeIdx.setStatus("current")
_OlOSCCrntPMOPRValue_Type = FixedX10
_OlOSCCrntPMOPRValue_Object = MibTableColumn
olOSCCrntPMOPRValue = _OlOSCCrntPMOPRValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 6),
    _OlOSCCrntPMOPRValue_Type()
)
olOSCCrntPMOPRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMOPRValue.setStatus("current")
if mibBuilder.loadTexts:
    olOSCCrntPMOPRValue.setUnits("dBm/10")
_OlOSCCrntPMOPRTimeStamp_Type = DateAndTime
_OlOSCCrntPMOPRTimeStamp_Object = MibTableColumn
olOSCCrntPMOPRTimeStamp = _OlOSCCrntPMOPRTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 7),
    _OlOSCCrntPMOPRTimeStamp_Type()
)
olOSCCrntPMOPRTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMOPRTimeStamp.setStatus("current")
_OlOSCCrntPMOPRValidity_Type = PMValidity
_OlOSCCrntPMOPRValidity_Object = MibTableColumn
olOSCCrntPMOPRValidity = _OlOSCCrntPMOPRValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 8),
    _OlOSCCrntPMOPRValidity_Type()
)
olOSCCrntPMOPRValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMOPRValidity.setStatus("current")
_OlOSCCrntPMOPTValue_Type = FixedX10
_OlOSCCrntPMOPTValue_Object = MibTableColumn
olOSCCrntPMOPTValue = _OlOSCCrntPMOPTValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 9),
    _OlOSCCrntPMOPTValue_Type()
)
olOSCCrntPMOPTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMOPTValue.setStatus("current")
if mibBuilder.loadTexts:
    olOSCCrntPMOPTValue.setUnits("dBm/10")
_OlOSCCrntPMOPTTimeStamp_Type = DateAndTime
_OlOSCCrntPMOPTTimeStamp_Object = MibTableColumn
olOSCCrntPMOPTTimeStamp = _OlOSCCrntPMOPTTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 10),
    _OlOSCCrntPMOPTTimeStamp_Type()
)
olOSCCrntPMOPTTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMOPTTimeStamp.setStatus("current")
_OlOSCCrntPMOPTValidity_Type = PMValidity
_OlOSCCrntPMOPTValidity_Object = MibTableColumn
olOSCCrntPMOPTValidity = _OlOSCCrntPMOPTValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 11),
    _OlOSCCrntPMOPTValidity_Type()
)
olOSCCrntPMOPTValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMOPTValidity.setStatus("current")
_OlOSCCrntPMOBRValue_Type = FixedX10
_OlOSCCrntPMOBRValue_Object = MibTableColumn
olOSCCrntPMOBRValue = _OlOSCCrntPMOBRValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 12),
    _OlOSCCrntPMOBRValue_Type()
)
olOSCCrntPMOBRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMOBRValue.setStatus("current")
if mibBuilder.loadTexts:
    olOSCCrntPMOBRValue.setUnits("dB/10")
_OlOSCCrntPMOBRTimeStamp_Type = DateAndTime
_OlOSCCrntPMOBRTimeStamp_Object = MibTableColumn
olOSCCrntPMOBRTimeStamp = _OlOSCCrntPMOBRTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 13),
    _OlOSCCrntPMOBRTimeStamp_Type()
)
olOSCCrntPMOBRTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMOBRTimeStamp.setStatus("current")
_OlOSCCrntPMOBRValidity_Type = PMValidity
_OlOSCCrntPMOBRValidity_Object = MibTableColumn
olOSCCrntPMOBRValidity = _OlOSCCrntPMOBRValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 14),
    _OlOSCCrntPMOBRValidity_Type()
)
olOSCCrntPMOBRValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMOBRValidity.setStatus("current")
_OlOSCCrntPMCVSValue_Type = Unsigned32
_OlOSCCrntPMCVSValue_Object = MibTableColumn
olOSCCrntPMCVSValue = _OlOSCCrntPMCVSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 15),
    _OlOSCCrntPMCVSValue_Type()
)
olOSCCrntPMCVSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCCrntPMCVSValue.setStatus("current")
_OlOSCCrntPMCVSTimeStamp_Type = DateAndTime
_OlOSCCrntPMCVSTimeStamp_Object = MibTableColumn
olOSCCrntPMCVSTimeStamp = _OlOSCCrntPMCVSTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 16),
    _OlOSCCrntPMCVSTimeStamp_Type()
)
olOSCCrntPMCVSTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMCVSTimeStamp.setStatus("current")
_OlOSCCrntPMCVSValidity_Type = PMValidity
_OlOSCCrntPMCVSValidity_Object = MibTableColumn
olOSCCrntPMCVSValidity = _OlOSCCrntPMCVSValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 17),
    _OlOSCCrntPMCVSValidity_Type()
)
olOSCCrntPMCVSValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMCVSValidity.setStatus("current")
_OlOSCCrntPMCVSInitialize_Type = InitializeCmd
_OlOSCCrntPMCVSInitialize_Object = MibTableColumn
olOSCCrntPMCVSInitialize = _OlOSCCrntPMCVSInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 18),
    _OlOSCCrntPMCVSInitialize_Type()
)
olOSCCrntPMCVSInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCCrntPMCVSInitialize.setStatus("current")
_OlOSCCrntPMESSValue_Type = Unsigned32
_OlOSCCrntPMESSValue_Object = MibTableColumn
olOSCCrntPMESSValue = _OlOSCCrntPMESSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 19),
    _OlOSCCrntPMESSValue_Type()
)
olOSCCrntPMESSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCCrntPMESSValue.setStatus("current")
_OlOSCCrntPMESSTimeStamp_Type = DateAndTime
_OlOSCCrntPMESSTimeStamp_Object = MibTableColumn
olOSCCrntPMESSTimeStamp = _OlOSCCrntPMESSTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 20),
    _OlOSCCrntPMESSTimeStamp_Type()
)
olOSCCrntPMESSTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMESSTimeStamp.setStatus("current")
_OlOSCCrntPMESSValidity_Type = PMValidity
_OlOSCCrntPMESSValidity_Object = MibTableColumn
olOSCCrntPMESSValidity = _OlOSCCrntPMESSValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 21),
    _OlOSCCrntPMESSValidity_Type()
)
olOSCCrntPMESSValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMESSValidity.setStatus("current")
_OlOSCCrntPMESSInitialize_Type = InitializeCmd
_OlOSCCrntPMESSInitialize_Object = MibTableColumn
olOSCCrntPMESSInitialize = _OlOSCCrntPMESSInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 22),
    _OlOSCCrntPMESSInitialize_Type()
)
olOSCCrntPMESSInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCCrntPMESSInitialize.setStatus("current")
_OlOSCCrntPMSESSValue_Type = Unsigned32
_OlOSCCrntPMSESSValue_Object = MibTableColumn
olOSCCrntPMSESSValue = _OlOSCCrntPMSESSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 23),
    _OlOSCCrntPMSESSValue_Type()
)
olOSCCrntPMSESSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCCrntPMSESSValue.setStatus("current")
_OlOSCCrntPMSESSTimeStamp_Type = DateAndTime
_OlOSCCrntPMSESSTimeStamp_Object = MibTableColumn
olOSCCrntPMSESSTimeStamp = _OlOSCCrntPMSESSTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 24),
    _OlOSCCrntPMSESSTimeStamp_Type()
)
olOSCCrntPMSESSTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMSESSTimeStamp.setStatus("current")
_OlOSCCrntPMSESSValidity_Type = PMValidity
_OlOSCCrntPMSESSValidity_Object = MibTableColumn
olOSCCrntPMSESSValidity = _OlOSCCrntPMSESSValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 25),
    _OlOSCCrntPMSESSValidity_Type()
)
olOSCCrntPMSESSValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMSESSValidity.setStatus("current")
_OlOSCCrntPMSESSInitialize_Type = InitializeCmd
_OlOSCCrntPMSESSInitialize_Object = MibTableColumn
olOSCCrntPMSESSInitialize = _OlOSCCrntPMSESSInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 26),
    _OlOSCCrntPMSESSInitialize_Type()
)
olOSCCrntPMSESSInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCCrntPMSESSInitialize.setStatus("current")
_OlOSCCrntPMSEFSSValue_Type = Unsigned32
_OlOSCCrntPMSEFSSValue_Object = MibTableColumn
olOSCCrntPMSEFSSValue = _OlOSCCrntPMSEFSSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 27),
    _OlOSCCrntPMSEFSSValue_Type()
)
olOSCCrntPMSEFSSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCCrntPMSEFSSValue.setStatus("current")
_OlOSCCrntPMSEFSSTimeStamp_Type = DateAndTime
_OlOSCCrntPMSEFSSTimeStamp_Object = MibTableColumn
olOSCCrntPMSEFSSTimeStamp = _OlOSCCrntPMSEFSSTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 28),
    _OlOSCCrntPMSEFSSTimeStamp_Type()
)
olOSCCrntPMSEFSSTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMSEFSSTimeStamp.setStatus("current")
_OlOSCCrntPMSEFSSValidity_Type = PMValidity
_OlOSCCrntPMSEFSSValidity_Object = MibTableColumn
olOSCCrntPMSEFSSValidity = _OlOSCCrntPMSEFSSValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 29),
    _OlOSCCrntPMSEFSSValidity_Type()
)
olOSCCrntPMSEFSSValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMSEFSSValidity.setStatus("current")
_OlOSCCrntPMSEFSSInitialize_Type = InitializeCmd
_OlOSCCrntPMSEFSSInitialize_Object = MibTableColumn
olOSCCrntPMSEFSSInitialize = _OlOSCCrntPMSEFSSInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 30),
    _OlOSCCrntPMSEFSSInitialize_Type()
)
olOSCCrntPMSEFSSInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCCrntPMSEFSSInitialize.setStatus("current")
_OlOSCCrntPMUASSValue_Type = Unsigned32
_OlOSCCrntPMUASSValue_Object = MibTableColumn
olOSCCrntPMUASSValue = _OlOSCCrntPMUASSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 31),
    _OlOSCCrntPMUASSValue_Type()
)
olOSCCrntPMUASSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCCrntPMUASSValue.setStatus("current")
_OlOSCCrntPMUASSTimeStamp_Type = DateAndTime
_OlOSCCrntPMUASSTimeStamp_Object = MibTableColumn
olOSCCrntPMUASSTimeStamp = _OlOSCCrntPMUASSTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 32),
    _OlOSCCrntPMUASSTimeStamp_Type()
)
olOSCCrntPMUASSTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMUASSTimeStamp.setStatus("current")
_OlOSCCrntPMUASSValidity_Type = PMValidity
_OlOSCCrntPMUASSValidity_Object = MibTableColumn
olOSCCrntPMUASSValidity = _OlOSCCrntPMUASSValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 33),
    _OlOSCCrntPMUASSValidity_Type()
)
olOSCCrntPMUASSValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCCrntPMUASSValidity.setStatus("current")
_OlOSCCrntPMUASSInitialize_Type = InitializeCmd
_OlOSCCrntPMUASSInitialize_Object = MibTableColumn
olOSCCrntPMUASSInitialize = _OlOSCCrntPMUASSInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 1, 1, 34),
    _OlOSCCrntPMUASSInitialize_Type()
)
olOSCCrntPMUASSInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCCrntPMUASSInitialize.setStatus("current")
_OlOSCHistPMTable_Object = MibTable
olOSCHistPMTable = _OlOSCHistPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2)
)
if mibBuilder.loadTexts:
    olOSCHistPMTable.setStatus("current")
_OlOSCHistPMEntry_Object = MibTableRow
olOSCHistPMEntry = _OlOSCHistPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1)
)
olOSCHistPMEntry.setIndexNames(
    (0, "BTI-OL-MIB", "olOSCHistPMCpTypeIdx"),
    (0, "BTI-OL-MIB", "olOSCHistPMShelfIdx"),
    (0, "BTI-OL-MIB", "olOSCHistPMSlotIdx"),
    (0, "BTI-OL-MIB", "olOSCHistPMLineIdx"),
    (0, "BTI-OL-MIB", "olOSCHistPMIntervalTypeIdx"),
    (0, "BTI-OL-MIB", "olOSCHistPMIntervalIdx"),
)
if mibBuilder.loadTexts:
    olOSCHistPMEntry.setStatus("current")
_OlOSCHistPMCpTypeIdx_Type = CpType
_OlOSCHistPMCpTypeIdx_Object = MibTableColumn
olOSCHistPMCpTypeIdx = _OlOSCHistPMCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 1),
    _OlOSCHistPMCpTypeIdx_Type()
)
olOSCHistPMCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCHistPMCpTypeIdx.setStatus("current")


class _OlOSCHistPMShelfIdx_Type(Integer32):
    """Custom type olOSCHistPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_OlOSCHistPMShelfIdx_Type.__name__ = "Integer32"
_OlOSCHistPMShelfIdx_Object = MibTableColumn
olOSCHistPMShelfIdx = _OlOSCHistPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 2),
    _OlOSCHistPMShelfIdx_Type()
)
olOSCHistPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCHistPMShelfIdx.setStatus("current")


class _OlOSCHistPMSlotIdx_Type(Integer32):
    """Custom type olOSCHistPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OlOSCHistPMSlotIdx_Type.__name__ = "Integer32"
_OlOSCHistPMSlotIdx_Object = MibTableColumn
olOSCHistPMSlotIdx = _OlOSCHistPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 3),
    _OlOSCHistPMSlotIdx_Type()
)
olOSCHistPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCHistPMSlotIdx.setStatus("current")


class _OlOSCHistPMLineIdx_Type(Integer32):
    """Custom type olOSCHistPMLineIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_OlOSCHistPMLineIdx_Type.__name__ = "Integer32"
_OlOSCHistPMLineIdx_Object = MibTableColumn
olOSCHistPMLineIdx = _OlOSCHistPMLineIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 4),
    _OlOSCHistPMLineIdx_Type()
)
olOSCHistPMLineIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCHistPMLineIdx.setStatus("current")
_OlOSCHistPMIntervalTypeIdx_Type = PMIntervalType
_OlOSCHistPMIntervalTypeIdx_Object = MibTableColumn
olOSCHistPMIntervalTypeIdx = _OlOSCHistPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 5),
    _OlOSCHistPMIntervalTypeIdx_Type()
)
olOSCHistPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCHistPMIntervalTypeIdx.setStatus("current")


class _OlOSCHistPMIntervalIdx_Type(Integer32):
    """Custom type olOSCHistPMIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_OlOSCHistPMIntervalIdx_Type.__name__ = "Integer32"
_OlOSCHistPMIntervalIdx_Object = MibTableColumn
olOSCHistPMIntervalIdx = _OlOSCHistPMIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 6),
    _OlOSCHistPMIntervalIdx_Type()
)
olOSCHistPMIntervalIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCHistPMIntervalIdx.setStatus("current")
_OlOSCHistPMOPRValue_Type = FixedX10
_OlOSCHistPMOPRValue_Object = MibTableColumn
olOSCHistPMOPRValue = _OlOSCHistPMOPRValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 7),
    _OlOSCHistPMOPRValue_Type()
)
olOSCHistPMOPRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMOPRValue.setStatus("current")
if mibBuilder.loadTexts:
    olOSCHistPMOPRValue.setUnits("dBm/10")
_OlOSCHistPMOPRTimeStamp_Type = DateAndTime
_OlOSCHistPMOPRTimeStamp_Object = MibTableColumn
olOSCHistPMOPRTimeStamp = _OlOSCHistPMOPRTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 8),
    _OlOSCHistPMOPRTimeStamp_Type()
)
olOSCHistPMOPRTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMOPRTimeStamp.setStatus("current")
_OlOSCHistPMOPRValidity_Type = PMValidity
_OlOSCHistPMOPRValidity_Object = MibTableColumn
olOSCHistPMOPRValidity = _OlOSCHistPMOPRValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 9),
    _OlOSCHistPMOPRValidity_Type()
)
olOSCHistPMOPRValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMOPRValidity.setStatus("current")
_OlOSCHistPMOPTValue_Type = FixedX10
_OlOSCHistPMOPTValue_Object = MibTableColumn
olOSCHistPMOPTValue = _OlOSCHistPMOPTValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 10),
    _OlOSCHistPMOPTValue_Type()
)
olOSCHistPMOPTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMOPTValue.setStatus("current")
if mibBuilder.loadTexts:
    olOSCHistPMOPTValue.setUnits("dBm/10")
_OlOSCHistPMOPTTimeStamp_Type = DateAndTime
_OlOSCHistPMOPTTimeStamp_Object = MibTableColumn
olOSCHistPMOPTTimeStamp = _OlOSCHistPMOPTTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 11),
    _OlOSCHistPMOPTTimeStamp_Type()
)
olOSCHistPMOPTTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMOPTTimeStamp.setStatus("current")
_OlOSCHistPMOPTValidity_Type = PMValidity
_OlOSCHistPMOPTValidity_Object = MibTableColumn
olOSCHistPMOPTValidity = _OlOSCHistPMOPTValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 12),
    _OlOSCHistPMOPTValidity_Type()
)
olOSCHistPMOPTValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMOPTValidity.setStatus("current")
_OlOSCHistPMOBRValue_Type = FixedX10
_OlOSCHistPMOBRValue_Object = MibTableColumn
olOSCHistPMOBRValue = _OlOSCHistPMOBRValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 13),
    _OlOSCHistPMOBRValue_Type()
)
olOSCHistPMOBRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMOBRValue.setStatus("current")
if mibBuilder.loadTexts:
    olOSCHistPMOBRValue.setUnits("dBm/10")
_OlOSCHistPMOBRTimeStamp_Type = DateAndTime
_OlOSCHistPMOBRTimeStamp_Object = MibTableColumn
olOSCHistPMOBRTimeStamp = _OlOSCHistPMOBRTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 14),
    _OlOSCHistPMOBRTimeStamp_Type()
)
olOSCHistPMOBRTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMOBRTimeStamp.setStatus("current")
_OlOSCHistPMOBRValidity_Type = PMValidity
_OlOSCHistPMOBRValidity_Object = MibTableColumn
olOSCHistPMOBRValidity = _OlOSCHistPMOBRValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 15),
    _OlOSCHistPMOBRValidity_Type()
)
olOSCHistPMOBRValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMOBRValidity.setStatus("current")
_OlOSCHistPMCVSValue_Type = Unsigned32
_OlOSCHistPMCVSValue_Object = MibTableColumn
olOSCHistPMCVSValue = _OlOSCHistPMCVSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 16),
    _OlOSCHistPMCVSValue_Type()
)
olOSCHistPMCVSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCHistPMCVSValue.setStatus("current")
_OlOSCHistPMCVSTimeStamp_Type = DateAndTime
_OlOSCHistPMCVSTimeStamp_Object = MibTableColumn
olOSCHistPMCVSTimeStamp = _OlOSCHistPMCVSTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 17),
    _OlOSCHistPMCVSTimeStamp_Type()
)
olOSCHistPMCVSTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMCVSTimeStamp.setStatus("current")
_OlOSCHistPMCVSValidity_Type = PMValidity
_OlOSCHistPMCVSValidity_Object = MibTableColumn
olOSCHistPMCVSValidity = _OlOSCHistPMCVSValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 18),
    _OlOSCHistPMCVSValidity_Type()
)
olOSCHistPMCVSValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMCVSValidity.setStatus("current")
_OlOSCHistPMCVSInitialize_Type = InitializeCmd
_OlOSCHistPMCVSInitialize_Object = MibTableColumn
olOSCHistPMCVSInitialize = _OlOSCHistPMCVSInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 19),
    _OlOSCHistPMCVSInitialize_Type()
)
olOSCHistPMCVSInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCHistPMCVSInitialize.setStatus("current")
_OlOSCHistPMESSValue_Type = Unsigned32
_OlOSCHistPMESSValue_Object = MibTableColumn
olOSCHistPMESSValue = _OlOSCHistPMESSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 20),
    _OlOSCHistPMESSValue_Type()
)
olOSCHistPMESSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCHistPMESSValue.setStatus("current")
_OlOSCHistPMESSTimeStamp_Type = DateAndTime
_OlOSCHistPMESSTimeStamp_Object = MibTableColumn
olOSCHistPMESSTimeStamp = _OlOSCHistPMESSTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 21),
    _OlOSCHistPMESSTimeStamp_Type()
)
olOSCHistPMESSTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMESSTimeStamp.setStatus("current")
_OlOSCHistPMESSValidity_Type = PMValidity
_OlOSCHistPMESSValidity_Object = MibTableColumn
olOSCHistPMESSValidity = _OlOSCHistPMESSValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 22),
    _OlOSCHistPMESSValidity_Type()
)
olOSCHistPMESSValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMESSValidity.setStatus("current")
_OlOSCHistPMESSInitialize_Type = InitializeCmd
_OlOSCHistPMESSInitialize_Object = MibTableColumn
olOSCHistPMESSInitialize = _OlOSCHistPMESSInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 23),
    _OlOSCHistPMESSInitialize_Type()
)
olOSCHistPMESSInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCHistPMESSInitialize.setStatus("current")
_OlOSCHistPMSESSValue_Type = Unsigned32
_OlOSCHistPMSESSValue_Object = MibTableColumn
olOSCHistPMSESSValue = _OlOSCHistPMSESSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 24),
    _OlOSCHistPMSESSValue_Type()
)
olOSCHistPMSESSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCHistPMSESSValue.setStatus("current")
_OlOSCHistPMSESSTimeStamp_Type = DateAndTime
_OlOSCHistPMSESSTimeStamp_Object = MibTableColumn
olOSCHistPMSESSTimeStamp = _OlOSCHistPMSESSTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 25),
    _OlOSCHistPMSESSTimeStamp_Type()
)
olOSCHistPMSESSTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMSESSTimeStamp.setStatus("current")
_OlOSCHistPMSESSValidity_Type = PMValidity
_OlOSCHistPMSESSValidity_Object = MibTableColumn
olOSCHistPMSESSValidity = _OlOSCHistPMSESSValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 26),
    _OlOSCHistPMSESSValidity_Type()
)
olOSCHistPMSESSValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMSESSValidity.setStatus("current")
_OlOSCHistPMSESSInitialize_Type = InitializeCmd
_OlOSCHistPMSESSInitialize_Object = MibTableColumn
olOSCHistPMSESSInitialize = _OlOSCHistPMSESSInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 27),
    _OlOSCHistPMSESSInitialize_Type()
)
olOSCHistPMSESSInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCHistPMSESSInitialize.setStatus("current")
_OlOSCHistPMSEFSSValue_Type = Unsigned32
_OlOSCHistPMSEFSSValue_Object = MibTableColumn
olOSCHistPMSEFSSValue = _OlOSCHistPMSEFSSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 28),
    _OlOSCHistPMSEFSSValue_Type()
)
olOSCHistPMSEFSSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCHistPMSEFSSValue.setStatus("current")
_OlOSCHistPMSEFSSTimeStamp_Type = DateAndTime
_OlOSCHistPMSEFSSTimeStamp_Object = MibTableColumn
olOSCHistPMSEFSSTimeStamp = _OlOSCHistPMSEFSSTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 29),
    _OlOSCHistPMSEFSSTimeStamp_Type()
)
olOSCHistPMSEFSSTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMSEFSSTimeStamp.setStatus("current")
_OlOSCHistPMSEFSSValidity_Type = PMValidity
_OlOSCHistPMSEFSSValidity_Object = MibTableColumn
olOSCHistPMSEFSSValidity = _OlOSCHistPMSEFSSValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 30),
    _OlOSCHistPMSEFSSValidity_Type()
)
olOSCHistPMSEFSSValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMSEFSSValidity.setStatus("current")
_OlOSCHistPMSEFSSInitialize_Type = InitializeCmd
_OlOSCHistPMSEFSSInitialize_Object = MibTableColumn
olOSCHistPMSEFSSInitialize = _OlOSCHistPMSEFSSInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 31),
    _OlOSCHistPMSEFSSInitialize_Type()
)
olOSCHistPMSEFSSInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCHistPMSEFSSInitialize.setStatus("current")
_OlOSCHistPMUASSValue_Type = Unsigned32
_OlOSCHistPMUASSValue_Object = MibTableColumn
olOSCHistPMUASSValue = _OlOSCHistPMUASSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 32),
    _OlOSCHistPMUASSValue_Type()
)
olOSCHistPMUASSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCHistPMUASSValue.setStatus("current")
_OlOSCHistPMUASSTimeStamp_Type = DateAndTime
_OlOSCHistPMUASSTimeStamp_Object = MibTableColumn
olOSCHistPMUASSTimeStamp = _OlOSCHistPMUASSTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 33),
    _OlOSCHistPMUASSTimeStamp_Type()
)
olOSCHistPMUASSTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMUASSTimeStamp.setStatus("current")
_OlOSCHistPMUASSValidity_Type = PMValidity
_OlOSCHistPMUASSValidity_Object = MibTableColumn
olOSCHistPMUASSValidity = _OlOSCHistPMUASSValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 34),
    _OlOSCHistPMUASSValidity_Type()
)
olOSCHistPMUASSValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olOSCHistPMUASSValidity.setStatus("current")
_OlOSCHistPMUASSInitialize_Type = InitializeCmd
_OlOSCHistPMUASSInitialize_Object = MibTableColumn
olOSCHistPMUASSInitialize = _OlOSCHistPMUASSInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 2, 1, 35),
    _OlOSCHistPMUASSInitialize_Type()
)
olOSCHistPMUASSInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCHistPMUASSInitialize.setStatus("current")
_OlOSCPMThresholdTable_Object = MibTable
olOSCPMThresholdTable = _OlOSCPMThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 3)
)
if mibBuilder.loadTexts:
    olOSCPMThresholdTable.setStatus("current")
_OlOSCPMThresholdEntry_Object = MibTableRow
olOSCPMThresholdEntry = _OlOSCPMThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 3, 1)
)
olOSCPMThresholdEntry.setIndexNames(
    (0, "BTI-OL-MIB", "olOSCPMThresholdCpTypeIdx"),
    (0, "BTI-OL-MIB", "olOSCPMThresholdShelfIdx"),
    (0, "BTI-OL-MIB", "olOSCPMThresholdSlotIdx"),
    (0, "BTI-OL-MIB", "olOSCPMThresholdLineIdx"),
    (0, "BTI-OL-MIB", "olOSCPMThresholdIntervalTypeIdx"),
)
if mibBuilder.loadTexts:
    olOSCPMThresholdEntry.setStatus("current")
_OlOSCPMThresholdCpTypeIdx_Type = CpType
_OlOSCPMThresholdCpTypeIdx_Object = MibTableColumn
olOSCPMThresholdCpTypeIdx = _OlOSCPMThresholdCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 3, 1, 1),
    _OlOSCPMThresholdCpTypeIdx_Type()
)
olOSCPMThresholdCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCPMThresholdCpTypeIdx.setStatus("current")


class _OlOSCPMThresholdShelfIdx_Type(Integer32):
    """Custom type olOSCPMThresholdShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_OlOSCPMThresholdShelfIdx_Type.__name__ = "Integer32"
_OlOSCPMThresholdShelfIdx_Object = MibTableColumn
olOSCPMThresholdShelfIdx = _OlOSCPMThresholdShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 3, 1, 2),
    _OlOSCPMThresholdShelfIdx_Type()
)
olOSCPMThresholdShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCPMThresholdShelfIdx.setStatus("current")


class _OlOSCPMThresholdSlotIdx_Type(Integer32):
    """Custom type olOSCPMThresholdSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OlOSCPMThresholdSlotIdx_Type.__name__ = "Integer32"
_OlOSCPMThresholdSlotIdx_Object = MibTableColumn
olOSCPMThresholdSlotIdx = _OlOSCPMThresholdSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 3, 1, 3),
    _OlOSCPMThresholdSlotIdx_Type()
)
olOSCPMThresholdSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCPMThresholdSlotIdx.setStatus("current")


class _OlOSCPMThresholdLineIdx_Type(Integer32):
    """Custom type olOSCPMThresholdLineIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_OlOSCPMThresholdLineIdx_Type.__name__ = "Integer32"
_OlOSCPMThresholdLineIdx_Object = MibTableColumn
olOSCPMThresholdLineIdx = _OlOSCPMThresholdLineIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 3, 1, 4),
    _OlOSCPMThresholdLineIdx_Type()
)
olOSCPMThresholdLineIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCPMThresholdLineIdx.setStatus("current")
_OlOSCPMThresholdIntervalTypeIdx_Type = PMIntervalType
_OlOSCPMThresholdIntervalTypeIdx_Object = MibTableColumn
olOSCPMThresholdIntervalTypeIdx = _OlOSCPMThresholdIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 3, 1, 5),
    _OlOSCPMThresholdIntervalTypeIdx_Type()
)
olOSCPMThresholdIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olOSCPMThresholdIntervalTypeIdx.setStatus("current")
_OlOSCPMThresholdCVSValue_Type = Unsigned32
_OlOSCPMThresholdCVSValue_Object = MibTableColumn
olOSCPMThresholdCVSValue = _OlOSCPMThresholdCVSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 3, 1, 6),
    _OlOSCPMThresholdCVSValue_Type()
)
olOSCPMThresholdCVSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCPMThresholdCVSValue.setStatus("current")
_OlOSCPMThresholdESSValue_Type = Unsigned32
_OlOSCPMThresholdESSValue_Object = MibTableColumn
olOSCPMThresholdESSValue = _OlOSCPMThresholdESSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 3, 1, 7),
    _OlOSCPMThresholdESSValue_Type()
)
olOSCPMThresholdESSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCPMThresholdESSValue.setStatus("current")
_OlOSCPMThresholdSESSValue_Type = Unsigned32
_OlOSCPMThresholdSESSValue_Object = MibTableColumn
olOSCPMThresholdSESSValue = _OlOSCPMThresholdSESSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 3, 1, 8),
    _OlOSCPMThresholdSESSValue_Type()
)
olOSCPMThresholdSESSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCPMThresholdSESSValue.setStatus("current")
_OlOSCPMThresholdSEFSSValue_Type = Unsigned32
_OlOSCPMThresholdSEFSSValue_Object = MibTableColumn
olOSCPMThresholdSEFSSValue = _OlOSCPMThresholdSEFSSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 3, 1, 9),
    _OlOSCPMThresholdSEFSSValue_Type()
)
olOSCPMThresholdSEFSSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCPMThresholdSEFSSValue.setStatus("current")
_OlOSCPMThresholdUASSValue_Type = Unsigned32
_OlOSCPMThresholdUASSValue_Object = MibTableColumn
olOSCPMThresholdUASSValue = _OlOSCPMThresholdUASSValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 3, 1, 10),
    _OlOSCPMThresholdUASSValue_Type()
)
olOSCPMThresholdUASSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olOSCPMThresholdUASSValue.setStatus("current")
_OlPortCrntPMTable_Object = MibTable
olPortCrntPMTable = _OlPortCrntPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4)
)
if mibBuilder.loadTexts:
    olPortCrntPMTable.setStatus("current")
_OlPortCrntPMEntry_Object = MibTableRow
olPortCrntPMEntry = _OlPortCrntPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1)
)
olPortCrntPMEntry.setIndexNames(
    (0, "BTI-OL-MIB", "olPortCrntPMCpTypeIdx"),
    (0, "BTI-OL-MIB", "olPortCrntPMShelfIdx"),
    (0, "BTI-OL-MIB", "olPortCrntPMSlotIdx"),
    (0, "BTI-OL-MIB", "olPortCrntPMTypeIdx"),
    (0, "BTI-OL-MIB", "olPortCrntPMIdx"),
    (0, "BTI-OL-MIB", "olPortCrntPMIntervalTypeIdx"),
)
if mibBuilder.loadTexts:
    olPortCrntPMEntry.setStatus("current")
_OlPortCrntPMCpTypeIdx_Type = CpType
_OlPortCrntPMCpTypeIdx_Object = MibTableColumn
olPortCrntPMCpTypeIdx = _OlPortCrntPMCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 1),
    _OlPortCrntPMCpTypeIdx_Type()
)
olPortCrntPMCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortCrntPMCpTypeIdx.setStatus("current")


class _OlPortCrntPMShelfIdx_Type(Integer32):
    """Custom type olPortCrntPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_OlPortCrntPMShelfIdx_Type.__name__ = "Integer32"
_OlPortCrntPMShelfIdx_Object = MibTableColumn
olPortCrntPMShelfIdx = _OlPortCrntPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 2),
    _OlPortCrntPMShelfIdx_Type()
)
olPortCrntPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortCrntPMShelfIdx.setStatus("current")


class _OlPortCrntPMSlotIdx_Type(Integer32):
    """Custom type olPortCrntPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OlPortCrntPMSlotIdx_Type.__name__ = "Integer32"
_OlPortCrntPMSlotIdx_Object = MibTableColumn
olPortCrntPMSlotIdx = _OlPortCrntPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 3),
    _OlPortCrntPMSlotIdx_Type()
)
olPortCrntPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortCrntPMSlotIdx.setStatus("current")
_OlPortCrntPMTypeIdx_Type = OlPortType
_OlPortCrntPMTypeIdx_Object = MibTableColumn
olPortCrntPMTypeIdx = _OlPortCrntPMTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 4),
    _OlPortCrntPMTypeIdx_Type()
)
olPortCrntPMTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortCrntPMTypeIdx.setStatus("current")


class _OlPortCrntPMIdx_Type(Integer32):
    """Custom type olPortCrntPMIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_OlPortCrntPMIdx_Type.__name__ = "Integer32"
_OlPortCrntPMIdx_Object = MibTableColumn
olPortCrntPMIdx = _OlPortCrntPMIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 5),
    _OlPortCrntPMIdx_Type()
)
olPortCrntPMIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortCrntPMIdx.setStatus("current")
_OlPortCrntPMIntervalTypeIdx_Type = PMIntervalType
_OlPortCrntPMIntervalTypeIdx_Object = MibTableColumn
olPortCrntPMIntervalTypeIdx = _OlPortCrntPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 6),
    _OlPortCrntPMIntervalTypeIdx_Type()
)
olPortCrntPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortCrntPMIntervalTypeIdx.setStatus("current")
_OlPortCrntPMOPRValue_Type = FixedX10
_OlPortCrntPMOPRValue_Object = MibTableColumn
olPortCrntPMOPRValue = _OlPortCrntPMOPRValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 7),
    _OlPortCrntPMOPRValue_Type()
)
olPortCrntPMOPRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortCrntPMOPRValue.setUnits("dBm/10")
_OlPortCrntPMOPRTimeStamp_Type = DateAndTime
_OlPortCrntPMOPRTimeStamp_Object = MibTableColumn
olPortCrntPMOPRTimeStamp = _OlPortCrntPMOPRTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 8),
    _OlPortCrntPMOPRTimeStamp_Type()
)
olPortCrntPMOPRTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRTimeStamp.setStatus("current")
_OlPortCrntPMOPRValidity_Type = PMValidity
_OlPortCrntPMOPRValidity_Object = MibTableColumn
olPortCrntPMOPRValidity = _OlPortCrntPMOPRValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 9),
    _OlPortCrntPMOPRValidity_Type()
)
olPortCrntPMOPRValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRValidity.setStatus("current")
_OlPortCrntPMOPRMinValue_Type = FixedX10
_OlPortCrntPMOPRMinValue_Object = MibTableColumn
olPortCrntPMOPRMinValue = _OlPortCrntPMOPRMinValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 10),
    _OlPortCrntPMOPRMinValue_Type()
)
olPortCrntPMOPRMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRMinValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortCrntPMOPRMinValue.setUnits("dBm/10")
_OlPortCrntPMOPRMinTimeStamp_Type = DateAndTime
_OlPortCrntPMOPRMinTimeStamp_Object = MibTableColumn
olPortCrntPMOPRMinTimeStamp = _OlPortCrntPMOPRMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 11),
    _OlPortCrntPMOPRMinTimeStamp_Type()
)
olPortCrntPMOPRMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRMinTimeStamp.setStatus("current")
_OlPortCrntPMOPRMinValidity_Type = PMValidity
_OlPortCrntPMOPRMinValidity_Object = MibTableColumn
olPortCrntPMOPRMinValidity = _OlPortCrntPMOPRMinValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 12),
    _OlPortCrntPMOPRMinValidity_Type()
)
olPortCrntPMOPRMinValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRMinValidity.setStatus("current")
_OlPortCrntPMOPRMaxValue_Type = FixedX10
_OlPortCrntPMOPRMaxValue_Object = MibTableColumn
olPortCrntPMOPRMaxValue = _OlPortCrntPMOPRMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 13),
    _OlPortCrntPMOPRMaxValue_Type()
)
olPortCrntPMOPRMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortCrntPMOPRMaxValue.setUnits("dBm/10")
_OlPortCrntPMOPRMaxTimeStamp_Type = DateAndTime
_OlPortCrntPMOPRMaxTimeStamp_Object = MibTableColumn
olPortCrntPMOPRMaxTimeStamp = _OlPortCrntPMOPRMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 14),
    _OlPortCrntPMOPRMaxTimeStamp_Type()
)
olPortCrntPMOPRMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRMaxTimeStamp.setStatus("current")
_OlPortCrntPMOPRMaxValidity_Type = PMValidity
_OlPortCrntPMOPRMaxValidity_Object = MibTableColumn
olPortCrntPMOPRMaxValidity = _OlPortCrntPMOPRMaxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 15),
    _OlPortCrntPMOPRMaxValidity_Type()
)
olPortCrntPMOPRMaxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRMaxValidity.setStatus("current")
_OlPortCrntPMOPRAvgValue_Type = FixedX10
_OlPortCrntPMOPRAvgValue_Object = MibTableColumn
olPortCrntPMOPRAvgValue = _OlPortCrntPMOPRAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 16),
    _OlPortCrntPMOPRAvgValue_Type()
)
olPortCrntPMOPRAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortCrntPMOPRAvgValue.setUnits("dBm/10")
_OlPortCrntPMOPRAvgTimeStamp_Type = DateAndTime
_OlPortCrntPMOPRAvgTimeStamp_Object = MibTableColumn
olPortCrntPMOPRAvgTimeStamp = _OlPortCrntPMOPRAvgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 17),
    _OlPortCrntPMOPRAvgTimeStamp_Type()
)
olPortCrntPMOPRAvgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRAvgTimeStamp.setStatus("current")
_OlPortCrntPMOPRAvgValidity_Type = PMValidity
_OlPortCrntPMOPRAvgValidity_Object = MibTableColumn
olPortCrntPMOPRAvgValidity = _OlPortCrntPMOPRAvgValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 18),
    _OlPortCrntPMOPRAvgValidity_Type()
)
olPortCrntPMOPRAvgValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRAvgValidity.setStatus("current")
_OlPortCrntPMOPRStdDevValue_Type = FixedX10
_OlPortCrntPMOPRStdDevValue_Object = MibTableColumn
olPortCrntPMOPRStdDevValue = _OlPortCrntPMOPRStdDevValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 19),
    _OlPortCrntPMOPRStdDevValue_Type()
)
olPortCrntPMOPRStdDevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRStdDevValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortCrntPMOPRStdDevValue.setUnits("dB/10")
_OlPortCrntPMOPRStdDevTimeStamp_Type = DateAndTime
_OlPortCrntPMOPRStdDevTimeStamp_Object = MibTableColumn
olPortCrntPMOPRStdDevTimeStamp = _OlPortCrntPMOPRStdDevTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 20),
    _OlPortCrntPMOPRStdDevTimeStamp_Type()
)
olPortCrntPMOPRStdDevTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRStdDevTimeStamp.setStatus("current")
_OlPortCrntPMOPRStdDevValidity_Type = PMValidity
_OlPortCrntPMOPRStdDevValidity_Object = MibTableColumn
olPortCrntPMOPRStdDevValidity = _OlPortCrntPMOPRStdDevValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 21),
    _OlPortCrntPMOPRStdDevValidity_Type()
)
olPortCrntPMOPRStdDevValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPRStdDevValidity.setStatus("current")
_OlPortCrntPMOPTValue_Type = FixedX10
_OlPortCrntPMOPTValue_Object = MibTableColumn
olPortCrntPMOPTValue = _OlPortCrntPMOPTValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 22),
    _OlPortCrntPMOPTValue_Type()
)
olPortCrntPMOPTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortCrntPMOPTValue.setUnits("dBm/10")
_OlPortCrntPMOPTTimeStamp_Type = DateAndTime
_OlPortCrntPMOPTTimeStamp_Object = MibTableColumn
olPortCrntPMOPTTimeStamp = _OlPortCrntPMOPTTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 23),
    _OlPortCrntPMOPTTimeStamp_Type()
)
olPortCrntPMOPTTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTTimeStamp.setStatus("current")
_OlPortCrntPMOPTValidity_Type = PMValidity
_OlPortCrntPMOPTValidity_Object = MibTableColumn
olPortCrntPMOPTValidity = _OlPortCrntPMOPTValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 24),
    _OlPortCrntPMOPTValidity_Type()
)
olPortCrntPMOPTValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTValidity.setStatus("current")
_OlPortCrntPMOPTMinValue_Type = FixedX10
_OlPortCrntPMOPTMinValue_Object = MibTableColumn
olPortCrntPMOPTMinValue = _OlPortCrntPMOPTMinValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 25),
    _OlPortCrntPMOPTMinValue_Type()
)
olPortCrntPMOPTMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTMinValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortCrntPMOPTMinValue.setUnits("dBm/10")
_OlPortCrntPMOPTMinTimeStamp_Type = DateAndTime
_OlPortCrntPMOPTMinTimeStamp_Object = MibTableColumn
olPortCrntPMOPTMinTimeStamp = _OlPortCrntPMOPTMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 26),
    _OlPortCrntPMOPTMinTimeStamp_Type()
)
olPortCrntPMOPTMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTMinTimeStamp.setStatus("current")
_OlPortCrntPMOPTMinValidity_Type = PMValidity
_OlPortCrntPMOPTMinValidity_Object = MibTableColumn
olPortCrntPMOPTMinValidity = _OlPortCrntPMOPTMinValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 27),
    _OlPortCrntPMOPTMinValidity_Type()
)
olPortCrntPMOPTMinValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTMinValidity.setStatus("current")
_OlPortCrntPMOPTMaxValue_Type = FixedX10
_OlPortCrntPMOPTMaxValue_Object = MibTableColumn
olPortCrntPMOPTMaxValue = _OlPortCrntPMOPTMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 28),
    _OlPortCrntPMOPTMaxValue_Type()
)
olPortCrntPMOPTMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortCrntPMOPTMaxValue.setUnits("dBm/10")
_OlPortCrntPMOPTMaxTimeStamp_Type = DateAndTime
_OlPortCrntPMOPTMaxTimeStamp_Object = MibTableColumn
olPortCrntPMOPTMaxTimeStamp = _OlPortCrntPMOPTMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 29),
    _OlPortCrntPMOPTMaxTimeStamp_Type()
)
olPortCrntPMOPTMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTMaxTimeStamp.setStatus("current")
_OlPortCrntPMOPTMaxValidity_Type = PMValidity
_OlPortCrntPMOPTMaxValidity_Object = MibTableColumn
olPortCrntPMOPTMaxValidity = _OlPortCrntPMOPTMaxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 30),
    _OlPortCrntPMOPTMaxValidity_Type()
)
olPortCrntPMOPTMaxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTMaxValidity.setStatus("current")
_OlPortCrntPMOPTAvgValue_Type = FixedX10
_OlPortCrntPMOPTAvgValue_Object = MibTableColumn
olPortCrntPMOPTAvgValue = _OlPortCrntPMOPTAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 31),
    _OlPortCrntPMOPTAvgValue_Type()
)
olPortCrntPMOPTAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortCrntPMOPTAvgValue.setUnits("dBm/10")
_OlPortCrntPMOPTAvgTimeStamp_Type = DateAndTime
_OlPortCrntPMOPTAvgTimeStamp_Object = MibTableColumn
olPortCrntPMOPTAvgTimeStamp = _OlPortCrntPMOPTAvgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 32),
    _OlPortCrntPMOPTAvgTimeStamp_Type()
)
olPortCrntPMOPTAvgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTAvgTimeStamp.setStatus("current")
_OlPortCrntPMOPTAvgValidity_Type = PMValidity
_OlPortCrntPMOPTAvgValidity_Object = MibTableColumn
olPortCrntPMOPTAvgValidity = _OlPortCrntPMOPTAvgValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 33),
    _OlPortCrntPMOPTAvgValidity_Type()
)
olPortCrntPMOPTAvgValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTAvgValidity.setStatus("current")
_OlPortCrntPMOPTStdDevValue_Type = FixedX10
_OlPortCrntPMOPTStdDevValue_Object = MibTableColumn
olPortCrntPMOPTStdDevValue = _OlPortCrntPMOPTStdDevValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 34),
    _OlPortCrntPMOPTStdDevValue_Type()
)
olPortCrntPMOPTStdDevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTStdDevValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortCrntPMOPTStdDevValue.setUnits("dB/10")
_OlPortCrntPMOPTStdDevTimeStamp_Type = DateAndTime
_OlPortCrntPMOPTStdDevTimeStamp_Object = MibTableColumn
olPortCrntPMOPTStdDevTimeStamp = _OlPortCrntPMOPTStdDevTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 35),
    _OlPortCrntPMOPTStdDevTimeStamp_Type()
)
olPortCrntPMOPTStdDevTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTStdDevTimeStamp.setStatus("current")
_OlPortCrntPMOPTStdDevValidity_Type = PMValidity
_OlPortCrntPMOPTStdDevValidity_Object = MibTableColumn
olPortCrntPMOPTStdDevValidity = _OlPortCrntPMOPTStdDevValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 36),
    _OlPortCrntPMOPTStdDevValidity_Type()
)
olPortCrntPMOPTStdDevValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMOPTStdDevValidity.setStatus("current")
_OlPortCrntPMLossRxValue_Type = FixedX10
_OlPortCrntPMLossRxValue_Object = MibTableColumn
olPortCrntPMLossRxValue = _OlPortCrntPMLossRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 37),
    _OlPortCrntPMLossRxValue_Type()
)
olPortCrntPMLossRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMLossRxValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortCrntPMLossRxValue.setUnits("dB/10")
_OlPortCrntPMLossRxTimeStamp_Type = DateAndTime
_OlPortCrntPMLossRxTimeStamp_Object = MibTableColumn
olPortCrntPMLossRxTimeStamp = _OlPortCrntPMLossRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 38),
    _OlPortCrntPMLossRxTimeStamp_Type()
)
olPortCrntPMLossRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMLossRxTimeStamp.setStatus("current")
_OlPortCrntPMLossRxValidity_Type = PMValidity
_OlPortCrntPMLossRxValidity_Object = MibTableColumn
olPortCrntPMLossRxValidity = _OlPortCrntPMLossRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 39),
    _OlPortCrntPMLossRxValidity_Type()
)
olPortCrntPMLossRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMLossRxValidity.setStatus("current")
_OlPortCrntPMLossTxValue_Type = FixedX10
_OlPortCrntPMLossTxValue_Object = MibTableColumn
olPortCrntPMLossTxValue = _OlPortCrntPMLossTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 40),
    _OlPortCrntPMLossTxValue_Type()
)
olPortCrntPMLossTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMLossTxValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortCrntPMLossTxValue.setUnits("dB/10")
_OlPortCrntPMLossTxTimeStamp_Type = DateAndTime
_OlPortCrntPMLossTxTimeStamp_Object = MibTableColumn
olPortCrntPMLossTxTimeStamp = _OlPortCrntPMLossTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 41),
    _OlPortCrntPMLossTxTimeStamp_Type()
)
olPortCrntPMLossTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMLossTxTimeStamp.setStatus("current")
_OlPortCrntPMLossTxValidity_Type = PMValidity
_OlPortCrntPMLossTxValidity_Object = MibTableColumn
olPortCrntPMLossTxValidity = _OlPortCrntPMLossTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 42),
    _OlPortCrntPMLossTxValidity_Type()
)
olPortCrntPMLossTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortCrntPMLossTxValidity.setStatus("current")
_OlPortCrntPMInitializeAll_Type = InitializeCmd
_OlPortCrntPMInitializeAll_Object = MibTableColumn
olPortCrntPMInitializeAll = _OlPortCrntPMInitializeAll_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 4, 1, 43),
    _OlPortCrntPMInitializeAll_Type()
)
olPortCrntPMInitializeAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olPortCrntPMInitializeAll.setStatus("current")
_OlPortHistPMTable_Object = MibTable
olPortHistPMTable = _OlPortHistPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5)
)
if mibBuilder.loadTexts:
    olPortHistPMTable.setStatus("current")
_OlPortHistPMEntry_Object = MibTableRow
olPortHistPMEntry = _OlPortHistPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1)
)
olPortHistPMEntry.setIndexNames(
    (0, "BTI-OL-MIB", "olPortHistPMCpTypeIdx"),
    (0, "BTI-OL-MIB", "olPortHistPMShelfIdx"),
    (0, "BTI-OL-MIB", "olPortHistPMSlotIdx"),
    (0, "BTI-OL-MIB", "olPortHistPMTypeIdx"),
    (0, "BTI-OL-MIB", "olPortHistPMIdx"),
    (0, "BTI-OL-MIB", "olPortHistPMIntervalTypeIdx"),
    (0, "BTI-OL-MIB", "olPortHistPMIntervalIdx"),
)
if mibBuilder.loadTexts:
    olPortHistPMEntry.setStatus("current")
_OlPortHistPMCpTypeIdx_Type = CpType
_OlPortHistPMCpTypeIdx_Object = MibTableColumn
olPortHistPMCpTypeIdx = _OlPortHistPMCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 1),
    _OlPortHistPMCpTypeIdx_Type()
)
olPortHistPMCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortHistPMCpTypeIdx.setStatus("current")


class _OlPortHistPMShelfIdx_Type(Integer32):
    """Custom type olPortHistPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_OlPortHistPMShelfIdx_Type.__name__ = "Integer32"
_OlPortHistPMShelfIdx_Object = MibTableColumn
olPortHistPMShelfIdx = _OlPortHistPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 2),
    _OlPortHistPMShelfIdx_Type()
)
olPortHistPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortHistPMShelfIdx.setStatus("current")


class _OlPortHistPMSlotIdx_Type(Integer32):
    """Custom type olPortHistPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OlPortHistPMSlotIdx_Type.__name__ = "Integer32"
_OlPortHistPMSlotIdx_Object = MibTableColumn
olPortHistPMSlotIdx = _OlPortHistPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 3),
    _OlPortHistPMSlotIdx_Type()
)
olPortHistPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortHistPMSlotIdx.setStatus("current")
_OlPortHistPMTypeIdx_Type = OlPortType
_OlPortHistPMTypeIdx_Object = MibTableColumn
olPortHistPMTypeIdx = _OlPortHistPMTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 4),
    _OlPortHistPMTypeIdx_Type()
)
olPortHistPMTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortHistPMTypeIdx.setStatus("current")


class _OlPortHistPMIdx_Type(Integer32):
    """Custom type olPortHistPMIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_OlPortHistPMIdx_Type.__name__ = "Integer32"
_OlPortHistPMIdx_Object = MibTableColumn
olPortHistPMIdx = _OlPortHistPMIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 5),
    _OlPortHistPMIdx_Type()
)
olPortHistPMIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortHistPMIdx.setStatus("current")
_OlPortHistPMIntervalTypeIdx_Type = PMIntervalType
_OlPortHistPMIntervalTypeIdx_Object = MibTableColumn
olPortHistPMIntervalTypeIdx = _OlPortHistPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 6),
    _OlPortHistPMIntervalTypeIdx_Type()
)
olPortHistPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortHistPMIntervalTypeIdx.setStatus("current")


class _OlPortHistPMIntervalIdx_Type(Integer32):
    """Custom type olPortHistPMIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_OlPortHistPMIntervalIdx_Type.__name__ = "Integer32"
_OlPortHistPMIntervalIdx_Object = MibTableColumn
olPortHistPMIntervalIdx = _OlPortHistPMIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 7),
    _OlPortHistPMIntervalIdx_Type()
)
olPortHistPMIntervalIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olPortHistPMIntervalIdx.setStatus("current")
_OlPortHistPMOPRValue_Type = FixedX10
_OlPortHistPMOPRValue_Object = MibTableColumn
olPortHistPMOPRValue = _OlPortHistPMOPRValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 8),
    _OlPortHistPMOPRValue_Type()
)
olPortHistPMOPRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortHistPMOPRValue.setUnits("dBm/10")
_OlPortHistPMOPRTimeStamp_Type = DateAndTime
_OlPortHistPMOPRTimeStamp_Object = MibTableColumn
olPortHistPMOPRTimeStamp = _OlPortHistPMOPRTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 9),
    _OlPortHistPMOPRTimeStamp_Type()
)
olPortHistPMOPRTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRTimeStamp.setStatus("current")
_OlPortHistPMOPRValidity_Type = PMValidity
_OlPortHistPMOPRValidity_Object = MibTableColumn
olPortHistPMOPRValidity = _OlPortHistPMOPRValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 10),
    _OlPortHistPMOPRValidity_Type()
)
olPortHistPMOPRValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRValidity.setStatus("current")
_OlPortHistPMOPRMinValue_Type = FixedX10
_OlPortHistPMOPRMinValue_Object = MibTableColumn
olPortHistPMOPRMinValue = _OlPortHistPMOPRMinValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 11),
    _OlPortHistPMOPRMinValue_Type()
)
olPortHistPMOPRMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRMinValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortHistPMOPRMinValue.setUnits("dBm/10")
_OlPortHistPMOPRMinTimeStamp_Type = DateAndTime
_OlPortHistPMOPRMinTimeStamp_Object = MibTableColumn
olPortHistPMOPRMinTimeStamp = _OlPortHistPMOPRMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 12),
    _OlPortHistPMOPRMinTimeStamp_Type()
)
olPortHistPMOPRMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRMinTimeStamp.setStatus("current")
_OlPortHistPMOPRMinValidity_Type = PMValidity
_OlPortHistPMOPRMinValidity_Object = MibTableColumn
olPortHistPMOPRMinValidity = _OlPortHistPMOPRMinValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 13),
    _OlPortHistPMOPRMinValidity_Type()
)
olPortHistPMOPRMinValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRMinValidity.setStatus("current")
_OlPortHistPMOPRMaxValue_Type = FixedX10
_OlPortHistPMOPRMaxValue_Object = MibTableColumn
olPortHistPMOPRMaxValue = _OlPortHistPMOPRMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 14),
    _OlPortHistPMOPRMaxValue_Type()
)
olPortHistPMOPRMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortHistPMOPRMaxValue.setUnits("dBm/10")
_OlPortHistPMOPRMaxTimeStamp_Type = DateAndTime
_OlPortHistPMOPRMaxTimeStamp_Object = MibTableColumn
olPortHistPMOPRMaxTimeStamp = _OlPortHistPMOPRMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 15),
    _OlPortHistPMOPRMaxTimeStamp_Type()
)
olPortHistPMOPRMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRMaxTimeStamp.setStatus("current")
_OlPortHistPMOPRMaxValidity_Type = PMValidity
_OlPortHistPMOPRMaxValidity_Object = MibTableColumn
olPortHistPMOPRMaxValidity = _OlPortHistPMOPRMaxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 16),
    _OlPortHistPMOPRMaxValidity_Type()
)
olPortHistPMOPRMaxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRMaxValidity.setStatus("current")
_OlPortHistPMOPRAvgValue_Type = FixedX10
_OlPortHistPMOPRAvgValue_Object = MibTableColumn
olPortHistPMOPRAvgValue = _OlPortHistPMOPRAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 17),
    _OlPortHistPMOPRAvgValue_Type()
)
olPortHistPMOPRAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortHistPMOPRAvgValue.setUnits("dBm/10")
_OlPortHistPMOPRAvgTimeStamp_Type = DateAndTime
_OlPortHistPMOPRAvgTimeStamp_Object = MibTableColumn
olPortHistPMOPRAvgTimeStamp = _OlPortHistPMOPRAvgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 18),
    _OlPortHistPMOPRAvgTimeStamp_Type()
)
olPortHistPMOPRAvgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRAvgTimeStamp.setStatus("current")
_OlPortHistPMOPRAvgValidity_Type = PMValidity
_OlPortHistPMOPRAvgValidity_Object = MibTableColumn
olPortHistPMOPRAvgValidity = _OlPortHistPMOPRAvgValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 19),
    _OlPortHistPMOPRAvgValidity_Type()
)
olPortHistPMOPRAvgValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRAvgValidity.setStatus("current")
_OlPortHistPMOPRStdDevValue_Type = FixedX10
_OlPortHistPMOPRStdDevValue_Object = MibTableColumn
olPortHistPMOPRStdDevValue = _OlPortHistPMOPRStdDevValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 20),
    _OlPortHistPMOPRStdDevValue_Type()
)
olPortHistPMOPRStdDevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRStdDevValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortHistPMOPRStdDevValue.setUnits("dB/10")
_OlPortHistPMOPRStdDevTimeStamp_Type = DateAndTime
_OlPortHistPMOPRStdDevTimeStamp_Object = MibTableColumn
olPortHistPMOPRStdDevTimeStamp = _OlPortHistPMOPRStdDevTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 21),
    _OlPortHistPMOPRStdDevTimeStamp_Type()
)
olPortHistPMOPRStdDevTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRStdDevTimeStamp.setStatus("current")
_OlPortHistPMOPRStdDevValidity_Type = PMValidity
_OlPortHistPMOPRStdDevValidity_Object = MibTableColumn
olPortHistPMOPRStdDevValidity = _OlPortHistPMOPRStdDevValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 22),
    _OlPortHistPMOPRStdDevValidity_Type()
)
olPortHistPMOPRStdDevValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPRStdDevValidity.setStatus("current")
_OlPortHistPMOPTValue_Type = FixedX10
_OlPortHistPMOPTValue_Object = MibTableColumn
olPortHistPMOPTValue = _OlPortHistPMOPTValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 23),
    _OlPortHistPMOPTValue_Type()
)
olPortHistPMOPTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortHistPMOPTValue.setUnits("dBm/10")
_OlPortHistPMOPTTimeStamp_Type = DateAndTime
_OlPortHistPMOPTTimeStamp_Object = MibTableColumn
olPortHistPMOPTTimeStamp = _OlPortHistPMOPTTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 24),
    _OlPortHistPMOPTTimeStamp_Type()
)
olPortHistPMOPTTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTTimeStamp.setStatus("current")
_OlPortHistPMOPTValidity_Type = PMValidity
_OlPortHistPMOPTValidity_Object = MibTableColumn
olPortHistPMOPTValidity = _OlPortHistPMOPTValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 25),
    _OlPortHistPMOPTValidity_Type()
)
olPortHistPMOPTValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTValidity.setStatus("current")
_OlPortHistPMOPTMinValue_Type = FixedX10
_OlPortHistPMOPTMinValue_Object = MibTableColumn
olPortHistPMOPTMinValue = _OlPortHistPMOPTMinValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 26),
    _OlPortHistPMOPTMinValue_Type()
)
olPortHistPMOPTMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTMinValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortHistPMOPTMinValue.setUnits("dBm/10")
_OlPortHistPMOPTMinTimeStamp_Type = DateAndTime
_OlPortHistPMOPTMinTimeStamp_Object = MibTableColumn
olPortHistPMOPTMinTimeStamp = _OlPortHistPMOPTMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 27),
    _OlPortHistPMOPTMinTimeStamp_Type()
)
olPortHistPMOPTMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTMinTimeStamp.setStatus("current")
_OlPortHistPMOPTMinValidity_Type = PMValidity
_OlPortHistPMOPTMinValidity_Object = MibTableColumn
olPortHistPMOPTMinValidity = _OlPortHistPMOPTMinValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 28),
    _OlPortHistPMOPTMinValidity_Type()
)
olPortHistPMOPTMinValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTMinValidity.setStatus("current")
_OlPortHistPMOPTMaxValue_Type = FixedX10
_OlPortHistPMOPTMaxValue_Object = MibTableColumn
olPortHistPMOPTMaxValue = _OlPortHistPMOPTMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 29),
    _OlPortHistPMOPTMaxValue_Type()
)
olPortHistPMOPTMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortHistPMOPTMaxValue.setUnits("dBm/10")
_OlPortHistPMOPTMaxTimeStamp_Type = DateAndTime
_OlPortHistPMOPTMaxTimeStamp_Object = MibTableColumn
olPortHistPMOPTMaxTimeStamp = _OlPortHistPMOPTMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 30),
    _OlPortHistPMOPTMaxTimeStamp_Type()
)
olPortHistPMOPTMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTMaxTimeStamp.setStatus("current")
_OlPortHistPMOPTMaxValidity_Type = PMValidity
_OlPortHistPMOPTMaxValidity_Object = MibTableColumn
olPortHistPMOPTMaxValidity = _OlPortHistPMOPTMaxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 31),
    _OlPortHistPMOPTMaxValidity_Type()
)
olPortHistPMOPTMaxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTMaxValidity.setStatus("current")
_OlPortHistPMOPTAvgValue_Type = FixedX10
_OlPortHistPMOPTAvgValue_Object = MibTableColumn
olPortHistPMOPTAvgValue = _OlPortHistPMOPTAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 32),
    _OlPortHistPMOPTAvgValue_Type()
)
olPortHistPMOPTAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortHistPMOPTAvgValue.setUnits("dBm/10")
_OlPortHistPMOPTAvgTimeStamp_Type = DateAndTime
_OlPortHistPMOPTAvgTimeStamp_Object = MibTableColumn
olPortHistPMOPTAvgTimeStamp = _OlPortHistPMOPTAvgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 33),
    _OlPortHistPMOPTAvgTimeStamp_Type()
)
olPortHistPMOPTAvgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTAvgTimeStamp.setStatus("current")
_OlPortHistPMOPTAvgValidity_Type = PMValidity
_OlPortHistPMOPTAvgValidity_Object = MibTableColumn
olPortHistPMOPTAvgValidity = _OlPortHistPMOPTAvgValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 34),
    _OlPortHistPMOPTAvgValidity_Type()
)
olPortHistPMOPTAvgValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTAvgValidity.setStatus("current")
_OlPortHistPMOPTStdDevValue_Type = FixedX10
_OlPortHistPMOPTStdDevValue_Object = MibTableColumn
olPortHistPMOPTStdDevValue = _OlPortHistPMOPTStdDevValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 35),
    _OlPortHistPMOPTStdDevValue_Type()
)
olPortHistPMOPTStdDevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTStdDevValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortHistPMOPTStdDevValue.setUnits("dB/10")
_OlPortHistPMOPTStdDevTimeStamp_Type = DateAndTime
_OlPortHistPMOPTStdDevTimeStamp_Object = MibTableColumn
olPortHistPMOPTStdDevTimeStamp = _OlPortHistPMOPTStdDevTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 36),
    _OlPortHistPMOPTStdDevTimeStamp_Type()
)
olPortHistPMOPTStdDevTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTStdDevTimeStamp.setStatus("current")
_OlPortHistPMOPTStdDevValidity_Type = PMValidity
_OlPortHistPMOPTStdDevValidity_Object = MibTableColumn
olPortHistPMOPTStdDevValidity = _OlPortHistPMOPTStdDevValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 37),
    _OlPortHistPMOPTStdDevValidity_Type()
)
olPortHistPMOPTStdDevValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMOPTStdDevValidity.setStatus("current")
_OlPortHistPMLossRxValue_Type = FixedX10
_OlPortHistPMLossRxValue_Object = MibTableColumn
olPortHistPMLossRxValue = _OlPortHistPMLossRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 38),
    _OlPortHistPMLossRxValue_Type()
)
olPortHistPMLossRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMLossRxValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortHistPMLossRxValue.setUnits("dB/10")
_OlPortHistPMLossRxTimeStamp_Type = DateAndTime
_OlPortHistPMLossRxTimeStamp_Object = MibTableColumn
olPortHistPMLossRxTimeStamp = _OlPortHistPMLossRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 39),
    _OlPortHistPMLossRxTimeStamp_Type()
)
olPortHistPMLossRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMLossRxTimeStamp.setStatus("current")
_OlPortHistPMLossRxValidity_Type = PMValidity
_OlPortHistPMLossRxValidity_Object = MibTableColumn
olPortHistPMLossRxValidity = _OlPortHistPMLossRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 40),
    _OlPortHistPMLossRxValidity_Type()
)
olPortHistPMLossRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMLossRxValidity.setStatus("current")
_OlPortHistPMLossTxValue_Type = FixedX10
_OlPortHistPMLossTxValue_Object = MibTableColumn
olPortHistPMLossTxValue = _OlPortHistPMLossTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 41),
    _OlPortHistPMLossTxValue_Type()
)
olPortHistPMLossTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMLossTxValue.setStatus("current")
if mibBuilder.loadTexts:
    olPortHistPMLossTxValue.setUnits("dB/10")
_OlPortHistPMLossTxTimeStamp_Type = DateAndTime
_OlPortHistPMLossTxTimeStamp_Object = MibTableColumn
olPortHistPMLossTxTimeStamp = _OlPortHistPMLossTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 42),
    _OlPortHistPMLossTxTimeStamp_Type()
)
olPortHistPMLossTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMLossTxTimeStamp.setStatus("current")
_OlPortHistPMLossTxValidity_Type = PMValidity
_OlPortHistPMLossTxValidity_Object = MibTableColumn
olPortHistPMLossTxValidity = _OlPortHistPMLossTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 43),
    _OlPortHistPMLossTxValidity_Type()
)
olPortHistPMLossTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortHistPMLossTxValidity.setStatus("current")
_OlPortHistPMInitializeAll_Type = InitializeCmd
_OlPortHistPMInitializeAll_Object = MibTableColumn
olPortHistPMInitializeAll = _OlPortHistPMInitializeAll_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 5, 1, 44),
    _OlPortHistPMInitializeAll_Type()
)
olPortHistPMInitializeAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olPortHistPMInitializeAll.setStatus("current")
_WchCrntPMTable_Object = MibTable
wchCrntPMTable = _WchCrntPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6)
)
if mibBuilder.loadTexts:
    wchCrntPMTable.setStatus("current")
_WchCrntPMEntry_Object = MibTableRow
wchCrntPMEntry = _WchCrntPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1)
)
wchCrntPMEntry.setIndexNames(
    (0, "BTI-OL-MIB", "wchCrntPMCpTypeIdx"),
    (0, "BTI-OL-MIB", "wchCrntPMShelfIdx"),
    (0, "BTI-OL-MIB", "wchCrntPMSlotIdx"),
    (0, "BTI-OL-MIB", "wchCrntPMPortTypeIdx"),
    (0, "BTI-OL-MIB", "wchCrntPMPortIdx"),
    (0, "BTI-OL-MIB", "wchCrntPMIdx"),
    (0, "BTI-OL-MIB", "wchCrntPMIntervalTypeIdx"),
)
if mibBuilder.loadTexts:
    wchCrntPMEntry.setStatus("current")
_WchCrntPMCpTypeIdx_Type = CpType
_WchCrntPMCpTypeIdx_Object = MibTableColumn
wchCrntPMCpTypeIdx = _WchCrntPMCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 1),
    _WchCrntPMCpTypeIdx_Type()
)
wchCrntPMCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchCrntPMCpTypeIdx.setStatus("current")


class _WchCrntPMShelfIdx_Type(Integer32):
    """Custom type wchCrntPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_WchCrntPMShelfIdx_Type.__name__ = "Integer32"
_WchCrntPMShelfIdx_Object = MibTableColumn
wchCrntPMShelfIdx = _WchCrntPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 2),
    _WchCrntPMShelfIdx_Type()
)
wchCrntPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchCrntPMShelfIdx.setStatus("current")


class _WchCrntPMSlotIdx_Type(Integer32):
    """Custom type wchCrntPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WchCrntPMSlotIdx_Type.__name__ = "Integer32"
_WchCrntPMSlotIdx_Object = MibTableColumn
wchCrntPMSlotIdx = _WchCrntPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 3),
    _WchCrntPMSlotIdx_Type()
)
wchCrntPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchCrntPMSlotIdx.setStatus("current")
_WchCrntPMPortTypeIdx_Type = OlPortType
_WchCrntPMPortTypeIdx_Object = MibTableColumn
wchCrntPMPortTypeIdx = _WchCrntPMPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 4),
    _WchCrntPMPortTypeIdx_Type()
)
wchCrntPMPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchCrntPMPortTypeIdx.setStatus("current")


class _WchCrntPMPortIdx_Type(Integer32):
    """Custom type wchCrntPMPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WchCrntPMPortIdx_Type.__name__ = "Integer32"
_WchCrntPMPortIdx_Object = MibTableColumn
wchCrntPMPortIdx = _WchCrntPMPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 5),
    _WchCrntPMPortIdx_Type()
)
wchCrntPMPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchCrntPMPortIdx.setStatus("current")


class _WchCrntPMIdx_Type(Integer32):
    """Custom type wchCrntPMIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(135, 610),
    )


_WchCrntPMIdx_Type.__name__ = "Integer32"
_WchCrntPMIdx_Object = MibTableColumn
wchCrntPMIdx = _WchCrntPMIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 6),
    _WchCrntPMIdx_Type()
)
wchCrntPMIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchCrntPMIdx.setStatus("current")
_WchCrntPMIntervalTypeIdx_Type = PMIntervalType
_WchCrntPMIntervalTypeIdx_Object = MibTableColumn
wchCrntPMIntervalTypeIdx = _WchCrntPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 7),
    _WchCrntPMIntervalTypeIdx_Type()
)
wchCrntPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchCrntPMIntervalTypeIdx.setStatus("current")
_WchCrntPMOPRValue_Type = FixedX10
_WchCrntPMOPRValue_Object = MibTableColumn
wchCrntPMOPRValue = _WchCrntPMOPRValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 8),
    _WchCrntPMOPRValue_Type()
)
wchCrntPMOPRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchCrntPMOPRValue.setStatus("current")
if mibBuilder.loadTexts:
    wchCrntPMOPRValue.setUnits("dBm/10")
_WchCrntPMOPRTimeStamp_Type = DateAndTime
_WchCrntPMOPRTimeStamp_Object = MibTableColumn
wchCrntPMOPRTimeStamp = _WchCrntPMOPRTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 9),
    _WchCrntPMOPRTimeStamp_Type()
)
wchCrntPMOPRTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchCrntPMOPRTimeStamp.setStatus("current")
_WchCrntPMOPRValidity_Type = PMValidity
_WchCrntPMOPRValidity_Object = MibTableColumn
wchCrntPMOPRValidity = _WchCrntPMOPRValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 10),
    _WchCrntPMOPRValidity_Type()
)
wchCrntPMOPRValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchCrntPMOPRValidity.setStatus("current")
_WchCrntPMOPRMinValue_Type = FixedX10
_WchCrntPMOPRMinValue_Object = MibTableColumn
wchCrntPMOPRMinValue = _WchCrntPMOPRMinValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 11),
    _WchCrntPMOPRMinValue_Type()
)
wchCrntPMOPRMinValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchCrntPMOPRMinValue.setStatus("current")
if mibBuilder.loadTexts:
    wchCrntPMOPRMinValue.setUnits("dBm/10")
_WchCrntPMOPRMinTimeStamp_Type = DateAndTime
_WchCrntPMOPRMinTimeStamp_Object = MibTableColumn
wchCrntPMOPRMinTimeStamp = _WchCrntPMOPRMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 12),
    _WchCrntPMOPRMinTimeStamp_Type()
)
wchCrntPMOPRMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchCrntPMOPRMinTimeStamp.setStatus("current")
_WchCrntPMOPRMinValidity_Type = PMValidity
_WchCrntPMOPRMinValidity_Object = MibTableColumn
wchCrntPMOPRMinValidity = _WchCrntPMOPRMinValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 13),
    _WchCrntPMOPRMinValidity_Type()
)
wchCrntPMOPRMinValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchCrntPMOPRMinValidity.setStatus("current")
_WchCrntPMOPRMinInitialize_Type = InitializeCmd
_WchCrntPMOPRMinInitialize_Object = MibTableColumn
wchCrntPMOPRMinInitialize = _WchCrntPMOPRMinInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 14),
    _WchCrntPMOPRMinInitialize_Type()
)
wchCrntPMOPRMinInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchCrntPMOPRMinInitialize.setStatus("current")
_WchCrntPMOPRMaxValue_Type = FixedX10
_WchCrntPMOPRMaxValue_Object = MibTableColumn
wchCrntPMOPRMaxValue = _WchCrntPMOPRMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 15),
    _WchCrntPMOPRMaxValue_Type()
)
wchCrntPMOPRMaxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchCrntPMOPRMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    wchCrntPMOPRMaxValue.setUnits("dBm/10")
_WchCrntPMOPRMaxTimeStamp_Type = DateAndTime
_WchCrntPMOPRMaxTimeStamp_Object = MibTableColumn
wchCrntPMOPRMaxTimeStamp = _WchCrntPMOPRMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 16),
    _WchCrntPMOPRMaxTimeStamp_Type()
)
wchCrntPMOPRMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchCrntPMOPRMaxTimeStamp.setStatus("current")
_WchCrntPMOPRMaxValidity_Type = PMValidity
_WchCrntPMOPRMaxValidity_Object = MibTableColumn
wchCrntPMOPRMaxValidity = _WchCrntPMOPRMaxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 17),
    _WchCrntPMOPRMaxValidity_Type()
)
wchCrntPMOPRMaxValidity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchCrntPMOPRMaxValidity.setStatus("current")
_WchCrntPMOPRMaxInitialize_Type = InitializeCmd
_WchCrntPMOPRMaxInitialize_Object = MibTableColumn
wchCrntPMOPRMaxInitialize = _WchCrntPMOPRMaxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 18),
    _WchCrntPMOPRMaxInitialize_Type()
)
wchCrntPMOPRMaxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchCrntPMOPRMaxInitialize.setStatus("current")
_WchCrntPMOPTValue_Type = FixedX10
_WchCrntPMOPTValue_Object = MibTableColumn
wchCrntPMOPTValue = _WchCrntPMOPTValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 19),
    _WchCrntPMOPTValue_Type()
)
wchCrntPMOPTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchCrntPMOPTValue.setStatus("current")
if mibBuilder.loadTexts:
    wchCrntPMOPTValue.setUnits("dBm/10")
_WchCrntPMOPTTimeStamp_Type = DateAndTime
_WchCrntPMOPTTimeStamp_Object = MibTableColumn
wchCrntPMOPTTimeStamp = _WchCrntPMOPTTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 20),
    _WchCrntPMOPTTimeStamp_Type()
)
wchCrntPMOPTTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchCrntPMOPTTimeStamp.setStatus("current")
_WchCrntPMOPTValidity_Type = PMValidity
_WchCrntPMOPTValidity_Object = MibTableColumn
wchCrntPMOPTValidity = _WchCrntPMOPTValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 21),
    _WchCrntPMOPTValidity_Type()
)
wchCrntPMOPTValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchCrntPMOPTValidity.setStatus("current")
_WchCrntPMOPTMinValue_Type = FixedX10
_WchCrntPMOPTMinValue_Object = MibTableColumn
wchCrntPMOPTMinValue = _WchCrntPMOPTMinValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 22),
    _WchCrntPMOPTMinValue_Type()
)
wchCrntPMOPTMinValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchCrntPMOPTMinValue.setStatus("current")
if mibBuilder.loadTexts:
    wchCrntPMOPTMinValue.setUnits("dBm/10")
_WchCrntPMOPTMinTimeStamp_Type = DateAndTime
_WchCrntPMOPTMinTimeStamp_Object = MibTableColumn
wchCrntPMOPTMinTimeStamp = _WchCrntPMOPTMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 23),
    _WchCrntPMOPTMinTimeStamp_Type()
)
wchCrntPMOPTMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchCrntPMOPTMinTimeStamp.setStatus("current")
_WchCrntPMOPTMinValidity_Type = PMValidity
_WchCrntPMOPTMinValidity_Object = MibTableColumn
wchCrntPMOPTMinValidity = _WchCrntPMOPTMinValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 24),
    _WchCrntPMOPTMinValidity_Type()
)
wchCrntPMOPTMinValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchCrntPMOPTMinValidity.setStatus("current")
_WchCrntPMOPTMinInitialize_Type = InitializeCmd
_WchCrntPMOPTMinInitialize_Object = MibTableColumn
wchCrntPMOPTMinInitialize = _WchCrntPMOPTMinInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 25),
    _WchCrntPMOPTMinInitialize_Type()
)
wchCrntPMOPTMinInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchCrntPMOPTMinInitialize.setStatus("current")
_WchCrntPMOPTMaxValue_Type = FixedX10
_WchCrntPMOPTMaxValue_Object = MibTableColumn
wchCrntPMOPTMaxValue = _WchCrntPMOPTMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 26),
    _WchCrntPMOPTMaxValue_Type()
)
wchCrntPMOPTMaxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchCrntPMOPTMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    wchCrntPMOPTMaxValue.setUnits("dBm/10")
_WchCrntPMOPTMaxTimeStamp_Type = DateAndTime
_WchCrntPMOPTMaxTimeStamp_Object = MibTableColumn
wchCrntPMOPTMaxTimeStamp = _WchCrntPMOPTMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 27),
    _WchCrntPMOPTMaxTimeStamp_Type()
)
wchCrntPMOPTMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchCrntPMOPTMaxTimeStamp.setStatus("current")
_WchCrntPMOPTMaxValidity_Type = PMValidity
_WchCrntPMOPTMaxValidity_Object = MibTableColumn
wchCrntPMOPTMaxValidity = _WchCrntPMOPTMaxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 28),
    _WchCrntPMOPTMaxValidity_Type()
)
wchCrntPMOPTMaxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchCrntPMOPTMaxValidity.setStatus("current")
_WchCrntPMOPTMaxInitialize_Type = InitializeCmd
_WchCrntPMOPTMaxInitialize_Object = MibTableColumn
wchCrntPMOPTMaxInitialize = _WchCrntPMOPTMaxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 6, 1, 29),
    _WchCrntPMOPTMaxInitialize_Type()
)
wchCrntPMOPTMaxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchCrntPMOPTMaxInitialize.setStatus("current")
_WchHistPMTable_Object = MibTable
wchHistPMTable = _WchHistPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7)
)
if mibBuilder.loadTexts:
    wchHistPMTable.setStatus("current")
_WchHistPMEntry_Object = MibTableRow
wchHistPMEntry = _WchHistPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1)
)
wchHistPMEntry.setIndexNames(
    (0, "BTI-OL-MIB", "wchHistPMCpTypeIdx"),
    (0, "BTI-OL-MIB", "wchHistPMShelfIdx"),
    (0, "BTI-OL-MIB", "wchHistPMSlotIdx"),
    (0, "BTI-OL-MIB", "wchHistPMPortTypeIdx"),
    (0, "BTI-OL-MIB", "wchHistPMPortIdx"),
    (0, "BTI-OL-MIB", "wchHistPMIdx"),
    (0, "BTI-OL-MIB", "wchHistPMIntervalTypeIdx"),
    (0, "BTI-OL-MIB", "wchHistPMIntervalIdx"),
)
if mibBuilder.loadTexts:
    wchHistPMEntry.setStatus("current")
_WchHistPMCpTypeIdx_Type = CpType
_WchHistPMCpTypeIdx_Object = MibTableColumn
wchHistPMCpTypeIdx = _WchHistPMCpTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 1),
    _WchHistPMCpTypeIdx_Type()
)
wchHistPMCpTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchHistPMCpTypeIdx.setStatus("current")


class _WchHistPMShelfIdx_Type(Integer32):
    """Custom type wchHistPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_WchHistPMShelfIdx_Type.__name__ = "Integer32"
_WchHistPMShelfIdx_Object = MibTableColumn
wchHistPMShelfIdx = _WchHistPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 2),
    _WchHistPMShelfIdx_Type()
)
wchHistPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchHistPMShelfIdx.setStatus("current")


class _WchHistPMSlotIdx_Type(Integer32):
    """Custom type wchHistPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WchHistPMSlotIdx_Type.__name__ = "Integer32"
_WchHistPMSlotIdx_Object = MibTableColumn
wchHistPMSlotIdx = _WchHistPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 3),
    _WchHistPMSlotIdx_Type()
)
wchHistPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchHistPMSlotIdx.setStatus("current")
_WchHistPMPortTypeIdx_Type = OlPortType
_WchHistPMPortTypeIdx_Object = MibTableColumn
wchHistPMPortTypeIdx = _WchHistPMPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 4),
    _WchHistPMPortTypeIdx_Type()
)
wchHistPMPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchHistPMPortTypeIdx.setStatus("current")


class _WchHistPMPortIdx_Type(Integer32):
    """Custom type wchHistPMPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WchHistPMPortIdx_Type.__name__ = "Integer32"
_WchHistPMPortIdx_Object = MibTableColumn
wchHistPMPortIdx = _WchHistPMPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 5),
    _WchHistPMPortIdx_Type()
)
wchHistPMPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchHistPMPortIdx.setStatus("current")


class _WchHistPMIdx_Type(Integer32):
    """Custom type wchHistPMIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(135, 610),
    )


_WchHistPMIdx_Type.__name__ = "Integer32"
_WchHistPMIdx_Object = MibTableColumn
wchHistPMIdx = _WchHistPMIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 6),
    _WchHistPMIdx_Type()
)
wchHistPMIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchHistPMIdx.setStatus("current")
_WchHistPMIntervalTypeIdx_Type = PMIntervalType
_WchHistPMIntervalTypeIdx_Object = MibTableColumn
wchHistPMIntervalTypeIdx = _WchHistPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 7),
    _WchHistPMIntervalTypeIdx_Type()
)
wchHistPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchHistPMIntervalTypeIdx.setStatus("current")


class _WchHistPMIntervalIdx_Type(Integer32):
    """Custom type wchHistPMIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_WchHistPMIntervalIdx_Type.__name__ = "Integer32"
_WchHistPMIntervalIdx_Object = MibTableColumn
wchHistPMIntervalIdx = _WchHistPMIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 8),
    _WchHistPMIntervalIdx_Type()
)
wchHistPMIntervalIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wchHistPMIntervalIdx.setStatus("current")
_WchHistPMOPRValue_Type = FixedX10
_WchHistPMOPRValue_Object = MibTableColumn
wchHistPMOPRValue = _WchHistPMOPRValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 9),
    _WchHistPMOPRValue_Type()
)
wchHistPMOPRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPRValue.setStatus("current")
if mibBuilder.loadTexts:
    wchHistPMOPRValue.setUnits("dBm/10")
_WchHistPMOPRTimeStamp_Type = DateAndTime
_WchHistPMOPRTimeStamp_Object = MibTableColumn
wchHistPMOPRTimeStamp = _WchHistPMOPRTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 10),
    _WchHistPMOPRTimeStamp_Type()
)
wchHistPMOPRTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPRTimeStamp.setStatus("current")
_WchHistPMOPRValidity_Type = PMValidity
_WchHistPMOPRValidity_Object = MibTableColumn
wchHistPMOPRValidity = _WchHistPMOPRValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 11),
    _WchHistPMOPRValidity_Type()
)
wchHistPMOPRValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPRValidity.setStatus("current")
_WchHistPMOPRMinValue_Type = FixedX10
_WchHistPMOPRMinValue_Object = MibTableColumn
wchHistPMOPRMinValue = _WchHistPMOPRMinValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 12),
    _WchHistPMOPRMinValue_Type()
)
wchHistPMOPRMinValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchHistPMOPRMinValue.setStatus("current")
if mibBuilder.loadTexts:
    wchHistPMOPRMinValue.setUnits("dBm/10")
_WchHistPMOPRMinTimeStamp_Type = DateAndTime
_WchHistPMOPRMinTimeStamp_Object = MibTableColumn
wchHistPMOPRMinTimeStamp = _WchHistPMOPRMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 13),
    _WchHistPMOPRMinTimeStamp_Type()
)
wchHistPMOPRMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPRMinTimeStamp.setStatus("current")
_WchHistPMOPRMinValidity_Type = PMValidity
_WchHistPMOPRMinValidity_Object = MibTableColumn
wchHistPMOPRMinValidity = _WchHistPMOPRMinValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 14),
    _WchHistPMOPRMinValidity_Type()
)
wchHistPMOPRMinValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPRMinValidity.setStatus("current")
_WchHistPMOPRMinInitialize_Type = InitializeCmd
_WchHistPMOPRMinInitialize_Object = MibTableColumn
wchHistPMOPRMinInitialize = _WchHistPMOPRMinInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 15),
    _WchHistPMOPRMinInitialize_Type()
)
wchHistPMOPRMinInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchHistPMOPRMinInitialize.setStatus("current")
_WchHistPMOPRMaxValue_Type = FixedX10
_WchHistPMOPRMaxValue_Object = MibTableColumn
wchHistPMOPRMaxValue = _WchHistPMOPRMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 16),
    _WchHistPMOPRMaxValue_Type()
)
wchHistPMOPRMaxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchHistPMOPRMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    wchHistPMOPRMaxValue.setUnits("dBm/10")
_WchHistPMOPRMaxTimeStamp_Type = DateAndTime
_WchHistPMOPRMaxTimeStamp_Object = MibTableColumn
wchHistPMOPRMaxTimeStamp = _WchHistPMOPRMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 17),
    _WchHistPMOPRMaxTimeStamp_Type()
)
wchHistPMOPRMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPRMaxTimeStamp.setStatus("current")
_WchHistPMOPRMaxValidity_Type = PMValidity
_WchHistPMOPRMaxValidity_Object = MibTableColumn
wchHistPMOPRMaxValidity = _WchHistPMOPRMaxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 18),
    _WchHistPMOPRMaxValidity_Type()
)
wchHistPMOPRMaxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPRMaxValidity.setStatus("current")
_WchHistPMOPRMaxInitialize_Type = InitializeCmd
_WchHistPMOPRMaxInitialize_Object = MibTableColumn
wchHistPMOPRMaxInitialize = _WchHistPMOPRMaxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 19),
    _WchHistPMOPRMaxInitialize_Type()
)
wchHistPMOPRMaxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchHistPMOPRMaxInitialize.setStatus("current")
_WchHistPMOPTValue_Type = FixedX10
_WchHistPMOPTValue_Object = MibTableColumn
wchHistPMOPTValue = _WchHistPMOPTValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 20),
    _WchHistPMOPTValue_Type()
)
wchHistPMOPTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPTValue.setStatus("current")
if mibBuilder.loadTexts:
    wchHistPMOPTValue.setUnits("dBm/10")
_WchHistPMOPTTimeStamp_Type = DateAndTime
_WchHistPMOPTTimeStamp_Object = MibTableColumn
wchHistPMOPTTimeStamp = _WchHistPMOPTTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 21),
    _WchHistPMOPTTimeStamp_Type()
)
wchHistPMOPTTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPTTimeStamp.setStatus("current")
_WchHistPMOPTValidity_Type = PMValidity
_WchHistPMOPTValidity_Object = MibTableColumn
wchHistPMOPTValidity = _WchHistPMOPTValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 22),
    _WchHistPMOPTValidity_Type()
)
wchHistPMOPTValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPTValidity.setStatus("current")
_WchHistPMOPTMinValue_Type = FixedX10
_WchHistPMOPTMinValue_Object = MibTableColumn
wchHistPMOPTMinValue = _WchHistPMOPTMinValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 23),
    _WchHistPMOPTMinValue_Type()
)
wchHistPMOPTMinValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchHistPMOPTMinValue.setStatus("current")
if mibBuilder.loadTexts:
    wchHistPMOPTMinValue.setUnits("dBm/10")
_WchHistPMOPTMinTimeStamp_Type = DateAndTime
_WchHistPMOPTMinTimeStamp_Object = MibTableColumn
wchHistPMOPTMinTimeStamp = _WchHistPMOPTMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 24),
    _WchHistPMOPTMinTimeStamp_Type()
)
wchHistPMOPTMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPTMinTimeStamp.setStatus("current")
_WchHistPMOPTMinValidity_Type = PMValidity
_WchHistPMOPTMinValidity_Object = MibTableColumn
wchHistPMOPTMinValidity = _WchHistPMOPTMinValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 25),
    _WchHistPMOPTMinValidity_Type()
)
wchHistPMOPTMinValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPTMinValidity.setStatus("current")
_WchHistPMOPTMinInitialize_Type = InitializeCmd
_WchHistPMOPTMinInitialize_Object = MibTableColumn
wchHistPMOPTMinInitialize = _WchHistPMOPTMinInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 26),
    _WchHistPMOPTMinInitialize_Type()
)
wchHistPMOPTMinInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchHistPMOPTMinInitialize.setStatus("current")
_WchHistPMOPTMaxValue_Type = FixedX10
_WchHistPMOPTMaxValue_Object = MibTableColumn
wchHistPMOPTMaxValue = _WchHistPMOPTMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 27),
    _WchHistPMOPTMaxValue_Type()
)
wchHistPMOPTMaxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchHistPMOPTMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    wchHistPMOPTMaxValue.setUnits("dBm/10")
_WchHistPMOPTMaxTimeStamp_Type = DateAndTime
_WchHistPMOPTMaxTimeStamp_Object = MibTableColumn
wchHistPMOPTMaxTimeStamp = _WchHistPMOPTMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 28),
    _WchHistPMOPTMaxTimeStamp_Type()
)
wchHistPMOPTMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPTMaxTimeStamp.setStatus("current")
_WchHistPMOPTMaxValidity_Type = PMValidity
_WchHistPMOPTMaxValidity_Object = MibTableColumn
wchHistPMOPTMaxValidity = _WchHistPMOPTMaxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 29),
    _WchHistPMOPTMaxValidity_Type()
)
wchHistPMOPTMaxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wchHistPMOPTMaxValidity.setStatus("current")
_WchHistPMOPTMaxInitialize_Type = InitializeCmd
_WchHistPMOPTMaxInitialize_Object = MibTableColumn
wchHistPMOPTMaxInitialize = _WchHistPMOPTMaxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 16, 12, 7, 1, 30),
    _WchHistPMOPTMaxInitialize_Type()
)
wchHistPMOPTMaxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wchHistPMOPTMaxInitialize.setStatus("current")
_OlOSCEvtNotifications_ObjectIdentity = ObjectIdentity
olOSCEvtNotifications = _OlOSCEvtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 33, 1)
)
_OlPortEvtNotifications_ObjectIdentity = ObjectIdentity
olPortEvtNotifications = _OlPortEvtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 33, 2)
)
_WdmEvtNotifications_ObjectIdentity = ObjectIdentity
wdmEvtNotifications = _WdmEvtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 33, 3)
)
_WchEvtNotifications_ObjectIdentity = ObjectIdentity
wchEvtNotifications = _WchEvtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 33, 4)
)
_OlOSCCondNotifications_ObjectIdentity = ObjectIdentity
olOSCCondNotifications = _OlOSCCondNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1)
)
_OlPortCondNotifications_ObjectIdentity = ObjectIdentity
olPortCondNotifications = _OlPortCondNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2)
)
_WdmCondNotifications_ObjectIdentity = ObjectIdentity
wdmCondNotifications = _WdmCondNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 3)
)
_WchCondNotifications_ObjectIdentity = ObjectIdentity
wchCondNotifications = _WchCondNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4)
)

# Managed Objects groups


# Notification objects

olOSCStatusChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 33, 1, 0, 1)
)
olOSCStatusChangeEvt.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-OL-MIB", "olOSCOperStatus"),
        ("BTI-OL-MIB", "olOSCOperStatQlfr"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    olOSCStatusChangeEvt.setStatus(
        "current"
    )

olOSCTcaEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 33, 1, 0, 2)
)
olOSCTcaEvt.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "tcaIntervalType"),
        ("BTI-7000-MIB", "tcaDateAndTime"),
        ("BTI-7000-MIB", "tcaMontype"),
        ("BTI-7000-MIB", "tcaValue"),
        ("BTI-7000-MIB", "tcaThreshold"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    olOSCTcaEvt.setStatus(
        "current"
    )

olPortStatusChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 33, 2, 0, 1)
)
olPortStatusChangeEvt.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-OL-MIB", "olPortOperStatus"),
        ("BTI-OL-MIB", "olPortOperStatQlfr"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    olPortStatusChangeEvt.setStatus(
        "current"
    )

wdmStatusChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 33, 3, 0, 1)
)
wdmStatusChangeEvt.setObjects(
      *(("BTI-OL-MIB", "wdmCpTypeIdx"),
        ("BTI-OL-MIB", "wdmShelfIdx"),
        ("BTI-OL-MIB", "wdmSlotIdx"),
        ("BTI-OL-MIB", "wdmLineIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-OL-MIB", "wdmOperStatus"),
        ("BTI-OL-MIB", "wdmOperStatQlfr"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    wdmStatusChangeEvt.setStatus(
        "current"
    )

wchStatusChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 33, 4, 0, 1)
)
wchStatusChangeEvt.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-OL-MIB", "wchOperStatus"),
        ("BTI-OL-MIB", "wchOperStatQlfr"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    wchStatusChangeEvt.setStatus(
        "current"
    )

olOSCLossOfLightRxCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 1)
)
olOSCLossOfLightRxCond.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCLossOfLightRxCond.setStatus(
        "current"
    )

olOSCLossOfLightRxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 2)
)
olOSCLossOfLightRxClear.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCLossOfLightRxClear.setStatus(
        "current"
    )

olOSCLossOfFrameCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 3)
)
olOSCLossOfFrameCond.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCLossOfFrameCond.setStatus(
        "current"
    )

olOSCLossOfFrameClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 4)
)
olOSCLossOfFrameClear.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCLossOfFrameClear.setStatus(
        "current"
    )

olOSCLossOfLightTxCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 5)
)
olOSCLossOfLightTxCond.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCLossOfLightTxCond.setStatus(
        "current"
    )

olOSCLossOfLightTxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 6)
)
olOSCLossOfLightTxClear.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCLossOfLightTxClear.setStatus(
        "current"
    )

olOSCFarEndIdMismatchCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 7)
)
olOSCFarEndIdMismatchCond.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCFarEndIdMismatchCond.setStatus(
        "current"
    )

olOSCFarEndIdMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 8)
)
olOSCFarEndIdMismatchClear.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCFarEndIdMismatchClear.setStatus(
        "current"
    )

olOSCFarEndNodeCnfgInconsistentCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 9)
)
olOSCFarEndNodeCnfgInconsistentCond.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCFarEndNodeCnfgInconsistentCond.setStatus(
        "current"
    )

olOSCFarEndNodeCnfgInconsistentClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 10)
)
olOSCFarEndNodeCnfgInconsistentClear.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCFarEndNodeCnfgInconsistentClear.setStatus(
        "current"
    )

olOSCSpanContCommCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 11)
)
olOSCSpanContCommCond.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCSpanContCommCond.setStatus(
        "current"
    )

olOSCSpanContCommClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 12)
)
olOSCSpanContCommClear.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCSpanContCommClear.setStatus(
        "current"
    )

olOSCEqlzContCommCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 13)
)
olOSCEqlzContCommCond.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCEqlzContCommCond.setStatus(
        "current"
    )

olOSCEqlzContCommClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 14)
)
olOSCEqlzContCommClear.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCEqlzContCommClear.setStatus(
        "current"
    )

olOSCOpticalBackReflOutOfSpecCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 15)
)
olOSCOpticalBackReflOutOfSpecCond.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCOpticalBackReflOutOfSpecCond.setStatus(
        "current"
    )

olOSCOpticalBackReflOutOfSpecClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 16)
)
olOSCOpticalBackReflOutOfSpecClear.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCOpticalBackReflOutOfSpecClear.setStatus(
        "current"
    )

olOSCOpticalBackReflHighThCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 17)
)
olOSCOpticalBackReflHighThCond.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCOpticalBackReflHighThCond.setStatus(
        "current"
    )

olOSCOpticalBackReflHighThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 1, 0, 18)
)
olOSCOpticalBackReflHighThClear.setObjects(
      *(("BTI-OL-MIB", "olOSCCpTypeIdx"),
        ("BTI-OL-MIB", "olOSCShelfIdx"),
        ("BTI-OL-MIB", "olOSCSlotIdx"),
        ("BTI-OL-MIB", "olOSCLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olOSCOpticalBackReflHighThClear.setStatus(
        "current"
    )

olPortPowerOutOfSpecRxCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 1)
)
olPortPowerOutOfSpecRxCond.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortPowerOutOfSpecRxCond.setStatus(
        "current"
    )

olPortPowerOutOfSpecRxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 2)
)
olPortPowerOutOfSpecRxClear.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortPowerOutOfSpecRxClear.setStatus(
        "current"
    )

olPortLossOfLightRxCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 3)
)
olPortLossOfLightRxCond.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortLossOfLightRxCond.setStatus(
        "current"
    )

olPortLossOfLightRxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 4)
)
olPortLossOfLightRxClear.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortLossOfLightRxClear.setStatus(
        "current"
    )

olPortLossRxOutOfSpecCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 5)
)
olPortLossRxOutOfSpecCond.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortLossRxOutOfSpecCond.setStatus(
        "current"
    )

olPortLossRxOutOfSpecClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 6)
)
olPortLossRxOutOfSpecClear.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortLossRxOutOfSpecClear.setStatus(
        "current"
    )

olPortLossRxHighThCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 7)
)
olPortLossRxHighThCond.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortLossRxHighThCond.setStatus(
        "current"
    )

olPortLossRxHighThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 8)
)
olPortLossRxHighThClear.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortLossRxHighThClear.setStatus(
        "current"
    )

olPortAPSDCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 9)
)
olPortAPSDCond.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortAPSDCond.setStatus(
        "current"
    )

olPortAPSDClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 10)
)
olPortAPSDClear.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortAPSDClear.setStatus(
        "current"
    )

olPortPayloadMissingIndCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 11)
)
olPortPayloadMissingIndCond.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortPayloadMissingIndCond.setStatus(
        "current"
    )

olPortPayloadMissingIndClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 12)
)
olPortPayloadMissingIndClear.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortPayloadMissingIndClear.setStatus(
        "current"
    )

olPortBackwardDefectIndCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 13)
)
olPortBackwardDefectIndCond.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortBackwardDefectIndCond.setStatus(
        "current"
    )

olPortBackwardDefectIndClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 14)
)
olPortBackwardDefectIndClear.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortBackwardDefectIndClear.setStatus(
        "current"
    )

olPortChannelCountDeficiencyCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 15)
)
olPortChannelCountDeficiencyCond.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortChannelCountDeficiencyCond.setStatus(
        "current"
    )

olPortChannelCountDeficiencyClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 16)
)
olPortChannelCountDeficiencyClear.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortChannelCountDeficiencyClear.setStatus(
        "current"
    )

olPortConnectionMismatchCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 17)
)
olPortConnectionMismatchCond.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-OL-MIB", "olPortExpCnxDegree"),
        ("BTI-OL-MIB", "olPortActCnxDegree"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortConnectionMismatchCond.setStatus(
        "current"
    )

olPortConnectionMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 18)
)
olPortConnectionMismatchClear.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortConnectionMismatchClear.setStatus(
        "current"
    )

olPortConnectionValidationTimeoutCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 19)
)
olPortConnectionValidationTimeoutCond.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortConnectionValidationTimeoutCond.setStatus(
        "current"
    )

olPortConnectionValidationTimeoutClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 2, 0, 20)
)
olPortConnectionValidationTimeoutClear.setObjects(
      *(("BTI-OL-MIB", "olPortCpTypeIdx"),
        ("BTI-OL-MIB", "olPortShelfIdx"),
        ("BTI-OL-MIB", "olPortSlotIdx"),
        ("BTI-OL-MIB", "olPortTypeIdx"),
        ("BTI-OL-MIB", "olPortIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    olPortConnectionValidationTimeoutClear.setStatus(
        "current"
    )

wdmInvalidPreAmpOperCnfgCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 3, 0, 1)
)
wdmInvalidPreAmpOperCnfgCond.setObjects(
      *(("BTI-OL-MIB", "wdmCpTypeIdx"),
        ("BTI-OL-MIB", "wdmShelfIdx"),
        ("BTI-OL-MIB", "wdmSlotIdx"),
        ("BTI-OL-MIB", "wdmLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wdmInvalidPreAmpOperCnfgCond.setStatus(
        "current"
    )

wdmInvalidPreAmpOperCnfgClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 3, 0, 2)
)
wdmInvalidPreAmpOperCnfgClear.setObjects(
      *(("BTI-OL-MIB", "wdmCpTypeIdx"),
        ("BTI-OL-MIB", "wdmShelfIdx"),
        ("BTI-OL-MIB", "wdmSlotIdx"),
        ("BTI-OL-MIB", "wdmLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wdmInvalidPreAmpOperCnfgClear.setStatus(
        "current"
    )

wdmInvalidMidAmpOperCnfgCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 3, 0, 3)
)
wdmInvalidMidAmpOperCnfgCond.setObjects(
      *(("BTI-OL-MIB", "wdmCpTypeIdx"),
        ("BTI-OL-MIB", "wdmShelfIdx"),
        ("BTI-OL-MIB", "wdmSlotIdx"),
        ("BTI-OL-MIB", "wdmLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wdmInvalidMidAmpOperCnfgCond.setStatus(
        "current"
    )

wdmInvalidMidAmpOperCnfgClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 3, 0, 4)
)
wdmInvalidMidAmpOperCnfgClear.setObjects(
      *(("BTI-OL-MIB", "wdmCpTypeIdx"),
        ("BTI-OL-MIB", "wdmShelfIdx"),
        ("BTI-OL-MIB", "wdmSlotIdx"),
        ("BTI-OL-MIB", "wdmLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wdmInvalidMidAmpOperCnfgClear.setStatus(
        "current"
    )

wdmInvalidBoostAmpOperCnfgCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 3, 0, 5)
)
wdmInvalidBoostAmpOperCnfgCond.setObjects(
      *(("BTI-OL-MIB", "wdmCpTypeIdx"),
        ("BTI-OL-MIB", "wdmShelfIdx"),
        ("BTI-OL-MIB", "wdmSlotIdx"),
        ("BTI-OL-MIB", "wdmLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wdmInvalidBoostAmpOperCnfgCond.setStatus(
        "current"
    )

wdmInvalidBoostAmpOperCnfgClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 3, 0, 6)
)
wdmInvalidBoostAmpOperCnfgClear.setObjects(
      *(("BTI-OL-MIB", "wdmCpTypeIdx"),
        ("BTI-OL-MIB", "wdmShelfIdx"),
        ("BTI-OL-MIB", "wdmSlotIdx"),
        ("BTI-OL-MIB", "wdmLineIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wdmInvalidBoostAmpOperCnfgClear.setStatus(
        "current"
    )

wchPowerOutOfSpecRxCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 1)
)
wchPowerOutOfSpecRxCond.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchPowerOutOfSpecRxCond.setStatus(
        "deprecated"
    )

wchPowerOutOfSpecRxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 2)
)
wchPowerOutOfSpecRxClear.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchPowerOutOfSpecRxClear.setStatus(
        "deprecated"
    )

wchLossOfLightRxCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 3)
)
wchLossOfLightRxCond.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchLossOfLightRxCond.setStatus(
        "current"
    )

wchLossOfLightRxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 4)
)
wchLossOfLightRxClear.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchLossOfLightRxClear.setStatus(
        "current"
    )

wchPowerOutOfSpecTxCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 5)
)
wchPowerOutOfSpecTxCond.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchPowerOutOfSpecTxCond.setStatus(
        "current"
    )

wchPowerOutOfSpecTxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 6)
)
wchPowerOutOfSpecTxClear.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchPowerOutOfSpecTxClear.setStatus(
        "current"
    )

wchLossOfLightTxCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 7)
)
wchLossOfLightTxCond.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchLossOfLightTxCond.setStatus(
        "current"
    )

wchLossOfLightTxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 8)
)
wchLossOfLightTxClear.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchLossOfLightTxClear.setStatus(
        "current"
    )

wchUnequippedCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 9)
)
wchUnequippedCond.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchUnequippedCond.setStatus(
        "current"
    )

wchUnequippedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 10)
)
wchUnequippedClear.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchUnequippedClear.setStatus(
        "current"
    )

wchAISCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 11)
)
wchAISCond.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchAISCond.setStatus(
        "current"
    )

wchAISClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 12)
)
wchAISClear.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchAISClear.setStatus(
        "current"
    )

wchPowerOutOfSpecRxHighCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 13)
)
wchPowerOutOfSpecRxHighCond.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchPowerOutOfSpecRxHighCond.setStatus(
        "deprecated"
    )

wchPowerOutOfSpecRxHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 14)
)
wchPowerOutOfSpecRxHighClear.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchPowerOutOfSpecRxHighClear.setStatus(
        "deprecated"
    )

wchPowerOutOfSpecRxLowCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 15)
)
wchPowerOutOfSpecRxLowCond.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchPowerOutOfSpecRxLowCond.setStatus(
        "deprecated"
    )

wchPowerOutOfSpecRxLowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 16)
)
wchPowerOutOfSpecRxLowClear.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchPowerOutOfSpecRxLowClear.setStatus(
        "deprecated"
    )

wchPowerRxHighFailCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 17)
)
wchPowerRxHighFailCond.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchPowerRxHighFailCond.setStatus(
        "deprecated"
    )

wchPowerRxHighFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 28, 4, 0, 18)
)
wchPowerRxHighFailClear.setObjects(
      *(("BTI-OL-MIB", "wchCpTypeIdx"),
        ("BTI-OL-MIB", "wchShelfIdx"),
        ("BTI-OL-MIB", "wchSlotIdx"),
        ("BTI-OL-MIB", "wchPortTypeIdx"),
        ("BTI-OL-MIB", "wchPortIdx"),
        ("BTI-OL-MIB", "wchIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    wchPowerRxHighFailClear.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BTI-OL-MIB",
    **{"OlGroupType": OlGroupType,
       "OlPortType": OlPortType,
       "olMib": olMib,
       "olGroupTable": olGroupTable,
       "olGroupEntry": olGroupEntry,
       "olGroupIdx": olGroupIdx,
       "olGroupType": olGroupType,
       "olGroupId": olGroupId,
       "olGroupCustom1": olGroupCustom1,
       "olGroupCustom2": olGroupCustom2,
       "olGroupCustom3": olGroupCustom3,
       "olGroupRowStatus": olGroupRowStatus,
       "olEqptTable": olEqptTable,
       "olEqptEntry": olEqptEntry,
       "olEqptCpTypeIdx": olEqptCpTypeIdx,
       "olEqptShelfIdx": olEqptShelfIdx,
       "olEqptSlotIdx": olEqptSlotIdx,
       "olEqptGroupNum": olEqptGroupNum,
       "olEqptDegreeNum": olEqptDegreeNum,
       "olEqptRowStatus": olEqptRowStatus,
       "olPortTable": olPortTable,
       "olPortEntry": olPortEntry,
       "olPortCpTypeIdx": olPortCpTypeIdx,
       "olPortShelfIdx": olPortShelfIdx,
       "olPortSlotIdx": olPortSlotIdx,
       "olPortTypeIdx": olPortTypeIdx,
       "olPortIdx": olPortIdx,
       "olPortId": olPortId,
       "olPortCustom1": olPortCustom1,
       "olPortCustom2": olPortCustom2,
       "olPortCustom3": olPortCustom3,
       "olPortDWDMType": olPortDWDMType,
       "olPortGrid": olPortGrid,
       "olPortWavelength": olPortWavelength,
       "olPortFrequency": olPortFrequency,
       "olPortOperStatus": olPortOperStatus,
       "olPortOperStatQlfr": olPortOperStatQlfr,
       "olPortRemoteId": olPortRemoteId,
       "olPortExpCnxDegree": olPortExpCnxDegree,
       "olPortActCnxDegree": olPortActCnxDegree,
       "olPortRowStatus": olPortRowStatus,
       "eqptConnTable": eqptConnTable,
       "eqptConnEntry": eqptConnEntry,
       "eqptConnSrcCpTypeIdx": eqptConnSrcCpTypeIdx,
       "eqptConnSrcShelfIdx": eqptConnSrcShelfIdx,
       "eqptConnSrcSlotIdx": eqptConnSrcSlotIdx,
       "eqptConnSrcPortTypeIdx": eqptConnSrcPortTypeIdx,
       "eqptConnSrcIdx": eqptConnSrcIdx,
       "eqptConnDstCpTypeIdx": eqptConnDstCpTypeIdx,
       "eqptConnDstShelfIdx": eqptConnDstShelfIdx,
       "eqptConnDstSlotIdx": eqptConnDstSlotIdx,
       "eqptConnDstPortTypeIdx": eqptConnDstPortTypeIdx,
       "eqptConnDstIdx": eqptConnDstIdx,
       "eqptConnType": eqptConnType,
       "eqptConnRowStatus": eqptConnRowStatus,
       "olOSCTable": olOSCTable,
       "olOSCEntry": olOSCEntry,
       "olOSCCpTypeIdx": olOSCCpTypeIdx,
       "olOSCShelfIdx": olOSCShelfIdx,
       "olOSCSlotIdx": olOSCSlotIdx,
       "olOSCLineIdx": olOSCLineIdx,
       "olOSCAdminStatus": olOSCAdminStatus,
       "olOSCOperStatus": olOSCOperStatus,
       "olOSCOperStatQlfr": olOSCOperStatQlfr,
       "olOSCAutoEnableTimer": olOSCAutoEnableTimer,
       "olOSCActAutoEnableTimer": olOSCActAutoEnableTimer,
       "olOSCId": olOSCId,
       "olOSCCustom1": olOSCCustom1,
       "olOSCCustom2": olOSCCustom2,
       "olOSCCustom3": olOSCCustom3,
       "olOSCFEIMMon": olOSCFEIMMon,
       "olOSCExpFESysName": olOSCExpFESysName,
       "olOSCExpFEIPAddr": olOSCExpFEIPAddr,
       "olOSCExpFEGrp": olOSCExpFEGrp,
       "olOSCExpFEDegr": olOSCExpFEDegr,
       "olOSCFESysName": olOSCFESysName,
       "olOSCFEIPAddr": olOSCFEIPAddr,
       "olOSCFEGrp": olOSCFEGrp,
       "olOSCFEDegr": olOSCFEDegr,
       "olOSCFEGrpType": olOSCFEGrpType,
       "olOSCRowStatus": olOSCRowStatus,
       "odccTable": odccTable,
       "odccEntry": odccEntry,
       "odccCpTypeIdx": odccCpTypeIdx,
       "odccShelfIdx": odccShelfIdx,
       "odccSlotIdx": odccSlotIdx,
       "odccLineIdx": odccLineIdx,
       "odccAdminStatus": odccAdminStatus,
       "odccRowStatus": odccRowStatus,
       "wdmTable": wdmTable,
       "wdmEntry": wdmEntry,
       "wdmCpTypeIdx": wdmCpTypeIdx,
       "wdmShelfIdx": wdmShelfIdx,
       "wdmSlotIdx": wdmSlotIdx,
       "wdmLineIdx": wdmLineIdx,
       "wdmAdminStatus": wdmAdminStatus,
       "wdmOperStatus": wdmOperStatus,
       "wdmOperStatQlfr": wdmOperStatQlfr,
       "wdmAutoEnableTimer": wdmAutoEnableTimer,
       "wdmActAutoEnableTimer": wdmActAutoEnableTimer,
       "wdmId": wdmId,
       "wdmCustom1": wdmCustom1,
       "wdmCustom2": wdmCustom2,
       "wdmCustom3": wdmCustom3,
       "wdmFiberType": wdmFiberType,
       "wdmSpanLength": wdmSpanLength,
       "wdmSpanLossRxHighTh": wdmSpanLossRxHighTh,
       "wdmSpanLossSpecMax": wdmSpanLossSpecMax,
       "wdmNumChannels": wdmNumChannels,
       "wdmRowStatus": wdmRowStatus,
       "wchXCTable": wchXCTable,
       "wchXCEntry": wchXCEntry,
       "wchXCSrcCpTypeIdx": wchXCSrcCpTypeIdx,
       "wchXCSrcShelfIdx": wchXCSrcShelfIdx,
       "wchXCSrcSlotIdx": wchXCSrcSlotIdx,
       "wchXCSrcPortTypeIdx": wchXCSrcPortTypeIdx,
       "wchXCSrcPortIdx": wchXCSrcPortIdx,
       "wchXCSrcChannelIdx": wchXCSrcChannelIdx,
       "wchXCDstCpTypeIdx": wchXCDstCpTypeIdx,
       "wchXCDstShelfIdx": wchXCDstShelfIdx,
       "wchXCDstSlotIdx": wchXCDstSlotIdx,
       "wchXCDstPortTypeIdx": wchXCDstPortTypeIdx,
       "wchXCDstPortIdx": wchXCDstPortIdx,
       "wchXCDstChannelIdx": wchXCDstChannelIdx,
       "wchXCServiceName": wchXCServiceName,
       "wchXCRowStatus": wchXCRowStatus,
       "wchTable": wchTable,
       "wchEntry": wchEntry,
       "wchCpTypeIdx": wchCpTypeIdx,
       "wchShelfIdx": wchShelfIdx,
       "wchSlotIdx": wchSlotIdx,
       "wchPortTypeIdx": wchPortTypeIdx,
       "wchPortIdx": wchPortIdx,
       "wchIdx": wchIdx,
       "wchAdminStatus": wchAdminStatus,
       "wchOperStatus": wchOperStatus,
       "wchOperStatQlfr": wchOperStatQlfr,
       "wchAutoEnableTimer": wchAutoEnableTimer,
       "wchActAutoEnableTimer": wchActAutoEnableTimer,
       "wchId": wchId,
       "wchCustom1": wchCustom1,
       "wchCustom2": wchCustom2,
       "wchCustom3": wchCustom3,
       "wchBitrate": wchBitrate,
       "wchGrid": wchGrid,
       "wchWavelength": wchWavelength,
       "wchFrequency": wchFrequency,
       "wchRowStatus": wchRowStatus,
       "olGroupMerge": olGroupMerge,
       "olGroupMergeCmd": olGroupMergeCmd,
       "olGroupMergePrimary": olGroupMergePrimary,
       "olGroupMergeSecondary": olGroupMergeSecondary,
       "olPerformance": olPerformance,
       "olOSCCrntPMTable": olOSCCrntPMTable,
       "olOSCCrntPMEntry": olOSCCrntPMEntry,
       "olOSCCrntPMCpTypeIdx": olOSCCrntPMCpTypeIdx,
       "olOSCCrntPMShelfIdx": olOSCCrntPMShelfIdx,
       "olOSCCrntPMSlotIdx": olOSCCrntPMSlotIdx,
       "olOSCCrntPMLineIdx": olOSCCrntPMLineIdx,
       "olOSCCrntPMIntervalTypeIdx": olOSCCrntPMIntervalTypeIdx,
       "olOSCCrntPMOPRValue": olOSCCrntPMOPRValue,
       "olOSCCrntPMOPRTimeStamp": olOSCCrntPMOPRTimeStamp,
       "olOSCCrntPMOPRValidity": olOSCCrntPMOPRValidity,
       "olOSCCrntPMOPTValue": olOSCCrntPMOPTValue,
       "olOSCCrntPMOPTTimeStamp": olOSCCrntPMOPTTimeStamp,
       "olOSCCrntPMOPTValidity": olOSCCrntPMOPTValidity,
       "olOSCCrntPMOBRValue": olOSCCrntPMOBRValue,
       "olOSCCrntPMOBRTimeStamp": olOSCCrntPMOBRTimeStamp,
       "olOSCCrntPMOBRValidity": olOSCCrntPMOBRValidity,
       "olOSCCrntPMCVSValue": olOSCCrntPMCVSValue,
       "olOSCCrntPMCVSTimeStamp": olOSCCrntPMCVSTimeStamp,
       "olOSCCrntPMCVSValidity": olOSCCrntPMCVSValidity,
       "olOSCCrntPMCVSInitialize": olOSCCrntPMCVSInitialize,
       "olOSCCrntPMESSValue": olOSCCrntPMESSValue,
       "olOSCCrntPMESSTimeStamp": olOSCCrntPMESSTimeStamp,
       "olOSCCrntPMESSValidity": olOSCCrntPMESSValidity,
       "olOSCCrntPMESSInitialize": olOSCCrntPMESSInitialize,
       "olOSCCrntPMSESSValue": olOSCCrntPMSESSValue,
       "olOSCCrntPMSESSTimeStamp": olOSCCrntPMSESSTimeStamp,
       "olOSCCrntPMSESSValidity": olOSCCrntPMSESSValidity,
       "olOSCCrntPMSESSInitialize": olOSCCrntPMSESSInitialize,
       "olOSCCrntPMSEFSSValue": olOSCCrntPMSEFSSValue,
       "olOSCCrntPMSEFSSTimeStamp": olOSCCrntPMSEFSSTimeStamp,
       "olOSCCrntPMSEFSSValidity": olOSCCrntPMSEFSSValidity,
       "olOSCCrntPMSEFSSInitialize": olOSCCrntPMSEFSSInitialize,
       "olOSCCrntPMUASSValue": olOSCCrntPMUASSValue,
       "olOSCCrntPMUASSTimeStamp": olOSCCrntPMUASSTimeStamp,
       "olOSCCrntPMUASSValidity": olOSCCrntPMUASSValidity,
       "olOSCCrntPMUASSInitialize": olOSCCrntPMUASSInitialize,
       "olOSCHistPMTable": olOSCHistPMTable,
       "olOSCHistPMEntry": olOSCHistPMEntry,
       "olOSCHistPMCpTypeIdx": olOSCHistPMCpTypeIdx,
       "olOSCHistPMShelfIdx": olOSCHistPMShelfIdx,
       "olOSCHistPMSlotIdx": olOSCHistPMSlotIdx,
       "olOSCHistPMLineIdx": olOSCHistPMLineIdx,
       "olOSCHistPMIntervalTypeIdx": olOSCHistPMIntervalTypeIdx,
       "olOSCHistPMIntervalIdx": olOSCHistPMIntervalIdx,
       "olOSCHistPMOPRValue": olOSCHistPMOPRValue,
       "olOSCHistPMOPRTimeStamp": olOSCHistPMOPRTimeStamp,
       "olOSCHistPMOPRValidity": olOSCHistPMOPRValidity,
       "olOSCHistPMOPTValue": olOSCHistPMOPTValue,
       "olOSCHistPMOPTTimeStamp": olOSCHistPMOPTTimeStamp,
       "olOSCHistPMOPTValidity": olOSCHistPMOPTValidity,
       "olOSCHistPMOBRValue": olOSCHistPMOBRValue,
       "olOSCHistPMOBRTimeStamp": olOSCHistPMOBRTimeStamp,
       "olOSCHistPMOBRValidity": olOSCHistPMOBRValidity,
       "olOSCHistPMCVSValue": olOSCHistPMCVSValue,
       "olOSCHistPMCVSTimeStamp": olOSCHistPMCVSTimeStamp,
       "olOSCHistPMCVSValidity": olOSCHistPMCVSValidity,
       "olOSCHistPMCVSInitialize": olOSCHistPMCVSInitialize,
       "olOSCHistPMESSValue": olOSCHistPMESSValue,
       "olOSCHistPMESSTimeStamp": olOSCHistPMESSTimeStamp,
       "olOSCHistPMESSValidity": olOSCHistPMESSValidity,
       "olOSCHistPMESSInitialize": olOSCHistPMESSInitialize,
       "olOSCHistPMSESSValue": olOSCHistPMSESSValue,
       "olOSCHistPMSESSTimeStamp": olOSCHistPMSESSTimeStamp,
       "olOSCHistPMSESSValidity": olOSCHistPMSESSValidity,
       "olOSCHistPMSESSInitialize": olOSCHistPMSESSInitialize,
       "olOSCHistPMSEFSSValue": olOSCHistPMSEFSSValue,
       "olOSCHistPMSEFSSTimeStamp": olOSCHistPMSEFSSTimeStamp,
       "olOSCHistPMSEFSSValidity": olOSCHistPMSEFSSValidity,
       "olOSCHistPMSEFSSInitialize": olOSCHistPMSEFSSInitialize,
       "olOSCHistPMUASSValue": olOSCHistPMUASSValue,
       "olOSCHistPMUASSTimeStamp": olOSCHistPMUASSTimeStamp,
       "olOSCHistPMUASSValidity": olOSCHistPMUASSValidity,
       "olOSCHistPMUASSInitialize": olOSCHistPMUASSInitialize,
       "olOSCPMThresholdTable": olOSCPMThresholdTable,
       "olOSCPMThresholdEntry": olOSCPMThresholdEntry,
       "olOSCPMThresholdCpTypeIdx": olOSCPMThresholdCpTypeIdx,
       "olOSCPMThresholdShelfIdx": olOSCPMThresholdShelfIdx,
       "olOSCPMThresholdSlotIdx": olOSCPMThresholdSlotIdx,
       "olOSCPMThresholdLineIdx": olOSCPMThresholdLineIdx,
       "olOSCPMThresholdIntervalTypeIdx": olOSCPMThresholdIntervalTypeIdx,
       "olOSCPMThresholdCVSValue": olOSCPMThresholdCVSValue,
       "olOSCPMThresholdESSValue": olOSCPMThresholdESSValue,
       "olOSCPMThresholdSESSValue": olOSCPMThresholdSESSValue,
       "olOSCPMThresholdSEFSSValue": olOSCPMThresholdSEFSSValue,
       "olOSCPMThresholdUASSValue": olOSCPMThresholdUASSValue,
       "olPortCrntPMTable": olPortCrntPMTable,
       "olPortCrntPMEntry": olPortCrntPMEntry,
       "olPortCrntPMCpTypeIdx": olPortCrntPMCpTypeIdx,
       "olPortCrntPMShelfIdx": olPortCrntPMShelfIdx,
       "olPortCrntPMSlotIdx": olPortCrntPMSlotIdx,
       "olPortCrntPMTypeIdx": olPortCrntPMTypeIdx,
       "olPortCrntPMIdx": olPortCrntPMIdx,
       "olPortCrntPMIntervalTypeIdx": olPortCrntPMIntervalTypeIdx,
       "olPortCrntPMOPRValue": olPortCrntPMOPRValue,
       "olPortCrntPMOPRTimeStamp": olPortCrntPMOPRTimeStamp,
       "olPortCrntPMOPRValidity": olPortCrntPMOPRValidity,
       "olPortCrntPMOPRMinValue": olPortCrntPMOPRMinValue,
       "olPortCrntPMOPRMinTimeStamp": olPortCrntPMOPRMinTimeStamp,
       "olPortCrntPMOPRMinValidity": olPortCrntPMOPRMinValidity,
       "olPortCrntPMOPRMaxValue": olPortCrntPMOPRMaxValue,
       "olPortCrntPMOPRMaxTimeStamp": olPortCrntPMOPRMaxTimeStamp,
       "olPortCrntPMOPRMaxValidity": olPortCrntPMOPRMaxValidity,
       "olPortCrntPMOPRAvgValue": olPortCrntPMOPRAvgValue,
       "olPortCrntPMOPRAvgTimeStamp": olPortCrntPMOPRAvgTimeStamp,
       "olPortCrntPMOPRAvgValidity": olPortCrntPMOPRAvgValidity,
       "olPortCrntPMOPRStdDevValue": olPortCrntPMOPRStdDevValue,
       "olPortCrntPMOPRStdDevTimeStamp": olPortCrntPMOPRStdDevTimeStamp,
       "olPortCrntPMOPRStdDevValidity": olPortCrntPMOPRStdDevValidity,
       "olPortCrntPMOPTValue": olPortCrntPMOPTValue,
       "olPortCrntPMOPTTimeStamp": olPortCrntPMOPTTimeStamp,
       "olPortCrntPMOPTValidity": olPortCrntPMOPTValidity,
       "olPortCrntPMOPTMinValue": olPortCrntPMOPTMinValue,
       "olPortCrntPMOPTMinTimeStamp": olPortCrntPMOPTMinTimeStamp,
       "olPortCrntPMOPTMinValidity": olPortCrntPMOPTMinValidity,
       "olPortCrntPMOPTMaxValue": olPortCrntPMOPTMaxValue,
       "olPortCrntPMOPTMaxTimeStamp": olPortCrntPMOPTMaxTimeStamp,
       "olPortCrntPMOPTMaxValidity": olPortCrntPMOPTMaxValidity,
       "olPortCrntPMOPTAvgValue": olPortCrntPMOPTAvgValue,
       "olPortCrntPMOPTAvgTimeStamp": olPortCrntPMOPTAvgTimeStamp,
       "olPortCrntPMOPTAvgValidity": olPortCrntPMOPTAvgValidity,
       "olPortCrntPMOPTStdDevValue": olPortCrntPMOPTStdDevValue,
       "olPortCrntPMOPTStdDevTimeStamp": olPortCrntPMOPTStdDevTimeStamp,
       "olPortCrntPMOPTStdDevValidity": olPortCrntPMOPTStdDevValidity,
       "olPortCrntPMLossRxValue": olPortCrntPMLossRxValue,
       "olPortCrntPMLossRxTimeStamp": olPortCrntPMLossRxTimeStamp,
       "olPortCrntPMLossRxValidity": olPortCrntPMLossRxValidity,
       "olPortCrntPMLossTxValue": olPortCrntPMLossTxValue,
       "olPortCrntPMLossTxTimeStamp": olPortCrntPMLossTxTimeStamp,
       "olPortCrntPMLossTxValidity": olPortCrntPMLossTxValidity,
       "olPortCrntPMInitializeAll": olPortCrntPMInitializeAll,
       "olPortHistPMTable": olPortHistPMTable,
       "olPortHistPMEntry": olPortHistPMEntry,
       "olPortHistPMCpTypeIdx": olPortHistPMCpTypeIdx,
       "olPortHistPMShelfIdx": olPortHistPMShelfIdx,
       "olPortHistPMSlotIdx": olPortHistPMSlotIdx,
       "olPortHistPMTypeIdx": olPortHistPMTypeIdx,
       "olPortHistPMIdx": olPortHistPMIdx,
       "olPortHistPMIntervalTypeIdx": olPortHistPMIntervalTypeIdx,
       "olPortHistPMIntervalIdx": olPortHistPMIntervalIdx,
       "olPortHistPMOPRValue": olPortHistPMOPRValue,
       "olPortHistPMOPRTimeStamp": olPortHistPMOPRTimeStamp,
       "olPortHistPMOPRValidity": olPortHistPMOPRValidity,
       "olPortHistPMOPRMinValue": olPortHistPMOPRMinValue,
       "olPortHistPMOPRMinTimeStamp": olPortHistPMOPRMinTimeStamp,
       "olPortHistPMOPRMinValidity": olPortHistPMOPRMinValidity,
       "olPortHistPMOPRMaxValue": olPortHistPMOPRMaxValue,
       "olPortHistPMOPRMaxTimeStamp": olPortHistPMOPRMaxTimeStamp,
       "olPortHistPMOPRMaxValidity": olPortHistPMOPRMaxValidity,
       "olPortHistPMOPRAvgValue": olPortHistPMOPRAvgValue,
       "olPortHistPMOPRAvgTimeStamp": olPortHistPMOPRAvgTimeStamp,
       "olPortHistPMOPRAvgValidity": olPortHistPMOPRAvgValidity,
       "olPortHistPMOPRStdDevValue": olPortHistPMOPRStdDevValue,
       "olPortHistPMOPRStdDevTimeStamp": olPortHistPMOPRStdDevTimeStamp,
       "olPortHistPMOPRStdDevValidity": olPortHistPMOPRStdDevValidity,
       "olPortHistPMOPTValue": olPortHistPMOPTValue,
       "olPortHistPMOPTTimeStamp": olPortHistPMOPTTimeStamp,
       "olPortHistPMOPTValidity": olPortHistPMOPTValidity,
       "olPortHistPMOPTMinValue": olPortHistPMOPTMinValue,
       "olPortHistPMOPTMinTimeStamp": olPortHistPMOPTMinTimeStamp,
       "olPortHistPMOPTMinValidity": olPortHistPMOPTMinValidity,
       "olPortHistPMOPTMaxValue": olPortHistPMOPTMaxValue,
       "olPortHistPMOPTMaxTimeStamp": olPortHistPMOPTMaxTimeStamp,
       "olPortHistPMOPTMaxValidity": olPortHistPMOPTMaxValidity,
       "olPortHistPMOPTAvgValue": olPortHistPMOPTAvgValue,
       "olPortHistPMOPTAvgTimeStamp": olPortHistPMOPTAvgTimeStamp,
       "olPortHistPMOPTAvgValidity": olPortHistPMOPTAvgValidity,
       "olPortHistPMOPTStdDevValue": olPortHistPMOPTStdDevValue,
       "olPortHistPMOPTStdDevTimeStamp": olPortHistPMOPTStdDevTimeStamp,
       "olPortHistPMOPTStdDevValidity": olPortHistPMOPTStdDevValidity,
       "olPortHistPMLossRxValue": olPortHistPMLossRxValue,
       "olPortHistPMLossRxTimeStamp": olPortHistPMLossRxTimeStamp,
       "olPortHistPMLossRxValidity": olPortHistPMLossRxValidity,
       "olPortHistPMLossTxValue": olPortHistPMLossTxValue,
       "olPortHistPMLossTxTimeStamp": olPortHistPMLossTxTimeStamp,
       "olPortHistPMLossTxValidity": olPortHistPMLossTxValidity,
       "olPortHistPMInitializeAll": olPortHistPMInitializeAll,
       "wchCrntPMTable": wchCrntPMTable,
       "wchCrntPMEntry": wchCrntPMEntry,
       "wchCrntPMCpTypeIdx": wchCrntPMCpTypeIdx,
       "wchCrntPMShelfIdx": wchCrntPMShelfIdx,
       "wchCrntPMSlotIdx": wchCrntPMSlotIdx,
       "wchCrntPMPortTypeIdx": wchCrntPMPortTypeIdx,
       "wchCrntPMPortIdx": wchCrntPMPortIdx,
       "wchCrntPMIdx": wchCrntPMIdx,
       "wchCrntPMIntervalTypeIdx": wchCrntPMIntervalTypeIdx,
       "wchCrntPMOPRValue": wchCrntPMOPRValue,
       "wchCrntPMOPRTimeStamp": wchCrntPMOPRTimeStamp,
       "wchCrntPMOPRValidity": wchCrntPMOPRValidity,
       "wchCrntPMOPRMinValue": wchCrntPMOPRMinValue,
       "wchCrntPMOPRMinTimeStamp": wchCrntPMOPRMinTimeStamp,
       "wchCrntPMOPRMinValidity": wchCrntPMOPRMinValidity,
       "wchCrntPMOPRMinInitialize": wchCrntPMOPRMinInitialize,
       "wchCrntPMOPRMaxValue": wchCrntPMOPRMaxValue,
       "wchCrntPMOPRMaxTimeStamp": wchCrntPMOPRMaxTimeStamp,
       "wchCrntPMOPRMaxValidity": wchCrntPMOPRMaxValidity,
       "wchCrntPMOPRMaxInitialize": wchCrntPMOPRMaxInitialize,
       "wchCrntPMOPTValue": wchCrntPMOPTValue,
       "wchCrntPMOPTTimeStamp": wchCrntPMOPTTimeStamp,
       "wchCrntPMOPTValidity": wchCrntPMOPTValidity,
       "wchCrntPMOPTMinValue": wchCrntPMOPTMinValue,
       "wchCrntPMOPTMinTimeStamp": wchCrntPMOPTMinTimeStamp,
       "wchCrntPMOPTMinValidity": wchCrntPMOPTMinValidity,
       "wchCrntPMOPTMinInitialize": wchCrntPMOPTMinInitialize,
       "wchCrntPMOPTMaxValue": wchCrntPMOPTMaxValue,
       "wchCrntPMOPTMaxTimeStamp": wchCrntPMOPTMaxTimeStamp,
       "wchCrntPMOPTMaxValidity": wchCrntPMOPTMaxValidity,
       "wchCrntPMOPTMaxInitialize": wchCrntPMOPTMaxInitialize,
       "wchHistPMTable": wchHistPMTable,
       "wchHistPMEntry": wchHistPMEntry,
       "wchHistPMCpTypeIdx": wchHistPMCpTypeIdx,
       "wchHistPMShelfIdx": wchHistPMShelfIdx,
       "wchHistPMSlotIdx": wchHistPMSlotIdx,
       "wchHistPMPortTypeIdx": wchHistPMPortTypeIdx,
       "wchHistPMPortIdx": wchHistPMPortIdx,
       "wchHistPMIdx": wchHistPMIdx,
       "wchHistPMIntervalTypeIdx": wchHistPMIntervalTypeIdx,
       "wchHistPMIntervalIdx": wchHistPMIntervalIdx,
       "wchHistPMOPRValue": wchHistPMOPRValue,
       "wchHistPMOPRTimeStamp": wchHistPMOPRTimeStamp,
       "wchHistPMOPRValidity": wchHistPMOPRValidity,
       "wchHistPMOPRMinValue": wchHistPMOPRMinValue,
       "wchHistPMOPRMinTimeStamp": wchHistPMOPRMinTimeStamp,
       "wchHistPMOPRMinValidity": wchHistPMOPRMinValidity,
       "wchHistPMOPRMinInitialize": wchHistPMOPRMinInitialize,
       "wchHistPMOPRMaxValue": wchHistPMOPRMaxValue,
       "wchHistPMOPRMaxTimeStamp": wchHistPMOPRMaxTimeStamp,
       "wchHistPMOPRMaxValidity": wchHistPMOPRMaxValidity,
       "wchHistPMOPRMaxInitialize": wchHistPMOPRMaxInitialize,
       "wchHistPMOPTValue": wchHistPMOPTValue,
       "wchHistPMOPTTimeStamp": wchHistPMOPTTimeStamp,
       "wchHistPMOPTValidity": wchHistPMOPTValidity,
       "wchHistPMOPTMinValue": wchHistPMOPTMinValue,
       "wchHistPMOPTMinTimeStamp": wchHistPMOPTMinTimeStamp,
       "wchHistPMOPTMinValidity": wchHistPMOPTMinValidity,
       "wchHistPMOPTMinInitialize": wchHistPMOPTMinInitialize,
       "wchHistPMOPTMaxValue": wchHistPMOPTMaxValue,
       "wchHistPMOPTMaxTimeStamp": wchHistPMOPTMaxTimeStamp,
       "wchHistPMOPTMaxValidity": wchHistPMOPTMaxValidity,
       "wchHistPMOPTMaxInitialize": wchHistPMOPTMaxInitialize,
       "olOSCEvtNotifications": olOSCEvtNotifications,
       "olOSCStatusChangeEvt": olOSCStatusChangeEvt,
       "olOSCTcaEvt": olOSCTcaEvt,
       "olPortEvtNotifications": olPortEvtNotifications,
       "olPortStatusChangeEvt": olPortStatusChangeEvt,
       "wdmEvtNotifications": wdmEvtNotifications,
       "wdmStatusChangeEvt": wdmStatusChangeEvt,
       "wchEvtNotifications": wchEvtNotifications,
       "wchStatusChangeEvt": wchStatusChangeEvt,
       "olOSCCondNotifications": olOSCCondNotifications,
       "olOSCLossOfLightRxCond": olOSCLossOfLightRxCond,
       "olOSCLossOfLightRxClear": olOSCLossOfLightRxClear,
       "olOSCLossOfFrameCond": olOSCLossOfFrameCond,
       "olOSCLossOfFrameClear": olOSCLossOfFrameClear,
       "olOSCLossOfLightTxCond": olOSCLossOfLightTxCond,
       "olOSCLossOfLightTxClear": olOSCLossOfLightTxClear,
       "olOSCFarEndIdMismatchCond": olOSCFarEndIdMismatchCond,
       "olOSCFarEndIdMismatchClear": olOSCFarEndIdMismatchClear,
       "olOSCFarEndNodeCnfgInconsistentCond": olOSCFarEndNodeCnfgInconsistentCond,
       "olOSCFarEndNodeCnfgInconsistentClear": olOSCFarEndNodeCnfgInconsistentClear,
       "olOSCSpanContCommCond": olOSCSpanContCommCond,
       "olOSCSpanContCommClear": olOSCSpanContCommClear,
       "olOSCEqlzContCommCond": olOSCEqlzContCommCond,
       "olOSCEqlzContCommClear": olOSCEqlzContCommClear,
       "olOSCOpticalBackReflOutOfSpecCond": olOSCOpticalBackReflOutOfSpecCond,
       "olOSCOpticalBackReflOutOfSpecClear": olOSCOpticalBackReflOutOfSpecClear,
       "olOSCOpticalBackReflHighThCond": olOSCOpticalBackReflHighThCond,
       "olOSCOpticalBackReflHighThClear": olOSCOpticalBackReflHighThClear,
       "olPortCondNotifications": olPortCondNotifications,
       "olPortPowerOutOfSpecRxCond": olPortPowerOutOfSpecRxCond,
       "olPortPowerOutOfSpecRxClear": olPortPowerOutOfSpecRxClear,
       "olPortLossOfLightRxCond": olPortLossOfLightRxCond,
       "olPortLossOfLightRxClear": olPortLossOfLightRxClear,
       "olPortLossRxOutOfSpecCond": olPortLossRxOutOfSpecCond,
       "olPortLossRxOutOfSpecClear": olPortLossRxOutOfSpecClear,
       "olPortLossRxHighThCond": olPortLossRxHighThCond,
       "olPortLossRxHighThClear": olPortLossRxHighThClear,
       "olPortAPSDCond": olPortAPSDCond,
       "olPortAPSDClear": olPortAPSDClear,
       "olPortPayloadMissingIndCond": olPortPayloadMissingIndCond,
       "olPortPayloadMissingIndClear": olPortPayloadMissingIndClear,
       "olPortBackwardDefectIndCond": olPortBackwardDefectIndCond,
       "olPortBackwardDefectIndClear": olPortBackwardDefectIndClear,
       "olPortChannelCountDeficiencyCond": olPortChannelCountDeficiencyCond,
       "olPortChannelCountDeficiencyClear": olPortChannelCountDeficiencyClear,
       "olPortConnectionMismatchCond": olPortConnectionMismatchCond,
       "olPortConnectionMismatchClear": olPortConnectionMismatchClear,
       "olPortConnectionValidationTimeoutCond": olPortConnectionValidationTimeoutCond,
       "olPortConnectionValidationTimeoutClear": olPortConnectionValidationTimeoutClear,
       "wdmCondNotifications": wdmCondNotifications,
       "wdmInvalidPreAmpOperCnfgCond": wdmInvalidPreAmpOperCnfgCond,
       "wdmInvalidPreAmpOperCnfgClear": wdmInvalidPreAmpOperCnfgClear,
       "wdmInvalidMidAmpOperCnfgCond": wdmInvalidMidAmpOperCnfgCond,
       "wdmInvalidMidAmpOperCnfgClear": wdmInvalidMidAmpOperCnfgClear,
       "wdmInvalidBoostAmpOperCnfgCond": wdmInvalidBoostAmpOperCnfgCond,
       "wdmInvalidBoostAmpOperCnfgClear": wdmInvalidBoostAmpOperCnfgClear,
       "wchCondNotifications": wchCondNotifications,
       "wchPowerOutOfSpecRxCond": wchPowerOutOfSpecRxCond,
       "wchPowerOutOfSpecRxClear": wchPowerOutOfSpecRxClear,
       "wchLossOfLightRxCond": wchLossOfLightRxCond,
       "wchLossOfLightRxClear": wchLossOfLightRxClear,
       "wchPowerOutOfSpecTxCond": wchPowerOutOfSpecTxCond,
       "wchPowerOutOfSpecTxClear": wchPowerOutOfSpecTxClear,
       "wchLossOfLightTxCond": wchLossOfLightTxCond,
       "wchLossOfLightTxClear": wchLossOfLightTxClear,
       "wchUnequippedCond": wchUnequippedCond,
       "wchUnequippedClear": wchUnequippedClear,
       "wchAISCond": wchAISCond,
       "wchAISClear": wchAISClear,
       "wchPowerOutOfSpecRxHighCond": wchPowerOutOfSpecRxHighCond,
       "wchPowerOutOfSpecRxHighClear": wchPowerOutOfSpecRxHighClear,
       "wchPowerOutOfSpecRxLowCond": wchPowerOutOfSpecRxLowCond,
       "wchPowerOutOfSpecRxLowClear": wchPowerOutOfSpecRxLowClear,
       "wchPowerRxHighFailCond": wchPowerRxHighFailCond,
       "wchPowerRxHighFailClear": wchPowerRxHighFailClear}
)
