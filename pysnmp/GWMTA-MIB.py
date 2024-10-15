# SNMP MIB module (GWMTA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GWMTA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:24 2024
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

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_Gwmta_ObjectIdentity = ObjectIdentity
gwmta = _Gwmta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 37)
)
_Mta_ObjectIdentity = ObjectIdentity
mta = _Mta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1)
)
_MtaTable_Object = MibTable
mtaTable = _MtaTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1)
)
if mibBuilder.loadTexts:
    mtaTable.setStatus("mandatory")
_MtaEntry_Object = MibTableRow
mtaEntry = _MtaEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1)
)
mtaEntry.setIndexNames(
    (0, "GWMTA-MIB", "mtaIndex"),
)
if mibBuilder.loadTexts:
    mtaEntry.setStatus("mandatory")
_MtaIndex_Type = Integer32
_MtaIndex_Object = MibTableColumn
mtaIndex = _MtaIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 1),
    _MtaIndex_Type()
)
mtaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtaIndex.setStatus("mandatory")


class _MtaDomainName_Type(DisplayString):
    """Custom type mtaDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MtaDomainName_Type.__name__ = "DisplayString"
_MtaDomainName_Object = MibTableColumn
mtaDomainName = _MtaDomainName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 2),
    _MtaDomainName_Type()
)
mtaDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaDomainName.setStatus("mandatory")
_MtaTotalDomains_Type = Gauge32
_MtaTotalDomains_Object = MibTableColumn
mtaTotalDomains = _MtaTotalDomains_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 3),
    _MtaTotalDomains_Type()
)
mtaTotalDomains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTotalDomains.setStatus("mandatory")
_MtaClosedDomains_Type = Gauge32
_MtaClosedDomains_Object = MibTableColumn
mtaClosedDomains = _MtaClosedDomains_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 4),
    _MtaClosedDomains_Type()
)
mtaClosedDomains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaClosedDomains.setStatus("mandatory")
_MtaTotalPostOffices_Type = Gauge32
_MtaTotalPostOffices_Object = MibTableColumn
mtaTotalPostOffices = _MtaTotalPostOffices_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 5),
    _MtaTotalPostOffices_Type()
)
mtaTotalPostOffices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTotalPostOffices.setStatus("mandatory")
_MtaClosedPostOffices_Type = Gauge32
_MtaClosedPostOffices_Object = MibTableColumn
mtaClosedPostOffices = _MtaClosedPostOffices_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 6),
    _MtaClosedPostOffices_Type()
)
mtaClosedPostOffices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaClosedPostOffices.setStatus("mandatory")
_MtaTotalGateways_Type = Gauge32
_MtaTotalGateways_Object = MibTableColumn
mtaTotalGateways = _MtaTotalGateways_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 7),
    _MtaTotalGateways_Type()
)
mtaTotalGateways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTotalGateways.setStatus("mandatory")
_MtaClosedGateways_Type = Gauge32
_MtaClosedGateways_Object = MibTableColumn
mtaClosedGateways = _MtaClosedGateways_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 8),
    _MtaClosedGateways_Type()
)
mtaClosedGateways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaClosedGateways.setStatus("mandatory")
_MtaRoutedMsgs_Type = Counter32
_MtaRoutedMsgs_Object = MibTableColumn
mtaRoutedMsgs = _MtaRoutedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 9),
    _MtaRoutedMsgs_Type()
)
mtaRoutedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaRoutedMsgs.setStatus("mandatory")
_MtaTenMinuteRoutedMsgs_Type = Gauge32
_MtaTenMinuteRoutedMsgs_Object = MibTableColumn
mtaTenMinuteRoutedMsgs = _MtaTenMinuteRoutedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 10),
    _MtaTenMinuteRoutedMsgs_Type()
)
mtaTenMinuteRoutedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTenMinuteRoutedMsgs.setStatus("mandatory")
_MtaUndeliverableMsgs_Type = Counter32
_MtaUndeliverableMsgs_Object = MibTableColumn
mtaUndeliverableMsgs = _MtaUndeliverableMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 11),
    _MtaUndeliverableMsgs_Type()
)
mtaUndeliverableMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaUndeliverableMsgs.setStatus("mandatory")
_MtaTenMinuteUndeliverableMsgs_Type = Gauge32
_MtaTenMinuteUndeliverableMsgs_Object = MibTableColumn
mtaTenMinuteUndeliverableMsgs = _MtaTenMinuteUndeliverableMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 12),
    _MtaTenMinuteUndeliverableMsgs_Type()
)
mtaTenMinuteUndeliverableMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTenMinuteUndeliverableMsgs.setStatus("mandatory")
_MtaErrorMsgs_Type = Counter32
_MtaErrorMsgs_Object = MibTableColumn
mtaErrorMsgs = _MtaErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 13),
    _MtaErrorMsgs_Type()
)
mtaErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaErrorMsgs.setStatus("mandatory")
_MtaTenMinuteErrorMsgs_Type = Gauge32
_MtaTenMinuteErrorMsgs_Object = MibTableColumn
mtaTenMinuteErrorMsgs = _MtaTenMinuteErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 14),
    _MtaTenMinuteErrorMsgs_Type()
)
mtaTenMinuteErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTenMinuteErrorMsgs.setStatus("mandatory")


class _MtaResiliencyState_Type(DisplayString):
    """Custom type mtaResiliencyState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MtaResiliencyState_Type.__name__ = "DisplayString"
_MtaResiliencyState_Object = MibTableColumn
mtaResiliencyState = _MtaResiliencyState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 15),
    _MtaResiliencyState_Type()
)
mtaResiliencyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaResiliencyState.setStatus("mandatory")
_MtaUptime_Type = TimeTicks
_MtaUptime_Object = MibTableColumn
mtaUptime = _MtaUptime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 16),
    _MtaUptime_Type()
)
mtaUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaUptime.setStatus("mandatory")


class _MtaLogLevel_Type(Integer32):
    """Custom type mtaLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("verbose", 2))
    )


_MtaLogLevel_Type.__name__ = "Integer32"
_MtaLogLevel_Object = MibTableColumn
mtaLogLevel = _MtaLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 17),
    _MtaLogLevel_Type()
)
mtaLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtaLogLevel.setStatus("mandatory")


class _MtaFileLogging_Type(Integer32):
    """Custom type mtaFileLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MtaFileLogging_Type.__name__ = "Integer32"
_MtaFileLogging_Object = MibTableColumn
mtaFileLogging = _MtaFileLogging_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 18),
    _MtaFileLogging_Type()
)
mtaFileLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtaFileLogging.setStatus("mandatory")
_MtaMaxLogFileAge_Type = Integer32
_MtaMaxLogFileAge_Object = MibTableColumn
mtaMaxLogFileAge = _MtaMaxLogFileAge_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 19),
    _MtaMaxLogFileAge_Type()
)
mtaMaxLogFileAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtaMaxLogFileAge.setStatus("mandatory")
_MtaMaxLogFileSpace_Type = Integer32
_MtaMaxLogFileSpace_Object = MibTableColumn
mtaMaxLogFileSpace = _MtaMaxLogFileSpace_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 20),
    _MtaMaxLogFileSpace_Type()
)
mtaMaxLogFileSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtaMaxLogFileSpace.setStatus("mandatory")


class _MtaCurrentLogFile_Type(DisplayString):
    """Custom type mtaCurrentLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MtaCurrentLogFile_Type.__name__ = "DisplayString"
_MtaCurrentLogFile_Object = MibTableColumn
mtaCurrentLogFile = _MtaCurrentLogFile_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 21),
    _MtaCurrentLogFile_Type()
)
mtaCurrentLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaCurrentLogFile.setStatus("mandatory")


class _MtaRestart_Type(Integer32):
    """Custom type mtaRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MtaRestart_Type.__name__ = "Integer32"
_MtaRestart_Object = MibTableColumn
mtaRestart = _MtaRestart_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 22),
    _MtaRestart_Type()
)
mtaRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtaRestart.setStatus("mandatory")


class _MtaGUID_Type(DisplayString):
    """Custom type mtaGUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_MtaGUID_Type.__name__ = "DisplayString"
_MtaGUID_Object = MibTableColumn
mtaGUID = _MtaGUID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 23),
    _MtaGUID_Type()
)
mtaGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGUID.setStatus("mandatory")


class _MtaOS_Type(DisplayString):
    """Custom type mtaOS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MtaOS_Type.__name__ = "DisplayString"
_MtaOS_Object = MibTableColumn
mtaOS = _MtaOS_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 24),
    _MtaOS_Type()
)
mtaOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaOS.setStatus("mandatory")


class _MtaVersion_Type(DisplayString):
    """Custom type mtaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MtaVersion_Type.__name__ = "DisplayString"
_MtaVersion_Object = MibTableColumn
mtaVersion = _MtaVersion_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 25),
    _MtaVersion_Type()
)
mtaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaVersion.setStatus("mandatory")


class _MtaAdmThreadStatus_Type(DisplayString):
    """Custom type mtaAdmThreadStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MtaAdmThreadStatus_Type.__name__ = "DisplayString"
_MtaAdmThreadStatus_Object = MibTableColumn
mtaAdmThreadStatus = _MtaAdmThreadStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 26),
    _MtaAdmThreadStatus_Type()
)
mtaAdmThreadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaAdmThreadStatus.setStatus("mandatory")
_MtaAdmCompletedMsgs_Type = Counter32
_MtaAdmCompletedMsgs_Object = MibTableColumn
mtaAdmCompletedMsgs = _MtaAdmCompletedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 27),
    _MtaAdmCompletedMsgs_Type()
)
mtaAdmCompletedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaAdmCompletedMsgs.setStatus("mandatory")
_MtaAdmErrorMsgs_Type = Counter32
_MtaAdmErrorMsgs_Object = MibTableColumn
mtaAdmErrorMsgs = _MtaAdmErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 28),
    _MtaAdmErrorMsgs_Type()
)
mtaAdmErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaAdmErrorMsgs.setStatus("mandatory")
_MtaAdmInQueueMsgs_Type = Gauge32
_MtaAdmInQueueMsgs_Object = MibTableColumn
mtaAdmInQueueMsgs = _MtaAdmInQueueMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 29),
    _MtaAdmInQueueMsgs_Type()
)
mtaAdmInQueueMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaAdmInQueueMsgs.setStatus("mandatory")


class _MtaAdmDBStatus_Type(DisplayString):
    """Custom type mtaAdmDBStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MtaAdmDBStatus_Type.__name__ = "DisplayString"
_MtaAdmDBStatus_Object = MibTableColumn
mtaAdmDBStatus = _MtaAdmDBStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 30),
    _MtaAdmDBStatus_Type()
)
mtaAdmDBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaAdmDBStatus.setStatus("mandatory")


class _MtaAdmDBSortLang_Type(DisplayString):
    """Custom type mtaAdmDBSortLang based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MtaAdmDBSortLang_Type.__name__ = "DisplayString"
_MtaAdmDBSortLang_Object = MibTableColumn
mtaAdmDBSortLang = _MtaAdmDBSortLang_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 31),
    _MtaAdmDBSortLang_Type()
)
mtaAdmDBSortLang.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaAdmDBSortLang.setStatus("mandatory")
_MtaAdmDBRecoverCnt_Type = Counter32
_MtaAdmDBRecoverCnt_Object = MibTableColumn
mtaAdmDBRecoverCnt = _MtaAdmDBRecoverCnt_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 32),
    _MtaAdmDBRecoverCnt_Type()
)
mtaAdmDBRecoverCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaAdmDBRecoverCnt.setStatus("mandatory")


class _MtaDN_Type(DisplayString):
    """Custom type mtaDN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MtaDN_Type.__name__ = "DisplayString"
_MtaDN_Object = MibTableColumn
mtaDN = _MtaDN_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 33),
    _MtaDN_Type()
)
mtaDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaDN.setStatus("mandatory")
_MtaLocalQCount_Type = Counter32
_MtaLocalQCount_Object = MibTableColumn
mtaLocalQCount = _MtaLocalQCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 34),
    _MtaLocalQCount_Type()
)
mtaLocalQCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaLocalQCount.setStatus("mandatory")
_MtaLocalQSize_Type = Counter32
_MtaLocalQSize_Object = MibTableColumn
mtaLocalQSize = _MtaLocalQSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 35),
    _MtaLocalQSize_Type()
)
mtaLocalQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaLocalQSize.setStatus("mandatory")
_MtaOtherQCount_Type = Counter32
_MtaOtherQCount_Object = MibTableColumn
mtaOtherQCount = _MtaOtherQCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 36),
    _MtaOtherQCount_Type()
)
mtaOtherQCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaOtherQCount.setStatus("mandatory")
_MtaOtherQSize_Type = Counter32
_MtaOtherQSize_Object = MibTableColumn
mtaOtherQSize = _MtaOtherQSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 37),
    _MtaOtherQSize_Type()
)
mtaOtherQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaOtherQSize.setStatus("mandatory")
_MtaINetQCount_Type = Counter32
_MtaINetQCount_Object = MibTableColumn
mtaINetQCount = _MtaINetQCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 38),
    _MtaINetQCount_Type()
)
mtaINetQCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaINetQCount.setStatus("mandatory")
_MtaINetQSize_Type = Counter32
_MtaINetQSize_Object = MibTableColumn
mtaINetQSize = _MtaINetQSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 39),
    _MtaINetQSize_Type()
)
mtaINetQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaINetQSize.setStatus("mandatory")
_MtaADAQCount_Type = Counter32
_MtaADAQCount_Object = MibTableColumn
mtaADAQCount = _MtaADAQCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 40),
    _MtaADAQCount_Type()
)
mtaADAQCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaADAQCount.setStatus("mandatory")
_MtaADAQSize_Type = Counter32
_MtaADAQSize_Object = MibTableColumn
mtaADAQSize = _MtaADAQSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 41),
    _MtaADAQSize_Type()
)
mtaADAQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaADAQSize.setStatus("mandatory")
_MtaOldestQMsg_Type = TimeTicks
_MtaOldestQMsg_Object = MibTableColumn
mtaOldestQMsg = _MtaOldestQMsg_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 42),
    _MtaOldestQMsg_Type()
)
mtaOldestQMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaOldestQMsg.setStatus("mandatory")


class _MtaOldestQDestname_Type(DisplayString):
    """Custom type mtaOldestQDestname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_MtaOldestQDestname_Type.__name__ = "DisplayString"
_MtaOldestQDestname_Object = MibTableColumn
mtaOldestQDestname = _MtaOldestQDestname_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 43),
    _MtaOldestQDestname_Type()
)
mtaOldestQDestname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaOldestQDestname.setStatus("mandatory")
_MtaOldestADAQMsg_Type = TimeTicks
_MtaOldestADAQMsg_Object = MibTableColumn
mtaOldestADAQMsg = _MtaOldestADAQMsg_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 44),
    _MtaOldestADAQMsg_Type()
)
mtaOldestADAQMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaOldestADAQMsg.setStatus("mandatory")
_MtaAvailDiskSpace_Type = Counter32
_MtaAvailDiskSpace_Object = MibTableColumn
mtaAvailDiskSpace = _MtaAvailDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 45),
    _MtaAvailDiskSpace_Type()
)
mtaAvailDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaAvailDiskSpace.setStatus("mandatory")
_MtaHTTPPort_Type = Integer32
_MtaHTTPPort_Object = MibTableColumn
mtaHTTPPort = _MtaHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 46),
    _MtaHTTPPort_Type()
)
mtaHTTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtaHTTPPort.setStatus("mandatory")


class _MtaAdmDBStatusNumber_Type(Integer32):
    """Custom type mtaAdmDBStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("normal", 0),
          ("recovering", 2),
          ("unknown", 3))
    )


_MtaAdmDBStatusNumber_Type.__name__ = "Integer32"
_MtaAdmDBStatusNumber_Object = MibTableColumn
mtaAdmDBStatusNumber = _MtaAdmDBStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 47),
    _MtaAdmDBStatusNumber_Type()
)
mtaAdmDBStatusNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtaAdmDBStatusNumber.setStatus("mandatory")
_MtaRouterQCount_Type = Counter32
_MtaRouterQCount_Object = MibTableColumn
mtaRouterQCount = _MtaRouterQCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 1, 1, 1, 48),
    _MtaRouterQCount_Type()
)
mtaRouterQCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaRouterQCount.setStatus("mandatory")
_MtaTrapInfo_ObjectIdentity = ObjectIdentity
mtaTrapInfo = _MtaTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 2)
)
_MtaTrapTime_Type = Integer32
_MtaTrapTime_Object = MibScalar
mtaTrapTime = _MtaTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 2, 1),
    _MtaTrapTime_Type()
)
mtaTrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtaTrapTime.setStatus("mandatory")


class _MtaServerName_Type(DisplayString):
    """Custom type mtaServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MtaServerName_Type.__name__ = "DisplayString"
_MtaServerName_Object = MibScalar
mtaServerName = _MtaServerName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 2, 2),
    _MtaServerName_Type()
)
mtaServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtaServerName.setStatus("mandatory")


class _MtaTrapDomainName_Type(DisplayString):
    """Custom type mtaTrapDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MtaTrapDomainName_Type.__name__ = "DisplayString"
_MtaTrapDomainName_Object = MibScalar
mtaTrapDomainName = _MtaTrapDomainName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 2, 3),
    _MtaTrapDomainName_Type()
)
mtaTrapDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtaTrapDomainName.setStatus("mandatory")


class _MtaFacilityName_Type(DisplayString):
    """Custom type mtaFacilityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MtaFacilityName_Type.__name__ = "DisplayString"
_MtaFacilityName_Object = MibScalar
mtaFacilityName = _MtaFacilityName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 2, 4),
    _MtaFacilityName_Type()
)
mtaFacilityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtaFacilityName.setStatus("mandatory")


class _MtaFacilityLink_Type(DisplayString):
    """Custom type mtaFacilityLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MtaFacilityLink_Type.__name__ = "DisplayString"
_MtaFacilityLink_Object = MibScalar
mtaFacilityLink = _MtaFacilityLink_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 2, 5),
    _MtaFacilityLink_Type()
)
mtaFacilityLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtaFacilityLink.setStatus("mandatory")


class _MtaClosureReason_Type(DisplayString):
    """Custom type mtaClosureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MtaClosureReason_Type.__name__ = "DisplayString"
_MtaClosureReason_Object = MibScalar
mtaClosureReason = _MtaClosureReason_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 2, 6),
    _MtaClosureReason_Type()
)
mtaClosureReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtaClosureReason.setStatus("mandatory")
_MtaTraps_ObjectIdentity = ObjectIdentity
mtaTraps = _MtaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 3)
)

# Managed Objects groups


# Notification objects

mtaStartupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 3, 0, 1)
)
mtaStartupTrap.setObjects(
      *(("GWMTA-MIB", "mtaTrapTime"),
        ("GWMTA-MIB", "mtaServerName"),
        ("GWMTA-MIB", "mtaGUID"))
)
if mibBuilder.loadTexts:
    mtaStartupTrap.setStatus(
        ""
    )

mtaShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 3, 0, 2)
)
mtaShutdownTrap.setObjects(
      *(("GWMTA-MIB", "mtaTrapTime"),
        ("GWMTA-MIB", "mtaServerName"),
        ("GWMTA-MIB", "mtaDomainName"),
        ("GWMTA-MIB", "mtaGUID"))
)
if mibBuilder.loadTexts:
    mtaShutdownTrap.setStatus(
        ""
    )

mtaRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 3, 0, 3)
)
mtaRestartTrap.setObjects(
      *(("GWMTA-MIB", "mtaTrapTime"),
        ("GWMTA-MIB", "mtaServerName"),
        ("GWMTA-MIB", "mtaDomainName"),
        ("GWMTA-MIB", "mtaGUID"))
)
if mibBuilder.loadTexts:
    mtaRestartTrap.setStatus(
        ""
    )

mtaConfigurationLoadedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 3, 0, 4)
)
mtaConfigurationLoadedTrap.setObjects(
      *(("GWMTA-MIB", "mtaTrapTime"),
        ("GWMTA-MIB", "mtaServerName"),
        ("GWMTA-MIB", "mtaDomainName"),
        ("GWMTA-MIB", "mtaGUID"))
)
if mibBuilder.loadTexts:
    mtaConfigurationLoadedTrap.setStatus(
        ""
    )

mtaFacilityClosedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 3, 0, 5)
)
mtaFacilityClosedTrap.setObjects(
      *(("GWMTA-MIB", "mtaTrapTime"),
        ("GWMTA-MIB", "mtaServerName"),
        ("GWMTA-MIB", "mtaDomainName"),
        ("GWMTA-MIB", "mtaFacilityName"),
        ("GWMTA-MIB", "mtaFacilityLink"),
        ("GWMTA-MIB", "mtaClosureReason"),
        ("GWMTA-MIB", "mtaGUID"))
)
if mibBuilder.loadTexts:
    mtaFacilityClosedTrap.setStatus(
        ""
    )

mtaFacilityOpenedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 3, 0, 6)
)
mtaFacilityOpenedTrap.setObjects(
      *(("GWMTA-MIB", "mtaTrapTime"),
        ("GWMTA-MIB", "mtaServerName"),
        ("GWMTA-MIB", "mtaDomainName"),
        ("GWMTA-MIB", "mtaFacilityName"),
        ("GWMTA-MIB", "mtaGUID"))
)
if mibBuilder.loadTexts:
    mtaFacilityOpenedTrap.setStatus(
        ""
    )

mtaBackupOnlineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 3, 0, 7)
)
mtaBackupOnlineTrap.setObjects(
      *(("GWMTA-MIB", "mtaTrapTime"),
        ("GWMTA-MIB", "mtaServerName"),
        ("GWMTA-MIB", "mtaDomainName"),
        ("GWMTA-MIB", "mtaGUID"))
)
if mibBuilder.loadTexts:
    mtaBackupOnlineTrap.setStatus(
        ""
    )

mtaBackupStandbyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 37, 3, 0, 8)
)
mtaBackupStandbyTrap.setObjects(
      *(("GWMTA-MIB", "mtaTrapTime"),
        ("GWMTA-MIB", "mtaServerName"),
        ("GWMTA-MIB", "mtaDomainName"),
        ("GWMTA-MIB", "mtaGUID"))
)
if mibBuilder.loadTexts:
    mtaBackupStandbyTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GWMTA-MIB",
    **{"novell": novell,
       "mibDoc": mibDoc,
       "gwmta": gwmta,
       "mta": mta,
       "mtaTable": mtaTable,
       "mtaEntry": mtaEntry,
       "mtaIndex": mtaIndex,
       "mtaDomainName": mtaDomainName,
       "mtaTotalDomains": mtaTotalDomains,
       "mtaClosedDomains": mtaClosedDomains,
       "mtaTotalPostOffices": mtaTotalPostOffices,
       "mtaClosedPostOffices": mtaClosedPostOffices,
       "mtaTotalGateways": mtaTotalGateways,
       "mtaClosedGateways": mtaClosedGateways,
       "mtaRoutedMsgs": mtaRoutedMsgs,
       "mtaTenMinuteRoutedMsgs": mtaTenMinuteRoutedMsgs,
       "mtaUndeliverableMsgs": mtaUndeliverableMsgs,
       "mtaTenMinuteUndeliverableMsgs": mtaTenMinuteUndeliverableMsgs,
       "mtaErrorMsgs": mtaErrorMsgs,
       "mtaTenMinuteErrorMsgs": mtaTenMinuteErrorMsgs,
       "mtaResiliencyState": mtaResiliencyState,
       "mtaUptime": mtaUptime,
       "mtaLogLevel": mtaLogLevel,
       "mtaFileLogging": mtaFileLogging,
       "mtaMaxLogFileAge": mtaMaxLogFileAge,
       "mtaMaxLogFileSpace": mtaMaxLogFileSpace,
       "mtaCurrentLogFile": mtaCurrentLogFile,
       "mtaRestart": mtaRestart,
       "mtaGUID": mtaGUID,
       "mtaOS": mtaOS,
       "mtaVersion": mtaVersion,
       "mtaAdmThreadStatus": mtaAdmThreadStatus,
       "mtaAdmCompletedMsgs": mtaAdmCompletedMsgs,
       "mtaAdmErrorMsgs": mtaAdmErrorMsgs,
       "mtaAdmInQueueMsgs": mtaAdmInQueueMsgs,
       "mtaAdmDBStatus": mtaAdmDBStatus,
       "mtaAdmDBSortLang": mtaAdmDBSortLang,
       "mtaAdmDBRecoverCnt": mtaAdmDBRecoverCnt,
       "mtaDN": mtaDN,
       "mtaLocalQCount": mtaLocalQCount,
       "mtaLocalQSize": mtaLocalQSize,
       "mtaOtherQCount": mtaOtherQCount,
       "mtaOtherQSize": mtaOtherQSize,
       "mtaINetQCount": mtaINetQCount,
       "mtaINetQSize": mtaINetQSize,
       "mtaADAQCount": mtaADAQCount,
       "mtaADAQSize": mtaADAQSize,
       "mtaOldestQMsg": mtaOldestQMsg,
       "mtaOldestQDestname": mtaOldestQDestname,
       "mtaOldestADAQMsg": mtaOldestADAQMsg,
       "mtaAvailDiskSpace": mtaAvailDiskSpace,
       "mtaHTTPPort": mtaHTTPPort,
       "mtaAdmDBStatusNumber": mtaAdmDBStatusNumber,
       "mtaRouterQCount": mtaRouterQCount,
       "mtaTrapInfo": mtaTrapInfo,
       "mtaTrapTime": mtaTrapTime,
       "mtaServerName": mtaServerName,
       "mtaTrapDomainName": mtaTrapDomainName,
       "mtaFacilityName": mtaFacilityName,
       "mtaFacilityLink": mtaFacilityLink,
       "mtaClosureReason": mtaClosureReason,
       "mtaTraps": mtaTraps,
       "mtaStartupTrap": mtaStartupTrap,
       "mtaShutdownTrap": mtaShutdownTrap,
       "mtaRestartTrap": mtaRestartTrap,
       "mtaConfigurationLoadedTrap": mtaConfigurationLoadedTrap,
       "mtaFacilityClosedTrap": mtaFacilityClosedTrap,
       "mtaFacilityOpenedTrap": mtaFacilityOpenedTrap,
       "mtaBackupOnlineTrap": mtaBackupOnlineTrap,
       "mtaBackupStandbyTrap": mtaBackupStandbyTrap}
)
