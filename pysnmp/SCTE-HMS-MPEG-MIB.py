# SNMP MIB module (SCTE-HMS-MPEG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCTE-HMS-MPEG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:50 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(HePIDValue,
 ProgDataType) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-TC-MIB",
    "HePIDValue",
    "ProgDataType")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(AutonomousType,
 DateAndTime,
 DisplayString,
 RowPointer,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

heMpegCommonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1)
)
heMpegCommonMIB.setRevisions(
        ("2008-10-03 17:00",
         "2008-10-03 06:49",
         "2008-10-03 01:35",
         "2008-10-03 00:00",
         "2008-02-04 17:00",
         "2007-12-17 17:00",
         "2007-10-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpegMIBObjects_ObjectIdentity = ObjectIdentity
mpegMIBObjects = _MpegMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    mpegMIBObjects.setStatus("current")
_MpegDigitalInputs_ObjectIdentity = ObjectIdentity
mpegDigitalInputs = _MpegDigitalInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpegDigitalInputs.setStatus("current")
_MpegLossOfSignalTimeout_Type = Unsigned32
_MpegLossOfSignalTimeout_Object = MibScalar
mpegLossOfSignalTimeout = _MpegLossOfSignalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 1),
    _MpegLossOfSignalTimeout_Type()
)
mpegLossOfSignalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpegLossOfSignalTimeout.setStatus("current")
if mibBuilder.loadTexts:
    mpegLossOfSignalTimeout.setUnits("milliseconds")
_MpegInputTSTable_Object = MibTable
mpegInputTSTable = _MpegInputTSTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mpegInputTSTable.setStatus("current")
_MpegInputTSEntry_Object = MibTableRow
mpegInputTSEntry = _MpegInputTSEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1)
)
mpegInputTSEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegInputTSIndex"),
)
if mibBuilder.loadTexts:
    mpegInputTSEntry.setStatus("current")
_MpegInputTSIndex_Type = Unsigned32
_MpegInputTSIndex_Object = MibTableColumn
mpegInputTSIndex = _MpegInputTSIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 1),
    _MpegInputTSIndex_Type()
)
mpegInputTSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegInputTSIndex.setStatus("current")


class _MpegInputTSType_Type(Integer32):
    """Custom type mpegInputTSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mpts", 2),
          ("spts", 1))
    )


_MpegInputTSType_Type.__name__ = "Integer32"
_MpegInputTSType_Object = MibTableColumn
mpegInputTSType = _MpegInputTSType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 2),
    _MpegInputTSType_Type()
)
mpegInputTSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSType.setStatus("current")


class _MpegInputTSConnectionType_Type(Integer32):
    """Custom type mpegInputTSConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("udp", 2))
    )


_MpegInputTSConnectionType_Type.__name__ = "Integer32"
_MpegInputTSConnectionType_Object = MibTableColumn
mpegInputTSConnectionType = _MpegInputTSConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 3),
    _MpegInputTSConnectionType_Type()
)
mpegInputTSConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSConnectionType.setStatus("current")
_MpegInputTSConnection_Type = RowPointer
_MpegInputTSConnection_Object = MibTableColumn
mpegInputTSConnection = _MpegInputTSConnection_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 4),
    _MpegInputTSConnection_Type()
)
mpegInputTSConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSConnection.setStatus("current")
_MpegInputTSActiveConnection_Type = RowPointer
_MpegInputTSActiveConnection_Object = MibTableColumn
mpegInputTSActiveConnection = _MpegInputTSActiveConnection_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 5),
    _MpegInputTSActiveConnection_Type()
)
mpegInputTSActiveConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSActiveConnection.setStatus("current")
_MpegInputTSPsiDetected_Type = TruthValue
_MpegInputTSPsiDetected_Object = MibTableColumn
mpegInputTSPsiDetected = _MpegInputTSPsiDetected_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 6),
    _MpegInputTSPsiDetected_Type()
)
mpegInputTSPsiDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSPsiDetected.setStatus("current")
_MpegInputTSStartTime_Type = DateAndTime
_MpegInputTSStartTime_Object = MibTableColumn
mpegInputTSStartTime = _MpegInputTSStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 7),
    _MpegInputTSStartTime_Type()
)
mpegInputTSStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSStartTime.setStatus("current")
_MpegInputTSResourceAllocated_Type = TruthValue
_MpegInputTSResourceAllocated_Object = MibTableColumn
mpegInputTSResourceAllocated = _MpegInputTSResourceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 8),
    _MpegInputTSResourceAllocated_Type()
)
mpegInputTSResourceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSResourceAllocated.setStatus("current")
_MpegInputTSNumPrograms_Type = Unsigned32
_MpegInputTSNumPrograms_Object = MibTableColumn
mpegInputTSNumPrograms = _MpegInputTSNumPrograms_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 9),
    _MpegInputTSNumPrograms_Type()
)
mpegInputTSNumPrograms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSNumPrograms.setStatus("current")
_MpegInputTSRate_Type = Unsigned32
_MpegInputTSRate_Object = MibTableColumn
mpegInputTSRate = _MpegInputTSRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 10),
    _MpegInputTSRate_Type()
)
mpegInputTSRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSRate.setStatus("current")
_MpegInputTSMaxRate_Type = Unsigned32
_MpegInputTSMaxRate_Object = MibTableColumn
mpegInputTSMaxRate = _MpegInputTSMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 11),
    _MpegInputTSMaxRate_Type()
)
mpegInputTSMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSMaxRate.setStatus("current")


class _MpegInputTSPatVersion_Type(Integer32):
    """Custom type mpegInputTSPatVersion based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31),
    )


_MpegInputTSPatVersion_Type.__name__ = "Integer32"
_MpegInputTSPatVersion_Object = MibTableColumn
mpegInputTSPatVersion = _MpegInputTSPatVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 12),
    _MpegInputTSPatVersion_Type()
)
mpegInputTSPatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSPatVersion.setStatus("current")


class _MpegInputTSCatVersion_Type(Integer32):
    """Custom type mpegInputTSCatVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31),
    )


_MpegInputTSCatVersion_Type.__name__ = "Integer32"
_MpegInputTSCatVersion_Object = MibTableColumn
mpegInputTSCatVersion = _MpegInputTSCatVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 13),
    _MpegInputTSCatVersion_Type()
)
mpegInputTSCatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSCatVersion.setStatus("current")
_MpegInputTSNitPid_Type = HePIDValue
_MpegInputTSNitPid_Object = MibTableColumn
mpegInputTSNitPid = _MpegInputTSNitPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 14),
    _MpegInputTSNitPid_Type()
)
mpegInputTSNitPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSNitPid.setStatus("current")


class _MpegInputTSNumEmms_Type(Unsigned32):
    """Custom type mpegInputTSNumEmms based on Unsigned32"""
    defaultValue = 9999


_MpegInputTSNumEmms_Object = MibTableColumn
mpegInputTSNumEmms = _MpegInputTSNumEmms_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 15),
    _MpegInputTSNumEmms_Type()
)
mpegInputTSNumEmms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSNumEmms.setStatus("current")
_MpegInputTSTSID_Type = Unsigned32
_MpegInputTSTSID_Object = MibTableColumn
mpegInputTSTSID = _MpegInputTSTSID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 16),
    _MpegInputTSTSID_Type()
)
mpegInputTSTSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSTSID.setStatus("current")


class _MpegInputTSLock_Type(Integer32):
    """Custom type mpegInputTSLock based on Integer32"""
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
        *(("intermittent", 3),
          ("locked", 1),
          ("notLocked", 2),
          ("notMonitored", 4))
    )


_MpegInputTSLock_Type.__name__ = "Integer32"
_MpegInputTSLock_Object = MibTableColumn
mpegInputTSLock = _MpegInputTSLock_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 2, 1, 17),
    _MpegInputTSLock_Type()
)
mpegInputTSLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSLock.setStatus("current")
_MpegInputProgTable_Object = MibTable
mpegInputProgTable = _MpegInputProgTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mpegInputProgTable.setStatus("current")
_MpegInputProgEntry_Object = MibTableRow
mpegInputProgEntry = _MpegInputProgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 3, 1)
)
mpegInputProgEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegInputTSIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegInputProgIndex"),
)
if mibBuilder.loadTexts:
    mpegInputProgEntry.setStatus("current")
_MpegInputProgIndex_Type = Unsigned32
_MpegInputProgIndex_Object = MibTableColumn
mpegInputProgIndex = _MpegInputProgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 3, 1, 1),
    _MpegInputProgIndex_Type()
)
mpegInputProgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegInputProgIndex.setStatus("current")
_MpegInputProgNo_Type = Unsigned32
_MpegInputProgNo_Object = MibTableColumn
mpegInputProgNo = _MpegInputProgNo_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 3, 1, 2),
    _MpegInputProgNo_Type()
)
mpegInputProgNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputProgNo.setStatus("current")


class _MpegInputProgPmtVersion_Type(Unsigned32):
    """Custom type mpegInputProgPmtVersion based on Unsigned32"""
    defaultValue = 0


_MpegInputProgPmtVersion_Object = MibTableColumn
mpegInputProgPmtVersion = _MpegInputProgPmtVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 3, 1, 3),
    _MpegInputProgPmtVersion_Type()
)
mpegInputProgPmtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputProgPmtVersion.setStatus("current")
_MpegInputProgPmtPid_Type = HePIDValue
_MpegInputProgPmtPid_Object = MibTableColumn
mpegInputProgPmtPid = _MpegInputProgPmtPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 3, 1, 4),
    _MpegInputProgPmtPid_Type()
)
mpegInputProgPmtPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputProgPmtPid.setStatus("current")
_MpegInputProgPcrPid_Type = HePIDValue
_MpegInputProgPcrPid_Object = MibTableColumn
mpegInputProgPcrPid = _MpegInputProgPcrPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 3, 1, 5),
    _MpegInputProgPcrPid_Type()
)
mpegInputProgPcrPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputProgPcrPid.setStatus("current")
_MpegInputProgEcmPid_Type = HePIDValue
_MpegInputProgEcmPid_Object = MibTableColumn
mpegInputProgEcmPid = _MpegInputProgEcmPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 3, 1, 6),
    _MpegInputProgEcmPid_Type()
)
mpegInputProgEcmPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputProgEcmPid.setStatus("current")
_MpegInputProgNumElems_Type = Unsigned32
_MpegInputProgNumElems_Object = MibTableColumn
mpegInputProgNumElems = _MpegInputProgNumElems_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 3, 1, 7),
    _MpegInputProgNumElems_Type()
)
mpegInputProgNumElems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputProgNumElems.setStatus("current")


class _MpegInputProgNumEcms_Type(Unsigned32):
    """Custom type mpegInputProgNumEcms based on Unsigned32"""
    defaultValue = 9999


_MpegInputProgNumEcms_Object = MibTableColumn
mpegInputProgNumEcms = _MpegInputProgNumEcms_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 3, 1, 8),
    _MpegInputProgNumEcms_Type()
)
mpegInputProgNumEcms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputProgNumEcms.setStatus("current")


class _MpegInputProgCaDescr_Type(OctetString):
    """Custom type mpegInputProgCaDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MpegInputProgCaDescr_Type.__name__ = "OctetString"
_MpegInputProgCaDescr_Object = MibTableColumn
mpegInputProgCaDescr = _MpegInputProgCaDescr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 3, 1, 9),
    _MpegInputProgCaDescr_Type()
)
mpegInputProgCaDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputProgCaDescr.setStatus("current")


class _MpegInputProgScte35Descr_Type(OctetString):
    """Custom type mpegInputProgScte35Descr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MpegInputProgScte35Descr_Type.__name__ = "OctetString"
_MpegInputProgScte35Descr_Object = MibTableColumn
mpegInputProgScte35Descr = _MpegInputProgScte35Descr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 3, 1, 10),
    _MpegInputProgScte35Descr_Type()
)
mpegInputProgScte35Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputProgScte35Descr.setStatus("current")


class _MpegInputProgScte18Descr_Type(OctetString):
    """Custom type mpegInputProgScte18Descr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MpegInputProgScte18Descr_Type.__name__ = "OctetString"
_MpegInputProgScte18Descr_Object = MibTableColumn
mpegInputProgScte18Descr = _MpegInputProgScte18Descr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 3, 1, 11),
    _MpegInputProgScte18Descr_Type()
)
mpegInputProgScte18Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputProgScte18Descr.setStatus("current")
_MpegProgESTable_Object = MibTable
mpegProgESTable = _MpegProgESTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mpegProgESTable.setStatus("current")
_MpegProgESEntry_Object = MibTableRow
mpegProgESEntry = _MpegProgESEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 4, 1)
)
mpegProgESEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegInputTSIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegInputProgIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegProgESIndex"),
)
if mibBuilder.loadTexts:
    mpegProgESEntry.setStatus("current")
_MpegProgESIndex_Type = Unsigned32
_MpegProgESIndex_Object = MibTableColumn
mpegProgESIndex = _MpegProgESIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 4, 1, 1),
    _MpegProgESIndex_Type()
)
mpegProgESIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegProgESIndex.setStatus("current")
_MpegProgESPID_Type = Integer32
_MpegProgESPID_Object = MibTableColumn
mpegProgESPID = _MpegProgESPID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 4, 1, 2),
    _MpegProgESPID_Type()
)
mpegProgESPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegProgESPID.setStatus("current")
_MpegProgESType_Type = ProgDataType
_MpegProgESType_Object = MibTableColumn
mpegProgESType = _MpegProgESType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 4, 1, 3),
    _MpegProgESType_Type()
)
mpegProgESType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegProgESType.setStatus("current")


class _MpegProgESCaDescr_Type(OctetString):
    """Custom type mpegProgESCaDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MpegProgESCaDescr_Type.__name__ = "OctetString"
_MpegProgESCaDescr_Object = MibTableColumn
mpegProgESCaDescr = _MpegProgESCaDescr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 4, 1, 4),
    _MpegProgESCaDescr_Type()
)
mpegProgESCaDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegProgESCaDescr.setStatus("current")


class _MpegProgESScte35Descr_Type(OctetString):
    """Custom type mpegProgESScte35Descr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MpegProgESScte35Descr_Type.__name__ = "OctetString"
_MpegProgESScte35Descr_Object = MibTableColumn
mpegProgESScte35Descr = _MpegProgESScte35Descr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 4, 1, 5),
    _MpegProgESScte35Descr_Type()
)
mpegProgESScte35Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegProgESScte35Descr.setStatus("current")


class _MpegProgESScte18Descr_Type(OctetString):
    """Custom type mpegProgESScte18Descr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MpegProgESScte18Descr_Type.__name__ = "OctetString"
_MpegProgESScte18Descr_Object = MibTableColumn
mpegProgESScte18Descr = _MpegProgESScte18Descr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 4, 1, 6),
    _MpegProgESScte18Descr_Type()
)
mpegProgESScte18Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegProgESScte18Descr.setStatus("current")
_MpegInputStatsTable_Object = MibTable
mpegInputStatsTable = _MpegInputStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mpegInputStatsTable.setStatus("current")
_MpegInputStatsEntry_Object = MibTableRow
mpegInputStatsEntry = _MpegInputStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 5, 1)
)
mpegInputStatsEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegInputTSIndex"),
)
if mibBuilder.loadTexts:
    mpegInputStatsEntry.setStatus("current")


class _MpegInputStatsPcrJitter_Type(Integer32):
    """Custom type mpegInputStatsPcrJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MpegInputStatsPcrJitter_Type.__name__ = "Integer32"
_MpegInputStatsPcrJitter_Object = MibTableColumn
mpegInputStatsPcrJitter = _MpegInputStatsPcrJitter_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 5, 1, 1),
    _MpegInputStatsPcrJitter_Type()
)
mpegInputStatsPcrJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputStatsPcrJitter.setStatus("current")
if mibBuilder.loadTexts:
    mpegInputStatsPcrJitter.setUnits("nanoseconds")


class _MpegInputStatsMaxPacketJitter_Type(Integer32):
    """Custom type mpegInputStatsMaxPacketJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MpegInputStatsMaxPacketJitter_Type.__name__ = "Integer32"
_MpegInputStatsMaxPacketJitter_Object = MibTableColumn
mpegInputStatsMaxPacketJitter = _MpegInputStatsMaxPacketJitter_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 5, 1, 2),
    _MpegInputStatsMaxPacketJitter_Type()
)
mpegInputStatsMaxPacketJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputStatsMaxPacketJitter.setStatus("current")
if mibBuilder.loadTexts:
    mpegInputStatsMaxPacketJitter.setUnits("milliseconds")
_MpegInputStatsPcrPackets_Type = Counter32
_MpegInputStatsPcrPackets_Object = MibTableColumn
mpegInputStatsPcrPackets = _MpegInputStatsPcrPackets_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 5, 1, 3),
    _MpegInputStatsPcrPackets_Type()
)
mpegInputStatsPcrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputStatsPcrPackets.setStatus("current")
_MpegInputStatsNonPcrPackets_Type = Counter32
_MpegInputStatsNonPcrPackets_Object = MibTableColumn
mpegInputStatsNonPcrPackets = _MpegInputStatsNonPcrPackets_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 5, 1, 4),
    _MpegInputStatsNonPcrPackets_Type()
)
mpegInputStatsNonPcrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputStatsNonPcrPackets.setStatus("current")
_MpegInputStatsUnexpectedPackets_Type = Counter32
_MpegInputStatsUnexpectedPackets_Object = MibTableColumn
mpegInputStatsUnexpectedPackets = _MpegInputStatsUnexpectedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 5, 1, 5),
    _MpegInputStatsUnexpectedPackets_Type()
)
mpegInputStatsUnexpectedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputStatsUnexpectedPackets.setStatus("current")
_MpegInputStatsContinuityErrors_Type = Counter32
_MpegInputStatsContinuityErrors_Object = MibTableColumn
mpegInputStatsContinuityErrors = _MpegInputStatsContinuityErrors_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 5, 1, 6),
    _MpegInputStatsContinuityErrors_Type()
)
mpegInputStatsContinuityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputStatsContinuityErrors.setStatus("current")
_MpegInputStatsSyncLossPackets_Type = Counter32
_MpegInputStatsSyncLossPackets_Object = MibTableColumn
mpegInputStatsSyncLossPackets = _MpegInputStatsSyncLossPackets_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 5, 1, 7),
    _MpegInputStatsSyncLossPackets_Type()
)
mpegInputStatsSyncLossPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputStatsSyncLossPackets.setStatus("current")
_MpegInputStatsPcrIntervalExceeds_Type = Counter32
_MpegInputStatsPcrIntervalExceeds_Object = MibTableColumn
mpegInputStatsPcrIntervalExceeds = _MpegInputStatsPcrIntervalExceeds_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 5, 1, 8),
    _MpegInputStatsPcrIntervalExceeds_Type()
)
mpegInputStatsPcrIntervalExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputStatsPcrIntervalExceeds.setStatus("current")
_MpegInputUdpOriginationTable_Object = MibTable
mpegInputUdpOriginationTable = _MpegInputUdpOriginationTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    mpegInputUdpOriginationTable.setStatus("current")
_MpegInputUdpOriginationEntry_Object = MibTableRow
mpegInputUdpOriginationEntry = _MpegInputUdpOriginationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 6, 1)
)
mpegInputUdpOriginationEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegInputUdpOriginationIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegInputUdpOriginationId"),
)
if mibBuilder.loadTexts:
    mpegInputUdpOriginationEntry.setStatus("current")
_MpegInputUdpOriginationIndex_Type = Unsigned32
_MpegInputUdpOriginationIndex_Object = MibTableColumn
mpegInputUdpOriginationIndex = _MpegInputUdpOriginationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 6, 1, 1),
    _MpegInputUdpOriginationIndex_Type()
)
mpegInputUdpOriginationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegInputUdpOriginationIndex.setStatus("current")
_MpegInputUdpOriginationId_Type = Unsigned32
_MpegInputUdpOriginationId_Object = MibTableColumn
mpegInputUdpOriginationId = _MpegInputUdpOriginationId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 6, 1, 2),
    _MpegInputUdpOriginationId_Type()
)
mpegInputUdpOriginationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegInputUdpOriginationId.setStatus("current")
_MpegInputUdpOriginationIfIndex_Type = InterfaceIndex
_MpegInputUdpOriginationIfIndex_Object = MibTableColumn
mpegInputUdpOriginationIfIndex = _MpegInputUdpOriginationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 6, 1, 3),
    _MpegInputUdpOriginationIfIndex_Type()
)
mpegInputUdpOriginationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputUdpOriginationIfIndex.setStatus("current")
_MpegInputUdpOriginationInetAddrType_Type = InetAddressType
_MpegInputUdpOriginationInetAddrType_Object = MibTableColumn
mpegInputUdpOriginationInetAddrType = _MpegInputUdpOriginationInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 6, 1, 4),
    _MpegInputUdpOriginationInetAddrType_Type()
)
mpegInputUdpOriginationInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputUdpOriginationInetAddrType.setStatus("current")
_MpegInputUdpOriginationSrcInetAddr_Type = InetAddress
_MpegInputUdpOriginationSrcInetAddr_Object = MibTableColumn
mpegInputUdpOriginationSrcInetAddr = _MpegInputUdpOriginationSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 6, 1, 5),
    _MpegInputUdpOriginationSrcInetAddr_Type()
)
mpegInputUdpOriginationSrcInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputUdpOriginationSrcInetAddr.setStatus("current")
_MpegInputUdpOriginationDestInetAddr_Type = InetAddress
_MpegInputUdpOriginationDestInetAddr_Object = MibTableColumn
mpegInputUdpOriginationDestInetAddr = _MpegInputUdpOriginationDestInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 6, 1, 6),
    _MpegInputUdpOriginationDestInetAddr_Type()
)
mpegInputUdpOriginationDestInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputUdpOriginationDestInetAddr.setStatus("current")
_MpegInputUdpOriginationDestPort_Type = InetPortNumber
_MpegInputUdpOriginationDestPort_Object = MibTableColumn
mpegInputUdpOriginationDestPort = _MpegInputUdpOriginationDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 6, 1, 7),
    _MpegInputUdpOriginationDestPort_Type()
)
mpegInputUdpOriginationDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputUdpOriginationDestPort.setStatus("current")
_MpegInputUdpOriginationActive_Type = TruthValue
_MpegInputUdpOriginationActive_Object = MibTableColumn
mpegInputUdpOriginationActive = _MpegInputUdpOriginationActive_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 6, 1, 8),
    _MpegInputUdpOriginationActive_Type()
)
mpegInputUdpOriginationActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputUdpOriginationActive.setStatus("current")
_MpegInputUdpOriginationPacketsDetected_Type = TruthValue
_MpegInputUdpOriginationPacketsDetected_Object = MibTableColumn
mpegInputUdpOriginationPacketsDetected = _MpegInputUdpOriginationPacketsDetected_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 6, 1, 9),
    _MpegInputUdpOriginationPacketsDetected_Type()
)
mpegInputUdpOriginationPacketsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputUdpOriginationPacketsDetected.setStatus("current")
_MpegInputUdpOriginationRank_Type = Unsigned32
_MpegInputUdpOriginationRank_Object = MibTableColumn
mpegInputUdpOriginationRank = _MpegInputUdpOriginationRank_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 6, 1, 10),
    _MpegInputUdpOriginationRank_Type()
)
mpegInputUdpOriginationRank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputUdpOriginationRank.setStatus("current")
_MpegInputUdpOriginationInputTSIndex_Type = Unsigned32
_MpegInputUdpOriginationInputTSIndex_Object = MibTableColumn
mpegInputUdpOriginationInputTSIndex = _MpegInputUdpOriginationInputTSIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 1, 6, 1, 11),
    _MpegInputUdpOriginationInputTSIndex_Type()
)
mpegInputUdpOriginationInputTSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputUdpOriginationInputTSIndex.setStatus("current")
_MpegOutputs_ObjectIdentity = ObjectIdentity
mpegOutputs = _MpegOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mpegOutputs.setStatus("current")
_MpegInsertPacketTable_Object = MibTable
mpegInsertPacketTable = _MpegInsertPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mpegInsertPacketTable.setStatus("current")
_MpegInsertPacketEntry_Object = MibTableRow
mpegInsertPacketEntry = _MpegInsertPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 1, 1)
)
mpegInsertPacketEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegInsertPacketIndex"),
)
if mibBuilder.loadTexts:
    mpegInsertPacketEntry.setStatus("current")


class _MpegInsertPacketIndex_Type(Unsigned32):
    """Custom type mpegInsertPacketIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MpegInsertPacketIndex_Type.__name__ = "Unsigned32"
_MpegInsertPacketIndex_Object = MibTableColumn
mpegInsertPacketIndex = _MpegInsertPacketIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 1, 1, 1),
    _MpegInsertPacketIndex_Type()
)
mpegInsertPacketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegInsertPacketIndex.setStatus("current")


class _MpegInsertPacketListId_Type(Unsigned32):
    """Custom type mpegInsertPacketListId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpegInsertPacketListId_Type.__name__ = "Unsigned32"
_MpegInsertPacketListId_Object = MibTableColumn
mpegInsertPacketListId = _MpegInsertPacketListId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 1, 1, 2),
    _MpegInsertPacketListId_Type()
)
mpegInsertPacketListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInsertPacketListId.setStatus("current")
_MpegInsertPacketImmediateExecution_Type = TruthValue
_MpegInsertPacketImmediateExecution_Object = MibTableColumn
mpegInsertPacketImmediateExecution = _MpegInsertPacketImmediateExecution_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 1, 1, 3),
    _MpegInsertPacketImmediateExecution_Type()
)
mpegInsertPacketImmediateExecution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInsertPacketImmediateExecution.setStatus("current")
_MpegInsertPacketStartTime_Type = DateAndTime
_MpegInsertPacketStartTime_Object = MibTableColumn
mpegInsertPacketStartTime = _MpegInsertPacketStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 1, 1, 4),
    _MpegInsertPacketStartTime_Type()
)
mpegInsertPacketStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInsertPacketStartTime.setStatus("current")


class _MpegInsertPacketRepeat_Type(Integer32):
    """Custom type mpegInsertPacketRepeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneTime", 2),
          ("repeat", 1))
    )


_MpegInsertPacketRepeat_Type.__name__ = "Integer32"
_MpegInsertPacketRepeat_Object = MibTableColumn
mpegInsertPacketRepeat = _MpegInsertPacketRepeat_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 1, 1, 5),
    _MpegInsertPacketRepeat_Type()
)
mpegInsertPacketRepeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInsertPacketRepeat.setStatus("current")
_MpegInsertPacketContinuousFlag_Type = TruthValue
_MpegInsertPacketContinuousFlag_Object = MibTableColumn
mpegInsertPacketContinuousFlag = _MpegInsertPacketContinuousFlag_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 1, 1, 6),
    _MpegInsertPacketContinuousFlag_Type()
)
mpegInsertPacketContinuousFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInsertPacketContinuousFlag.setStatus("current")
_MpegInsertPacketRate_Type = Unsigned32
_MpegInsertPacketRate_Object = MibTableColumn
mpegInsertPacketRate = _MpegInsertPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 1, 1, 7),
    _MpegInsertPacketRate_Type()
)
mpegInsertPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInsertPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    mpegInsertPacketRate.setUnits("milliseconds")
_MpegInsertPacketDeviceIfIndex_Type = InterfaceIndex
_MpegInsertPacketDeviceIfIndex_Object = MibTableColumn
mpegInsertPacketDeviceIfIndex = _MpegInsertPacketDeviceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 1, 1, 8),
    _MpegInsertPacketDeviceIfIndex_Type()
)
mpegInsertPacketDeviceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInsertPacketDeviceIfIndex.setStatus("current")
_MpegOutputStatsTable_Object = MibTable
mpegOutputStatsTable = _MpegOutputStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mpegOutputStatsTable.setStatus("current")
_MpegOutputStatsEntry_Object = MibTableRow
mpegOutputStatsEntry = _MpegOutputStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 2, 1)
)
mpegOutputStatsEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegOutputTSIndex"),
)
if mibBuilder.loadTexts:
    mpegOutputStatsEntry.setStatus("current")
_MpegOutputStatsDroppedPackets_Type = Counter32
_MpegOutputStatsDroppedPackets_Object = MibTableColumn
mpegOutputStatsDroppedPackets = _MpegOutputStatsDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 2, 1, 1),
    _MpegOutputStatsDroppedPackets_Type()
)
mpegOutputStatsDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputStatsDroppedPackets.setStatus("current")
_MpegOutputStatsFifoOverflow_Type = Counter32
_MpegOutputStatsFifoOverflow_Object = MibTableColumn
mpegOutputStatsFifoOverflow = _MpegOutputStatsFifoOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 2, 1, 2),
    _MpegOutputStatsFifoOverflow_Type()
)
mpegOutputStatsFifoOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputStatsFifoOverflow.setStatus("current")
_MpegOutputStatsFifoUnderflow_Type = Counter32
_MpegOutputStatsFifoUnderflow_Object = MibTableColumn
mpegOutputStatsFifoUnderflow = _MpegOutputStatsFifoUnderflow_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 2, 1, 3),
    _MpegOutputStatsFifoUnderflow_Type()
)
mpegOutputStatsFifoUnderflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputStatsFifoUnderflow.setStatus("current")
_MpegOutputStatsDataRate_Type = Unsigned32
_MpegOutputStatsDataRate_Object = MibTableColumn
mpegOutputStatsDataRate = _MpegOutputStatsDataRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 2, 1, 4),
    _MpegOutputStatsDataRate_Type()
)
mpegOutputStatsDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputStatsDataRate.setStatus("current")
if mibBuilder.loadTexts:
    mpegOutputStatsDataRate.setUnits("bps")
_MpegOutputStatsAvailableBandwidth_Type = Unsigned32
_MpegOutputStatsAvailableBandwidth_Object = MibTableColumn
mpegOutputStatsAvailableBandwidth = _MpegOutputStatsAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 2, 1, 5),
    _MpegOutputStatsAvailableBandwidth_Type()
)
mpegOutputStatsAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputStatsAvailableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mpegOutputStatsAvailableBandwidth.setUnits("bps")


class _MpegOutputStatsChannelUtilization_Type(Integer32):
    """Custom type mpegOutputStatsChannelUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000),
    )


_MpegOutputStatsChannelUtilization_Type.__name__ = "Integer32"
_MpegOutputStatsChannelUtilization_Object = MibTableColumn
mpegOutputStatsChannelUtilization = _MpegOutputStatsChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 2, 1, 6),
    _MpegOutputStatsChannelUtilization_Type()
)
mpegOutputStatsChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputStatsChannelUtilization.setStatus("current")
if mibBuilder.loadTexts:
    mpegOutputStatsChannelUtilization.setUnits("0.1 Percent")
_MpegOutputStatsTotalPackets_Type = Counter64
_MpegOutputStatsTotalPackets_Object = MibTableColumn
mpegOutputStatsTotalPackets = _MpegOutputStatsTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 2, 1, 7),
    _MpegOutputStatsTotalPackets_Type()
)
mpegOutputStatsTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputStatsTotalPackets.setStatus("current")
_MpegOutputTSTable_Object = MibTable
mpegOutputTSTable = _MpegOutputTSTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mpegOutputTSTable.setStatus("current")
_MpegOutputTSEntry_Object = MibTableRow
mpegOutputTSEntry = _MpegOutputTSEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3, 1)
)
mpegOutputTSEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegOutputTSIndex"),
)
if mibBuilder.loadTexts:
    mpegOutputTSEntry.setStatus("current")
_MpegOutputTSIndex_Type = Unsigned32
_MpegOutputTSIndex_Object = MibTableColumn
mpegOutputTSIndex = _MpegOutputTSIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3, 1, 1),
    _MpegOutputTSIndex_Type()
)
mpegOutputTSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegOutputTSIndex.setStatus("current")


class _MpegOutputTSType_Type(Integer32):
    """Custom type mpegOutputTSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mpts", 2),
          ("spts", 1))
    )


_MpegOutputTSType_Type.__name__ = "Integer32"
_MpegOutputTSType_Object = MibTableColumn
mpegOutputTSType = _MpegOutputTSType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3, 1, 2),
    _MpegOutputTSType_Type()
)
mpegOutputTSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputTSType.setStatus("current")


class _MpegOutputTSConnectionType_Type(Integer32):
    """Custom type mpegOutputTSConnectionType based on Integer32"""
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
          ("qam", 2),
          ("udp", 3))
    )


_MpegOutputTSConnectionType_Type.__name__ = "Integer32"
_MpegOutputTSConnectionType_Object = MibTableColumn
mpegOutputTSConnectionType = _MpegOutputTSConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3, 1, 3),
    _MpegOutputTSConnectionType_Type()
)
mpegOutputTSConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputTSConnectionType.setStatus("current")
_MpegOutputTSConnection_Type = RowPointer
_MpegOutputTSConnection_Object = MibTableColumn
mpegOutputTSConnection = _MpegOutputTSConnection_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3, 1, 4),
    _MpegOutputTSConnection_Type()
)
mpegOutputTSConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputTSConnection.setStatus("current")
_MpegOutputTSNumPrograms_Type = Unsigned32
_MpegOutputTSNumPrograms_Object = MibTableColumn
mpegOutputTSNumPrograms = _MpegOutputTSNumPrograms_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3, 1, 5),
    _MpegOutputTSNumPrograms_Type()
)
mpegOutputTSNumPrograms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputTSNumPrograms.setStatus("current")
_MpegOutputTSTSID_Type = Unsigned32
_MpegOutputTSTSID_Object = MibTableColumn
mpegOutputTSTSID = _MpegOutputTSTSID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3, 1, 6),
    _MpegOutputTSTSID_Type()
)
mpegOutputTSTSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputTSTSID.setStatus("current")
_MpegOutputTSNitPid_Type = HePIDValue
_MpegOutputTSNitPid_Object = MibTableColumn
mpegOutputTSNitPid = _MpegOutputTSNitPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3, 1, 7),
    _MpegOutputTSNitPid_Type()
)
mpegOutputTSNitPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputTSNitPid.setStatus("current")
_MpegOutputTSCaPid_Type = HePIDValue
_MpegOutputTSCaPid_Object = MibTableColumn
mpegOutputTSCaPid = _MpegOutputTSCaPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3, 1, 8),
    _MpegOutputTSCaPid_Type()
)
mpegOutputTSCaPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputTSCaPid.setStatus("current")
_MpegOutputTSCatInsertRate_Type = Unsigned32
_MpegOutputTSCatInsertRate_Object = MibTableColumn
mpegOutputTSCatInsertRate = _MpegOutputTSCatInsertRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3, 1, 9),
    _MpegOutputTSCatInsertRate_Type()
)
mpegOutputTSCatInsertRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputTSCatInsertRate.setStatus("current")
if mibBuilder.loadTexts:
    mpegOutputTSCatInsertRate.setUnits("tables/ms")
_MpegOutputTSPatInsertRate_Type = Unsigned32
_MpegOutputTSPatInsertRate_Object = MibTableColumn
mpegOutputTSPatInsertRate = _MpegOutputTSPatInsertRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3, 1, 10),
    _MpegOutputTSPatInsertRate_Type()
)
mpegOutputTSPatInsertRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputTSPatInsertRate.setStatus("current")
if mibBuilder.loadTexts:
    mpegOutputTSPatInsertRate.setUnits("tables/ms")
_MpegOutputTSPmtInsertRate_Type = Unsigned32
_MpegOutputTSPmtInsertRate_Object = MibTableColumn
mpegOutputTSPmtInsertRate = _MpegOutputTSPmtInsertRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3, 1, 11),
    _MpegOutputTSPmtInsertRate_Type()
)
mpegOutputTSPmtInsertRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputTSPmtInsertRate.setStatus("current")
if mibBuilder.loadTexts:
    mpegOutputTSPmtInsertRate.setUnits("tables/ms")
_MpegOutputTSStartTime_Type = DateAndTime
_MpegOutputTSStartTime_Object = MibTableColumn
mpegOutputTSStartTime = _MpegOutputTSStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 3, 1, 12),
    _MpegOutputTSStartTime_Type()
)
mpegOutputTSStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputTSStartTime.setStatus("current")
_MpegOutputProgTable_Object = MibTable
mpegOutputProgTable = _MpegOutputProgTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    mpegOutputProgTable.setStatus("current")
_MpegOutputProgEntry_Object = MibTableRow
mpegOutputProgEntry = _MpegOutputProgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 4, 1)
)
mpegOutputProgEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegOutputTSIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegOutputProgIndex"),
)
if mibBuilder.loadTexts:
    mpegOutputProgEntry.setStatus("current")
_MpegOutputProgIndex_Type = Unsigned32
_MpegOutputProgIndex_Object = MibTableColumn
mpegOutputProgIndex = _MpegOutputProgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 4, 1, 1),
    _MpegOutputProgIndex_Type()
)
mpegOutputProgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegOutputProgIndex.setStatus("current")
_MpegOutputProgNo_Type = Unsigned32
_MpegOutputProgNo_Object = MibTableColumn
mpegOutputProgNo = _MpegOutputProgNo_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 4, 1, 2),
    _MpegOutputProgNo_Type()
)
mpegOutputProgNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputProgNo.setStatus("current")


class _MpegOutputProgPmtVersion_Type(Unsigned32):
    """Custom type mpegOutputProgPmtVersion based on Unsigned32"""
    defaultValue = 0


_MpegOutputProgPmtVersion_Object = MibTableColumn
mpegOutputProgPmtVersion = _MpegOutputProgPmtVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 4, 1, 3),
    _MpegOutputProgPmtVersion_Type()
)
mpegOutputProgPmtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputProgPmtVersion.setStatus("current")
_MpegOutputProgPmtPid_Type = HePIDValue
_MpegOutputProgPmtPid_Object = MibTableColumn
mpegOutputProgPmtPid = _MpegOutputProgPmtPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 4, 1, 4),
    _MpegOutputProgPmtPid_Type()
)
mpegOutputProgPmtPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputProgPmtPid.setStatus("current")
_MpegOutputProgPcrPid_Type = HePIDValue
_MpegOutputProgPcrPid_Object = MibTableColumn
mpegOutputProgPcrPid = _MpegOutputProgPcrPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 4, 1, 5),
    _MpegOutputProgPcrPid_Type()
)
mpegOutputProgPcrPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputProgPcrPid.setStatus("current")
_MpegOutputProgEcmPid_Type = HePIDValue
_MpegOutputProgEcmPid_Object = MibTableColumn
mpegOutputProgEcmPid = _MpegOutputProgEcmPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 4, 1, 6),
    _MpegOutputProgEcmPid_Type()
)
mpegOutputProgEcmPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputProgEcmPid.setStatus("current")
_MpegOutputProgNumElems_Type = Unsigned32
_MpegOutputProgNumElems_Object = MibTableColumn
mpegOutputProgNumElems = _MpegOutputProgNumElems_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 4, 1, 7),
    _MpegOutputProgNumElems_Type()
)
mpegOutputProgNumElems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputProgNumElems.setStatus("current")


class _MpegOutputProgNumEcms_Type(Unsigned32):
    """Custom type mpegOutputProgNumEcms based on Unsigned32"""
    defaultValue = 9999


_MpegOutputProgNumEcms_Object = MibTableColumn
mpegOutputProgNumEcms = _MpegOutputProgNumEcms_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 4, 1, 8),
    _MpegOutputProgNumEcms_Type()
)
mpegOutputProgNumEcms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputProgNumEcms.setStatus("current")


class _MpegOutputProgCaDescr_Type(OctetString):
    """Custom type mpegOutputProgCaDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MpegOutputProgCaDescr_Type.__name__ = "OctetString"
_MpegOutputProgCaDescr_Object = MibTableColumn
mpegOutputProgCaDescr = _MpegOutputProgCaDescr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 4, 1, 9),
    _MpegOutputProgCaDescr_Type()
)
mpegOutputProgCaDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputProgCaDescr.setStatus("current")


class _MpegOutputProgScte35Descr_Type(OctetString):
    """Custom type mpegOutputProgScte35Descr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MpegOutputProgScte35Descr_Type.__name__ = "OctetString"
_MpegOutputProgScte35Descr_Object = MibTableColumn
mpegOutputProgScte35Descr = _MpegOutputProgScte35Descr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 4, 1, 10),
    _MpegOutputProgScte35Descr_Type()
)
mpegOutputProgScte35Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputProgScte35Descr.setStatus("current")


class _MpegOutputProgScte18Descr_Type(OctetString):
    """Custom type mpegOutputProgScte18Descr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MpegOutputProgScte18Descr_Type.__name__ = "OctetString"
_MpegOutputProgScte18Descr_Object = MibTableColumn
mpegOutputProgScte18Descr = _MpegOutputProgScte18Descr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 4, 1, 11),
    _MpegOutputProgScte18Descr_Type()
)
mpegOutputProgScte18Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputProgScte18Descr.setStatus("current")
_MpegOutputProgElemStatsTable_Object = MibTable
mpegOutputProgElemStatsTable = _MpegOutputProgElemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    mpegOutputProgElemStatsTable.setStatus("current")
_MpegOutputProgElemStatsEntry_Object = MibTableRow
mpegOutputProgElemStatsEntry = _MpegOutputProgElemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 5, 1)
)
mpegOutputProgElemStatsEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegOutputTSIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegOutputProgIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegOutputProgElemStatsIndex"),
)
if mibBuilder.loadTexts:
    mpegOutputProgElemStatsEntry.setStatus("current")
_MpegOutputProgElemStatsIndex_Type = Unsigned32
_MpegOutputProgElemStatsIndex_Object = MibTableColumn
mpegOutputProgElemStatsIndex = _MpegOutputProgElemStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 5, 1, 1),
    _MpegOutputProgElemStatsIndex_Type()
)
mpegOutputProgElemStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegOutputProgElemStatsIndex.setStatus("current")
_MpegOutputProgElemStatsPid_Type = HePIDValue
_MpegOutputProgElemStatsPid_Object = MibTableColumn
mpegOutputProgElemStatsPid = _MpegOutputProgElemStatsPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 5, 1, 2),
    _MpegOutputProgElemStatsPid_Type()
)
mpegOutputProgElemStatsPid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegOutputProgElemStatsPid.setStatus("current")


class _MpegOutputProgElemStatsElemType_Type(Integer32):
    """Custom type mpegOutputProgElemStatsElemType based on Integer32"""
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
        *(("audio", 2),
          ("data", 3),
          ("scte18", 4),
          ("scte35", 5),
          ("unknown", 6),
          ("video", 1))
    )


_MpegOutputProgElemStatsElemType_Type.__name__ = "Integer32"
_MpegOutputProgElemStatsElemType_Object = MibTableColumn
mpegOutputProgElemStatsElemType = _MpegOutputProgElemStatsElemType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 5, 1, 3),
    _MpegOutputProgElemStatsElemType_Type()
)
mpegOutputProgElemStatsElemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputProgElemStatsElemType.setStatus("current")
_MpegOutputProgElemStatsDataRate_Type = Integer32
_MpegOutputProgElemStatsDataRate_Object = MibTableColumn
mpegOutputProgElemStatsDataRate = _MpegOutputProgElemStatsDataRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 5, 1, 4),
    _MpegOutputProgElemStatsDataRate_Type()
)
mpegOutputProgElemStatsDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputProgElemStatsDataRate.setStatus("current")
if mibBuilder.loadTexts:
    mpegOutputProgElemStatsDataRate.setUnits("bps")
_MpegOutputUdpDestinationTable_Object = MibTable
mpegOutputUdpDestinationTable = _MpegOutputUdpDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mpegOutputUdpDestinationTable.setStatus("current")
_MpegOutputUdpDestinationEntry_Object = MibTableRow
mpegOutputUdpDestinationEntry = _MpegOutputUdpDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 6, 1)
)
mpegOutputUdpDestinationEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegOutputUdpDestinationIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegOutputUdpDestinationId"),
)
if mibBuilder.loadTexts:
    mpegOutputUdpDestinationEntry.setStatus("current")
_MpegOutputUdpDestinationIndex_Type = Unsigned32
_MpegOutputUdpDestinationIndex_Object = MibTableColumn
mpegOutputUdpDestinationIndex = _MpegOutputUdpDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 6, 1, 1),
    _MpegOutputUdpDestinationIndex_Type()
)
mpegOutputUdpDestinationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegOutputUdpDestinationIndex.setStatus("current")
_MpegOutputUdpDestinationId_Type = Unsigned32
_MpegOutputUdpDestinationId_Object = MibTableColumn
mpegOutputUdpDestinationId = _MpegOutputUdpDestinationId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 6, 1, 2),
    _MpegOutputUdpDestinationId_Type()
)
mpegOutputUdpDestinationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegOutputUdpDestinationId.setStatus("current")
_MpegOutputUdpDestinationIfIndex_Type = InterfaceIndex
_MpegOutputUdpDestinationIfIndex_Object = MibTableColumn
mpegOutputUdpDestinationIfIndex = _MpegOutputUdpDestinationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 6, 1, 3),
    _MpegOutputUdpDestinationIfIndex_Type()
)
mpegOutputUdpDestinationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputUdpDestinationIfIndex.setStatus("current")
_MpegOutputUdpDestinationInetAddrType_Type = InetAddressType
_MpegOutputUdpDestinationInetAddrType_Object = MibTableColumn
mpegOutputUdpDestinationInetAddrType = _MpegOutputUdpDestinationInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 6, 1, 4),
    _MpegOutputUdpDestinationInetAddrType_Type()
)
mpegOutputUdpDestinationInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputUdpDestinationInetAddrType.setStatus("current")
_MpegOutputUdpDestinationSrcInetAddr_Type = InetAddress
_MpegOutputUdpDestinationSrcInetAddr_Object = MibTableColumn
mpegOutputUdpDestinationSrcInetAddr = _MpegOutputUdpDestinationSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 6, 1, 5),
    _MpegOutputUdpDestinationSrcInetAddr_Type()
)
mpegOutputUdpDestinationSrcInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputUdpDestinationSrcInetAddr.setStatus("current")
_MpegOutputUdpDestinationDestInetAddr_Type = InetAddress
_MpegOutputUdpDestinationDestInetAddr_Object = MibTableColumn
mpegOutputUdpDestinationDestInetAddr = _MpegOutputUdpDestinationDestInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 6, 1, 6),
    _MpegOutputUdpDestinationDestInetAddr_Type()
)
mpegOutputUdpDestinationDestInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputUdpDestinationDestInetAddr.setStatus("current")
_MpegOutputUdpDestinationDestPort_Type = InetPortNumber
_MpegOutputUdpDestinationDestPort_Object = MibTableColumn
mpegOutputUdpDestinationDestPort = _MpegOutputUdpDestinationDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 6, 1, 7),
    _MpegOutputUdpDestinationDestPort_Type()
)
mpegOutputUdpDestinationDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputUdpDestinationDestPort.setStatus("current")
_MpegOutputUdpDestinationOutputTSIndex_Type = Unsigned32
_MpegOutputUdpDestinationOutputTSIndex_Object = MibTableColumn
mpegOutputUdpDestinationOutputTSIndex = _MpegOutputUdpDestinationOutputTSIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 2, 6, 1, 8),
    _MpegOutputUdpDestinationOutputTSIndex_Type()
)
mpegOutputUdpDestinationOutputTSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegOutputUdpDestinationOutputTSIndex.setStatus("current")
_MpegProgramMappingTable_Object = MibTable
mpegProgramMappingTable = _MpegProgramMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mpegProgramMappingTable.setStatus("current")
_MpegProgramMappingEntry_Object = MibTableRow
mpegProgramMappingEntry = _MpegProgramMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 3, 1)
)
mpegProgramMappingEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegProgramMappingIndex"),
)
if mibBuilder.loadTexts:
    mpegProgramMappingEntry.setStatus("current")
_MpegProgramMappingIndex_Type = Unsigned32
_MpegProgramMappingIndex_Object = MibTableColumn
mpegProgramMappingIndex = _MpegProgramMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 3, 1, 1),
    _MpegProgramMappingIndex_Type()
)
mpegProgramMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegProgramMappingIndex.setStatus("current")
_MpegProgramMappingOutputProgIndex_Type = Unsigned32
_MpegProgramMappingOutputProgIndex_Object = MibTableColumn
mpegProgramMappingOutputProgIndex = _MpegProgramMappingOutputProgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 3, 1, 2),
    _MpegProgramMappingOutputProgIndex_Type()
)
mpegProgramMappingOutputProgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegProgramMappingOutputProgIndex.setStatus("current")
_MpegProgramMappingOutputTSIndex_Type = Unsigned32
_MpegProgramMappingOutputTSIndex_Object = MibTableColumn
mpegProgramMappingOutputTSIndex = _MpegProgramMappingOutputTSIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 3, 1, 3),
    _MpegProgramMappingOutputTSIndex_Type()
)
mpegProgramMappingOutputTSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegProgramMappingOutputTSIndex.setStatus("current")
_MpegProgramMappingInputProgIndex_Type = Unsigned32
_MpegProgramMappingInputProgIndex_Object = MibTableColumn
mpegProgramMappingInputProgIndex = _MpegProgramMappingInputProgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 3, 1, 4),
    _MpegProgramMappingInputProgIndex_Type()
)
mpegProgramMappingInputProgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegProgramMappingInputProgIndex.setStatus("current")
_MpegProgramMappingInputTSIndex_Type = Unsigned32
_MpegProgramMappingInputTSIndex_Object = MibTableColumn
mpegProgramMappingInputTSIndex = _MpegProgramMappingInputTSIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 3, 1, 5),
    _MpegProgramMappingInputTSIndex_Type()
)
mpegProgramMappingInputTSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegProgramMappingInputTSIndex.setStatus("current")
_MpegVideoSessionTable_Object = MibTable
mpegVideoSessionTable = _MpegVideoSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mpegVideoSessionTable.setStatus("current")
_MpegVideoSessionEntry_Object = MibTableRow
mpegVideoSessionEntry = _MpegVideoSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4, 1)
)
mpegVideoSessionEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionIndex"),
)
if mibBuilder.loadTexts:
    mpegVideoSessionEntry.setStatus("current")
_MpegVideoSessionIndex_Type = Unsigned32
_MpegVideoSessionIndex_Object = MibTableColumn
mpegVideoSessionIndex = _MpegVideoSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4, 1, 1),
    _MpegVideoSessionIndex_Type()
)
mpegVideoSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegVideoSessionIndex.setStatus("current")
_MpegVideoSessionPhyMappingIndex_Type = Unsigned32
_MpegVideoSessionPhyMappingIndex_Object = MibTableColumn
mpegVideoSessionPhyMappingIndex = _MpegVideoSessionPhyMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4, 1, 2),
    _MpegVideoSessionPhyMappingIndex_Type()
)
mpegVideoSessionPhyMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegVideoSessionPhyMappingIndex.setStatus("current")
_MpegVideoSessionPIDRemap_Type = TruthValue
_MpegVideoSessionPIDRemap_Object = MibTableColumn
mpegVideoSessionPIDRemap = _MpegVideoSessionPIDRemap_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4, 1, 3),
    _MpegVideoSessionPIDRemap_Type()
)
mpegVideoSessionPIDRemap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegVideoSessionPIDRemap.setStatus("current")


class _MpegVideoSessionMode_Type(Integer32):
    """Custom type mpegVideoSessionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiplexing", 3),
          ("other", 1),
          ("passThrough", 2))
    )


_MpegVideoSessionMode_Type.__name__ = "Integer32"
_MpegVideoSessionMode_Object = MibTableColumn
mpegVideoSessionMode = _MpegVideoSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4, 1, 4),
    _MpegVideoSessionMode_Type()
)
mpegVideoSessionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegVideoSessionMode.setStatus("current")


class _MpegVideoSessionState_Type(Integer32):
    """Custom type mpegVideoSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("provisioned", 2))
    )


_MpegVideoSessionState_Type.__name__ = "Integer32"
_MpegVideoSessionState_Object = MibTableColumn
mpegVideoSessionState = _MpegVideoSessionState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4, 1, 5),
    _MpegVideoSessionState_Type()
)
mpegVideoSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegVideoSessionState.setStatus("current")


class _MpegVideoSessionProvMethod_Type(Integer32):
    """Custom type mpegVideoSessionProvMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("sessionBased", 2),
          ("tableBased", 1))
    )


_MpegVideoSessionProvMethod_Type.__name__ = "Integer32"
_MpegVideoSessionProvMethod_Object = MibTableColumn
mpegVideoSessionProvMethod = _MpegVideoSessionProvMethod_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4, 1, 6),
    _MpegVideoSessionProvMethod_Type()
)
mpegVideoSessionProvMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegVideoSessionProvMethod.setStatus("current")


class _MpegVideoSessionEncryptionType_Type(Integer32):
    """Custom type mpegVideoSessionEncryptionType based on Integer32"""
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
        *(("aes", 6),
          ("des", 4),
          ("des3", 5),
          ("dvbCsa", 7),
          ("dvs042", 10),
          ("mediac", 9),
          ("none", 1),
          ("other", 2),
          ("pkey", 8),
          ("preencrypted", 3))
    )


_MpegVideoSessionEncryptionType_Type.__name__ = "Integer32"
_MpegVideoSessionEncryptionType_Object = MibTableColumn
mpegVideoSessionEncryptionType = _MpegVideoSessionEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4, 1, 7),
    _MpegVideoSessionEncryptionType_Type()
)
mpegVideoSessionEncryptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegVideoSessionEncryptionType.setStatus("current")
_MpegVideoSessionEncryptionInfo_Type = AutonomousType
_MpegVideoSessionEncryptionInfo_Object = MibTableColumn
mpegVideoSessionEncryptionInfo = _MpegVideoSessionEncryptionInfo_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4, 1, 8),
    _MpegVideoSessionEncryptionInfo_Type()
)
mpegVideoSessionEncryptionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegVideoSessionEncryptionInfo.setStatus("current")
_MpegVideoSessionBitRate_Type = Unsigned32
_MpegVideoSessionBitRate_Object = MibTableColumn
mpegVideoSessionBitRate = _MpegVideoSessionBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4, 1, 9),
    _MpegVideoSessionBitRate_Type()
)
mpegVideoSessionBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegVideoSessionBitRate.setStatus("current")
if mibBuilder.loadTexts:
    mpegVideoSessionBitRate.setUnits("bps")


class _MpegVideoSessionID_Type(OctetString):
    """Custom type mpegVideoSessionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MpegVideoSessionID_Type.__name__ = "OctetString"
_MpegVideoSessionID_Object = MibTableColumn
mpegVideoSessionID = _MpegVideoSessionID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4, 1, 10),
    _MpegVideoSessionID_Type()
)
mpegVideoSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegVideoSessionID.setStatus("current")
_MpegVideoSessionSelectedInput_Type = RowPointer
_MpegVideoSessionSelectedInput_Object = MibTableColumn
mpegVideoSessionSelectedInput = _MpegVideoSessionSelectedInput_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4, 1, 11),
    _MpegVideoSessionSelectedInput_Type()
)
mpegVideoSessionSelectedInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegVideoSessionSelectedInput.setStatus("current")
_MpegVideoSessionSelectedOutput_Type = RowPointer
_MpegVideoSessionSelectedOutput_Object = MibTableColumn
mpegVideoSessionSelectedOutput = _MpegVideoSessionSelectedOutput_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 4, 1, 12),
    _MpegVideoSessionSelectedOutput_Type()
)
mpegVideoSessionSelectedOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegVideoSessionSelectedOutput.setStatus("current")
_MpegVideoSessionPtrTable_Object = MibTable
mpegVideoSessionPtrTable = _MpegVideoSessionPtrTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mpegVideoSessionPtrTable.setStatus("current")
_MpegVideoSessionPtrEntry_Object = MibTableRow
mpegVideoSessionPtrEntry = _MpegVideoSessionPtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 5, 1)
)
mpegVideoSessionPtrEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionPtrInputProgIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionPtrInputTSIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionPtrInputTSConnType"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionPtrInputTSConnection"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionPtrOutputProgIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionPtrOutputTSIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionPtrOutputTSConnType"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionPtrOutputTSConnection"),
)
if mibBuilder.loadTexts:
    mpegVideoSessionPtrEntry.setStatus("current")
_MpegVideoSessionPtrInputProgIndex_Type = Unsigned32
_MpegVideoSessionPtrInputProgIndex_Object = MibTableColumn
mpegVideoSessionPtrInputProgIndex = _MpegVideoSessionPtrInputProgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 5, 1, 1),
    _MpegVideoSessionPtrInputProgIndex_Type()
)
mpegVideoSessionPtrInputProgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegVideoSessionPtrInputProgIndex.setStatus("current")
_MpegVideoSessionPtrInputTSIndex_Type = Unsigned32
_MpegVideoSessionPtrInputTSIndex_Object = MibTableColumn
mpegVideoSessionPtrInputTSIndex = _MpegVideoSessionPtrInputTSIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 5, 1, 2),
    _MpegVideoSessionPtrInputTSIndex_Type()
)
mpegVideoSessionPtrInputTSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegVideoSessionPtrInputTSIndex.setStatus("current")
_MpegVideoSessionPtrInputTSConnType_Type = Unsigned32
_MpegVideoSessionPtrInputTSConnType_Object = MibTableColumn
mpegVideoSessionPtrInputTSConnType = _MpegVideoSessionPtrInputTSConnType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 5, 1, 3),
    _MpegVideoSessionPtrInputTSConnType_Type()
)
mpegVideoSessionPtrInputTSConnType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegVideoSessionPtrInputTSConnType.setStatus("current")
_MpegVideoSessionPtrInputTSConnection_Type = Unsigned32
_MpegVideoSessionPtrInputTSConnection_Object = MibTableColumn
mpegVideoSessionPtrInputTSConnection = _MpegVideoSessionPtrInputTSConnection_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 5, 1, 4),
    _MpegVideoSessionPtrInputTSConnection_Type()
)
mpegVideoSessionPtrInputTSConnection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegVideoSessionPtrInputTSConnection.setStatus("current")
_MpegVideoSessionPtrOutputProgIndex_Type = Unsigned32
_MpegVideoSessionPtrOutputProgIndex_Object = MibTableColumn
mpegVideoSessionPtrOutputProgIndex = _MpegVideoSessionPtrOutputProgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 5, 1, 5),
    _MpegVideoSessionPtrOutputProgIndex_Type()
)
mpegVideoSessionPtrOutputProgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegVideoSessionPtrOutputProgIndex.setStatus("current")
_MpegVideoSessionPtrOutputTSIndex_Type = Unsigned32
_MpegVideoSessionPtrOutputTSIndex_Object = MibTableColumn
mpegVideoSessionPtrOutputTSIndex = _MpegVideoSessionPtrOutputTSIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 5, 1, 6),
    _MpegVideoSessionPtrOutputTSIndex_Type()
)
mpegVideoSessionPtrOutputTSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegVideoSessionPtrOutputTSIndex.setStatus("current")
_MpegVideoSessionPtrOutputTSConnType_Type = Unsigned32
_MpegVideoSessionPtrOutputTSConnType_Object = MibTableColumn
mpegVideoSessionPtrOutputTSConnType = _MpegVideoSessionPtrOutputTSConnType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 5, 1, 7),
    _MpegVideoSessionPtrOutputTSConnType_Type()
)
mpegVideoSessionPtrOutputTSConnType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegVideoSessionPtrOutputTSConnType.setStatus("current")
_MpegVideoSessionPtrOutputTSConnection_Type = Unsigned32
_MpegVideoSessionPtrOutputTSConnection_Object = MibTableColumn
mpegVideoSessionPtrOutputTSConnection = _MpegVideoSessionPtrOutputTSConnection_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 5, 1, 8),
    _MpegVideoSessionPtrOutputTSConnection_Type()
)
mpegVideoSessionPtrOutputTSConnection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpegVideoSessionPtrOutputTSConnection.setStatus("current")


class _MpegVideoSessionPtrStatus_Type(Integer32):
    """Custom type mpegVideoSessionPtrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("closed", 2))
    )


_MpegVideoSessionPtrStatus_Type.__name__ = "Integer32"
_MpegVideoSessionPtrStatus_Object = MibTableColumn
mpegVideoSessionPtrStatus = _MpegVideoSessionPtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 5, 1, 9),
    _MpegVideoSessionPtrStatus_Type()
)
mpegVideoSessionPtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegVideoSessionPtrStatus.setStatus("current")
_MpegInputTSOutputSessionTable_Object = MibTable
mpegInputTSOutputSessionTable = _MpegInputTSOutputSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    mpegInputTSOutputSessionTable.setStatus("current")
_MpegInputTSOutputSessionEntry_Object = MibTableRow
mpegInputTSOutputSessionEntry = _MpegInputTSOutputSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 6, 1)
)
mpegInputTSOutputSessionEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-MIB", "mpegInputTSIndex"),
    (0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionIndex"),
)
if mibBuilder.loadTexts:
    mpegInputTSOutputSessionEntry.setStatus("current")
_MpegInputTSOutputSessionCreateTime_Type = DateAndTime
_MpegInputTSOutputSessionCreateTime_Object = MibTableColumn
mpegInputTSOutputSessionCreateTime = _MpegInputTSOutputSessionCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 1, 6, 1, 1),
    _MpegInputTSOutputSessionCreateTime_Type()
)
mpegInputTSOutputSessionCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpegInputTSOutputSessionCreateTime.setStatus("current")
_MpegMIBConformance_ObjectIdentity = ObjectIdentity
mpegMIBConformance = _MpegMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 2)
)
if mibBuilder.loadTexts:
    mpegMIBConformance.setStatus("current")
_MpegMIBCompliances_ObjectIdentity = ObjectIdentity
mpegMIBCompliances = _MpegMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mpegMIBCompliances.setStatus("current")
_MpegMIBGroups_ObjectIdentity = ObjectIdentity
mpegMIBGroups = _MpegMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mpegMIBGroups.setStatus("current")

# Managed Objects groups

mpegInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 2, 2, 1)
)
mpegInputGroup.setObjects(
      *(("SCTE-HMS-MPEG-MIB", "mpegInputTSType"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSConnectionType"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSConnection"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSActiveConnection"),
        ("SCTE-HMS-MPEG-MIB", "mpegLossOfSignalTimeout"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSPsiDetected"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSStartTime"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSResourceAllocated"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSNumPrograms"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSRate"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSMaxRate"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSPatVersion"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSCatVersion"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSNitPid"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSNumEmms"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSTSID"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSLock"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputUdpOriginationIfIndex"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputUdpOriginationInetAddrType"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputUdpOriginationSrcInetAddr"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputUdpOriginationDestInetAddr"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputUdpOriginationDestPort"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputUdpOriginationActive"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputUdpOriginationPacketsDetected"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputUdpOriginationRank"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputUdpOriginationInputTSIndex"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputProgPmtVersion"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputProgNo"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputProgPmtVersion"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputProgPmtPid"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputProgPcrPid"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputProgEcmPid"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputProgNumElems"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputProgNumEcms"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputProgCaDescr"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputProgScte35Descr"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputProgScte18Descr"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputStatsPcrPackets"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputStatsNonPcrPackets"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputStatsUnexpectedPackets"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputStatsContinuityErrors"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputStatsSyncLossPackets"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputStatsPcrIntervalExceeds"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputStatsPcrJitter"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputStatsMaxPacketJitter"))
)
if mibBuilder.loadTexts:
    mpegInputGroup.setStatus("current")

mpegInputProgESGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 2, 2, 2)
)
mpegInputProgESGroup.setObjects(
      *(("SCTE-HMS-MPEG-MIB", "mpegProgESScte18Descr"),
        ("SCTE-HMS-MPEG-MIB", "mpegProgESScte35Descr"),
        ("SCTE-HMS-MPEG-MIB", "mpegProgESCaDescr"),
        ("SCTE-HMS-MPEG-MIB", "mpegProgESPID"),
        ("SCTE-HMS-MPEG-MIB", "mpegProgESType"))
)
if mibBuilder.loadTexts:
    mpegInputProgESGroup.setStatus("current")

mpegOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 2, 2, 3)
)
mpegOutputGroup.setObjects(
      *(("SCTE-HMS-MPEG-MIB", "mpegInsertPacketListId"),
        ("SCTE-HMS-MPEG-MIB", "mpegInsertPacketImmediateExecution"),
        ("SCTE-HMS-MPEG-MIB", "mpegInsertPacketStartTime"),
        ("SCTE-HMS-MPEG-MIB", "mpegInsertPacketRepeat"),
        ("SCTE-HMS-MPEG-MIB", "mpegInsertPacketContinuousFlag"),
        ("SCTE-HMS-MPEG-MIB", "mpegInsertPacketRate"),
        ("SCTE-HMS-MPEG-MIB", "mpegInsertPacketDeviceIfIndex"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputStatsDroppedPackets"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputStatsFifoOverflow"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputStatsFifoUnderflow"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputStatsDataRate"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputStatsAvailableBandwidth"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputProgNo"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputProgPmtVersion"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputProgPmtPid"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputProgPcrPid"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputProgEcmPid"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputProgNumElems"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputProgNumEcms"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputProgCaDescr"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputProgScte35Descr"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputTSType"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputTSConnectionType"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputTSConnection"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputTSNumPrograms"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputTSTSID"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputTSNitPid"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputTSCaPid"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputTSCatInsertRate"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputTSPatInsertRate"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputProgScte18Descr"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputTSPmtInsertRate"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputTSStartTime"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputUdpDestinationIfIndex"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputUdpDestinationInetAddrType"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputUdpDestinationSrcInetAddr"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputUdpDestinationDestInetAddr"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputUdpDestinationDestPort"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputUdpDestinationOutputTSIndex"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputStatsChannelUtilization"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputStatsTotalPackets"))
)
if mibBuilder.loadTexts:
    mpegOutputGroup.setStatus("current")

mpegOutputProgElemStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 2, 2, 4)
)
mpegOutputProgElemStatsGroup.setObjects(
      *(("SCTE-HMS-MPEG-MIB", "mpegOutputProgElemStatsDataRate"),
        ("SCTE-HMS-MPEG-MIB", "mpegOutputProgElemStatsElemType"))
)
if mibBuilder.loadTexts:
    mpegOutputProgElemStatsGroup.setStatus("current")

mpegMappingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 2, 2, 5)
)
mpegMappingsGroup.setObjects(
      *(("SCTE-HMS-MPEG-MIB", "mpegProgramMappingOutputProgIndex"),
        ("SCTE-HMS-MPEG-MIB", "mpegProgramMappingOutputTSIndex"),
        ("SCTE-HMS-MPEG-MIB", "mpegProgramMappingInputProgIndex"),
        ("SCTE-HMS-MPEG-MIB", "mpegProgramMappingInputTSIndex"))
)
if mibBuilder.loadTexts:
    mpegMappingsGroup.setStatus("current")

mpegSessionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 2, 2, 6)
)
mpegSessionsGroup.setObjects(
      *(("SCTE-HMS-MPEG-MIB", "mpegVideoSessionPhyMappingIndex"),
        ("SCTE-HMS-MPEG-MIB", "mpegVideoSessionPIDRemap"),
        ("SCTE-HMS-MPEG-MIB", "mpegVideoSessionMode"),
        ("SCTE-HMS-MPEG-MIB", "mpegVideoSessionState"),
        ("SCTE-HMS-MPEG-MIB", "mpegVideoSessionProvMethod"),
        ("SCTE-HMS-MPEG-MIB", "mpegVideoSessionEncryptionType"),
        ("SCTE-HMS-MPEG-MIB", "mpegVideoSessionEncryptionInfo"),
        ("SCTE-HMS-MPEG-MIB", "mpegVideoSessionBitRate"),
        ("SCTE-HMS-MPEG-MIB", "mpegVideoSessionID"),
        ("SCTE-HMS-MPEG-MIB", "mpegVideoSessionSelectedInput"),
        ("SCTE-HMS-MPEG-MIB", "mpegVideoSessionSelectedOutput"),
        ("SCTE-HMS-MPEG-MIB", "mpegVideoSessionPtrStatus"),
        ("SCTE-HMS-MPEG-MIB", "mpegInputTSOutputSessionCreateTime"))
)
if mibBuilder.loadTexts:
    mpegSessionsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mpegSupport = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mpegSupport.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-MPEG-MIB",
    **{"heMpegCommonMIB": heMpegCommonMIB,
       "mpegMIBObjects": mpegMIBObjects,
       "mpegDigitalInputs": mpegDigitalInputs,
       "mpegLossOfSignalTimeout": mpegLossOfSignalTimeout,
       "mpegInputTSTable": mpegInputTSTable,
       "mpegInputTSEntry": mpegInputTSEntry,
       "mpegInputTSIndex": mpegInputTSIndex,
       "mpegInputTSType": mpegInputTSType,
       "mpegInputTSConnectionType": mpegInputTSConnectionType,
       "mpegInputTSConnection": mpegInputTSConnection,
       "mpegInputTSActiveConnection": mpegInputTSActiveConnection,
       "mpegInputTSPsiDetected": mpegInputTSPsiDetected,
       "mpegInputTSStartTime": mpegInputTSStartTime,
       "mpegInputTSResourceAllocated": mpegInputTSResourceAllocated,
       "mpegInputTSNumPrograms": mpegInputTSNumPrograms,
       "mpegInputTSRate": mpegInputTSRate,
       "mpegInputTSMaxRate": mpegInputTSMaxRate,
       "mpegInputTSPatVersion": mpegInputTSPatVersion,
       "mpegInputTSCatVersion": mpegInputTSCatVersion,
       "mpegInputTSNitPid": mpegInputTSNitPid,
       "mpegInputTSNumEmms": mpegInputTSNumEmms,
       "mpegInputTSTSID": mpegInputTSTSID,
       "mpegInputTSLock": mpegInputTSLock,
       "mpegInputProgTable": mpegInputProgTable,
       "mpegInputProgEntry": mpegInputProgEntry,
       "mpegInputProgIndex": mpegInputProgIndex,
       "mpegInputProgNo": mpegInputProgNo,
       "mpegInputProgPmtVersion": mpegInputProgPmtVersion,
       "mpegInputProgPmtPid": mpegInputProgPmtPid,
       "mpegInputProgPcrPid": mpegInputProgPcrPid,
       "mpegInputProgEcmPid": mpegInputProgEcmPid,
       "mpegInputProgNumElems": mpegInputProgNumElems,
       "mpegInputProgNumEcms": mpegInputProgNumEcms,
       "mpegInputProgCaDescr": mpegInputProgCaDescr,
       "mpegInputProgScte35Descr": mpegInputProgScte35Descr,
       "mpegInputProgScte18Descr": mpegInputProgScte18Descr,
       "mpegProgESTable": mpegProgESTable,
       "mpegProgESEntry": mpegProgESEntry,
       "mpegProgESIndex": mpegProgESIndex,
       "mpegProgESPID": mpegProgESPID,
       "mpegProgESType": mpegProgESType,
       "mpegProgESCaDescr": mpegProgESCaDescr,
       "mpegProgESScte35Descr": mpegProgESScte35Descr,
       "mpegProgESScte18Descr": mpegProgESScte18Descr,
       "mpegInputStatsTable": mpegInputStatsTable,
       "mpegInputStatsEntry": mpegInputStatsEntry,
       "mpegInputStatsPcrJitter": mpegInputStatsPcrJitter,
       "mpegInputStatsMaxPacketJitter": mpegInputStatsMaxPacketJitter,
       "mpegInputStatsPcrPackets": mpegInputStatsPcrPackets,
       "mpegInputStatsNonPcrPackets": mpegInputStatsNonPcrPackets,
       "mpegInputStatsUnexpectedPackets": mpegInputStatsUnexpectedPackets,
       "mpegInputStatsContinuityErrors": mpegInputStatsContinuityErrors,
       "mpegInputStatsSyncLossPackets": mpegInputStatsSyncLossPackets,
       "mpegInputStatsPcrIntervalExceeds": mpegInputStatsPcrIntervalExceeds,
       "mpegInputUdpOriginationTable": mpegInputUdpOriginationTable,
       "mpegInputUdpOriginationEntry": mpegInputUdpOriginationEntry,
       "mpegInputUdpOriginationIndex": mpegInputUdpOriginationIndex,
       "mpegInputUdpOriginationId": mpegInputUdpOriginationId,
       "mpegInputUdpOriginationIfIndex": mpegInputUdpOriginationIfIndex,
       "mpegInputUdpOriginationInetAddrType": mpegInputUdpOriginationInetAddrType,
       "mpegInputUdpOriginationSrcInetAddr": mpegInputUdpOriginationSrcInetAddr,
       "mpegInputUdpOriginationDestInetAddr": mpegInputUdpOriginationDestInetAddr,
       "mpegInputUdpOriginationDestPort": mpegInputUdpOriginationDestPort,
       "mpegInputUdpOriginationActive": mpegInputUdpOriginationActive,
       "mpegInputUdpOriginationPacketsDetected": mpegInputUdpOriginationPacketsDetected,
       "mpegInputUdpOriginationRank": mpegInputUdpOriginationRank,
       "mpegInputUdpOriginationInputTSIndex": mpegInputUdpOriginationInputTSIndex,
       "mpegOutputs": mpegOutputs,
       "mpegInsertPacketTable": mpegInsertPacketTable,
       "mpegInsertPacketEntry": mpegInsertPacketEntry,
       "mpegInsertPacketIndex": mpegInsertPacketIndex,
       "mpegInsertPacketListId": mpegInsertPacketListId,
       "mpegInsertPacketImmediateExecution": mpegInsertPacketImmediateExecution,
       "mpegInsertPacketStartTime": mpegInsertPacketStartTime,
       "mpegInsertPacketRepeat": mpegInsertPacketRepeat,
       "mpegInsertPacketContinuousFlag": mpegInsertPacketContinuousFlag,
       "mpegInsertPacketRate": mpegInsertPacketRate,
       "mpegInsertPacketDeviceIfIndex": mpegInsertPacketDeviceIfIndex,
       "mpegOutputStatsTable": mpegOutputStatsTable,
       "mpegOutputStatsEntry": mpegOutputStatsEntry,
       "mpegOutputStatsDroppedPackets": mpegOutputStatsDroppedPackets,
       "mpegOutputStatsFifoOverflow": mpegOutputStatsFifoOverflow,
       "mpegOutputStatsFifoUnderflow": mpegOutputStatsFifoUnderflow,
       "mpegOutputStatsDataRate": mpegOutputStatsDataRate,
       "mpegOutputStatsAvailableBandwidth": mpegOutputStatsAvailableBandwidth,
       "mpegOutputStatsChannelUtilization": mpegOutputStatsChannelUtilization,
       "mpegOutputStatsTotalPackets": mpegOutputStatsTotalPackets,
       "mpegOutputTSTable": mpegOutputTSTable,
       "mpegOutputTSEntry": mpegOutputTSEntry,
       "mpegOutputTSIndex": mpegOutputTSIndex,
       "mpegOutputTSType": mpegOutputTSType,
       "mpegOutputTSConnectionType": mpegOutputTSConnectionType,
       "mpegOutputTSConnection": mpegOutputTSConnection,
       "mpegOutputTSNumPrograms": mpegOutputTSNumPrograms,
       "mpegOutputTSTSID": mpegOutputTSTSID,
       "mpegOutputTSNitPid": mpegOutputTSNitPid,
       "mpegOutputTSCaPid": mpegOutputTSCaPid,
       "mpegOutputTSCatInsertRate": mpegOutputTSCatInsertRate,
       "mpegOutputTSPatInsertRate": mpegOutputTSPatInsertRate,
       "mpegOutputTSPmtInsertRate": mpegOutputTSPmtInsertRate,
       "mpegOutputTSStartTime": mpegOutputTSStartTime,
       "mpegOutputProgTable": mpegOutputProgTable,
       "mpegOutputProgEntry": mpegOutputProgEntry,
       "mpegOutputProgIndex": mpegOutputProgIndex,
       "mpegOutputProgNo": mpegOutputProgNo,
       "mpegOutputProgPmtVersion": mpegOutputProgPmtVersion,
       "mpegOutputProgPmtPid": mpegOutputProgPmtPid,
       "mpegOutputProgPcrPid": mpegOutputProgPcrPid,
       "mpegOutputProgEcmPid": mpegOutputProgEcmPid,
       "mpegOutputProgNumElems": mpegOutputProgNumElems,
       "mpegOutputProgNumEcms": mpegOutputProgNumEcms,
       "mpegOutputProgCaDescr": mpegOutputProgCaDescr,
       "mpegOutputProgScte35Descr": mpegOutputProgScte35Descr,
       "mpegOutputProgScte18Descr": mpegOutputProgScte18Descr,
       "mpegOutputProgElemStatsTable": mpegOutputProgElemStatsTable,
       "mpegOutputProgElemStatsEntry": mpegOutputProgElemStatsEntry,
       "mpegOutputProgElemStatsIndex": mpegOutputProgElemStatsIndex,
       "mpegOutputProgElemStatsPid": mpegOutputProgElemStatsPid,
       "mpegOutputProgElemStatsElemType": mpegOutputProgElemStatsElemType,
       "mpegOutputProgElemStatsDataRate": mpegOutputProgElemStatsDataRate,
       "mpegOutputUdpDestinationTable": mpegOutputUdpDestinationTable,
       "mpegOutputUdpDestinationEntry": mpegOutputUdpDestinationEntry,
       "mpegOutputUdpDestinationIndex": mpegOutputUdpDestinationIndex,
       "mpegOutputUdpDestinationId": mpegOutputUdpDestinationId,
       "mpegOutputUdpDestinationIfIndex": mpegOutputUdpDestinationIfIndex,
       "mpegOutputUdpDestinationInetAddrType": mpegOutputUdpDestinationInetAddrType,
       "mpegOutputUdpDestinationSrcInetAddr": mpegOutputUdpDestinationSrcInetAddr,
       "mpegOutputUdpDestinationDestInetAddr": mpegOutputUdpDestinationDestInetAddr,
       "mpegOutputUdpDestinationDestPort": mpegOutputUdpDestinationDestPort,
       "mpegOutputUdpDestinationOutputTSIndex": mpegOutputUdpDestinationOutputTSIndex,
       "mpegProgramMappingTable": mpegProgramMappingTable,
       "mpegProgramMappingEntry": mpegProgramMappingEntry,
       "mpegProgramMappingIndex": mpegProgramMappingIndex,
       "mpegProgramMappingOutputProgIndex": mpegProgramMappingOutputProgIndex,
       "mpegProgramMappingOutputTSIndex": mpegProgramMappingOutputTSIndex,
       "mpegProgramMappingInputProgIndex": mpegProgramMappingInputProgIndex,
       "mpegProgramMappingInputTSIndex": mpegProgramMappingInputTSIndex,
       "mpegVideoSessionTable": mpegVideoSessionTable,
       "mpegVideoSessionEntry": mpegVideoSessionEntry,
       "mpegVideoSessionIndex": mpegVideoSessionIndex,
       "mpegVideoSessionPhyMappingIndex": mpegVideoSessionPhyMappingIndex,
       "mpegVideoSessionPIDRemap": mpegVideoSessionPIDRemap,
       "mpegVideoSessionMode": mpegVideoSessionMode,
       "mpegVideoSessionState": mpegVideoSessionState,
       "mpegVideoSessionProvMethod": mpegVideoSessionProvMethod,
       "mpegVideoSessionEncryptionType": mpegVideoSessionEncryptionType,
       "mpegVideoSessionEncryptionInfo": mpegVideoSessionEncryptionInfo,
       "mpegVideoSessionBitRate": mpegVideoSessionBitRate,
       "mpegVideoSessionID": mpegVideoSessionID,
       "mpegVideoSessionSelectedInput": mpegVideoSessionSelectedInput,
       "mpegVideoSessionSelectedOutput": mpegVideoSessionSelectedOutput,
       "mpegVideoSessionPtrTable": mpegVideoSessionPtrTable,
       "mpegVideoSessionPtrEntry": mpegVideoSessionPtrEntry,
       "mpegVideoSessionPtrInputProgIndex": mpegVideoSessionPtrInputProgIndex,
       "mpegVideoSessionPtrInputTSIndex": mpegVideoSessionPtrInputTSIndex,
       "mpegVideoSessionPtrInputTSConnType": mpegVideoSessionPtrInputTSConnType,
       "mpegVideoSessionPtrInputTSConnection": mpegVideoSessionPtrInputTSConnection,
       "mpegVideoSessionPtrOutputProgIndex": mpegVideoSessionPtrOutputProgIndex,
       "mpegVideoSessionPtrOutputTSIndex": mpegVideoSessionPtrOutputTSIndex,
       "mpegVideoSessionPtrOutputTSConnType": mpegVideoSessionPtrOutputTSConnType,
       "mpegVideoSessionPtrOutputTSConnection": mpegVideoSessionPtrOutputTSConnection,
       "mpegVideoSessionPtrStatus": mpegVideoSessionPtrStatus,
       "mpegInputTSOutputSessionTable": mpegInputTSOutputSessionTable,
       "mpegInputTSOutputSessionEntry": mpegInputTSOutputSessionEntry,
       "mpegInputTSOutputSessionCreateTime": mpegInputTSOutputSessionCreateTime,
       "mpegMIBConformance": mpegMIBConformance,
       "mpegMIBCompliances": mpegMIBCompliances,
       "mpegSupport": mpegSupport,
       "mpegMIBGroups": mpegMIBGroups,
       "mpegInputGroup": mpegInputGroup,
       "mpegInputProgESGroup": mpegInputProgESGroup,
       "mpegOutputGroup": mpegOutputGroup,
       "mpegOutputProgElemStatsGroup": mpegOutputProgElemStatsGroup,
       "mpegMappingsGroup": mpegMappingsGroup,
       "mpegSessionsGroup": mpegSessionsGroup}
)
