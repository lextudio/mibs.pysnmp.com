# SNMP MIB module (BN-LOG-MESSAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BN-LOG-MESSAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:29 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(bnLogMsg,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "bnLogMsg")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

bnLogMsgMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1)
)
bnLogMsgMIB.setRevisions(
        ("2013-10-10 00:00",
         "2012-04-10 00:00",
         "2012-03-26 00:00",
         "2011-04-20 00:00",
         "2010-06-29 00:00",
         "2009-04-15 00:00",
         "2009-04-14 00:00",
         "2009-03-31 00:00",
         "2009-03-23 00:00",
         "2007-09-04 00:00",
         "2005-05-04 00:00",
         "2005-04-27 00:00",
         "2003-02-24 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BnLogMsgMIBObjects_ObjectIdentity = ObjectIdentity
bnLogMsgMIBObjects = _BnLogMsgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1)
)


class _BnLogMsgBufferOperaton_Type(Integer32):
    """Custom type bnLogMsgBufferOperaton based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_BnLogMsgBufferOperaton_Type.__name__ = "Integer32"
_BnLogMsgBufferOperaton_Object = MibScalar
bnLogMsgBufferOperaton = _BnLogMsgBufferOperaton_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 1),
    _BnLogMsgBufferOperaton_Type()
)
bnLogMsgBufferOperaton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgBufferOperaton.setStatus("current")


class _BnLogMsgBufferMaxSize_Type(Integer32):
    """Custom type bnLogMsgBufferMaxSize based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              100,
              200,
              400)
        )
    )
    namedValues = NamedValues(
        *(("msgBufferSizeLarge", 200),
          ("msgBufferSizeMedium", 100),
          ("msgBufferSizeSmall", 50),
          ("msgBufferSizeVeryLarge", 400))
    )


_BnLogMsgBufferMaxSize_Type.__name__ = "Integer32"
_BnLogMsgBufferMaxSize_Object = MibScalar
bnLogMsgBufferMaxSize = _BnLogMsgBufferMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 2),
    _BnLogMsgBufferMaxSize_Type()
)
bnLogMsgBufferMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgBufferMaxSize.setStatus("current")


class _BnLogMsgBufferCurSize_Type(Integer32):
    """Custom type bnLogMsgBufferCurSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_BnLogMsgBufferCurSize_Type.__name__ = "Integer32"
_BnLogMsgBufferCurSize_Object = MibScalar
bnLogMsgBufferCurSize = _BnLogMsgBufferCurSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 3),
    _BnLogMsgBufferCurSize_Type()
)
bnLogMsgBufferCurSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnLogMsgBufferCurSize.setStatus("current")


class _BnLogMsgBufferFullAction_Type(Integer32):
    """Custom type bnLogMsgBufferFullAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("latch", 2),
          ("overwrite", 1))
    )


_BnLogMsgBufferFullAction_Type.__name__ = "Integer32"
_BnLogMsgBufferFullAction_Object = MibScalar
bnLogMsgBufferFullAction = _BnLogMsgBufferFullAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 4),
    _BnLogMsgBufferFullAction_Type()
)
bnLogMsgBufferFullAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgBufferFullAction.setStatus("current")


class _BnLogMsgBufferSaveTargets_Type(Integer32):
    """Custom type bnLogMsgBufferSaveTargets based on Integer32"""
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
        *(("msgTypeCritical", 1),
          ("msgTypeInformational", 3),
          ("msgTypeNone", 4),
          ("msgTypeSerious", 2))
    )


_BnLogMsgBufferSaveTargets_Type.__name__ = "Integer32"
_BnLogMsgBufferSaveTargets_Object = MibScalar
bnLogMsgBufferSaveTargets = _BnLogMsgBufferSaveTargets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 5),
    _BnLogMsgBufferSaveTargets_Type()
)
bnLogMsgBufferSaveTargets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgBufferSaveTargets.setStatus("current")


class _BnLogMsgBufferClearTargets_Type(Integer32):
    """Custom type bnLogMsgBufferClearTargets based on Integer32"""
    defaultValue = 4

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
        *(("msgTypeAllVolatile", 4),
          ("msgTypeCritical", 1),
          ("msgTypeInformational", 3),
          ("msgTypeNonVolatile", 5),
          ("msgTypeSerious", 2))
    )


_BnLogMsgBufferClearTargets_Type.__name__ = "Integer32"
_BnLogMsgBufferClearTargets_Object = MibScalar
bnLogMsgBufferClearTargets = _BnLogMsgBufferClearTargets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 6),
    _BnLogMsgBufferClearTargets_Type()
)
bnLogMsgBufferClearTargets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgBufferClearTargets.setStatus("deprecated")


class _BnLogMsgBufferClearMsgs_Type(Integer32):
    """Custom type bnLogMsgBufferClearMsgs based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearMsgs", 1),
          ("savingMsgs", 2))
    )


_BnLogMsgBufferClearMsgs_Type.__name__ = "Integer32"
_BnLogMsgBufferClearMsgs_Object = MibScalar
bnLogMsgBufferClearMsgs = _BnLogMsgBufferClearMsgs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 7),
    _BnLogMsgBufferClearMsgs_Type()
)
bnLogMsgBufferClearMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgBufferClearMsgs.setStatus("deprecated")


class _BnLogMsgBufferNonVolCurSize_Type(Integer32):
    """Custom type bnLogMsgBufferNonVolCurSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_BnLogMsgBufferNonVolCurSize_Type.__name__ = "Integer32"
_BnLogMsgBufferNonVolCurSize_Object = MibScalar
bnLogMsgBufferNonVolCurSize = _BnLogMsgBufferNonVolCurSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 8),
    _BnLogMsgBufferNonVolCurSize_Type()
)
bnLogMsgBufferNonVolCurSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnLogMsgBufferNonVolCurSize.setStatus("current")


class _BnLogMsgBufferNonVolSaveTargets_Type(Integer32):
    """Custom type bnLogMsgBufferNonVolSaveTargets based on Integer32"""
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
        *(("msgTypeCritical", 1),
          ("msgTypeInformational", 3),
          ("msgTypeNone", 4),
          ("msgTypeSerious", 2))
    )


_BnLogMsgBufferNonVolSaveTargets_Type.__name__ = "Integer32"
_BnLogMsgBufferNonVolSaveTargets_Object = MibScalar
bnLogMsgBufferNonVolSaveTargets = _BnLogMsgBufferNonVolSaveTargets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 9),
    _BnLogMsgBufferNonVolSaveTargets_Type()
)
bnLogMsgBufferNonVolSaveTargets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgBufferNonVolSaveTargets.setStatus("current")
_BnLogMsgBufferTable_Object = MibTable
bnLogMsgBufferTable = _BnLogMsgBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10)
)
if mibBuilder.loadTexts:
    bnLogMsgBufferTable.setStatus("current")
_BnLogMsgBufferEntry_Object = MibTableRow
bnLogMsgBufferEntry = _BnLogMsgBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1)
)
bnLogMsgBufferEntry.setIndexNames(
    (0, "BN-LOG-MESSAGE-MIB", "bnLogMsgBufferMsgOrig"),
    (0, "BN-LOG-MESSAGE-MIB", "bnLogMsgBufferMsgTime"),
    (0, "BN-LOG-MESSAGE-MIB", "bnLogMsgBufferMsgIndex"),
)
if mibBuilder.loadTexts:
    bnLogMsgBufferEntry.setStatus("current")


class _BnLogMsgBufferMsgIndex_Type(Integer32):
    """Custom type bnLogMsgBufferMsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BnLogMsgBufferMsgIndex_Type.__name__ = "Integer32"
_BnLogMsgBufferMsgIndex_Object = MibTableColumn
bnLogMsgBufferMsgIndex = _BnLogMsgBufferMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 1),
    _BnLogMsgBufferMsgIndex_Type()
)
bnLogMsgBufferMsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bnLogMsgBufferMsgIndex.setStatus("current")


class _BnLogMsgBufferMsgOrig_Type(Integer32):
    """Custom type bnLogMsgBufferMsgOrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BnLogMsgBufferMsgOrig_Type.__name__ = "Integer32"
_BnLogMsgBufferMsgOrig_Object = MibTableColumn
bnLogMsgBufferMsgOrig = _BnLogMsgBufferMsgOrig_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 2),
    _BnLogMsgBufferMsgOrig_Type()
)
bnLogMsgBufferMsgOrig.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bnLogMsgBufferMsgOrig.setStatus("current")
_BnLogMsgBufferMsgTime_Type = TimeTicks
_BnLogMsgBufferMsgTime_Object = MibTableColumn
bnLogMsgBufferMsgTime = _BnLogMsgBufferMsgTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 3),
    _BnLogMsgBufferMsgTime_Type()
)
bnLogMsgBufferMsgTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bnLogMsgBufferMsgTime.setStatus("current")


class _BnLogMsgBufferMsgSrc_Type(Integer32):
    """Custom type bnLogMsgBufferMsgSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("msgSrcNonVol", 2),
          ("msgSrcRunning", 1))
    )


_BnLogMsgBufferMsgSrc_Type.__name__ = "Integer32"
_BnLogMsgBufferMsgSrc_Object = MibTableColumn
bnLogMsgBufferMsgSrc = _BnLogMsgBufferMsgSrc_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 4),
    _BnLogMsgBufferMsgSrc_Type()
)
bnLogMsgBufferMsgSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnLogMsgBufferMsgSrc.setStatus("current")
_BnLogMsgBufferMsgCode_Type = Integer32
_BnLogMsgBufferMsgCode_Object = MibTableColumn
bnLogMsgBufferMsgCode = _BnLogMsgBufferMsgCode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 5),
    _BnLogMsgBufferMsgCode_Type()
)
bnLogMsgBufferMsgCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnLogMsgBufferMsgCode.setStatus("current")
_BnLogMsgBufferMsgString_Type = DisplayString
_BnLogMsgBufferMsgString_Object = MibTableColumn
bnLogMsgBufferMsgString = _BnLogMsgBufferMsgString_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 6),
    _BnLogMsgBufferMsgString_Type()
)
bnLogMsgBufferMsgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnLogMsgBufferMsgString.setStatus("current")
_BnLogMsgBufferMsgParam1_Type = Integer32
_BnLogMsgBufferMsgParam1_Object = MibTableColumn
bnLogMsgBufferMsgParam1 = _BnLogMsgBufferMsgParam1_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 7),
    _BnLogMsgBufferMsgParam1_Type()
)
bnLogMsgBufferMsgParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnLogMsgBufferMsgParam1.setStatus("current")
_BnLogMsgBufferMsgParam2_Type = Integer32
_BnLogMsgBufferMsgParam2_Object = MibTableColumn
bnLogMsgBufferMsgParam2 = _BnLogMsgBufferMsgParam2_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 8),
    _BnLogMsgBufferMsgParam2_Type()
)
bnLogMsgBufferMsgParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnLogMsgBufferMsgParam2.setStatus("current")
_BnLogMsgBufferMsgParam3_Type = Integer32
_BnLogMsgBufferMsgParam3_Object = MibTableColumn
bnLogMsgBufferMsgParam3 = _BnLogMsgBufferMsgParam3_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 9),
    _BnLogMsgBufferMsgParam3_Type()
)
bnLogMsgBufferMsgParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnLogMsgBufferMsgParam3.setStatus("current")
_BnLogMsgBufferMsgUtcTime_Type = DateAndTime
_BnLogMsgBufferMsgUtcTime_Object = MibTableColumn
bnLogMsgBufferMsgUtcTime = _BnLogMsgBufferMsgUtcTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 10),
    _BnLogMsgBufferMsgUtcTime_Type()
)
bnLogMsgBufferMsgUtcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnLogMsgBufferMsgUtcTime.setStatus("current")


class _BnLogMsgBufferMsgType_Type(Integer32):
    """Custom type bnLogMsgBufferMsgType based on Integer32"""
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
        *(("msgTypeCritical", 1),
          ("msgTypeInformational", 3),
          ("msgTypeNone", 4),
          ("msgTypeSerious", 2))
    )


_BnLogMsgBufferMsgType_Type.__name__ = "Integer32"
_BnLogMsgBufferMsgType_Object = MibTableColumn
bnLogMsgBufferMsgType = _BnLogMsgBufferMsgType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 11),
    _BnLogMsgBufferMsgType_Type()
)
bnLogMsgBufferMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnLogMsgBufferMsgType.setStatus("current")


class _BnLogMsgRemoteSyslogEnabled_Type(TruthValue):
    """Custom type bnLogMsgRemoteSyslogEnabled based on TruthValue"""


_BnLogMsgRemoteSyslogEnabled_Object = MibScalar
bnLogMsgRemoteSyslogEnabled = _BnLogMsgRemoteSyslogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 11),
    _BnLogMsgRemoteSyslogEnabled_Type()
)
bnLogMsgRemoteSyslogEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgRemoteSyslogEnabled.setStatus("current")


class _BnLogMsgRemoteSyslogAddress_Type(IpAddress):
    """Custom type bnLogMsgRemoteSyslogAddress based on IpAddress"""
    defaultHexValue = "00000000"


_BnLogMsgRemoteSyslogAddress_Object = MibScalar
bnLogMsgRemoteSyslogAddress = _BnLogMsgRemoteSyslogAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 12),
    _BnLogMsgRemoteSyslogAddress_Type()
)
bnLogMsgRemoteSyslogAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgRemoteSyslogAddress.setStatus("current")


class _BnLogMsgRemoteSyslogSaveTargets_Type(Integer32):
    """Custom type bnLogMsgRemoteSyslogSaveTargets based on Integer32"""
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
        *(("msgTypeCritical", 1),
          ("msgTypeInformational", 3),
          ("msgTypeNone", 4),
          ("msgTypeSerious", 2))
    )


_BnLogMsgRemoteSyslogSaveTargets_Type.__name__ = "Integer32"
_BnLogMsgRemoteSyslogSaveTargets_Object = MibScalar
bnLogMsgRemoteSyslogSaveTargets = _BnLogMsgRemoteSyslogSaveTargets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 13),
    _BnLogMsgRemoteSyslogSaveTargets_Type()
)
bnLogMsgRemoteSyslogSaveTargets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgRemoteSyslogSaveTargets.setStatus("current")


class _BnLogMsgClearMessageBuffers_Type(Bits):
    """Custom type bnLogMsgClearMessageBuffers based on Bits"""
    namedValues = NamedValues(
        *(("nonVolCritical", 4),
          ("nonVolInformational", 6),
          ("nonVolSerious", 5),
          ("none", 0),
          ("volCritical", 1),
          ("volInformational", 3),
          ("volSerious", 2))
    )

_BnLogMsgClearMessageBuffers_Type.__name__ = "Bits"
_BnLogMsgClearMessageBuffers_Object = MibScalar
bnLogMsgClearMessageBuffers = _BnLogMsgClearMessageBuffers_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 14),
    _BnLogMsgClearMessageBuffers_Type()
)
bnLogMsgClearMessageBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgClearMessageBuffers.setStatus("current")


class _BnLogMsgRemoteSyslogInetAddressType_Type(InetAddressType):
    """Custom type bnLogMsgRemoteSyslogInetAddressType based on InetAddressType"""


_BnLogMsgRemoteSyslogInetAddressType_Object = MibScalar
bnLogMsgRemoteSyslogInetAddressType = _BnLogMsgRemoteSyslogInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 15),
    _BnLogMsgRemoteSyslogInetAddressType_Type()
)
bnLogMsgRemoteSyslogInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgRemoteSyslogInetAddressType.setStatus("current")


class _BnLogMsgRemoteSyslogInetAddress_Type(InetAddress):
    """Custom type bnLogMsgRemoteSyslogInetAddress based on InetAddress"""
    defaultHexValue = ""


_BnLogMsgRemoteSyslogInetAddress_Object = MibScalar
bnLogMsgRemoteSyslogInetAddress = _BnLogMsgRemoteSyslogInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 16),
    _BnLogMsgRemoteSyslogInetAddress_Type()
)
bnLogMsgRemoteSyslogInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgRemoteSyslogInetAddress.setStatus("current")


class _BnLogMsgRemoteSyslogSecondaryInetAddressType_Type(InetAddressType):
    """Custom type bnLogMsgRemoteSyslogSecondaryInetAddressType based on InetAddressType"""


_BnLogMsgRemoteSyslogSecondaryInetAddressType_Object = MibScalar
bnLogMsgRemoteSyslogSecondaryInetAddressType = _BnLogMsgRemoteSyslogSecondaryInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 17),
    _BnLogMsgRemoteSyslogSecondaryInetAddressType_Type()
)
bnLogMsgRemoteSyslogSecondaryInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgRemoteSyslogSecondaryInetAddressType.setStatus("current")


class _BnLogMsgRemoteSyslogSecondaryInetAddress_Type(InetAddress):
    """Custom type bnLogMsgRemoteSyslogSecondaryInetAddress based on InetAddress"""
    defaultHexValue = ""


_BnLogMsgRemoteSyslogSecondaryInetAddress_Object = MibScalar
bnLogMsgRemoteSyslogSecondaryInetAddress = _BnLogMsgRemoteSyslogSecondaryInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 18),
    _BnLogMsgRemoteSyslogSecondaryInetAddress_Type()
)
bnLogMsgRemoteSyslogSecondaryInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgRemoteSyslogSecondaryInetAddress.setStatus("current")
_BnLogMsgRemoteServerTable_Object = MibTable
bnLogMsgRemoteServerTable = _BnLogMsgRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19)
)
if mibBuilder.loadTexts:
    bnLogMsgRemoteServerTable.setStatus("current")
_BnLogMsgRemoteServerEntry_Object = MibTableRow
bnLogMsgRemoteServerEntry = _BnLogMsgRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1)
)
bnLogMsgRemoteServerEntry.setIndexNames(
    (0, "BN-LOG-MESSAGE-MIB", "bnLogMsgRemoteServerAddressType"),
    (0, "BN-LOG-MESSAGE-MIB", "bnLogMsgRemoteServerAddress"),
)
if mibBuilder.loadTexts:
    bnLogMsgRemoteServerEntry.setStatus("current")
_BnLogMsgRemoteServerAddressType_Type = InetAddressType
_BnLogMsgRemoteServerAddressType_Object = MibTableColumn
bnLogMsgRemoteServerAddressType = _BnLogMsgRemoteServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1, 1),
    _BnLogMsgRemoteServerAddressType_Type()
)
bnLogMsgRemoteServerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bnLogMsgRemoteServerAddressType.setStatus("current")


class _BnLogMsgRemoteServerAddress_Type(InetAddress):
    """Custom type bnLogMsgRemoteServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_BnLogMsgRemoteServerAddress_Type.__name__ = "InetAddress"
_BnLogMsgRemoteServerAddress_Object = MibTableColumn
bnLogMsgRemoteServerAddress = _BnLogMsgRemoteServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1, 2),
    _BnLogMsgRemoteServerAddress_Type()
)
bnLogMsgRemoteServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bnLogMsgRemoteServerAddress.setStatus("current")


class _BnLogMsgRemoteServerEnabled_Type(TruthValue):
    """Custom type bnLogMsgRemoteServerEnabled based on TruthValue"""


_BnLogMsgRemoteServerEnabled_Object = MibTableColumn
bnLogMsgRemoteServerEnabled = _BnLogMsgRemoteServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1, 3),
    _BnLogMsgRemoteServerEnabled_Type()
)
bnLogMsgRemoteServerEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bnLogMsgRemoteServerEnabled.setStatus("current")


class _BnLogMsgRemoteServerSaveTargets_Type(Integer32):
    """Custom type bnLogMsgRemoteServerSaveTargets based on Integer32"""
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
        *(("msgTypeCritical", 1),
          ("msgTypeInformational", 3),
          ("msgTypeNone", 4),
          ("msgTypeSerious", 2))
    )


_BnLogMsgRemoteServerSaveTargets_Type.__name__ = "Integer32"
_BnLogMsgRemoteServerSaveTargets_Object = MibTableColumn
bnLogMsgRemoteServerSaveTargets = _BnLogMsgRemoteServerSaveTargets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1, 4),
    _BnLogMsgRemoteServerSaveTargets_Type()
)
bnLogMsgRemoteServerSaveTargets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bnLogMsgRemoteServerSaveTargets.setStatus("current")
_BnLogMsgRemoteServerRowStatus_Type = RowStatus
_BnLogMsgRemoteServerRowStatus_Object = MibTableColumn
bnLogMsgRemoteServerRowStatus = _BnLogMsgRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1, 5),
    _BnLogMsgRemoteServerRowStatus_Type()
)
bnLogMsgRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bnLogMsgRemoteServerRowStatus.setStatus("current")


class _BnLogMsgRemoteServerStandardSaveTargets_Type(Integer32):
    """Custom type bnLogMsgRemoteServerStandardSaveTargets based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("msgTypeAlert", 1),
          ("msgTypeCritical", 2),
          ("msgTypeDebug", 7),
          ("msgTypeEmergency", 0),
          ("msgTypeError", 3),
          ("msgTypeInformational", 6),
          ("msgTypeNone", 8),
          ("msgTypeNotice", 5),
          ("msgTypeSerious", 4))
    )


_BnLogMsgRemoteServerStandardSaveTargets_Type.__name__ = "Integer32"
_BnLogMsgRemoteServerStandardSaveTargets_Object = MibTableColumn
bnLogMsgRemoteServerStandardSaveTargets = _BnLogMsgRemoteServerStandardSaveTargets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1, 6),
    _BnLogMsgRemoteServerStandardSaveTargets_Type()
)
bnLogMsgRemoteServerStandardSaveTargets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bnLogMsgRemoteServerStandardSaveTargets.setStatus("current")


class _BnLogMsgRemoteSyslogFacility_Type(Integer32):
    """Custom type bnLogMsgRemoteSyslogFacility based on Integer32"""
    defaultValue = 4

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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("fltClockDaemon", 10),
          ("fltClockDaemon2", 16),
          ("fltDaemon", 4),
          ("fltFTPDaemon", 12),
          ("fltKernel", 1),
          ("fltLinePrinter", 7),
          ("fltLocal0", 17),
          ("fltLocal1", 18),
          ("fltLocal2", 19),
          ("fltLocal3", 20),
          ("fltLocal4", 21),
          ("fltLocal5", 22),
          ("fltLocal6", 23),
          ("fltLocal7", 24),
          ("fltLogAlert", 15),
          ("fltLogAudit", 14),
          ("fltMailSystem", 3),
          ("fltMsgGenInt", 6),
          ("fltNTP", 13),
          ("fltNetNews", 8),
          ("fltNone", 25),
          ("fltSecAuthor", 5),
          ("fltSecAuthor2", 11),
          ("fltUUCP", 9),
          ("fltUserLevel", 2))
    )


_BnLogMsgRemoteSyslogFacility_Type.__name__ = "Integer32"
_BnLogMsgRemoteSyslogFacility_Object = MibScalar
bnLogMsgRemoteSyslogFacility = _BnLogMsgRemoteSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 20),
    _BnLogMsgRemoteSyslogFacility_Type()
)
bnLogMsgRemoteSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgRemoteSyslogFacility.setStatus("current")


class _BnLogMsgRemoteSyslogStandardSaveTargets_Type(Integer32):
    """Custom type bnLogMsgRemoteSyslogStandardSaveTargets based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("msgTypeAlert", 1),
          ("msgTypeCritical", 2),
          ("msgTypeDebug", 7),
          ("msgTypeEmergency", 0),
          ("msgTypeError", 3),
          ("msgTypeInformational", 6),
          ("msgTypeNone", 8),
          ("msgTypeNotice", 5),
          ("msgTypeSerious", 4))
    )


_BnLogMsgRemoteSyslogStandardSaveTargets_Type.__name__ = "Integer32"
_BnLogMsgRemoteSyslogStandardSaveTargets_Object = MibScalar
bnLogMsgRemoteSyslogStandardSaveTargets = _BnLogMsgRemoteSyslogStandardSaveTargets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 21),
    _BnLogMsgRemoteSyslogStandardSaveTargets_Type()
)
bnLogMsgRemoteSyslogStandardSaveTargets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgRemoteSyslogStandardSaveTargets.setStatus("current")


class _BnLogMsgRemoteSyslogPrimaryTcpPort_Type(Integer32):
    """Custom type bnLogMsgRemoteSyslogPrimaryTcpPort based on Integer32"""
    defaultValue = 601

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(601, 601),
        ValueRangeConstraint(1024, 65535),
    )


_BnLogMsgRemoteSyslogPrimaryTcpPort_Type.__name__ = "Integer32"
_BnLogMsgRemoteSyslogPrimaryTcpPort_Object = MibScalar
bnLogMsgRemoteSyslogPrimaryTcpPort = _BnLogMsgRemoteSyslogPrimaryTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 22),
    _BnLogMsgRemoteSyslogPrimaryTcpPort_Type()
)
bnLogMsgRemoteSyslogPrimaryTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgRemoteSyslogPrimaryTcpPort.setStatus("current")


class _BnLogMsgRemoteSyslogSecondaryTcpPort_Type(Integer32):
    """Custom type bnLogMsgRemoteSyslogSecondaryTcpPort based on Integer32"""
    defaultValue = 601

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(601, 601),
        ValueRangeConstraint(1024, 65535),
    )


_BnLogMsgRemoteSyslogSecondaryTcpPort_Type.__name__ = "Integer32"
_BnLogMsgRemoteSyslogSecondaryTcpPort_Object = MibScalar
bnLogMsgRemoteSyslogSecondaryTcpPort = _BnLogMsgRemoteSyslogSecondaryTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 23),
    _BnLogMsgRemoteSyslogSecondaryTcpPort_Type()
)
bnLogMsgRemoteSyslogSecondaryTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgRemoteSyslogSecondaryTcpPort.setStatus("current")


class _BnLogMsgRemoteSyslogPrimaryConnectionType_Type(Integer32):
    """Custom type bnLogMsgRemoteSyslogPrimaryConnectionType based on Integer32"""
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
        *(("connectionTypeTCP", 2),
          ("connectionTypeTCPSecure", 3),
          ("connectionTypeUDP", 1))
    )


_BnLogMsgRemoteSyslogPrimaryConnectionType_Type.__name__ = "Integer32"
_BnLogMsgRemoteSyslogPrimaryConnectionType_Object = MibScalar
bnLogMsgRemoteSyslogPrimaryConnectionType = _BnLogMsgRemoteSyslogPrimaryConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 24),
    _BnLogMsgRemoteSyslogPrimaryConnectionType_Type()
)
bnLogMsgRemoteSyslogPrimaryConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgRemoteSyslogPrimaryConnectionType.setStatus("current")


class _BnLogMsgRemoteSyslogSecondaryConnectionType_Type(Integer32):
    """Custom type bnLogMsgRemoteSyslogSecondaryConnectionType based on Integer32"""
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
        *(("connectionTypeTCP", 2),
          ("connectionTypeTCPSecure", 3),
          ("connectionTypeUDP", 1))
    )


_BnLogMsgRemoteSyslogSecondaryConnectionType_Type.__name__ = "Integer32"
_BnLogMsgRemoteSyslogSecondaryConnectionType_Object = MibScalar
bnLogMsgRemoteSyslogSecondaryConnectionType = _BnLogMsgRemoteSyslogSecondaryConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 25),
    _BnLogMsgRemoteSyslogSecondaryConnectionType_Type()
)
bnLogMsgRemoteSyslogSecondaryConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnLogMsgRemoteSyslogSecondaryConnectionType.setStatus("current")
_BnLogMsgMIBTraps_ObjectIdentity = ObjectIdentity
bnLogMsgMIBTraps = _BnLogMsgMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 2)
)
_BnLogMsgMIBTrapPrefix_ObjectIdentity = ObjectIdentity
bnLogMsgMIBTrapPrefix = _BnLogMsgMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 2, 0)
)
_BnLogMsgMIBConformance_ObjectIdentity = ObjectIdentity
bnLogMsgMIBConformance = _BnLogMsgMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 3)
)

# Managed Objects groups


# Notification objects

bnLogMsgBufferFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 2, 0, 1)
)
bnLogMsgBufferFull.setObjects(
      *(("BN-LOG-MESSAGE-MIB", "bnLogMsgBufferCurSize"),
        ("BN-LOG-MESSAGE-MIB", "bnLogMsgBufferNonVolCurSize"))
)
if mibBuilder.loadTexts:
    bnLogMsgBufferFull.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BN-LOG-MESSAGE-MIB",
    **{"bnLogMsgMIB": bnLogMsgMIB,
       "bnLogMsgMIBObjects": bnLogMsgMIBObjects,
       "bnLogMsgBufferOperaton": bnLogMsgBufferOperaton,
       "bnLogMsgBufferMaxSize": bnLogMsgBufferMaxSize,
       "bnLogMsgBufferCurSize": bnLogMsgBufferCurSize,
       "bnLogMsgBufferFullAction": bnLogMsgBufferFullAction,
       "bnLogMsgBufferSaveTargets": bnLogMsgBufferSaveTargets,
       "bnLogMsgBufferClearTargets": bnLogMsgBufferClearTargets,
       "bnLogMsgBufferClearMsgs": bnLogMsgBufferClearMsgs,
       "bnLogMsgBufferNonVolCurSize": bnLogMsgBufferNonVolCurSize,
       "bnLogMsgBufferNonVolSaveTargets": bnLogMsgBufferNonVolSaveTargets,
       "bnLogMsgBufferTable": bnLogMsgBufferTable,
       "bnLogMsgBufferEntry": bnLogMsgBufferEntry,
       "bnLogMsgBufferMsgIndex": bnLogMsgBufferMsgIndex,
       "bnLogMsgBufferMsgOrig": bnLogMsgBufferMsgOrig,
       "bnLogMsgBufferMsgTime": bnLogMsgBufferMsgTime,
       "bnLogMsgBufferMsgSrc": bnLogMsgBufferMsgSrc,
       "bnLogMsgBufferMsgCode": bnLogMsgBufferMsgCode,
       "bnLogMsgBufferMsgString": bnLogMsgBufferMsgString,
       "bnLogMsgBufferMsgParam1": bnLogMsgBufferMsgParam1,
       "bnLogMsgBufferMsgParam2": bnLogMsgBufferMsgParam2,
       "bnLogMsgBufferMsgParam3": bnLogMsgBufferMsgParam3,
       "bnLogMsgBufferMsgUtcTime": bnLogMsgBufferMsgUtcTime,
       "bnLogMsgBufferMsgType": bnLogMsgBufferMsgType,
       "bnLogMsgRemoteSyslogEnabled": bnLogMsgRemoteSyslogEnabled,
       "bnLogMsgRemoteSyslogAddress": bnLogMsgRemoteSyslogAddress,
       "bnLogMsgRemoteSyslogSaveTargets": bnLogMsgRemoteSyslogSaveTargets,
       "bnLogMsgClearMessageBuffers": bnLogMsgClearMessageBuffers,
       "bnLogMsgRemoteSyslogInetAddressType": bnLogMsgRemoteSyslogInetAddressType,
       "bnLogMsgRemoteSyslogInetAddress": bnLogMsgRemoteSyslogInetAddress,
       "bnLogMsgRemoteSyslogSecondaryInetAddressType": bnLogMsgRemoteSyslogSecondaryInetAddressType,
       "bnLogMsgRemoteSyslogSecondaryInetAddress": bnLogMsgRemoteSyslogSecondaryInetAddress,
       "bnLogMsgRemoteServerTable": bnLogMsgRemoteServerTable,
       "bnLogMsgRemoteServerEntry": bnLogMsgRemoteServerEntry,
       "bnLogMsgRemoteServerAddressType": bnLogMsgRemoteServerAddressType,
       "bnLogMsgRemoteServerAddress": bnLogMsgRemoteServerAddress,
       "bnLogMsgRemoteServerEnabled": bnLogMsgRemoteServerEnabled,
       "bnLogMsgRemoteServerSaveTargets": bnLogMsgRemoteServerSaveTargets,
       "bnLogMsgRemoteServerRowStatus": bnLogMsgRemoteServerRowStatus,
       "bnLogMsgRemoteServerStandardSaveTargets": bnLogMsgRemoteServerStandardSaveTargets,
       "bnLogMsgRemoteSyslogFacility": bnLogMsgRemoteSyslogFacility,
       "bnLogMsgRemoteSyslogStandardSaveTargets": bnLogMsgRemoteSyslogStandardSaveTargets,
       "bnLogMsgRemoteSyslogPrimaryTcpPort": bnLogMsgRemoteSyslogPrimaryTcpPort,
       "bnLogMsgRemoteSyslogSecondaryTcpPort": bnLogMsgRemoteSyslogSecondaryTcpPort,
       "bnLogMsgRemoteSyslogPrimaryConnectionType": bnLogMsgRemoteSyslogPrimaryConnectionType,
       "bnLogMsgRemoteSyslogSecondaryConnectionType": bnLogMsgRemoteSyslogSecondaryConnectionType,
       "bnLogMsgMIBTraps": bnLogMsgMIBTraps,
       "bnLogMsgMIBTrapPrefix": bnLogMsgMIBTrapPrefix,
       "bnLogMsgBufferFull": bnLogMsgBufferFull,
       "bnLogMsgMIBConformance": bnLogMsgMIBConformance}
)
