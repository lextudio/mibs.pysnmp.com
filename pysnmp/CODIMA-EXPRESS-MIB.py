# SNMP MIB module (CODIMA-EXPRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CODIMA-EXPRESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:07 2024
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

(codimaProducts,) = mibBuilder.importSymbols(
    "CODIMA-GLOBAL-REG",
    "codimaProducts")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

codimaExpressMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2)
)
codimaExpressMIB.setRevisions(
        ("2003-05-30 09:59",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CodimaExpressObjects_ObjectIdentity = ObjectIdentity
codimaExpressObjects = _CodimaExpressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1)
)
if mibBuilder.loadTexts:
    codimaExpressObjects.setStatus("current")
_ExpHistoryDatabases_ObjectIdentity = ObjectIdentity
expHistoryDatabases = _ExpHistoryDatabases_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    expHistoryDatabases.setStatus("current")
_DbControl_ObjectIdentity = ObjectIdentity
dbControl = _DbControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dbControl.setStatus("current")
_CtrlTimeTable_Object = MibTable
ctrlTimeTable = _CtrlTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ctrlTimeTable.setStatus("current")
_CtrlTimeEntry_Object = MibTableRow
ctrlTimeEntry = _CtrlTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 1, 1, 1)
)
ctrlTimeEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "ctSampleType"),
)
if mibBuilder.loadTexts:
    ctrlTimeEntry.setStatus("current")


class _CtSampleType_Type(Integer32):
    """Custom type ctSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("longTerm", 1),
          ("shortTerm", 2))
    )


_CtSampleType_Type.__name__ = "Integer32"
_CtSampleType_Object = MibTableColumn
ctSampleType = _CtSampleType_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 1, 1, 1, 1),
    _CtSampleType_Type()
)
ctSampleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctSampleType.setStatus("current")


class _CtTimeSlots_Type(Integer32):
    """Custom type ctTimeSlots based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CtTimeSlots_Type.__name__ = "Integer32"
_CtTimeSlots_Object = MibTableColumn
ctTimeSlots = _CtTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 1, 1, 1, 2),
    _CtTimeSlots_Type()
)
ctTimeSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTimeSlots.setStatus("current")


class _CtLockMethod_Type(Integer32):
    """Custom type ctLockMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockRealTime", 2),
          ("lockUserTime", 1))
    )


_CtLockMethod_Type.__name__ = "Integer32"
_CtLockMethod_Object = MibTableColumn
ctLockMethod = _CtLockMethod_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 1, 1, 1, 3),
    _CtLockMethod_Type()
)
ctLockMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctLockMethod.setStatus("current")
_CtLockUserTime_Type = DisplayString
_CtLockUserTime_Object = MibTableColumn
ctLockUserTime = _CtLockUserTime_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 1, 1, 1, 4),
    _CtLockUserTime_Type()
)
ctLockUserTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctLockUserTime.setStatus("current")


class _CtLockRealTime_Type(DisplayString):
    """Custom type ctLockRealTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_CtLockRealTime_Type.__name__ = "DisplayString"
_CtLockRealTime_Object = MibTableColumn
ctLockRealTime = _CtLockRealTime_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 1, 1, 1, 5),
    _CtLockRealTime_Type()
)
ctLockRealTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctLockRealTime.setStatus("current")
_DbSegment_ObjectIdentity = ObjectIdentity
dbSegment = _DbSegment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dbSegment.setStatus("current")
_SegLongTerm_ObjectIdentity = ObjectIdentity
segLongTerm = _SegLongTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    segLongTerm.setStatus("current")
_SlBaseTable_Object = MibTable
slBaseTable = _SlBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    slBaseTable.setStatus("current")
_SlBaseEntry_Object = MibTableRow
slBaseEntry = _SlBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 1, 1)
)
slBaseEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "slbTimeStampIndex"),
)
if mibBuilder.loadTexts:
    slBaseEntry.setStatus("current")
_SlbTimeStampIndex_Type = Unsigned32
_SlbTimeStampIndex_Object = MibTableColumn
slbTimeStampIndex = _SlbTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 1, 1, 1),
    _SlbTimeStampIndex_Type()
)
slbTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbTimeStampIndex.setStatus("current")


class _SlbTimeStamp_Type(DisplayString):
    """Custom type slbTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SlbTimeStamp_Type.__name__ = "DisplayString"
_SlbTimeStamp_Object = MibTableColumn
slbTimeStamp = _SlbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 1, 1, 2),
    _SlbTimeStamp_Type()
)
slbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbTimeStamp.setStatus("current")
_SlbFrames_Type = Counter32
_SlbFrames_Object = MibTableColumn
slbFrames = _SlbFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 1, 1, 3),
    _SlbFrames_Type()
)
slbFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFrames.setStatus("current")
_SlbBytes_Type = Counter32
_SlbBytes_Object = MibTableColumn
slbBytes = _SlbBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 1, 1, 4),
    _SlbBytes_Type()
)
slbBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbBytes.setStatus("current")
_SlbFrameSize_Type = Gauge32
_SlbFrameSize_Object = MibTableColumn
slbFrameSize = _SlbFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 1, 1, 5),
    _SlbFrameSize_Type()
)
slbFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    slbFrameSize.setUnits("bytes")
_SlbHardwareErrors_Type = Counter32
_SlbHardwareErrors_Object = MibTableColumn
slbHardwareErrors = _SlbHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 1, 1, 6),
    _SlbHardwareErrors_Type()
)
slbHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbHardwareErrors.setStatus("current")
_SlbSoftwareErrors_Type = Counter32
_SlbSoftwareErrors_Object = MibTableColumn
slbSoftwareErrors = _SlbSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 1, 1, 7),
    _SlbSoftwareErrors_Type()
)
slbSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSoftwareErrors.setStatus("current")
_SlbActiveNodes_Type = Gauge32
_SlbActiveNodes_Object = MibTableColumn
slbActiveNodes = _SlbActiveNodes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 1, 1, 8),
    _SlbActiveNodes_Type()
)
slbActiveNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbActiveNodes.setStatus("current")
_SlBroadcastTable_Object = MibTable
slBroadcastTable = _SlBroadcastTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    slBroadcastTable.setStatus("current")
_SlBroadcastEntry_Object = MibTableRow
slBroadcastEntry = _SlBroadcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 2, 1)
)
slBroadcastEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "slbcTimeStampIndex"),
)
if mibBuilder.loadTexts:
    slBroadcastEntry.setStatus("current")
_SlbcTimeStampIndex_Type = Unsigned32
_SlbcTimeStampIndex_Object = MibTableColumn
slbcTimeStampIndex = _SlbcTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 2, 1, 1),
    _SlbcTimeStampIndex_Type()
)
slbcTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbcTimeStampIndex.setStatus("current")


class _SlbcTimeStamp_Type(DisplayString):
    """Custom type slbcTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SlbcTimeStamp_Type.__name__ = "DisplayString"
_SlbcTimeStamp_Object = MibTableColumn
slbcTimeStamp = _SlbcTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 2, 1, 2),
    _SlbcTimeStamp_Type()
)
slbcTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbcTimeStamp.setStatus("current")
_SlbcBytes_Type = Counter32
_SlbcBytes_Object = MibTableColumn
slbcBytes = _SlbcBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 2, 1, 3),
    _SlbcBytes_Type()
)
slbcBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbcBytes.setStatus("current")
_SlbcPercentBytes_Type = Gauge32
_SlbcPercentBytes_Object = MibTableColumn
slbcPercentBytes = _SlbcPercentBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 2, 1, 4),
    _SlbcPercentBytes_Type()
)
slbcPercentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbcPercentBytes.setStatus("current")
_SlbcFrames_Type = Counter32
_SlbcFrames_Object = MibTableColumn
slbcFrames = _SlbcFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 2, 1, 5),
    _SlbcFrames_Type()
)
slbcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbcFrames.setStatus("current")
_SlbcPercentFrames_Type = Gauge32
_SlbcPercentFrames_Object = MibTableColumn
slbcPercentFrames = _SlbcPercentFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 2, 1, 6),
    _SlbcPercentFrames_Type()
)
slbcPercentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbcPercentFrames.setStatus("current")
_SlDerivedTable_Object = MibTable
slDerivedTable = _SlDerivedTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    slDerivedTable.setStatus("current")
_SlDerivedEntry_Object = MibTableRow
slDerivedEntry = _SlDerivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 3, 1)
)
slDerivedEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "sldTimeStampIndex"),
)
if mibBuilder.loadTexts:
    slDerivedEntry.setStatus("current")
_SldTimeStampIndex_Type = Unsigned32
_SldTimeStampIndex_Object = MibTableColumn
sldTimeStampIndex = _SldTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 3, 1, 1),
    _SldTimeStampIndex_Type()
)
sldTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sldTimeStampIndex.setStatus("current")


class _SldTimeStamp_Type(DisplayString):
    """Custom type sldTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SldTimeStamp_Type.__name__ = "DisplayString"
_SldTimeStamp_Object = MibTableColumn
sldTimeStamp = _SldTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 3, 1, 2),
    _SldTimeStamp_Type()
)
sldTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sldTimeStamp.setStatus("current")
_SldUtilization_Type = Gauge32
_SldUtilization_Object = MibTableColumn
sldUtilization = _SldUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 3, 1, 3),
    _SldUtilization_Type()
)
sldUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sldUtilization.setStatus("current")
_SldErrorFrames_Type = Gauge32
_SldErrorFrames_Object = MibTableColumn
sldErrorFrames = _SldErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 3, 1, 4),
    _SldErrorFrames_Type()
)
sldErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sldErrorFrames.setStatus("current")
_SlEthernetTable_Object = MibTable
slEthernetTable = _SlEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    slEthernetTable.setStatus("current")
_SlEthernetEntry_Object = MibTableRow
slEthernetEntry = _SlEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 4, 1)
)
slEthernetEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "sleTimeStampIndex"),
)
if mibBuilder.loadTexts:
    slEthernetEntry.setStatus("current")
_SleTimeStampIndex_Type = Unsigned32
_SleTimeStampIndex_Object = MibTableColumn
sleTimeStampIndex = _SleTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 4, 1, 1),
    _SleTimeStampIndex_Type()
)
sleTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTimeStampIndex.setStatus("current")


class _SleTimeStamp_Type(DisplayString):
    """Custom type sleTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SleTimeStamp_Type.__name__ = "DisplayString"
_SleTimeStamp_Object = MibTableColumn
sleTimeStamp = _SleTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 4, 1, 2),
    _SleTimeStamp_Type()
)
sleTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTimeStamp.setStatus("current")
_SleRunts_Type = Counter32
_SleRunts_Object = MibTableColumn
sleRunts = _SleRunts_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 4, 1, 3),
    _SleRunts_Type()
)
sleRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRunts.setStatus("current")
_SleJabbers_Type = Counter32
_SleJabbers_Object = MibTableColumn
sleJabbers = _SleJabbers_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 4, 1, 4),
    _SleJabbers_Type()
)
sleJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleJabbers.setStatus("current")
_SleCrc_Type = Counter32
_SleCrc_Object = MibTableColumn
sleCrc = _SleCrc_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 4, 1, 5),
    _SleCrc_Type()
)
sleCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCrc.setStatus("current")
_SleCollisions_Type = Counter32
_SleCollisions_Object = MibTableColumn
sleCollisions = _SleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 4, 1, 6),
    _SleCollisions_Type()
)
sleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCollisions.setStatus("current")
_SleLateCollisions_Type = Counter32
_SleLateCollisions_Object = MibTableColumn
sleLateCollisions = _SleLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 4, 1, 7),
    _SleLateCollisions_Type()
)
sleLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLateCollisions.setStatus("current")
_SlIcmpTable_Object = MibTable
slIcmpTable = _SlIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    slIcmpTable.setStatus("current")
_SlIcmpEntry_Object = MibTableRow
slIcmpEntry = _SlIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1)
)
slIcmpEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "sliTimeStampIndex"),
)
if mibBuilder.loadTexts:
    slIcmpEntry.setStatus("current")
_SliTimeStampIndex_Type = Unsigned32
_SliTimeStampIndex_Object = MibTableColumn
sliTimeStampIndex = _SliTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 1),
    _SliTimeStampIndex_Type()
)
sliTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliTimeStampIndex.setStatus("current")


class _SliTimeStamp_Type(DisplayString):
    """Custom type sliTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SliTimeStamp_Type.__name__ = "DisplayString"
_SliTimeStamp_Object = MibTableColumn
sliTimeStamp = _SliTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 2),
    _SliTimeStamp_Type()
)
sliTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliTimeStamp.setStatus("current")
_SliPing_Type = Counter32
_SliPing_Object = MibTableColumn
sliPing = _SliPing_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 3),
    _SliPing_Type()
)
sliPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliPing.setStatus("current")
_SliSrcQuench_Type = Counter32
_SliSrcQuench_Object = MibTableColumn
sliSrcQuench = _SliSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 4),
    _SliSrcQuench_Type()
)
sliSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliSrcQuench.setStatus("current")
_SliRedirect_Type = Counter32
_SliRedirect_Object = MibTableColumn
sliRedirect = _SliRedirect_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 5),
    _SliRedirect_Type()
)
sliRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliRedirect.setStatus("current")
_SliTtlExceeded_Type = Counter32
_SliTtlExceeded_Object = MibTableColumn
sliTtlExceeded = _SliTtlExceeded_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 6),
    _SliTtlExceeded_Type()
)
sliTtlExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliTtlExceeded.setStatus("current")
_SliParamProblem_Type = Counter32
_SliParamProblem_Object = MibTableColumn
sliParamProblem = _SliParamProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 7),
    _SliParamProblem_Type()
)
sliParamProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliParamProblem.setStatus("current")
_SliTimestamp_Type = Counter32
_SliTimestamp_Object = MibTableColumn
sliTimestamp = _SliTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 8),
    _SliTimestamp_Type()
)
sliTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliTimestamp.setStatus("current")
_SliFragTimeout_Type = Counter32
_SliFragTimeout_Object = MibTableColumn
sliFragTimeout = _SliFragTimeout_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 9),
    _SliFragTimeout_Type()
)
sliFragTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliFragTimeout.setStatus("current")
_SliNetUnreachable_Type = Counter32
_SliNetUnreachable_Object = MibTableColumn
sliNetUnreachable = _SliNetUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 10),
    _SliNetUnreachable_Type()
)
sliNetUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliNetUnreachable.setStatus("current")
_SliHostUnreachable_Type = Counter32
_SliHostUnreachable_Object = MibTableColumn
sliHostUnreachable = _SliHostUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 11),
    _SliHostUnreachable_Type()
)
sliHostUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliHostUnreachable.setStatus("current")
_SliProtocolUnreachable_Type = Counter32
_SliProtocolUnreachable_Object = MibTableColumn
sliProtocolUnreachable = _SliProtocolUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 12),
    _SliProtocolUnreachable_Type()
)
sliProtocolUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliProtocolUnreachable.setStatus("current")
_SliPortUnreachable_Type = Counter32
_SliPortUnreachable_Object = MibTableColumn
sliPortUnreachable = _SliPortUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 13),
    _SliPortUnreachable_Type()
)
sliPortUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliPortUnreachable.setStatus("current")
_SliFragRequired_Type = Counter32
_SliFragRequired_Object = MibTableColumn
sliFragRequired = _SliFragRequired_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 14),
    _SliFragRequired_Type()
)
sliFragRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliFragRequired.setStatus("current")
_SliSrcRouteFail_Type = Counter32
_SliSrcRouteFail_Object = MibTableColumn
sliSrcRouteFail = _SliSrcRouteFail_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 15),
    _SliSrcRouteFail_Type()
)
sliSrcRouteFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliSrcRouteFail.setStatus("current")
_SliDestNetUnknown_Type = Counter32
_SliDestNetUnknown_Object = MibTableColumn
sliDestNetUnknown = _SliDestNetUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 16),
    _SliDestNetUnknown_Type()
)
sliDestNetUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliDestNetUnknown.setStatus("current")
_SliDestHostUnknown_Type = Counter32
_SliDestHostUnknown_Object = MibTableColumn
sliDestHostUnknown = _SliDestHostUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 17),
    _SliDestHostUnknown_Type()
)
sliDestHostUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliDestHostUnknown.setStatus("current")
_SliSrcHostIsolated_Type = Counter32
_SliSrcHostIsolated_Object = MibTableColumn
sliSrcHostIsolated = _SliSrcHostIsolated_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 18),
    _SliSrcHostIsolated_Type()
)
sliSrcHostIsolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliSrcHostIsolated.setStatus("current")
_SliNetProhibited_Type = Counter32
_SliNetProhibited_Object = MibTableColumn
sliNetProhibited = _SliNetProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 19),
    _SliNetProhibited_Type()
)
sliNetProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliNetProhibited.setStatus("current")
_SliHostProhibited_Type = Counter32
_SliHostProhibited_Object = MibTableColumn
sliHostProhibited = _SliHostProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 20),
    _SliHostProhibited_Type()
)
sliHostProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliHostProhibited.setStatus("current")
_SliNetTosUnreachable_Type = Counter32
_SliNetTosUnreachable_Object = MibTableColumn
sliNetTosUnreachable = _SliNetTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 21),
    _SliNetTosUnreachable_Type()
)
sliNetTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliNetTosUnreachable.setStatus("current")
_SliHostTosUnreachable_Type = Counter32
_SliHostTosUnreachable_Object = MibTableColumn
sliHostTosUnreachable = _SliHostTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 22),
    _SliHostTosUnreachable_Type()
)
sliHostTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliHostTosUnreachable.setStatus("current")
_SliPerformance_Type = Counter32
_SliPerformance_Object = MibTableColumn
sliPerformance = _SliPerformance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 23),
    _SliPerformance_Type()
)
sliPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliPerformance.setStatus("current")
_SliNetRouteProblem_Type = Counter32
_SliNetRouteProblem_Object = MibTableColumn
sliNetRouteProblem = _SliNetRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 24),
    _SliNetRouteProblem_Type()
)
sliNetRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliNetRouteProblem.setStatus("current")
_SliHostRouteProblem_Type = Counter32
_SliHostRouteProblem_Object = MibTableColumn
sliHostRouteProblem = _SliHostRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 25),
    _SliHostRouteProblem_Type()
)
sliHostRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliHostRouteProblem.setStatus("current")
_SliAppRouteProblem_Type = Counter32
_SliAppRouteProblem_Object = MibTableColumn
sliAppRouteProblem = _SliAppRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 26),
    _SliAppRouteProblem_Type()
)
sliAppRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliAppRouteProblem.setStatus("current")
_SliRouteChange_Type = Counter32
_SliRouteChange_Object = MibTableColumn
sliRouteChange = _SliRouteChange_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 27),
    _SliRouteChange_Type()
)
sliRouteChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliRouteChange.setStatus("current")
_SliGrpErrors_Type = Counter32
_SliGrpErrors_Object = MibTableColumn
sliGrpErrors = _SliGrpErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 28),
    _SliGrpErrors_Type()
)
sliGrpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliGrpErrors.setStatus("current")
_SliMaintenance_Type = Counter32
_SliMaintenance_Object = MibTableColumn
sliMaintenance = _SliMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 5, 1, 29),
    _SliMaintenance_Type()
)
sliMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sliMaintenance.setStatus("current")
_SlPortTable_Object = MibTable
slPortTable = _SlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    slPortTable.setStatus("current")
_SlPortEntry_Object = MibTableRow
slPortEntry = _SlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1)
)
slPortEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "slp1TimeStampIndex"),
)
if mibBuilder.loadTexts:
    slPortEntry.setStatus("current")
_Slp1TimeStampIndex_Type = Unsigned32
_Slp1TimeStampIndex_Object = MibTableColumn
slp1TimeStampIndex = _Slp1TimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 1),
    _Slp1TimeStampIndex_Type()
)
slp1TimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1TimeStampIndex.setStatus("current")


class _Slp1TimeStamp_Type(DisplayString):
    """Custom type slp1TimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_Slp1TimeStamp_Type.__name__ = "DisplayString"
_Slp1TimeStamp_Object = MibTableColumn
slp1TimeStamp = _Slp1TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 2),
    _Slp1TimeStamp_Type()
)
slp1TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1TimeStamp.setStatus("current")
_Slp1Frames_Type = Counter32
_Slp1Frames_Object = MibTableColumn
slp1Frames = _Slp1Frames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 3),
    _Slp1Frames_Type()
)
slp1Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1Frames.setStatus("current")
_Slp1Bytes_Type = Counter32
_Slp1Bytes_Object = MibTableColumn
slp1Bytes = _Slp1Bytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 4),
    _Slp1Bytes_Type()
)
slp1Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1Bytes.setStatus("current")
_Slp1FrameSize_Type = Gauge32
_Slp1FrameSize_Object = MibTableColumn
slp1FrameSize = _Slp1FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 5),
    _Slp1FrameSize_Type()
)
slp1FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1FrameSize.setStatus("current")
if mibBuilder.loadTexts:
    slp1FrameSize.setUnits("bytes")
_Slp1Utilization_Type = Gauge32
_Slp1Utilization_Object = MibTableColumn
slp1Utilization = _Slp1Utilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 6),
    _Slp1Utilization_Type()
)
slp1Utilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1Utilization.setStatus("current")
_Slp1LineSpeed_Type = Gauge32
_Slp1LineSpeed_Object = MibTableColumn
slp1LineSpeed = _Slp1LineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 7),
    _Slp1LineSpeed_Type()
)
slp1LineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1LineSpeed.setStatus("current")
if mibBuilder.loadTexts:
    slp1LineSpeed.setUnits("bits per second")
_Slp1SoftErrors_Type = Counter32
_Slp1SoftErrors_Object = MibTableColumn
slp1SoftErrors = _Slp1SoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 8),
    _Slp1SoftErrors_Type()
)
slp1SoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1SoftErrors.setStatus("current")
_Slp1Runts_Type = Counter32
_Slp1Runts_Object = MibTableColumn
slp1Runts = _Slp1Runts_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 9),
    _Slp1Runts_Type()
)
slp1Runts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1Runts.setStatus("current")
_Slp1Jabbers_Type = Counter32
_Slp1Jabbers_Object = MibTableColumn
slp1Jabbers = _Slp1Jabbers_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 10),
    _Slp1Jabbers_Type()
)
slp1Jabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1Jabbers.setStatus("current")
_Slp1Crc_Type = Counter32
_Slp1Crc_Object = MibTableColumn
slp1Crc = _Slp1Crc_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 11),
    _Slp1Crc_Type()
)
slp1Crc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1Crc.setStatus("current")
_Slp1Collisions_Type = Counter32
_Slp1Collisions_Object = MibTableColumn
slp1Collisions = _Slp1Collisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 12),
    _Slp1Collisions_Type()
)
slp1Collisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1Collisions.setStatus("current")
_Slp1LateCollisions_Type = Counter32
_Slp1LateCollisions_Object = MibTableColumn
slp1LateCollisions = _Slp1LateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 13),
    _Slp1LateCollisions_Type()
)
slp1LateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1LateCollisions.setStatus("current")
_Slp1LineNoise_Type = Counter32
_Slp1LineNoise_Object = MibTableColumn
slp1LineNoise = _Slp1LineNoise_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 14),
    _Slp1LineNoise_Type()
)
slp1LineNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1LineNoise.setStatus("current")
_Slp2Frames_Type = Counter32
_Slp2Frames_Object = MibTableColumn
slp2Frames = _Slp2Frames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 15),
    _Slp2Frames_Type()
)
slp2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp2Frames.setStatus("current")
_Slp2Bytes_Type = Counter32
_Slp2Bytes_Object = MibTableColumn
slp2Bytes = _Slp2Bytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 16),
    _Slp2Bytes_Type()
)
slp2Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp2Bytes.setStatus("current")
_Slp2FrameSize_Type = Gauge32
_Slp2FrameSize_Object = MibTableColumn
slp2FrameSize = _Slp2FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 17),
    _Slp2FrameSize_Type()
)
slp2FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp2FrameSize.setStatus("current")
if mibBuilder.loadTexts:
    slp2FrameSize.setUnits("bytes")
_Slp2Utilization_Type = Gauge32
_Slp2Utilization_Object = MibTableColumn
slp2Utilization = _Slp2Utilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 18),
    _Slp2Utilization_Type()
)
slp2Utilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp2Utilization.setStatus("current")
_Slp2LineSpeed_Type = Gauge32
_Slp2LineSpeed_Object = MibTableColumn
slp2LineSpeed = _Slp2LineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 19),
    _Slp2LineSpeed_Type()
)
slp2LineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp2LineSpeed.setStatus("current")
if mibBuilder.loadTexts:
    slp2LineSpeed.setUnits("bits per second")
_Slp2SoftErrors_Type = Counter32
_Slp2SoftErrors_Object = MibTableColumn
slp2SoftErrors = _Slp2SoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 20),
    _Slp2SoftErrors_Type()
)
slp2SoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp2SoftErrors.setStatus("current")
_Slp2Runts_Type = Counter32
_Slp2Runts_Object = MibTableColumn
slp2Runts = _Slp2Runts_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 21),
    _Slp2Runts_Type()
)
slp2Runts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp2Runts.setStatus("current")
_Slp2Jabbers_Type = Counter32
_Slp2Jabbers_Object = MibTableColumn
slp2Jabbers = _Slp2Jabbers_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 22),
    _Slp2Jabbers_Type()
)
slp2Jabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp2Jabbers.setStatus("current")
_Slp2Crc_Type = Counter32
_Slp2Crc_Object = MibTableColumn
slp2Crc = _Slp2Crc_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 23),
    _Slp2Crc_Type()
)
slp2Crc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp2Crc.setStatus("current")
_Slp2Collisions_Type = Counter32
_Slp2Collisions_Object = MibTableColumn
slp2Collisions = _Slp2Collisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 24),
    _Slp2Collisions_Type()
)
slp2Collisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp2Collisions.setStatus("current")
_Slp2LateCollisions_Type = Counter32
_Slp2LateCollisions_Object = MibTableColumn
slp2LateCollisions = _Slp2LateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 25),
    _Slp2LateCollisions_Type()
)
slp2LateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp2LateCollisions.setStatus("current")
_Slp2LineNoise_Type = Counter32
_Slp2LineNoise_Object = MibTableColumn
slp2LineNoise = _Slp2LineNoise_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 1, 6, 1, 26),
    _Slp2LineNoise_Type()
)
slp2LineNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp2LineNoise.setStatus("current")
_SegShortTerm_ObjectIdentity = ObjectIdentity
segShortTerm = _SegShortTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    segShortTerm.setStatus("current")
_SsBaseTable_Object = MibTable
ssBaseTable = _SsBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ssBaseTable.setStatus("current")
_SsBaseEntry_Object = MibTableRow
ssBaseEntry = _SsBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 1, 1)
)
ssBaseEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "ssbTimeStampIndex"),
)
if mibBuilder.loadTexts:
    ssBaseEntry.setStatus("current")
_SsbTimeStampIndex_Type = Unsigned32
_SsbTimeStampIndex_Object = MibTableColumn
ssbTimeStampIndex = _SsbTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 1, 1, 1),
    _SsbTimeStampIndex_Type()
)
ssbTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbTimeStampIndex.setStatus("current")


class _SsbTimeStamp_Type(DisplayString):
    """Custom type ssbTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SsbTimeStamp_Type.__name__ = "DisplayString"
_SsbTimeStamp_Object = MibTableColumn
ssbTimeStamp = _SsbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 1, 1, 2),
    _SsbTimeStamp_Type()
)
ssbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbTimeStamp.setStatus("current")
_SsbFrames_Type = Counter32
_SsbFrames_Object = MibTableColumn
ssbFrames = _SsbFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 1, 1, 3),
    _SsbFrames_Type()
)
ssbFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbFrames.setStatus("current")
_SsbBytes_Type = Counter32
_SsbBytes_Object = MibTableColumn
ssbBytes = _SsbBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 1, 1, 4),
    _SsbBytes_Type()
)
ssbBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbBytes.setStatus("current")
_SsbFrameSize_Type = Gauge32
_SsbFrameSize_Object = MibTableColumn
ssbFrameSize = _SsbFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 1, 1, 5),
    _SsbFrameSize_Type()
)
ssbFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    ssbFrameSize.setUnits("bytes")
_SsbHardwareErrors_Type = Counter32
_SsbHardwareErrors_Object = MibTableColumn
ssbHardwareErrors = _SsbHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 1, 1, 6),
    _SsbHardwareErrors_Type()
)
ssbHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbHardwareErrors.setStatus("current")
_SsbSoftwareErrors_Type = Counter32
_SsbSoftwareErrors_Object = MibTableColumn
ssbSoftwareErrors = _SsbSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 1, 1, 7),
    _SsbSoftwareErrors_Type()
)
ssbSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbSoftwareErrors.setStatus("current")
_SsbActiveNodes_Type = Gauge32
_SsbActiveNodes_Object = MibTableColumn
ssbActiveNodes = _SsbActiveNodes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 1, 1, 8),
    _SsbActiveNodes_Type()
)
ssbActiveNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbActiveNodes.setStatus("current")
_SsBroadcastTable_Object = MibTable
ssBroadcastTable = _SsBroadcastTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ssBroadcastTable.setStatus("current")
_SsBroadcastEntry_Object = MibTableRow
ssBroadcastEntry = _SsBroadcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 2, 1)
)
ssBroadcastEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "ssbcTimeStampIndex"),
)
if mibBuilder.loadTexts:
    ssBroadcastEntry.setStatus("current")
_SsbcTimeStampIndex_Type = Unsigned32
_SsbcTimeStampIndex_Object = MibTableColumn
ssbcTimeStampIndex = _SsbcTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 2, 1, 1),
    _SsbcTimeStampIndex_Type()
)
ssbcTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbcTimeStampIndex.setStatus("current")


class _SsbcTimeStamp_Type(DisplayString):
    """Custom type ssbcTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SsbcTimeStamp_Type.__name__ = "DisplayString"
_SsbcTimeStamp_Object = MibTableColumn
ssbcTimeStamp = _SsbcTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 2, 1, 2),
    _SsbcTimeStamp_Type()
)
ssbcTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbcTimeStamp.setStatus("current")
_SsbcBytes_Type = Counter32
_SsbcBytes_Object = MibTableColumn
ssbcBytes = _SsbcBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 2, 1, 3),
    _SsbcBytes_Type()
)
ssbcBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbcBytes.setStatus("current")
_SsbcBytesPercent_Type = Gauge32
_SsbcBytesPercent_Object = MibTableColumn
ssbcBytesPercent = _SsbcBytesPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 2, 1, 4),
    _SsbcBytesPercent_Type()
)
ssbcBytesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbcBytesPercent.setStatus("current")
_SsbcFrames_Type = Counter32
_SsbcFrames_Object = MibTableColumn
ssbcFrames = _SsbcFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 2, 1, 5),
    _SsbcFrames_Type()
)
ssbcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbcFrames.setStatus("current")
_SsbcFramesPercent_Type = Gauge32
_SsbcFramesPercent_Object = MibTableColumn
ssbcFramesPercent = _SsbcFramesPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 2, 1, 6),
    _SsbcFramesPercent_Type()
)
ssbcFramesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbcFramesPercent.setStatus("current")
_SsDerivedTable_Object = MibTable
ssDerivedTable = _SsDerivedTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    ssDerivedTable.setStatus("current")
_SsDerivedEntry_Object = MibTableRow
ssDerivedEntry = _SsDerivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 3, 1)
)
ssDerivedEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "ssdTimeStampIndex"),
)
if mibBuilder.loadTexts:
    ssDerivedEntry.setStatus("current")
_SsdTimeStampIndex_Type = Unsigned32
_SsdTimeStampIndex_Object = MibTableColumn
ssdTimeStampIndex = _SsdTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 3, 1, 1),
    _SsdTimeStampIndex_Type()
)
ssdTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdTimeStampIndex.setStatus("current")


class _SsdTimeStamp_Type(DisplayString):
    """Custom type ssdTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SsdTimeStamp_Type.__name__ = "DisplayString"
_SsdTimeStamp_Object = MibTableColumn
ssdTimeStamp = _SsdTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 3, 1, 2),
    _SsdTimeStamp_Type()
)
ssdTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdTimeStamp.setStatus("current")
_SsdUtilization_Type = Gauge32
_SsdUtilization_Object = MibTableColumn
ssdUtilization = _SsdUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 3, 1, 3),
    _SsdUtilization_Type()
)
ssdUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdUtilization.setStatus("current")
_SsdErrorFrames_Type = Gauge32
_SsdErrorFrames_Object = MibTableColumn
ssdErrorFrames = _SsdErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 3, 1, 4),
    _SsdErrorFrames_Type()
)
ssdErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdErrorFrames.setStatus("current")
_SsEthernetTable_Object = MibTable
ssEthernetTable = _SsEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    ssEthernetTable.setStatus("current")
_SsEthernetEntry_Object = MibTableRow
ssEthernetEntry = _SsEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 4, 1)
)
ssEthernetEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "sseTimeStampIndex"),
)
if mibBuilder.loadTexts:
    ssEthernetEntry.setStatus("current")
_SseTimeStampIndex_Type = Unsigned32
_SseTimeStampIndex_Object = MibTableColumn
sseTimeStampIndex = _SseTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 4, 1, 1),
    _SseTimeStampIndex_Type()
)
sseTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sseTimeStampIndex.setStatus("current")


class _SseTimeStamp_Type(DisplayString):
    """Custom type sseTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SseTimeStamp_Type.__name__ = "DisplayString"
_SseTimeStamp_Object = MibTableColumn
sseTimeStamp = _SseTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 4, 1, 2),
    _SseTimeStamp_Type()
)
sseTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sseTimeStamp.setStatus("current")
_SseRunts_Type = Counter32
_SseRunts_Object = MibTableColumn
sseRunts = _SseRunts_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 4, 1, 3),
    _SseRunts_Type()
)
sseRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sseRunts.setStatus("current")
_SseJabbers_Type = Counter32
_SseJabbers_Object = MibTableColumn
sseJabbers = _SseJabbers_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 4, 1, 4),
    _SseJabbers_Type()
)
sseJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sseJabbers.setStatus("current")
_SseCrc_Type = Counter32
_SseCrc_Object = MibTableColumn
sseCrc = _SseCrc_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 4, 1, 5),
    _SseCrc_Type()
)
sseCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sseCrc.setStatus("current")
_SseCollisions_Type = Counter32
_SseCollisions_Object = MibTableColumn
sseCollisions = _SseCollisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 4, 1, 6),
    _SseCollisions_Type()
)
sseCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sseCollisions.setStatus("current")
_SseLateCollisions_Type = Counter32
_SseLateCollisions_Object = MibTableColumn
sseLateCollisions = _SseLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 4, 1, 7),
    _SseLateCollisions_Type()
)
sseLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sseLateCollisions.setStatus("current")
_SsIcmpTable_Object = MibTable
ssIcmpTable = _SsIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    ssIcmpTable.setStatus("current")
_SsIcmpEntry_Object = MibTableRow
ssIcmpEntry = _SsIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1)
)
ssIcmpEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "ssiTimeStampIndex"),
)
if mibBuilder.loadTexts:
    ssIcmpEntry.setStatus("current")
_SsiTimeStampIndex_Type = Unsigned32
_SsiTimeStampIndex_Object = MibTableColumn
ssiTimeStampIndex = _SsiTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 1),
    _SsiTimeStampIndex_Type()
)
ssiTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiTimeStampIndex.setStatus("current")


class _SsiTimeStamp_Type(DisplayString):
    """Custom type ssiTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SsiTimeStamp_Type.__name__ = "DisplayString"
_SsiTimeStamp_Object = MibTableColumn
ssiTimeStamp = _SsiTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 2),
    _SsiTimeStamp_Type()
)
ssiTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiTimeStamp.setStatus("current")
_SsiPing_Type = Counter32
_SsiPing_Object = MibTableColumn
ssiPing = _SsiPing_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 3),
    _SsiPing_Type()
)
ssiPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiPing.setStatus("current")
_SsiSrcQuench_Type = Counter32
_SsiSrcQuench_Object = MibTableColumn
ssiSrcQuench = _SsiSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 4),
    _SsiSrcQuench_Type()
)
ssiSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSrcQuench.setStatus("current")
_SsiRedirect_Type = Counter32
_SsiRedirect_Object = MibTableColumn
ssiRedirect = _SsiRedirect_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 5),
    _SsiRedirect_Type()
)
ssiRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiRedirect.setStatus("current")
_SsiTtlExceeded_Type = Counter32
_SsiTtlExceeded_Object = MibTableColumn
ssiTtlExceeded = _SsiTtlExceeded_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 6),
    _SsiTtlExceeded_Type()
)
ssiTtlExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiTtlExceeded.setStatus("current")
_SsiParamProblem_Type = Counter32
_SsiParamProblem_Object = MibTableColumn
ssiParamProblem = _SsiParamProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 7),
    _SsiParamProblem_Type()
)
ssiParamProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiParamProblem.setStatus("current")
_SsiTimestamp_Type = Counter32
_SsiTimestamp_Object = MibTableColumn
ssiTimestamp = _SsiTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 8),
    _SsiTimestamp_Type()
)
ssiTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiTimestamp.setStatus("current")
_SsiFragTimeout_Type = Counter32
_SsiFragTimeout_Object = MibTableColumn
ssiFragTimeout = _SsiFragTimeout_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 9),
    _SsiFragTimeout_Type()
)
ssiFragTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiFragTimeout.setStatus("current")
_SsiNetUnreachable_Type = Counter32
_SsiNetUnreachable_Object = MibTableColumn
ssiNetUnreachable = _SsiNetUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 10),
    _SsiNetUnreachable_Type()
)
ssiNetUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiNetUnreachable.setStatus("current")
_SsiHostUnreachable_Type = Counter32
_SsiHostUnreachable_Object = MibTableColumn
ssiHostUnreachable = _SsiHostUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 11),
    _SsiHostUnreachable_Type()
)
ssiHostUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiHostUnreachable.setStatus("current")
_SsiProtocolUnreachable_Type = Counter32
_SsiProtocolUnreachable_Object = MibTableColumn
ssiProtocolUnreachable = _SsiProtocolUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 12),
    _SsiProtocolUnreachable_Type()
)
ssiProtocolUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiProtocolUnreachable.setStatus("current")
_SsiPortUnreachable_Type = Counter32
_SsiPortUnreachable_Object = MibTableColumn
ssiPortUnreachable = _SsiPortUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 13),
    _SsiPortUnreachable_Type()
)
ssiPortUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiPortUnreachable.setStatus("current")
_SsiFragRequired_Type = Counter32
_SsiFragRequired_Object = MibTableColumn
ssiFragRequired = _SsiFragRequired_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 14),
    _SsiFragRequired_Type()
)
ssiFragRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiFragRequired.setStatus("current")
_SsiSrcRouteFail_Type = Counter32
_SsiSrcRouteFail_Object = MibTableColumn
ssiSrcRouteFail = _SsiSrcRouteFail_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 15),
    _SsiSrcRouteFail_Type()
)
ssiSrcRouteFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSrcRouteFail.setStatus("current")
_SsiDestNetUnknown_Type = Counter32
_SsiDestNetUnknown_Object = MibTableColumn
ssiDestNetUnknown = _SsiDestNetUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 16),
    _SsiDestNetUnknown_Type()
)
ssiDestNetUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiDestNetUnknown.setStatus("current")
_SsiDestHostUnknown_Type = Counter32
_SsiDestHostUnknown_Object = MibTableColumn
ssiDestHostUnknown = _SsiDestHostUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 17),
    _SsiDestHostUnknown_Type()
)
ssiDestHostUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiDestHostUnknown.setStatus("current")
_SsiSrcHostIsolated_Type = Counter32
_SsiSrcHostIsolated_Object = MibTableColumn
ssiSrcHostIsolated = _SsiSrcHostIsolated_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 18),
    _SsiSrcHostIsolated_Type()
)
ssiSrcHostIsolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiSrcHostIsolated.setStatus("current")
_SsiNetProhibited_Type = Counter32
_SsiNetProhibited_Object = MibTableColumn
ssiNetProhibited = _SsiNetProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 19),
    _SsiNetProhibited_Type()
)
ssiNetProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiNetProhibited.setStatus("current")
_SsiHostProhibited_Type = Counter32
_SsiHostProhibited_Object = MibTableColumn
ssiHostProhibited = _SsiHostProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 20),
    _SsiHostProhibited_Type()
)
ssiHostProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiHostProhibited.setStatus("current")
_SsiNetTosUnreachable_Type = Counter32
_SsiNetTosUnreachable_Object = MibTableColumn
ssiNetTosUnreachable = _SsiNetTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 21),
    _SsiNetTosUnreachable_Type()
)
ssiNetTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiNetTosUnreachable.setStatus("current")
_SsiHostTosUnreachable_Type = Counter32
_SsiHostTosUnreachable_Object = MibTableColumn
ssiHostTosUnreachable = _SsiHostTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 22),
    _SsiHostTosUnreachable_Type()
)
ssiHostTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiHostTosUnreachable.setStatus("current")
_SsiPerformance_Type = Counter32
_SsiPerformance_Object = MibTableColumn
ssiPerformance = _SsiPerformance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 23),
    _SsiPerformance_Type()
)
ssiPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiPerformance.setStatus("current")
_SsiNetRouteProblem_Type = Counter32
_SsiNetRouteProblem_Object = MibTableColumn
ssiNetRouteProblem = _SsiNetRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 24),
    _SsiNetRouteProblem_Type()
)
ssiNetRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiNetRouteProblem.setStatus("current")
_SsiHostRouteProblem_Type = Counter32
_SsiHostRouteProblem_Object = MibTableColumn
ssiHostRouteProblem = _SsiHostRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 25),
    _SsiHostRouteProblem_Type()
)
ssiHostRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiHostRouteProblem.setStatus("current")
_SsiAppRouteProblem_Type = Counter32
_SsiAppRouteProblem_Object = MibTableColumn
ssiAppRouteProblem = _SsiAppRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 26),
    _SsiAppRouteProblem_Type()
)
ssiAppRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiAppRouteProblem.setStatus("current")
_SsiRouteChange_Type = Counter32
_SsiRouteChange_Object = MibTableColumn
ssiRouteChange = _SsiRouteChange_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 27),
    _SsiRouteChange_Type()
)
ssiRouteChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiRouteChange.setStatus("current")
_SsiErrors_Type = Counter32
_SsiErrors_Object = MibTableColumn
ssiErrors = _SsiErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 28),
    _SsiErrors_Type()
)
ssiErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiErrors.setStatus("current")
_SsiMaintenance_Type = Counter32
_SsiMaintenance_Object = MibTableColumn
ssiMaintenance = _SsiMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 5, 1, 29),
    _SsiMaintenance_Type()
)
ssiMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssiMaintenance.setStatus("current")
_SsPortTable_Object = MibTable
ssPortTable = _SsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    ssPortTable.setStatus("current")
_SsPortEntry_Object = MibTableRow
ssPortEntry = _SsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1)
)
ssPortEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "sspTimeStampIndex"),
)
if mibBuilder.loadTexts:
    ssPortEntry.setStatus("current")
_SspTimeStampIndex_Type = Unsigned32
_SspTimeStampIndex_Object = MibTableColumn
sspTimeStampIndex = _SspTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 1),
    _SspTimeStampIndex_Type()
)
sspTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspTimeStampIndex.setStatus("current")


class _SspTimeStamp_Type(DisplayString):
    """Custom type sspTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SspTimeStamp_Type.__name__ = "DisplayString"
_SspTimeStamp_Object = MibTableColumn
sspTimeStamp = _SspTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 2),
    _SspTimeStamp_Type()
)
sspTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspTimeStamp.setStatus("current")
_Ssp1Frames_Type = Counter32
_Ssp1Frames_Object = MibTableColumn
ssp1Frames = _Ssp1Frames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 3),
    _Ssp1Frames_Type()
)
ssp1Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp1Frames.setStatus("current")
_Ssp1Bytes_Type = Counter32
_Ssp1Bytes_Object = MibTableColumn
ssp1Bytes = _Ssp1Bytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 4),
    _Ssp1Bytes_Type()
)
ssp1Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp1Bytes.setStatus("current")
_Ssp1FrameSize_Type = Gauge32
_Ssp1FrameSize_Object = MibTableColumn
ssp1FrameSize = _Ssp1FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 5),
    _Ssp1FrameSize_Type()
)
ssp1FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp1FrameSize.setStatus("current")
if mibBuilder.loadTexts:
    ssp1FrameSize.setUnits("bytes")
_Ssp1Utilization_Type = Gauge32
_Ssp1Utilization_Object = MibTableColumn
ssp1Utilization = _Ssp1Utilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 6),
    _Ssp1Utilization_Type()
)
ssp1Utilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp1Utilization.setStatus("current")
_Ssp1LineSpeed_Type = Gauge32
_Ssp1LineSpeed_Object = MibTableColumn
ssp1LineSpeed = _Ssp1LineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 7),
    _Ssp1LineSpeed_Type()
)
ssp1LineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp1LineSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ssp1LineSpeed.setUnits("bits per second")
_Ssp1SoftErrors_Type = Counter32
_Ssp1SoftErrors_Object = MibTableColumn
ssp1SoftErrors = _Ssp1SoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 8),
    _Ssp1SoftErrors_Type()
)
ssp1SoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp1SoftErrors.setStatus("current")
_Ssp1Runts_Type = Counter32
_Ssp1Runts_Object = MibTableColumn
ssp1Runts = _Ssp1Runts_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 9),
    _Ssp1Runts_Type()
)
ssp1Runts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp1Runts.setStatus("current")
_Ssp1Jabbers_Type = Counter32
_Ssp1Jabbers_Object = MibTableColumn
ssp1Jabbers = _Ssp1Jabbers_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 10),
    _Ssp1Jabbers_Type()
)
ssp1Jabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp1Jabbers.setStatus("current")
_Ssp1Crc_Type = Counter32
_Ssp1Crc_Object = MibTableColumn
ssp1Crc = _Ssp1Crc_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 11),
    _Ssp1Crc_Type()
)
ssp1Crc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp1Crc.setStatus("current")
_Ssp1Collisions_Type = Counter32
_Ssp1Collisions_Object = MibTableColumn
ssp1Collisions = _Ssp1Collisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 12),
    _Ssp1Collisions_Type()
)
ssp1Collisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp1Collisions.setStatus("current")
_Ssp1LateCollisions_Type = Counter32
_Ssp1LateCollisions_Object = MibTableColumn
ssp1LateCollisions = _Ssp1LateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 13),
    _Ssp1LateCollisions_Type()
)
ssp1LateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp1LateCollisions.setStatus("current")
_Ssp1LineNoise_Type = Counter32
_Ssp1LineNoise_Object = MibTableColumn
ssp1LineNoise = _Ssp1LineNoise_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 14),
    _Ssp1LineNoise_Type()
)
ssp1LineNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp1LineNoise.setStatus("current")
_Ssp2Frames_Type = Counter32
_Ssp2Frames_Object = MibTableColumn
ssp2Frames = _Ssp2Frames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 15),
    _Ssp2Frames_Type()
)
ssp2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp2Frames.setStatus("current")
_Ssp2Bytes_Type = Counter32
_Ssp2Bytes_Object = MibTableColumn
ssp2Bytes = _Ssp2Bytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 16),
    _Ssp2Bytes_Type()
)
ssp2Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp2Bytes.setStatus("current")
_Ssp2FrameSize_Type = Gauge32
_Ssp2FrameSize_Object = MibTableColumn
ssp2FrameSize = _Ssp2FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 17),
    _Ssp2FrameSize_Type()
)
ssp2FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp2FrameSize.setStatus("current")
if mibBuilder.loadTexts:
    ssp2FrameSize.setUnits("bytes")
_Ssp2Utilization_Type = Gauge32
_Ssp2Utilization_Object = MibTableColumn
ssp2Utilization = _Ssp2Utilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 18),
    _Ssp2Utilization_Type()
)
ssp2Utilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp2Utilization.setStatus("current")
_Ssp2LineSpeed_Type = Gauge32
_Ssp2LineSpeed_Object = MibTableColumn
ssp2LineSpeed = _Ssp2LineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 19),
    _Ssp2LineSpeed_Type()
)
ssp2LineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp2LineSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ssp2LineSpeed.setUnits("bits per second")
_Ssp2SoftErrors_Type = Counter32
_Ssp2SoftErrors_Object = MibTableColumn
ssp2SoftErrors = _Ssp2SoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 20),
    _Ssp2SoftErrors_Type()
)
ssp2SoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp2SoftErrors.setStatus("current")
_Ssp2Runts_Type = Counter32
_Ssp2Runts_Object = MibTableColumn
ssp2Runts = _Ssp2Runts_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 21),
    _Ssp2Runts_Type()
)
ssp2Runts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp2Runts.setStatus("current")
_Ssp2Jabbers_Type = Counter32
_Ssp2Jabbers_Object = MibTableColumn
ssp2Jabbers = _Ssp2Jabbers_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 22),
    _Ssp2Jabbers_Type()
)
ssp2Jabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp2Jabbers.setStatus("current")
_Ssp2Crc_Type = Counter32
_Ssp2Crc_Object = MibTableColumn
ssp2Crc = _Ssp2Crc_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 23),
    _Ssp2Crc_Type()
)
ssp2Crc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp2Crc.setStatus("current")
_Ssp2Collisions_Type = Counter32
_Ssp2Collisions_Object = MibTableColumn
ssp2Collisions = _Ssp2Collisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 24),
    _Ssp2Collisions_Type()
)
ssp2Collisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp2Collisions.setStatus("current")
_Ssp2LateCollisions_Type = Counter32
_Ssp2LateCollisions_Object = MibTableColumn
ssp2LateCollisions = _Ssp2LateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 25),
    _Ssp2LateCollisions_Type()
)
ssp2LateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp2LateCollisions.setStatus("current")
_Ssp2LineNoise_Type = Counter32
_Ssp2LineNoise_Object = MibTableColumn
ssp2LineNoise = _Ssp2LineNoise_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 2, 2, 6, 1, 26),
    _Ssp2LineNoise_Type()
)
ssp2LineNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssp2LineNoise.setStatus("current")
_DbMac_ObjectIdentity = ObjectIdentity
dbMac = _DbMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dbMac.setStatus("current")
_MacLongTerm_ObjectIdentity = ObjectIdentity
macLongTerm = _MacLongTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    macLongTerm.setStatus("current")
_MlBaseTable_Object = MibTable
mlBaseTable = _MlBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mlBaseTable.setStatus("current")
_MlBaseEntry_Object = MibTableRow
mlBaseEntry = _MlBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 1, 1)
)
mlBaseEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mlbMacIndex"),
    (0, "CODIMA-EXPRESS-MIB", "mlbTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mlBaseEntry.setStatus("current")
_MlbMacIndex_Type = MacAddress
_MlbMacIndex_Object = MibTableColumn
mlbMacIndex = _MlbMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 1, 1, 1),
    _MlbMacIndex_Type()
)
mlbMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbMacIndex.setStatus("current")
_MlbTimeStampIndex_Type = Unsigned32
_MlbTimeStampIndex_Object = MibTableColumn
mlbTimeStampIndex = _MlbTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 1, 1, 2),
    _MlbTimeStampIndex_Type()
)
mlbTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbTimeStampIndex.setStatus("current")


class _MlbTimeStamp_Type(DisplayString):
    """Custom type mlbTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MlbTimeStamp_Type.__name__ = "DisplayString"
_MlbTimeStamp_Object = MibTableColumn
mlbTimeStamp = _MlbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 1, 1, 3),
    _MlbTimeStamp_Type()
)
mlbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbTimeStamp.setStatus("current")
_MlbFrames_Type = Counter32
_MlbFrames_Object = MibTableColumn
mlbFrames = _MlbFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 1, 1, 4),
    _MlbFrames_Type()
)
mlbFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbFrames.setStatus("current")
_MlbBytes_Type = Counter32
_MlbBytes_Object = MibTableColumn
mlbBytes = _MlbBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 1, 1, 5),
    _MlbBytes_Type()
)
mlbBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbBytes.setStatus("current")
_MlbFrameSize_Type = Gauge32
_MlbFrameSize_Object = MibTableColumn
mlbFrameSize = _MlbFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 1, 1, 6),
    _MlbFrameSize_Type()
)
mlbFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    mlbFrameSize.setUnits("bytes")
_MlbHardwareErrors_Type = Counter32
_MlbHardwareErrors_Object = MibTableColumn
mlbHardwareErrors = _MlbHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 1, 1, 7),
    _MlbHardwareErrors_Type()
)
mlbHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbHardwareErrors.setStatus("current")
_MlbSoftwareErrors_Type = Counter32
_MlbSoftwareErrors_Object = MibTableColumn
mlbSoftwareErrors = _MlbSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 1, 1, 8),
    _MlbSoftwareErrors_Type()
)
mlbSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbSoftwareErrors.setStatus("current")
_MlDerivedTable_Object = MibTable
mlDerivedTable = _MlDerivedTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    mlDerivedTable.setStatus("current")
_MlDerivedEntry_Object = MibTableRow
mlDerivedEntry = _MlDerivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 2, 1)
)
mlDerivedEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mldMacIndex"),
    (0, "CODIMA-EXPRESS-MIB", "mldTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mlDerivedEntry.setStatus("current")
_MldMacIndex_Type = MacAddress
_MldMacIndex_Object = MibTableColumn
mldMacIndex = _MldMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 2, 1, 1),
    _MldMacIndex_Type()
)
mldMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldMacIndex.setStatus("current")
_MldTimeStampIndex_Type = Unsigned32
_MldTimeStampIndex_Object = MibTableColumn
mldTimeStampIndex = _MldTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 2, 1, 2),
    _MldTimeStampIndex_Type()
)
mldTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldTimeStampIndex.setStatus("current")


class _MldTimeStamp_Type(DisplayString):
    """Custom type mldTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_MldTimeStamp_Type.__name__ = "DisplayString"
_MldTimeStamp_Object = MibTableColumn
mldTimeStamp = _MldTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 2, 1, 3),
    _MldTimeStamp_Type()
)
mldTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldTimeStamp.setStatus("current")
_MldUtilization_Type = Gauge32
_MldUtilization_Object = MibTableColumn
mldUtilization = _MldUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 2, 1, 4),
    _MldUtilization_Type()
)
mldUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldUtilization.setStatus("current")
_MldErrorFrames_Type = Gauge32
_MldErrorFrames_Object = MibTableColumn
mldErrorFrames = _MldErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 2, 1, 5),
    _MldErrorFrames_Type()
)
mldErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldErrorFrames.setStatus("current")
_MlDuplexTable_Object = MibTable
mlDuplexTable = _MlDuplexTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    mlDuplexTable.setStatus("current")
_MlDuplexEntry_Object = MibTableRow
mlDuplexEntry = _MlDuplexEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 3, 1)
)
mlDuplexEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mlduMacIndex"),
    (0, "CODIMA-EXPRESS-MIB", "mlduTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mlDuplexEntry.setStatus("current")
_MlduMacIndex_Type = MacAddress
_MlduMacIndex_Object = MibTableColumn
mlduMacIndex = _MlduMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 3, 1, 1),
    _MlduMacIndex_Type()
)
mlduMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlduMacIndex.setStatus("current")
_MlduTimeStampIndex_Type = Unsigned32
_MlduTimeStampIndex_Object = MibTableColumn
mlduTimeStampIndex = _MlduTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 3, 1, 2),
    _MlduTimeStampIndex_Type()
)
mlduTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlduTimeStampIndex.setStatus("current")


class _MlduTimeStamp_Type(DisplayString):
    """Custom type mlduTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MlduTimeStamp_Type.__name__ = "DisplayString"
_MlduTimeStamp_Object = MibTableColumn
mlduTimeStamp = _MlduTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 3, 1, 3),
    _MlduTimeStamp_Type()
)
mlduTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlduTimeStamp.setStatus("current")
_MlduTxFrames_Type = Counter32
_MlduTxFrames_Object = MibTableColumn
mlduTxFrames = _MlduTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 3, 1, 4),
    _MlduTxFrames_Type()
)
mlduTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlduTxFrames.setStatus("current")
_MlduTxBytes_Type = Counter32
_MlduTxBytes_Object = MibTableColumn
mlduTxBytes = _MlduTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 3, 1, 5),
    _MlduTxBytes_Type()
)
mlduTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlduTxBytes.setStatus("current")
_MlduTxFrameSize_Type = Gauge32
_MlduTxFrameSize_Object = MibTableColumn
mlduTxFrameSize = _MlduTxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 3, 1, 6),
    _MlduTxFrameSize_Type()
)
mlduTxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlduTxFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    mlduTxFrameSize.setUnits("bytes")
_MlduTxUtilization_Type = Gauge32
_MlduTxUtilization_Object = MibTableColumn
mlduTxUtilization = _MlduTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 3, 1, 7),
    _MlduTxUtilization_Type()
)
mlduTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlduTxUtilization.setStatus("current")
_MlduRxFrames_Type = Counter32
_MlduRxFrames_Object = MibTableColumn
mlduRxFrames = _MlduRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 3, 1, 8),
    _MlduRxFrames_Type()
)
mlduRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlduRxFrames.setStatus("current")
_MlduRxBytes_Type = Counter32
_MlduRxBytes_Object = MibTableColumn
mlduRxBytes = _MlduRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 3, 1, 9),
    _MlduRxBytes_Type()
)
mlduRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlduRxBytes.setStatus("current")
_MlduRxFrameSize_Type = Gauge32
_MlduRxFrameSize_Object = MibTableColumn
mlduRxFrameSize = _MlduRxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 3, 1, 10),
    _MlduRxFrameSize_Type()
)
mlduRxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlduRxFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    mlduRxFrameSize.setUnits("bytes")
_MlduRxUtilization_Type = Gauge32
_MlduRxUtilization_Object = MibTableColumn
mlduRxUtilization = _MlduRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 3, 1, 11),
    _MlduRxUtilization_Type()
)
mlduRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlduRxUtilization.setStatus("current")
_MlEthernetTable_Object = MibTable
mlEthernetTable = _MlEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    mlEthernetTable.setStatus("current")
_MlEthernetEntry_Object = MibTableRow
mlEthernetEntry = _MlEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 4, 1)
)
mlEthernetEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mleMacIndex"),
    (0, "CODIMA-EXPRESS-MIB", "mleTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mlEthernetEntry.setStatus("current")
_MleMacIndex_Type = MacAddress
_MleMacIndex_Object = MibTableColumn
mleMacIndex = _MleMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 4, 1, 1),
    _MleMacIndex_Type()
)
mleMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mleMacIndex.setStatus("current")
_MleTimeStampIndex_Type = Unsigned32
_MleTimeStampIndex_Object = MibTableColumn
mleTimeStampIndex = _MleTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 4, 1, 2),
    _MleTimeStampIndex_Type()
)
mleTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mleTimeStampIndex.setStatus("current")


class _MleTimeStamp_Type(DisplayString):
    """Custom type mleTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MleTimeStamp_Type.__name__ = "DisplayString"
_MleTimeStamp_Object = MibTableColumn
mleTimeStamp = _MleTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 4, 1, 3),
    _MleTimeStamp_Type()
)
mleTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mleTimeStamp.setStatus("current")
_MleRunts_Type = Counter32
_MleRunts_Object = MibTableColumn
mleRunts = _MleRunts_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 4, 1, 4),
    _MleRunts_Type()
)
mleRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mleRunts.setStatus("current")
_MleJabbers_Type = Counter32
_MleJabbers_Object = MibTableColumn
mleJabbers = _MleJabbers_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 4, 1, 5),
    _MleJabbers_Type()
)
mleJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mleJabbers.setStatus("current")
_MleCrc_Type = Counter32
_MleCrc_Object = MibTableColumn
mleCrc = _MleCrc_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 4, 1, 6),
    _MleCrc_Type()
)
mleCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mleCrc.setStatus("current")
_MleCollisions_Type = Counter32
_MleCollisions_Object = MibTableColumn
mleCollisions = _MleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 4, 1, 7),
    _MleCollisions_Type()
)
mleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mleCollisions.setStatus("current")
_MleLateCollisions_Type = Counter32
_MleLateCollisions_Object = MibTableColumn
mleLateCollisions = _MleLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 4, 1, 8),
    _MleLateCollisions_Type()
)
mleLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mleLateCollisions.setStatus("current")
_MlIcmpTable_Object = MibTable
mlIcmpTable = _MlIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    mlIcmpTable.setStatus("current")
_MlIcmpEntry_Object = MibTableRow
mlIcmpEntry = _MlIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1)
)
mlIcmpEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mliMacIndex"),
    (0, "CODIMA-EXPRESS-MIB", "mliTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mlIcmpEntry.setStatus("current")
_MliMacIndex_Type = MacAddress
_MliMacIndex_Object = MibTableColumn
mliMacIndex = _MliMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 1),
    _MliMacIndex_Type()
)
mliMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliMacIndex.setStatus("current")
_MliTimeStampIndex_Type = Unsigned32
_MliTimeStampIndex_Object = MibTableColumn
mliTimeStampIndex = _MliTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 2),
    _MliTimeStampIndex_Type()
)
mliTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliTimeStampIndex.setStatus("current")


class _MliTimeStamp_Type(DisplayString):
    """Custom type mliTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MliTimeStamp_Type.__name__ = "DisplayString"
_MliTimeStamp_Object = MibTableColumn
mliTimeStamp = _MliTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 3),
    _MliTimeStamp_Type()
)
mliTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliTimeStamp.setStatus("current")
_MliPing_Type = Counter32
_MliPing_Object = MibTableColumn
mliPing = _MliPing_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 4),
    _MliPing_Type()
)
mliPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliPing.setStatus("current")
_MliSrcQuench_Type = Counter32
_MliSrcQuench_Object = MibTableColumn
mliSrcQuench = _MliSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 5),
    _MliSrcQuench_Type()
)
mliSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliSrcQuench.setStatus("current")
_MliRedirect_Type = Counter32
_MliRedirect_Object = MibTableColumn
mliRedirect = _MliRedirect_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 6),
    _MliRedirect_Type()
)
mliRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliRedirect.setStatus("current")
_MliTtlExceeded_Type = Counter32
_MliTtlExceeded_Object = MibTableColumn
mliTtlExceeded = _MliTtlExceeded_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 7),
    _MliTtlExceeded_Type()
)
mliTtlExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliTtlExceeded.setStatus("current")
_MliParamProblem_Type = Counter32
_MliParamProblem_Object = MibTableColumn
mliParamProblem = _MliParamProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 8),
    _MliParamProblem_Type()
)
mliParamProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliParamProblem.setStatus("current")
_MliTimestamp_Type = Counter32
_MliTimestamp_Object = MibTableColumn
mliTimestamp = _MliTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 9),
    _MliTimestamp_Type()
)
mliTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliTimestamp.setStatus("current")
_MliFragTimeout_Type = Counter32
_MliFragTimeout_Object = MibTableColumn
mliFragTimeout = _MliFragTimeout_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 10),
    _MliFragTimeout_Type()
)
mliFragTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliFragTimeout.setStatus("current")
_MliNetUnreachable_Type = Counter32
_MliNetUnreachable_Object = MibTableColumn
mliNetUnreachable = _MliNetUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 11),
    _MliNetUnreachable_Type()
)
mliNetUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliNetUnreachable.setStatus("current")
_MliHostUnreachable_Type = Counter32
_MliHostUnreachable_Object = MibTableColumn
mliHostUnreachable = _MliHostUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 12),
    _MliHostUnreachable_Type()
)
mliHostUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliHostUnreachable.setStatus("current")
_MliProtocolUnreachable_Type = Counter32
_MliProtocolUnreachable_Object = MibTableColumn
mliProtocolUnreachable = _MliProtocolUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 13),
    _MliProtocolUnreachable_Type()
)
mliProtocolUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliProtocolUnreachable.setStatus("current")
_MliPortUnreachable_Type = Counter32
_MliPortUnreachable_Object = MibTableColumn
mliPortUnreachable = _MliPortUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 14),
    _MliPortUnreachable_Type()
)
mliPortUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliPortUnreachable.setStatus("current")
_MliFragRequired_Type = Counter32
_MliFragRequired_Object = MibTableColumn
mliFragRequired = _MliFragRequired_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 15),
    _MliFragRequired_Type()
)
mliFragRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliFragRequired.setStatus("current")
_MliSrcRouteFail_Type = Counter32
_MliSrcRouteFail_Object = MibTableColumn
mliSrcRouteFail = _MliSrcRouteFail_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 16),
    _MliSrcRouteFail_Type()
)
mliSrcRouteFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliSrcRouteFail.setStatus("current")
_MliDestNetUnknown_Type = Counter32
_MliDestNetUnknown_Object = MibTableColumn
mliDestNetUnknown = _MliDestNetUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 17),
    _MliDestNetUnknown_Type()
)
mliDestNetUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliDestNetUnknown.setStatus("current")
_MliDestHostUnknown_Type = Counter32
_MliDestHostUnknown_Object = MibTableColumn
mliDestHostUnknown = _MliDestHostUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 18),
    _MliDestHostUnknown_Type()
)
mliDestHostUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliDestHostUnknown.setStatus("current")
_MliSrcHostIsolated_Type = Counter32
_MliSrcHostIsolated_Object = MibTableColumn
mliSrcHostIsolated = _MliSrcHostIsolated_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 19),
    _MliSrcHostIsolated_Type()
)
mliSrcHostIsolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliSrcHostIsolated.setStatus("current")
_MliNetProhibited_Type = Counter32
_MliNetProhibited_Object = MibTableColumn
mliNetProhibited = _MliNetProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 20),
    _MliNetProhibited_Type()
)
mliNetProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliNetProhibited.setStatus("current")
_MliHostProhibited_Type = Counter32
_MliHostProhibited_Object = MibTableColumn
mliHostProhibited = _MliHostProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 21),
    _MliHostProhibited_Type()
)
mliHostProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliHostProhibited.setStatus("current")
_MliNetTosUnreachable_Type = Counter32
_MliNetTosUnreachable_Object = MibTableColumn
mliNetTosUnreachable = _MliNetTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 22),
    _MliNetTosUnreachable_Type()
)
mliNetTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliNetTosUnreachable.setStatus("current")
_MliHostTosUnreachable_Type = Counter32
_MliHostTosUnreachable_Object = MibTableColumn
mliHostTosUnreachable = _MliHostTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 23),
    _MliHostTosUnreachable_Type()
)
mliHostTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliHostTosUnreachable.setStatus("current")
_MliPerformance_Type = Counter32
_MliPerformance_Object = MibTableColumn
mliPerformance = _MliPerformance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 24),
    _MliPerformance_Type()
)
mliPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliPerformance.setStatus("current")
_MliNetRouteProblem_Type = Counter32
_MliNetRouteProblem_Object = MibTableColumn
mliNetRouteProblem = _MliNetRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 25),
    _MliNetRouteProblem_Type()
)
mliNetRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliNetRouteProblem.setStatus("current")
_MliHostRouteProblem_Type = Counter32
_MliHostRouteProblem_Object = MibTableColumn
mliHostRouteProblem = _MliHostRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 26),
    _MliHostRouteProblem_Type()
)
mliHostRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliHostRouteProblem.setStatus("current")
_MliAppRouteProblem_Type = Counter32
_MliAppRouteProblem_Object = MibTableColumn
mliAppRouteProblem = _MliAppRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 27),
    _MliAppRouteProblem_Type()
)
mliAppRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliAppRouteProblem.setStatus("current")
_MliRouteChange_Type = Counter32
_MliRouteChange_Object = MibTableColumn
mliRouteChange = _MliRouteChange_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 28),
    _MliRouteChange_Type()
)
mliRouteChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliRouteChange.setStatus("current")
_MliErrors_Type = Counter32
_MliErrors_Object = MibTableColumn
mliErrors = _MliErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 29),
    _MliErrors_Type()
)
mliErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliErrors.setStatus("current")
_MliMaintenance_Type = Counter32
_MliMaintenance_Object = MibTableColumn
mliMaintenance = _MliMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 5, 1, 30),
    _MliMaintenance_Type()
)
mliMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mliMaintenance.setStatus("current")
_MlProtocolTable_Object = MibTable
mlProtocolTable = _MlProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    mlProtocolTable.setStatus("current")
_MlProtocolEntry_Object = MibTableRow
mlProtocolEntry = _MlProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1)
)
mlProtocolEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mlpMacIndex"),
    (0, "CODIMA-EXPRESS-MIB", "mlpTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mlProtocolEntry.setStatus("current")
_MlpMacIndex_Type = MacAddress
_MlpMacIndex_Object = MibTableColumn
mlpMacIndex = _MlpMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 1),
    _MlpMacIndex_Type()
)
mlpMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpMacIndex.setStatus("current")
_MlpTimeStampIndex_Type = Unsigned32
_MlpTimeStampIndex_Object = MibTableColumn
mlpTimeStampIndex = _MlpTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 2),
    _MlpTimeStampIndex_Type()
)
mlpTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpTimeStampIndex.setStatus("current")


class _MlpTimeStamp_Type(DisplayString):
    """Custom type mlpTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MlpTimeStamp_Type.__name__ = "DisplayString"
_MlpTimeStamp_Object = MibTableColumn
mlpTimeStamp = _MlpTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 3),
    _MlpTimeStamp_Type()
)
mlpTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpTimeStamp.setStatus("current")
_MlpNovell_Type = Counter32
_MlpNovell_Object = MibTableColumn
mlpNovell = _MlpNovell_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 4),
    _MlpNovell_Type()
)
mlpNovell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpNovell.setStatus("current")
_MlpSnmp_Type = Counter32
_MlpSnmp_Object = MibTableColumn
mlpSnmp = _MlpSnmp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 5),
    _MlpSnmp_Type()
)
mlpSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpSnmp.setStatus("current")
_MlpRouting_Type = Counter32
_MlpRouting_Object = MibTableColumn
mlpRouting = _MlpRouting_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 6),
    _MlpRouting_Type()
)
mlpRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpRouting.setStatus("current")
_MlpWww_Type = Counter32
_MlpWww_Object = MibTableColumn
mlpWww = _MlpWww_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 7),
    _MlpWww_Type()
)
mlpWww.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpWww.setStatus("current")
_MlpIcmp_Type = Counter32
_MlpIcmp_Object = MibTableColumn
mlpIcmp = _MlpIcmp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 8),
    _MlpIcmp_Type()
)
mlpIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpIcmp.setStatus("current")
_MlpIso_Type = Counter32
_MlpIso_Object = MibTableColumn
mlpIso = _MlpIso_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 9),
    _MlpIso_Type()
)
mlpIso.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpIso.setStatus("current")
_MlpMail_Type = Counter32
_MlpMail_Object = MibTableColumn
mlpMail = _MlpMail_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 10),
    _MlpMail_Type()
)
mlpMail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpMail.setStatus("current")
_MlpNetbios_Type = Counter32
_MlpNetbios_Object = MibTableColumn
mlpNetbios = _MlpNetbios_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 11),
    _MlpNetbios_Type()
)
mlpNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpNetbios.setStatus("current")
_MlpDns_Type = Counter32
_MlpDns_Object = MibTableColumn
mlpDns = _MlpDns_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 12),
    _MlpDns_Type()
)
mlpDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpDns.setStatus("current")
_MlpIp_Type = Counter32
_MlpIp_Object = MibTableColumn
mlpIp = _MlpIp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 13),
    _MlpIp_Type()
)
mlpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpIp.setStatus("current")
_MlpVoip_Type = Counter32
_MlpVoip_Object = MibTableColumn
mlpVoip = _MlpVoip_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 14),
    _MlpVoip_Type()
)
mlpVoip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpVoip.setStatus("current")
_MlpLayer3Traffic_Type = Counter32
_MlpLayer3Traffic_Object = MibTableColumn
mlpLayer3Traffic = _MlpLayer3Traffic_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 15),
    _MlpLayer3Traffic_Type()
)
mlpLayer3Traffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpLayer3Traffic.setStatus("current")
_MlpIpData_Type = Counter32
_MlpIpData_Object = MibTableColumn
mlpIpData = _MlpIpData_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 16),
    _MlpIpData_Type()
)
mlpIpData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpIpData.setStatus("current")
_MlpApplications_Type = Counter32
_MlpApplications_Object = MibTableColumn
mlpApplications = _MlpApplications_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 17),
    _MlpApplications_Type()
)
mlpApplications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpApplications.setStatus("current")
_MlpIpControl_Type = Counter32
_MlpIpControl_Object = MibTableColumn
mlpIpControl = _MlpIpControl_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 18),
    _MlpIpControl_Type()
)
mlpIpControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpIpControl.setStatus("current")
_MlpManagement_Type = Counter32
_MlpManagement_Object = MibTableColumn
mlpManagement = _MlpManagement_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 1, 6, 1, 19),
    _MlpManagement_Type()
)
mlpManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpManagement.setStatus("current")
_MacShortTerm_ObjectIdentity = ObjectIdentity
macShortTerm = _MacShortTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    macShortTerm.setStatus("current")
_MsBaseTable_Object = MibTable
msBaseTable = _MsBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    msBaseTable.setStatus("current")
_MsBaseEntry_Object = MibTableRow
msBaseEntry = _MsBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 1, 1)
)
msBaseEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "msbMacIndex"),
    (0, "CODIMA-EXPRESS-MIB", "msbTimeStampIndex"),
)
if mibBuilder.loadTexts:
    msBaseEntry.setStatus("current")
_MsbMacIndex_Type = MacAddress
_MsbMacIndex_Object = MibTableColumn
msbMacIndex = _MsbMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 1, 1, 1),
    _MsbMacIndex_Type()
)
msbMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msbMacIndex.setStatus("current")
_MsbTimeStampIndex_Type = Unsigned32
_MsbTimeStampIndex_Object = MibTableColumn
msbTimeStampIndex = _MsbTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 1, 1, 2),
    _MsbTimeStampIndex_Type()
)
msbTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msbTimeStampIndex.setStatus("current")


class _MsbTimeStamp_Type(DisplayString):
    """Custom type msbTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MsbTimeStamp_Type.__name__ = "DisplayString"
_MsbTimeStamp_Object = MibTableColumn
msbTimeStamp = _MsbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 1, 1, 3),
    _MsbTimeStamp_Type()
)
msbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msbTimeStamp.setStatus("current")
_MsbFrames_Type = Counter32
_MsbFrames_Object = MibTableColumn
msbFrames = _MsbFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 1, 1, 4),
    _MsbFrames_Type()
)
msbFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msbFrames.setStatus("current")
_MsbBytes_Type = Counter32
_MsbBytes_Object = MibTableColumn
msbBytes = _MsbBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 1, 1, 5),
    _MsbBytes_Type()
)
msbBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msbBytes.setStatus("current")
_MsbFrameSize_Type = Gauge32
_MsbFrameSize_Object = MibTableColumn
msbFrameSize = _MsbFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 1, 1, 6),
    _MsbFrameSize_Type()
)
msbFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msbFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    msbFrameSize.setUnits("bytes")
_MsbHardwareErrors_Type = Counter32
_MsbHardwareErrors_Object = MibTableColumn
msbHardwareErrors = _MsbHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 1, 1, 7),
    _MsbHardwareErrors_Type()
)
msbHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msbHardwareErrors.setStatus("current")
_MsbSoftwareErrors_Type = Counter32
_MsbSoftwareErrors_Object = MibTableColumn
msbSoftwareErrors = _MsbSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 1, 1, 8),
    _MsbSoftwareErrors_Type()
)
msbSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msbSoftwareErrors.setStatus("current")
_MsDerivedTable_Object = MibTable
msDerivedTable = _MsDerivedTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    msDerivedTable.setStatus("current")
_MsDerivedEntry_Object = MibTableRow
msDerivedEntry = _MsDerivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 2, 1)
)
msDerivedEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "msdMacIndex"),
    (0, "CODIMA-EXPRESS-MIB", "msdTimeStampIndex"),
)
if mibBuilder.loadTexts:
    msDerivedEntry.setStatus("current")
_MsdMacIndex_Type = MacAddress
_MsdMacIndex_Object = MibTableColumn
msdMacIndex = _MsdMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 2, 1, 1),
    _MsdMacIndex_Type()
)
msdMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdMacIndex.setStatus("current")
_MsdTimeStampIndex_Type = Unsigned32
_MsdTimeStampIndex_Object = MibTableColumn
msdTimeStampIndex = _MsdTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 2, 1, 2),
    _MsdTimeStampIndex_Type()
)
msdTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdTimeStampIndex.setStatus("current")


class _MsdTimeStamp_Type(DisplayString):
    """Custom type msdTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MsdTimeStamp_Type.__name__ = "DisplayString"
_MsdTimeStamp_Object = MibTableColumn
msdTimeStamp = _MsdTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 2, 1, 3),
    _MsdTimeStamp_Type()
)
msdTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdTimeStamp.setStatus("current")
_MsdUtilization_Type = Gauge32
_MsdUtilization_Object = MibTableColumn
msdUtilization = _MsdUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 2, 1, 4),
    _MsdUtilization_Type()
)
msdUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdUtilization.setStatus("current")
_MsdErrorFrames_Type = Gauge32
_MsdErrorFrames_Object = MibTableColumn
msdErrorFrames = _MsdErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 2, 1, 5),
    _MsdErrorFrames_Type()
)
msdErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdErrorFrames.setStatus("current")
_MsDuplexTable_Object = MibTable
msDuplexTable = _MsDuplexTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    msDuplexTable.setStatus("current")
_MsDuplexEntry_Object = MibTableRow
msDuplexEntry = _MsDuplexEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 3, 1)
)
msDuplexEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "msdpMacIndex"),
    (0, "CODIMA-EXPRESS-MIB", "msdpTimeStampIndex"),
)
if mibBuilder.loadTexts:
    msDuplexEntry.setStatus("current")
_MsdpMacIndex_Type = MacAddress
_MsdpMacIndex_Object = MibTableColumn
msdpMacIndex = _MsdpMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 3, 1, 1),
    _MsdpMacIndex_Type()
)
msdpMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpMacIndex.setStatus("current")
_MsdpTimeStampIndex_Type = Unsigned32
_MsdpTimeStampIndex_Object = MibTableColumn
msdpTimeStampIndex = _MsdpTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 3, 1, 2),
    _MsdpTimeStampIndex_Type()
)
msdpTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpTimeStampIndex.setStatus("current")


class _MsdpTimeStamp_Type(DisplayString):
    """Custom type msdpTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MsdpTimeStamp_Type.__name__ = "DisplayString"
_MsdpTimeStamp_Object = MibTableColumn
msdpTimeStamp = _MsdpTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 3, 1, 3),
    _MsdpTimeStamp_Type()
)
msdpTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpTimeStamp.setStatus("current")
_MsdpTxFrames_Type = Counter32
_MsdpTxFrames_Object = MibTableColumn
msdpTxFrames = _MsdpTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 3, 1, 4),
    _MsdpTxFrames_Type()
)
msdpTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpTxFrames.setStatus("current")
_MsdpTxBytes_Type = Counter32
_MsdpTxBytes_Object = MibTableColumn
msdpTxBytes = _MsdpTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 3, 1, 5),
    _MsdpTxBytes_Type()
)
msdpTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpTxBytes.setStatus("current")
_MsdpTxFrameSize_Type = Gauge32
_MsdpTxFrameSize_Object = MibTableColumn
msdpTxFrameSize = _MsdpTxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 3, 1, 6),
    _MsdpTxFrameSize_Type()
)
msdpTxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpTxFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    msdpTxFrameSize.setUnits("bytes")
_MsdpTxUtilization_Type = Gauge32
_MsdpTxUtilization_Object = MibTableColumn
msdpTxUtilization = _MsdpTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 3, 1, 7),
    _MsdpTxUtilization_Type()
)
msdpTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpTxUtilization.setStatus("current")
_MsdpRxFrames_Type = Counter32
_MsdpRxFrames_Object = MibTableColumn
msdpRxFrames = _MsdpRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 3, 1, 8),
    _MsdpRxFrames_Type()
)
msdpRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpRxFrames.setStatus("current")
_MsdpRxBytes_Type = Counter32
_MsdpRxBytes_Object = MibTableColumn
msdpRxBytes = _MsdpRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 3, 1, 9),
    _MsdpRxBytes_Type()
)
msdpRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpRxBytes.setStatus("current")
_MsdpRxFrameSize_Type = Gauge32
_MsdpRxFrameSize_Object = MibTableColumn
msdpRxFrameSize = _MsdpRxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 3, 1, 10),
    _MsdpRxFrameSize_Type()
)
msdpRxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpRxFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    msdpRxFrameSize.setUnits("bytes")
_MsdpRxUtilization_Type = Gauge32
_MsdpRxUtilization_Object = MibTableColumn
msdpRxUtilization = _MsdpRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 3, 1, 11),
    _MsdpRxUtilization_Type()
)
msdpRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpRxUtilization.setStatus("current")
_MsEthernetTable_Object = MibTable
msEthernetTable = _MsEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    msEthernetTable.setStatus("current")
_MsEthernetEntry_Object = MibTableRow
msEthernetEntry = _MsEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 4, 1)
)
msEthernetEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mseMacIndex"),
    (0, "CODIMA-EXPRESS-MIB", "mseTimeStampIndex"),
)
if mibBuilder.loadTexts:
    msEthernetEntry.setStatus("current")
_MseMacIndex_Type = MacAddress
_MseMacIndex_Object = MibTableColumn
mseMacIndex = _MseMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 4, 1, 1),
    _MseMacIndex_Type()
)
mseMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mseMacIndex.setStatus("current")
_MseTimeStampIndex_Type = Unsigned32
_MseTimeStampIndex_Object = MibTableColumn
mseTimeStampIndex = _MseTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 4, 1, 2),
    _MseTimeStampIndex_Type()
)
mseTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mseTimeStampIndex.setStatus("current")


class _MseTimeStamp_Type(DisplayString):
    """Custom type mseTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MseTimeStamp_Type.__name__ = "DisplayString"
_MseTimeStamp_Object = MibTableColumn
mseTimeStamp = _MseTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 4, 1, 3),
    _MseTimeStamp_Type()
)
mseTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mseTimeStamp.setStatus("current")
_MseRunts_Type = Counter32
_MseRunts_Object = MibTableColumn
mseRunts = _MseRunts_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 4, 1, 4),
    _MseRunts_Type()
)
mseRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mseRunts.setStatus("current")
_MseJabbers_Type = Counter32
_MseJabbers_Object = MibTableColumn
mseJabbers = _MseJabbers_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 4, 1, 5),
    _MseJabbers_Type()
)
mseJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mseJabbers.setStatus("current")
_MseCrc_Type = Counter32
_MseCrc_Object = MibTableColumn
mseCrc = _MseCrc_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 4, 1, 6),
    _MseCrc_Type()
)
mseCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mseCrc.setStatus("current")
_MseCollisions_Type = Counter32
_MseCollisions_Object = MibTableColumn
mseCollisions = _MseCollisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 4, 1, 7),
    _MseCollisions_Type()
)
mseCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mseCollisions.setStatus("current")
_MseLateCollisions_Type = Counter32
_MseLateCollisions_Object = MibTableColumn
mseLateCollisions = _MseLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 4, 1, 8),
    _MseLateCollisions_Type()
)
mseLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mseLateCollisions.setStatus("current")
_MsIcmpTable_Object = MibTable
msIcmpTable = _MsIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    msIcmpTable.setStatus("current")
_MsIcmpEntry_Object = MibTableRow
msIcmpEntry = _MsIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1)
)
msIcmpEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "msiMacIndex"),
    (0, "CODIMA-EXPRESS-MIB", "msiTimeStampIndex"),
)
if mibBuilder.loadTexts:
    msIcmpEntry.setStatus("current")
_MsiMacIndex_Type = MacAddress
_MsiMacIndex_Object = MibTableColumn
msiMacIndex = _MsiMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 1),
    _MsiMacIndex_Type()
)
msiMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiMacIndex.setStatus("current")
_MsiTimeStampIndex_Type = Unsigned32
_MsiTimeStampIndex_Object = MibTableColumn
msiTimeStampIndex = _MsiTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 2),
    _MsiTimeStampIndex_Type()
)
msiTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiTimeStampIndex.setStatus("current")


class _MsiTimeStamp_Type(DisplayString):
    """Custom type msiTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MsiTimeStamp_Type.__name__ = "DisplayString"
_MsiTimeStamp_Object = MibTableColumn
msiTimeStamp = _MsiTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 3),
    _MsiTimeStamp_Type()
)
msiTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiTimeStamp.setStatus("current")
_MsiPing_Type = Counter32
_MsiPing_Object = MibTableColumn
msiPing = _MsiPing_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 4),
    _MsiPing_Type()
)
msiPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiPing.setStatus("current")
_MsiSrcQuench_Type = Counter32
_MsiSrcQuench_Object = MibTableColumn
msiSrcQuench = _MsiSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 5),
    _MsiSrcQuench_Type()
)
msiSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiSrcQuench.setStatus("current")
_MsiRedirect_Type = Counter32
_MsiRedirect_Object = MibTableColumn
msiRedirect = _MsiRedirect_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 6),
    _MsiRedirect_Type()
)
msiRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiRedirect.setStatus("current")
_MsiTtlExceeded_Type = Counter32
_MsiTtlExceeded_Object = MibTableColumn
msiTtlExceeded = _MsiTtlExceeded_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 7),
    _MsiTtlExceeded_Type()
)
msiTtlExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiTtlExceeded.setStatus("current")
_MsiParamProblem_Type = Counter32
_MsiParamProblem_Object = MibTableColumn
msiParamProblem = _MsiParamProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 8),
    _MsiParamProblem_Type()
)
msiParamProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiParamProblem.setStatus("current")
_MsiTimestamp_Type = Counter32
_MsiTimestamp_Object = MibTableColumn
msiTimestamp = _MsiTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 9),
    _MsiTimestamp_Type()
)
msiTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiTimestamp.setStatus("current")
_MsiFragTimeout_Type = Counter32
_MsiFragTimeout_Object = MibTableColumn
msiFragTimeout = _MsiFragTimeout_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 10),
    _MsiFragTimeout_Type()
)
msiFragTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiFragTimeout.setStatus("current")
_MsiNetUnreachable_Type = Counter32
_MsiNetUnreachable_Object = MibTableColumn
msiNetUnreachable = _MsiNetUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 11),
    _MsiNetUnreachable_Type()
)
msiNetUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiNetUnreachable.setStatus("current")
_MsiHostUnreachable_Type = Counter32
_MsiHostUnreachable_Object = MibTableColumn
msiHostUnreachable = _MsiHostUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 12),
    _MsiHostUnreachable_Type()
)
msiHostUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiHostUnreachable.setStatus("current")
_MsiProtocolUnreachable_Type = Counter32
_MsiProtocolUnreachable_Object = MibTableColumn
msiProtocolUnreachable = _MsiProtocolUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 13),
    _MsiProtocolUnreachable_Type()
)
msiProtocolUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiProtocolUnreachable.setStatus("current")
_MsiPortUnreachable_Type = Counter32
_MsiPortUnreachable_Object = MibTableColumn
msiPortUnreachable = _MsiPortUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 14),
    _MsiPortUnreachable_Type()
)
msiPortUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiPortUnreachable.setStatus("current")
_MsiFragRequired_Type = Counter32
_MsiFragRequired_Object = MibTableColumn
msiFragRequired = _MsiFragRequired_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 15),
    _MsiFragRequired_Type()
)
msiFragRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiFragRequired.setStatus("current")
_MsiSrcRouteFail_Type = Counter32
_MsiSrcRouteFail_Object = MibTableColumn
msiSrcRouteFail = _MsiSrcRouteFail_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 16),
    _MsiSrcRouteFail_Type()
)
msiSrcRouteFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiSrcRouteFail.setStatus("current")
_MsiDestNetUnknown_Type = Counter32
_MsiDestNetUnknown_Object = MibTableColumn
msiDestNetUnknown = _MsiDestNetUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 17),
    _MsiDestNetUnknown_Type()
)
msiDestNetUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiDestNetUnknown.setStatus("current")
_MsiDestHostUnknown_Type = Counter32
_MsiDestHostUnknown_Object = MibTableColumn
msiDestHostUnknown = _MsiDestHostUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 18),
    _MsiDestHostUnknown_Type()
)
msiDestHostUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiDestHostUnknown.setStatus("current")
_MsiSrcHostIsolated_Type = Counter32
_MsiSrcHostIsolated_Object = MibTableColumn
msiSrcHostIsolated = _MsiSrcHostIsolated_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 19),
    _MsiSrcHostIsolated_Type()
)
msiSrcHostIsolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiSrcHostIsolated.setStatus("current")
_MsiNetProhibited_Type = Counter32
_MsiNetProhibited_Object = MibTableColumn
msiNetProhibited = _MsiNetProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 20),
    _MsiNetProhibited_Type()
)
msiNetProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiNetProhibited.setStatus("current")
_MsiHostProhibited_Type = Counter32
_MsiHostProhibited_Object = MibTableColumn
msiHostProhibited = _MsiHostProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 21),
    _MsiHostProhibited_Type()
)
msiHostProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiHostProhibited.setStatus("current")
_MsiNetTosUnreachable_Type = Counter32
_MsiNetTosUnreachable_Object = MibTableColumn
msiNetTosUnreachable = _MsiNetTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 22),
    _MsiNetTosUnreachable_Type()
)
msiNetTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiNetTosUnreachable.setStatus("current")
_MsiHostTosUnreachable_Type = Counter32
_MsiHostTosUnreachable_Object = MibTableColumn
msiHostTosUnreachable = _MsiHostTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 23),
    _MsiHostTosUnreachable_Type()
)
msiHostTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiHostTosUnreachable.setStatus("current")
_MsiPerformance_Type = Counter32
_MsiPerformance_Object = MibTableColumn
msiPerformance = _MsiPerformance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 24),
    _MsiPerformance_Type()
)
msiPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiPerformance.setStatus("current")
_MsiNetRouteProblem_Type = Counter32
_MsiNetRouteProblem_Object = MibTableColumn
msiNetRouteProblem = _MsiNetRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 25),
    _MsiNetRouteProblem_Type()
)
msiNetRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiNetRouteProblem.setStatus("current")
_MsiHostRouteProblem_Type = Counter32
_MsiHostRouteProblem_Object = MibTableColumn
msiHostRouteProblem = _MsiHostRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 26),
    _MsiHostRouteProblem_Type()
)
msiHostRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiHostRouteProblem.setStatus("current")
_MsiAppRouteProblem_Type = Counter32
_MsiAppRouteProblem_Object = MibTableColumn
msiAppRouteProblem = _MsiAppRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 27),
    _MsiAppRouteProblem_Type()
)
msiAppRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiAppRouteProblem.setStatus("current")
_MsiRouteChange_Type = Counter32
_MsiRouteChange_Object = MibTableColumn
msiRouteChange = _MsiRouteChange_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 28),
    _MsiRouteChange_Type()
)
msiRouteChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiRouteChange.setStatus("current")
_MsiErrors_Type = Counter32
_MsiErrors_Object = MibTableColumn
msiErrors = _MsiErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 29),
    _MsiErrors_Type()
)
msiErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiErrors.setStatus("current")
_MsiMaintenance_Type = Counter32
_MsiMaintenance_Object = MibTableColumn
msiMaintenance = _MsiMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 5, 1, 30),
    _MsiMaintenance_Type()
)
msiMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msiMaintenance.setStatus("current")
_MsProtocolTable_Object = MibTable
msProtocolTable = _MsProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6)
)
if mibBuilder.loadTexts:
    msProtocolTable.setStatus("current")
_MsProtocolEntry_Object = MibTableRow
msProtocolEntry = _MsProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1)
)
msProtocolEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mspMacIndex"),
    (0, "CODIMA-EXPRESS-MIB", "mspTimeStampIndex"),
)
if mibBuilder.loadTexts:
    msProtocolEntry.setStatus("current")
_MspMacIndex_Type = MacAddress
_MspMacIndex_Object = MibTableColumn
mspMacIndex = _MspMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 1),
    _MspMacIndex_Type()
)
mspMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspMacIndex.setStatus("current")
_MspTimeStampIndex_Type = Unsigned32
_MspTimeStampIndex_Object = MibTableColumn
mspTimeStampIndex = _MspTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 2),
    _MspTimeStampIndex_Type()
)
mspTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspTimeStampIndex.setStatus("current")


class _MspTimeStamp_Type(DisplayString):
    """Custom type mspTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MspTimeStamp_Type.__name__ = "DisplayString"
_MspTimeStamp_Object = MibTableColumn
mspTimeStamp = _MspTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 3),
    _MspTimeStamp_Type()
)
mspTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspTimeStamp.setStatus("current")
_MspNovell_Type = Counter32
_MspNovell_Object = MibTableColumn
mspNovell = _MspNovell_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 4),
    _MspNovell_Type()
)
mspNovell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspNovell.setStatus("current")
_MspSnmp_Type = Counter32
_MspSnmp_Object = MibTableColumn
mspSnmp = _MspSnmp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 5),
    _MspSnmp_Type()
)
mspSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspSnmp.setStatus("current")
_MspRouting_Type = Counter32
_MspRouting_Object = MibTableColumn
mspRouting = _MspRouting_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 6),
    _MspRouting_Type()
)
mspRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspRouting.setStatus("current")
_MspWww_Type = Counter32
_MspWww_Object = MibTableColumn
mspWww = _MspWww_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 7),
    _MspWww_Type()
)
mspWww.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspWww.setStatus("current")
_MspIcmp_Type = Counter32
_MspIcmp_Object = MibTableColumn
mspIcmp = _MspIcmp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 8),
    _MspIcmp_Type()
)
mspIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspIcmp.setStatus("current")
_MspIso_Type = Counter32
_MspIso_Object = MibTableColumn
mspIso = _MspIso_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 9),
    _MspIso_Type()
)
mspIso.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspIso.setStatus("current")
_MspMail_Type = Counter32
_MspMail_Object = MibTableColumn
mspMail = _MspMail_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 10),
    _MspMail_Type()
)
mspMail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspMail.setStatus("current")
_MspNetbios_Type = Counter32
_MspNetbios_Object = MibTableColumn
mspNetbios = _MspNetbios_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 11),
    _MspNetbios_Type()
)
mspNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspNetbios.setStatus("current")
_MspDns_Type = Counter32
_MspDns_Object = MibTableColumn
mspDns = _MspDns_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 12),
    _MspDns_Type()
)
mspDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspDns.setStatus("current")
_MspIp_Type = Counter32
_MspIp_Object = MibTableColumn
mspIp = _MspIp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 13),
    _MspIp_Type()
)
mspIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspIp.setStatus("current")
_MspVoip_Type = Counter32
_MspVoip_Object = MibTableColumn
mspVoip = _MspVoip_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 14),
    _MspVoip_Type()
)
mspVoip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspVoip.setStatus("current")
_MspLayer3Traffic_Type = Counter32
_MspLayer3Traffic_Object = MibTableColumn
mspLayer3Traffic = _MspLayer3Traffic_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 15),
    _MspLayer3Traffic_Type()
)
mspLayer3Traffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspLayer3Traffic.setStatus("current")
_MspIpData_Type = Counter32
_MspIpData_Object = MibTableColumn
mspIpData = _MspIpData_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 16),
    _MspIpData_Type()
)
mspIpData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspIpData.setStatus("current")
_MspApplications_Type = Counter32
_MspApplications_Object = MibTableColumn
mspApplications = _MspApplications_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 17),
    _MspApplications_Type()
)
mspApplications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspApplications.setStatus("current")
_MspIpControl_Type = Counter32
_MspIpControl_Object = MibTableColumn
mspIpControl = _MspIpControl_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 18),
    _MspIpControl_Type()
)
mspIpControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspIpControl.setStatus("current")
_MspManagement_Type = Counter32
_MspManagement_Object = MibTableColumn
mspManagement = _MspManagement_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 3, 2, 6, 1, 19),
    _MspManagement_Type()
)
mspManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspManagement.setStatus("current")
_DbMacPeer_ObjectIdentity = ObjectIdentity
dbMacPeer = _DbMacPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dbMacPeer.setStatus("current")
_MacPeerLongTerm_ObjectIdentity = ObjectIdentity
macPeerLongTerm = _MacPeerLongTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    macPeerLongTerm.setStatus("current")
_MplBaseTable_Object = MibTable
mplBaseTable = _MplBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    mplBaseTable.setStatus("current")
_MplBaseEntry_Object = MibTableRow
mplBaseEntry = _MplBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 1, 1)
)
mplBaseEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mplbMac1Index"),
    (0, "CODIMA-EXPRESS-MIB", "mplbMac2Index"),
    (0, "CODIMA-EXPRESS-MIB", "mplbTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mplBaseEntry.setStatus("current")
_MplbMac1Index_Type = MacAddress
_MplbMac1Index_Object = MibTableColumn
mplbMac1Index = _MplbMac1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 1, 1, 1),
    _MplbMac1Index_Type()
)
mplbMac1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplbMac1Index.setStatus("current")
_MplbMac2Index_Type = MacAddress
_MplbMac2Index_Object = MibTableColumn
mplbMac2Index = _MplbMac2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 1, 1, 2),
    _MplbMac2Index_Type()
)
mplbMac2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplbMac2Index.setStatus("current")
_MplbTimeStampIndex_Type = Unsigned32
_MplbTimeStampIndex_Object = MibTableColumn
mplbTimeStampIndex = _MplbTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 1, 1, 3),
    _MplbTimeStampIndex_Type()
)
mplbTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplbTimeStampIndex.setStatus("current")


class _MplbTimeStamp_Type(DisplayString):
    """Custom type mplbTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_MplbTimeStamp_Type.__name__ = "DisplayString"
_MplbTimeStamp_Object = MibTableColumn
mplbTimeStamp = _MplbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 1, 1, 4),
    _MplbTimeStamp_Type()
)
mplbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplbTimeStamp.setStatus("current")
_MplbFrames_Type = Counter32
_MplbFrames_Object = MibTableColumn
mplbFrames = _MplbFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 1, 1, 5),
    _MplbFrames_Type()
)
mplbFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplbFrames.setStatus("current")
_MplbBytes_Type = Counter32
_MplbBytes_Object = MibTableColumn
mplbBytes = _MplbBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 1, 1, 6),
    _MplbBytes_Type()
)
mplbBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplbBytes.setStatus("current")
_MplbFrameSize_Type = Gauge32
_MplbFrameSize_Object = MibTableColumn
mplbFrameSize = _MplbFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 1, 1, 7),
    _MplbFrameSize_Type()
)
mplbFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplbFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    mplbFrameSize.setUnits("bytes")
_MplbHardwareErrors_Type = Counter32
_MplbHardwareErrors_Object = MibTableColumn
mplbHardwareErrors = _MplbHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 1, 1, 8),
    _MplbHardwareErrors_Type()
)
mplbHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplbHardwareErrors.setStatus("current")
_MplbSoftwareErrors_Type = Counter32
_MplbSoftwareErrors_Object = MibTableColumn
mplbSoftwareErrors = _MplbSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 1, 1, 9),
    _MplbSoftwareErrors_Type()
)
mplbSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplbSoftwareErrors.setStatus("current")
_MplDerivedTable_Object = MibTable
mplDerivedTable = _MplDerivedTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    mplDerivedTable.setStatus("current")
_MplDerivedEntry_Object = MibTableRow
mplDerivedEntry = _MplDerivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 2, 1)
)
mplDerivedEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mpldMac1Index"),
    (0, "CODIMA-EXPRESS-MIB", "mpldMac2Index"),
    (0, "CODIMA-EXPRESS-MIB", "mpldTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mplDerivedEntry.setStatus("current")
_MpldMac1Index_Type = MacAddress
_MpldMac1Index_Object = MibTableColumn
mpldMac1Index = _MpldMac1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 2, 1, 1),
    _MpldMac1Index_Type()
)
mpldMac1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpldMac1Index.setStatus("current")
_MpldMac2Index_Type = MacAddress
_MpldMac2Index_Object = MibTableColumn
mpldMac2Index = _MpldMac2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 2, 1, 2),
    _MpldMac2Index_Type()
)
mpldMac2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpldMac2Index.setStatus("current")
_MpldTimeStampIndex_Type = Unsigned32
_MpldTimeStampIndex_Object = MibTableColumn
mpldTimeStampIndex = _MpldTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 2, 1, 3),
    _MpldTimeStampIndex_Type()
)
mpldTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpldTimeStampIndex.setStatus("current")


class _MpldTimeStamp_Type(DisplayString):
    """Custom type mpldTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MpldTimeStamp_Type.__name__ = "DisplayString"
_MpldTimeStamp_Object = MibTableColumn
mpldTimeStamp = _MpldTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 2, 1, 4),
    _MpldTimeStamp_Type()
)
mpldTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpldTimeStamp.setStatus("current")
_MpldUtilization_Type = Gauge32
_MpldUtilization_Object = MibTableColumn
mpldUtilization = _MpldUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 2, 1, 5),
    _MpldUtilization_Type()
)
mpldUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpldUtilization.setStatus("current")
_MpldErrorFrames_Type = Gauge32
_MpldErrorFrames_Object = MibTableColumn
mpldErrorFrames = _MpldErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 2, 1, 6),
    _MpldErrorFrames_Type()
)
mpldErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpldErrorFrames.setStatus("current")
_MplDuplexTable_Object = MibTable
mplDuplexTable = _MplDuplexTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    mplDuplexTable.setStatus("current")
_MplDuplexEntry_Object = MibTableRow
mplDuplexEntry = _MplDuplexEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3, 1)
)
mplDuplexEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mplduMac1Index"),
    (0, "CODIMA-EXPRESS-MIB", "mplduMac2Index"),
    (0, "CODIMA-EXPRESS-MIB", "mplduTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mplDuplexEntry.setStatus("current")
_MplduMac1Index_Type = MacAddress
_MplduMac1Index_Object = MibTableColumn
mplduMac1Index = _MplduMac1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3, 1, 1),
    _MplduMac1Index_Type()
)
mplduMac1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplduMac1Index.setStatus("current")
_MplduMac2Index_Type = MacAddress
_MplduMac2Index_Object = MibTableColumn
mplduMac2Index = _MplduMac2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3, 1, 2),
    _MplduMac2Index_Type()
)
mplduMac2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplduMac2Index.setStatus("current")
_MplduTimeStampIndex_Type = Unsigned32
_MplduTimeStampIndex_Object = MibTableColumn
mplduTimeStampIndex = _MplduTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3, 1, 3),
    _MplduTimeStampIndex_Type()
)
mplduTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplduTimeStampIndex.setStatus("current")


class _MplduTimeStamp_Type(DisplayString):
    """Custom type mplduTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MplduTimeStamp_Type.__name__ = "DisplayString"
_MplduTimeStamp_Object = MibTableColumn
mplduTimeStamp = _MplduTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3, 1, 4),
    _MplduTimeStamp_Type()
)
mplduTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplduTimeStamp.setStatus("current")
_MplduTxFrames_Type = Counter32
_MplduTxFrames_Object = MibTableColumn
mplduTxFrames = _MplduTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3, 1, 5),
    _MplduTxFrames_Type()
)
mplduTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplduTxFrames.setStatus("current")
_MplduTxBytes_Type = Counter32
_MplduTxBytes_Object = MibTableColumn
mplduTxBytes = _MplduTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3, 1, 6),
    _MplduTxBytes_Type()
)
mplduTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplduTxBytes.setStatus("current")
_MplduTxFrameSize_Type = Gauge32
_MplduTxFrameSize_Object = MibTableColumn
mplduTxFrameSize = _MplduTxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3, 1, 7),
    _MplduTxFrameSize_Type()
)
mplduTxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplduTxFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    mplduTxFrameSize.setUnits("bytes")
_MplduTxUtilization_Type = Gauge32
_MplduTxUtilization_Object = MibTableColumn
mplduTxUtilization = _MplduTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3, 1, 8),
    _MplduTxUtilization_Type()
)
mplduTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplduTxUtilization.setStatus("current")
_MplduRxFrames_Type = Counter32
_MplduRxFrames_Object = MibTableColumn
mplduRxFrames = _MplduRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3, 1, 9),
    _MplduRxFrames_Type()
)
mplduRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplduRxFrames.setStatus("current")
_MplduRxBytes_Type = Counter32
_MplduRxBytes_Object = MibTableColumn
mplduRxBytes = _MplduRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3, 1, 10),
    _MplduRxBytes_Type()
)
mplduRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplduRxBytes.setStatus("current")
_MplduRxFrameSize_Type = Gauge32
_MplduRxFrameSize_Object = MibTableColumn
mplduRxFrameSize = _MplduRxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3, 1, 11),
    _MplduRxFrameSize_Type()
)
mplduRxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplduRxFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    mplduRxFrameSize.setUnits("bytes")
_MplduRxUtilization_Type = Gauge32
_MplduRxUtilization_Object = MibTableColumn
mplduRxUtilization = _MplduRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 3, 1, 12),
    _MplduRxUtilization_Type()
)
mplduRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplduRxUtilization.setStatus("current")
_MplProtocolTable_Object = MibTable
mplProtocolTable = _MplProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    mplProtocolTable.setStatus("current")
_MplProtocolEntry_Object = MibTableRow
mplProtocolEntry = _MplProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1)
)
mplProtocolEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mplpMac1Index"),
    (0, "CODIMA-EXPRESS-MIB", "mplpMac2Index"),
    (0, "CODIMA-EXPRESS-MIB", "mplpTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mplProtocolEntry.setStatus("current")
_MplpMac1Index_Type = MacAddress
_MplpMac1Index_Object = MibTableColumn
mplpMac1Index = _MplpMac1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 1),
    _MplpMac1Index_Type()
)
mplpMac1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpMac1Index.setStatus("current")
_MplpMac2Index_Type = MacAddress
_MplpMac2Index_Object = MibTableColumn
mplpMac2Index = _MplpMac2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 2),
    _MplpMac2Index_Type()
)
mplpMac2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpMac2Index.setStatus("current")
_MplpTimeStampIndex_Type = Unsigned32
_MplpTimeStampIndex_Object = MibTableColumn
mplpTimeStampIndex = _MplpTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 3),
    _MplpTimeStampIndex_Type()
)
mplpTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpTimeStampIndex.setStatus("current")


class _MplpTimeStamp_Type(DisplayString):
    """Custom type mplpTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MplpTimeStamp_Type.__name__ = "DisplayString"
_MplpTimeStamp_Object = MibTableColumn
mplpTimeStamp = _MplpTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 4),
    _MplpTimeStamp_Type()
)
mplpTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpTimeStamp.setStatus("current")
_MplpNovell_Type = Counter32
_MplpNovell_Object = MibTableColumn
mplpNovell = _MplpNovell_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 5),
    _MplpNovell_Type()
)
mplpNovell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpNovell.setStatus("current")
_MplpSnmp_Type = Counter32
_MplpSnmp_Object = MibTableColumn
mplpSnmp = _MplpSnmp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 6),
    _MplpSnmp_Type()
)
mplpSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpSnmp.setStatus("current")
_MplpRouting_Type = Counter32
_MplpRouting_Object = MibTableColumn
mplpRouting = _MplpRouting_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 7),
    _MplpRouting_Type()
)
mplpRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpRouting.setStatus("current")
_MplpWww_Type = Counter32
_MplpWww_Object = MibTableColumn
mplpWww = _MplpWww_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 8),
    _MplpWww_Type()
)
mplpWww.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpWww.setStatus("current")
_MplpIcmp_Type = Counter32
_MplpIcmp_Object = MibTableColumn
mplpIcmp = _MplpIcmp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 9),
    _MplpIcmp_Type()
)
mplpIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpIcmp.setStatus("current")
_MplpIso_Type = Counter32
_MplpIso_Object = MibTableColumn
mplpIso = _MplpIso_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 10),
    _MplpIso_Type()
)
mplpIso.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpIso.setStatus("current")
_MplpMail_Type = Counter32
_MplpMail_Object = MibTableColumn
mplpMail = _MplpMail_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 11),
    _MplpMail_Type()
)
mplpMail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpMail.setStatus("current")
_MplpNetbios_Type = Counter32
_MplpNetbios_Object = MibTableColumn
mplpNetbios = _MplpNetbios_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 12),
    _MplpNetbios_Type()
)
mplpNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpNetbios.setStatus("current")
_MplpDns_Type = Counter32
_MplpDns_Object = MibTableColumn
mplpDns = _MplpDns_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 13),
    _MplpDns_Type()
)
mplpDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpDns.setStatus("current")
_MplpIp_Type = Counter32
_MplpIp_Object = MibTableColumn
mplpIp = _MplpIp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 14),
    _MplpIp_Type()
)
mplpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpIp.setStatus("current")
_MplpVoip_Type = Counter32
_MplpVoip_Object = MibTableColumn
mplpVoip = _MplpVoip_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 15),
    _MplpVoip_Type()
)
mplpVoip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpVoip.setStatus("current")
_MplpLayer3Traffic_Type = Counter32
_MplpLayer3Traffic_Object = MibTableColumn
mplpLayer3Traffic = _MplpLayer3Traffic_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 16),
    _MplpLayer3Traffic_Type()
)
mplpLayer3Traffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpLayer3Traffic.setStatus("current")
_MplpIpData_Type = Counter32
_MplpIpData_Object = MibTableColumn
mplpIpData = _MplpIpData_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 17),
    _MplpIpData_Type()
)
mplpIpData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpIpData.setStatus("current")
_MplpApplications_Type = Counter32
_MplpApplications_Object = MibTableColumn
mplpApplications = _MplpApplications_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 18),
    _MplpApplications_Type()
)
mplpApplications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpApplications.setStatus("current")
_MplpIpControl_Type = Counter32
_MplpIpControl_Object = MibTableColumn
mplpIpControl = _MplpIpControl_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 19),
    _MplpIpControl_Type()
)
mplpIpControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpIpControl.setStatus("current")
_MplpManagement_Type = Counter32
_MplpManagement_Object = MibTableColumn
mplpManagement = _MplpManagement_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 1, 4, 1, 20),
    _MplpManagement_Type()
)
mplpManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplpManagement.setStatus("current")
_MacPeerShortTerm_ObjectIdentity = ObjectIdentity
macPeerShortTerm = _MacPeerShortTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    macPeerShortTerm.setStatus("current")
_MpsBaseTable_Object = MibTable
mpsBaseTable = _MpsBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mpsBaseTable.setStatus("current")
_MpsBaseEntry_Object = MibTableRow
mpsBaseEntry = _MpsBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 1, 1)
)
mpsBaseEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mpsbMac1Index"),
    (0, "CODIMA-EXPRESS-MIB", "mpsbMac2Index"),
    (0, "CODIMA-EXPRESS-MIB", "mpsbTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mpsBaseEntry.setStatus("current")
_MpsbMac1Index_Type = MacAddress
_MpsbMac1Index_Object = MibTableColumn
mpsbMac1Index = _MpsbMac1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 1, 1, 1),
    _MpsbMac1Index_Type()
)
mpsbMac1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsbMac1Index.setStatus("current")
_MpsbMac2Index_Type = MacAddress
_MpsbMac2Index_Object = MibTableColumn
mpsbMac2Index = _MpsbMac2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 1, 1, 2),
    _MpsbMac2Index_Type()
)
mpsbMac2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsbMac2Index.setStatus("current")
_MpsbTimeStampIndex_Type = Unsigned32
_MpsbTimeStampIndex_Object = MibTableColumn
mpsbTimeStampIndex = _MpsbTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 1, 1, 3),
    _MpsbTimeStampIndex_Type()
)
mpsbTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsbTimeStampIndex.setStatus("current")


class _MpsbTimeStamp_Type(DisplayString):
    """Custom type mpsbTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MpsbTimeStamp_Type.__name__ = "DisplayString"
_MpsbTimeStamp_Object = MibTableColumn
mpsbTimeStamp = _MpsbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 1, 1, 4),
    _MpsbTimeStamp_Type()
)
mpsbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsbTimeStamp.setStatus("current")
_MpsbFrames_Type = Counter32
_MpsbFrames_Object = MibTableColumn
mpsbFrames = _MpsbFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 1, 1, 5),
    _MpsbFrames_Type()
)
mpsbFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsbFrames.setStatus("current")
_MpsbBytes_Type = Counter32
_MpsbBytes_Object = MibTableColumn
mpsbBytes = _MpsbBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 1, 1, 6),
    _MpsbBytes_Type()
)
mpsbBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsbBytes.setStatus("current")
_MpsbFrameSize_Type = Gauge32
_MpsbFrameSize_Object = MibTableColumn
mpsbFrameSize = _MpsbFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 1, 1, 7),
    _MpsbFrameSize_Type()
)
mpsbFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsbFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    mpsbFrameSize.setUnits("bytes")
_MpsbHardwareErrors_Type = Counter32
_MpsbHardwareErrors_Object = MibTableColumn
mpsbHardwareErrors = _MpsbHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 1, 1, 8),
    _MpsbHardwareErrors_Type()
)
mpsbHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsbHardwareErrors.setStatus("current")
_MpsbSoftwareErrors_Type = Counter32
_MpsbSoftwareErrors_Object = MibTableColumn
mpsbSoftwareErrors = _MpsbSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 1, 1, 9),
    _MpsbSoftwareErrors_Type()
)
mpsbSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsbSoftwareErrors.setStatus("current")
_MpsDerivedTable_Object = MibTable
mpsDerivedTable = _MpsDerivedTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    mpsDerivedTable.setStatus("current")
_MpsDerivedEntry_Object = MibTableRow
mpsDerivedEntry = _MpsDerivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 2, 1)
)
mpsDerivedEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mpsdMac1Index"),
    (0, "CODIMA-EXPRESS-MIB", "mpsdMac2Index"),
    (0, "CODIMA-EXPRESS-MIB", "mpsdTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mpsDerivedEntry.setStatus("current")
_MpsdMac1Index_Type = MacAddress
_MpsdMac1Index_Object = MibTableColumn
mpsdMac1Index = _MpsdMac1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 2, 1, 1),
    _MpsdMac1Index_Type()
)
mpsdMac1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsdMac1Index.setStatus("current")
_MpsdMac2Index_Type = MacAddress
_MpsdMac2Index_Object = MibTableColumn
mpsdMac2Index = _MpsdMac2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 2, 1, 2),
    _MpsdMac2Index_Type()
)
mpsdMac2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsdMac2Index.setStatus("current")
_MpsdTimeStampIndex_Type = Unsigned32
_MpsdTimeStampIndex_Object = MibTableColumn
mpsdTimeStampIndex = _MpsdTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 2, 1, 3),
    _MpsdTimeStampIndex_Type()
)
mpsdTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsdTimeStampIndex.setStatus("current")


class _MpsdTimeStamp_Type(DisplayString):
    """Custom type mpsdTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MpsdTimeStamp_Type.__name__ = "DisplayString"
_MpsdTimeStamp_Object = MibTableColumn
mpsdTimeStamp = _MpsdTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 2, 1, 4),
    _MpsdTimeStamp_Type()
)
mpsdTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsdTimeStamp.setStatus("current")
_MpsdUtilization_Type = Gauge32
_MpsdUtilization_Object = MibTableColumn
mpsdUtilization = _MpsdUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 2, 1, 5),
    _MpsdUtilization_Type()
)
mpsdUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsdUtilization.setStatus("current")
_MpsdErrorFrames_Type = Gauge32
_MpsdErrorFrames_Object = MibTableColumn
mpsdErrorFrames = _MpsdErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 2, 1, 6),
    _MpsdErrorFrames_Type()
)
mpsdErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsdErrorFrames.setStatus("current")
_MpsDuplexTable_Object = MibTable
mpsDuplexTable = _MpsDuplexTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    mpsDuplexTable.setStatus("current")
_MpsDuplexEntry_Object = MibTableRow
mpsDuplexEntry = _MpsDuplexEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3, 1)
)
mpsDuplexEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mpsduMac1Index"),
    (0, "CODIMA-EXPRESS-MIB", "mpsduMac2Index"),
    (0, "CODIMA-EXPRESS-MIB", "mpsduTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mpsDuplexEntry.setStatus("current")
_MpsduMac1Index_Type = MacAddress
_MpsduMac1Index_Object = MibTableColumn
mpsduMac1Index = _MpsduMac1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3, 1, 1),
    _MpsduMac1Index_Type()
)
mpsduMac1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsduMac1Index.setStatus("current")
_MpsduMac2Index_Type = MacAddress
_MpsduMac2Index_Object = MibTableColumn
mpsduMac2Index = _MpsduMac2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3, 1, 2),
    _MpsduMac2Index_Type()
)
mpsduMac2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsduMac2Index.setStatus("current")
_MpsduTimeStampIndex_Type = Unsigned32
_MpsduTimeStampIndex_Object = MibTableColumn
mpsduTimeStampIndex = _MpsduTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3, 1, 3),
    _MpsduTimeStampIndex_Type()
)
mpsduTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsduTimeStampIndex.setStatus("current")


class _MpsduTimeStamp_Type(DisplayString):
    """Custom type mpsduTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MpsduTimeStamp_Type.__name__ = "DisplayString"
_MpsduTimeStamp_Object = MibTableColumn
mpsduTimeStamp = _MpsduTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3, 1, 4),
    _MpsduTimeStamp_Type()
)
mpsduTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsduTimeStamp.setStatus("current")
_MpsduTxFrames_Type = Counter32
_MpsduTxFrames_Object = MibTableColumn
mpsduTxFrames = _MpsduTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3, 1, 5),
    _MpsduTxFrames_Type()
)
mpsduTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsduTxFrames.setStatus("current")
_MpsduTxBytes_Type = Counter32
_MpsduTxBytes_Object = MibTableColumn
mpsduTxBytes = _MpsduTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3, 1, 6),
    _MpsduTxBytes_Type()
)
mpsduTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsduTxBytes.setStatus("current")
_MpsduTxFrameSize_Type = Gauge32
_MpsduTxFrameSize_Object = MibTableColumn
mpsduTxFrameSize = _MpsduTxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3, 1, 7),
    _MpsduTxFrameSize_Type()
)
mpsduTxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsduTxFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    mpsduTxFrameSize.setUnits("bytes")
_MpsduTxUtilization_Type = Gauge32
_MpsduTxUtilization_Object = MibTableColumn
mpsduTxUtilization = _MpsduTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3, 1, 8),
    _MpsduTxUtilization_Type()
)
mpsduTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsduTxUtilization.setStatus("current")
_MpsduRxFrames_Type = Counter32
_MpsduRxFrames_Object = MibTableColumn
mpsduRxFrames = _MpsduRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3, 1, 9),
    _MpsduRxFrames_Type()
)
mpsduRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsduRxFrames.setStatus("current")
_MpsduRxBytes_Type = Counter32
_MpsduRxBytes_Object = MibTableColumn
mpsduRxBytes = _MpsduRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3, 1, 10),
    _MpsduRxBytes_Type()
)
mpsduRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsduRxBytes.setStatus("current")
_MpsduRxFrameSize_Type = Gauge32
_MpsduRxFrameSize_Object = MibTableColumn
mpsduRxFrameSize = _MpsduRxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3, 1, 11),
    _MpsduRxFrameSize_Type()
)
mpsduRxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsduRxFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    mpsduRxFrameSize.setUnits("bytes")
_MpsduRxUtilization_Type = Gauge32
_MpsduRxUtilization_Object = MibTableColumn
mpsduRxUtilization = _MpsduRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 3, 1, 12),
    _MpsduRxUtilization_Type()
)
mpsduRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsduRxUtilization.setStatus("current")
_MpsProtocolTable_Object = MibTable
mpsProtocolTable = _MpsProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    mpsProtocolTable.setStatus("current")
_MpsProtocolEntry_Object = MibTableRow
mpsProtocolEntry = _MpsProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1)
)
mpsProtocolEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "mpspMac1Index"),
    (0, "CODIMA-EXPRESS-MIB", "mpspMac2Index"),
    (0, "CODIMA-EXPRESS-MIB", "mpspTimeStampIndex"),
)
if mibBuilder.loadTexts:
    mpsProtocolEntry.setStatus("current")
_MpspMac1Index_Type = MacAddress
_MpspMac1Index_Object = MibTableColumn
mpspMac1Index = _MpspMac1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 1),
    _MpspMac1Index_Type()
)
mpspMac1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspMac1Index.setStatus("current")
_MpspMac2Index_Type = MacAddress
_MpspMac2Index_Object = MibTableColumn
mpspMac2Index = _MpspMac2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 2),
    _MpspMac2Index_Type()
)
mpspMac2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspMac2Index.setStatus("current")
_MpspTimeStampIndex_Type = Unsigned32
_MpspTimeStampIndex_Object = MibTableColumn
mpspTimeStampIndex = _MpspTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 3),
    _MpspTimeStampIndex_Type()
)
mpspTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspTimeStampIndex.setStatus("current")


class _MpspTimeStamp_Type(DisplayString):
    """Custom type mpspTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MpspTimeStamp_Type.__name__ = "DisplayString"
_MpspTimeStamp_Object = MibTableColumn
mpspTimeStamp = _MpspTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 4),
    _MpspTimeStamp_Type()
)
mpspTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspTimeStamp.setStatus("current")
_MpspNovell_Type = Counter32
_MpspNovell_Object = MibTableColumn
mpspNovell = _MpspNovell_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 5),
    _MpspNovell_Type()
)
mpspNovell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspNovell.setStatus("current")
_MpspSnmp_Type = Counter32
_MpspSnmp_Object = MibTableColumn
mpspSnmp = _MpspSnmp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 6),
    _MpspSnmp_Type()
)
mpspSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspSnmp.setStatus("current")
_MpspRouting_Type = Counter32
_MpspRouting_Object = MibTableColumn
mpspRouting = _MpspRouting_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 7),
    _MpspRouting_Type()
)
mpspRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspRouting.setStatus("current")
_MpspWww_Type = Counter32
_MpspWww_Object = MibTableColumn
mpspWww = _MpspWww_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 8),
    _MpspWww_Type()
)
mpspWww.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspWww.setStatus("current")
_MpspIcmp_Type = Counter32
_MpspIcmp_Object = MibTableColumn
mpspIcmp = _MpspIcmp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 9),
    _MpspIcmp_Type()
)
mpspIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspIcmp.setStatus("current")
_MpspIso_Type = Counter32
_MpspIso_Object = MibTableColumn
mpspIso = _MpspIso_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 10),
    _MpspIso_Type()
)
mpspIso.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspIso.setStatus("current")
_MpspMail_Type = Counter32
_MpspMail_Object = MibTableColumn
mpspMail = _MpspMail_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 11),
    _MpspMail_Type()
)
mpspMail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspMail.setStatus("current")
_MpspNetbios_Type = Counter32
_MpspNetbios_Object = MibTableColumn
mpspNetbios = _MpspNetbios_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 12),
    _MpspNetbios_Type()
)
mpspNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspNetbios.setStatus("current")
_MpspDns_Type = Counter32
_MpspDns_Object = MibTableColumn
mpspDns = _MpspDns_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 13),
    _MpspDns_Type()
)
mpspDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspDns.setStatus("current")
_MpspIp_Type = Counter32
_MpspIp_Object = MibTableColumn
mpspIp = _MpspIp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 14),
    _MpspIp_Type()
)
mpspIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspIp.setStatus("current")
_MpspVoip_Type = Counter32
_MpspVoip_Object = MibTableColumn
mpspVoip = _MpspVoip_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 15),
    _MpspVoip_Type()
)
mpspVoip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspVoip.setStatus("current")
_MpspLayer3Traffic_Type = Counter32
_MpspLayer3Traffic_Object = MibTableColumn
mpspLayer3Traffic = _MpspLayer3Traffic_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 16),
    _MpspLayer3Traffic_Type()
)
mpspLayer3Traffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspLayer3Traffic.setStatus("current")
_MpspIpData_Type = Counter32
_MpspIpData_Object = MibTableColumn
mpspIpData = _MpspIpData_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 17),
    _MpspIpData_Type()
)
mpspIpData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspIpData.setStatus("current")
_MpspApplications_Type = Counter32
_MpspApplications_Object = MibTableColumn
mpspApplications = _MpspApplications_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 18),
    _MpspApplications_Type()
)
mpspApplications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspApplications.setStatus("current")
_MpspIpControl_Type = Counter32
_MpspIpControl_Object = MibTableColumn
mpspIpControl = _MpspIpControl_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 19),
    _MpspIpControl_Type()
)
mpspIpControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspIpControl.setStatus("current")
_MpspManagement_Type = Counter32
_MpspManagement_Object = MibTableColumn
mpspManagement = _MpspManagement_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 4, 2, 4, 1, 20),
    _MpspManagement_Type()
)
mpspManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpspManagement.setStatus("current")
_DbIPv4_ObjectIdentity = ObjectIdentity
dbIPv4 = _DbIPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dbIPv4.setStatus("current")
_IpLongTerm_ObjectIdentity = ObjectIdentity
ipLongTerm = _IpLongTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ipLongTerm.setStatus("current")
_IlBaseTable_Object = MibTable
ilBaseTable = _IlBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ilBaseTable.setStatus("current")
_IlBaseEntry_Object = MibTableRow
ilBaseEntry = _IlBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 1, 1)
)
ilBaseEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "ilbIpIndex"),
    (0, "CODIMA-EXPRESS-MIB", "ilbTimeStampIndex"),
)
if mibBuilder.loadTexts:
    ilBaseEntry.setStatus("current")
_IlbIpIndex_Type = IpAddress
_IlbIpIndex_Object = MibTableColumn
ilbIpIndex = _IlbIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 1, 1, 1),
    _IlbIpIndex_Type()
)
ilbIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilbIpIndex.setStatus("current")
_IlbTimeStampIndex_Type = Unsigned32
_IlbTimeStampIndex_Object = MibTableColumn
ilbTimeStampIndex = _IlbTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 1, 1, 2),
    _IlbTimeStampIndex_Type()
)
ilbTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilbTimeStampIndex.setStatus("current")


class _IlbTimeStamp_Type(DisplayString):
    """Custom type ilbTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IlbTimeStamp_Type.__name__ = "DisplayString"
_IlbTimeStamp_Object = MibTableColumn
ilbTimeStamp = _IlbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 1, 1, 3),
    _IlbTimeStamp_Type()
)
ilbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilbTimeStamp.setStatus("current")
_IlbFrames_Type = Counter32
_IlbFrames_Object = MibTableColumn
ilbFrames = _IlbFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 1, 1, 4),
    _IlbFrames_Type()
)
ilbFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilbFrames.setStatus("current")
_IlbBytes_Type = Counter32
_IlbBytes_Object = MibTableColumn
ilbBytes = _IlbBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 1, 1, 5),
    _IlbBytes_Type()
)
ilbBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilbBytes.setStatus("current")
_IlbFrameSize_Type = Gauge32
_IlbFrameSize_Object = MibTableColumn
ilbFrameSize = _IlbFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 1, 1, 6),
    _IlbFrameSize_Type()
)
ilbFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilbFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    ilbFrameSize.setUnits("bytes")
_IlbHardwareErrors_Type = Counter32
_IlbHardwareErrors_Object = MibTableColumn
ilbHardwareErrors = _IlbHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 1, 1, 7),
    _IlbHardwareErrors_Type()
)
ilbHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilbHardwareErrors.setStatus("current")
_IlbSoftwareErrors_Type = Counter32
_IlbSoftwareErrors_Object = MibTableColumn
ilbSoftwareErrors = _IlbSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 1, 1, 8),
    _IlbSoftwareErrors_Type()
)
ilbSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilbSoftwareErrors.setStatus("current")
_IlDerivedTable_Object = MibTable
ilDerivedTable = _IlDerivedTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ilDerivedTable.setStatus("current")
_IlDerivedEntry_Object = MibTableRow
ilDerivedEntry = _IlDerivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 2, 1)
)
ilDerivedEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "ildIpIndex"),
    (0, "CODIMA-EXPRESS-MIB", "ildTimeStampIndex"),
)
if mibBuilder.loadTexts:
    ilDerivedEntry.setStatus("current")
_IldIpIndex_Type = IpAddress
_IldIpIndex_Object = MibTableColumn
ildIpIndex = _IldIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 2, 1, 1),
    _IldIpIndex_Type()
)
ildIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ildIpIndex.setStatus("current")
_IldTimeStampIndex_Type = Unsigned32
_IldTimeStampIndex_Object = MibTableColumn
ildTimeStampIndex = _IldTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 2, 1, 2),
    _IldTimeStampIndex_Type()
)
ildTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ildTimeStampIndex.setStatus("current")


class _IldTimeStamp_Type(DisplayString):
    """Custom type ildTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IldTimeStamp_Type.__name__ = "DisplayString"
_IldTimeStamp_Object = MibTableColumn
ildTimeStamp = _IldTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 2, 1, 3),
    _IldTimeStamp_Type()
)
ildTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ildTimeStamp.setStatus("current")
_IldUtilization_Type = Gauge32
_IldUtilization_Object = MibTableColumn
ildUtilization = _IldUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 2, 1, 4),
    _IldUtilization_Type()
)
ildUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ildUtilization.setStatus("current")
_IldErrorFrames_Type = Gauge32
_IldErrorFrames_Object = MibTableColumn
ildErrorFrames = _IldErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 2, 1, 5),
    _IldErrorFrames_Type()
)
ildErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ildErrorFrames.setStatus("current")
_IlIcmpTable_Object = MibTable
ilIcmpTable = _IlIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    ilIcmpTable.setStatus("current")
_IlIcmpEntry_Object = MibTableRow
ilIcmpEntry = _IlIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1)
)
ilIcmpEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "iliTimeStampIndex"),
)
if mibBuilder.loadTexts:
    ilIcmpEntry.setStatus("current")
_IliIpIndex_Type = IpAddress
_IliIpIndex_Object = MibTableColumn
iliIpIndex = _IliIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 1),
    _IliIpIndex_Type()
)
iliIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliIpIndex.setStatus("current")
_IliTimeStampIndex_Type = Unsigned32
_IliTimeStampIndex_Object = MibTableColumn
iliTimeStampIndex = _IliTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 2),
    _IliTimeStampIndex_Type()
)
iliTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliTimeStampIndex.setStatus("current")


class _IliTimeStamp_Type(DisplayString):
    """Custom type iliTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IliTimeStamp_Type.__name__ = "DisplayString"
_IliTimeStamp_Object = MibTableColumn
iliTimeStamp = _IliTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 3),
    _IliTimeStamp_Type()
)
iliTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliTimeStamp.setStatus("current")
_IliPing_Type = Counter32
_IliPing_Object = MibTableColumn
iliPing = _IliPing_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 4),
    _IliPing_Type()
)
iliPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliPing.setStatus("current")
_IliSrcQuench_Type = Counter32
_IliSrcQuench_Object = MibTableColumn
iliSrcQuench = _IliSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 5),
    _IliSrcQuench_Type()
)
iliSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliSrcQuench.setStatus("current")
_IliRedirect_Type = Counter32
_IliRedirect_Object = MibTableColumn
iliRedirect = _IliRedirect_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 6),
    _IliRedirect_Type()
)
iliRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliRedirect.setStatus("current")
_IliTtlExceeded_Type = Counter32
_IliTtlExceeded_Object = MibTableColumn
iliTtlExceeded = _IliTtlExceeded_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 7),
    _IliTtlExceeded_Type()
)
iliTtlExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliTtlExceeded.setStatus("current")
_IliParamProblem_Type = Counter32
_IliParamProblem_Object = MibTableColumn
iliParamProblem = _IliParamProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 8),
    _IliParamProblem_Type()
)
iliParamProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliParamProblem.setStatus("current")
_IliTimestamp_Type = Counter32
_IliTimestamp_Object = MibTableColumn
iliTimestamp = _IliTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 9),
    _IliTimestamp_Type()
)
iliTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliTimestamp.setStatus("current")
_IliFragTimeout_Type = Counter32
_IliFragTimeout_Object = MibTableColumn
iliFragTimeout = _IliFragTimeout_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 10),
    _IliFragTimeout_Type()
)
iliFragTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliFragTimeout.setStatus("current")
_IliNetUnreachable_Type = Counter32
_IliNetUnreachable_Object = MibTableColumn
iliNetUnreachable = _IliNetUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 11),
    _IliNetUnreachable_Type()
)
iliNetUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliNetUnreachable.setStatus("current")
_IliHostUnreachable_Type = Counter32
_IliHostUnreachable_Object = MibTableColumn
iliHostUnreachable = _IliHostUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 12),
    _IliHostUnreachable_Type()
)
iliHostUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliHostUnreachable.setStatus("current")
_IliProtocolUnreachable_Type = Counter32
_IliProtocolUnreachable_Object = MibTableColumn
iliProtocolUnreachable = _IliProtocolUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 13),
    _IliProtocolUnreachable_Type()
)
iliProtocolUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliProtocolUnreachable.setStatus("current")
_IliPortUnreachable_Type = Counter32
_IliPortUnreachable_Object = MibTableColumn
iliPortUnreachable = _IliPortUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 14),
    _IliPortUnreachable_Type()
)
iliPortUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliPortUnreachable.setStatus("current")
_IliFragRequired_Type = Counter32
_IliFragRequired_Object = MibTableColumn
iliFragRequired = _IliFragRequired_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 15),
    _IliFragRequired_Type()
)
iliFragRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliFragRequired.setStatus("current")
_IliSrcRouteFail_Type = Counter32
_IliSrcRouteFail_Object = MibTableColumn
iliSrcRouteFail = _IliSrcRouteFail_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 16),
    _IliSrcRouteFail_Type()
)
iliSrcRouteFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliSrcRouteFail.setStatus("current")
_IliDestNetUnknown_Type = Counter32
_IliDestNetUnknown_Object = MibTableColumn
iliDestNetUnknown = _IliDestNetUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 17),
    _IliDestNetUnknown_Type()
)
iliDestNetUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliDestNetUnknown.setStatus("current")
_IliDestHostUnknown_Type = Counter32
_IliDestHostUnknown_Object = MibTableColumn
iliDestHostUnknown = _IliDestHostUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 18),
    _IliDestHostUnknown_Type()
)
iliDestHostUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliDestHostUnknown.setStatus("current")
_IliSrcHostIsolated_Type = Counter32
_IliSrcHostIsolated_Object = MibTableColumn
iliSrcHostIsolated = _IliSrcHostIsolated_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 19),
    _IliSrcHostIsolated_Type()
)
iliSrcHostIsolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliSrcHostIsolated.setStatus("current")
_IliNetProhibited_Type = Counter32
_IliNetProhibited_Object = MibTableColumn
iliNetProhibited = _IliNetProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 20),
    _IliNetProhibited_Type()
)
iliNetProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliNetProhibited.setStatus("current")
_IliHostProhibited_Type = Counter32
_IliHostProhibited_Object = MibTableColumn
iliHostProhibited = _IliHostProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 21),
    _IliHostProhibited_Type()
)
iliHostProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliHostProhibited.setStatus("current")
_IliNetTosUnreachable_Type = Counter32
_IliNetTosUnreachable_Object = MibTableColumn
iliNetTosUnreachable = _IliNetTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 22),
    _IliNetTosUnreachable_Type()
)
iliNetTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliNetTosUnreachable.setStatus("current")
_IliHostTosUnreachable_Type = Counter32
_IliHostTosUnreachable_Object = MibTableColumn
iliHostTosUnreachable = _IliHostTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 23),
    _IliHostTosUnreachable_Type()
)
iliHostTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliHostTosUnreachable.setStatus("current")
_IliPerformance_Type = Counter32
_IliPerformance_Object = MibTableColumn
iliPerformance = _IliPerformance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 24),
    _IliPerformance_Type()
)
iliPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliPerformance.setStatus("current")
_IliNetRouteProblem_Type = Counter32
_IliNetRouteProblem_Object = MibTableColumn
iliNetRouteProblem = _IliNetRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 25),
    _IliNetRouteProblem_Type()
)
iliNetRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliNetRouteProblem.setStatus("current")
_IliHostRouteProblem_Type = Counter32
_IliHostRouteProblem_Object = MibTableColumn
iliHostRouteProblem = _IliHostRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 26),
    _IliHostRouteProblem_Type()
)
iliHostRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliHostRouteProblem.setStatus("current")
_IliAppRouteProblem_Type = Counter32
_IliAppRouteProblem_Object = MibTableColumn
iliAppRouteProblem = _IliAppRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 27),
    _IliAppRouteProblem_Type()
)
iliAppRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliAppRouteProblem.setStatus("current")
_IliRouteChange_Type = Counter32
_IliRouteChange_Object = MibTableColumn
iliRouteChange = _IliRouteChange_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 28),
    _IliRouteChange_Type()
)
iliRouteChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliRouteChange.setStatus("current")
_IliErrors_Type = Counter32
_IliErrors_Object = MibTableColumn
iliErrors = _IliErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 29),
    _IliErrors_Type()
)
iliErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliErrors.setStatus("current")
_IliMaintenance_Type = Counter32
_IliMaintenance_Object = MibTableColumn
iliMaintenance = _IliMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 1, 3, 1, 30),
    _IliMaintenance_Type()
)
iliMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iliMaintenance.setStatus("current")
_IpShortTerm_ObjectIdentity = ObjectIdentity
ipShortTerm = _IpShortTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ipShortTerm.setStatus("current")
_IsBaseTable_Object = MibTable
isBaseTable = _IsBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    isBaseTable.setStatus("current")
_IsBaseEntry_Object = MibTableRow
isBaseEntry = _IsBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 1, 1)
)
isBaseEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "isbIpIndex"),
    (0, "CODIMA-EXPRESS-MIB", "isbTimeStampIndex"),
)
if mibBuilder.loadTexts:
    isBaseEntry.setStatus("current")
_IsbIpIndex_Type = IpAddress
_IsbIpIndex_Object = MibTableColumn
isbIpIndex = _IsbIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 1, 1, 1),
    _IsbIpIndex_Type()
)
isbIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isbIpIndex.setStatus("current")
_IsbTimeStampIndex_Type = Unsigned32
_IsbTimeStampIndex_Object = MibTableColumn
isbTimeStampIndex = _IsbTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 1, 1, 2),
    _IsbTimeStampIndex_Type()
)
isbTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isbTimeStampIndex.setStatus("current")


class _IsbTimeStamp_Type(DisplayString):
    """Custom type isbTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IsbTimeStamp_Type.__name__ = "DisplayString"
_IsbTimeStamp_Object = MibTableColumn
isbTimeStamp = _IsbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 1, 1, 3),
    _IsbTimeStamp_Type()
)
isbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isbTimeStamp.setStatus("current")
_IsbFrames_Type = Counter32
_IsbFrames_Object = MibTableColumn
isbFrames = _IsbFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 1, 1, 4),
    _IsbFrames_Type()
)
isbFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isbFrames.setStatus("current")
_IsbBytes_Type = Counter32
_IsbBytes_Object = MibTableColumn
isbBytes = _IsbBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 1, 1, 5),
    _IsbBytes_Type()
)
isbBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isbBytes.setStatus("current")
_IsbFrameSize_Type = Gauge32
_IsbFrameSize_Object = MibTableColumn
isbFrameSize = _IsbFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 1, 1, 6),
    _IsbFrameSize_Type()
)
isbFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isbFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    isbFrameSize.setUnits("bytes")
_IsbHardwareErrors_Type = Counter32
_IsbHardwareErrors_Object = MibTableColumn
isbHardwareErrors = _IsbHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 1, 1, 7),
    _IsbHardwareErrors_Type()
)
isbHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isbHardwareErrors.setStatus("current")
_IsbSoftwareErrors_Type = Counter32
_IsbSoftwareErrors_Object = MibTableColumn
isbSoftwareErrors = _IsbSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 1, 1, 8),
    _IsbSoftwareErrors_Type()
)
isbSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isbSoftwareErrors.setStatus("current")
_IsDerivedTable_Object = MibTable
isDerivedTable = _IsDerivedTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    isDerivedTable.setStatus("current")
_IsDerivedEntry_Object = MibTableRow
isDerivedEntry = _IsDerivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 2, 1)
)
isDerivedEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "isdIpIndex"),
    (0, "CODIMA-EXPRESS-MIB", "isdTimeStampIndex"),
)
if mibBuilder.loadTexts:
    isDerivedEntry.setStatus("current")
_IsdIpIndex_Type = IpAddress
_IsdIpIndex_Object = MibTableColumn
isdIpIndex = _IsdIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 2, 1, 1),
    _IsdIpIndex_Type()
)
isdIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdIpIndex.setStatus("current")
_IsdTimeStampIndex_Type = Unsigned32
_IsdTimeStampIndex_Object = MibTableColumn
isdTimeStampIndex = _IsdTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 2, 1, 2),
    _IsdTimeStampIndex_Type()
)
isdTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdTimeStampIndex.setStatus("current")


class _IsdTimeStamp_Type(DisplayString):
    """Custom type isdTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IsdTimeStamp_Type.__name__ = "DisplayString"
_IsdTimeStamp_Object = MibTableColumn
isdTimeStamp = _IsdTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 2, 1, 3),
    _IsdTimeStamp_Type()
)
isdTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdTimeStamp.setStatus("current")
_IsdUtilization_Type = Gauge32
_IsdUtilization_Object = MibTableColumn
isdUtilization = _IsdUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 2, 1, 4),
    _IsdUtilization_Type()
)
isdUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdUtilization.setStatus("current")
_IsdErrorFrames_Type = Gauge32
_IsdErrorFrames_Object = MibTableColumn
isdErrorFrames = _IsdErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 2, 1, 5),
    _IsdErrorFrames_Type()
)
isdErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdErrorFrames.setStatus("current")
_IsIcmpTable_Object = MibTable
isIcmpTable = _IsIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    isIcmpTable.setStatus("current")
_IsIcmpEntry_Object = MibTableRow
isIcmpEntry = _IsIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1)
)
isIcmpEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "isiTimeStampIndex"),
)
if mibBuilder.loadTexts:
    isIcmpEntry.setStatus("current")
_IsiIpIndex_Type = IpAddress
_IsiIpIndex_Object = MibTableColumn
isiIpIndex = _IsiIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 1),
    _IsiIpIndex_Type()
)
isiIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiIpIndex.setStatus("current")
_IsiTimeStampIndex_Type = Unsigned32
_IsiTimeStampIndex_Object = MibTableColumn
isiTimeStampIndex = _IsiTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 2),
    _IsiTimeStampIndex_Type()
)
isiTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiTimeStampIndex.setStatus("current")


class _IsiTimeStamp_Type(DisplayString):
    """Custom type isiTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IsiTimeStamp_Type.__name__ = "DisplayString"
_IsiTimeStamp_Object = MibTableColumn
isiTimeStamp = _IsiTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 3),
    _IsiTimeStamp_Type()
)
isiTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiTimeStamp.setStatus("current")
_IsiPing_Type = Counter32
_IsiPing_Object = MibTableColumn
isiPing = _IsiPing_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 4),
    _IsiPing_Type()
)
isiPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiPing.setStatus("current")
_IsiSrcQuench_Type = Counter32
_IsiSrcQuench_Object = MibTableColumn
isiSrcQuench = _IsiSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 5),
    _IsiSrcQuench_Type()
)
isiSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiSrcQuench.setStatus("current")
_IsiRedirect_Type = Counter32
_IsiRedirect_Object = MibTableColumn
isiRedirect = _IsiRedirect_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 6),
    _IsiRedirect_Type()
)
isiRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiRedirect.setStatus("current")
_IsiTtlExceeded_Type = Counter32
_IsiTtlExceeded_Object = MibTableColumn
isiTtlExceeded = _IsiTtlExceeded_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 7),
    _IsiTtlExceeded_Type()
)
isiTtlExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiTtlExceeded.setStatus("current")
_IsiParamProblem_Type = Counter32
_IsiParamProblem_Object = MibTableColumn
isiParamProblem = _IsiParamProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 8),
    _IsiParamProblem_Type()
)
isiParamProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiParamProblem.setStatus("current")
_IsiTimestamp_Type = Counter32
_IsiTimestamp_Object = MibTableColumn
isiTimestamp = _IsiTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 9),
    _IsiTimestamp_Type()
)
isiTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiTimestamp.setStatus("current")
_IsiFragTimeout_Type = Counter32
_IsiFragTimeout_Object = MibTableColumn
isiFragTimeout = _IsiFragTimeout_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 10),
    _IsiFragTimeout_Type()
)
isiFragTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiFragTimeout.setStatus("current")
_IsiNetUnreachable_Type = Counter32
_IsiNetUnreachable_Object = MibTableColumn
isiNetUnreachable = _IsiNetUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 11),
    _IsiNetUnreachable_Type()
)
isiNetUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiNetUnreachable.setStatus("current")
_IsiHostUnreachable_Type = Counter32
_IsiHostUnreachable_Object = MibTableColumn
isiHostUnreachable = _IsiHostUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 12),
    _IsiHostUnreachable_Type()
)
isiHostUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiHostUnreachable.setStatus("current")
_IsiProtocolUnreachable_Type = Counter32
_IsiProtocolUnreachable_Object = MibTableColumn
isiProtocolUnreachable = _IsiProtocolUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 13),
    _IsiProtocolUnreachable_Type()
)
isiProtocolUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiProtocolUnreachable.setStatus("current")
_IsiPortUnreachable_Type = Counter32
_IsiPortUnreachable_Object = MibTableColumn
isiPortUnreachable = _IsiPortUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 14),
    _IsiPortUnreachable_Type()
)
isiPortUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiPortUnreachable.setStatus("current")
_IsiFragRequired_Type = Counter32
_IsiFragRequired_Object = MibTableColumn
isiFragRequired = _IsiFragRequired_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 15),
    _IsiFragRequired_Type()
)
isiFragRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiFragRequired.setStatus("current")
_IsiSrcRouteFail_Type = Counter32
_IsiSrcRouteFail_Object = MibTableColumn
isiSrcRouteFail = _IsiSrcRouteFail_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 16),
    _IsiSrcRouteFail_Type()
)
isiSrcRouteFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiSrcRouteFail.setStatus("current")
_IsiDestNetUnknown_Type = Counter32
_IsiDestNetUnknown_Object = MibTableColumn
isiDestNetUnknown = _IsiDestNetUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 17),
    _IsiDestNetUnknown_Type()
)
isiDestNetUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiDestNetUnknown.setStatus("current")
_IsiDestHostUnknown_Type = Counter32
_IsiDestHostUnknown_Object = MibTableColumn
isiDestHostUnknown = _IsiDestHostUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 18),
    _IsiDestHostUnknown_Type()
)
isiDestHostUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiDestHostUnknown.setStatus("current")
_IsiSrcHostIsolated_Type = Counter32
_IsiSrcHostIsolated_Object = MibTableColumn
isiSrcHostIsolated = _IsiSrcHostIsolated_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 19),
    _IsiSrcHostIsolated_Type()
)
isiSrcHostIsolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiSrcHostIsolated.setStatus("current")
_IsiNetProhibited_Type = Counter32
_IsiNetProhibited_Object = MibTableColumn
isiNetProhibited = _IsiNetProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 20),
    _IsiNetProhibited_Type()
)
isiNetProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiNetProhibited.setStatus("current")
_IsiHostProhibited_Type = Counter32
_IsiHostProhibited_Object = MibTableColumn
isiHostProhibited = _IsiHostProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 21),
    _IsiHostProhibited_Type()
)
isiHostProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiHostProhibited.setStatus("current")
_IsiNetTosUnreachable_Type = Counter32
_IsiNetTosUnreachable_Object = MibTableColumn
isiNetTosUnreachable = _IsiNetTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 22),
    _IsiNetTosUnreachable_Type()
)
isiNetTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiNetTosUnreachable.setStatus("current")
_IsiHostTosUnreachable_Type = Counter32
_IsiHostTosUnreachable_Object = MibTableColumn
isiHostTosUnreachable = _IsiHostTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 23),
    _IsiHostTosUnreachable_Type()
)
isiHostTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiHostTosUnreachable.setStatus("current")
_IsiPerformance_Type = Counter32
_IsiPerformance_Object = MibTableColumn
isiPerformance = _IsiPerformance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 24),
    _IsiPerformance_Type()
)
isiPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiPerformance.setStatus("current")
_IsiNetRouteProblem_Type = Counter32
_IsiNetRouteProblem_Object = MibTableColumn
isiNetRouteProblem = _IsiNetRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 25),
    _IsiNetRouteProblem_Type()
)
isiNetRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiNetRouteProblem.setStatus("current")
_IsiHostRouteProblem_Type = Counter32
_IsiHostRouteProblem_Object = MibTableColumn
isiHostRouteProblem = _IsiHostRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 26),
    _IsiHostRouteProblem_Type()
)
isiHostRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiHostRouteProblem.setStatus("current")
_IsiAppRouteProblem_Type = Counter32
_IsiAppRouteProblem_Object = MibTableColumn
isiAppRouteProblem = _IsiAppRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 27),
    _IsiAppRouteProblem_Type()
)
isiAppRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiAppRouteProblem.setStatus("current")
_IsiRouteChange_Type = Counter32
_IsiRouteChange_Object = MibTableColumn
isiRouteChange = _IsiRouteChange_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 28),
    _IsiRouteChange_Type()
)
isiRouteChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiRouteChange.setStatus("current")
_IsiErrors_Type = Counter32
_IsiErrors_Object = MibTableColumn
isiErrors = _IsiErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 29),
    _IsiErrors_Type()
)
isiErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiErrors.setStatus("current")
_IsiMaintenance_Type = Counter32
_IsiMaintenance_Object = MibTableColumn
isiMaintenance = _IsiMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 5, 2, 3, 1, 30),
    _IsiMaintenance_Type()
)
isiMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isiMaintenance.setStatus("current")
_DbIPv4Peer_ObjectIdentity = ObjectIdentity
dbIPv4Peer = _DbIPv4Peer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    dbIPv4Peer.setStatus("current")
_IpPeerLongTerm_ObjectIdentity = ObjectIdentity
ipPeerLongTerm = _IpPeerLongTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ipPeerLongTerm.setStatus("current")
_IplBaseTable_Object = MibTable
iplBaseTable = _IplBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    iplBaseTable.setStatus("current")
_IplBaseEntry_Object = MibTableRow
iplBaseEntry = _IplBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 1, 1)
)
iplBaseEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "iplbIp1Index"),
    (0, "CODIMA-EXPRESS-MIB", "iplbIp2Index"),
    (0, "CODIMA-EXPRESS-MIB", "iplbTimeStampIndex"),
)
if mibBuilder.loadTexts:
    iplBaseEntry.setStatus("current")
_IplbIp1Index_Type = IpAddress
_IplbIp1Index_Object = MibTableColumn
iplbIp1Index = _IplbIp1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 1, 1, 1),
    _IplbIp1Index_Type()
)
iplbIp1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iplbIp1Index.setStatus("current")
_IplbIp2Index_Type = IpAddress
_IplbIp2Index_Object = MibTableColumn
iplbIp2Index = _IplbIp2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 1, 1, 2),
    _IplbIp2Index_Type()
)
iplbIp2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iplbIp2Index.setStatus("current")
_IplbTimeStampIndex_Type = Unsigned32
_IplbTimeStampIndex_Object = MibTableColumn
iplbTimeStampIndex = _IplbTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 1, 1, 3),
    _IplbTimeStampIndex_Type()
)
iplbTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iplbTimeStampIndex.setStatus("current")


class _IplbTimeStamp_Type(DisplayString):
    """Custom type iplbTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_IplbTimeStamp_Type.__name__ = "DisplayString"
_IplbTimeStamp_Object = MibTableColumn
iplbTimeStamp = _IplbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 1, 1, 4),
    _IplbTimeStamp_Type()
)
iplbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iplbTimeStamp.setStatus("current")
_IplbFrames_Type = Counter32
_IplbFrames_Object = MibTableColumn
iplbFrames = _IplbFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 1, 1, 5),
    _IplbFrames_Type()
)
iplbFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iplbFrames.setStatus("current")
_IplbBytes_Type = Counter32
_IplbBytes_Object = MibTableColumn
iplbBytes = _IplbBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 1, 1, 6),
    _IplbBytes_Type()
)
iplbBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iplbBytes.setStatus("current")
_IplbFrameSize_Type = Gauge32
_IplbFrameSize_Object = MibTableColumn
iplbFrameSize = _IplbFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 1, 1, 7),
    _IplbFrameSize_Type()
)
iplbFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iplbFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    iplbFrameSize.setUnits("bytes")
_IplbHardwareErrors_Type = Counter32
_IplbHardwareErrors_Object = MibTableColumn
iplbHardwareErrors = _IplbHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 1, 1, 8),
    _IplbHardwareErrors_Type()
)
iplbHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iplbHardwareErrors.setStatus("current")
_IplbSoftwareErrors_Type = Counter32
_IplbSoftwareErrors_Object = MibTableColumn
iplbSoftwareErrors = _IplbSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 1, 1, 9),
    _IplbSoftwareErrors_Type()
)
iplbSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iplbSoftwareErrors.setStatus("current")
_IplDerivedTable_Object = MibTable
iplDerivedTable = _IplDerivedTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    iplDerivedTable.setStatus("current")
_IplDerivedEntry_Object = MibTableRow
iplDerivedEntry = _IplDerivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 2, 1)
)
iplDerivedEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "ipldIp1Index"),
    (0, "CODIMA-EXPRESS-MIB", "ipldIp2Index"),
    (0, "CODIMA-EXPRESS-MIB", "ipldTimeStampIndex"),
)
if mibBuilder.loadTexts:
    iplDerivedEntry.setStatus("current")
_IpldIp1Index_Type = IpAddress
_IpldIp1Index_Object = MibTableColumn
ipldIp1Index = _IpldIp1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 2, 1, 1),
    _IpldIp1Index_Type()
)
ipldIp1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipldIp1Index.setStatus("current")
_IpldIp2Index_Type = IpAddress
_IpldIp2Index_Object = MibTableColumn
ipldIp2Index = _IpldIp2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 2, 1, 2),
    _IpldIp2Index_Type()
)
ipldIp2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipldIp2Index.setStatus("current")
_IpldTimeStampIndex_Type = Unsigned32
_IpldTimeStampIndex_Object = MibTableColumn
ipldTimeStampIndex = _IpldTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 2, 1, 3),
    _IpldTimeStampIndex_Type()
)
ipldTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipldTimeStampIndex.setStatus("current")


class _IpldTimeStamp_Type(DisplayString):
    """Custom type ipldTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IpldTimeStamp_Type.__name__ = "DisplayString"
_IpldTimeStamp_Object = MibTableColumn
ipldTimeStamp = _IpldTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 2, 1, 4),
    _IpldTimeStamp_Type()
)
ipldTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipldTimeStamp.setStatus("current")
_IpldUtilization_Type = Gauge32
_IpldUtilization_Object = MibTableColumn
ipldUtilization = _IpldUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 2, 1, 5),
    _IpldUtilization_Type()
)
ipldUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipldUtilization.setStatus("current")
_IpldErrorFrames_Type = Gauge32
_IpldErrorFrames_Object = MibTableColumn
ipldErrorFrames = _IpldErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 2, 1, 6),
    _IpldErrorFrames_Type()
)
ipldErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipldErrorFrames.setStatus("current")
_IplIcmpTable_Object = MibTable
iplIcmpTable = _IplIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    iplIcmpTable.setStatus("current")
_IplIcmpEntry_Object = MibTableRow
iplIcmpEntry = _IplIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1)
)
iplIcmpEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "ipliIp1Index"),
    (0, "CODIMA-EXPRESS-MIB", "ipliIp2Index"),
    (0, "CODIMA-EXPRESS-MIB", "ipliTimeStampIndex"),
)
if mibBuilder.loadTexts:
    iplIcmpEntry.setStatus("current")
_IpliIp1Index_Type = IpAddress
_IpliIp1Index_Object = MibTableColumn
ipliIp1Index = _IpliIp1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 1),
    _IpliIp1Index_Type()
)
ipliIp1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliIp1Index.setStatus("current")
_IpliIp2Index_Type = IpAddress
_IpliIp2Index_Object = MibTableColumn
ipliIp2Index = _IpliIp2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 2),
    _IpliIp2Index_Type()
)
ipliIp2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliIp2Index.setStatus("current")
_IpliTimeStampIndex_Type = Unsigned32
_IpliTimeStampIndex_Object = MibTableColumn
ipliTimeStampIndex = _IpliTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 3),
    _IpliTimeStampIndex_Type()
)
ipliTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliTimeStampIndex.setStatus("current")


class _IpliTimeStamp_Type(DisplayString):
    """Custom type ipliTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IpliTimeStamp_Type.__name__ = "DisplayString"
_IpliTimeStamp_Object = MibTableColumn
ipliTimeStamp = _IpliTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 4),
    _IpliTimeStamp_Type()
)
ipliTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliTimeStamp.setStatus("current")
_IpliPing_Type = Counter32
_IpliPing_Object = MibTableColumn
ipliPing = _IpliPing_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 5),
    _IpliPing_Type()
)
ipliPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliPing.setStatus("current")
_IpliSrcQuench_Type = Counter32
_IpliSrcQuench_Object = MibTableColumn
ipliSrcQuench = _IpliSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 6),
    _IpliSrcQuench_Type()
)
ipliSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliSrcQuench.setStatus("current")
_IpliRedirect_Type = Counter32
_IpliRedirect_Object = MibTableColumn
ipliRedirect = _IpliRedirect_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 7),
    _IpliRedirect_Type()
)
ipliRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliRedirect.setStatus("current")
_IpliTtlExceeded_Type = Counter32
_IpliTtlExceeded_Object = MibTableColumn
ipliTtlExceeded = _IpliTtlExceeded_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 8),
    _IpliTtlExceeded_Type()
)
ipliTtlExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliTtlExceeded.setStatus("current")
_IpliParamProblem_Type = Counter32
_IpliParamProblem_Object = MibTableColumn
ipliParamProblem = _IpliParamProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 9),
    _IpliParamProblem_Type()
)
ipliParamProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliParamProblem.setStatus("current")
_IpliTimestamp_Type = Counter32
_IpliTimestamp_Object = MibTableColumn
ipliTimestamp = _IpliTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 10),
    _IpliTimestamp_Type()
)
ipliTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliTimestamp.setStatus("current")
_IpliFragTimeout_Type = Counter32
_IpliFragTimeout_Object = MibTableColumn
ipliFragTimeout = _IpliFragTimeout_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 11),
    _IpliFragTimeout_Type()
)
ipliFragTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliFragTimeout.setStatus("current")
_IpliNetUnreachable_Type = Counter32
_IpliNetUnreachable_Object = MibTableColumn
ipliNetUnreachable = _IpliNetUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 12),
    _IpliNetUnreachable_Type()
)
ipliNetUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliNetUnreachable.setStatus("current")
_IpliHostUnreachable_Type = Counter32
_IpliHostUnreachable_Object = MibTableColumn
ipliHostUnreachable = _IpliHostUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 13),
    _IpliHostUnreachable_Type()
)
ipliHostUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliHostUnreachable.setStatus("current")
_IpliProtocolUnreachable_Type = Counter32
_IpliProtocolUnreachable_Object = MibTableColumn
ipliProtocolUnreachable = _IpliProtocolUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 14),
    _IpliProtocolUnreachable_Type()
)
ipliProtocolUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliProtocolUnreachable.setStatus("current")
_IpliPortUnreachable_Type = Counter32
_IpliPortUnreachable_Object = MibTableColumn
ipliPortUnreachable = _IpliPortUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 15),
    _IpliPortUnreachable_Type()
)
ipliPortUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliPortUnreachable.setStatus("current")
_IpliFragRequired_Type = Counter32
_IpliFragRequired_Object = MibTableColumn
ipliFragRequired = _IpliFragRequired_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 16),
    _IpliFragRequired_Type()
)
ipliFragRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliFragRequired.setStatus("current")
_IpliSrcRouteFail_Type = Counter32
_IpliSrcRouteFail_Object = MibTableColumn
ipliSrcRouteFail = _IpliSrcRouteFail_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 17),
    _IpliSrcRouteFail_Type()
)
ipliSrcRouteFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliSrcRouteFail.setStatus("current")
_IpliDestNetUnknown_Type = Counter32
_IpliDestNetUnknown_Object = MibTableColumn
ipliDestNetUnknown = _IpliDestNetUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 18),
    _IpliDestNetUnknown_Type()
)
ipliDestNetUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliDestNetUnknown.setStatus("current")
_IpliDestHostUnknown_Type = Counter32
_IpliDestHostUnknown_Object = MibTableColumn
ipliDestHostUnknown = _IpliDestHostUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 19),
    _IpliDestHostUnknown_Type()
)
ipliDestHostUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliDestHostUnknown.setStatus("current")
_IpliSrcHostIsolated_Type = Counter32
_IpliSrcHostIsolated_Object = MibTableColumn
ipliSrcHostIsolated = _IpliSrcHostIsolated_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 20),
    _IpliSrcHostIsolated_Type()
)
ipliSrcHostIsolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliSrcHostIsolated.setStatus("current")
_IpliNetProhibited_Type = Counter32
_IpliNetProhibited_Object = MibTableColumn
ipliNetProhibited = _IpliNetProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 21),
    _IpliNetProhibited_Type()
)
ipliNetProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliNetProhibited.setStatus("current")
_IpliHostProhibited_Type = Counter32
_IpliHostProhibited_Object = MibTableColumn
ipliHostProhibited = _IpliHostProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 22),
    _IpliHostProhibited_Type()
)
ipliHostProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliHostProhibited.setStatus("current")
_IpliNetTosUnreachable_Type = Counter32
_IpliNetTosUnreachable_Object = MibTableColumn
ipliNetTosUnreachable = _IpliNetTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 23),
    _IpliNetTosUnreachable_Type()
)
ipliNetTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliNetTosUnreachable.setStatus("current")
_IpliHostTosUnreachable_Type = Counter32
_IpliHostTosUnreachable_Object = MibTableColumn
ipliHostTosUnreachable = _IpliHostTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 24),
    _IpliHostTosUnreachable_Type()
)
ipliHostTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliHostTosUnreachable.setStatus("current")
_IpliPerformance_Type = Counter32
_IpliPerformance_Object = MibTableColumn
ipliPerformance = _IpliPerformance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 25),
    _IpliPerformance_Type()
)
ipliPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliPerformance.setStatus("current")
_IpliNetRouteProblem_Type = Counter32
_IpliNetRouteProblem_Object = MibTableColumn
ipliNetRouteProblem = _IpliNetRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 26),
    _IpliNetRouteProblem_Type()
)
ipliNetRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliNetRouteProblem.setStatus("current")
_IpliHostRouteProblem_Type = Counter32
_IpliHostRouteProblem_Object = MibTableColumn
ipliHostRouteProblem = _IpliHostRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 27),
    _IpliHostRouteProblem_Type()
)
ipliHostRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliHostRouteProblem.setStatus("current")
_IpliAppRouteProblem_Type = Counter32
_IpliAppRouteProblem_Object = MibTableColumn
ipliAppRouteProblem = _IpliAppRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 28),
    _IpliAppRouteProblem_Type()
)
ipliAppRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliAppRouteProblem.setStatus("current")
_IpliRouteChange_Type = Counter32
_IpliRouteChange_Object = MibTableColumn
ipliRouteChange = _IpliRouteChange_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 29),
    _IpliRouteChange_Type()
)
ipliRouteChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliRouteChange.setStatus("current")
_IpliErrors_Type = Counter32
_IpliErrors_Object = MibTableColumn
ipliErrors = _IpliErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 30),
    _IpliErrors_Type()
)
ipliErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliErrors.setStatus("current")
_IpliMaintenance_Type = Counter32
_IpliMaintenance_Object = MibTableColumn
ipliMaintenance = _IpliMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 1, 3, 1, 31),
    _IpliMaintenance_Type()
)
ipliMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipliMaintenance.setStatus("current")
_IpPeerShortTerm_ObjectIdentity = ObjectIdentity
ipPeerShortTerm = _IpPeerShortTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ipPeerShortTerm.setStatus("current")
_IpsBaseTable_Object = MibTable
ipsBaseTable = _IpsBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    ipsBaseTable.setStatus("current")
_IpsBaseEntry_Object = MibTableRow
ipsBaseEntry = _IpsBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 1, 1)
)
ipsBaseEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "ipsbIp1Index"),
    (0, "CODIMA-EXPRESS-MIB", "ipsbIp2Index"),
    (0, "CODIMA-EXPRESS-MIB", "ipsbTimeStampIndex"),
)
if mibBuilder.loadTexts:
    ipsBaseEntry.setStatus("current")
_IpsbIp1Index_Type = IpAddress
_IpsbIp1Index_Object = MibTableColumn
ipsbIp1Index = _IpsbIp1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 1, 1, 1),
    _IpsbIp1Index_Type()
)
ipsbIp1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsbIp1Index.setStatus("current")
_IpsbIp2Index_Type = IpAddress
_IpsbIp2Index_Object = MibTableColumn
ipsbIp2Index = _IpsbIp2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 1, 1, 2),
    _IpsbIp2Index_Type()
)
ipsbIp2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsbIp2Index.setStatus("current")
_IpsbTimeStampIndex_Type = Unsigned32
_IpsbTimeStampIndex_Object = MibTableColumn
ipsbTimeStampIndex = _IpsbTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 1, 1, 3),
    _IpsbTimeStampIndex_Type()
)
ipsbTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsbTimeStampIndex.setStatus("current")


class _IpsbTimeStamp_Type(DisplayString):
    """Custom type ipsbTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IpsbTimeStamp_Type.__name__ = "DisplayString"
_IpsbTimeStamp_Object = MibTableColumn
ipsbTimeStamp = _IpsbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 1, 1, 4),
    _IpsbTimeStamp_Type()
)
ipsbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsbTimeStamp.setStatus("current")
_IpsbFrames_Type = Counter32
_IpsbFrames_Object = MibTableColumn
ipsbFrames = _IpsbFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 1, 1, 5),
    _IpsbFrames_Type()
)
ipsbFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsbFrames.setStatus("current")
_IpsbBytes_Type = Counter32
_IpsbBytes_Object = MibTableColumn
ipsbBytes = _IpsbBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 1, 1, 6),
    _IpsbBytes_Type()
)
ipsbBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsbBytes.setStatus("current")
_IpsbFrameSize_Type = Gauge32
_IpsbFrameSize_Object = MibTableColumn
ipsbFrameSize = _IpsbFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 1, 1, 7),
    _IpsbFrameSize_Type()
)
ipsbFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsbFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    ipsbFrameSize.setUnits("bytes")
_IpsbHardwareErrors_Type = Counter32
_IpsbHardwareErrors_Object = MibTableColumn
ipsbHardwareErrors = _IpsbHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 1, 1, 8),
    _IpsbHardwareErrors_Type()
)
ipsbHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsbHardwareErrors.setStatus("current")
_IpsbSoftwareErrors_Type = Counter32
_IpsbSoftwareErrors_Object = MibTableColumn
ipsbSoftwareErrors = _IpsbSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 1, 1, 9),
    _IpsbSoftwareErrors_Type()
)
ipsbSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsbSoftwareErrors.setStatus("current")
_IpsDerivedTable_Object = MibTable
ipsDerivedTable = _IpsDerivedTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    ipsDerivedTable.setStatus("current")
_IpsDerivedEntry_Object = MibTableRow
ipsDerivedEntry = _IpsDerivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 2, 1)
)
ipsDerivedEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "ipsdIp1Index"),
    (0, "CODIMA-EXPRESS-MIB", "ipsdIp2Index"),
    (0, "CODIMA-EXPRESS-MIB", "ipsdTimeStampIndex"),
)
if mibBuilder.loadTexts:
    ipsDerivedEntry.setStatus("current")
_IpsdIp1Index_Type = IpAddress
_IpsdIp1Index_Object = MibTableColumn
ipsdIp1Index = _IpsdIp1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 2, 1, 1),
    _IpsdIp1Index_Type()
)
ipsdIp1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsdIp1Index.setStatus("current")
_IpsdIp2Index_Type = IpAddress
_IpsdIp2Index_Object = MibTableColumn
ipsdIp2Index = _IpsdIp2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 2, 1, 2),
    _IpsdIp2Index_Type()
)
ipsdIp2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsdIp2Index.setStatus("current")
_IpsdTimeStampIndex_Type = Unsigned32
_IpsdTimeStampIndex_Object = MibTableColumn
ipsdTimeStampIndex = _IpsdTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 2, 1, 3),
    _IpsdTimeStampIndex_Type()
)
ipsdTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsdTimeStampIndex.setStatus("current")


class _IpsdTimeStamp_Type(DisplayString):
    """Custom type ipsdTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IpsdTimeStamp_Type.__name__ = "DisplayString"
_IpsdTimeStamp_Object = MibTableColumn
ipsdTimeStamp = _IpsdTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 2, 1, 4),
    _IpsdTimeStamp_Type()
)
ipsdTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsdTimeStamp.setStatus("current")
_IpsdUtilization_Type = Gauge32
_IpsdUtilization_Object = MibTableColumn
ipsdUtilization = _IpsdUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 2, 1, 5),
    _IpsdUtilization_Type()
)
ipsdUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsdUtilization.setStatus("current")
_IpsdErrorFrames_Type = Gauge32
_IpsdErrorFrames_Object = MibTableColumn
ipsdErrorFrames = _IpsdErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 2, 1, 6),
    _IpsdErrorFrames_Type()
)
ipsdErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsdErrorFrames.setStatus("current")
_IpsIcmpTable_Object = MibTable
ipsIcmpTable = _IpsIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    ipsIcmpTable.setStatus("current")
_IpsIcmpEntry_Object = MibTableRow
ipsIcmpEntry = _IpsIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1)
)
ipsIcmpEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "ipsiIp1Index"),
    (0, "CODIMA-EXPRESS-MIB", "ipsiIp2Index"),
    (0, "CODIMA-EXPRESS-MIB", "ipsiTimeStampIndex"),
)
if mibBuilder.loadTexts:
    ipsIcmpEntry.setStatus("current")
_IpsiIp1Index_Type = IpAddress
_IpsiIp1Index_Object = MibTableColumn
ipsiIp1Index = _IpsiIp1Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 1),
    _IpsiIp1Index_Type()
)
ipsiIp1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiIp1Index.setStatus("current")
_IpsiIp2Index_Type = IpAddress
_IpsiIp2Index_Object = MibTableColumn
ipsiIp2Index = _IpsiIp2Index_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 2),
    _IpsiIp2Index_Type()
)
ipsiIp2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiIp2Index.setStatus("current")
_IpsiTimeStampIndex_Type = Unsigned32
_IpsiTimeStampIndex_Object = MibTableColumn
ipsiTimeStampIndex = _IpsiTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 3),
    _IpsiTimeStampIndex_Type()
)
ipsiTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiTimeStampIndex.setStatus("current")


class _IpsiTimeStamp_Type(DisplayString):
    """Custom type ipsiTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IpsiTimeStamp_Type.__name__ = "DisplayString"
_IpsiTimeStamp_Object = MibTableColumn
ipsiTimeStamp = _IpsiTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 4),
    _IpsiTimeStamp_Type()
)
ipsiTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiTimeStamp.setStatus("current")
_IpsiPing_Type = Counter32
_IpsiPing_Object = MibTableColumn
ipsiPing = _IpsiPing_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 5),
    _IpsiPing_Type()
)
ipsiPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiPing.setStatus("current")
_IpsiSrcQuench_Type = Counter32
_IpsiSrcQuench_Object = MibTableColumn
ipsiSrcQuench = _IpsiSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 6),
    _IpsiSrcQuench_Type()
)
ipsiSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiSrcQuench.setStatus("current")
_IpsiRedirect_Type = Counter32
_IpsiRedirect_Object = MibTableColumn
ipsiRedirect = _IpsiRedirect_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 7),
    _IpsiRedirect_Type()
)
ipsiRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiRedirect.setStatus("current")
_IpsiTtlExceeded_Type = Counter32
_IpsiTtlExceeded_Object = MibTableColumn
ipsiTtlExceeded = _IpsiTtlExceeded_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 8),
    _IpsiTtlExceeded_Type()
)
ipsiTtlExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiTtlExceeded.setStatus("current")
_IpsiParamProblem_Type = Counter32
_IpsiParamProblem_Object = MibTableColumn
ipsiParamProblem = _IpsiParamProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 9),
    _IpsiParamProblem_Type()
)
ipsiParamProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiParamProblem.setStatus("current")
_IpsiTimestamp_Type = Counter32
_IpsiTimestamp_Object = MibTableColumn
ipsiTimestamp = _IpsiTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 10),
    _IpsiTimestamp_Type()
)
ipsiTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiTimestamp.setStatus("current")
_IpsiFragTimeout_Type = Counter32
_IpsiFragTimeout_Object = MibTableColumn
ipsiFragTimeout = _IpsiFragTimeout_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 11),
    _IpsiFragTimeout_Type()
)
ipsiFragTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiFragTimeout.setStatus("current")
_IpsiNetUnreachable_Type = Counter32
_IpsiNetUnreachable_Object = MibTableColumn
ipsiNetUnreachable = _IpsiNetUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 12),
    _IpsiNetUnreachable_Type()
)
ipsiNetUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiNetUnreachable.setStatus("current")
_IpsiHostUnreachable_Type = Counter32
_IpsiHostUnreachable_Object = MibTableColumn
ipsiHostUnreachable = _IpsiHostUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 13),
    _IpsiHostUnreachable_Type()
)
ipsiHostUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiHostUnreachable.setStatus("current")
_IpsiProtocolUnreachable_Type = Counter32
_IpsiProtocolUnreachable_Object = MibTableColumn
ipsiProtocolUnreachable = _IpsiProtocolUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 14),
    _IpsiProtocolUnreachable_Type()
)
ipsiProtocolUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiProtocolUnreachable.setStatus("current")
_IpsiPortUnreachable_Type = Counter32
_IpsiPortUnreachable_Object = MibTableColumn
ipsiPortUnreachable = _IpsiPortUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 15),
    _IpsiPortUnreachable_Type()
)
ipsiPortUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiPortUnreachable.setStatus("current")
_IpsiFragRequired_Type = Counter32
_IpsiFragRequired_Object = MibTableColumn
ipsiFragRequired = _IpsiFragRequired_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 16),
    _IpsiFragRequired_Type()
)
ipsiFragRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiFragRequired.setStatus("current")
_IpsiSrcRouteFail_Type = Counter32
_IpsiSrcRouteFail_Object = MibTableColumn
ipsiSrcRouteFail = _IpsiSrcRouteFail_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 17),
    _IpsiSrcRouteFail_Type()
)
ipsiSrcRouteFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiSrcRouteFail.setStatus("current")
_IpsiDestNetUnknown_Type = Counter32
_IpsiDestNetUnknown_Object = MibTableColumn
ipsiDestNetUnknown = _IpsiDestNetUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 18),
    _IpsiDestNetUnknown_Type()
)
ipsiDestNetUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiDestNetUnknown.setStatus("current")
_IpsiDestHostUnknown_Type = Counter32
_IpsiDestHostUnknown_Object = MibTableColumn
ipsiDestHostUnknown = _IpsiDestHostUnknown_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 19),
    _IpsiDestHostUnknown_Type()
)
ipsiDestHostUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiDestHostUnknown.setStatus("current")
_IpsiSrcHostIsolated_Type = Counter32
_IpsiSrcHostIsolated_Object = MibTableColumn
ipsiSrcHostIsolated = _IpsiSrcHostIsolated_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 20),
    _IpsiSrcHostIsolated_Type()
)
ipsiSrcHostIsolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiSrcHostIsolated.setStatus("current")
_IpsiNetProhibited_Type = Counter32
_IpsiNetProhibited_Object = MibTableColumn
ipsiNetProhibited = _IpsiNetProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 21),
    _IpsiNetProhibited_Type()
)
ipsiNetProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiNetProhibited.setStatus("current")
_IpsiHostProhibited_Type = Counter32
_IpsiHostProhibited_Object = MibTableColumn
ipsiHostProhibited = _IpsiHostProhibited_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 22),
    _IpsiHostProhibited_Type()
)
ipsiHostProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiHostProhibited.setStatus("current")
_IpsiNetTosUnreachable_Type = Counter32
_IpsiNetTosUnreachable_Object = MibTableColumn
ipsiNetTosUnreachable = _IpsiNetTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 23),
    _IpsiNetTosUnreachable_Type()
)
ipsiNetTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiNetTosUnreachable.setStatus("current")
_IpsiHostTosUnreachable_Type = Counter32
_IpsiHostTosUnreachable_Object = MibTableColumn
ipsiHostTosUnreachable = _IpsiHostTosUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 24),
    _IpsiHostTosUnreachable_Type()
)
ipsiHostTosUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiHostTosUnreachable.setStatus("current")
_IpsiPerformance_Type = Counter32
_IpsiPerformance_Object = MibTableColumn
ipsiPerformance = _IpsiPerformance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 25),
    _IpsiPerformance_Type()
)
ipsiPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiPerformance.setStatus("current")
_IpsiNetRouteProblem_Type = Counter32
_IpsiNetRouteProblem_Object = MibTableColumn
ipsiNetRouteProblem = _IpsiNetRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 26),
    _IpsiNetRouteProblem_Type()
)
ipsiNetRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiNetRouteProblem.setStatus("current")
_IpsiHostRouteProblem_Type = Counter32
_IpsiHostRouteProblem_Object = MibTableColumn
ipsiHostRouteProblem = _IpsiHostRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 27),
    _IpsiHostRouteProblem_Type()
)
ipsiHostRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiHostRouteProblem.setStatus("current")
_IpsiAppRouteProblem_Type = Counter32
_IpsiAppRouteProblem_Object = MibTableColumn
ipsiAppRouteProblem = _IpsiAppRouteProblem_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 28),
    _IpsiAppRouteProblem_Type()
)
ipsiAppRouteProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiAppRouteProblem.setStatus("current")
_IpsiRouteChange_Type = Counter32
_IpsiRouteChange_Object = MibTableColumn
ipsiRouteChange = _IpsiRouteChange_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 29),
    _IpsiRouteChange_Type()
)
ipsiRouteChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiRouteChange.setStatus("current")
_IpsiErrors_Type = Counter32
_IpsiErrors_Object = MibTableColumn
ipsiErrors = _IpsiErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 30),
    _IpsiErrors_Type()
)
ipsiErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiErrors.setStatus("current")
_IpsiMaintenance_Type = Counter32
_IpsiMaintenance_Object = MibTableColumn
ipsiMaintenance = _IpsiMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 6, 2, 3, 1, 31),
    _IpsiMaintenance_Type()
)
ipsiMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsiMaintenance.setStatus("current")
_DbProtocol_ObjectIdentity = ObjectIdentity
dbProtocol = _DbProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    dbProtocol.setStatus("current")
_ProtocolLongTerm_ObjectIdentity = ObjectIdentity
protocolLongTerm = _ProtocolLongTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    protocolLongTerm.setStatus("current")
_PlBaseTable_Object = MibTable
plBaseTable = _PlBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    plBaseTable.setStatus("current")
_PlBaseEntry_Object = MibTableRow
plBaseEntry = _PlBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 1, 1)
)
plBaseEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "plbLayerIndex"),
    (0, "CODIMA-EXPRESS-MIB", "plbIdIndex"),
    (0, "CODIMA-EXPRESS-MIB", "plbTimeStampIndex"),
)
if mibBuilder.loadTexts:
    plBaseEntry.setStatus("current")


class _PlbLayerIndex_Type(Integer32):
    """Custom type plbLayerIndex based on Integer32"""
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
        *(("application", 7),
          ("dataLink", 2),
          ("network", 3),
          ("physical", 1),
          ("presentation", 6),
          ("session", 5),
          ("transport", 4))
    )


_PlbLayerIndex_Type.__name__ = "Integer32"
_PlbLayerIndex_Object = MibTableColumn
plbLayerIndex = _PlbLayerIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 1, 1, 1),
    _PlbLayerIndex_Type()
)
plbLayerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plbLayerIndex.setStatus("current")


class _PlbIdIndex_Type(OctetString):
    """Custom type plbIdIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PlbIdIndex_Type.__name__ = "OctetString"
_PlbIdIndex_Object = MibTableColumn
plbIdIndex = _PlbIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 1, 1, 2),
    _PlbIdIndex_Type()
)
plbIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plbIdIndex.setStatus("current")
_PlbTimeStampIndex_Type = Unsigned32
_PlbTimeStampIndex_Object = MibTableColumn
plbTimeStampIndex = _PlbTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 1, 1, 3),
    _PlbTimeStampIndex_Type()
)
plbTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plbTimeStampIndex.setStatus("current")


class _PlbTimeStamp_Type(DisplayString):
    """Custom type plbTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_PlbTimeStamp_Type.__name__ = "DisplayString"
_PlbTimeStamp_Object = MibTableColumn
plbTimeStamp = _PlbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 1, 1, 4),
    _PlbTimeStamp_Type()
)
plbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plbTimeStamp.setStatus("current")
_PlbProtocolName_Type = DisplayString
_PlbProtocolName_Object = MibTableColumn
plbProtocolName = _PlbProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 1, 1, 5),
    _PlbProtocolName_Type()
)
plbProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plbProtocolName.setStatus("current")
_PlbFrames_Type = Counter32
_PlbFrames_Object = MibTableColumn
plbFrames = _PlbFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 1, 1, 6),
    _PlbFrames_Type()
)
plbFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plbFrames.setStatus("current")
_PlbBytes_Type = Counter32
_PlbBytes_Object = MibTableColumn
plbBytes = _PlbBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 1, 1, 7),
    _PlbBytes_Type()
)
plbBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plbBytes.setStatus("current")
_PlbFrameSize_Type = Gauge32
_PlbFrameSize_Object = MibTableColumn
plbFrameSize = _PlbFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 1, 1, 8),
    _PlbFrameSize_Type()
)
plbFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plbFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    plbFrameSize.setUnits("bytes")
_PlbHardwareErrors_Type = Counter32
_PlbHardwareErrors_Object = MibTableColumn
plbHardwareErrors = _PlbHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 1, 1, 9),
    _PlbHardwareErrors_Type()
)
plbHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plbHardwareErrors.setStatus("current")
_PlbSoftwareErrors_Type = Counter32
_PlbSoftwareErrors_Object = MibTableColumn
plbSoftwareErrors = _PlbSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 1, 1, 10),
    _PlbSoftwareErrors_Type()
)
plbSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plbSoftwareErrors.setStatus("current")
_PlDerivedTable_Object = MibTable
plDerivedTable = _PlDerivedTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    plDerivedTable.setStatus("current")
_PlDerivedEntry_Object = MibTableRow
plDerivedEntry = _PlDerivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 2, 1)
)
plDerivedEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "pldLayerIndex"),
    (0, "CODIMA-EXPRESS-MIB", "pldIdIndex"),
    (0, "CODIMA-EXPRESS-MIB", "pldTimeStampIndex"),
)
if mibBuilder.loadTexts:
    plDerivedEntry.setStatus("current")


class _PldLayerIndex_Type(Integer32):
    """Custom type pldLayerIndex based on Integer32"""
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
        *(("application", 7),
          ("dataLink", 2),
          ("network", 3),
          ("physical", 1),
          ("presentation", 6),
          ("session", 5),
          ("transport", 4))
    )


_PldLayerIndex_Type.__name__ = "Integer32"
_PldLayerIndex_Object = MibTableColumn
pldLayerIndex = _PldLayerIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 2, 1, 1),
    _PldLayerIndex_Type()
)
pldLayerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldLayerIndex.setStatus("current")


class _PldIdIndex_Type(OctetString):
    """Custom type pldIdIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PldIdIndex_Type.__name__ = "OctetString"
_PldIdIndex_Object = MibTableColumn
pldIdIndex = _PldIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 2, 1, 2),
    _PldIdIndex_Type()
)
pldIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldIdIndex.setStatus("current")
_PldTimeStampIndex_Type = Unsigned32
_PldTimeStampIndex_Object = MibTableColumn
pldTimeStampIndex = _PldTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 2, 1, 3),
    _PldTimeStampIndex_Type()
)
pldTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldTimeStampIndex.setStatus("current")


class _PldTimeStamp_Type(DisplayString):
    """Custom type pldTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_PldTimeStamp_Type.__name__ = "DisplayString"
_PldTimeStamp_Object = MibTableColumn
pldTimeStamp = _PldTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 2, 1, 4),
    _PldTimeStamp_Type()
)
pldTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldTimeStamp.setStatus("current")
_PldProtocolName_Type = DisplayString
_PldProtocolName_Object = MibTableColumn
pldProtocolName = _PldProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 2, 1, 5),
    _PldProtocolName_Type()
)
pldProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldProtocolName.setStatus("current")
_PldUtilization_Type = Gauge32
_PldUtilization_Object = MibTableColumn
pldUtilization = _PldUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 2, 1, 6),
    _PldUtilization_Type()
)
pldUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldUtilization.setStatus("current")
_PldErrorFrames_Type = Gauge32
_PldErrorFrames_Object = MibTableColumn
pldErrorFrames = _PldErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 1, 2, 1, 7),
    _PldErrorFrames_Type()
)
pldErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldErrorFrames.setStatus("current")
_ProtocolShortTerm_ObjectIdentity = ObjectIdentity
protocolShortTerm = _ProtocolShortTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    protocolShortTerm.setStatus("current")
_PsBaseTable_Object = MibTable
psBaseTable = _PsBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    psBaseTable.setStatus("current")
_PsBaseEntry_Object = MibTableRow
psBaseEntry = _PsBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 1, 1)
)
psBaseEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "psbLayerIndex"),
    (0, "CODIMA-EXPRESS-MIB", "psbIdIndex"),
    (0, "CODIMA-EXPRESS-MIB", "psbTimeStampIndex"),
)
if mibBuilder.loadTexts:
    psBaseEntry.setStatus("current")


class _PsbLayerIndex_Type(Integer32):
    """Custom type psbLayerIndex based on Integer32"""
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
        *(("application", 7),
          ("dataLink", 2),
          ("network", 3),
          ("physical", 1),
          ("presentation", 6),
          ("session", 5),
          ("transport", 4))
    )


_PsbLayerIndex_Type.__name__ = "Integer32"
_PsbLayerIndex_Object = MibTableColumn
psbLayerIndex = _PsbLayerIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 1, 1, 1),
    _PsbLayerIndex_Type()
)
psbLayerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbLayerIndex.setStatus("current")


class _PsbIdIndex_Type(OctetString):
    """Custom type psbIdIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PsbIdIndex_Type.__name__ = "OctetString"
_PsbIdIndex_Object = MibTableColumn
psbIdIndex = _PsbIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 1, 1, 2),
    _PsbIdIndex_Type()
)
psbIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbIdIndex.setStatus("current")
_PsbTimeStampIndex_Type = Unsigned32
_PsbTimeStampIndex_Object = MibTableColumn
psbTimeStampIndex = _PsbTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 1, 1, 3),
    _PsbTimeStampIndex_Type()
)
psbTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbTimeStampIndex.setStatus("current")


class _PsbTimeStamp_Type(DisplayString):
    """Custom type psbTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_PsbTimeStamp_Type.__name__ = "DisplayString"
_PsbTimeStamp_Object = MibTableColumn
psbTimeStamp = _PsbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 1, 1, 4),
    _PsbTimeStamp_Type()
)
psbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbTimeStamp.setStatus("current")
_PsbProtocolName_Type = DisplayString
_PsbProtocolName_Object = MibTableColumn
psbProtocolName = _PsbProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 1, 1, 5),
    _PsbProtocolName_Type()
)
psbProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbProtocolName.setStatus("current")
_PsbFrames_Type = Counter32
_PsbFrames_Object = MibTableColumn
psbFrames = _PsbFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 1, 1, 6),
    _PsbFrames_Type()
)
psbFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbFrames.setStatus("current")
_PsbBytes_Type = Counter32
_PsbBytes_Object = MibTableColumn
psbBytes = _PsbBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 1, 1, 7),
    _PsbBytes_Type()
)
psbBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbBytes.setStatus("current")
_PsbFrameSize_Type = Gauge32
_PsbFrameSize_Object = MibTableColumn
psbFrameSize = _PsbFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 1, 1, 8),
    _PsbFrameSize_Type()
)
psbFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    psbFrameSize.setUnits("bytes")
_PsbHardwareErrors_Type = Counter32
_PsbHardwareErrors_Object = MibTableColumn
psbHardwareErrors = _PsbHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 1, 1, 9),
    _PsbHardwareErrors_Type()
)
psbHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbHardwareErrors.setStatus("current")
_PsbSoftwareErrors_Type = Counter32
_PsbSoftwareErrors_Object = MibTableColumn
psbSoftwareErrors = _PsbSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 1, 1, 10),
    _PsbSoftwareErrors_Type()
)
psbSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbSoftwareErrors.setStatus("current")
_PsDerivedTable_Object = MibTable
psDerivedTable = _PsDerivedTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    psDerivedTable.setStatus("current")
_PsDerivedEntry_Object = MibTableRow
psDerivedEntry = _PsDerivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 2, 1)
)
psDerivedEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "psdLayerIndex"),
    (0, "CODIMA-EXPRESS-MIB", "psdIdIndex"),
    (0, "CODIMA-EXPRESS-MIB", "psdTimeStampIndex"),
)
if mibBuilder.loadTexts:
    psDerivedEntry.setStatus("current")


class _PsdLayerIndex_Type(Integer32):
    """Custom type psdLayerIndex based on Integer32"""
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
        *(("application", 7),
          ("dataLink", 2),
          ("network", 3),
          ("physical", 1),
          ("presentation", 6),
          ("session", 5),
          ("transport", 4))
    )


_PsdLayerIndex_Type.__name__ = "Integer32"
_PsdLayerIndex_Object = MibTableColumn
psdLayerIndex = _PsdLayerIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 2, 1, 1),
    _PsdLayerIndex_Type()
)
psdLayerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psdLayerIndex.setStatus("current")


class _PsdIdIndex_Type(OctetString):
    """Custom type psdIdIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PsdIdIndex_Type.__name__ = "OctetString"
_PsdIdIndex_Object = MibTableColumn
psdIdIndex = _PsdIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 2, 1, 2),
    _PsdIdIndex_Type()
)
psdIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psdIdIndex.setStatus("current")
_PsdTimeStampIndex_Type = Unsigned32
_PsdTimeStampIndex_Object = MibTableColumn
psdTimeStampIndex = _PsdTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 2, 1, 3),
    _PsdTimeStampIndex_Type()
)
psdTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psdTimeStampIndex.setStatus("current")


class _PsdTimeStamp_Type(DisplayString):
    """Custom type psdTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_PsdTimeStamp_Type.__name__ = "DisplayString"
_PsdTimeStamp_Object = MibTableColumn
psdTimeStamp = _PsdTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 2, 1, 4),
    _PsdTimeStamp_Type()
)
psdTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psdTimeStamp.setStatus("current")
_PsdProtocolName_Type = DisplayString
_PsdProtocolName_Object = MibTableColumn
psdProtocolName = _PsdProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 2, 1, 5),
    _PsdProtocolName_Type()
)
psdProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psdProtocolName.setStatus("current")
_PsdUtilization_Type = Gauge32
_PsdUtilization_Object = MibTableColumn
psdUtilization = _PsdUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 2, 1, 6),
    _PsdUtilization_Type()
)
psdUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psdUtilization.setStatus("current")
_PsdErrorFrames_Type = Gauge32
_PsdErrorFrames_Object = MibTableColumn
psdErrorFrames = _PsdErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 7, 2, 2, 1, 7),
    _PsdErrorFrames_Type()
)
psdErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psdErrorFrames.setStatus("current")
_DbNetChannel_ObjectIdentity = ObjectIdentity
dbNetChannel = _DbNetChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    dbNetChannel.setStatus("current")
_NetChanLongTermTable_Object = MibTable
netChanLongTermTable = _NetChanLongTermTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    netChanLongTermTable.setStatus("current")
_NetChanLongTermEntry_Object = MibTableRow
netChanLongTermEntry = _NetChanLongTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1)
)
netChanLongTermEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "nlNameIndex"),
    (0, "CODIMA-EXPRESS-MIB", "nlTimeStampIndex"),
    (0, "CODIMA-EXPRESS-MIB", "nlTypeIndex"),
)
if mibBuilder.loadTexts:
    netChanLongTermEntry.setStatus("current")


class _NlTypeIndex_Type(Integer32):
    """Custom type nlTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 2),
          ("netChannel", 1))
    )


_NlTypeIndex_Type.__name__ = "Integer32"
_NlTypeIndex_Object = MibTableColumn
nlTypeIndex = _NlTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 1),
    _NlTypeIndex_Type()
)
nlTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlTypeIndex.setStatus("current")


class _NlNameIndex_Type(DisplayString):
    """Custom type nlNameIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_NlNameIndex_Type.__name__ = "DisplayString"
_NlNameIndex_Object = MibTableColumn
nlNameIndex = _NlNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 2),
    _NlNameIndex_Type()
)
nlNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlNameIndex.setStatus("current")
_NlTimeStampIndex_Type = Unsigned32
_NlTimeStampIndex_Object = MibTableColumn
nlTimeStampIndex = _NlTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 3),
    _NlTimeStampIndex_Type()
)
nlTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlTimeStampIndex.setStatus("current")


class _NlTimeStamp_Type(DisplayString):
    """Custom type nlTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_NlTimeStamp_Type.__name__ = "DisplayString"
_NlTimeStamp_Object = MibTableColumn
nlTimeStamp = _NlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 4),
    _NlTimeStamp_Type()
)
nlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlTimeStamp.setStatus("current")
_NlFrames_Type = Counter32
_NlFrames_Object = MibTableColumn
nlFrames = _NlFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 5),
    _NlFrames_Type()
)
nlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlFrames.setStatus("current")
_NlBytes_Type = Counter32
_NlBytes_Object = MibTableColumn
nlBytes = _NlBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 6),
    _NlBytes_Type()
)
nlBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlBytes.setStatus("current")
_NlFrameSize_Type = Gauge32
_NlFrameSize_Object = MibTableColumn
nlFrameSize = _NlFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 7),
    _NlFrameSize_Type()
)
nlFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    nlFrameSize.setUnits("bytes")
_NlHardErrors_Type = Counter32
_NlHardErrors_Object = MibTableColumn
nlHardErrors = _NlHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 8),
    _NlHardErrors_Type()
)
nlHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHardErrors.setStatus("current")
_NlSoftErrors_Type = Counter32
_NlSoftErrors_Object = MibTableColumn
nlSoftErrors = _NlSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 9),
    _NlSoftErrors_Type()
)
nlSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlSoftErrors.setStatus("current")
_NlUtilization_Type = Gauge32
_NlUtilization_Object = MibTableColumn
nlUtilization = _NlUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 10),
    _NlUtilization_Type()
)
nlUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlUtilization.setStatus("current")
_NlHardErrorsPercent_Type = Gauge32
_NlHardErrorsPercent_Object = MibTableColumn
nlHardErrorsPercent = _NlHardErrorsPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 11),
    _NlHardErrorsPercent_Type()
)
nlHardErrorsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHardErrorsPercent.setStatus("current")
_NlSoftErrorsPercent_Type = Gauge32
_NlSoftErrorsPercent_Object = MibTableColumn
nlSoftErrorsPercent = _NlSoftErrorsPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 12),
    _NlSoftErrorsPercent_Type()
)
nlSoftErrorsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlSoftErrorsPercent.setStatus("current")
_NlFramesPercent_Type = Gauge32
_NlFramesPercent_Object = MibTableColumn
nlFramesPercent = _NlFramesPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 13),
    _NlFramesPercent_Type()
)
nlFramesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlFramesPercent.setStatus("current")
_NlBytesPercent_Type = Gauge32
_NlBytesPercent_Object = MibTableColumn
nlBytesPercent = _NlBytesPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 1, 1, 14),
    _NlBytesPercent_Type()
)
nlBytesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlBytesPercent.setStatus("current")
_NetChanShortTermTable_Object = MibTable
netChanShortTermTable = _NetChanShortTermTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    netChanShortTermTable.setStatus("current")
_NetChanShortTermEntry_Object = MibTableRow
netChanShortTermEntry = _NetChanShortTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1)
)
netChanShortTermEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "nsTypeIndex"),
    (0, "CODIMA-EXPRESS-MIB", "nsNameIndex"),
    (0, "CODIMA-EXPRESS-MIB", "nsTimeStampIndex"),
)
if mibBuilder.loadTexts:
    netChanShortTermEntry.setStatus("current")


class _NsTypeIndex_Type(Integer32):
    """Custom type nsTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 2),
          ("netChannel", 1))
    )


_NsTypeIndex_Type.__name__ = "Integer32"
_NsTypeIndex_Object = MibTableColumn
nsTypeIndex = _NsTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 1),
    _NsTypeIndex_Type()
)
nsTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsTypeIndex.setStatus("current")


class _NsNameIndex_Type(DisplayString):
    """Custom type nsNameIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_NsNameIndex_Type.__name__ = "DisplayString"
_NsNameIndex_Object = MibTableColumn
nsNameIndex = _NsNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 2),
    _NsNameIndex_Type()
)
nsNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNameIndex.setStatus("current")
_NsTimeStampIndex_Type = Unsigned32
_NsTimeStampIndex_Object = MibTableColumn
nsTimeStampIndex = _NsTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 3),
    _NsTimeStampIndex_Type()
)
nsTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsTimeStampIndex.setStatus("current")


class _NsTimeStamp_Type(DisplayString):
    """Custom type nsTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_NsTimeStamp_Type.__name__ = "DisplayString"
_NsTimeStamp_Object = MibTableColumn
nsTimeStamp = _NsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 4),
    _NsTimeStamp_Type()
)
nsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsTimeStamp.setStatus("current")
_NsFrames_Type = Counter32
_NsFrames_Object = MibTableColumn
nsFrames = _NsFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 5),
    _NsFrames_Type()
)
nsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsFrames.setStatus("current")
_NsBytes_Type = Counter32
_NsBytes_Object = MibTableColumn
nsBytes = _NsBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 6),
    _NsBytes_Type()
)
nsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBytes.setStatus("current")
_NsFrameSize_Type = Gauge32
_NsFrameSize_Object = MibTableColumn
nsFrameSize = _NsFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 7),
    _NsFrameSize_Type()
)
nsFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    nsFrameSize.setUnits("bytes")
_NsHardErrors_Type = Counter32
_NsHardErrors_Object = MibTableColumn
nsHardErrors = _NsHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 8),
    _NsHardErrors_Type()
)
nsHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHardErrors.setStatus("current")
_NsSoftErrors_Type = Counter32
_NsSoftErrors_Object = MibTableColumn
nsSoftErrors = _NsSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 9),
    _NsSoftErrors_Type()
)
nsSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSoftErrors.setStatus("current")
_NsUtilization_Type = Gauge32
_NsUtilization_Object = MibTableColumn
nsUtilization = _NsUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 10),
    _NsUtilization_Type()
)
nsUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsUtilization.setStatus("current")
_NsHardErrorsPercent_Type = Gauge32
_NsHardErrorsPercent_Object = MibTableColumn
nsHardErrorsPercent = _NsHardErrorsPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 11),
    _NsHardErrorsPercent_Type()
)
nsHardErrorsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHardErrorsPercent.setStatus("current")
_NsSoftErrorsPercent_Type = Gauge32
_NsSoftErrorsPercent_Object = MibTableColumn
nsSoftErrorsPercent = _NsSoftErrorsPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 12),
    _NsSoftErrorsPercent_Type()
)
nsSoftErrorsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSoftErrorsPercent.setStatus("current")
_NsFramesPercent_Type = Gauge32
_NsFramesPercent_Object = MibTableColumn
nsFramesPercent = _NsFramesPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 13),
    _NsFramesPercent_Type()
)
nsFramesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsFramesPercent.setStatus("current")
_NsBytesPercent_Type = Gauge32
_NsBytesPercent_Object = MibTableColumn
nsBytesPercent = _NsBytesPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 8, 2, 1, 14),
    _NsBytesPercent_Type()
)
nsBytesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBytesPercent.setStatus("current")
_DbVlan_ObjectIdentity = ObjectIdentity
dbVlan = _DbVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9)
)
if mibBuilder.loadTexts:
    dbVlan.setStatus("current")
_VlanLongTermTable_Object = MibTable
vlanLongTermTable = _VlanLongTermTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    vlanLongTermTable.setStatus("current")
_VlanLongTermEntry_Object = MibTableRow
vlanLongTermEntry = _VlanLongTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1)
)
vlanLongTermEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "vlIdIndex"),
    (0, "CODIMA-EXPRESS-MIB", "vlTimeStampIndex"),
)
if mibBuilder.loadTexts:
    vlanLongTermEntry.setStatus("current")


class _VlIdIndex_Type(Unsigned32):
    """Custom type vlIdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlIdIndex_Type.__name__ = "Unsigned32"
_VlIdIndex_Object = MibTableColumn
vlIdIndex = _VlIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 1),
    _VlIdIndex_Type()
)
vlIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlIdIndex.setStatus("current")
_VlTimeStampIndex_Type = Unsigned32
_VlTimeStampIndex_Object = MibTableColumn
vlTimeStampIndex = _VlTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 2),
    _VlTimeStampIndex_Type()
)
vlTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlTimeStampIndex.setStatus("current")


class _VlTimeStamp_Type(DisplayString):
    """Custom type vlTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_VlTimeStamp_Type.__name__ = "DisplayString"
_VlTimeStamp_Object = MibTableColumn
vlTimeStamp = _VlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 3),
    _VlTimeStamp_Type()
)
vlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlTimeStamp.setStatus("current")


class _VlName_Type(DisplayString):
    """Custom type vlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VlName_Type.__name__ = "DisplayString"
_VlName_Object = MibTableColumn
vlName = _VlName_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 4),
    _VlName_Type()
)
vlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlName.setStatus("current")
_VlFrames_Type = Counter32
_VlFrames_Object = MibTableColumn
vlFrames = _VlFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 5),
    _VlFrames_Type()
)
vlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlFrames.setStatus("current")
_VlBytes_Type = Counter32
_VlBytes_Object = MibTableColumn
vlBytes = _VlBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 6),
    _VlBytes_Type()
)
vlBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlBytes.setStatus("current")
_VlFrameSize_Type = Gauge32
_VlFrameSize_Object = MibTableColumn
vlFrameSize = _VlFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 7),
    _VlFrameSize_Type()
)
vlFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    vlFrameSize.setUnits("bytes")
_VlHardErrors_Type = Counter32
_VlHardErrors_Object = MibTableColumn
vlHardErrors = _VlHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 8),
    _VlHardErrors_Type()
)
vlHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlHardErrors.setStatus("current")
_VlSoftErrors_Type = Counter32
_VlSoftErrors_Object = MibTableColumn
vlSoftErrors = _VlSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 9),
    _VlSoftErrors_Type()
)
vlSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlSoftErrors.setStatus("current")
_VlUtilization_Type = Gauge32
_VlUtilization_Object = MibTableColumn
vlUtilization = _VlUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 10),
    _VlUtilization_Type()
)
vlUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlUtilization.setStatus("current")
_VlHardErrorsPercent_Type = Gauge32
_VlHardErrorsPercent_Object = MibTableColumn
vlHardErrorsPercent = _VlHardErrorsPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 11),
    _VlHardErrorsPercent_Type()
)
vlHardErrorsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlHardErrorsPercent.setStatus("current")
_VlSoftErrorsPercent_Type = Gauge32
_VlSoftErrorsPercent_Object = MibTableColumn
vlSoftErrorsPercent = _VlSoftErrorsPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 12),
    _VlSoftErrorsPercent_Type()
)
vlSoftErrorsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlSoftErrorsPercent.setStatus("current")
_VlFramesPercent_Type = Gauge32
_VlFramesPercent_Object = MibTableColumn
vlFramesPercent = _VlFramesPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 13),
    _VlFramesPercent_Type()
)
vlFramesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlFramesPercent.setStatus("current")
_VlBytesPercent_Type = Gauge32
_VlBytesPercent_Object = MibTableColumn
vlBytesPercent = _VlBytesPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 1, 1, 14),
    _VlBytesPercent_Type()
)
vlBytesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlBytesPercent.setStatus("current")
_VlanShortTermTable_Object = MibTable
vlanShortTermTable = _VlanShortTermTable_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2)
)
if mibBuilder.loadTexts:
    vlanShortTermTable.setStatus("current")
_VlanShortTermEntry_Object = MibTableRow
vlanShortTermEntry = _VlanShortTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1)
)
vlanShortTermEntry.setIndexNames(
    (0, "CODIMA-EXPRESS-MIB", "vsIdIndex"),
    (0, "CODIMA-EXPRESS-MIB", "vsTimeStampIndex"),
)
if mibBuilder.loadTexts:
    vlanShortTermEntry.setStatus("current")


class _VsIdIndex_Type(Unsigned32):
    """Custom type vsIdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VsIdIndex_Type.__name__ = "Unsigned32"
_VsIdIndex_Object = MibTableColumn
vsIdIndex = _VsIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 1),
    _VsIdIndex_Type()
)
vsIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsIdIndex.setStatus("current")
_VsTimeStampIndex_Type = Unsigned32
_VsTimeStampIndex_Object = MibTableColumn
vsTimeStampIndex = _VsTimeStampIndex_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 2),
    _VsTimeStampIndex_Type()
)
vsTimeStampIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsTimeStampIndex.setStatus("current")


class _VsTimeStamp_Type(DisplayString):
    """Custom type vsTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_VsTimeStamp_Type.__name__ = "DisplayString"
_VsTimeStamp_Object = MibTableColumn
vsTimeStamp = _VsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 3),
    _VsTimeStamp_Type()
)
vsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsTimeStamp.setStatus("current")


class _VsName_Type(DisplayString):
    """Custom type vsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VsName_Type.__name__ = "DisplayString"
_VsName_Object = MibTableColumn
vsName = _VsName_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 4),
    _VsName_Type()
)
vsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsName.setStatus("current")
_VsFrames_Type = Counter32
_VsFrames_Object = MibTableColumn
vsFrames = _VsFrames_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 5),
    _VsFrames_Type()
)
vsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFrames.setStatus("current")
_VsBytes_Type = Counter32
_VsBytes_Object = MibTableColumn
vsBytes = _VsBytes_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 6),
    _VsBytes_Type()
)
vsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsBytes.setStatus("current")
_VsFrameSize_Type = Gauge32
_VsFrameSize_Object = MibTableColumn
vsFrameSize = _VsFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 7),
    _VsFrameSize_Type()
)
vsFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    vsFrameSize.setUnits("bytes")
_VsHardErrors_Type = Counter32
_VsHardErrors_Object = MibTableColumn
vsHardErrors = _VsHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 8),
    _VsHardErrors_Type()
)
vsHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsHardErrors.setStatus("current")
_VsSoftErrors_Type = Counter32
_VsSoftErrors_Object = MibTableColumn
vsSoftErrors = _VsSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 9),
    _VsSoftErrors_Type()
)
vsSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsSoftErrors.setStatus("current")
_VsUtilization_Type = Gauge32
_VsUtilization_Object = MibTableColumn
vsUtilization = _VsUtilization_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 10),
    _VsUtilization_Type()
)
vsUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsUtilization.setStatus("current")
_VsHardErrorsPercent_Type = Gauge32
_VsHardErrorsPercent_Object = MibTableColumn
vsHardErrorsPercent = _VsHardErrorsPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 11),
    _VsHardErrorsPercent_Type()
)
vsHardErrorsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsHardErrorsPercent.setStatus("current")
_VsSoftErrorsPercent_Type = Gauge32
_VsSoftErrorsPercent_Object = MibTableColumn
vsSoftErrorsPercent = _VsSoftErrorsPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 12),
    _VsSoftErrorsPercent_Type()
)
vsSoftErrorsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsSoftErrorsPercent.setStatus("current")
_VsFramesPercent_Type = Gauge32
_VsFramesPercent_Object = MibTableColumn
vsFramesPercent = _VsFramesPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 13),
    _VsFramesPercent_Type()
)
vsFramesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramesPercent.setStatus("current")
_VsBytesPercent_Type = Gauge32
_VsBytesPercent_Object = MibTableColumn
vsBytesPercent = _VsBytesPercent_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 1, 9, 2, 1, 14),
    _VsBytesPercent_Type()
)
vsBytesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsBytesPercent.setStatus("current")
_ExpAlarms_ObjectIdentity = ObjectIdentity
expAlarms = _ExpAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    expAlarms.setStatus("current")
_AlarmMessage_Type = DisplayString
_AlarmMessage_Object = MibScalar
alarmMessage = _AlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 2, 1),
    _AlarmMessage_Type()
)
alarmMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmMessage.setStatus("current")
_AlarmLayer_Type = DisplayString
_AlarmLayer_Object = MibScalar
alarmLayer = _AlarmLayer_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 2, 2),
    _AlarmLayer_Type()
)
alarmLayer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmLayer.setStatus("current")
_AlarmTopProtocol_Type = DisplayString
_AlarmTopProtocol_Object = MibScalar
alarmTopProtocol = _AlarmTopProtocol_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 2, 3),
    _AlarmTopProtocol_Type()
)
alarmTopProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmTopProtocol.setStatus("current")
_AlarmBaseProtocol_Type = DisplayString
_AlarmBaseProtocol_Object = MibScalar
alarmBaseProtocol = _AlarmBaseProtocol_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 2, 4),
    _AlarmBaseProtocol_Type()
)
alarmBaseProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmBaseProtocol.setStatus("current")
_AlarmCode_Type = DisplayString
_AlarmCode_Object = MibScalar
alarmCode = _AlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 2, 5),
    _AlarmCode_Type()
)
alarmCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmCode.setStatus("current")
_AlarmFunction_Type = DisplayString
_AlarmFunction_Object = MibScalar
alarmFunction = _AlarmFunction_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 2, 6),
    _AlarmFunction_Type()
)
alarmFunction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmFunction.setStatus("current")
_AlarmGroup_Type = DisplayString
_AlarmGroup_Object = MibScalar
alarmGroup = _AlarmGroup_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 2, 7),
    _AlarmGroup_Type()
)
alarmGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmGroup.setStatus("current")
_AlarmUnitType_Type = DisplayString
_AlarmUnitType_Object = MibScalar
alarmUnitType = _AlarmUnitType_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 2, 8),
    _AlarmUnitType_Type()
)
alarmUnitType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmUnitType.setStatus("current")
_AlarmClass_Type = DisplayString
_AlarmClass_Object = MibScalar
alarmClass = _AlarmClass_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 2, 9),
    _AlarmClass_Type()
)
alarmClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmClass.setStatus("current")
_AlarmTime_Type = DisplayString
_AlarmTime_Object = MibScalar
alarmTime = _AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 1, 2, 10),
    _AlarmTime_Type()
)
alarmTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmTime.setStatus("current")
_CodimaExpressNotifications_ObjectIdentity = ObjectIdentity
codimaExpressNotifications = _CodimaExpressNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 2)
)
if mibBuilder.loadTexts:
    codimaExpressNotifications.setStatus("current")
_ExpressTraps_ObjectIdentity = ObjectIdentity
expressTraps = _ExpressTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    expressTraps.setStatus("current")
_CodimaExpressConformance_ObjectIdentity = ObjectIdentity
codimaExpressConformance = _CodimaExpressConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3)
)
if mibBuilder.loadTexts:
    codimaExpressConformance.setStatus("current")
_ExpressObjectGroups_ObjectIdentity = ObjectIdentity
expressObjectGroups = _ExpressObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1)
)
_HistoryDatabaseGroups_ObjectIdentity = ObjectIdentity
historyDatabaseGroups = _HistoryDatabaseGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1)
)
_DbControlGroups_ObjectIdentity = ObjectIdentity
dbControlGroups = _DbControlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 1)
)
_DbSegmentGroups_ObjectIdentity = ObjectIdentity
dbSegmentGroups = _DbSegmentGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2)
)
_SegLongTermGroups_ObjectIdentity = ObjectIdentity
segLongTermGroups = _SegLongTermGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 1)
)
_SegShortTermGroups_ObjectIdentity = ObjectIdentity
segShortTermGroups = _SegShortTermGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 2)
)
_DbMacGroups_ObjectIdentity = ObjectIdentity
dbMacGroups = _DbMacGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3)
)
_MacLongTermGroups_ObjectIdentity = ObjectIdentity
macLongTermGroups = _MacLongTermGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 1)
)
_MacShortTermGroups_ObjectIdentity = ObjectIdentity
macShortTermGroups = _MacShortTermGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 2)
)
_DbMacPeerGroups_ObjectIdentity = ObjectIdentity
dbMacPeerGroups = _DbMacPeerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 4)
)
_MacPeerLongTermGroups_ObjectIdentity = ObjectIdentity
macPeerLongTermGroups = _MacPeerLongTermGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 4, 1)
)
_MacPeerShortTermGroups_ObjectIdentity = ObjectIdentity
macPeerShortTermGroups = _MacPeerShortTermGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 4, 2)
)
_DbIPv4Groups_ObjectIdentity = ObjectIdentity
dbIPv4Groups = _DbIPv4Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 5)
)
_IpLongTermGroups_ObjectIdentity = ObjectIdentity
ipLongTermGroups = _IpLongTermGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 5, 1)
)
_IpShortTermGroups_ObjectIdentity = ObjectIdentity
ipShortTermGroups = _IpShortTermGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 5, 2)
)
_DpIPv4PeerGroups_ObjectIdentity = ObjectIdentity
dpIPv4PeerGroups = _DpIPv4PeerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 6)
)
_IpPeerLongTermGroups_ObjectIdentity = ObjectIdentity
ipPeerLongTermGroups = _IpPeerLongTermGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 6, 1)
)
_IpPeerShortTermGroups_ObjectIdentity = ObjectIdentity
ipPeerShortTermGroups = _IpPeerShortTermGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 6, 2)
)
_DbProtocolGroups_ObjectIdentity = ObjectIdentity
dbProtocolGroups = _DbProtocolGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 7)
)
_ProtocolLongTermGroups_ObjectIdentity = ObjectIdentity
protocolLongTermGroups = _ProtocolLongTermGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 7, 1)
)
_ProtocolShortTermGroups_ObjectIdentity = ObjectIdentity
protocolShortTermGroups = _ProtocolShortTermGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 7, 2)
)
_DbNetChannelGroups_ObjectIdentity = ObjectIdentity
dbNetChannelGroups = _DbNetChannelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 8)
)
_DbVlanGroups_ObjectIdentity = ObjectIdentity
dbVlanGroups = _DbVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 9)
)
_ExpressNotificationGroups_ObjectIdentity = ObjectIdentity
expressNotificationGroups = _ExpressNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 2)
)

# Managed Objects groups

ctrlTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 1, 1)
)
ctrlTimeGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "ctSampleType"),
        ("CODIMA-EXPRESS-MIB", "ctTimeSlots"),
        ("CODIMA-EXPRESS-MIB", "ctLockMethod"),
        ("CODIMA-EXPRESS-MIB", "ctLockUserTime"),
        ("CODIMA-EXPRESS-MIB", "ctLockRealTime"))
)
if mibBuilder.loadTexts:
    ctrlTimeGroup.setStatus("current")

slBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 1, 1)
)
slBaseGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "slbTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "slbTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "slbFrames"),
        ("CODIMA-EXPRESS-MIB", "slbBytes"),
        ("CODIMA-EXPRESS-MIB", "slbFrameSize"),
        ("CODIMA-EXPRESS-MIB", "slbHardwareErrors"),
        ("CODIMA-EXPRESS-MIB", "slbSoftwareErrors"),
        ("CODIMA-EXPRESS-MIB", "slbActiveNodes"))
)
if mibBuilder.loadTexts:
    slBaseGroup.setStatus("current")

slBroadcastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 1, 2)
)
slBroadcastGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "slbcTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "slbcTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "slbcBytes"),
        ("CODIMA-EXPRESS-MIB", "slbcPercentBytes"),
        ("CODIMA-EXPRESS-MIB", "slbcFrames"),
        ("CODIMA-EXPRESS-MIB", "slbcPercentFrames"))
)
if mibBuilder.loadTexts:
    slBroadcastGroup.setStatus("current")

slDerivedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 1, 3)
)
slDerivedGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "sldTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "sldTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "sldUtilization"),
        ("CODIMA-EXPRESS-MIB", "sldErrorFrames"))
)
if mibBuilder.loadTexts:
    slDerivedGroup.setStatus("current")

slEthernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 1, 4)
)
slEthernetGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "sleTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "sleTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "sleRunts"),
        ("CODIMA-EXPRESS-MIB", "sleJabbers"),
        ("CODIMA-EXPRESS-MIB", "sleCrc"),
        ("CODIMA-EXPRESS-MIB", "sleCollisions"),
        ("CODIMA-EXPRESS-MIB", "sleLateCollisions"))
)
if mibBuilder.loadTexts:
    slEthernetGroup.setStatus("current")

slIcmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 1, 5)
)
slIcmpGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "sliTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "sliTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "sliPing"),
        ("CODIMA-EXPRESS-MIB", "sliSrcQuench"),
        ("CODIMA-EXPRESS-MIB", "sliRedirect"),
        ("CODIMA-EXPRESS-MIB", "sliTtlExceeded"),
        ("CODIMA-EXPRESS-MIB", "sliParamProblem"),
        ("CODIMA-EXPRESS-MIB", "sliTimestamp"),
        ("CODIMA-EXPRESS-MIB", "sliFragTimeout"),
        ("CODIMA-EXPRESS-MIB", "sliNetUnreachable"),
        ("CODIMA-EXPRESS-MIB", "sliHostUnreachable"),
        ("CODIMA-EXPRESS-MIB", "sliProtocolUnreachable"),
        ("CODIMA-EXPRESS-MIB", "sliPortUnreachable"),
        ("CODIMA-EXPRESS-MIB", "sliFragRequired"),
        ("CODIMA-EXPRESS-MIB", "sliSrcRouteFail"),
        ("CODIMA-EXPRESS-MIB", "sliDestNetUnknown"),
        ("CODIMA-EXPRESS-MIB", "sliDestHostUnknown"),
        ("CODIMA-EXPRESS-MIB", "sliSrcHostIsolated"),
        ("CODIMA-EXPRESS-MIB", "sliNetProhibited"),
        ("CODIMA-EXPRESS-MIB", "sliHostProhibited"),
        ("CODIMA-EXPRESS-MIB", "sliNetTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "sliHostTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "sliPerformance"),
        ("CODIMA-EXPRESS-MIB", "sliNetRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "sliHostRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "sliAppRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "sliRouteChange"),
        ("CODIMA-EXPRESS-MIB", "sliGrpErrors"),
        ("CODIMA-EXPRESS-MIB", "sliMaintenance"))
)
if mibBuilder.loadTexts:
    slIcmpGroup.setStatus("current")

slPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 1, 6)
)
slPortGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "slp1TimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "slp1TimeStamp"),
        ("CODIMA-EXPRESS-MIB", "slp1Frames"),
        ("CODIMA-EXPRESS-MIB", "slp1Bytes"),
        ("CODIMA-EXPRESS-MIB", "slp1FrameSize"),
        ("CODIMA-EXPRESS-MIB", "slp1Utilization"),
        ("CODIMA-EXPRESS-MIB", "slp1LineSpeed"),
        ("CODIMA-EXPRESS-MIB", "slp1SoftErrors"),
        ("CODIMA-EXPRESS-MIB", "slp1Runts"),
        ("CODIMA-EXPRESS-MIB", "slp1Jabbers"),
        ("CODIMA-EXPRESS-MIB", "slp1Crc"),
        ("CODIMA-EXPRESS-MIB", "slp1Collisions"),
        ("CODIMA-EXPRESS-MIB", "slp1LateCollisions"),
        ("CODIMA-EXPRESS-MIB", "slp1LineNoise"),
        ("CODIMA-EXPRESS-MIB", "slp2Frames"),
        ("CODIMA-EXPRESS-MIB", "slp2Bytes"),
        ("CODIMA-EXPRESS-MIB", "slp2FrameSize"),
        ("CODIMA-EXPRESS-MIB", "slp2Utilization"),
        ("CODIMA-EXPRESS-MIB", "slp2LineSpeed"),
        ("CODIMA-EXPRESS-MIB", "slp2SoftErrors"),
        ("CODIMA-EXPRESS-MIB", "slp2Runts"),
        ("CODIMA-EXPRESS-MIB", "slp2Jabbers"),
        ("CODIMA-EXPRESS-MIB", "slp2Crc"),
        ("CODIMA-EXPRESS-MIB", "slp2Collisions"),
        ("CODIMA-EXPRESS-MIB", "slp2LateCollisions"),
        ("CODIMA-EXPRESS-MIB", "slp2LineNoise"))
)
if mibBuilder.loadTexts:
    slPortGroup.setStatus("current")

ssBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 2, 1)
)
ssBaseGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "ssbTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "ssbTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "ssbFrames"),
        ("CODIMA-EXPRESS-MIB", "ssbBytes"),
        ("CODIMA-EXPRESS-MIB", "ssbFrameSize"),
        ("CODIMA-EXPRESS-MIB", "ssbHardwareErrors"),
        ("CODIMA-EXPRESS-MIB", "ssbSoftwareErrors"),
        ("CODIMA-EXPRESS-MIB", "ssbActiveNodes"))
)
if mibBuilder.loadTexts:
    ssBaseGroup.setStatus("current")

ssBroadcastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 2, 2)
)
ssBroadcastGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "ssbcTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "ssbcTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "ssbcBytes"),
        ("CODIMA-EXPRESS-MIB", "ssbcBytesPercent"),
        ("CODIMA-EXPRESS-MIB", "ssbcFrames"),
        ("CODIMA-EXPRESS-MIB", "ssbcFramesPercent"))
)
if mibBuilder.loadTexts:
    ssBroadcastGroup.setStatus("current")

ssDerivedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 2, 3)
)
ssDerivedGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "ssdTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "ssdTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "ssdUtilization"),
        ("CODIMA-EXPRESS-MIB", "ssdErrorFrames"))
)
if mibBuilder.loadTexts:
    ssDerivedGroup.setStatus("current")

ssEthernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 2, 4)
)
ssEthernetGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "sseTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "sseTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "sseRunts"),
        ("CODIMA-EXPRESS-MIB", "sseJabbers"),
        ("CODIMA-EXPRESS-MIB", "sseCrc"),
        ("CODIMA-EXPRESS-MIB", "sseCollisions"),
        ("CODIMA-EXPRESS-MIB", "sseLateCollisions"))
)
if mibBuilder.loadTexts:
    ssEthernetGroup.setStatus("current")

ssIcmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 2, 5)
)
ssIcmpGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "ssiTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "ssiTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "ssiPing"),
        ("CODIMA-EXPRESS-MIB", "ssiSrcQuench"),
        ("CODIMA-EXPRESS-MIB", "ssiRedirect"),
        ("CODIMA-EXPRESS-MIB", "ssiTtlExceeded"),
        ("CODIMA-EXPRESS-MIB", "ssiParamProblem"),
        ("CODIMA-EXPRESS-MIB", "ssiTimestamp"),
        ("CODIMA-EXPRESS-MIB", "ssiFragTimeout"),
        ("CODIMA-EXPRESS-MIB", "ssiNetUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ssiHostUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ssiProtocolUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ssiPortUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ssiFragRequired"),
        ("CODIMA-EXPRESS-MIB", "ssiSrcRouteFail"),
        ("CODIMA-EXPRESS-MIB", "ssiDestNetUnknown"),
        ("CODIMA-EXPRESS-MIB", "ssiDestHostUnknown"),
        ("CODIMA-EXPRESS-MIB", "ssiSrcHostIsolated"),
        ("CODIMA-EXPRESS-MIB", "ssiNetProhibited"),
        ("CODIMA-EXPRESS-MIB", "ssiHostProhibited"),
        ("CODIMA-EXPRESS-MIB", "ssiNetTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ssiHostTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ssiPerformance"),
        ("CODIMA-EXPRESS-MIB", "ssiNetRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "ssiHostRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "ssiAppRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "ssiRouteChange"),
        ("CODIMA-EXPRESS-MIB", "ssiErrors"),
        ("CODIMA-EXPRESS-MIB", "ssiMaintenance"))
)
if mibBuilder.loadTexts:
    ssIcmpGroup.setStatus("current")

ssPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 2, 2, 6)
)
ssPortGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "sspTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "sspTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "ssp1Frames"),
        ("CODIMA-EXPRESS-MIB", "ssp1Bytes"),
        ("CODIMA-EXPRESS-MIB", "ssp1FrameSize"),
        ("CODIMA-EXPRESS-MIB", "ssp1Utilization"),
        ("CODIMA-EXPRESS-MIB", "ssp1LineSpeed"),
        ("CODIMA-EXPRESS-MIB", "ssp1SoftErrors"),
        ("CODIMA-EXPRESS-MIB", "ssp1Runts"),
        ("CODIMA-EXPRESS-MIB", "ssp1Jabbers"),
        ("CODIMA-EXPRESS-MIB", "ssp1Crc"),
        ("CODIMA-EXPRESS-MIB", "ssp1Collisions"),
        ("CODIMA-EXPRESS-MIB", "ssp1LateCollisions"),
        ("CODIMA-EXPRESS-MIB", "ssp1LineNoise"),
        ("CODIMA-EXPRESS-MIB", "ssp2Frames"),
        ("CODIMA-EXPRESS-MIB", "ssp2Bytes"),
        ("CODIMA-EXPRESS-MIB", "ssp2FrameSize"),
        ("CODIMA-EXPRESS-MIB", "ssp2Utilization"),
        ("CODIMA-EXPRESS-MIB", "ssp2LineSpeed"),
        ("CODIMA-EXPRESS-MIB", "ssp2SoftErrors"),
        ("CODIMA-EXPRESS-MIB", "ssp2Runts"),
        ("CODIMA-EXPRESS-MIB", "ssp2Jabbers"),
        ("CODIMA-EXPRESS-MIB", "ssp2Crc"),
        ("CODIMA-EXPRESS-MIB", "ssp2Collisions"),
        ("CODIMA-EXPRESS-MIB", "ssp2LateCollisions"),
        ("CODIMA-EXPRESS-MIB", "ssp2LineNoise"))
)
if mibBuilder.loadTexts:
    ssPortGroup.setStatus("current")

mlBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 1, 1)
)
mlBaseGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mlbMacIndex"),
        ("CODIMA-EXPRESS-MIB", "mlbTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mlbTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mlbFrames"),
        ("CODIMA-EXPRESS-MIB", "mlbBytes"),
        ("CODIMA-EXPRESS-MIB", "mlbFrameSize"),
        ("CODIMA-EXPRESS-MIB", "mlbHardwareErrors"),
        ("CODIMA-EXPRESS-MIB", "mlbSoftwareErrors"))
)
if mibBuilder.loadTexts:
    mlBaseGroup.setStatus("current")

mlDerivedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 1, 2)
)
mlDerivedGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mldMacIndex"),
        ("CODIMA-EXPRESS-MIB", "mldTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mldTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mldUtilization"),
        ("CODIMA-EXPRESS-MIB", "mldErrorFrames"))
)
if mibBuilder.loadTexts:
    mlDerivedGroup.setStatus("current")

mlDuplexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 1, 3)
)
mlDuplexGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mlduMacIndex"),
        ("CODIMA-EXPRESS-MIB", "mlduTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mlduTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mlduTxFrames"),
        ("CODIMA-EXPRESS-MIB", "mlduTxBytes"),
        ("CODIMA-EXPRESS-MIB", "mlduTxFrameSize"),
        ("CODIMA-EXPRESS-MIB", "mlduTxUtilization"),
        ("CODIMA-EXPRESS-MIB", "mlduRxFrames"),
        ("CODIMA-EXPRESS-MIB", "mlduRxBytes"),
        ("CODIMA-EXPRESS-MIB", "mlduRxFrameSize"),
        ("CODIMA-EXPRESS-MIB", "mlduRxUtilization"))
)
if mibBuilder.loadTexts:
    mlDuplexGroup.setStatus("current")

mlEthernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 1, 4)
)
mlEthernetGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mleMacIndex"),
        ("CODIMA-EXPRESS-MIB", "mleTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mleTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mleRunts"),
        ("CODIMA-EXPRESS-MIB", "mleJabbers"),
        ("CODIMA-EXPRESS-MIB", "mleCrc"),
        ("CODIMA-EXPRESS-MIB", "mleCollisions"),
        ("CODIMA-EXPRESS-MIB", "mleLateCollisions"))
)
if mibBuilder.loadTexts:
    mlEthernetGroup.setStatus("current")

mlIcmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 1, 5)
)
mlIcmpGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mliMacIndex"),
        ("CODIMA-EXPRESS-MIB", "mliTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mliTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mliPing"),
        ("CODIMA-EXPRESS-MIB", "mliSrcQuench"),
        ("CODIMA-EXPRESS-MIB", "mliRedirect"),
        ("CODIMA-EXPRESS-MIB", "mliTtlExceeded"),
        ("CODIMA-EXPRESS-MIB", "mliParamProblem"),
        ("CODIMA-EXPRESS-MIB", "mliTimestamp"),
        ("CODIMA-EXPRESS-MIB", "mliFragTimeout"),
        ("CODIMA-EXPRESS-MIB", "mliNetUnreachable"),
        ("CODIMA-EXPRESS-MIB", "mliHostUnreachable"),
        ("CODIMA-EXPRESS-MIB", "mliProtocolUnreachable"),
        ("CODIMA-EXPRESS-MIB", "mliPortUnreachable"),
        ("CODIMA-EXPRESS-MIB", "mliFragRequired"),
        ("CODIMA-EXPRESS-MIB", "mliSrcRouteFail"),
        ("CODIMA-EXPRESS-MIB", "mliDestNetUnknown"),
        ("CODIMA-EXPRESS-MIB", "mliDestHostUnknown"),
        ("CODIMA-EXPRESS-MIB", "mliSrcHostIsolated"),
        ("CODIMA-EXPRESS-MIB", "mliNetProhibited"),
        ("CODIMA-EXPRESS-MIB", "mliHostProhibited"),
        ("CODIMA-EXPRESS-MIB", "mliNetTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "mliHostTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "mliPerformance"),
        ("CODIMA-EXPRESS-MIB", "mliNetRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "mliHostRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "mliAppRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "mliRouteChange"),
        ("CODIMA-EXPRESS-MIB", "mliErrors"),
        ("CODIMA-EXPRESS-MIB", "mliMaintenance"))
)
if mibBuilder.loadTexts:
    mlIcmpGroup.setStatus("current")

mlProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 1, 6)
)
mlProtocolGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mlpMacIndex"),
        ("CODIMA-EXPRESS-MIB", "mlpTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mlpTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mlpNovell"),
        ("CODIMA-EXPRESS-MIB", "mlpSnmp"),
        ("CODIMA-EXPRESS-MIB", "mlpRouting"),
        ("CODIMA-EXPRESS-MIB", "mlpWww"),
        ("CODIMA-EXPRESS-MIB", "mlpIcmp"),
        ("CODIMA-EXPRESS-MIB", "mlpIso"),
        ("CODIMA-EXPRESS-MIB", "mlpMail"),
        ("CODIMA-EXPRESS-MIB", "mlpNetbios"),
        ("CODIMA-EXPRESS-MIB", "mlpDns"),
        ("CODIMA-EXPRESS-MIB", "mlpIp"),
        ("CODIMA-EXPRESS-MIB", "mlpVoip"),
        ("CODIMA-EXPRESS-MIB", "mlpLayer3Traffic"),
        ("CODIMA-EXPRESS-MIB", "mlpIpData"),
        ("CODIMA-EXPRESS-MIB", "mlpApplications"),
        ("CODIMA-EXPRESS-MIB", "mlpIpControl"),
        ("CODIMA-EXPRESS-MIB", "mlpManagement"))
)
if mibBuilder.loadTexts:
    mlProtocolGroup.setStatus("current")

msBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 2, 1)
)
msBaseGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "msbMacIndex"),
        ("CODIMA-EXPRESS-MIB", "msbTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "msbTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "msbFrames"),
        ("CODIMA-EXPRESS-MIB", "msbBytes"),
        ("CODIMA-EXPRESS-MIB", "msbFrameSize"),
        ("CODIMA-EXPRESS-MIB", "msbHardwareErrors"),
        ("CODIMA-EXPRESS-MIB", "msbSoftwareErrors"))
)
if mibBuilder.loadTexts:
    msBaseGroup.setStatus("current")

msDerivedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 2, 2)
)
msDerivedGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "msdMacIndex"),
        ("CODIMA-EXPRESS-MIB", "msdTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "msdTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "msdUtilization"),
        ("CODIMA-EXPRESS-MIB", "msdErrorFrames"))
)
if mibBuilder.loadTexts:
    msDerivedGroup.setStatus("current")

msDuplexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 2, 3)
)
msDuplexGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "msdpMacIndex"),
        ("CODIMA-EXPRESS-MIB", "msdpTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "msdpTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "msdpTxFrames"),
        ("CODIMA-EXPRESS-MIB", "msdpTxBytes"),
        ("CODIMA-EXPRESS-MIB", "msdpTxFrameSize"),
        ("CODIMA-EXPRESS-MIB", "msdpTxUtilization"),
        ("CODIMA-EXPRESS-MIB", "msdpRxFrames"),
        ("CODIMA-EXPRESS-MIB", "msdpRxBytes"),
        ("CODIMA-EXPRESS-MIB", "msdpRxFrameSize"),
        ("CODIMA-EXPRESS-MIB", "msdpRxUtilization"))
)
if mibBuilder.loadTexts:
    msDuplexGroup.setStatus("current")

msEthernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 2, 4)
)
msEthernetGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mseMacIndex"),
        ("CODIMA-EXPRESS-MIB", "mseTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mseTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mseRunts"),
        ("CODIMA-EXPRESS-MIB", "mseJabbers"),
        ("CODIMA-EXPRESS-MIB", "mseCrc"),
        ("CODIMA-EXPRESS-MIB", "mseCollisions"),
        ("CODIMA-EXPRESS-MIB", "mseLateCollisions"))
)
if mibBuilder.loadTexts:
    msEthernetGroup.setStatus("current")

msIcmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 2, 5)
)
msIcmpGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "msiMacIndex"),
        ("CODIMA-EXPRESS-MIB", "msiTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "msiTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "msiPing"),
        ("CODIMA-EXPRESS-MIB", "msiSrcQuench"),
        ("CODIMA-EXPRESS-MIB", "msiRedirect"),
        ("CODIMA-EXPRESS-MIB", "msiTtlExceeded"),
        ("CODIMA-EXPRESS-MIB", "msiParamProblem"),
        ("CODIMA-EXPRESS-MIB", "msiTimestamp"),
        ("CODIMA-EXPRESS-MIB", "msiFragTimeout"),
        ("CODIMA-EXPRESS-MIB", "msiNetUnreachable"),
        ("CODIMA-EXPRESS-MIB", "msiHostUnreachable"),
        ("CODIMA-EXPRESS-MIB", "msiProtocolUnreachable"),
        ("CODIMA-EXPRESS-MIB", "msiPortUnreachable"),
        ("CODIMA-EXPRESS-MIB", "msiFragRequired"),
        ("CODIMA-EXPRESS-MIB", "msiSrcRouteFail"),
        ("CODIMA-EXPRESS-MIB", "msiDestNetUnknown"),
        ("CODIMA-EXPRESS-MIB", "msiDestHostUnknown"),
        ("CODIMA-EXPRESS-MIB", "msiSrcHostIsolated"),
        ("CODIMA-EXPRESS-MIB", "msiNetProhibited"),
        ("CODIMA-EXPRESS-MIB", "msiHostProhibited"),
        ("CODIMA-EXPRESS-MIB", "msiNetTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "msiHostTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "msiPerformance"),
        ("CODIMA-EXPRESS-MIB", "msiNetRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "msiHostRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "msiAppRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "msiRouteChange"),
        ("CODIMA-EXPRESS-MIB", "msiErrors"),
        ("CODIMA-EXPRESS-MIB", "msiMaintenance"))
)
if mibBuilder.loadTexts:
    msIcmpGroup.setStatus("current")

msProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 3, 2, 6)
)
msProtocolGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mspMacIndex"),
        ("CODIMA-EXPRESS-MIB", "mspTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mspTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mspNovell"),
        ("CODIMA-EXPRESS-MIB", "mspSnmp"),
        ("CODIMA-EXPRESS-MIB", "mspRouting"),
        ("CODIMA-EXPRESS-MIB", "mspWww"),
        ("CODIMA-EXPRESS-MIB", "mspIcmp"),
        ("CODIMA-EXPRESS-MIB", "mspIso"),
        ("CODIMA-EXPRESS-MIB", "mspMail"),
        ("CODIMA-EXPRESS-MIB", "mspNetbios"),
        ("CODIMA-EXPRESS-MIB", "mspDns"),
        ("CODIMA-EXPRESS-MIB", "mspIp"),
        ("CODIMA-EXPRESS-MIB", "mspVoip"),
        ("CODIMA-EXPRESS-MIB", "mspLayer3Traffic"),
        ("CODIMA-EXPRESS-MIB", "mspIpData"),
        ("CODIMA-EXPRESS-MIB", "mspApplications"),
        ("CODIMA-EXPRESS-MIB", "mspIpControl"),
        ("CODIMA-EXPRESS-MIB", "mspManagement"))
)
if mibBuilder.loadTexts:
    msProtocolGroup.setStatus("current")

mplBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 4, 1, 1)
)
mplBaseGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mplbMac1Index"),
        ("CODIMA-EXPRESS-MIB", "mplbMac2Index"),
        ("CODIMA-EXPRESS-MIB", "mplbTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mplbTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mplbFrames"),
        ("CODIMA-EXPRESS-MIB", "mplbBytes"),
        ("CODIMA-EXPRESS-MIB", "mplbFrameSize"),
        ("CODIMA-EXPRESS-MIB", "mplbHardwareErrors"),
        ("CODIMA-EXPRESS-MIB", "mplbSoftwareErrors"))
)
if mibBuilder.loadTexts:
    mplBaseGroup.setStatus("current")

mplDerivedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 4, 1, 2)
)
mplDerivedGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mpldMac1Index"),
        ("CODIMA-EXPRESS-MIB", "mpldMac2Index"),
        ("CODIMA-EXPRESS-MIB", "mpldTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mpldTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mpldUtilization"),
        ("CODIMA-EXPRESS-MIB", "mpldErrorFrames"))
)
if mibBuilder.loadTexts:
    mplDerivedGroup.setStatus("current")

mplDuplexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 4, 1, 3)
)
mplDuplexGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mplduMac1Index"),
        ("CODIMA-EXPRESS-MIB", "mplduMac2Index"),
        ("CODIMA-EXPRESS-MIB", "mplduTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mplduTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mplduTxFrames"),
        ("CODIMA-EXPRESS-MIB", "mplduTxBytes"),
        ("CODIMA-EXPRESS-MIB", "mplduTxFrameSize"),
        ("CODIMA-EXPRESS-MIB", "mplduTxUtilization"),
        ("CODIMA-EXPRESS-MIB", "mplduRxFrames"),
        ("CODIMA-EXPRESS-MIB", "mplduRxBytes"),
        ("CODIMA-EXPRESS-MIB", "mplduRxFrameSize"),
        ("CODIMA-EXPRESS-MIB", "mplduRxUtilization"))
)
if mibBuilder.loadTexts:
    mplDuplexGroup.setStatus("current")

mplProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 4, 1, 4)
)
mplProtocolGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mplpMac1Index"),
        ("CODIMA-EXPRESS-MIB", "mplpMac2Index"),
        ("CODIMA-EXPRESS-MIB", "mplpTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mplpTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mplpNovell"),
        ("CODIMA-EXPRESS-MIB", "mplpSnmp"),
        ("CODIMA-EXPRESS-MIB", "mplpRouting"),
        ("CODIMA-EXPRESS-MIB", "mplpWww"),
        ("CODIMA-EXPRESS-MIB", "mplpIcmp"),
        ("CODIMA-EXPRESS-MIB", "mplpIso"),
        ("CODIMA-EXPRESS-MIB", "mplpMail"),
        ("CODIMA-EXPRESS-MIB", "mplpNetbios"),
        ("CODIMA-EXPRESS-MIB", "mplpDns"),
        ("CODIMA-EXPRESS-MIB", "mplpIp"),
        ("CODIMA-EXPRESS-MIB", "mplpVoip"),
        ("CODIMA-EXPRESS-MIB", "mplpLayer3Traffic"),
        ("CODIMA-EXPRESS-MIB", "mplpIpData"),
        ("CODIMA-EXPRESS-MIB", "mplpApplications"),
        ("CODIMA-EXPRESS-MIB", "mplpIpControl"),
        ("CODIMA-EXPRESS-MIB", "mplpManagement"))
)
if mibBuilder.loadTexts:
    mplProtocolGroup.setStatus("current")

mpsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 4, 2, 1)
)
mpsBaseGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mpsbMac1Index"),
        ("CODIMA-EXPRESS-MIB", "mpsbMac2Index"),
        ("CODIMA-EXPRESS-MIB", "mpsbTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mpsbTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mpsbFrames"),
        ("CODIMA-EXPRESS-MIB", "mpsbBytes"),
        ("CODIMA-EXPRESS-MIB", "mpsbFrameSize"),
        ("CODIMA-EXPRESS-MIB", "mpsbHardwareErrors"),
        ("CODIMA-EXPRESS-MIB", "mpsbSoftwareErrors"))
)
if mibBuilder.loadTexts:
    mpsBaseGroup.setStatus("current")

mpsDerivedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 4, 2, 2)
)
mpsDerivedGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mpsdMac1Index"),
        ("CODIMA-EXPRESS-MIB", "mpsdMac2Index"),
        ("CODIMA-EXPRESS-MIB", "mpsdTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mpsdTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mpsdUtilization"),
        ("CODIMA-EXPRESS-MIB", "mpsdErrorFrames"))
)
if mibBuilder.loadTexts:
    mpsDerivedGroup.setStatus("current")

mpsDuplexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 4, 2, 3)
)
mpsDuplexGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mpsduMac1Index"),
        ("CODIMA-EXPRESS-MIB", "mpsduMac2Index"),
        ("CODIMA-EXPRESS-MIB", "mpsduTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mpsduTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mpsduTxFrames"),
        ("CODIMA-EXPRESS-MIB", "mpsduTxBytes"),
        ("CODIMA-EXPRESS-MIB", "mpsduTxFrameSize"),
        ("CODIMA-EXPRESS-MIB", "mpsduTxUtilization"),
        ("CODIMA-EXPRESS-MIB", "mpsduRxFrames"),
        ("CODIMA-EXPRESS-MIB", "mpsduRxBytes"),
        ("CODIMA-EXPRESS-MIB", "mpsduRxFrameSize"),
        ("CODIMA-EXPRESS-MIB", "mpsduRxUtilization"))
)
if mibBuilder.loadTexts:
    mpsDuplexGroup.setStatus("current")

mpsProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 4, 2, 4)
)
mpsProtocolGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "mpspMac1Index"),
        ("CODIMA-EXPRESS-MIB", "mpspMac2Index"),
        ("CODIMA-EXPRESS-MIB", "mpspTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "mpspTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "mpspNovell"),
        ("CODIMA-EXPRESS-MIB", "mpspSnmp"),
        ("CODIMA-EXPRESS-MIB", "mpspRouting"),
        ("CODIMA-EXPRESS-MIB", "mpspWww"),
        ("CODIMA-EXPRESS-MIB", "mpspIcmp"),
        ("CODIMA-EXPRESS-MIB", "mpspIso"),
        ("CODIMA-EXPRESS-MIB", "mpspMail"),
        ("CODIMA-EXPRESS-MIB", "mpspNetbios"),
        ("CODIMA-EXPRESS-MIB", "mpspDns"),
        ("CODIMA-EXPRESS-MIB", "mpspIp"),
        ("CODIMA-EXPRESS-MIB", "mpspVoip"),
        ("CODIMA-EXPRESS-MIB", "mpspLayer3Traffic"),
        ("CODIMA-EXPRESS-MIB", "mpspIpData"),
        ("CODIMA-EXPRESS-MIB", "mpspApplications"),
        ("CODIMA-EXPRESS-MIB", "mpspIpControl"),
        ("CODIMA-EXPRESS-MIB", "mpspManagement"))
)
if mibBuilder.loadTexts:
    mpsProtocolGroup.setStatus("current")

ilBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 5, 1, 1)
)
ilBaseGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "ilbIpIndex"),
        ("CODIMA-EXPRESS-MIB", "ilbTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "ilbTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "ilbFrames"),
        ("CODIMA-EXPRESS-MIB", "ilbBytes"),
        ("CODIMA-EXPRESS-MIB", "ilbFrameSize"),
        ("CODIMA-EXPRESS-MIB", "ilbHardwareErrors"),
        ("CODIMA-EXPRESS-MIB", "ilbSoftwareErrors"))
)
if mibBuilder.loadTexts:
    ilBaseGroup.setStatus("current")

ilDerivedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 5, 1, 2)
)
ilDerivedGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "ildIpIndex"),
        ("CODIMA-EXPRESS-MIB", "ildTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "ildTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "ildUtilization"),
        ("CODIMA-EXPRESS-MIB", "ildErrorFrames"))
)
if mibBuilder.loadTexts:
    ilDerivedGroup.setStatus("current")

ilIcmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 5, 1, 3)
)
ilIcmpGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "iliIpIndex"),
        ("CODIMA-EXPRESS-MIB", "iliTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "iliTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "iliPing"),
        ("CODIMA-EXPRESS-MIB", "iliSrcQuench"),
        ("CODIMA-EXPRESS-MIB", "iliRedirect"),
        ("CODIMA-EXPRESS-MIB", "iliTtlExceeded"),
        ("CODIMA-EXPRESS-MIB", "iliParamProblem"),
        ("CODIMA-EXPRESS-MIB", "iliTimestamp"),
        ("CODIMA-EXPRESS-MIB", "iliFragTimeout"),
        ("CODIMA-EXPRESS-MIB", "iliNetUnreachable"),
        ("CODIMA-EXPRESS-MIB", "iliHostUnreachable"),
        ("CODIMA-EXPRESS-MIB", "iliProtocolUnreachable"),
        ("CODIMA-EXPRESS-MIB", "iliPortUnreachable"),
        ("CODIMA-EXPRESS-MIB", "iliFragRequired"),
        ("CODIMA-EXPRESS-MIB", "iliSrcRouteFail"),
        ("CODIMA-EXPRESS-MIB", "iliDestNetUnknown"),
        ("CODIMA-EXPRESS-MIB", "iliDestHostUnknown"),
        ("CODIMA-EXPRESS-MIB", "iliSrcHostIsolated"),
        ("CODIMA-EXPRESS-MIB", "iliNetProhibited"),
        ("CODIMA-EXPRESS-MIB", "iliHostProhibited"),
        ("CODIMA-EXPRESS-MIB", "iliNetTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "iliHostTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "iliPerformance"),
        ("CODIMA-EXPRESS-MIB", "iliNetRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "iliHostRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "iliAppRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "iliRouteChange"),
        ("CODIMA-EXPRESS-MIB", "iliErrors"),
        ("CODIMA-EXPRESS-MIB", "iliMaintenance"))
)
if mibBuilder.loadTexts:
    ilIcmpGroup.setStatus("current")

isBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 5, 2, 1)
)
isBaseGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "isbIpIndex"),
        ("CODIMA-EXPRESS-MIB", "isbTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "isbTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "isbFrames"),
        ("CODIMA-EXPRESS-MIB", "isbBytes"),
        ("CODIMA-EXPRESS-MIB", "isbFrameSize"),
        ("CODIMA-EXPRESS-MIB", "isbHardwareErrors"),
        ("CODIMA-EXPRESS-MIB", "isbSoftwareErrors"))
)
if mibBuilder.loadTexts:
    isBaseGroup.setStatus("current")

isDerivedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 5, 2, 2)
)
isDerivedGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "isdIpIndex"),
        ("CODIMA-EXPRESS-MIB", "isdTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "isdTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "isdUtilization"),
        ("CODIMA-EXPRESS-MIB", "isdErrorFrames"))
)
if mibBuilder.loadTexts:
    isDerivedGroup.setStatus("current")

isIcmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 5, 2, 3)
)
isIcmpGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "isiIpIndex"),
        ("CODIMA-EXPRESS-MIB", "isiTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "isiTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "isiPing"),
        ("CODIMA-EXPRESS-MIB", "isiSrcQuench"),
        ("CODIMA-EXPRESS-MIB", "isiRedirect"),
        ("CODIMA-EXPRESS-MIB", "isiTtlExceeded"),
        ("CODIMA-EXPRESS-MIB", "isiParamProblem"),
        ("CODIMA-EXPRESS-MIB", "isiTimestamp"),
        ("CODIMA-EXPRESS-MIB", "isiFragTimeout"),
        ("CODIMA-EXPRESS-MIB", "isiNetUnreachable"),
        ("CODIMA-EXPRESS-MIB", "isiHostUnreachable"),
        ("CODIMA-EXPRESS-MIB", "isiProtocolUnreachable"),
        ("CODIMA-EXPRESS-MIB", "isiPortUnreachable"),
        ("CODIMA-EXPRESS-MIB", "isiFragRequired"),
        ("CODIMA-EXPRESS-MIB", "isiSrcRouteFail"),
        ("CODIMA-EXPRESS-MIB", "isiDestNetUnknown"),
        ("CODIMA-EXPRESS-MIB", "isiDestHostUnknown"),
        ("CODIMA-EXPRESS-MIB", "isiSrcHostIsolated"),
        ("CODIMA-EXPRESS-MIB", "isiNetProhibited"),
        ("CODIMA-EXPRESS-MIB", "isiHostProhibited"),
        ("CODIMA-EXPRESS-MIB", "isiNetTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "isiHostTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "isiPerformance"),
        ("CODIMA-EXPRESS-MIB", "isiNetRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "isiHostRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "isiAppRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "isiRouteChange"),
        ("CODIMA-EXPRESS-MIB", "isiErrors"),
        ("CODIMA-EXPRESS-MIB", "isiMaintenance"))
)
if mibBuilder.loadTexts:
    isIcmpGroup.setStatus("current")

iplBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 6, 1, 1)
)
iplBaseGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "iplbIp1Index"),
        ("CODIMA-EXPRESS-MIB", "iplbIp2Index"),
        ("CODIMA-EXPRESS-MIB", "iplbTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "iplbTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "iplbFrames"),
        ("CODIMA-EXPRESS-MIB", "iplbBytes"),
        ("CODIMA-EXPRESS-MIB", "iplbFrameSize"),
        ("CODIMA-EXPRESS-MIB", "iplbHardwareErrors"),
        ("CODIMA-EXPRESS-MIB", "iplbSoftwareErrors"))
)
if mibBuilder.loadTexts:
    iplBaseGroup.setStatus("current")

iplDerivedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 6, 1, 2)
)
iplDerivedGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "ipldIp1Index"),
        ("CODIMA-EXPRESS-MIB", "ipldIp2Index"),
        ("CODIMA-EXPRESS-MIB", "ipldTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "ipldTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "ipldUtilization"),
        ("CODIMA-EXPRESS-MIB", "ipldErrorFrames"))
)
if mibBuilder.loadTexts:
    iplDerivedGroup.setStatus("current")

iplIcmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 6, 1, 3)
)
iplIcmpGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "ipliIp1Index"),
        ("CODIMA-EXPRESS-MIB", "ipliIp2Index"),
        ("CODIMA-EXPRESS-MIB", "ipliTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "ipliTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "ipliPing"),
        ("CODIMA-EXPRESS-MIB", "ipliSrcQuench"),
        ("CODIMA-EXPRESS-MIB", "ipliRedirect"),
        ("CODIMA-EXPRESS-MIB", "ipliTtlExceeded"),
        ("CODIMA-EXPRESS-MIB", "ipliParamProblem"),
        ("CODIMA-EXPRESS-MIB", "ipliTimestamp"),
        ("CODIMA-EXPRESS-MIB", "ipliFragTimeout"),
        ("CODIMA-EXPRESS-MIB", "ipliNetUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ipliHostUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ipliProtocolUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ipliPortUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ipliFragRequired"),
        ("CODIMA-EXPRESS-MIB", "ipliSrcRouteFail"),
        ("CODIMA-EXPRESS-MIB", "ipliDestNetUnknown"),
        ("CODIMA-EXPRESS-MIB", "ipliDestHostUnknown"),
        ("CODIMA-EXPRESS-MIB", "ipliSrcHostIsolated"),
        ("CODIMA-EXPRESS-MIB", "ipliNetProhibited"),
        ("CODIMA-EXPRESS-MIB", "ipliHostProhibited"),
        ("CODIMA-EXPRESS-MIB", "ipliNetTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ipliHostTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ipliPerformance"),
        ("CODIMA-EXPRESS-MIB", "ipliNetRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "ipliHostRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "ipliAppRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "ipliRouteChange"),
        ("CODIMA-EXPRESS-MIB", "ipliErrors"),
        ("CODIMA-EXPRESS-MIB", "ipliMaintenance"))
)
if mibBuilder.loadTexts:
    iplIcmpGroup.setStatus("current")

ipsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 6, 2, 1)
)
ipsBaseGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "ipsbIp1Index"),
        ("CODIMA-EXPRESS-MIB", "ipsbIp2Index"),
        ("CODIMA-EXPRESS-MIB", "ipsbTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "ipsbTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "ipsbFrames"),
        ("CODIMA-EXPRESS-MIB", "ipsbBytes"),
        ("CODIMA-EXPRESS-MIB", "ipsbFrameSize"),
        ("CODIMA-EXPRESS-MIB", "ipsbHardwareErrors"),
        ("CODIMA-EXPRESS-MIB", "ipsbSoftwareErrors"))
)
if mibBuilder.loadTexts:
    ipsBaseGroup.setStatus("current")

ipsDerivedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 6, 2, 2)
)
ipsDerivedGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "ipsdIp1Index"),
        ("CODIMA-EXPRESS-MIB", "ipsdIp2Index"),
        ("CODIMA-EXPRESS-MIB", "ipsdTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "ipsdTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "ipsdUtilization"),
        ("CODIMA-EXPRESS-MIB", "ipsdErrorFrames"))
)
if mibBuilder.loadTexts:
    ipsDerivedGroup.setStatus("current")

ipsIcmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 6, 2, 3)
)
ipsIcmpGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "ipsiIp1Index"),
        ("CODIMA-EXPRESS-MIB", "ipsiIp2Index"),
        ("CODIMA-EXPRESS-MIB", "ipsiTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "ipsiTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "ipsiPing"),
        ("CODIMA-EXPRESS-MIB", "ipsiSrcQuench"),
        ("CODIMA-EXPRESS-MIB", "ipsiRedirect"),
        ("CODIMA-EXPRESS-MIB", "ipsiTtlExceeded"),
        ("CODIMA-EXPRESS-MIB", "ipsiParamProblem"),
        ("CODIMA-EXPRESS-MIB", "ipsiTimestamp"),
        ("CODIMA-EXPRESS-MIB", "ipsiFragTimeout"),
        ("CODIMA-EXPRESS-MIB", "ipsiNetUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ipsiHostUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ipsiProtocolUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ipsiPortUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ipsiFragRequired"),
        ("CODIMA-EXPRESS-MIB", "ipsiSrcRouteFail"),
        ("CODIMA-EXPRESS-MIB", "ipsiDestNetUnknown"),
        ("CODIMA-EXPRESS-MIB", "ipsiDestHostUnknown"),
        ("CODIMA-EXPRESS-MIB", "ipsiSrcHostIsolated"),
        ("CODIMA-EXPRESS-MIB", "ipsiNetProhibited"),
        ("CODIMA-EXPRESS-MIB", "ipsiHostProhibited"),
        ("CODIMA-EXPRESS-MIB", "ipsiNetTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ipsiHostTosUnreachable"),
        ("CODIMA-EXPRESS-MIB", "ipsiPerformance"),
        ("CODIMA-EXPRESS-MIB", "ipsiNetRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "ipsiHostRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "ipsiAppRouteProblem"),
        ("CODIMA-EXPRESS-MIB", "ipsiRouteChange"),
        ("CODIMA-EXPRESS-MIB", "ipsiErrors"),
        ("CODIMA-EXPRESS-MIB", "ipsiMaintenance"))
)
if mibBuilder.loadTexts:
    ipsIcmpGroup.setStatus("current")

plBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 7, 1, 1)
)
plBaseGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "plbLayerIndex"),
        ("CODIMA-EXPRESS-MIB", "plbIdIndex"),
        ("CODIMA-EXPRESS-MIB", "plbTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "plbTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "plbProtocolName"),
        ("CODIMA-EXPRESS-MIB", "plbFrames"),
        ("CODIMA-EXPRESS-MIB", "plbBytes"),
        ("CODIMA-EXPRESS-MIB", "plbFrameSize"),
        ("CODIMA-EXPRESS-MIB", "plbHardwareErrors"),
        ("CODIMA-EXPRESS-MIB", "plbSoftwareErrors"))
)
if mibBuilder.loadTexts:
    plBaseGroup.setStatus("current")

plDerivedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 7, 1, 2)
)
plDerivedGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "pldLayerIndex"),
        ("CODIMA-EXPRESS-MIB", "pldIdIndex"),
        ("CODIMA-EXPRESS-MIB", "pldTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "pldTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "pldProtocolName"),
        ("CODIMA-EXPRESS-MIB", "pldUtilization"),
        ("CODIMA-EXPRESS-MIB", "pldErrorFrames"))
)
if mibBuilder.loadTexts:
    plDerivedGroup.setStatus("current")

psBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 7, 2, 1)
)
psBaseGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "psbLayerIndex"),
        ("CODIMA-EXPRESS-MIB", "psbIdIndex"),
        ("CODIMA-EXPRESS-MIB", "psbTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "psbTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "psbProtocolName"),
        ("CODIMA-EXPRESS-MIB", "psbFrames"),
        ("CODIMA-EXPRESS-MIB", "psbBytes"),
        ("CODIMA-EXPRESS-MIB", "psbFrameSize"),
        ("CODIMA-EXPRESS-MIB", "psbHardwareErrors"),
        ("CODIMA-EXPRESS-MIB", "psbSoftwareErrors"))
)
if mibBuilder.loadTexts:
    psBaseGroup.setStatus("current")

psDerivedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 7, 2, 2)
)
psDerivedGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "psdLayerIndex"),
        ("CODIMA-EXPRESS-MIB", "psdIdIndex"),
        ("CODIMA-EXPRESS-MIB", "psdTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "psdTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "psdProtocolName"),
        ("CODIMA-EXPRESS-MIB", "psdUtilization"),
        ("CODIMA-EXPRESS-MIB", "psdErrorFrames"))
)
if mibBuilder.loadTexts:
    psDerivedGroup.setStatus("current")

netChannelLongTermGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 8, 1)
)
netChannelLongTermGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "nlTypeIndex"),
        ("CODIMA-EXPRESS-MIB", "nlNameIndex"),
        ("CODIMA-EXPRESS-MIB", "nlTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "nlTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "nlFrames"),
        ("CODIMA-EXPRESS-MIB", "nlBytes"),
        ("CODIMA-EXPRESS-MIB", "nlFrameSize"),
        ("CODIMA-EXPRESS-MIB", "nlHardErrors"),
        ("CODIMA-EXPRESS-MIB", "nlSoftErrors"),
        ("CODIMA-EXPRESS-MIB", "nlUtilization"),
        ("CODIMA-EXPRESS-MIB", "nlHardErrorsPercent"),
        ("CODIMA-EXPRESS-MIB", "nlSoftErrorsPercent"),
        ("CODIMA-EXPRESS-MIB", "nlFramesPercent"),
        ("CODIMA-EXPRESS-MIB", "nlBytesPercent"))
)
if mibBuilder.loadTexts:
    netChannelLongTermGroup.setStatus("current")

netChannelShortTermGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 8, 2)
)
netChannelShortTermGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "nsTypeIndex"),
        ("CODIMA-EXPRESS-MIB", "nsNameIndex"),
        ("CODIMA-EXPRESS-MIB", "nsTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "nsTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "nsFrames"),
        ("CODIMA-EXPRESS-MIB", "nsBytes"),
        ("CODIMA-EXPRESS-MIB", "nsFrameSize"),
        ("CODIMA-EXPRESS-MIB", "nsHardErrors"),
        ("CODIMA-EXPRESS-MIB", "nsSoftErrors"),
        ("CODIMA-EXPRESS-MIB", "nsUtilization"),
        ("CODIMA-EXPRESS-MIB", "nsHardErrorsPercent"),
        ("CODIMA-EXPRESS-MIB", "nsSoftErrorsPercent"),
        ("CODIMA-EXPRESS-MIB", "nsFramesPercent"),
        ("CODIMA-EXPRESS-MIB", "nsBytesPercent"))
)
if mibBuilder.loadTexts:
    netChannelShortTermGroup.setStatus("current")

vlanLongTermGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 9, 1)
)
vlanLongTermGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "vlIdIndex"),
        ("CODIMA-EXPRESS-MIB", "vlTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "vlTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "vlName"),
        ("CODIMA-EXPRESS-MIB", "vlFrames"),
        ("CODIMA-EXPRESS-MIB", "vlBytes"),
        ("CODIMA-EXPRESS-MIB", "vlFrameSize"),
        ("CODIMA-EXPRESS-MIB", "vlHardErrors"),
        ("CODIMA-EXPRESS-MIB", "vlSoftErrors"),
        ("CODIMA-EXPRESS-MIB", "vlUtilization"),
        ("CODIMA-EXPRESS-MIB", "vlHardErrorsPercent"),
        ("CODIMA-EXPRESS-MIB", "vlSoftErrorsPercent"),
        ("CODIMA-EXPRESS-MIB", "vlFramesPercent"),
        ("CODIMA-EXPRESS-MIB", "vlBytesPercent"))
)
if mibBuilder.loadTexts:
    vlanLongTermGroup.setStatus("current")

vlanShortTermGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 1, 9, 2)
)
vlanShortTermGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "vsIdIndex"),
        ("CODIMA-EXPRESS-MIB", "vsTimeStampIndex"),
        ("CODIMA-EXPRESS-MIB", "vsTimeStamp"),
        ("CODIMA-EXPRESS-MIB", "vsName"),
        ("CODIMA-EXPRESS-MIB", "vsFrames"),
        ("CODIMA-EXPRESS-MIB", "vsBytes"),
        ("CODIMA-EXPRESS-MIB", "vsFrameSize"),
        ("CODIMA-EXPRESS-MIB", "vsHardErrors"),
        ("CODIMA-EXPRESS-MIB", "vsSoftErrors"),
        ("CODIMA-EXPRESS-MIB", "vsUtilization"),
        ("CODIMA-EXPRESS-MIB", "vsHardErrorsPercent"),
        ("CODIMA-EXPRESS-MIB", "vsSoftErrorsPercent"),
        ("CODIMA-EXPRESS-MIB", "vsFramesPercent"),
        ("CODIMA-EXPRESS-MIB", "vsBytesPercent"))
)
if mibBuilder.loadTexts:
    vlanShortTermGroup.setStatus("current")

alarmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 1, 2)
)
alarmObjectGroup.setObjects(
      *(("CODIMA-EXPRESS-MIB", "alarmMessage"),
        ("CODIMA-EXPRESS-MIB", "alarmTime"),
        ("CODIMA-EXPRESS-MIB", "alarmClass"),
        ("CODIMA-EXPRESS-MIB", "alarmUnitType"),
        ("CODIMA-EXPRESS-MIB", "alarmGroup"),
        ("CODIMA-EXPRESS-MIB", "alarmFunction"),
        ("CODIMA-EXPRESS-MIB", "alarmCode"),
        ("CODIMA-EXPRESS-MIB", "alarmLayer"),
        ("CODIMA-EXPRESS-MIB", "alarmBaseProtocol"),
        ("CODIMA-EXPRESS-MIB", "alarmTopProtocol"))
)
if mibBuilder.loadTexts:
    alarmObjectGroup.setStatus("current")


# Notification objects

expressAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 2, 1, 1)
)
expressAlarm.setObjects(
      *(("CODIMA-EXPRESS-MIB", "alarmMessage"),
        ("CODIMA-EXPRESS-MIB", "alarmLayer"),
        ("CODIMA-EXPRESS-MIB", "alarmTopProtocol"),
        ("CODIMA-EXPRESS-MIB", "alarmBaseProtocol"),
        ("CODIMA-EXPRESS-MIB", "alarmCode"),
        ("CODIMA-EXPRESS-MIB", "alarmFunction"),
        ("CODIMA-EXPRESS-MIB", "alarmGroup"),
        ("CODIMA-EXPRESS-MIB", "alarmUnitType"),
        ("CODIMA-EXPRESS-MIB", "alarmClass"),
        ("CODIMA-EXPRESS-MIB", "alarmTime"))
)
if mibBuilder.loadTexts:
    expressAlarm.setStatus(
        "current"
    )


# Notifications groups

alarmNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 226, 3, 2, 3, 2, 1)
)
alarmNotifyGroup.setObjects(
    ("CODIMA-EXPRESS-MIB", "expressAlarm")
)
if mibBuilder.loadTexts:
    alarmNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CODIMA-EXPRESS-MIB",
    **{"codimaExpressMIB": codimaExpressMIB,
       "codimaExpressObjects": codimaExpressObjects,
       "expHistoryDatabases": expHistoryDatabases,
       "dbControl": dbControl,
       "ctrlTimeTable": ctrlTimeTable,
       "ctrlTimeEntry": ctrlTimeEntry,
       "ctSampleType": ctSampleType,
       "ctTimeSlots": ctTimeSlots,
       "ctLockMethod": ctLockMethod,
       "ctLockUserTime": ctLockUserTime,
       "ctLockRealTime": ctLockRealTime,
       "dbSegment": dbSegment,
       "segLongTerm": segLongTerm,
       "slBaseTable": slBaseTable,
       "slBaseEntry": slBaseEntry,
       "slbTimeStampIndex": slbTimeStampIndex,
       "slbTimeStamp": slbTimeStamp,
       "slbFrames": slbFrames,
       "slbBytes": slbBytes,
       "slbFrameSize": slbFrameSize,
       "slbHardwareErrors": slbHardwareErrors,
       "slbSoftwareErrors": slbSoftwareErrors,
       "slbActiveNodes": slbActiveNodes,
       "slBroadcastTable": slBroadcastTable,
       "slBroadcastEntry": slBroadcastEntry,
       "slbcTimeStampIndex": slbcTimeStampIndex,
       "slbcTimeStamp": slbcTimeStamp,
       "slbcBytes": slbcBytes,
       "slbcPercentBytes": slbcPercentBytes,
       "slbcFrames": slbcFrames,
       "slbcPercentFrames": slbcPercentFrames,
       "slDerivedTable": slDerivedTable,
       "slDerivedEntry": slDerivedEntry,
       "sldTimeStampIndex": sldTimeStampIndex,
       "sldTimeStamp": sldTimeStamp,
       "sldUtilization": sldUtilization,
       "sldErrorFrames": sldErrorFrames,
       "slEthernetTable": slEthernetTable,
       "slEthernetEntry": slEthernetEntry,
       "sleTimeStampIndex": sleTimeStampIndex,
       "sleTimeStamp": sleTimeStamp,
       "sleRunts": sleRunts,
       "sleJabbers": sleJabbers,
       "sleCrc": sleCrc,
       "sleCollisions": sleCollisions,
       "sleLateCollisions": sleLateCollisions,
       "slIcmpTable": slIcmpTable,
       "slIcmpEntry": slIcmpEntry,
       "sliTimeStampIndex": sliTimeStampIndex,
       "sliTimeStamp": sliTimeStamp,
       "sliPing": sliPing,
       "sliSrcQuench": sliSrcQuench,
       "sliRedirect": sliRedirect,
       "sliTtlExceeded": sliTtlExceeded,
       "sliParamProblem": sliParamProblem,
       "sliTimestamp": sliTimestamp,
       "sliFragTimeout": sliFragTimeout,
       "sliNetUnreachable": sliNetUnreachable,
       "sliHostUnreachable": sliHostUnreachable,
       "sliProtocolUnreachable": sliProtocolUnreachable,
       "sliPortUnreachable": sliPortUnreachable,
       "sliFragRequired": sliFragRequired,
       "sliSrcRouteFail": sliSrcRouteFail,
       "sliDestNetUnknown": sliDestNetUnknown,
       "sliDestHostUnknown": sliDestHostUnknown,
       "sliSrcHostIsolated": sliSrcHostIsolated,
       "sliNetProhibited": sliNetProhibited,
       "sliHostProhibited": sliHostProhibited,
       "sliNetTosUnreachable": sliNetTosUnreachable,
       "sliHostTosUnreachable": sliHostTosUnreachable,
       "sliPerformance": sliPerformance,
       "sliNetRouteProblem": sliNetRouteProblem,
       "sliHostRouteProblem": sliHostRouteProblem,
       "sliAppRouteProblem": sliAppRouteProblem,
       "sliRouteChange": sliRouteChange,
       "sliGrpErrors": sliGrpErrors,
       "sliMaintenance": sliMaintenance,
       "slPortTable": slPortTable,
       "slPortEntry": slPortEntry,
       "slp1TimeStampIndex": slp1TimeStampIndex,
       "slp1TimeStamp": slp1TimeStamp,
       "slp1Frames": slp1Frames,
       "slp1Bytes": slp1Bytes,
       "slp1FrameSize": slp1FrameSize,
       "slp1Utilization": slp1Utilization,
       "slp1LineSpeed": slp1LineSpeed,
       "slp1SoftErrors": slp1SoftErrors,
       "slp1Runts": slp1Runts,
       "slp1Jabbers": slp1Jabbers,
       "slp1Crc": slp1Crc,
       "slp1Collisions": slp1Collisions,
       "slp1LateCollisions": slp1LateCollisions,
       "slp1LineNoise": slp1LineNoise,
       "slp2Frames": slp2Frames,
       "slp2Bytes": slp2Bytes,
       "slp2FrameSize": slp2FrameSize,
       "slp2Utilization": slp2Utilization,
       "slp2LineSpeed": slp2LineSpeed,
       "slp2SoftErrors": slp2SoftErrors,
       "slp2Runts": slp2Runts,
       "slp2Jabbers": slp2Jabbers,
       "slp2Crc": slp2Crc,
       "slp2Collisions": slp2Collisions,
       "slp2LateCollisions": slp2LateCollisions,
       "slp2LineNoise": slp2LineNoise,
       "segShortTerm": segShortTerm,
       "ssBaseTable": ssBaseTable,
       "ssBaseEntry": ssBaseEntry,
       "ssbTimeStampIndex": ssbTimeStampIndex,
       "ssbTimeStamp": ssbTimeStamp,
       "ssbFrames": ssbFrames,
       "ssbBytes": ssbBytes,
       "ssbFrameSize": ssbFrameSize,
       "ssbHardwareErrors": ssbHardwareErrors,
       "ssbSoftwareErrors": ssbSoftwareErrors,
       "ssbActiveNodes": ssbActiveNodes,
       "ssBroadcastTable": ssBroadcastTable,
       "ssBroadcastEntry": ssBroadcastEntry,
       "ssbcTimeStampIndex": ssbcTimeStampIndex,
       "ssbcTimeStamp": ssbcTimeStamp,
       "ssbcBytes": ssbcBytes,
       "ssbcBytesPercent": ssbcBytesPercent,
       "ssbcFrames": ssbcFrames,
       "ssbcFramesPercent": ssbcFramesPercent,
       "ssDerivedTable": ssDerivedTable,
       "ssDerivedEntry": ssDerivedEntry,
       "ssdTimeStampIndex": ssdTimeStampIndex,
       "ssdTimeStamp": ssdTimeStamp,
       "ssdUtilization": ssdUtilization,
       "ssdErrorFrames": ssdErrorFrames,
       "ssEthernetTable": ssEthernetTable,
       "ssEthernetEntry": ssEthernetEntry,
       "sseTimeStampIndex": sseTimeStampIndex,
       "sseTimeStamp": sseTimeStamp,
       "sseRunts": sseRunts,
       "sseJabbers": sseJabbers,
       "sseCrc": sseCrc,
       "sseCollisions": sseCollisions,
       "sseLateCollisions": sseLateCollisions,
       "ssIcmpTable": ssIcmpTable,
       "ssIcmpEntry": ssIcmpEntry,
       "ssiTimeStampIndex": ssiTimeStampIndex,
       "ssiTimeStamp": ssiTimeStamp,
       "ssiPing": ssiPing,
       "ssiSrcQuench": ssiSrcQuench,
       "ssiRedirect": ssiRedirect,
       "ssiTtlExceeded": ssiTtlExceeded,
       "ssiParamProblem": ssiParamProblem,
       "ssiTimestamp": ssiTimestamp,
       "ssiFragTimeout": ssiFragTimeout,
       "ssiNetUnreachable": ssiNetUnreachable,
       "ssiHostUnreachable": ssiHostUnreachable,
       "ssiProtocolUnreachable": ssiProtocolUnreachable,
       "ssiPortUnreachable": ssiPortUnreachable,
       "ssiFragRequired": ssiFragRequired,
       "ssiSrcRouteFail": ssiSrcRouteFail,
       "ssiDestNetUnknown": ssiDestNetUnknown,
       "ssiDestHostUnknown": ssiDestHostUnknown,
       "ssiSrcHostIsolated": ssiSrcHostIsolated,
       "ssiNetProhibited": ssiNetProhibited,
       "ssiHostProhibited": ssiHostProhibited,
       "ssiNetTosUnreachable": ssiNetTosUnreachable,
       "ssiHostTosUnreachable": ssiHostTosUnreachable,
       "ssiPerformance": ssiPerformance,
       "ssiNetRouteProblem": ssiNetRouteProblem,
       "ssiHostRouteProblem": ssiHostRouteProblem,
       "ssiAppRouteProblem": ssiAppRouteProblem,
       "ssiRouteChange": ssiRouteChange,
       "ssiErrors": ssiErrors,
       "ssiMaintenance": ssiMaintenance,
       "ssPortTable": ssPortTable,
       "ssPortEntry": ssPortEntry,
       "sspTimeStampIndex": sspTimeStampIndex,
       "sspTimeStamp": sspTimeStamp,
       "ssp1Frames": ssp1Frames,
       "ssp1Bytes": ssp1Bytes,
       "ssp1FrameSize": ssp1FrameSize,
       "ssp1Utilization": ssp1Utilization,
       "ssp1LineSpeed": ssp1LineSpeed,
       "ssp1SoftErrors": ssp1SoftErrors,
       "ssp1Runts": ssp1Runts,
       "ssp1Jabbers": ssp1Jabbers,
       "ssp1Crc": ssp1Crc,
       "ssp1Collisions": ssp1Collisions,
       "ssp1LateCollisions": ssp1LateCollisions,
       "ssp1LineNoise": ssp1LineNoise,
       "ssp2Frames": ssp2Frames,
       "ssp2Bytes": ssp2Bytes,
       "ssp2FrameSize": ssp2FrameSize,
       "ssp2Utilization": ssp2Utilization,
       "ssp2LineSpeed": ssp2LineSpeed,
       "ssp2SoftErrors": ssp2SoftErrors,
       "ssp2Runts": ssp2Runts,
       "ssp2Jabbers": ssp2Jabbers,
       "ssp2Crc": ssp2Crc,
       "ssp2Collisions": ssp2Collisions,
       "ssp2LateCollisions": ssp2LateCollisions,
       "ssp2LineNoise": ssp2LineNoise,
       "dbMac": dbMac,
       "macLongTerm": macLongTerm,
       "mlBaseTable": mlBaseTable,
       "mlBaseEntry": mlBaseEntry,
       "mlbMacIndex": mlbMacIndex,
       "mlbTimeStampIndex": mlbTimeStampIndex,
       "mlbTimeStamp": mlbTimeStamp,
       "mlbFrames": mlbFrames,
       "mlbBytes": mlbBytes,
       "mlbFrameSize": mlbFrameSize,
       "mlbHardwareErrors": mlbHardwareErrors,
       "mlbSoftwareErrors": mlbSoftwareErrors,
       "mlDerivedTable": mlDerivedTable,
       "mlDerivedEntry": mlDerivedEntry,
       "mldMacIndex": mldMacIndex,
       "mldTimeStampIndex": mldTimeStampIndex,
       "mldTimeStamp": mldTimeStamp,
       "mldUtilization": mldUtilization,
       "mldErrorFrames": mldErrorFrames,
       "mlDuplexTable": mlDuplexTable,
       "mlDuplexEntry": mlDuplexEntry,
       "mlduMacIndex": mlduMacIndex,
       "mlduTimeStampIndex": mlduTimeStampIndex,
       "mlduTimeStamp": mlduTimeStamp,
       "mlduTxFrames": mlduTxFrames,
       "mlduTxBytes": mlduTxBytes,
       "mlduTxFrameSize": mlduTxFrameSize,
       "mlduTxUtilization": mlduTxUtilization,
       "mlduRxFrames": mlduRxFrames,
       "mlduRxBytes": mlduRxBytes,
       "mlduRxFrameSize": mlduRxFrameSize,
       "mlduRxUtilization": mlduRxUtilization,
       "mlEthernetTable": mlEthernetTable,
       "mlEthernetEntry": mlEthernetEntry,
       "mleMacIndex": mleMacIndex,
       "mleTimeStampIndex": mleTimeStampIndex,
       "mleTimeStamp": mleTimeStamp,
       "mleRunts": mleRunts,
       "mleJabbers": mleJabbers,
       "mleCrc": mleCrc,
       "mleCollisions": mleCollisions,
       "mleLateCollisions": mleLateCollisions,
       "mlIcmpTable": mlIcmpTable,
       "mlIcmpEntry": mlIcmpEntry,
       "mliMacIndex": mliMacIndex,
       "mliTimeStampIndex": mliTimeStampIndex,
       "mliTimeStamp": mliTimeStamp,
       "mliPing": mliPing,
       "mliSrcQuench": mliSrcQuench,
       "mliRedirect": mliRedirect,
       "mliTtlExceeded": mliTtlExceeded,
       "mliParamProblem": mliParamProblem,
       "mliTimestamp": mliTimestamp,
       "mliFragTimeout": mliFragTimeout,
       "mliNetUnreachable": mliNetUnreachable,
       "mliHostUnreachable": mliHostUnreachable,
       "mliProtocolUnreachable": mliProtocolUnreachable,
       "mliPortUnreachable": mliPortUnreachable,
       "mliFragRequired": mliFragRequired,
       "mliSrcRouteFail": mliSrcRouteFail,
       "mliDestNetUnknown": mliDestNetUnknown,
       "mliDestHostUnknown": mliDestHostUnknown,
       "mliSrcHostIsolated": mliSrcHostIsolated,
       "mliNetProhibited": mliNetProhibited,
       "mliHostProhibited": mliHostProhibited,
       "mliNetTosUnreachable": mliNetTosUnreachable,
       "mliHostTosUnreachable": mliHostTosUnreachable,
       "mliPerformance": mliPerformance,
       "mliNetRouteProblem": mliNetRouteProblem,
       "mliHostRouteProblem": mliHostRouteProblem,
       "mliAppRouteProblem": mliAppRouteProblem,
       "mliRouteChange": mliRouteChange,
       "mliErrors": mliErrors,
       "mliMaintenance": mliMaintenance,
       "mlProtocolTable": mlProtocolTable,
       "mlProtocolEntry": mlProtocolEntry,
       "mlpMacIndex": mlpMacIndex,
       "mlpTimeStampIndex": mlpTimeStampIndex,
       "mlpTimeStamp": mlpTimeStamp,
       "mlpNovell": mlpNovell,
       "mlpSnmp": mlpSnmp,
       "mlpRouting": mlpRouting,
       "mlpWww": mlpWww,
       "mlpIcmp": mlpIcmp,
       "mlpIso": mlpIso,
       "mlpMail": mlpMail,
       "mlpNetbios": mlpNetbios,
       "mlpDns": mlpDns,
       "mlpIp": mlpIp,
       "mlpVoip": mlpVoip,
       "mlpLayer3Traffic": mlpLayer3Traffic,
       "mlpIpData": mlpIpData,
       "mlpApplications": mlpApplications,
       "mlpIpControl": mlpIpControl,
       "mlpManagement": mlpManagement,
       "macShortTerm": macShortTerm,
       "msBaseTable": msBaseTable,
       "msBaseEntry": msBaseEntry,
       "msbMacIndex": msbMacIndex,
       "msbTimeStampIndex": msbTimeStampIndex,
       "msbTimeStamp": msbTimeStamp,
       "msbFrames": msbFrames,
       "msbBytes": msbBytes,
       "msbFrameSize": msbFrameSize,
       "msbHardwareErrors": msbHardwareErrors,
       "msbSoftwareErrors": msbSoftwareErrors,
       "msDerivedTable": msDerivedTable,
       "msDerivedEntry": msDerivedEntry,
       "msdMacIndex": msdMacIndex,
       "msdTimeStampIndex": msdTimeStampIndex,
       "msdTimeStamp": msdTimeStamp,
       "msdUtilization": msdUtilization,
       "msdErrorFrames": msdErrorFrames,
       "msDuplexTable": msDuplexTable,
       "msDuplexEntry": msDuplexEntry,
       "msdpMacIndex": msdpMacIndex,
       "msdpTimeStampIndex": msdpTimeStampIndex,
       "msdpTimeStamp": msdpTimeStamp,
       "msdpTxFrames": msdpTxFrames,
       "msdpTxBytes": msdpTxBytes,
       "msdpTxFrameSize": msdpTxFrameSize,
       "msdpTxUtilization": msdpTxUtilization,
       "msdpRxFrames": msdpRxFrames,
       "msdpRxBytes": msdpRxBytes,
       "msdpRxFrameSize": msdpRxFrameSize,
       "msdpRxUtilization": msdpRxUtilization,
       "msEthernetTable": msEthernetTable,
       "msEthernetEntry": msEthernetEntry,
       "mseMacIndex": mseMacIndex,
       "mseTimeStampIndex": mseTimeStampIndex,
       "mseTimeStamp": mseTimeStamp,
       "mseRunts": mseRunts,
       "mseJabbers": mseJabbers,
       "mseCrc": mseCrc,
       "mseCollisions": mseCollisions,
       "mseLateCollisions": mseLateCollisions,
       "msIcmpTable": msIcmpTable,
       "msIcmpEntry": msIcmpEntry,
       "msiMacIndex": msiMacIndex,
       "msiTimeStampIndex": msiTimeStampIndex,
       "msiTimeStamp": msiTimeStamp,
       "msiPing": msiPing,
       "msiSrcQuench": msiSrcQuench,
       "msiRedirect": msiRedirect,
       "msiTtlExceeded": msiTtlExceeded,
       "msiParamProblem": msiParamProblem,
       "msiTimestamp": msiTimestamp,
       "msiFragTimeout": msiFragTimeout,
       "msiNetUnreachable": msiNetUnreachable,
       "msiHostUnreachable": msiHostUnreachable,
       "msiProtocolUnreachable": msiProtocolUnreachable,
       "msiPortUnreachable": msiPortUnreachable,
       "msiFragRequired": msiFragRequired,
       "msiSrcRouteFail": msiSrcRouteFail,
       "msiDestNetUnknown": msiDestNetUnknown,
       "msiDestHostUnknown": msiDestHostUnknown,
       "msiSrcHostIsolated": msiSrcHostIsolated,
       "msiNetProhibited": msiNetProhibited,
       "msiHostProhibited": msiHostProhibited,
       "msiNetTosUnreachable": msiNetTosUnreachable,
       "msiHostTosUnreachable": msiHostTosUnreachable,
       "msiPerformance": msiPerformance,
       "msiNetRouteProblem": msiNetRouteProblem,
       "msiHostRouteProblem": msiHostRouteProblem,
       "msiAppRouteProblem": msiAppRouteProblem,
       "msiRouteChange": msiRouteChange,
       "msiErrors": msiErrors,
       "msiMaintenance": msiMaintenance,
       "msProtocolTable": msProtocolTable,
       "msProtocolEntry": msProtocolEntry,
       "mspMacIndex": mspMacIndex,
       "mspTimeStampIndex": mspTimeStampIndex,
       "mspTimeStamp": mspTimeStamp,
       "mspNovell": mspNovell,
       "mspSnmp": mspSnmp,
       "mspRouting": mspRouting,
       "mspWww": mspWww,
       "mspIcmp": mspIcmp,
       "mspIso": mspIso,
       "mspMail": mspMail,
       "mspNetbios": mspNetbios,
       "mspDns": mspDns,
       "mspIp": mspIp,
       "mspVoip": mspVoip,
       "mspLayer3Traffic": mspLayer3Traffic,
       "mspIpData": mspIpData,
       "mspApplications": mspApplications,
       "mspIpControl": mspIpControl,
       "mspManagement": mspManagement,
       "dbMacPeer": dbMacPeer,
       "macPeerLongTerm": macPeerLongTerm,
       "mplBaseTable": mplBaseTable,
       "mplBaseEntry": mplBaseEntry,
       "mplbMac1Index": mplbMac1Index,
       "mplbMac2Index": mplbMac2Index,
       "mplbTimeStampIndex": mplbTimeStampIndex,
       "mplbTimeStamp": mplbTimeStamp,
       "mplbFrames": mplbFrames,
       "mplbBytes": mplbBytes,
       "mplbFrameSize": mplbFrameSize,
       "mplbHardwareErrors": mplbHardwareErrors,
       "mplbSoftwareErrors": mplbSoftwareErrors,
       "mplDerivedTable": mplDerivedTable,
       "mplDerivedEntry": mplDerivedEntry,
       "mpldMac1Index": mpldMac1Index,
       "mpldMac2Index": mpldMac2Index,
       "mpldTimeStampIndex": mpldTimeStampIndex,
       "mpldTimeStamp": mpldTimeStamp,
       "mpldUtilization": mpldUtilization,
       "mpldErrorFrames": mpldErrorFrames,
       "mplDuplexTable": mplDuplexTable,
       "mplDuplexEntry": mplDuplexEntry,
       "mplduMac1Index": mplduMac1Index,
       "mplduMac2Index": mplduMac2Index,
       "mplduTimeStampIndex": mplduTimeStampIndex,
       "mplduTimeStamp": mplduTimeStamp,
       "mplduTxFrames": mplduTxFrames,
       "mplduTxBytes": mplduTxBytes,
       "mplduTxFrameSize": mplduTxFrameSize,
       "mplduTxUtilization": mplduTxUtilization,
       "mplduRxFrames": mplduRxFrames,
       "mplduRxBytes": mplduRxBytes,
       "mplduRxFrameSize": mplduRxFrameSize,
       "mplduRxUtilization": mplduRxUtilization,
       "mplProtocolTable": mplProtocolTable,
       "mplProtocolEntry": mplProtocolEntry,
       "mplpMac1Index": mplpMac1Index,
       "mplpMac2Index": mplpMac2Index,
       "mplpTimeStampIndex": mplpTimeStampIndex,
       "mplpTimeStamp": mplpTimeStamp,
       "mplpNovell": mplpNovell,
       "mplpSnmp": mplpSnmp,
       "mplpRouting": mplpRouting,
       "mplpWww": mplpWww,
       "mplpIcmp": mplpIcmp,
       "mplpIso": mplpIso,
       "mplpMail": mplpMail,
       "mplpNetbios": mplpNetbios,
       "mplpDns": mplpDns,
       "mplpIp": mplpIp,
       "mplpVoip": mplpVoip,
       "mplpLayer3Traffic": mplpLayer3Traffic,
       "mplpIpData": mplpIpData,
       "mplpApplications": mplpApplications,
       "mplpIpControl": mplpIpControl,
       "mplpManagement": mplpManagement,
       "macPeerShortTerm": macPeerShortTerm,
       "mpsBaseTable": mpsBaseTable,
       "mpsBaseEntry": mpsBaseEntry,
       "mpsbMac1Index": mpsbMac1Index,
       "mpsbMac2Index": mpsbMac2Index,
       "mpsbTimeStampIndex": mpsbTimeStampIndex,
       "mpsbTimeStamp": mpsbTimeStamp,
       "mpsbFrames": mpsbFrames,
       "mpsbBytes": mpsbBytes,
       "mpsbFrameSize": mpsbFrameSize,
       "mpsbHardwareErrors": mpsbHardwareErrors,
       "mpsbSoftwareErrors": mpsbSoftwareErrors,
       "mpsDerivedTable": mpsDerivedTable,
       "mpsDerivedEntry": mpsDerivedEntry,
       "mpsdMac1Index": mpsdMac1Index,
       "mpsdMac2Index": mpsdMac2Index,
       "mpsdTimeStampIndex": mpsdTimeStampIndex,
       "mpsdTimeStamp": mpsdTimeStamp,
       "mpsdUtilization": mpsdUtilization,
       "mpsdErrorFrames": mpsdErrorFrames,
       "mpsDuplexTable": mpsDuplexTable,
       "mpsDuplexEntry": mpsDuplexEntry,
       "mpsduMac1Index": mpsduMac1Index,
       "mpsduMac2Index": mpsduMac2Index,
       "mpsduTimeStampIndex": mpsduTimeStampIndex,
       "mpsduTimeStamp": mpsduTimeStamp,
       "mpsduTxFrames": mpsduTxFrames,
       "mpsduTxBytes": mpsduTxBytes,
       "mpsduTxFrameSize": mpsduTxFrameSize,
       "mpsduTxUtilization": mpsduTxUtilization,
       "mpsduRxFrames": mpsduRxFrames,
       "mpsduRxBytes": mpsduRxBytes,
       "mpsduRxFrameSize": mpsduRxFrameSize,
       "mpsduRxUtilization": mpsduRxUtilization,
       "mpsProtocolTable": mpsProtocolTable,
       "mpsProtocolEntry": mpsProtocolEntry,
       "mpspMac1Index": mpspMac1Index,
       "mpspMac2Index": mpspMac2Index,
       "mpspTimeStampIndex": mpspTimeStampIndex,
       "mpspTimeStamp": mpspTimeStamp,
       "mpspNovell": mpspNovell,
       "mpspSnmp": mpspSnmp,
       "mpspRouting": mpspRouting,
       "mpspWww": mpspWww,
       "mpspIcmp": mpspIcmp,
       "mpspIso": mpspIso,
       "mpspMail": mpspMail,
       "mpspNetbios": mpspNetbios,
       "mpspDns": mpspDns,
       "mpspIp": mpspIp,
       "mpspVoip": mpspVoip,
       "mpspLayer3Traffic": mpspLayer3Traffic,
       "mpspIpData": mpspIpData,
       "mpspApplications": mpspApplications,
       "mpspIpControl": mpspIpControl,
       "mpspManagement": mpspManagement,
       "dbIPv4": dbIPv4,
       "ipLongTerm": ipLongTerm,
       "ilBaseTable": ilBaseTable,
       "ilBaseEntry": ilBaseEntry,
       "ilbIpIndex": ilbIpIndex,
       "ilbTimeStampIndex": ilbTimeStampIndex,
       "ilbTimeStamp": ilbTimeStamp,
       "ilbFrames": ilbFrames,
       "ilbBytes": ilbBytes,
       "ilbFrameSize": ilbFrameSize,
       "ilbHardwareErrors": ilbHardwareErrors,
       "ilbSoftwareErrors": ilbSoftwareErrors,
       "ilDerivedTable": ilDerivedTable,
       "ilDerivedEntry": ilDerivedEntry,
       "ildIpIndex": ildIpIndex,
       "ildTimeStampIndex": ildTimeStampIndex,
       "ildTimeStamp": ildTimeStamp,
       "ildUtilization": ildUtilization,
       "ildErrorFrames": ildErrorFrames,
       "ilIcmpTable": ilIcmpTable,
       "ilIcmpEntry": ilIcmpEntry,
       "iliIpIndex": iliIpIndex,
       "iliTimeStampIndex": iliTimeStampIndex,
       "iliTimeStamp": iliTimeStamp,
       "iliPing": iliPing,
       "iliSrcQuench": iliSrcQuench,
       "iliRedirect": iliRedirect,
       "iliTtlExceeded": iliTtlExceeded,
       "iliParamProblem": iliParamProblem,
       "iliTimestamp": iliTimestamp,
       "iliFragTimeout": iliFragTimeout,
       "iliNetUnreachable": iliNetUnreachable,
       "iliHostUnreachable": iliHostUnreachable,
       "iliProtocolUnreachable": iliProtocolUnreachable,
       "iliPortUnreachable": iliPortUnreachable,
       "iliFragRequired": iliFragRequired,
       "iliSrcRouteFail": iliSrcRouteFail,
       "iliDestNetUnknown": iliDestNetUnknown,
       "iliDestHostUnknown": iliDestHostUnknown,
       "iliSrcHostIsolated": iliSrcHostIsolated,
       "iliNetProhibited": iliNetProhibited,
       "iliHostProhibited": iliHostProhibited,
       "iliNetTosUnreachable": iliNetTosUnreachable,
       "iliHostTosUnreachable": iliHostTosUnreachable,
       "iliPerformance": iliPerformance,
       "iliNetRouteProblem": iliNetRouteProblem,
       "iliHostRouteProblem": iliHostRouteProblem,
       "iliAppRouteProblem": iliAppRouteProblem,
       "iliRouteChange": iliRouteChange,
       "iliErrors": iliErrors,
       "iliMaintenance": iliMaintenance,
       "ipShortTerm": ipShortTerm,
       "isBaseTable": isBaseTable,
       "isBaseEntry": isBaseEntry,
       "isbIpIndex": isbIpIndex,
       "isbTimeStampIndex": isbTimeStampIndex,
       "isbTimeStamp": isbTimeStamp,
       "isbFrames": isbFrames,
       "isbBytes": isbBytes,
       "isbFrameSize": isbFrameSize,
       "isbHardwareErrors": isbHardwareErrors,
       "isbSoftwareErrors": isbSoftwareErrors,
       "isDerivedTable": isDerivedTable,
       "isDerivedEntry": isDerivedEntry,
       "isdIpIndex": isdIpIndex,
       "isdTimeStampIndex": isdTimeStampIndex,
       "isdTimeStamp": isdTimeStamp,
       "isdUtilization": isdUtilization,
       "isdErrorFrames": isdErrorFrames,
       "isIcmpTable": isIcmpTable,
       "isIcmpEntry": isIcmpEntry,
       "isiIpIndex": isiIpIndex,
       "isiTimeStampIndex": isiTimeStampIndex,
       "isiTimeStamp": isiTimeStamp,
       "isiPing": isiPing,
       "isiSrcQuench": isiSrcQuench,
       "isiRedirect": isiRedirect,
       "isiTtlExceeded": isiTtlExceeded,
       "isiParamProblem": isiParamProblem,
       "isiTimestamp": isiTimestamp,
       "isiFragTimeout": isiFragTimeout,
       "isiNetUnreachable": isiNetUnreachable,
       "isiHostUnreachable": isiHostUnreachable,
       "isiProtocolUnreachable": isiProtocolUnreachable,
       "isiPortUnreachable": isiPortUnreachable,
       "isiFragRequired": isiFragRequired,
       "isiSrcRouteFail": isiSrcRouteFail,
       "isiDestNetUnknown": isiDestNetUnknown,
       "isiDestHostUnknown": isiDestHostUnknown,
       "isiSrcHostIsolated": isiSrcHostIsolated,
       "isiNetProhibited": isiNetProhibited,
       "isiHostProhibited": isiHostProhibited,
       "isiNetTosUnreachable": isiNetTosUnreachable,
       "isiHostTosUnreachable": isiHostTosUnreachable,
       "isiPerformance": isiPerformance,
       "isiNetRouteProblem": isiNetRouteProblem,
       "isiHostRouteProblem": isiHostRouteProblem,
       "isiAppRouteProblem": isiAppRouteProblem,
       "isiRouteChange": isiRouteChange,
       "isiErrors": isiErrors,
       "isiMaintenance": isiMaintenance,
       "dbIPv4Peer": dbIPv4Peer,
       "ipPeerLongTerm": ipPeerLongTerm,
       "iplBaseTable": iplBaseTable,
       "iplBaseEntry": iplBaseEntry,
       "iplbIp1Index": iplbIp1Index,
       "iplbIp2Index": iplbIp2Index,
       "iplbTimeStampIndex": iplbTimeStampIndex,
       "iplbTimeStamp": iplbTimeStamp,
       "iplbFrames": iplbFrames,
       "iplbBytes": iplbBytes,
       "iplbFrameSize": iplbFrameSize,
       "iplbHardwareErrors": iplbHardwareErrors,
       "iplbSoftwareErrors": iplbSoftwareErrors,
       "iplDerivedTable": iplDerivedTable,
       "iplDerivedEntry": iplDerivedEntry,
       "ipldIp1Index": ipldIp1Index,
       "ipldIp2Index": ipldIp2Index,
       "ipldTimeStampIndex": ipldTimeStampIndex,
       "ipldTimeStamp": ipldTimeStamp,
       "ipldUtilization": ipldUtilization,
       "ipldErrorFrames": ipldErrorFrames,
       "iplIcmpTable": iplIcmpTable,
       "iplIcmpEntry": iplIcmpEntry,
       "ipliIp1Index": ipliIp1Index,
       "ipliIp2Index": ipliIp2Index,
       "ipliTimeStampIndex": ipliTimeStampIndex,
       "ipliTimeStamp": ipliTimeStamp,
       "ipliPing": ipliPing,
       "ipliSrcQuench": ipliSrcQuench,
       "ipliRedirect": ipliRedirect,
       "ipliTtlExceeded": ipliTtlExceeded,
       "ipliParamProblem": ipliParamProblem,
       "ipliTimestamp": ipliTimestamp,
       "ipliFragTimeout": ipliFragTimeout,
       "ipliNetUnreachable": ipliNetUnreachable,
       "ipliHostUnreachable": ipliHostUnreachable,
       "ipliProtocolUnreachable": ipliProtocolUnreachable,
       "ipliPortUnreachable": ipliPortUnreachable,
       "ipliFragRequired": ipliFragRequired,
       "ipliSrcRouteFail": ipliSrcRouteFail,
       "ipliDestNetUnknown": ipliDestNetUnknown,
       "ipliDestHostUnknown": ipliDestHostUnknown,
       "ipliSrcHostIsolated": ipliSrcHostIsolated,
       "ipliNetProhibited": ipliNetProhibited,
       "ipliHostProhibited": ipliHostProhibited,
       "ipliNetTosUnreachable": ipliNetTosUnreachable,
       "ipliHostTosUnreachable": ipliHostTosUnreachable,
       "ipliPerformance": ipliPerformance,
       "ipliNetRouteProblem": ipliNetRouteProblem,
       "ipliHostRouteProblem": ipliHostRouteProblem,
       "ipliAppRouteProblem": ipliAppRouteProblem,
       "ipliRouteChange": ipliRouteChange,
       "ipliErrors": ipliErrors,
       "ipliMaintenance": ipliMaintenance,
       "ipPeerShortTerm": ipPeerShortTerm,
       "ipsBaseTable": ipsBaseTable,
       "ipsBaseEntry": ipsBaseEntry,
       "ipsbIp1Index": ipsbIp1Index,
       "ipsbIp2Index": ipsbIp2Index,
       "ipsbTimeStampIndex": ipsbTimeStampIndex,
       "ipsbTimeStamp": ipsbTimeStamp,
       "ipsbFrames": ipsbFrames,
       "ipsbBytes": ipsbBytes,
       "ipsbFrameSize": ipsbFrameSize,
       "ipsbHardwareErrors": ipsbHardwareErrors,
       "ipsbSoftwareErrors": ipsbSoftwareErrors,
       "ipsDerivedTable": ipsDerivedTable,
       "ipsDerivedEntry": ipsDerivedEntry,
       "ipsdIp1Index": ipsdIp1Index,
       "ipsdIp2Index": ipsdIp2Index,
       "ipsdTimeStampIndex": ipsdTimeStampIndex,
       "ipsdTimeStamp": ipsdTimeStamp,
       "ipsdUtilization": ipsdUtilization,
       "ipsdErrorFrames": ipsdErrorFrames,
       "ipsIcmpTable": ipsIcmpTable,
       "ipsIcmpEntry": ipsIcmpEntry,
       "ipsiIp1Index": ipsiIp1Index,
       "ipsiIp2Index": ipsiIp2Index,
       "ipsiTimeStampIndex": ipsiTimeStampIndex,
       "ipsiTimeStamp": ipsiTimeStamp,
       "ipsiPing": ipsiPing,
       "ipsiSrcQuench": ipsiSrcQuench,
       "ipsiRedirect": ipsiRedirect,
       "ipsiTtlExceeded": ipsiTtlExceeded,
       "ipsiParamProblem": ipsiParamProblem,
       "ipsiTimestamp": ipsiTimestamp,
       "ipsiFragTimeout": ipsiFragTimeout,
       "ipsiNetUnreachable": ipsiNetUnreachable,
       "ipsiHostUnreachable": ipsiHostUnreachable,
       "ipsiProtocolUnreachable": ipsiProtocolUnreachable,
       "ipsiPortUnreachable": ipsiPortUnreachable,
       "ipsiFragRequired": ipsiFragRequired,
       "ipsiSrcRouteFail": ipsiSrcRouteFail,
       "ipsiDestNetUnknown": ipsiDestNetUnknown,
       "ipsiDestHostUnknown": ipsiDestHostUnknown,
       "ipsiSrcHostIsolated": ipsiSrcHostIsolated,
       "ipsiNetProhibited": ipsiNetProhibited,
       "ipsiHostProhibited": ipsiHostProhibited,
       "ipsiNetTosUnreachable": ipsiNetTosUnreachable,
       "ipsiHostTosUnreachable": ipsiHostTosUnreachable,
       "ipsiPerformance": ipsiPerformance,
       "ipsiNetRouteProblem": ipsiNetRouteProblem,
       "ipsiHostRouteProblem": ipsiHostRouteProblem,
       "ipsiAppRouteProblem": ipsiAppRouteProblem,
       "ipsiRouteChange": ipsiRouteChange,
       "ipsiErrors": ipsiErrors,
       "ipsiMaintenance": ipsiMaintenance,
       "dbProtocol": dbProtocol,
       "protocolLongTerm": protocolLongTerm,
       "plBaseTable": plBaseTable,
       "plBaseEntry": plBaseEntry,
       "plbLayerIndex": plbLayerIndex,
       "plbIdIndex": plbIdIndex,
       "plbTimeStampIndex": plbTimeStampIndex,
       "plbTimeStamp": plbTimeStamp,
       "plbProtocolName": plbProtocolName,
       "plbFrames": plbFrames,
       "plbBytes": plbBytes,
       "plbFrameSize": plbFrameSize,
       "plbHardwareErrors": plbHardwareErrors,
       "plbSoftwareErrors": plbSoftwareErrors,
       "plDerivedTable": plDerivedTable,
       "plDerivedEntry": plDerivedEntry,
       "pldLayerIndex": pldLayerIndex,
       "pldIdIndex": pldIdIndex,
       "pldTimeStampIndex": pldTimeStampIndex,
       "pldTimeStamp": pldTimeStamp,
       "pldProtocolName": pldProtocolName,
       "pldUtilization": pldUtilization,
       "pldErrorFrames": pldErrorFrames,
       "protocolShortTerm": protocolShortTerm,
       "psBaseTable": psBaseTable,
       "psBaseEntry": psBaseEntry,
       "psbLayerIndex": psbLayerIndex,
       "psbIdIndex": psbIdIndex,
       "psbTimeStampIndex": psbTimeStampIndex,
       "psbTimeStamp": psbTimeStamp,
       "psbProtocolName": psbProtocolName,
       "psbFrames": psbFrames,
       "psbBytes": psbBytes,
       "psbFrameSize": psbFrameSize,
       "psbHardwareErrors": psbHardwareErrors,
       "psbSoftwareErrors": psbSoftwareErrors,
       "psDerivedTable": psDerivedTable,
       "psDerivedEntry": psDerivedEntry,
       "psdLayerIndex": psdLayerIndex,
       "psdIdIndex": psdIdIndex,
       "psdTimeStampIndex": psdTimeStampIndex,
       "psdTimeStamp": psdTimeStamp,
       "psdProtocolName": psdProtocolName,
       "psdUtilization": psdUtilization,
       "psdErrorFrames": psdErrorFrames,
       "dbNetChannel": dbNetChannel,
       "netChanLongTermTable": netChanLongTermTable,
       "netChanLongTermEntry": netChanLongTermEntry,
       "nlTypeIndex": nlTypeIndex,
       "nlNameIndex": nlNameIndex,
       "nlTimeStampIndex": nlTimeStampIndex,
       "nlTimeStamp": nlTimeStamp,
       "nlFrames": nlFrames,
       "nlBytes": nlBytes,
       "nlFrameSize": nlFrameSize,
       "nlHardErrors": nlHardErrors,
       "nlSoftErrors": nlSoftErrors,
       "nlUtilization": nlUtilization,
       "nlHardErrorsPercent": nlHardErrorsPercent,
       "nlSoftErrorsPercent": nlSoftErrorsPercent,
       "nlFramesPercent": nlFramesPercent,
       "nlBytesPercent": nlBytesPercent,
       "netChanShortTermTable": netChanShortTermTable,
       "netChanShortTermEntry": netChanShortTermEntry,
       "nsTypeIndex": nsTypeIndex,
       "nsNameIndex": nsNameIndex,
       "nsTimeStampIndex": nsTimeStampIndex,
       "nsTimeStamp": nsTimeStamp,
       "nsFrames": nsFrames,
       "nsBytes": nsBytes,
       "nsFrameSize": nsFrameSize,
       "nsHardErrors": nsHardErrors,
       "nsSoftErrors": nsSoftErrors,
       "nsUtilization": nsUtilization,
       "nsHardErrorsPercent": nsHardErrorsPercent,
       "nsSoftErrorsPercent": nsSoftErrorsPercent,
       "nsFramesPercent": nsFramesPercent,
       "nsBytesPercent": nsBytesPercent,
       "dbVlan": dbVlan,
       "vlanLongTermTable": vlanLongTermTable,
       "vlanLongTermEntry": vlanLongTermEntry,
       "vlIdIndex": vlIdIndex,
       "vlTimeStampIndex": vlTimeStampIndex,
       "vlTimeStamp": vlTimeStamp,
       "vlName": vlName,
       "vlFrames": vlFrames,
       "vlBytes": vlBytes,
       "vlFrameSize": vlFrameSize,
       "vlHardErrors": vlHardErrors,
       "vlSoftErrors": vlSoftErrors,
       "vlUtilization": vlUtilization,
       "vlHardErrorsPercent": vlHardErrorsPercent,
       "vlSoftErrorsPercent": vlSoftErrorsPercent,
       "vlFramesPercent": vlFramesPercent,
       "vlBytesPercent": vlBytesPercent,
       "vlanShortTermTable": vlanShortTermTable,
       "vlanShortTermEntry": vlanShortTermEntry,
       "vsIdIndex": vsIdIndex,
       "vsTimeStampIndex": vsTimeStampIndex,
       "vsTimeStamp": vsTimeStamp,
       "vsName": vsName,
       "vsFrames": vsFrames,
       "vsBytes": vsBytes,
       "vsFrameSize": vsFrameSize,
       "vsHardErrors": vsHardErrors,
       "vsSoftErrors": vsSoftErrors,
       "vsUtilization": vsUtilization,
       "vsHardErrorsPercent": vsHardErrorsPercent,
       "vsSoftErrorsPercent": vsSoftErrorsPercent,
       "vsFramesPercent": vsFramesPercent,
       "vsBytesPercent": vsBytesPercent,
       "expAlarms": expAlarms,
       "alarmMessage": alarmMessage,
       "alarmLayer": alarmLayer,
       "alarmTopProtocol": alarmTopProtocol,
       "alarmBaseProtocol": alarmBaseProtocol,
       "alarmCode": alarmCode,
       "alarmFunction": alarmFunction,
       "alarmGroup": alarmGroup,
       "alarmUnitType": alarmUnitType,
       "alarmClass": alarmClass,
       "alarmTime": alarmTime,
       "codimaExpressNotifications": codimaExpressNotifications,
       "expressTraps": expressTraps,
       "expressAlarm": expressAlarm,
       "codimaExpressConformance": codimaExpressConformance,
       "expressObjectGroups": expressObjectGroups,
       "historyDatabaseGroups": historyDatabaseGroups,
       "dbControlGroups": dbControlGroups,
       "ctrlTimeGroup": ctrlTimeGroup,
       "dbSegmentGroups": dbSegmentGroups,
       "segLongTermGroups": segLongTermGroups,
       "slBaseGroup": slBaseGroup,
       "slBroadcastGroup": slBroadcastGroup,
       "slDerivedGroup": slDerivedGroup,
       "slEthernetGroup": slEthernetGroup,
       "slIcmpGroup": slIcmpGroup,
       "slPortGroup": slPortGroup,
       "segShortTermGroups": segShortTermGroups,
       "ssBaseGroup": ssBaseGroup,
       "ssBroadcastGroup": ssBroadcastGroup,
       "ssDerivedGroup": ssDerivedGroup,
       "ssEthernetGroup": ssEthernetGroup,
       "ssIcmpGroup": ssIcmpGroup,
       "ssPortGroup": ssPortGroup,
       "dbMacGroups": dbMacGroups,
       "macLongTermGroups": macLongTermGroups,
       "mlBaseGroup": mlBaseGroup,
       "mlDerivedGroup": mlDerivedGroup,
       "mlDuplexGroup": mlDuplexGroup,
       "mlEthernetGroup": mlEthernetGroup,
       "mlIcmpGroup": mlIcmpGroup,
       "mlProtocolGroup": mlProtocolGroup,
       "macShortTermGroups": macShortTermGroups,
       "msBaseGroup": msBaseGroup,
       "msDerivedGroup": msDerivedGroup,
       "msDuplexGroup": msDuplexGroup,
       "msEthernetGroup": msEthernetGroup,
       "msIcmpGroup": msIcmpGroup,
       "msProtocolGroup": msProtocolGroup,
       "dbMacPeerGroups": dbMacPeerGroups,
       "macPeerLongTermGroups": macPeerLongTermGroups,
       "mplBaseGroup": mplBaseGroup,
       "mplDerivedGroup": mplDerivedGroup,
       "mplDuplexGroup": mplDuplexGroup,
       "mplProtocolGroup": mplProtocolGroup,
       "macPeerShortTermGroups": macPeerShortTermGroups,
       "mpsBaseGroup": mpsBaseGroup,
       "mpsDerivedGroup": mpsDerivedGroup,
       "mpsDuplexGroup": mpsDuplexGroup,
       "mpsProtocolGroup": mpsProtocolGroup,
       "dbIPv4Groups": dbIPv4Groups,
       "ipLongTermGroups": ipLongTermGroups,
       "ilBaseGroup": ilBaseGroup,
       "ilDerivedGroup": ilDerivedGroup,
       "ilIcmpGroup": ilIcmpGroup,
       "ipShortTermGroups": ipShortTermGroups,
       "isBaseGroup": isBaseGroup,
       "isDerivedGroup": isDerivedGroup,
       "isIcmpGroup": isIcmpGroup,
       "dpIPv4PeerGroups": dpIPv4PeerGroups,
       "ipPeerLongTermGroups": ipPeerLongTermGroups,
       "iplBaseGroup": iplBaseGroup,
       "iplDerivedGroup": iplDerivedGroup,
       "iplIcmpGroup": iplIcmpGroup,
       "ipPeerShortTermGroups": ipPeerShortTermGroups,
       "ipsBaseGroup": ipsBaseGroup,
       "ipsDerivedGroup": ipsDerivedGroup,
       "ipsIcmpGroup": ipsIcmpGroup,
       "dbProtocolGroups": dbProtocolGroups,
       "protocolLongTermGroups": protocolLongTermGroups,
       "plBaseGroup": plBaseGroup,
       "plDerivedGroup": plDerivedGroup,
       "protocolShortTermGroups": protocolShortTermGroups,
       "psBaseGroup": psBaseGroup,
       "psDerivedGroup": psDerivedGroup,
       "dbNetChannelGroups": dbNetChannelGroups,
       "netChannelLongTermGroup": netChannelLongTermGroup,
       "netChannelShortTermGroup": netChannelShortTermGroup,
       "dbVlanGroups": dbVlanGroups,
       "vlanLongTermGroup": vlanLongTermGroup,
       "vlanShortTermGroup": vlanShortTermGroup,
       "alarmObjectGroup": alarmObjectGroup,
       "expressNotificationGroups": expressNotificationGroups,
       "alarmNotifyGroup": alarmNotifyGroup}
)
