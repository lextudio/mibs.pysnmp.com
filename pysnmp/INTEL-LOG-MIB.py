# SNMP MIB module (INTEL-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-LOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:54 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Log_ObjectIdentity = ObjectIdentity
log = _Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 8)
)
_LogInfo_ObjectIdentity = ObjectIdentity
logInfo = _LogInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1)
)
_LogListTable_Object = MibTable
logListTable = _LogListTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1)
)
if mibBuilder.loadTexts:
    logListTable.setStatus("mandatory")
_LogListEntry_Object = MibTableRow
logListEntry = _LogListEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1)
)
logListEntry.setIndexNames(
    (0, "INTEL-LOG-MIB", "logListSeqno"),
)
if mibBuilder.loadTexts:
    logListEntry.setStatus("mandatory")


class _LogListSeqno_Type(OctetString):
    """Custom type logListSeqno based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_LogListSeqno_Type.__name__ = "OctetString"
_LogListSeqno_Object = MibTableColumn
logListSeqno = _LogListSeqno_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 1),
    _LogListSeqno_Type()
)
logListSeqno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListSeqno.setStatus("mandatory")
_LogListCode_Type = Integer32
_LogListCode_Object = MibTableColumn
logListCode = _LogListCode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 2),
    _LogListCode_Type()
)
logListCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListCode.setStatus("mandatory")


class _LogListSource_Type(Integer32):
    """Custom type logListSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
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
        *(("bridging", 25),
          ("callcontrol", 9),
          ("csu", 15),
          ("framerelay", 10),
          ("gmrp", 23),
          ("hdlc", 16),
          ("ip", 7),
          ("ipm", 19),
          ("ipru", 22),
          ("ipx", 6),
          ("isdn", 8),
          ("l3l", 21),
          ("lapb", 24),
          ("link", 12),
          ("misc", 1),
          ("modem", 18),
          ("ppp", 11),
          ("rsvp", 20),
          ("syslogd", 3),
          ("system", 2),
          ("tunnel", 13),
          ("wanPort", 17),
          ("x25", 14))
    )


_LogListSource_Type.__name__ = "Integer32"
_LogListSource_Object = MibTableColumn
logListSource = _LogListSource_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 3),
    _LogListSource_Type()
)
logListSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListSource.setStatus("mandatory")


class _LogListCategory_Type(OctetString):
    """Custom type logListCategory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_LogListCategory_Type.__name__ = "OctetString"
_LogListCategory_Object = MibTableColumn
logListCategory = _LogListCategory_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 4),
    _LogListCategory_Type()
)
logListCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListCategory.setStatus("mandatory")


class _LogListLevel_Type(Integer32):
    """Custom type logListLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(30,
              40,
              50,
              60,
              70,
              100)
        )
    )
    namedValues = NamedValues(
        *(("debug", 30),
          ("error", 70),
          ("fatalError", 100),
          ("info", 40),
          ("note", 50),
          ("warning", 60))
    )


_LogListLevel_Type.__name__ = "Integer32"
_LogListLevel_Object = MibTableColumn
logListLevel = _LogListLevel_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 5),
    _LogListLevel_Type()
)
logListLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListLevel.setStatus("mandatory")
_LogListTimeStamp_Type = TimeTicks
_LogListTimeStamp_Object = MibTableColumn
logListTimeStamp = _LogListTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 6),
    _LogListTimeStamp_Type()
)
logListTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListTimeStamp.setStatus("mandatory")


class _LogListMulti_Type(OctetString):
    """Custom type logListMulti based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_LogListMulti_Type.__name__ = "OctetString"
_LogListMulti_Object = MibTableColumn
logListMulti = _LogListMulti_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 7),
    _LogListMulti_Type()
)
logListMulti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListMulti.setStatus("mandatory")


class _LogListText1_Type(DisplayString):
    """Custom type logListText1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(250, 250),
    )


_LogListText1_Type.__name__ = "DisplayString"
_LogListText1_Object = MibTableColumn
logListText1 = _LogListText1_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 8),
    _LogListText1_Type()
)
logListText1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListText1.setStatus("mandatory")


class _LogListText2_Type(DisplayString):
    """Custom type logListText2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(250, 250),
    )


_LogListText2_Type.__name__ = "DisplayString"
_LogListText2_Object = MibTableColumn
logListText2 = _LogListText2_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 9),
    _LogListText2_Type()
)
logListText2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListText2.setStatus("mandatory")


class _LogListText3_Type(DisplayString):
    """Custom type logListText3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(250, 250),
    )


_LogListText3_Type.__name__ = "DisplayString"
_LogListText3_Object = MibTableColumn
logListText3 = _LogListText3_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 10),
    _LogListText3_Type()
)
logListText3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListText3.setStatus("mandatory")


class _LogListText4_Type(DisplayString):
    """Custom type logListText4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(250, 250),
    )


_LogListText4_Type.__name__ = "DisplayString"
_LogListText4_Object = MibTableColumn
logListText4 = _LogListText4_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 11),
    _LogListText4_Type()
)
logListText4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListText4.setStatus("mandatory")
_LogListChassis_Type = Integer32
_LogListChassis_Object = MibTableColumn
logListChassis = _LogListChassis_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 12),
    _LogListChassis_Type()
)
logListChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListChassis.setStatus("mandatory")
_LogListModule_Type = Integer32
_LogListModule_Object = MibTableColumn
logListModule = _LogListModule_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 13),
    _LogListModule_Type()
)
logListModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListModule.setStatus("mandatory")
_LogListPort_Type = Integer32
_LogListPort_Object = MibTableColumn
logListPort = _LogListPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 14),
    _LogListPort_Type()
)
logListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListPort.setStatus("mandatory")
_LogListExtFlags_Type = Integer32
_LogListExtFlags_Object = MibTableColumn
logListExtFlags = _LogListExtFlags_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 15),
    _LogListExtFlags_Type()
)
logListExtFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logListExtFlags.setStatus("mandatory")
_LogListRepeats_Type = Counter32
_LogListRepeats_Object = MibTableColumn
logListRepeats = _LogListRepeats_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 1, 1, 16),
    _LogListRepeats_Type()
)
logListRepeats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListRepeats.setStatus("mandatory")
_LogArgListTable_Object = MibTable
logArgListTable = _LogArgListTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 2)
)
if mibBuilder.loadTexts:
    logArgListTable.setStatus("mandatory")
_LogArgListEntry_Object = MibTableRow
logArgListEntry = _LogArgListEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 2, 1)
)
logArgListEntry.setIndexNames(
    (0, "INTEL-LOG-MIB", "logArgListSeqno"),
    (0, "INTEL-LOG-MIB", "logArgListArgNumber"),
)
if mibBuilder.loadTexts:
    logArgListEntry.setStatus("mandatory")


class _LogArgListSeqno_Type(OctetString):
    """Custom type logArgListSeqno based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_LogArgListSeqno_Type.__name__ = "OctetString"
_LogArgListSeqno_Object = MibTableColumn
logArgListSeqno = _LogArgListSeqno_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 2, 1, 1),
    _LogArgListSeqno_Type()
)
logArgListSeqno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logArgListSeqno.setStatus("mandatory")


class _LogArgListArgNumber_Type(OctetString):
    """Custom type logArgListArgNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LogArgListArgNumber_Type.__name__ = "OctetString"
_LogArgListArgNumber_Object = MibTableColumn
logArgListArgNumber = _LogArgListArgNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 2, 1, 2),
    _LogArgListArgNumber_Type()
)
logArgListArgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logArgListArgNumber.setStatus("mandatory")


class _LogArgListArg_Type(DisplayString):
    """Custom type logArgListArg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LogArgListArg_Type.__name__ = "DisplayString"
_LogArgListArg_Object = MibTableColumn
logArgListArg = _LogArgListArg_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 2, 1, 3),
    _LogArgListArg_Type()
)
logArgListArg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logArgListArg.setStatus("mandatory")
_LogMgmtTable_Object = MibTable
logMgmtTable = _LogMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 3)
)
if mibBuilder.loadTexts:
    logMgmtTable.setStatus("mandatory")
_LogMgmtEntry_Object = MibTableRow
logMgmtEntry = _LogMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 3, 1)
)
logMgmtEntry.setIndexNames(
    (0, "INTEL-LOG-MIB", "logMgmtIpAddress"),
)
if mibBuilder.loadTexts:
    logMgmtEntry.setStatus("mandatory")


class _LogMgmtIpAddress_Type(OctetString):
    """Custom type logMgmtIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LogMgmtIpAddress_Type.__name__ = "OctetString"
_LogMgmtIpAddress_Object = MibTableColumn
logMgmtIpAddress = _LogMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 3, 1, 1),
    _LogMgmtIpAddress_Type()
)
logMgmtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMgmtIpAddress.setStatus("mandatory")


class _LogMgmtSeqno_Type(OctetString):
    """Custom type logMgmtSeqno based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_LogMgmtSeqno_Type.__name__ = "OctetString"
_LogMgmtSeqno_Object = MibTableColumn
logMgmtSeqno = _LogMgmtSeqno_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 3, 1, 2),
    _LogMgmtSeqno_Type()
)
logMgmtSeqno.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMgmtSeqno.setStatus("mandatory")
_LogListEntryCount_Type = Integer32
_LogListEntryCount_Object = MibScalar
logListEntryCount = _LogListEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 4),
    _LogListEntryCount_Type()
)
logListEntryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logListEntryCount.setStatus("mandatory")


class _LogListFirstSeqno_Type(OctetString):
    """Custom type logListFirstSeqno based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_LogListFirstSeqno_Type.__name__ = "OctetString"
_LogListFirstSeqno_Object = MibScalar
logListFirstSeqno = _LogListFirstSeqno_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 5),
    _LogListFirstSeqno_Type()
)
logListFirstSeqno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListFirstSeqno.setStatus("mandatory")


class _LogListLastSeqno_Type(OctetString):
    """Custom type logListLastSeqno based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_LogListLastSeqno_Type.__name__ = "OctetString"
_LogListLastSeqno_Object = MibScalar
logListLastSeqno = _LogListLastSeqno_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 6),
    _LogListLastSeqno_Type()
)
logListLastSeqno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListLastSeqno.setStatus("mandatory")
_LogListLastUpdateTime_Type = TimeTicks
_LogListLastUpdateTime_Object = MibScalar
logListLastUpdateTime = _LogListLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 8, 1, 7),
    _LogListLastUpdateTime_Type()
)
logListLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logListLastUpdateTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-LOG-MIB",
    **{"log": log,
       "logInfo": logInfo,
       "logListTable": logListTable,
       "logListEntry": logListEntry,
       "logListSeqno": logListSeqno,
       "logListCode": logListCode,
       "logListSource": logListSource,
       "logListCategory": logListCategory,
       "logListLevel": logListLevel,
       "logListTimeStamp": logListTimeStamp,
       "logListMulti": logListMulti,
       "logListText1": logListText1,
       "logListText2": logListText2,
       "logListText3": logListText3,
       "logListText4": logListText4,
       "logListChassis": logListChassis,
       "logListModule": logListModule,
       "logListPort": logListPort,
       "logListExtFlags": logListExtFlags,
       "logListRepeats": logListRepeats,
       "logArgListTable": logArgListTable,
       "logArgListEntry": logArgListEntry,
       "logArgListSeqno": logArgListSeqno,
       "logArgListArgNumber": logArgListArgNumber,
       "logArgListArg": logArgListArg,
       "logMgmtTable": logMgmtTable,
       "logMgmtEntry": logMgmtEntry,
       "logMgmtIpAddress": logMgmtIpAddress,
       "logMgmtSeqno": logMgmtSeqno,
       "logListEntryCount": logListEntryCount,
       "logListFirstSeqno": logListFirstSeqno,
       "logListLastSeqno": logListLastSeqno,
       "logListLastUpdateTime": logListLastUpdateTime}
)
