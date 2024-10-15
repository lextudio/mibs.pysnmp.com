# SNMP MIB module (HDSL2-SHDSL-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDSL2-SHDSL-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:06 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hdsl2ShdslMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 48)
)
hdsl2ShdslMIB.setRevisions(
        ("2011-12-21 00:00",
         "2005-12-07 00:00",
         "2002-05-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hdsl2ShdslPerfCurrDayCount(Gauge32, TextualConvention):
    status = "current"
    displayHint = "d"


class Hdsl2Shdsl1DayIntervalCount(Gauge32, TextualConvention):
    status = "current"
    displayHint = "d"


class Hdsl2ShdslPerfTimeElapsed(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )



class Hdsl2ShdslPerfIntervalThreshold(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )



class Hdsl2ShdslUnitId(Integer32, TextualConvention):
    status = "current"
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



class Hdsl2ShdslUnitSide(Integer32, TextualConvention):
    status = "current"
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



class Hdsl2ShdslWirePair(Integer32, TextualConvention):
    status = "current"
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
        *(("wirePair1", 1),
          ("wirePair2", 2),
          ("wirePair3", 3),
          ("wirePair4", 4))
    )



class Hdsl2ShdslTransmissionModeType(Bits, TextualConvention):
    status = "current"


class Hdsl2ShdslClockReferenceType(Integer32, TextualConvention):
    status = "current"
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
        *(("dataClk", 4),
          ("dataOrNetworkClk", 3),
          ("localClk", 1),
          ("networkClk", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hdsl2ShdslNotifications_ObjectIdentity = ObjectIdentity
hdsl2ShdslNotifications = _Hdsl2ShdslNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 48, 0)
)
_Hdsl2ShdslMibObjects_ObjectIdentity = ObjectIdentity
hdsl2ShdslMibObjects = _Hdsl2ShdslMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 48, 1)
)
_Hdsl2ShdslSpanConfTable_Object = MibTable
hdsl2ShdslSpanConfTable = _Hdsl2ShdslSpanConfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 1)
)
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfTable.setStatus("current")
_Hdsl2ShdslSpanConfEntry_Object = MibTableRow
hdsl2ShdslSpanConfEntry = _Hdsl2ShdslSpanConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 1, 1)
)
hdsl2ShdslSpanConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfEntry.setStatus("current")


class _Hdsl2ShdslSpanConfNumRepeaters_Type(Unsigned32):
    """Custom type hdsl2ShdslSpanConfNumRepeaters based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Hdsl2ShdslSpanConfNumRepeaters_Type.__name__ = "Unsigned32"
_Hdsl2ShdslSpanConfNumRepeaters_Object = MibTableColumn
hdsl2ShdslSpanConfNumRepeaters = _Hdsl2ShdslSpanConfNumRepeaters_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 1, 1, 1),
    _Hdsl2ShdslSpanConfNumRepeaters_Type()
)
hdsl2ShdslSpanConfNumRepeaters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfNumRepeaters.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfNumRepeaters.setUnits("repeaters")


class _Hdsl2ShdslSpanConfProfile_Type(SnmpAdminString):
    """Custom type hdsl2ShdslSpanConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hdsl2ShdslSpanConfProfile_Type.__name__ = "SnmpAdminString"
_Hdsl2ShdslSpanConfProfile_Object = MibTableColumn
hdsl2ShdslSpanConfProfile = _Hdsl2ShdslSpanConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 1, 1, 2),
    _Hdsl2ShdslSpanConfProfile_Type()
)
hdsl2ShdslSpanConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfProfile.setStatus("current")


class _Hdsl2ShdslSpanConfAlarmProfile_Type(SnmpAdminString):
    """Custom type hdsl2ShdslSpanConfAlarmProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hdsl2ShdslSpanConfAlarmProfile_Type.__name__ = "SnmpAdminString"
_Hdsl2ShdslSpanConfAlarmProfile_Object = MibTableColumn
hdsl2ShdslSpanConfAlarmProfile = _Hdsl2ShdslSpanConfAlarmProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 1, 1, 3),
    _Hdsl2ShdslSpanConfAlarmProfile_Type()
)
hdsl2ShdslSpanConfAlarmProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfAlarmProfile.setStatus("current")
_Hdsl2ShdslSpanStatusTable_Object = MibTable
hdsl2ShdslSpanStatusTable = _Hdsl2ShdslSpanStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 2)
)
if mibBuilder.loadTexts:
    hdsl2ShdslSpanStatusTable.setStatus("current")
_Hdsl2ShdslSpanStatusEntry_Object = MibTableRow
hdsl2ShdslSpanStatusEntry = _Hdsl2ShdslSpanStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 2, 1)
)
hdsl2ShdslSpanStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hdsl2ShdslSpanStatusEntry.setStatus("current")


class _Hdsl2ShdslStatusNumAvailRepeaters_Type(Unsigned32):
    """Custom type hdsl2ShdslStatusNumAvailRepeaters based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Hdsl2ShdslStatusNumAvailRepeaters_Type.__name__ = "Unsigned32"
_Hdsl2ShdslStatusNumAvailRepeaters_Object = MibTableColumn
hdsl2ShdslStatusNumAvailRepeaters = _Hdsl2ShdslStatusNumAvailRepeaters_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 2, 1, 1),
    _Hdsl2ShdslStatusNumAvailRepeaters_Type()
)
hdsl2ShdslStatusNumAvailRepeaters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslStatusNumAvailRepeaters.setStatus("current")


class _Hdsl2ShdslStatusMaxAttainableLineRate_Type(Unsigned32):
    """Custom type hdsl2ShdslStatusMaxAttainableLineRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hdsl2ShdslStatusMaxAttainableLineRate_Type.__name__ = "Unsigned32"
_Hdsl2ShdslStatusMaxAttainableLineRate_Object = MibTableColumn
hdsl2ShdslStatusMaxAttainableLineRate = _Hdsl2ShdslStatusMaxAttainableLineRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 2, 1, 2),
    _Hdsl2ShdslStatusMaxAttainableLineRate_Type()
)
hdsl2ShdslStatusMaxAttainableLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslStatusMaxAttainableLineRate.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslStatusMaxAttainableLineRate.setUnits("bps")


class _Hdsl2ShdslStatusActualLineRate_Type(Unsigned32):
    """Custom type hdsl2ShdslStatusActualLineRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hdsl2ShdslStatusActualLineRate_Type.__name__ = "Unsigned32"
_Hdsl2ShdslStatusActualLineRate_Object = MibTableColumn
hdsl2ShdslStatusActualLineRate = _Hdsl2ShdslStatusActualLineRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 2, 1, 3),
    _Hdsl2ShdslStatusActualLineRate_Type()
)
hdsl2ShdslStatusActualLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslStatusActualLineRate.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslStatusActualLineRate.setUnits("bps")
_Hdsl2ShdslStatusTransmissionModeCurrent_Type = Hdsl2ShdslTransmissionModeType
_Hdsl2ShdslStatusTransmissionModeCurrent_Object = MibTableColumn
hdsl2ShdslStatusTransmissionModeCurrent = _Hdsl2ShdslStatusTransmissionModeCurrent_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 2, 1, 4),
    _Hdsl2ShdslStatusTransmissionModeCurrent_Type()
)
hdsl2ShdslStatusTransmissionModeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslStatusTransmissionModeCurrent.setStatus("current")


class _Hdsl2ShdslStatusMaxAttainablePayloadRate_Type(Unsigned32):
    """Custom type hdsl2ShdslStatusMaxAttainablePayloadRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hdsl2ShdslStatusMaxAttainablePayloadRate_Type.__name__ = "Unsigned32"
_Hdsl2ShdslStatusMaxAttainablePayloadRate_Object = MibTableColumn
hdsl2ShdslStatusMaxAttainablePayloadRate = _Hdsl2ShdslStatusMaxAttainablePayloadRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 2, 1, 5),
    _Hdsl2ShdslStatusMaxAttainablePayloadRate_Type()
)
hdsl2ShdslStatusMaxAttainablePayloadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslStatusMaxAttainablePayloadRate.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslStatusMaxAttainablePayloadRate.setUnits("bps")


class _Hdsl2ShdslStatusActualPayloadRate_Type(Unsigned32):
    """Custom type hdsl2ShdslStatusActualPayloadRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hdsl2ShdslStatusActualPayloadRate_Type.__name__ = "Unsigned32"
_Hdsl2ShdslStatusActualPayloadRate_Object = MibTableColumn
hdsl2ShdslStatusActualPayloadRate = _Hdsl2ShdslStatusActualPayloadRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 2, 1, 6),
    _Hdsl2ShdslStatusActualPayloadRate_Type()
)
hdsl2ShdslStatusActualPayloadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslStatusActualPayloadRate.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslStatusActualPayloadRate.setUnits("bps")
_Hdsl2ShdslInventoryTable_Object = MibTable
hdsl2ShdslInventoryTable = _Hdsl2ShdslInventoryTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3)
)
if mibBuilder.loadTexts:
    hdsl2ShdslInventoryTable.setStatus("current")
_Hdsl2ShdslInventoryEntry_Object = MibTableRow
hdsl2ShdslInventoryEntry = _Hdsl2ShdslInventoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3, 1)
)
hdsl2ShdslInventoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvIndex"),
)
if mibBuilder.loadTexts:
    hdsl2ShdslInventoryEntry.setStatus("current")
_Hdsl2ShdslInvIndex_Type = Hdsl2ShdslUnitId
_Hdsl2ShdslInvIndex_Object = MibTableColumn
hdsl2ShdslInvIndex = _Hdsl2ShdslInvIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3, 1, 1),
    _Hdsl2ShdslInvIndex_Type()
)
hdsl2ShdslInvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hdsl2ShdslInvIndex.setStatus("current")


class _Hdsl2ShdslInvVendorID_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hdsl2ShdslInvVendorID_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorID_Object = MibTableColumn
hdsl2ShdslInvVendorID = _Hdsl2ShdslInvVendorID_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3, 1, 2),
    _Hdsl2ShdslInvVendorID_Type()
)
hdsl2ShdslInvVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorID.setStatus("current")


class _Hdsl2ShdslInvVendorModelNumber_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorModelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Hdsl2ShdslInvVendorModelNumber_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorModelNumber_Object = MibTableColumn
hdsl2ShdslInvVendorModelNumber = _Hdsl2ShdslInvVendorModelNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3, 1, 3),
    _Hdsl2ShdslInvVendorModelNumber_Type()
)
hdsl2ShdslInvVendorModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorModelNumber.setStatus("current")


class _Hdsl2ShdslInvVendorSerialNumber_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Hdsl2ShdslInvVendorSerialNumber_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorSerialNumber_Object = MibTableColumn
hdsl2ShdslInvVendorSerialNumber = _Hdsl2ShdslInvVendorSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3, 1, 4),
    _Hdsl2ShdslInvVendorSerialNumber_Type()
)
hdsl2ShdslInvVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorSerialNumber.setStatus("current")
_Hdsl2ShdslInvVendorEOCSoftwareVersion_Type = Integer32
_Hdsl2ShdslInvVendorEOCSoftwareVersion_Object = MibTableColumn
hdsl2ShdslInvVendorEOCSoftwareVersion = _Hdsl2ShdslInvVendorEOCSoftwareVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3, 1, 5),
    _Hdsl2ShdslInvVendorEOCSoftwareVersion_Type()
)
hdsl2ShdslInvVendorEOCSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorEOCSoftwareVersion.setStatus("current")
_Hdsl2ShdslInvStandardVersion_Type = Integer32
_Hdsl2ShdslInvStandardVersion_Object = MibTableColumn
hdsl2ShdslInvStandardVersion = _Hdsl2ShdslInvStandardVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3, 1, 6),
    _Hdsl2ShdslInvStandardVersion_Type()
)
hdsl2ShdslInvStandardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvStandardVersion.setStatus("current")


class _Hdsl2ShdslInvVendorListNumber_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorListNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Hdsl2ShdslInvVendorListNumber_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorListNumber_Object = MibTableColumn
hdsl2ShdslInvVendorListNumber = _Hdsl2ShdslInvVendorListNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3, 1, 7),
    _Hdsl2ShdslInvVendorListNumber_Type()
)
hdsl2ShdslInvVendorListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorListNumber.setStatus("current")


class _Hdsl2ShdslInvVendorIssueNumber_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorIssueNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hdsl2ShdslInvVendorIssueNumber_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorIssueNumber_Object = MibTableColumn
hdsl2ShdslInvVendorIssueNumber = _Hdsl2ShdslInvVendorIssueNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3, 1, 8),
    _Hdsl2ShdslInvVendorIssueNumber_Type()
)
hdsl2ShdslInvVendorIssueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorIssueNumber.setStatus("current")


class _Hdsl2ShdslInvVendorSoftwareVersion_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Hdsl2ShdslInvVendorSoftwareVersion_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorSoftwareVersion_Object = MibTableColumn
hdsl2ShdslInvVendorSoftwareVersion = _Hdsl2ShdslInvVendorSoftwareVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3, 1, 9),
    _Hdsl2ShdslInvVendorSoftwareVersion_Type()
)
hdsl2ShdslInvVendorSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorSoftwareVersion.setStatus("current")


class _Hdsl2ShdslInvEquipmentCode_Type(OctetString):
    """Custom type hdsl2ShdslInvEquipmentCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Hdsl2ShdslInvEquipmentCode_Type.__name__ = "OctetString"
_Hdsl2ShdslInvEquipmentCode_Object = MibTableColumn
hdsl2ShdslInvEquipmentCode = _Hdsl2ShdslInvEquipmentCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3, 1, 10),
    _Hdsl2ShdslInvEquipmentCode_Type()
)
hdsl2ShdslInvEquipmentCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvEquipmentCode.setStatus("current")


class _Hdsl2ShdslInvVendorOther_Type(OctetString):
    """Custom type hdsl2ShdslInvVendorOther based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Hdsl2ShdslInvVendorOther_Type.__name__ = "OctetString"
_Hdsl2ShdslInvVendorOther_Object = MibTableColumn
hdsl2ShdslInvVendorOther = _Hdsl2ShdslInvVendorOther_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3, 1, 11),
    _Hdsl2ShdslInvVendorOther_Type()
)
hdsl2ShdslInvVendorOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvVendorOther.setStatus("current")
_Hdsl2ShdslInvTransmissionModeCapability_Type = Hdsl2ShdslTransmissionModeType
_Hdsl2ShdslInvTransmissionModeCapability_Object = MibTableColumn
hdsl2ShdslInvTransmissionModeCapability = _Hdsl2ShdslInvTransmissionModeCapability_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 3, 1, 12),
    _Hdsl2ShdslInvTransmissionModeCapability_Type()
)
hdsl2ShdslInvTransmissionModeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslInvTransmissionModeCapability.setStatus("current")
_Hdsl2ShdslEndpointConfTable_Object = MibTable
hdsl2ShdslEndpointConfTable = _Hdsl2ShdslEndpointConfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 4)
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfTable.setStatus("current")
_Hdsl2ShdslEndpointConfEntry_Object = MibTableRow
hdsl2ShdslEndpointConfEntry = _Hdsl2ShdslEndpointConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 4, 1)
)
hdsl2ShdslEndpointConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointSide"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointWirePair"),
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfEntry.setStatus("current")
_Hdsl2ShdslEndpointSide_Type = Hdsl2ShdslUnitSide
_Hdsl2ShdslEndpointSide_Object = MibTableColumn
hdsl2ShdslEndpointSide = _Hdsl2ShdslEndpointSide_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 4, 1, 1),
    _Hdsl2ShdslEndpointSide_Type()
)
hdsl2ShdslEndpointSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointSide.setStatus("current")
_Hdsl2ShdslEndpointWirePair_Type = Hdsl2ShdslWirePair
_Hdsl2ShdslEndpointWirePair_Object = MibTableColumn
hdsl2ShdslEndpointWirePair = _Hdsl2ShdslEndpointWirePair_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 4, 1, 2),
    _Hdsl2ShdslEndpointWirePair_Type()
)
hdsl2ShdslEndpointWirePair.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointWirePair.setStatus("current")


class _Hdsl2ShdslEndpointAlarmConfProfile_Type(SnmpAdminString):
    """Custom type hdsl2ShdslEndpointAlarmConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hdsl2ShdslEndpointAlarmConfProfile_Type.__name__ = "SnmpAdminString"
_Hdsl2ShdslEndpointAlarmConfProfile_Object = MibTableColumn
hdsl2ShdslEndpointAlarmConfProfile = _Hdsl2ShdslEndpointAlarmConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 4, 1, 3),
    _Hdsl2ShdslEndpointAlarmConfProfile_Type()
)
hdsl2ShdslEndpointAlarmConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointAlarmConfProfile.setStatus("current")
_Hdsl2ShdslEndpointCurrTable_Object = MibTable
hdsl2ShdslEndpointCurrTable = _Hdsl2ShdslEndpointCurrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5)
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrTable.setStatus("current")
_Hdsl2ShdslEndpointCurrEntry_Object = MibTableRow
hdsl2ShdslEndpointCurrEntry = _Hdsl2ShdslEndpointCurrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1)
)
hdsl2ShdslEndpointCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointSide"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointWirePair"),
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrEntry.setStatus("current")


class _Hdsl2ShdslEndpointCurrAtn_Type(Integer32):
    """Custom type hdsl2ShdslEndpointCurrAtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_Hdsl2ShdslEndpointCurrAtn_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointCurrAtn_Object = MibTableColumn
hdsl2ShdslEndpointCurrAtn = _Hdsl2ShdslEndpointCurrAtn_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 1),
    _Hdsl2ShdslEndpointCurrAtn_Type()
)
hdsl2ShdslEndpointCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrAtn.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrAtn.setUnits("dB")


class _Hdsl2ShdslEndpointCurrSnrMgn_Type(Integer32):
    """Custom type hdsl2ShdslEndpointCurrSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_Hdsl2ShdslEndpointCurrSnrMgn_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointCurrSnrMgn_Object = MibTableColumn
hdsl2ShdslEndpointCurrSnrMgn = _Hdsl2ShdslEndpointCurrSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 2),
    _Hdsl2ShdslEndpointCurrSnrMgn_Type()
)
hdsl2ShdslEndpointCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrSnrMgn.setUnits("dB")


class _Hdsl2ShdslEndpointCurrStatus_Type(Bits):
    """Custom type hdsl2ShdslEndpointCurrStatus based on Bits"""
    namedValues = NamedValues(
        *(("configInitFailure", 7),
          ("dcContinuityFault", 3),
          ("deviceFault", 2),
          ("loopAttenuationAlarm", 5),
          ("loopbackActive", 10),
          ("loswFailureAlarm", 6),
          ("noDefect", 0),
          ("noNeighborPresent", 9),
          ("powerBackoff", 1),
          ("protocolInitFailure", 8),
          ("snrMarginAlarm", 4))
    )

_Hdsl2ShdslEndpointCurrStatus_Type.__name__ = "Bits"
_Hdsl2ShdslEndpointCurrStatus_Object = MibTableColumn
hdsl2ShdslEndpointCurrStatus = _Hdsl2ShdslEndpointCurrStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 3),
    _Hdsl2ShdslEndpointCurrStatus_Type()
)
hdsl2ShdslEndpointCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrStatus.setStatus("current")
_Hdsl2ShdslEndpointES_Type = Counter32
_Hdsl2ShdslEndpointES_Object = MibTableColumn
hdsl2ShdslEndpointES = _Hdsl2ShdslEndpointES_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 4),
    _Hdsl2ShdslEndpointES_Type()
)
hdsl2ShdslEndpointES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointES.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointES.setUnits("seconds")
_Hdsl2ShdslEndpointSES_Type = Counter32
_Hdsl2ShdslEndpointSES_Object = MibTableColumn
hdsl2ShdslEndpointSES = _Hdsl2ShdslEndpointSES_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 5),
    _Hdsl2ShdslEndpointSES_Type()
)
hdsl2ShdslEndpointSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointSES.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointSES.setUnits("seconds")
_Hdsl2ShdslEndpointCRCanomalies_Type = Counter32
_Hdsl2ShdslEndpointCRCanomalies_Object = MibTableColumn
hdsl2ShdslEndpointCRCanomalies = _Hdsl2ShdslEndpointCRCanomalies_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 6),
    _Hdsl2ShdslEndpointCRCanomalies_Type()
)
hdsl2ShdslEndpointCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCRCanomalies.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCRCanomalies.setUnits("detected CRC Anomalies")
_Hdsl2ShdslEndpointLOSWS_Type = Counter32
_Hdsl2ShdslEndpointLOSWS_Object = MibTableColumn
hdsl2ShdslEndpointLOSWS = _Hdsl2ShdslEndpointLOSWS_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 7),
    _Hdsl2ShdslEndpointLOSWS_Type()
)
hdsl2ShdslEndpointLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointLOSWS.setUnits("seconds")
_Hdsl2ShdslEndpointUAS_Type = Counter32
_Hdsl2ShdslEndpointUAS_Object = MibTableColumn
hdsl2ShdslEndpointUAS = _Hdsl2ShdslEndpointUAS_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 8),
    _Hdsl2ShdslEndpointUAS_Type()
)
hdsl2ShdslEndpointUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointUAS.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointUAS.setUnits("seconds")
_Hdsl2ShdslEndpointCurr15MinTimeElapsed_Type = Hdsl2ShdslPerfTimeElapsed
_Hdsl2ShdslEndpointCurr15MinTimeElapsed_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinTimeElapsed = _Hdsl2ShdslEndpointCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 9),
    _Hdsl2ShdslEndpointCurr15MinTimeElapsed_Type()
)
hdsl2ShdslEndpointCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinTimeElapsed.setUnits("seconds")
_Hdsl2ShdslEndpointCurr15MinES_Type = PerfCurrentCount
_Hdsl2ShdslEndpointCurr15MinES_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinES = _Hdsl2ShdslEndpointCurr15MinES_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 10),
    _Hdsl2ShdslEndpointCurr15MinES_Type()
)
hdsl2ShdslEndpointCurr15MinES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinES.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinES.setUnits("seconds")
_Hdsl2ShdslEndpointCurr15MinSES_Type = PerfCurrentCount
_Hdsl2ShdslEndpointCurr15MinSES_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinSES = _Hdsl2ShdslEndpointCurr15MinSES_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 11),
    _Hdsl2ShdslEndpointCurr15MinSES_Type()
)
hdsl2ShdslEndpointCurr15MinSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinSES.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinSES.setUnits("seconds")
_Hdsl2ShdslEndpointCurr15MinCRCanomalies_Type = PerfCurrentCount
_Hdsl2ShdslEndpointCurr15MinCRCanomalies_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinCRCanomalies = _Hdsl2ShdslEndpointCurr15MinCRCanomalies_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 12),
    _Hdsl2ShdslEndpointCurr15MinCRCanomalies_Type()
)
hdsl2ShdslEndpointCurr15MinCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinCRCanomalies.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinCRCanomalies.setUnits("detected CRC Anomalies")
_Hdsl2ShdslEndpointCurr15MinLOSWS_Type = PerfCurrentCount
_Hdsl2ShdslEndpointCurr15MinLOSWS_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinLOSWS = _Hdsl2ShdslEndpointCurr15MinLOSWS_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 13),
    _Hdsl2ShdslEndpointCurr15MinLOSWS_Type()
)
hdsl2ShdslEndpointCurr15MinLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinLOSWS.setUnits("seconds")
_Hdsl2ShdslEndpointCurr15MinUAS_Type = PerfCurrentCount
_Hdsl2ShdslEndpointCurr15MinUAS_Object = MibTableColumn
hdsl2ShdslEndpointCurr15MinUAS = _Hdsl2ShdslEndpointCurr15MinUAS_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 14),
    _Hdsl2ShdslEndpointCurr15MinUAS_Type()
)
hdsl2ShdslEndpointCurr15MinUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinUAS.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr15MinUAS.setUnits("seconds")
_Hdsl2ShdslEndpointCurr1DayTimeElapsed_Type = Hdsl2ShdslPerfTimeElapsed
_Hdsl2ShdslEndpointCurr1DayTimeElapsed_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayTimeElapsed = _Hdsl2ShdslEndpointCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 15),
    _Hdsl2ShdslEndpointCurr1DayTimeElapsed_Type()
)
hdsl2ShdslEndpointCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayTimeElapsed.setUnits("seconds")
_Hdsl2ShdslEndpointCurr1DayES_Type = Hdsl2ShdslPerfCurrDayCount
_Hdsl2ShdslEndpointCurr1DayES_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayES = _Hdsl2ShdslEndpointCurr1DayES_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 16),
    _Hdsl2ShdslEndpointCurr1DayES_Type()
)
hdsl2ShdslEndpointCurr1DayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayES.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayES.setUnits("seconds")
_Hdsl2ShdslEndpointCurr1DaySES_Type = Hdsl2ShdslPerfCurrDayCount
_Hdsl2ShdslEndpointCurr1DaySES_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DaySES = _Hdsl2ShdslEndpointCurr1DaySES_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 17),
    _Hdsl2ShdslEndpointCurr1DaySES_Type()
)
hdsl2ShdslEndpointCurr1DaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DaySES.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DaySES.setUnits("seconds")
_Hdsl2ShdslEndpointCurr1DayCRCanomalies_Type = Hdsl2ShdslPerfCurrDayCount
_Hdsl2ShdslEndpointCurr1DayCRCanomalies_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayCRCanomalies = _Hdsl2ShdslEndpointCurr1DayCRCanomalies_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 18),
    _Hdsl2ShdslEndpointCurr1DayCRCanomalies_Type()
)
hdsl2ShdslEndpointCurr1DayCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayCRCanomalies.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayCRCanomalies.setUnits("detected CRC Anomalies")
_Hdsl2ShdslEndpointCurr1DayLOSWS_Type = Hdsl2ShdslPerfCurrDayCount
_Hdsl2ShdslEndpointCurr1DayLOSWS_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayLOSWS = _Hdsl2ShdslEndpointCurr1DayLOSWS_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 19),
    _Hdsl2ShdslEndpointCurr1DayLOSWS_Type()
)
hdsl2ShdslEndpointCurr1DayLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayLOSWS.setUnits("seconds")
_Hdsl2ShdslEndpointCurr1DayUAS_Type = Hdsl2ShdslPerfCurrDayCount
_Hdsl2ShdslEndpointCurr1DayUAS_Object = MibTableColumn
hdsl2ShdslEndpointCurr1DayUAS = _Hdsl2ShdslEndpointCurr1DayUAS_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 20),
    _Hdsl2ShdslEndpointCurr1DayUAS_Type()
)
hdsl2ShdslEndpointCurr1DayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayUAS.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurr1DayUAS.setUnits("seconds")


class _Hdsl2ShdslEndpointCurrTipRingReversal_Type(Integer32):
    """Custom type hdsl2ShdslEndpointCurrTipRingReversal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reversed", 2))
    )


_Hdsl2ShdslEndpointCurrTipRingReversal_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointCurrTipRingReversal_Object = MibTableColumn
hdsl2ShdslEndpointCurrTipRingReversal = _Hdsl2ShdslEndpointCurrTipRingReversal_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 21),
    _Hdsl2ShdslEndpointCurrTipRingReversal_Type()
)
hdsl2ShdslEndpointCurrTipRingReversal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrTipRingReversal.setStatus("current")


class _Hdsl2ShdslEndpointCurrActivationState_Type(Integer32):
    """Custom type hdsl2ShdslEndpointCurrActivationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activation", 2),
          ("data", 3),
          ("preActivation", 1))
    )


_Hdsl2ShdslEndpointCurrActivationState_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointCurrActivationState_Object = MibTableColumn
hdsl2ShdslEndpointCurrActivationState = _Hdsl2ShdslEndpointCurrActivationState_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 5, 1, 22),
    _Hdsl2ShdslEndpointCurrActivationState_Type()
)
hdsl2ShdslEndpointCurrActivationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrActivationState.setStatus("current")
_Hdsl2Shdsl15MinIntervalTable_Object = MibTable
hdsl2Shdsl15MinIntervalTable = _Hdsl2Shdsl15MinIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 6)
)
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalTable.setStatus("current")
_Hdsl2Shdsl15MinIntervalEntry_Object = MibTableRow
hdsl2Shdsl15MinIntervalEntry = _Hdsl2Shdsl15MinIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 6, 1)
)
hdsl2Shdsl15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointSide"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointWirePair"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2Shdsl15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalEntry.setStatus("current")


class _Hdsl2Shdsl15MinIntervalNumber_Type(Unsigned32):
    """Custom type hdsl2Shdsl15MinIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Hdsl2Shdsl15MinIntervalNumber_Type.__name__ = "Unsigned32"
_Hdsl2Shdsl15MinIntervalNumber_Object = MibTableColumn
hdsl2Shdsl15MinIntervalNumber = _Hdsl2Shdsl15MinIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 6, 1, 1),
    _Hdsl2Shdsl15MinIntervalNumber_Type()
)
hdsl2Shdsl15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalNumber.setStatus("current")
_Hdsl2Shdsl15MinIntervalES_Type = PerfIntervalCount
_Hdsl2Shdsl15MinIntervalES_Object = MibTableColumn
hdsl2Shdsl15MinIntervalES = _Hdsl2Shdsl15MinIntervalES_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 6, 1, 2),
    _Hdsl2Shdsl15MinIntervalES_Type()
)
hdsl2Shdsl15MinIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalES.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalES.setUnits("seconds")
_Hdsl2Shdsl15MinIntervalSES_Type = PerfIntervalCount
_Hdsl2Shdsl15MinIntervalSES_Object = MibTableColumn
hdsl2Shdsl15MinIntervalSES = _Hdsl2Shdsl15MinIntervalSES_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 6, 1, 3),
    _Hdsl2Shdsl15MinIntervalSES_Type()
)
hdsl2Shdsl15MinIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalSES.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalSES.setUnits("seconds")
_Hdsl2Shdsl15MinIntervalCRCanomalies_Type = PerfIntervalCount
_Hdsl2Shdsl15MinIntervalCRCanomalies_Object = MibTableColumn
hdsl2Shdsl15MinIntervalCRCanomalies = _Hdsl2Shdsl15MinIntervalCRCanomalies_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 6, 1, 4),
    _Hdsl2Shdsl15MinIntervalCRCanomalies_Type()
)
hdsl2Shdsl15MinIntervalCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalCRCanomalies.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalCRCanomalies.setUnits("detected CRC Anomalies")
_Hdsl2Shdsl15MinIntervalLOSWS_Type = PerfIntervalCount
_Hdsl2Shdsl15MinIntervalLOSWS_Object = MibTableColumn
hdsl2Shdsl15MinIntervalLOSWS = _Hdsl2Shdsl15MinIntervalLOSWS_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 6, 1, 5),
    _Hdsl2Shdsl15MinIntervalLOSWS_Type()
)
hdsl2Shdsl15MinIntervalLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalLOSWS.setUnits("seconds")
_Hdsl2Shdsl15MinIntervalUAS_Type = PerfIntervalCount
_Hdsl2Shdsl15MinIntervalUAS_Object = MibTableColumn
hdsl2Shdsl15MinIntervalUAS = _Hdsl2Shdsl15MinIntervalUAS_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 6, 1, 6),
    _Hdsl2Shdsl15MinIntervalUAS_Type()
)
hdsl2Shdsl15MinIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalUAS.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalUAS.setUnits("seconds")
_Hdsl2Shdsl1DayIntervalTable_Object = MibTable
hdsl2Shdsl1DayIntervalTable = _Hdsl2Shdsl1DayIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 7)
)
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalTable.setStatus("current")
_Hdsl2Shdsl1DayIntervalEntry_Object = MibTableRow
hdsl2Shdsl1DayIntervalEntry = _Hdsl2Shdsl1DayIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 7, 1)
)
hdsl2Shdsl1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointSide"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointWirePair"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2Shdsl1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalEntry.setStatus("current")


class _Hdsl2Shdsl1DayIntervalNumber_Type(Unsigned32):
    """Custom type hdsl2Shdsl1DayIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Hdsl2Shdsl1DayIntervalNumber_Type.__name__ = "Unsigned32"
_Hdsl2Shdsl1DayIntervalNumber_Object = MibTableColumn
hdsl2Shdsl1DayIntervalNumber = _Hdsl2Shdsl1DayIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 7, 1, 1),
    _Hdsl2Shdsl1DayIntervalNumber_Type()
)
hdsl2Shdsl1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalNumber.setStatus("current")
_Hdsl2Shdsl1DayIntervalMoniSecs_Type = Hdsl2ShdslPerfTimeElapsed
_Hdsl2Shdsl1DayIntervalMoniSecs_Object = MibTableColumn
hdsl2Shdsl1DayIntervalMoniSecs = _Hdsl2Shdsl1DayIntervalMoniSecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 7, 1, 2),
    _Hdsl2Shdsl1DayIntervalMoniSecs_Type()
)
hdsl2Shdsl1DayIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalMoniSecs.setUnits("seconds")
_Hdsl2Shdsl1DayIntervalES_Type = Hdsl2Shdsl1DayIntervalCount
_Hdsl2Shdsl1DayIntervalES_Object = MibTableColumn
hdsl2Shdsl1DayIntervalES = _Hdsl2Shdsl1DayIntervalES_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 7, 1, 3),
    _Hdsl2Shdsl1DayIntervalES_Type()
)
hdsl2Shdsl1DayIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalES.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalES.setUnits("seconds")
_Hdsl2Shdsl1DayIntervalSES_Type = Hdsl2Shdsl1DayIntervalCount
_Hdsl2Shdsl1DayIntervalSES_Object = MibTableColumn
hdsl2Shdsl1DayIntervalSES = _Hdsl2Shdsl1DayIntervalSES_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 7, 1, 4),
    _Hdsl2Shdsl1DayIntervalSES_Type()
)
hdsl2Shdsl1DayIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalSES.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalSES.setUnits("seconds")
_Hdsl2Shdsl1DayIntervalCRCanomalies_Type = Hdsl2Shdsl1DayIntervalCount
_Hdsl2Shdsl1DayIntervalCRCanomalies_Object = MibTableColumn
hdsl2Shdsl1DayIntervalCRCanomalies = _Hdsl2Shdsl1DayIntervalCRCanomalies_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 7, 1, 5),
    _Hdsl2Shdsl1DayIntervalCRCanomalies_Type()
)
hdsl2Shdsl1DayIntervalCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalCRCanomalies.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalCRCanomalies.setUnits("detected CRC Anomalies")
_Hdsl2Shdsl1DayIntervalLOSWS_Type = Hdsl2Shdsl1DayIntervalCount
_Hdsl2Shdsl1DayIntervalLOSWS_Object = MibTableColumn
hdsl2Shdsl1DayIntervalLOSWS = _Hdsl2Shdsl1DayIntervalLOSWS_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 7, 1, 6),
    _Hdsl2Shdsl1DayIntervalLOSWS_Type()
)
hdsl2Shdsl1DayIntervalLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalLOSWS.setUnits("seconds")
_Hdsl2Shdsl1DayIntervalUAS_Type = Hdsl2Shdsl1DayIntervalCount
_Hdsl2Shdsl1DayIntervalUAS_Object = MibTableColumn
hdsl2Shdsl1DayIntervalUAS = _Hdsl2Shdsl1DayIntervalUAS_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 7, 1, 7),
    _Hdsl2Shdsl1DayIntervalUAS_Type()
)
hdsl2Shdsl1DayIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalUAS.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalUAS.setUnits("seconds")
_Hdsl2ShdslEndpointMaintTable_Object = MibTable
hdsl2ShdslEndpointMaintTable = _Hdsl2ShdslEndpointMaintTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 8)
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointMaintTable.setStatus("current")
_Hdsl2ShdslEndpointMaintEntry_Object = MibTableRow
hdsl2ShdslEndpointMaintEntry = _Hdsl2ShdslEndpointMaintEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 8, 1)
)
hdsl2ShdslEndpointMaintEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointSide"),
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointMaintEntry.setStatus("current")


class _Hdsl2ShdslMaintLoopbackConfig_Type(Integer32):
    """Custom type hdsl2ShdslMaintLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLoopback", 1),
          ("normalLoopback", 2),
          ("specialLoopback", 3))
    )


_Hdsl2ShdslMaintLoopbackConfig_Type.__name__ = "Integer32"
_Hdsl2ShdslMaintLoopbackConfig_Object = MibTableColumn
hdsl2ShdslMaintLoopbackConfig = _Hdsl2ShdslMaintLoopbackConfig_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 8, 1, 1),
    _Hdsl2ShdslMaintLoopbackConfig_Type()
)
hdsl2ShdslMaintLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslMaintLoopbackConfig.setStatus("current")


class _Hdsl2ShdslMaintTipRingReversal_Type(Integer32):
    """Custom type hdsl2ShdslMaintTipRingReversal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reversed", 2))
    )


_Hdsl2ShdslMaintTipRingReversal_Type.__name__ = "Integer32"
_Hdsl2ShdslMaintTipRingReversal_Object = MibTableColumn
hdsl2ShdslMaintTipRingReversal = _Hdsl2ShdslMaintTipRingReversal_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 8, 1, 2),
    _Hdsl2ShdslMaintTipRingReversal_Type()
)
hdsl2ShdslMaintTipRingReversal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslMaintTipRingReversal.setStatus("current")


class _Hdsl2ShdslMaintPowerBackOff_Type(Integer32):
    """Custom type hdsl2ShdslMaintPowerBackOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("enhanced", 2))
    )


_Hdsl2ShdslMaintPowerBackOff_Type.__name__ = "Integer32"
_Hdsl2ShdslMaintPowerBackOff_Object = MibTableColumn
hdsl2ShdslMaintPowerBackOff = _Hdsl2ShdslMaintPowerBackOff_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 8, 1, 3),
    _Hdsl2ShdslMaintPowerBackOff_Type()
)
hdsl2ShdslMaintPowerBackOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslMaintPowerBackOff.setStatus("current")


class _Hdsl2ShdslMaintSoftRestart_Type(Integer32):
    """Custom type hdsl2ShdslMaintSoftRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("restart", 2))
    )


_Hdsl2ShdslMaintSoftRestart_Type.__name__ = "Integer32"
_Hdsl2ShdslMaintSoftRestart_Object = MibTableColumn
hdsl2ShdslMaintSoftRestart = _Hdsl2ShdslMaintSoftRestart_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 8, 1, 4),
    _Hdsl2ShdslMaintSoftRestart_Type()
)
hdsl2ShdslMaintSoftRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslMaintSoftRestart.setStatus("current")
_Hdsl2ShdslUnitMaintTable_Object = MibTable
hdsl2ShdslUnitMaintTable = _Hdsl2ShdslUnitMaintTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 9)
)
if mibBuilder.loadTexts:
    hdsl2ShdslUnitMaintTable.setStatus("current")
_Hdsl2ShdslUnitMaintEntry_Object = MibTableRow
hdsl2ShdslUnitMaintEntry = _Hdsl2ShdslUnitMaintEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 9, 1)
)
hdsl2ShdslUnitMaintEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvIndex"),
)
if mibBuilder.loadTexts:
    hdsl2ShdslUnitMaintEntry.setStatus("current")


class _Hdsl2ShdslMaintLoopbackTimeout_Type(Integer32):
    """Custom type hdsl2ShdslMaintLoopbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Hdsl2ShdslMaintLoopbackTimeout_Type.__name__ = "Integer32"
_Hdsl2ShdslMaintLoopbackTimeout_Object = MibTableColumn
hdsl2ShdslMaintLoopbackTimeout = _Hdsl2ShdslMaintLoopbackTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 9, 1, 1),
    _Hdsl2ShdslMaintLoopbackTimeout_Type()
)
hdsl2ShdslMaintLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2ShdslMaintLoopbackTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslMaintLoopbackTimeout.setUnits("minutes")


class _Hdsl2ShdslMaintUnitPowerSource_Type(Integer32):
    """Custom type hdsl2ShdslMaintUnitPowerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("span", 2))
    )


_Hdsl2ShdslMaintUnitPowerSource_Type.__name__ = "Integer32"
_Hdsl2ShdslMaintUnitPowerSource_Object = MibTableColumn
hdsl2ShdslMaintUnitPowerSource = _Hdsl2ShdslMaintUnitPowerSource_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 9, 1, 2),
    _Hdsl2ShdslMaintUnitPowerSource_Type()
)
hdsl2ShdslMaintUnitPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2ShdslMaintUnitPowerSource.setStatus("current")
_Hdsl2ShdslSpanConfProfileTable_Object = MibTable
hdsl2ShdslSpanConfProfileTable = _Hdsl2ShdslSpanConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10)
)
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfProfileTable.setStatus("current")
_Hdsl2ShdslSpanConfProfileEntry_Object = MibTableRow
hdsl2ShdslSpanConfProfileEntry = _Hdsl2ShdslSpanConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1)
)
hdsl2ShdslSpanConfProfileEntry.setIndexNames(
    (1, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfProfileName"),
)
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfProfileEntry.setStatus("current")


class _Hdsl2ShdslSpanConfProfileName_Type(SnmpAdminString):
    """Custom type hdsl2ShdslSpanConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hdsl2ShdslSpanConfProfileName_Type.__name__ = "SnmpAdminString"
_Hdsl2ShdslSpanConfProfileName_Object = MibTableColumn
hdsl2ShdslSpanConfProfileName = _Hdsl2ShdslSpanConfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 1),
    _Hdsl2ShdslSpanConfProfileName_Type()
)
hdsl2ShdslSpanConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfProfileName.setStatus("current")


class _Hdsl2ShdslSpanConfWireInterface_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfWireInterface based on Integer32"""
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
        *(("eightWire", 4),
          ("fourWire", 2),
          ("sixWire", 3),
          ("twoWire", 1))
    )


_Hdsl2ShdslSpanConfWireInterface_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfWireInterface_Object = MibTableColumn
hdsl2ShdslSpanConfWireInterface = _Hdsl2ShdslSpanConfWireInterface_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 2),
    _Hdsl2ShdslSpanConfWireInterface_Type()
)
hdsl2ShdslSpanConfWireInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfWireInterface.setStatus("current")


class _Hdsl2ShdslSpanConfMinLineRate_Type(Unsigned32):
    """Custom type hdsl2ShdslSpanConfMinLineRate based on Unsigned32"""
    defaultValue = 1552000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hdsl2ShdslSpanConfMinLineRate_Type.__name__ = "Unsigned32"
_Hdsl2ShdslSpanConfMinLineRate_Object = MibTableColumn
hdsl2ShdslSpanConfMinLineRate = _Hdsl2ShdslSpanConfMinLineRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 3),
    _Hdsl2ShdslSpanConfMinLineRate_Type()
)
hdsl2ShdslSpanConfMinLineRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfMinLineRate.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfMinLineRate.setUnits("bps")


class _Hdsl2ShdslSpanConfMaxLineRate_Type(Unsigned32):
    """Custom type hdsl2ShdslSpanConfMaxLineRate based on Unsigned32"""
    defaultValue = 1552000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hdsl2ShdslSpanConfMaxLineRate_Type.__name__ = "Unsigned32"
_Hdsl2ShdslSpanConfMaxLineRate_Object = MibTableColumn
hdsl2ShdslSpanConfMaxLineRate = _Hdsl2ShdslSpanConfMaxLineRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 4),
    _Hdsl2ShdslSpanConfMaxLineRate_Type()
)
hdsl2ShdslSpanConfMaxLineRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfMaxLineRate.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfMaxLineRate.setUnits("bps")


class _Hdsl2ShdslSpanConfPSD_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfPSD based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asymmetric", 2),
          ("symmetric", 1))
    )


_Hdsl2ShdslSpanConfPSD_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfPSD_Object = MibTableColumn
hdsl2ShdslSpanConfPSD = _Hdsl2ShdslSpanConfPSD_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 5),
    _Hdsl2ShdslSpanConfPSD_Type()
)
hdsl2ShdslSpanConfPSD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfPSD.setStatus("current")


class _Hdsl2ShdslSpanConfTransmissionMode_Type(Hdsl2ShdslTransmissionModeType):
    """Custom type hdsl2ShdslSpanConfTransmissionMode based on Hdsl2ShdslTransmissionModeType"""
    defaultBinValue = "1"


_Hdsl2ShdslSpanConfTransmissionMode_Object = MibTableColumn
hdsl2ShdslSpanConfTransmissionMode = _Hdsl2ShdslSpanConfTransmissionMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 6),
    _Hdsl2ShdslSpanConfTransmissionMode_Type()
)
hdsl2ShdslSpanConfTransmissionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfTransmissionMode.setStatus("current")


class _Hdsl2ShdslSpanConfRemoteEnabled_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfRemoteEnabled based on Integer32"""
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


_Hdsl2ShdslSpanConfRemoteEnabled_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfRemoteEnabled_Object = MibTableColumn
hdsl2ShdslSpanConfRemoteEnabled = _Hdsl2ShdslSpanConfRemoteEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 7),
    _Hdsl2ShdslSpanConfRemoteEnabled_Type()
)
hdsl2ShdslSpanConfRemoteEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfRemoteEnabled.setStatus("current")


class _Hdsl2ShdslSpanConfPowerFeeding_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfPowerFeeding based on Integer32"""
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
        *(("noPower", 1),
          ("powerFeed", 2),
          ("wettingCurrent", 3))
    )


_Hdsl2ShdslSpanConfPowerFeeding_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfPowerFeeding_Object = MibTableColumn
hdsl2ShdslSpanConfPowerFeeding = _Hdsl2ShdslSpanConfPowerFeeding_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 8),
    _Hdsl2ShdslSpanConfPowerFeeding_Type()
)
hdsl2ShdslSpanConfPowerFeeding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfPowerFeeding.setStatus("current")


class _Hdsl2ShdslSpanConfCurrCondTargetMarginDown_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfCurrCondTargetMarginDown based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 21),
    )


_Hdsl2ShdslSpanConfCurrCondTargetMarginDown_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfCurrCondTargetMarginDown_Object = MibTableColumn
hdsl2ShdslSpanConfCurrCondTargetMarginDown = _Hdsl2ShdslSpanConfCurrCondTargetMarginDown_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 9),
    _Hdsl2ShdslSpanConfCurrCondTargetMarginDown_Type()
)
hdsl2ShdslSpanConfCurrCondTargetMarginDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfCurrCondTargetMarginDown.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfCurrCondTargetMarginDown.setUnits("dB")


class _Hdsl2ShdslSpanConfWorstCaseTargetMarginDown_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfWorstCaseTargetMarginDown based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 21),
    )


_Hdsl2ShdslSpanConfWorstCaseTargetMarginDown_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfWorstCaseTargetMarginDown_Object = MibTableColumn
hdsl2ShdslSpanConfWorstCaseTargetMarginDown = _Hdsl2ShdslSpanConfWorstCaseTargetMarginDown_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 10),
    _Hdsl2ShdslSpanConfWorstCaseTargetMarginDown_Type()
)
hdsl2ShdslSpanConfWorstCaseTargetMarginDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfWorstCaseTargetMarginDown.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfWorstCaseTargetMarginDown.setUnits("dB")


class _Hdsl2ShdslSpanConfCurrCondTargetMarginUp_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfCurrCondTargetMarginUp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 21),
    )


_Hdsl2ShdslSpanConfCurrCondTargetMarginUp_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfCurrCondTargetMarginUp_Object = MibTableColumn
hdsl2ShdslSpanConfCurrCondTargetMarginUp = _Hdsl2ShdslSpanConfCurrCondTargetMarginUp_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 11),
    _Hdsl2ShdslSpanConfCurrCondTargetMarginUp_Type()
)
hdsl2ShdslSpanConfCurrCondTargetMarginUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfCurrCondTargetMarginUp.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfCurrCondTargetMarginUp.setUnits("dB")


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
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 12),
    _Hdsl2ShdslSpanConfWorstCaseTargetMarginUp_Type()
)
hdsl2ShdslSpanConfWorstCaseTargetMarginUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfWorstCaseTargetMarginUp.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfWorstCaseTargetMarginUp.setUnits("dB")


class _Hdsl2ShdslSpanConfUsedTargetMargins_Type(Bits):
    """Custom type hdsl2ShdslSpanConfUsedTargetMargins based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("currCondDown", 0),
          ("currCondUp", 2),
          ("worstCaseDown", 1),
          ("worstCaseUp", 3))
    )

_Hdsl2ShdslSpanConfUsedTargetMargins_Type.__name__ = "Bits"
_Hdsl2ShdslSpanConfUsedTargetMargins_Object = MibTableColumn
hdsl2ShdslSpanConfUsedTargetMargins = _Hdsl2ShdslSpanConfUsedTargetMargins_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 13),
    _Hdsl2ShdslSpanConfUsedTargetMargins_Type()
)
hdsl2ShdslSpanConfUsedTargetMargins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfUsedTargetMargins.setStatus("current")


class _Hdsl2ShdslSpanConfReferenceClock_Type(Hdsl2ShdslClockReferenceType):
    """Custom type hdsl2ShdslSpanConfReferenceClock based on Hdsl2ShdslClockReferenceType"""


_Hdsl2ShdslSpanConfReferenceClock_Object = MibTableColumn
hdsl2ShdslSpanConfReferenceClock = _Hdsl2ShdslSpanConfReferenceClock_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 14),
    _Hdsl2ShdslSpanConfReferenceClock_Type()
)
hdsl2ShdslSpanConfReferenceClock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfReferenceClock.setStatus("current")


class _Hdsl2ShdslSpanConfLineProbeEnable_Type(Integer32):
    """Custom type hdsl2ShdslSpanConfLineProbeEnable based on Integer32"""
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


_Hdsl2ShdslSpanConfLineProbeEnable_Type.__name__ = "Integer32"
_Hdsl2ShdslSpanConfLineProbeEnable_Object = MibTableColumn
hdsl2ShdslSpanConfLineProbeEnable = _Hdsl2ShdslSpanConfLineProbeEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 15),
    _Hdsl2ShdslSpanConfLineProbeEnable_Type()
)
hdsl2ShdslSpanConfLineProbeEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfLineProbeEnable.setStatus("current")
_Hdsl2ShdslSpanConfProfileRowStatus_Type = RowStatus
_Hdsl2ShdslSpanConfProfileRowStatus_Object = MibTableColumn
hdsl2ShdslSpanConfProfileRowStatus = _Hdsl2ShdslSpanConfProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 10, 1, 16),
    _Hdsl2ShdslSpanConfProfileRowStatus_Type()
)
hdsl2ShdslSpanConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfProfileRowStatus.setStatus("current")
_Hdsl2ShdslEndpointAlarmConfProfileTable_Object = MibTable
hdsl2ShdslEndpointAlarmConfProfileTable = _Hdsl2ShdslEndpointAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 11)
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointAlarmConfProfileTable.setStatus("current")
_Hdsl2ShdslEndpointAlarmConfProfileEntry_Object = MibTableRow
hdsl2ShdslEndpointAlarmConfProfileEntry = _Hdsl2ShdslEndpointAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 11, 1)
)
hdsl2ShdslEndpointAlarmConfProfileEntry.setIndexNames(
    (1, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointAlarmConfProfileEntry.setStatus("current")


class _Hdsl2ShdslEndpointAlarmConfProfileName_Type(SnmpAdminString):
    """Custom type hdsl2ShdslEndpointAlarmConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hdsl2ShdslEndpointAlarmConfProfileName_Type.__name__ = "SnmpAdminString"
_Hdsl2ShdslEndpointAlarmConfProfileName_Object = MibTableColumn
hdsl2ShdslEndpointAlarmConfProfileName = _Hdsl2ShdslEndpointAlarmConfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 11, 1, 1),
    _Hdsl2ShdslEndpointAlarmConfProfileName_Type()
)
hdsl2ShdslEndpointAlarmConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointAlarmConfProfileName.setStatus("current")


class _Hdsl2ShdslEndpointThreshLoopAttenuation_Type(Integer32):
    """Custom type hdsl2ShdslEndpointThreshLoopAttenuation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_Hdsl2ShdslEndpointThreshLoopAttenuation_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointThreshLoopAttenuation_Object = MibTableColumn
hdsl2ShdslEndpointThreshLoopAttenuation = _Hdsl2ShdslEndpointThreshLoopAttenuation_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 11, 1, 2),
    _Hdsl2ShdslEndpointThreshLoopAttenuation_Type()
)
hdsl2ShdslEndpointThreshLoopAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshLoopAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshLoopAttenuation.setUnits("dB")


class _Hdsl2ShdslEndpointThreshSNRMargin_Type(Integer32):
    """Custom type hdsl2ShdslEndpointThreshSNRMargin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_Hdsl2ShdslEndpointThreshSNRMargin_Type.__name__ = "Integer32"
_Hdsl2ShdslEndpointThreshSNRMargin_Object = MibTableColumn
hdsl2ShdslEndpointThreshSNRMargin = _Hdsl2ShdslEndpointThreshSNRMargin_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 11, 1, 3),
    _Hdsl2ShdslEndpointThreshSNRMargin_Type()
)
hdsl2ShdslEndpointThreshSNRMargin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshSNRMargin.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshSNRMargin.setUnits("dB")


class _Hdsl2ShdslEndpointThreshES_Type(Hdsl2ShdslPerfIntervalThreshold):
    """Custom type hdsl2ShdslEndpointThreshES based on Hdsl2ShdslPerfIntervalThreshold"""
    defaultValue = 0


_Hdsl2ShdslEndpointThreshES_Object = MibTableColumn
hdsl2ShdslEndpointThreshES = _Hdsl2ShdslEndpointThreshES_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 11, 1, 4),
    _Hdsl2ShdslEndpointThreshES_Type()
)
hdsl2ShdslEndpointThreshES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshES.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshES.setUnits("seconds")


class _Hdsl2ShdslEndpointThreshSES_Type(Hdsl2ShdslPerfIntervalThreshold):
    """Custom type hdsl2ShdslEndpointThreshSES based on Hdsl2ShdslPerfIntervalThreshold"""
    defaultValue = 0


_Hdsl2ShdslEndpointThreshSES_Object = MibTableColumn
hdsl2ShdslEndpointThreshSES = _Hdsl2ShdslEndpointThreshSES_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 11, 1, 5),
    _Hdsl2ShdslEndpointThreshSES_Type()
)
hdsl2ShdslEndpointThreshSES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshSES.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshSES.setUnits("seconds")


class _Hdsl2ShdslEndpointThreshCRCanomalies_Type(Integer32):
    """Custom type hdsl2ShdslEndpointThreshCRCanomalies based on Integer32"""
    defaultValue = 0


_Hdsl2ShdslEndpointThreshCRCanomalies_Object = MibTableColumn
hdsl2ShdslEndpointThreshCRCanomalies = _Hdsl2ShdslEndpointThreshCRCanomalies_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 11, 1, 6),
    _Hdsl2ShdslEndpointThreshCRCanomalies_Type()
)
hdsl2ShdslEndpointThreshCRCanomalies.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshCRCanomalies.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshCRCanomalies.setUnits("detected CRC Anomalies")


class _Hdsl2ShdslEndpointThreshLOSWS_Type(Hdsl2ShdslPerfIntervalThreshold):
    """Custom type hdsl2ShdslEndpointThreshLOSWS based on Hdsl2ShdslPerfIntervalThreshold"""
    defaultValue = 0


_Hdsl2ShdslEndpointThreshLOSWS_Object = MibTableColumn
hdsl2ShdslEndpointThreshLOSWS = _Hdsl2ShdslEndpointThreshLOSWS_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 11, 1, 7),
    _Hdsl2ShdslEndpointThreshLOSWS_Type()
)
hdsl2ShdslEndpointThreshLOSWS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshLOSWS.setUnits("seconds")


class _Hdsl2ShdslEndpointThreshUAS_Type(Hdsl2ShdslPerfIntervalThreshold):
    """Custom type hdsl2ShdslEndpointThreshUAS based on Hdsl2ShdslPerfIntervalThreshold"""
    defaultValue = 0


_Hdsl2ShdslEndpointThreshUAS_Object = MibTableColumn
hdsl2ShdslEndpointThreshUAS = _Hdsl2ShdslEndpointThreshUAS_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 11, 1, 8),
    _Hdsl2ShdslEndpointThreshUAS_Type()
)
hdsl2ShdslEndpointThreshUAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshUAS.setStatus("current")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointThreshUAS.setUnits("seconds")
_Hdsl2ShdslEndpointAlarmConfProfileRowStatus_Type = RowStatus
_Hdsl2ShdslEndpointAlarmConfProfileRowStatus_Object = MibTableColumn
hdsl2ShdslEndpointAlarmConfProfileRowStatus = _Hdsl2ShdslEndpointAlarmConfProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 48, 1, 11, 1, 9),
    _Hdsl2ShdslEndpointAlarmConfProfileRowStatus_Type()
)
hdsl2ShdslEndpointAlarmConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointAlarmConfProfileRowStatus.setStatus("current")
_Hdsl2ShdslConformance_ObjectIdentity = ObjectIdentity
hdsl2ShdslConformance = _Hdsl2ShdslConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 48, 3)
)
_Hdsl2ShdslGroups_ObjectIdentity = ObjectIdentity
hdsl2ShdslGroups = _Hdsl2ShdslGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1)
)
_Hdsl2ShdslCompliances_ObjectIdentity = ObjectIdentity
hdsl2ShdslCompliances = _Hdsl2ShdslCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 2)
)

# Managed Objects groups

hdsl2ShdslSpanConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 1)
)
hdsl2ShdslSpanConfGroup.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfNumRepeaters"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfProfile"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfAlarmProfile"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfGroup.setStatus("current")

hdsl2ShdslSpanStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 2)
)
hdsl2ShdslSpanStatusGroup.setObjects(
    ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslStatusNumAvailRepeaters")
)
if mibBuilder.loadTexts:
    hdsl2ShdslSpanStatusGroup.setStatus("current")

hdsl2ShdslInventoryShdslGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 3)
)
hdsl2ShdslInventoryShdslGroup.setObjects(
    ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvTransmissionModeCapability")
)
if mibBuilder.loadTexts:
    hdsl2ShdslInventoryShdslGroup.setStatus("current")

hdsl2ShdslSpanShdslStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 4)
)
hdsl2ShdslSpanShdslStatusGroup.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslStatusMaxAttainableLineRate"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslStatusActualLineRate"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslStatusTransmissionModeCurrent"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslSpanShdslStatusGroup.setStatus("current")

hdsl2ShdslInventoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 5)
)
hdsl2ShdslInventoryGroup.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvVendorID"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvVendorModelNumber"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvVendorSerialNumber"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvVendorEOCSoftwareVersion"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvStandardVersion"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvVendorListNumber"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvVendorIssueNumber"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvVendorSoftwareVersion"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvEquipmentCode"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvVendorOther"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslInventoryGroup.setStatus("current")

hdsl2ShdslEndpointConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 6)
)
hdsl2ShdslEndpointConfGroup.setObjects(
    ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrAtn")
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointConfGroup.setStatus("current")

hdsl2ShdslEndpointCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 7)
)
hdsl2ShdslEndpointCurrGroup.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrAtn"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrSnrMgn"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrStatus"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointSES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCRCanomalies"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointLOSWS"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointUAS"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr15MinTimeElapsed"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr15MinES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr15MinSES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr15MinCRCanomalies"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr15MinLOSWS"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr15MinUAS"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr1DayTimeElapsed"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr1DayES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr1DaySES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr1DayCRCanomalies"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr1DayLOSWS"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr1DayUAS"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointCurrGroup.setStatus("current")

hdsl2Shdsl15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 8)
)
hdsl2Shdsl15MinIntervalGroup.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2Shdsl15MinIntervalES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2Shdsl15MinIntervalSES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2Shdsl15MinIntervalCRCanomalies"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2Shdsl15MinIntervalLOSWS"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2Shdsl15MinIntervalUAS"))
)
if mibBuilder.loadTexts:
    hdsl2Shdsl15MinIntervalGroup.setStatus("current")

hdsl2Shdsl1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 9)
)
hdsl2Shdsl1DayIntervalGroup.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2Shdsl1DayIntervalMoniSecs"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2Shdsl1DayIntervalES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2Shdsl1DayIntervalSES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2Shdsl1DayIntervalCRCanomalies"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2Shdsl1DayIntervalLOSWS"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2Shdsl1DayIntervalUAS"))
)
if mibBuilder.loadTexts:
    hdsl2Shdsl1DayIntervalGroup.setStatus("current")

hdsl2ShdslMaintenanceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 10)
)
hdsl2ShdslMaintenanceGroup.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslMaintLoopbackConfig"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslMaintTipRingReversal"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslMaintPowerBackOff"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslMaintSoftRestart"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslMaintLoopbackTimeout"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslMaintUnitPowerSource"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslMaintenanceGroup.setStatus("current")

hdsl2ShdslEndpointAlarmConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 11)
)
hdsl2ShdslEndpointAlarmConfGroup.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointAlarmConfProfile"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshLoopAttenuation"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshSNRMargin"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshSES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshCRCanomalies"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshLOSWS"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshUAS"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointAlarmConfProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslEndpointAlarmConfGroup.setStatus("current")

hdsl2ShdslSpanConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 13)
)
hdsl2ShdslSpanConfProfileGroup.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfWireInterface"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfMinLineRate"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfMaxLineRate"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfPSD"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfTransmissionMode"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfRemoteEnabled"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfPowerFeeding"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfCurrCondTargetMarginDown"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfWorstCaseTargetMarginDown"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfCurrCondTargetMarginUp"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfWorstCaseTargetMarginUp"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfUsedTargetMargins"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfReferenceClock"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfLineProbeEnable"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslSpanConfProfileGroup.setStatus("current")

hdsl2ShdslWirePairGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 14)
)
hdsl2ShdslWirePairGroup.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrTipRingReversal"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrActivationState"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslWirePairGroup.setStatus("current")

hdsl2ShdslPayloadRateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 15)
)
hdsl2ShdslPayloadRateGroup.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslStatusMaxAttainablePayloadRate"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslStatusActualPayloadRate"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslPayloadRateGroup.setStatus("current")


# Notification objects

hdsl2ShdslLoopAttenCrossing = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 1)
)
hdsl2ShdslLoopAttenCrossing.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrAtn"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshLoopAttenuation"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslLoopAttenCrossing.setStatus(
        "current"
    )

hdsl2ShdslSNRMarginCrossing = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 2)
)
hdsl2ShdslSNRMarginCrossing.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrSnrMgn"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshSNRMargin"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslSNRMarginCrossing.setStatus(
        "current"
    )

hdsl2ShdslPerfESThresh = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 3)
)
hdsl2ShdslPerfESThresh.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr15MinES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshES"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslPerfESThresh.setStatus(
        "current"
    )

hdsl2ShdslPerfSESThresh = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 4)
)
hdsl2ShdslPerfSESThresh.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr15MinSES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshSES"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslPerfSESThresh.setStatus(
        "current"
    )

hdsl2ShdslPerfCRCanomaliesThresh = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 5)
)
hdsl2ShdslPerfCRCanomaliesThresh.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr15MinCRCanomalies"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshCRCanomalies"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslPerfCRCanomaliesThresh.setStatus(
        "current"
    )

hdsl2ShdslPerfLOSWSThresh = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 6)
)
hdsl2ShdslPerfLOSWSThresh.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr15MinLOSWS"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshLOSWS"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslPerfLOSWSThresh.setStatus(
        "current"
    )

hdsl2ShdslPerfUASThresh = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 7)
)
hdsl2ShdslPerfUASThresh.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurr15MinUAS"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshUAS"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslPerfUASThresh.setStatus(
        "current"
    )

hdsl2ShdslSpanInvalidNumRepeaters = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 8)
)
hdsl2ShdslSpanInvalidNumRepeaters.setObjects(
    ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfNumRepeaters")
)
if mibBuilder.loadTexts:
    hdsl2ShdslSpanInvalidNumRepeaters.setStatus(
        "current"
    )

hdsl2ShdslLoopbackFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 9)
)
hdsl2ShdslLoopbackFailure.setObjects(
    ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslMaintLoopbackConfig")
)
if mibBuilder.loadTexts:
    hdsl2ShdslLoopbackFailure.setStatus(
        "current"
    )

hdsl2ShdslpowerBackoff = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 10)
)
hdsl2ShdslpowerBackoff.setObjects(
    ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrStatus")
)
if mibBuilder.loadTexts:
    hdsl2ShdslpowerBackoff.setStatus(
        "current"
    )

hdsl2ShdsldeviceFault = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 11)
)
hdsl2ShdsldeviceFault.setObjects(
    ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrStatus")
)
if mibBuilder.loadTexts:
    hdsl2ShdsldeviceFault.setStatus(
        "current"
    )

hdsl2ShdsldcContinuityFault = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 12)
)
hdsl2ShdsldcContinuityFault.setObjects(
    ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrStatus")
)
if mibBuilder.loadTexts:
    hdsl2ShdsldcContinuityFault.setStatus(
        "current"
    )

hdsl2ShdslconfigInitFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 13)
)
hdsl2ShdslconfigInitFailure.setObjects(
    ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrStatus")
)
if mibBuilder.loadTexts:
    hdsl2ShdslconfigInitFailure.setStatus(
        "current"
    )

hdsl2ShdslprotocolInitFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 14)
)
hdsl2ShdslprotocolInitFailure.setObjects(
    ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrStatus")
)
if mibBuilder.loadTexts:
    hdsl2ShdslprotocolInitFailure.setStatus(
        "current"
    )

hdsl2ShdslnoNeighborPresent = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 15)
)
hdsl2ShdslnoNeighborPresent.setObjects(
    ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointCurrStatus")
)
if mibBuilder.loadTexts:
    hdsl2ShdslnoNeighborPresent.setStatus(
        "current"
    )

hdsl2ShdslLocalPowerLoss = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 48, 0, 16)
)
hdsl2ShdslLocalPowerLoss.setObjects(
    ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvVendorID")
)
if mibBuilder.loadTexts:
    hdsl2ShdslLocalPowerLoss.setStatus(
        "current"
    )


# Notifications groups

hdsl2ShdslNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 1, 12)
)
hdsl2ShdslNotificationGroup.setObjects(
      *(("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslLoopAttenCrossing"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSNRMarginCrossing"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslPerfESThresh"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslPerfSESThresh"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslPerfCRCanomaliesThresh"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslPerfLOSWSThresh"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslPerfUASThresh"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanInvalidNumRepeaters"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslLoopbackFailure"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslpowerBackoff"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdsldeviceFault"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdsldcContinuityFault"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslconfigInitFailure"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslprotocolInitFailure"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslnoNeighborPresent"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslLocalPowerLoss"))
)
if mibBuilder.loadTexts:
    hdsl2ShdslNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hdsl2ShdslLineMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hdsl2ShdslLineMibCompliance.setStatus(
        "deprecated"
    )

hdsl2GshdslbisLineMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 48, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hdsl2GshdslbisLineMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDSL2-SHDSL-LINE-MIB",
    **{"Hdsl2ShdslPerfCurrDayCount": Hdsl2ShdslPerfCurrDayCount,
       "Hdsl2Shdsl1DayIntervalCount": Hdsl2Shdsl1DayIntervalCount,
       "Hdsl2ShdslPerfTimeElapsed": Hdsl2ShdslPerfTimeElapsed,
       "Hdsl2ShdslPerfIntervalThreshold": Hdsl2ShdslPerfIntervalThreshold,
       "Hdsl2ShdslUnitId": Hdsl2ShdslUnitId,
       "Hdsl2ShdslUnitSide": Hdsl2ShdslUnitSide,
       "Hdsl2ShdslWirePair": Hdsl2ShdslWirePair,
       "Hdsl2ShdslTransmissionModeType": Hdsl2ShdslTransmissionModeType,
       "Hdsl2ShdslClockReferenceType": Hdsl2ShdslClockReferenceType,
       "hdsl2ShdslMIB": hdsl2ShdslMIB,
       "hdsl2ShdslNotifications": hdsl2ShdslNotifications,
       "hdsl2ShdslLoopAttenCrossing": hdsl2ShdslLoopAttenCrossing,
       "hdsl2ShdslSNRMarginCrossing": hdsl2ShdslSNRMarginCrossing,
       "hdsl2ShdslPerfESThresh": hdsl2ShdslPerfESThresh,
       "hdsl2ShdslPerfSESThresh": hdsl2ShdslPerfSESThresh,
       "hdsl2ShdslPerfCRCanomaliesThresh": hdsl2ShdslPerfCRCanomaliesThresh,
       "hdsl2ShdslPerfLOSWSThresh": hdsl2ShdslPerfLOSWSThresh,
       "hdsl2ShdslPerfUASThresh": hdsl2ShdslPerfUASThresh,
       "hdsl2ShdslSpanInvalidNumRepeaters": hdsl2ShdslSpanInvalidNumRepeaters,
       "hdsl2ShdslLoopbackFailure": hdsl2ShdslLoopbackFailure,
       "hdsl2ShdslpowerBackoff": hdsl2ShdslpowerBackoff,
       "hdsl2ShdsldeviceFault": hdsl2ShdsldeviceFault,
       "hdsl2ShdsldcContinuityFault": hdsl2ShdsldcContinuityFault,
       "hdsl2ShdslconfigInitFailure": hdsl2ShdslconfigInitFailure,
       "hdsl2ShdslprotocolInitFailure": hdsl2ShdslprotocolInitFailure,
       "hdsl2ShdslnoNeighborPresent": hdsl2ShdslnoNeighborPresent,
       "hdsl2ShdslLocalPowerLoss": hdsl2ShdslLocalPowerLoss,
       "hdsl2ShdslMibObjects": hdsl2ShdslMibObjects,
       "hdsl2ShdslSpanConfTable": hdsl2ShdslSpanConfTable,
       "hdsl2ShdslSpanConfEntry": hdsl2ShdslSpanConfEntry,
       "hdsl2ShdslSpanConfNumRepeaters": hdsl2ShdslSpanConfNumRepeaters,
       "hdsl2ShdslSpanConfProfile": hdsl2ShdslSpanConfProfile,
       "hdsl2ShdslSpanConfAlarmProfile": hdsl2ShdslSpanConfAlarmProfile,
       "hdsl2ShdslSpanStatusTable": hdsl2ShdslSpanStatusTable,
       "hdsl2ShdslSpanStatusEntry": hdsl2ShdslSpanStatusEntry,
       "hdsl2ShdslStatusNumAvailRepeaters": hdsl2ShdslStatusNumAvailRepeaters,
       "hdsl2ShdslStatusMaxAttainableLineRate": hdsl2ShdslStatusMaxAttainableLineRate,
       "hdsl2ShdslStatusActualLineRate": hdsl2ShdslStatusActualLineRate,
       "hdsl2ShdslStatusTransmissionModeCurrent": hdsl2ShdslStatusTransmissionModeCurrent,
       "hdsl2ShdslStatusMaxAttainablePayloadRate": hdsl2ShdslStatusMaxAttainablePayloadRate,
       "hdsl2ShdslStatusActualPayloadRate": hdsl2ShdslStatusActualPayloadRate,
       "hdsl2ShdslInventoryTable": hdsl2ShdslInventoryTable,
       "hdsl2ShdslInventoryEntry": hdsl2ShdslInventoryEntry,
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
       "hdsl2ShdslEndpointSide": hdsl2ShdslEndpointSide,
       "hdsl2ShdslEndpointWirePair": hdsl2ShdslEndpointWirePair,
       "hdsl2ShdslEndpointAlarmConfProfile": hdsl2ShdslEndpointAlarmConfProfile,
       "hdsl2ShdslEndpointCurrTable": hdsl2ShdslEndpointCurrTable,
       "hdsl2ShdslEndpointCurrEntry": hdsl2ShdslEndpointCurrEntry,
       "hdsl2ShdslEndpointCurrAtn": hdsl2ShdslEndpointCurrAtn,
       "hdsl2ShdslEndpointCurrSnrMgn": hdsl2ShdslEndpointCurrSnrMgn,
       "hdsl2ShdslEndpointCurrStatus": hdsl2ShdslEndpointCurrStatus,
       "hdsl2ShdslEndpointES": hdsl2ShdslEndpointES,
       "hdsl2ShdslEndpointSES": hdsl2ShdslEndpointSES,
       "hdsl2ShdslEndpointCRCanomalies": hdsl2ShdslEndpointCRCanomalies,
       "hdsl2ShdslEndpointLOSWS": hdsl2ShdslEndpointLOSWS,
       "hdsl2ShdslEndpointUAS": hdsl2ShdslEndpointUAS,
       "hdsl2ShdslEndpointCurr15MinTimeElapsed": hdsl2ShdslEndpointCurr15MinTimeElapsed,
       "hdsl2ShdslEndpointCurr15MinES": hdsl2ShdslEndpointCurr15MinES,
       "hdsl2ShdslEndpointCurr15MinSES": hdsl2ShdslEndpointCurr15MinSES,
       "hdsl2ShdslEndpointCurr15MinCRCanomalies": hdsl2ShdslEndpointCurr15MinCRCanomalies,
       "hdsl2ShdslEndpointCurr15MinLOSWS": hdsl2ShdslEndpointCurr15MinLOSWS,
       "hdsl2ShdslEndpointCurr15MinUAS": hdsl2ShdslEndpointCurr15MinUAS,
       "hdsl2ShdslEndpointCurr1DayTimeElapsed": hdsl2ShdslEndpointCurr1DayTimeElapsed,
       "hdsl2ShdslEndpointCurr1DayES": hdsl2ShdslEndpointCurr1DayES,
       "hdsl2ShdslEndpointCurr1DaySES": hdsl2ShdslEndpointCurr1DaySES,
       "hdsl2ShdslEndpointCurr1DayCRCanomalies": hdsl2ShdslEndpointCurr1DayCRCanomalies,
       "hdsl2ShdslEndpointCurr1DayLOSWS": hdsl2ShdslEndpointCurr1DayLOSWS,
       "hdsl2ShdslEndpointCurr1DayUAS": hdsl2ShdslEndpointCurr1DayUAS,
       "hdsl2ShdslEndpointCurrTipRingReversal": hdsl2ShdslEndpointCurrTipRingReversal,
       "hdsl2ShdslEndpointCurrActivationState": hdsl2ShdslEndpointCurrActivationState,
       "hdsl2Shdsl15MinIntervalTable": hdsl2Shdsl15MinIntervalTable,
       "hdsl2Shdsl15MinIntervalEntry": hdsl2Shdsl15MinIntervalEntry,
       "hdsl2Shdsl15MinIntervalNumber": hdsl2Shdsl15MinIntervalNumber,
       "hdsl2Shdsl15MinIntervalES": hdsl2Shdsl15MinIntervalES,
       "hdsl2Shdsl15MinIntervalSES": hdsl2Shdsl15MinIntervalSES,
       "hdsl2Shdsl15MinIntervalCRCanomalies": hdsl2Shdsl15MinIntervalCRCanomalies,
       "hdsl2Shdsl15MinIntervalLOSWS": hdsl2Shdsl15MinIntervalLOSWS,
       "hdsl2Shdsl15MinIntervalUAS": hdsl2Shdsl15MinIntervalUAS,
       "hdsl2Shdsl1DayIntervalTable": hdsl2Shdsl1DayIntervalTable,
       "hdsl2Shdsl1DayIntervalEntry": hdsl2Shdsl1DayIntervalEntry,
       "hdsl2Shdsl1DayIntervalNumber": hdsl2Shdsl1DayIntervalNumber,
       "hdsl2Shdsl1DayIntervalMoniSecs": hdsl2Shdsl1DayIntervalMoniSecs,
       "hdsl2Shdsl1DayIntervalES": hdsl2Shdsl1DayIntervalES,
       "hdsl2Shdsl1DayIntervalSES": hdsl2Shdsl1DayIntervalSES,
       "hdsl2Shdsl1DayIntervalCRCanomalies": hdsl2Shdsl1DayIntervalCRCanomalies,
       "hdsl2Shdsl1DayIntervalLOSWS": hdsl2Shdsl1DayIntervalLOSWS,
       "hdsl2Shdsl1DayIntervalUAS": hdsl2Shdsl1DayIntervalUAS,
       "hdsl2ShdslEndpointMaintTable": hdsl2ShdslEndpointMaintTable,
       "hdsl2ShdslEndpointMaintEntry": hdsl2ShdslEndpointMaintEntry,
       "hdsl2ShdslMaintLoopbackConfig": hdsl2ShdslMaintLoopbackConfig,
       "hdsl2ShdslMaintTipRingReversal": hdsl2ShdslMaintTipRingReversal,
       "hdsl2ShdslMaintPowerBackOff": hdsl2ShdslMaintPowerBackOff,
       "hdsl2ShdslMaintSoftRestart": hdsl2ShdslMaintSoftRestart,
       "hdsl2ShdslUnitMaintTable": hdsl2ShdslUnitMaintTable,
       "hdsl2ShdslUnitMaintEntry": hdsl2ShdslUnitMaintEntry,
       "hdsl2ShdslMaintLoopbackTimeout": hdsl2ShdslMaintLoopbackTimeout,
       "hdsl2ShdslMaintUnitPowerSource": hdsl2ShdslMaintUnitPowerSource,
       "hdsl2ShdslSpanConfProfileTable": hdsl2ShdslSpanConfProfileTable,
       "hdsl2ShdslSpanConfProfileEntry": hdsl2ShdslSpanConfProfileEntry,
       "hdsl2ShdslSpanConfProfileName": hdsl2ShdslSpanConfProfileName,
       "hdsl2ShdslSpanConfWireInterface": hdsl2ShdslSpanConfWireInterface,
       "hdsl2ShdslSpanConfMinLineRate": hdsl2ShdslSpanConfMinLineRate,
       "hdsl2ShdslSpanConfMaxLineRate": hdsl2ShdslSpanConfMaxLineRate,
       "hdsl2ShdslSpanConfPSD": hdsl2ShdslSpanConfPSD,
       "hdsl2ShdslSpanConfTransmissionMode": hdsl2ShdslSpanConfTransmissionMode,
       "hdsl2ShdslSpanConfRemoteEnabled": hdsl2ShdslSpanConfRemoteEnabled,
       "hdsl2ShdslSpanConfPowerFeeding": hdsl2ShdslSpanConfPowerFeeding,
       "hdsl2ShdslSpanConfCurrCondTargetMarginDown": hdsl2ShdslSpanConfCurrCondTargetMarginDown,
       "hdsl2ShdslSpanConfWorstCaseTargetMarginDown": hdsl2ShdslSpanConfWorstCaseTargetMarginDown,
       "hdsl2ShdslSpanConfCurrCondTargetMarginUp": hdsl2ShdslSpanConfCurrCondTargetMarginUp,
       "hdsl2ShdslSpanConfWorstCaseTargetMarginUp": hdsl2ShdslSpanConfWorstCaseTargetMarginUp,
       "hdsl2ShdslSpanConfUsedTargetMargins": hdsl2ShdslSpanConfUsedTargetMargins,
       "hdsl2ShdslSpanConfReferenceClock": hdsl2ShdslSpanConfReferenceClock,
       "hdsl2ShdslSpanConfLineProbeEnable": hdsl2ShdslSpanConfLineProbeEnable,
       "hdsl2ShdslSpanConfProfileRowStatus": hdsl2ShdslSpanConfProfileRowStatus,
       "hdsl2ShdslEndpointAlarmConfProfileTable": hdsl2ShdslEndpointAlarmConfProfileTable,
       "hdsl2ShdslEndpointAlarmConfProfileEntry": hdsl2ShdslEndpointAlarmConfProfileEntry,
       "hdsl2ShdslEndpointAlarmConfProfileName": hdsl2ShdslEndpointAlarmConfProfileName,
       "hdsl2ShdslEndpointThreshLoopAttenuation": hdsl2ShdslEndpointThreshLoopAttenuation,
       "hdsl2ShdslEndpointThreshSNRMargin": hdsl2ShdslEndpointThreshSNRMargin,
       "hdsl2ShdslEndpointThreshES": hdsl2ShdslEndpointThreshES,
       "hdsl2ShdslEndpointThreshSES": hdsl2ShdslEndpointThreshSES,
       "hdsl2ShdslEndpointThreshCRCanomalies": hdsl2ShdslEndpointThreshCRCanomalies,
       "hdsl2ShdslEndpointThreshLOSWS": hdsl2ShdslEndpointThreshLOSWS,
       "hdsl2ShdslEndpointThreshUAS": hdsl2ShdslEndpointThreshUAS,
       "hdsl2ShdslEndpointAlarmConfProfileRowStatus": hdsl2ShdslEndpointAlarmConfProfileRowStatus,
       "hdsl2ShdslConformance": hdsl2ShdslConformance,
       "hdsl2ShdslGroups": hdsl2ShdslGroups,
       "hdsl2ShdslSpanConfGroup": hdsl2ShdslSpanConfGroup,
       "hdsl2ShdslSpanStatusGroup": hdsl2ShdslSpanStatusGroup,
       "hdsl2ShdslInventoryShdslGroup": hdsl2ShdslInventoryShdslGroup,
       "hdsl2ShdslSpanShdslStatusGroup": hdsl2ShdslSpanShdslStatusGroup,
       "hdsl2ShdslInventoryGroup": hdsl2ShdslInventoryGroup,
       "hdsl2ShdslEndpointConfGroup": hdsl2ShdslEndpointConfGroup,
       "hdsl2ShdslEndpointCurrGroup": hdsl2ShdslEndpointCurrGroup,
       "hdsl2Shdsl15MinIntervalGroup": hdsl2Shdsl15MinIntervalGroup,
       "hdsl2Shdsl1DayIntervalGroup": hdsl2Shdsl1DayIntervalGroup,
       "hdsl2ShdslMaintenanceGroup": hdsl2ShdslMaintenanceGroup,
       "hdsl2ShdslEndpointAlarmConfGroup": hdsl2ShdslEndpointAlarmConfGroup,
       "hdsl2ShdslNotificationGroup": hdsl2ShdslNotificationGroup,
       "hdsl2ShdslSpanConfProfileGroup": hdsl2ShdslSpanConfProfileGroup,
       "hdsl2ShdslWirePairGroup": hdsl2ShdslWirePairGroup,
       "hdsl2ShdslPayloadRateGroup": hdsl2ShdslPayloadRateGroup,
       "hdsl2ShdslCompliances": hdsl2ShdslCompliances,
       "hdsl2ShdslLineMibCompliance": hdsl2ShdslLineMibCompliance,
       "hdsl2GshdslbisLineMibCompliance": hdsl2GshdslbisLineMibCompliance}
)
