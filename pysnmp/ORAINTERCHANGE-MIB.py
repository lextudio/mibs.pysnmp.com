# SNMP MIB module (ORAINTERCHANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ORAINTERCHANGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:38 2024
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

(applIndex,) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "applIndex")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oracle_ObjectIdentity = ObjectIdentity
oracle = _Oracle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111)
)
_OraInterchangeMIB_ObjectIdentity = ObjectIdentity
oraInterchangeMIB = _OraInterchangeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 7)
)
_OraInterchangeObjects_ObjectIdentity = ObjectIdentity
oraInterchangeObjects = _OraInterchangeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 7, 1)
)
_OraInterchgTable_Object = MibTable
oraInterchgTable = _OraInterchgTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 1)
)
if mibBuilder.loadTexts:
    oraInterchgTable.setStatus("mandatory")
_OraInterchgEntry_Object = MibTableRow
oraInterchgEntry = _OraInterchgEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 1, 1)
)
oraInterchgEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    oraInterchgEntry.setStatus("mandatory")
_OraInterchgConfigDirectory_Type = DisplayString
_OraInterchgConfigDirectory_Object = MibTableColumn
oraInterchgConfigDirectory = _OraInterchgConfigDirectory_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 1, 1, 1),
    _OraInterchgConfigDirectory_Type()
)
oraInterchgConfigDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraInterchgConfigDirectory.setStatus("mandatory")
_OraInterchgContactInfo_Type = DisplayString
_OraInterchgContactInfo_Object = MibTableColumn
oraInterchgContactInfo = _OraInterchgContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 1, 1, 2),
    _OraInterchgContactInfo_Type()
)
oraInterchgContactInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraInterchgContactInfo.setStatus("mandatory")
_OraNavigatorTable_Object = MibTable
oraNavigatorTable = _OraNavigatorTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2)
)
if mibBuilder.loadTexts:
    oraNavigatorTable.setStatus("mandatory")
_OraNavigatorEntry_Object = MibTableRow
oraNavigatorEntry = _OraNavigatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1)
)
oraNavigatorEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    oraNavigatorEntry.setStatus("mandatory")
_OraNavigatorRunningTime_Type = DisplayString
_OraNavigatorRunningTime_Object = MibTableColumn
oraNavigatorRunningTime = _OraNavigatorRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 1),
    _OraNavigatorRunningTime_Type()
)
oraNavigatorRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorRunningTime.setStatus("mandatory")


class _OraNavigatorLogging_Type(Integer32):
    """Custom type oraNavigatorLogging based on Integer32"""
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


_OraNavigatorLogging_Type.__name__ = "Integer32"
_OraNavigatorLogging_Object = MibTableColumn
oraNavigatorLogging = _OraNavigatorLogging_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 2),
    _OraNavigatorLogging_Type()
)
oraNavigatorLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNavigatorLogging.setStatus("mandatory")


class _OraNavigatorLoggingLevel_Type(Integer32):
    """Custom type oraNavigatorLoggingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("errors", 2))
    )


_OraNavigatorLoggingLevel_Type.__name__ = "Integer32"
_OraNavigatorLoggingLevel_Object = MibTableColumn
oraNavigatorLoggingLevel = _OraNavigatorLoggingLevel_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 3),
    _OraNavigatorLoggingLevel_Type()
)
oraNavigatorLoggingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNavigatorLoggingLevel.setStatus("mandatory")
_OraNavigatorLogFile_Type = DisplayString
_OraNavigatorLogFile_Object = MibTableColumn
oraNavigatorLogFile = _OraNavigatorLogFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 4),
    _OraNavigatorLogFile_Type()
)
oraNavigatorLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorLogFile.setStatus("mandatory")


class _OraNavigatorTraceLevel_Type(Integer32):
    """Custom type oraNavigatorTraceLevel based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("admin", 6),
          ("level1", 1),
          ("level10", 10),
          ("level11", 11),
          ("level12", 12),
          ("level13", 13),
          ("level14", 14),
          ("level15", 15),
          ("level16", 16),
          ("level2", 2),
          ("level3", 3),
          ("level5", 5),
          ("level7", 7),
          ("level8", 8),
          ("level9", 9),
          ("off", 17),
          ("user", 4))
    )


_OraNavigatorTraceLevel_Type.__name__ = "Integer32"
_OraNavigatorTraceLevel_Object = MibTableColumn
oraNavigatorTraceLevel = _OraNavigatorTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 5),
    _OraNavigatorTraceLevel_Type()
)
oraNavigatorTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNavigatorTraceLevel.setStatus("mandatory")
_OraNavigatorTraceFile_Type = DisplayString
_OraNavigatorTraceFile_Object = MibTableColumn
oraNavigatorTraceFile = _OraNavigatorTraceFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 6),
    _OraNavigatorTraceFile_Type()
)
oraNavigatorTraceFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorTraceFile.setStatus("mandatory")


class _OraNavigatorStoppable_Type(Integer32):
    """Custom type oraNavigatorStoppable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_OraNavigatorStoppable_Type.__name__ = "Integer32"
_OraNavigatorStoppable_Object = MibTableColumn
oraNavigatorStoppable = _OraNavigatorStoppable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 7),
    _OraNavigatorStoppable_Type()
)
oraNavigatorStoppable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraNavigatorStoppable.setStatus("mandatory")
_OraNavigatorAccumulatedSuccessfulRequests_Type = Counter32
_OraNavigatorAccumulatedSuccessfulRequests_Object = MibTableColumn
oraNavigatorAccumulatedSuccessfulRequests = _OraNavigatorAccumulatedSuccessfulRequests_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 8),
    _OraNavigatorAccumulatedSuccessfulRequests_Type()
)
oraNavigatorAccumulatedSuccessfulRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorAccumulatedSuccessfulRequests.setStatus("mandatory")
_OraNavigatorAccumulatedFailedRequests_Type = Counter32
_OraNavigatorAccumulatedFailedRequests_Object = MibTableColumn
oraNavigatorAccumulatedFailedRequests = _OraNavigatorAccumulatedFailedRequests_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 9),
    _OraNavigatorAccumulatedFailedRequests_Type()
)
oraNavigatorAccumulatedFailedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorAccumulatedFailedRequests.setStatus("mandatory")


class _OraNavigatorState_Type(Integer32):
    """Custom type oraNavigatorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_OraNavigatorState_Type.__name__ = "Integer32"
_OraNavigatorState_Object = MibTableColumn
oraNavigatorState = _OraNavigatorState_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 10),
    _OraNavigatorState_Type()
)
oraNavigatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorState.setStatus("mandatory")
_OraNavigatorErrors_Type = DisplayString
_OraNavigatorErrors_Object = MibTableColumn
oraNavigatorErrors = _OraNavigatorErrors_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 11),
    _OraNavigatorErrors_Type()
)
oraNavigatorErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorErrors.setStatus("mandatory")
_OraNavigatorErrorMessage_Type = DisplayString
_OraNavigatorErrorMessage_Object = MibTableColumn
oraNavigatorErrorMessage = _OraNavigatorErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 2, 1, 12),
    _OraNavigatorErrorMessage_Type()
)
oraNavigatorErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorErrorMessage.setStatus("mandatory")
_OraNavigatorListenAddressTable_Object = MibTable
oraNavigatorListenAddressTable = _OraNavigatorListenAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 3)
)
if mibBuilder.loadTexts:
    oraNavigatorListenAddressTable.setStatus("mandatory")
_OraNavigatorListenAddressEntry_Object = MibTableRow
oraNavigatorListenAddressEntry = _OraNavigatorListenAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 3, 1)
)
oraNavigatorListenAddressEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "ORAINTERCHANGE-MIB", "oraNavigatorListenAddressIndex"),
)
if mibBuilder.loadTexts:
    oraNavigatorListenAddressEntry.setStatus("mandatory")
_OraNavigatorListenAddressIndex_Type = Integer32
_OraNavigatorListenAddressIndex_Object = MibTableColumn
oraNavigatorListenAddressIndex = _OraNavigatorListenAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 3, 1, 1),
    _OraNavigatorListenAddressIndex_Type()
)
oraNavigatorListenAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorListenAddressIndex.setStatus("mandatory")
_OraNavigatorListenAddress_Type = DisplayString
_OraNavigatorListenAddress_Object = MibTableColumn
oraNavigatorListenAddress = _OraNavigatorListenAddress_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 3, 1, 2),
    _OraNavigatorListenAddress_Type()
)
oraNavigatorListenAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorListenAddress.setStatus("mandatory")
_OraNavigatorFailedAddressTable_Object = MibTable
oraNavigatorFailedAddressTable = _OraNavigatorFailedAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 4)
)
if mibBuilder.loadTexts:
    oraNavigatorFailedAddressTable.setStatus("mandatory")
_OraNavigatorFailedAddressEntry_Object = MibTableRow
oraNavigatorFailedAddressEntry = _OraNavigatorFailedAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 4, 1)
)
oraNavigatorFailedAddressEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "ORAINTERCHANGE-MIB", "oraNavigatorFailedAddressIndex"),
)
if mibBuilder.loadTexts:
    oraNavigatorFailedAddressEntry.setStatus("mandatory")
_OraNavigatorFailedAddressIndex_Type = Integer32
_OraNavigatorFailedAddressIndex_Object = MibTableColumn
oraNavigatorFailedAddressIndex = _OraNavigatorFailedAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 4, 1, 1),
    _OraNavigatorFailedAddressIndex_Type()
)
oraNavigatorFailedAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorFailedAddressIndex.setStatus("mandatory")
_OraNavigatorFailedAddress_Type = DisplayString
_OraNavigatorFailedAddress_Object = MibTableColumn
oraNavigatorFailedAddress = _OraNavigatorFailedAddress_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 4, 1, 2),
    _OraNavigatorFailedAddress_Type()
)
oraNavigatorFailedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorFailedAddress.setStatus("mandatory")
_OraNavigatorRouteAddressTable_Object = MibTable
oraNavigatorRouteAddressTable = _OraNavigatorRouteAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 5)
)
if mibBuilder.loadTexts:
    oraNavigatorRouteAddressTable.setStatus("mandatory")
_OraNavigatorRouteAddressEntry_Object = MibTableRow
oraNavigatorRouteAddressEntry = _OraNavigatorRouteAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 5, 1)
)
oraNavigatorRouteAddressEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "ORAINTERCHANGE-MIB", "oraNavigatorRouteAddressIndex"),
)
if mibBuilder.loadTexts:
    oraNavigatorRouteAddressEntry.setStatus("mandatory")
_OraNavigatorRouteAddressIndex_Type = Integer32
_OraNavigatorRouteAddressIndex_Object = MibTableColumn
oraNavigatorRouteAddressIndex = _OraNavigatorRouteAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 5, 1, 1),
    _OraNavigatorRouteAddressIndex_Type()
)
oraNavigatorRouteAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorRouteAddressIndex.setStatus("mandatory")
_OraNavigatorRouteAddress_Type = DisplayString
_OraNavigatorRouteAddress_Object = MibTableColumn
oraNavigatorRouteAddress = _OraNavigatorRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 5, 1, 2),
    _OraNavigatorRouteAddress_Type()
)
oraNavigatorRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraNavigatorRouteAddress.setStatus("mandatory")
_OraCmanagerTable_Object = MibTable
oraCmanagerTable = _OraCmanagerTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6)
)
if mibBuilder.loadTexts:
    oraCmanagerTable.setStatus("mandatory")
_OraCmanagerEntry_Object = MibTableRow
oraCmanagerEntry = _OraCmanagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1)
)
oraCmanagerEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    oraCmanagerEntry.setStatus("mandatory")
_OraCmanagerStartTime_Type = DisplayString
_OraCmanagerStartTime_Object = MibTableColumn
oraCmanagerStartTime = _OraCmanagerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 1),
    _OraCmanagerStartTime_Type()
)
oraCmanagerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerStartTime.setStatus("mandatory")
_OraCmanagerRunningTime_Type = DisplayString
_OraCmanagerRunningTime_Object = MibTableColumn
oraCmanagerRunningTime = _OraCmanagerRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 2),
    _OraCmanagerRunningTime_Type()
)
oraCmanagerRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerRunningTime.setStatus("mandatory")


class _OraCmanagerLogging_Type(Integer32):
    """Custom type oraCmanagerLogging based on Integer32"""
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


_OraCmanagerLogging_Type.__name__ = "Integer32"
_OraCmanagerLogging_Object = MibTableColumn
oraCmanagerLogging = _OraCmanagerLogging_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 3),
    _OraCmanagerLogging_Type()
)
oraCmanagerLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraCmanagerLogging.setStatus("mandatory")
_OraCmanagerLogFile_Type = DisplayString
_OraCmanagerLogFile_Object = MibTableColumn
oraCmanagerLogFile = _OraCmanagerLogFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 4),
    _OraCmanagerLogFile_Type()
)
oraCmanagerLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerLogFile.setStatus("mandatory")


class _OraCmanagerTraceLevel_Type(Integer32):
    """Custom type oraCmanagerTraceLevel based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("admin", 6),
          ("level1", 1),
          ("level10", 10),
          ("level11", 11),
          ("level12", 12),
          ("level13", 13),
          ("level14", 14),
          ("level15", 15),
          ("level16", 16),
          ("level2", 2),
          ("level3", 3),
          ("level5", 5),
          ("level7", 7),
          ("level8", 8),
          ("level9", 9),
          ("off", 17),
          ("user", 4))
    )


_OraCmanagerTraceLevel_Type.__name__ = "Integer32"
_OraCmanagerTraceLevel_Object = MibTableColumn
oraCmanagerTraceLevel = _OraCmanagerTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 5),
    _OraCmanagerTraceLevel_Type()
)
oraCmanagerTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraCmanagerTraceLevel.setStatus("mandatory")
_OraCmanagerTraceFile_Type = DisplayString
_OraCmanagerTraceFile_Object = MibTableColumn
oraCmanagerTraceFile = _OraCmanagerTraceFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 6),
    _OraCmanagerTraceFile_Type()
)
oraCmanagerTraceFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerTraceFile.setStatus("mandatory")


class _OraCmanagerStoppable_Type(Integer32):
    """Custom type oraCmanagerStoppable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_OraCmanagerStoppable_Type.__name__ = "Integer32"
_OraCmanagerStoppable_Object = MibTableColumn
oraCmanagerStoppable = _OraCmanagerStoppable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 7),
    _OraCmanagerStoppable_Type()
)
oraCmanagerStoppable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraCmanagerStoppable.setStatus("mandatory")
_OraCmanagerMaximumPumps_Type = Integer32
_OraCmanagerMaximumPumps_Object = MibTableColumn
oraCmanagerMaximumPumps = _OraCmanagerMaximumPumps_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 8),
    _OraCmanagerMaximumPumps_Type()
)
oraCmanagerMaximumPumps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraCmanagerMaximumPumps.setStatus("mandatory")
_OraCmanagerMaximumConnectionsPerPump_Type = Integer32
_OraCmanagerMaximumConnectionsPerPump_Object = MibTableColumn
oraCmanagerMaximumConnectionsPerPump = _OraCmanagerMaximumConnectionsPerPump_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 9),
    _OraCmanagerMaximumConnectionsPerPump_Type()
)
oraCmanagerMaximumConnectionsPerPump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraCmanagerMaximumConnectionsPerPump.setStatus("mandatory")


class _OraCmanagerPumpStrategy_Type(Integer32):
    """Custom type oraCmanagerPumpStrategy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("distribute", 1),
          ("group", 2))
    )


_OraCmanagerPumpStrategy_Type.__name__ = "Integer32"
_OraCmanagerPumpStrategy_Object = MibTableColumn
oraCmanagerPumpStrategy = _OraCmanagerPumpStrategy_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 10),
    _OraCmanagerPumpStrategy_Type()
)
oraCmanagerPumpStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraCmanagerPumpStrategy.setStatus("mandatory")
_OraCmanagerActivePumps_Type = Gauge32
_OraCmanagerActivePumps_Object = MibTableColumn
oraCmanagerActivePumps = _OraCmanagerActivePumps_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 11),
    _OraCmanagerActivePumps_Type()
)
oraCmanagerActivePumps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerActivePumps.setStatus("mandatory")
_OraCmanagerMaximumConnections_Type = Integer32
_OraCmanagerMaximumConnections_Object = MibTableColumn
oraCmanagerMaximumConnections = _OraCmanagerMaximumConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 12),
    _OraCmanagerMaximumConnections_Type()
)
oraCmanagerMaximumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerMaximumConnections.setStatus("mandatory")
_OraCmanagerCurrentConnectionsInUse_Type = Gauge32
_OraCmanagerCurrentConnectionsInUse_Object = MibTableColumn
oraCmanagerCurrentConnectionsInUse = _OraCmanagerCurrentConnectionsInUse_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 13),
    _OraCmanagerCurrentConnectionsInUse_Type()
)
oraCmanagerCurrentConnectionsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerCurrentConnectionsInUse.setStatus("mandatory")
_OraCmanagerAccumulatedSuccessfulConnections_Type = Counter32
_OraCmanagerAccumulatedSuccessfulConnections_Object = MibTableColumn
oraCmanagerAccumulatedSuccessfulConnections = _OraCmanagerAccumulatedSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 14),
    _OraCmanagerAccumulatedSuccessfulConnections_Type()
)
oraCmanagerAccumulatedSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerAccumulatedSuccessfulConnections.setStatus("mandatory")
_OraCmanagerAccumulatedFailedConnections_Type = Counter32
_OraCmanagerAccumulatedFailedConnections_Object = MibTableColumn
oraCmanagerAccumulatedFailedConnections = _OraCmanagerAccumulatedFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 15),
    _OraCmanagerAccumulatedFailedConnections_Type()
)
oraCmanagerAccumulatedFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerAccumulatedFailedConnections.setStatus("mandatory")
_OraCmanagerImmediateAverageBytes_Type = Integer32
_OraCmanagerImmediateAverageBytes_Object = MibTableColumn
oraCmanagerImmediateAverageBytes = _OraCmanagerImmediateAverageBytes_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 16),
    _OraCmanagerImmediateAverageBytes_Type()
)
oraCmanagerImmediateAverageBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerImmediateAverageBytes.setStatus("mandatory")
_OraCmanagerMaximumConnectTime_Type = Integer32
_OraCmanagerMaximumConnectTime_Object = MibTableColumn
oraCmanagerMaximumConnectTime = _OraCmanagerMaximumConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 17),
    _OraCmanagerMaximumConnectTime_Type()
)
oraCmanagerMaximumConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerMaximumConnectTime.setStatus("mandatory")
_OraCmanagerMinimumConnectTime_Type = Integer32
_OraCmanagerMinimumConnectTime_Object = MibTableColumn
oraCmanagerMinimumConnectTime = _OraCmanagerMinimumConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 18),
    _OraCmanagerMinimumConnectTime_Type()
)
oraCmanagerMinimumConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerMinimumConnectTime.setStatus("mandatory")
_OraCmanagerAverageConnectTime_Type = Integer32
_OraCmanagerAverageConnectTime_Object = MibTableColumn
oraCmanagerAverageConnectTime = _OraCmanagerAverageConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 19),
    _OraCmanagerAverageConnectTime_Type()
)
oraCmanagerAverageConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerAverageConnectTime.setStatus("mandatory")
_OraCmanagerMaximumConnectDuration_Type = Integer32
_OraCmanagerMaximumConnectDuration_Object = MibTableColumn
oraCmanagerMaximumConnectDuration = _OraCmanagerMaximumConnectDuration_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 20),
    _OraCmanagerMaximumConnectDuration_Type()
)
oraCmanagerMaximumConnectDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerMaximumConnectDuration.setStatus("mandatory")


class _OraCmanagerState_Type(Integer32):
    """Custom type oraCmanagerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_OraCmanagerState_Type.__name__ = "Integer32"
_OraCmanagerState_Object = MibTableColumn
oraCmanagerState = _OraCmanagerState_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 21),
    _OraCmanagerState_Type()
)
oraCmanagerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerState.setStatus("mandatory")
_OraCmanagerErrors_Type = DisplayString
_OraCmanagerErrors_Object = MibTableColumn
oraCmanagerErrors = _OraCmanagerErrors_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 22),
    _OraCmanagerErrors_Type()
)
oraCmanagerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerErrors.setStatus("mandatory")
_OraCmanagerErrorMessage_Type = DisplayString
_OraCmanagerErrorMessage_Object = MibTableColumn
oraCmanagerErrorMessage = _OraCmanagerErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 6, 1, 23),
    _OraCmanagerErrorMessage_Type()
)
oraCmanagerErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerErrorMessage.setStatus("mandatory")
_OraCmanagerListenAddressTable_Object = MibTable
oraCmanagerListenAddressTable = _OraCmanagerListenAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 7)
)
if mibBuilder.loadTexts:
    oraCmanagerListenAddressTable.setStatus("mandatory")
_OraCmanagerListenAddressEntry_Object = MibTableRow
oraCmanagerListenAddressEntry = _OraCmanagerListenAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 7, 1)
)
oraCmanagerListenAddressEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "ORAINTERCHANGE-MIB", "oraCmanagerListenAddressIndex"),
)
if mibBuilder.loadTexts:
    oraCmanagerListenAddressEntry.setStatus("mandatory")
_OraCmanagerListenAddressIndex_Type = Integer32
_OraCmanagerListenAddressIndex_Object = MibTableColumn
oraCmanagerListenAddressIndex = _OraCmanagerListenAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 7, 1, 1),
    _OraCmanagerListenAddressIndex_Type()
)
oraCmanagerListenAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerListenAddressIndex.setStatus("mandatory")
_OraCmanagerListenAddress_Type = DisplayString
_OraCmanagerListenAddress_Object = MibTableColumn
oraCmanagerListenAddress = _OraCmanagerListenAddress_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 7, 1, 2),
    _OraCmanagerListenAddress_Type()
)
oraCmanagerListenAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerListenAddress.setStatus("mandatory")
_OraCmanagerFailedAddressTable_Object = MibTable
oraCmanagerFailedAddressTable = _OraCmanagerFailedAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 8)
)
if mibBuilder.loadTexts:
    oraCmanagerFailedAddressTable.setStatus("mandatory")
_OraCmanagerFailedAddressEntry_Object = MibTableRow
oraCmanagerFailedAddressEntry = _OraCmanagerFailedAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 8, 1)
)
oraCmanagerFailedAddressEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "ORAINTERCHANGE-MIB", "oraCmanagerFailedAddressIndex"),
)
if mibBuilder.loadTexts:
    oraCmanagerFailedAddressEntry.setStatus("mandatory")
_OraCmanagerFailedAddressIndex_Type = Integer32
_OraCmanagerFailedAddressIndex_Object = MibTableColumn
oraCmanagerFailedAddressIndex = _OraCmanagerFailedAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 8, 1, 1),
    _OraCmanagerFailedAddressIndex_Type()
)
oraCmanagerFailedAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerFailedAddressIndex.setStatus("mandatory")
_OraCmanagerFailedAddress_Type = DisplayString
_OraCmanagerFailedAddress_Object = MibTableColumn
oraCmanagerFailedAddress = _OraCmanagerFailedAddress_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 8, 1, 2),
    _OraCmanagerFailedAddress_Type()
)
oraCmanagerFailedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraCmanagerFailedAddress.setStatus("mandatory")
_OraPumpTable_Object = MibTable
oraPumpTable = _OraPumpTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9)
)
if mibBuilder.loadTexts:
    oraPumpTable.setStatus("mandatory")
_OraPumpEntry_Object = MibTableRow
oraPumpEntry = _OraPumpEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1)
)
oraPumpEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "ORAINTERCHANGE-MIB", "oraPumpIndex"),
)
if mibBuilder.loadTexts:
    oraPumpEntry.setStatus("mandatory")
_OraPumpIndex_Type = Integer32
_OraPumpIndex_Object = MibTableColumn
oraPumpIndex = _OraPumpIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 1),
    _OraPumpIndex_Type()
)
oraPumpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpIndex.setStatus("mandatory")
_OraPumpActiveTime_Type = Integer32
_OraPumpActiveTime_Object = MibTableColumn
oraPumpActiveTime = _OraPumpActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 2),
    _OraPumpActiveTime_Type()
)
oraPumpActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpActiveTime.setStatus("mandatory")


class _OraPumpTraceLevel_Type(Integer32):
    """Custom type oraPumpTraceLevel based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("admin", 6),
          ("level1", 1),
          ("level10", 10),
          ("level11", 11),
          ("level12", 12),
          ("level13", 13),
          ("level14", 14),
          ("level15", 15),
          ("level16", 16),
          ("level2", 2),
          ("level3", 3),
          ("level5", 5),
          ("level7", 7),
          ("level8", 8),
          ("level9", 9),
          ("off", 17),
          ("user", 4))
    )


_OraPumpTraceLevel_Type.__name__ = "Integer32"
_OraPumpTraceLevel_Object = MibTableColumn
oraPumpTraceLevel = _OraPumpTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 3),
    _OraPumpTraceLevel_Type()
)
oraPumpTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraPumpTraceLevel.setStatus("mandatory")
_OraPumpTraceFile_Type = DisplayString
_OraPumpTraceFile_Object = MibTableColumn
oraPumpTraceFile = _OraPumpTraceFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 4),
    _OraPumpTraceFile_Type()
)
oraPumpTraceFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpTraceFile.setStatus("mandatory")
_OraPumpActiveConnections_Type = Gauge32
_OraPumpActiveConnections_Object = MibTableColumn
oraPumpActiveConnections = _OraPumpActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 5),
    _OraPumpActiveConnections_Type()
)
oraPumpActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpActiveConnections.setStatus("mandatory")
_OraPumpSuccessfulConnections_Type = Counter32
_OraPumpSuccessfulConnections_Object = MibTableColumn
oraPumpSuccessfulConnections = _OraPumpSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 6),
    _OraPumpSuccessfulConnections_Type()
)
oraPumpSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpSuccessfulConnections.setStatus("mandatory")
_OraPumpFailedConnections_Type = Counter32
_OraPumpFailedConnections_Object = MibTableColumn
oraPumpFailedConnections = _OraPumpFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 7),
    _OraPumpFailedConnections_Type()
)
oraPumpFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpFailedConnections.setStatus("mandatory")
_OraPumpAccumulatedBytesSent_Type = Counter32
_OraPumpAccumulatedBytesSent_Object = MibTableColumn
oraPumpAccumulatedBytesSent = _OraPumpAccumulatedBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 8),
    _OraPumpAccumulatedBytesSent_Type()
)
oraPumpAccumulatedBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpAccumulatedBytesSent.setStatus("mandatory")
_OraPumpCurrentBytesPerSecond_Type = Integer32
_OraPumpCurrentBytesPerSecond_Object = MibTableColumn
oraPumpCurrentBytesPerSecond = _OraPumpCurrentBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 9),
    _OraPumpCurrentBytesPerSecond_Type()
)
oraPumpCurrentBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpCurrentBytesPerSecond.setStatus("mandatory")
_OraPumpMaximumAverageBytes_Type = Integer32
_OraPumpMaximumAverageBytes_Object = MibTableColumn
oraPumpMaximumAverageBytes = _OraPumpMaximumAverageBytes_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 10),
    _OraPumpMaximumAverageBytes_Type()
)
oraPumpMaximumAverageBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpMaximumAverageBytes.setStatus("mandatory")
_OraPumpImmediateAverageBytes_Type = Integer32
_OraPumpImmediateAverageBytes_Object = MibTableColumn
oraPumpImmediateAverageBytes = _OraPumpImmediateAverageBytes_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 11),
    _OraPumpImmediateAverageBytes_Type()
)
oraPumpImmediateAverageBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpImmediateAverageBytes.setStatus("mandatory")
_OraPumpMaximumConnectTime_Type = Integer32
_OraPumpMaximumConnectTime_Object = MibTableColumn
oraPumpMaximumConnectTime = _OraPumpMaximumConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 12),
    _OraPumpMaximumConnectTime_Type()
)
oraPumpMaximumConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpMaximumConnectTime.setStatus("mandatory")
_OraPumpMinimumConnectTime_Type = Integer32
_OraPumpMinimumConnectTime_Object = MibTableColumn
oraPumpMinimumConnectTime = _OraPumpMinimumConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 13),
    _OraPumpMinimumConnectTime_Type()
)
oraPumpMinimumConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpMinimumConnectTime.setStatus("mandatory")
_OraPumpAverageConnectTime_Type = Integer32
_OraPumpAverageConnectTime_Object = MibTableColumn
oraPumpAverageConnectTime = _OraPumpAverageConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 14),
    _OraPumpAverageConnectTime_Type()
)
oraPumpAverageConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpAverageConnectTime.setStatus("mandatory")
_OraPumpMaximumConnectDuration_Type = Integer32
_OraPumpMaximumConnectDuration_Object = MibTableColumn
oraPumpMaximumConnectDuration = _OraPumpMaximumConnectDuration_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 15),
    _OraPumpMaximumConnectDuration_Type()
)
oraPumpMaximumConnectDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpMaximumConnectDuration.setStatus("mandatory")
_OraPumpMaximumBuffers_Type = Integer32
_OraPumpMaximumBuffers_Object = MibTableColumn
oraPumpMaximumBuffers = _OraPumpMaximumBuffers_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 16),
    _OraPumpMaximumBuffers_Type()
)
oraPumpMaximumBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraPumpMaximumBuffers.setStatus("mandatory")
_OraPumpBufferUtilization_Type = Gauge32
_OraPumpBufferUtilization_Object = MibTableColumn
oraPumpBufferUtilization = _OraPumpBufferUtilization_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 17),
    _OraPumpBufferUtilization_Type()
)
oraPumpBufferUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpBufferUtilization.setStatus("mandatory")
_OraPumpErrors_Type = DisplayString
_OraPumpErrors_Object = MibTableColumn
oraPumpErrors = _OraPumpErrors_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 18),
    _OraPumpErrors_Type()
)
oraPumpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpErrors.setStatus("mandatory")
_OraPumpErrorMessage_Type = DisplayString
_OraPumpErrorMessage_Object = MibTableColumn
oraPumpErrorMessage = _OraPumpErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 9, 1, 19),
    _OraPumpErrorMessage_Type()
)
oraPumpErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpErrorMessage.setStatus("mandatory")
_OraPumpListenAddressTable_Object = MibTable
oraPumpListenAddressTable = _OraPumpListenAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 10)
)
if mibBuilder.loadTexts:
    oraPumpListenAddressTable.setStatus("mandatory")
_OraPumpListenAddressEntry_Object = MibTableRow
oraPumpListenAddressEntry = _OraPumpListenAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 10, 1)
)
oraPumpListenAddressEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "ORAINTERCHANGE-MIB", "oraPumpIndex"),
    (0, "ORAINTERCHANGE-MIB", "oraPumpListenAddressIndex"),
)
if mibBuilder.loadTexts:
    oraPumpListenAddressEntry.setStatus("mandatory")
_OraPumpListenAddressIndex_Type = Integer32
_OraPumpListenAddressIndex_Object = MibTableColumn
oraPumpListenAddressIndex = _OraPumpListenAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 10, 1, 1),
    _OraPumpListenAddressIndex_Type()
)
oraPumpListenAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpListenAddressIndex.setStatus("mandatory")
_OraPumpListenAddress_Type = DisplayString
_OraPumpListenAddress_Object = MibTableColumn
oraPumpListenAddress = _OraPumpListenAddress_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 10, 1, 2),
    _OraPumpListenAddress_Type()
)
oraPumpListenAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpListenAddress.setStatus("mandatory")
_OraPumpFailedAddressTable_Object = MibTable
oraPumpFailedAddressTable = _OraPumpFailedAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 11)
)
if mibBuilder.loadTexts:
    oraPumpFailedAddressTable.setStatus("mandatory")
_OraPumpFailedAddressEntry_Object = MibTableRow
oraPumpFailedAddressEntry = _OraPumpFailedAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 11, 1)
)
oraPumpFailedAddressEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "ORAINTERCHANGE-MIB", "oraPumpIndex"),
    (0, "ORAINTERCHANGE-MIB", "oraPumpFailedAddressIndex"),
)
if mibBuilder.loadTexts:
    oraPumpFailedAddressEntry.setStatus("mandatory")
_OraPumpFailedAddressIndex_Type = Integer32
_OraPumpFailedAddressIndex_Object = MibTableColumn
oraPumpFailedAddressIndex = _OraPumpFailedAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 11, 1, 1),
    _OraPumpFailedAddressIndex_Type()
)
oraPumpFailedAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpFailedAddressIndex.setStatus("mandatory")
_OraPumpFailedAddress_Type = DisplayString
_OraPumpFailedAddress_Object = MibTableColumn
oraPumpFailedAddress = _OraPumpFailedAddress_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 11, 1, 2),
    _OraPumpFailedAddress_Type()
)
oraPumpFailedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPumpFailedAddress.setStatus("mandatory")
_OraConnectionTable_Object = MibTable
oraConnectionTable = _OraConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 12)
)
if mibBuilder.loadTexts:
    oraConnectionTable.setStatus("mandatory")
_OraConnectionEntry_Object = MibTableRow
oraConnectionEntry = _OraConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1)
)
oraConnectionEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "ORAINTERCHANGE-MIB", "oraPumpIndex"),
    (0, "ORAINTERCHANGE-MIB", "oraConnectionIndex"),
)
if mibBuilder.loadTexts:
    oraConnectionEntry.setStatus("mandatory")
_OraConnectionIndex_Type = Integer32
_OraConnectionIndex_Object = MibTableColumn
oraConnectionIndex = _OraConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1, 1),
    _OraConnectionIndex_Type()
)
oraConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraConnectionIndex.setStatus("mandatory")
_OraConnectionPumpID_Type = Integer32
_OraConnectionPumpID_Object = MibTableColumn
oraConnectionPumpID = _OraConnectionPumpID_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1, 2),
    _OraConnectionPumpID_Type()
)
oraConnectionPumpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraConnectionPumpID.setStatus("mandatory")
_OraConnectionIdleTime_Type = Integer32
_OraConnectionIdleTime_Object = MibTableColumn
oraConnectionIdleTime = _OraConnectionIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1, 3),
    _OraConnectionIdleTime_Type()
)
oraConnectionIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraConnectionIdleTime.setStatus("mandatory")
_OraConnectionDuration_Type = Integer32
_OraConnectionDuration_Object = MibTableColumn
oraConnectionDuration = _OraConnectionDuration_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1, 4),
    _OraConnectionDuration_Type()
)
oraConnectionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraConnectionDuration.setStatus("mandatory")
_OraConnectionSourceAddress_Type = DisplayString
_OraConnectionSourceAddress_Object = MibTableColumn
oraConnectionSourceAddress = _OraConnectionSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1, 5),
    _OraConnectionSourceAddress_Type()
)
oraConnectionSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraConnectionSourceAddress.setStatus("mandatory")
_OraConnectionDestinationAddress_Type = DisplayString
_OraConnectionDestinationAddress_Object = MibTableColumn
oraConnectionDestinationAddress = _OraConnectionDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 111, 7, 1, 12, 1, 6),
    _OraConnectionDestinationAddress_Type()
)
oraConnectionDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraConnectionDestinationAddress.setStatus("mandatory")
_OraInterchgTraps_ObjectIdentity = ObjectIdentity
oraInterchgTraps = _OraInterchgTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 7, 2)
)

# Managed Objects groups


# Notification objects

oraNavigatorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 111, 7, 2, 0, 1)
)
oraNavigatorStateChange.setObjects(
    ("ORAINTERCHANGE-MIB", "oraNavigatorState")
)
if mibBuilder.loadTexts:
    oraNavigatorStateChange.setStatus(
        ""
    )

oraCmanagerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 111, 7, 2, 0, 2)
)
oraCmanagerStateChange.setObjects(
    ("ORAINTERCHANGE-MIB", "oraCmanagerState")
)
if mibBuilder.loadTexts:
    oraCmanagerStateChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ORAINTERCHANGE-MIB",
    **{"oracle": oracle,
       "oraInterchangeMIB": oraInterchangeMIB,
       "oraInterchangeObjects": oraInterchangeObjects,
       "oraInterchgTable": oraInterchgTable,
       "oraInterchgEntry": oraInterchgEntry,
       "oraInterchgConfigDirectory": oraInterchgConfigDirectory,
       "oraInterchgContactInfo": oraInterchgContactInfo,
       "oraNavigatorTable": oraNavigatorTable,
       "oraNavigatorEntry": oraNavigatorEntry,
       "oraNavigatorRunningTime": oraNavigatorRunningTime,
       "oraNavigatorLogging": oraNavigatorLogging,
       "oraNavigatorLoggingLevel": oraNavigatorLoggingLevel,
       "oraNavigatorLogFile": oraNavigatorLogFile,
       "oraNavigatorTraceLevel": oraNavigatorTraceLevel,
       "oraNavigatorTraceFile": oraNavigatorTraceFile,
       "oraNavigatorStoppable": oraNavigatorStoppable,
       "oraNavigatorAccumulatedSuccessfulRequests": oraNavigatorAccumulatedSuccessfulRequests,
       "oraNavigatorAccumulatedFailedRequests": oraNavigatorAccumulatedFailedRequests,
       "oraNavigatorState": oraNavigatorState,
       "oraNavigatorErrors": oraNavigatorErrors,
       "oraNavigatorErrorMessage": oraNavigatorErrorMessage,
       "oraNavigatorListenAddressTable": oraNavigatorListenAddressTable,
       "oraNavigatorListenAddressEntry": oraNavigatorListenAddressEntry,
       "oraNavigatorListenAddressIndex": oraNavigatorListenAddressIndex,
       "oraNavigatorListenAddress": oraNavigatorListenAddress,
       "oraNavigatorFailedAddressTable": oraNavigatorFailedAddressTable,
       "oraNavigatorFailedAddressEntry": oraNavigatorFailedAddressEntry,
       "oraNavigatorFailedAddressIndex": oraNavigatorFailedAddressIndex,
       "oraNavigatorFailedAddress": oraNavigatorFailedAddress,
       "oraNavigatorRouteAddressTable": oraNavigatorRouteAddressTable,
       "oraNavigatorRouteAddressEntry": oraNavigatorRouteAddressEntry,
       "oraNavigatorRouteAddressIndex": oraNavigatorRouteAddressIndex,
       "oraNavigatorRouteAddress": oraNavigatorRouteAddress,
       "oraCmanagerTable": oraCmanagerTable,
       "oraCmanagerEntry": oraCmanagerEntry,
       "oraCmanagerStartTime": oraCmanagerStartTime,
       "oraCmanagerRunningTime": oraCmanagerRunningTime,
       "oraCmanagerLogging": oraCmanagerLogging,
       "oraCmanagerLogFile": oraCmanagerLogFile,
       "oraCmanagerTraceLevel": oraCmanagerTraceLevel,
       "oraCmanagerTraceFile": oraCmanagerTraceFile,
       "oraCmanagerStoppable": oraCmanagerStoppable,
       "oraCmanagerMaximumPumps": oraCmanagerMaximumPumps,
       "oraCmanagerMaximumConnectionsPerPump": oraCmanagerMaximumConnectionsPerPump,
       "oraCmanagerPumpStrategy": oraCmanagerPumpStrategy,
       "oraCmanagerActivePumps": oraCmanagerActivePumps,
       "oraCmanagerMaximumConnections": oraCmanagerMaximumConnections,
       "oraCmanagerCurrentConnectionsInUse": oraCmanagerCurrentConnectionsInUse,
       "oraCmanagerAccumulatedSuccessfulConnections": oraCmanagerAccumulatedSuccessfulConnections,
       "oraCmanagerAccumulatedFailedConnections": oraCmanagerAccumulatedFailedConnections,
       "oraCmanagerImmediateAverageBytes": oraCmanagerImmediateAverageBytes,
       "oraCmanagerMaximumConnectTime": oraCmanagerMaximumConnectTime,
       "oraCmanagerMinimumConnectTime": oraCmanagerMinimumConnectTime,
       "oraCmanagerAverageConnectTime": oraCmanagerAverageConnectTime,
       "oraCmanagerMaximumConnectDuration": oraCmanagerMaximumConnectDuration,
       "oraCmanagerState": oraCmanagerState,
       "oraCmanagerErrors": oraCmanagerErrors,
       "oraCmanagerErrorMessage": oraCmanagerErrorMessage,
       "oraCmanagerListenAddressTable": oraCmanagerListenAddressTable,
       "oraCmanagerListenAddressEntry": oraCmanagerListenAddressEntry,
       "oraCmanagerListenAddressIndex": oraCmanagerListenAddressIndex,
       "oraCmanagerListenAddress": oraCmanagerListenAddress,
       "oraCmanagerFailedAddressTable": oraCmanagerFailedAddressTable,
       "oraCmanagerFailedAddressEntry": oraCmanagerFailedAddressEntry,
       "oraCmanagerFailedAddressIndex": oraCmanagerFailedAddressIndex,
       "oraCmanagerFailedAddress": oraCmanagerFailedAddress,
       "oraPumpTable": oraPumpTable,
       "oraPumpEntry": oraPumpEntry,
       "oraPumpIndex": oraPumpIndex,
       "oraPumpActiveTime": oraPumpActiveTime,
       "oraPumpTraceLevel": oraPumpTraceLevel,
       "oraPumpTraceFile": oraPumpTraceFile,
       "oraPumpActiveConnections": oraPumpActiveConnections,
       "oraPumpSuccessfulConnections": oraPumpSuccessfulConnections,
       "oraPumpFailedConnections": oraPumpFailedConnections,
       "oraPumpAccumulatedBytesSent": oraPumpAccumulatedBytesSent,
       "oraPumpCurrentBytesPerSecond": oraPumpCurrentBytesPerSecond,
       "oraPumpMaximumAverageBytes": oraPumpMaximumAverageBytes,
       "oraPumpImmediateAverageBytes": oraPumpImmediateAverageBytes,
       "oraPumpMaximumConnectTime": oraPumpMaximumConnectTime,
       "oraPumpMinimumConnectTime": oraPumpMinimumConnectTime,
       "oraPumpAverageConnectTime": oraPumpAverageConnectTime,
       "oraPumpMaximumConnectDuration": oraPumpMaximumConnectDuration,
       "oraPumpMaximumBuffers": oraPumpMaximumBuffers,
       "oraPumpBufferUtilization": oraPumpBufferUtilization,
       "oraPumpErrors": oraPumpErrors,
       "oraPumpErrorMessage": oraPumpErrorMessage,
       "oraPumpListenAddressTable": oraPumpListenAddressTable,
       "oraPumpListenAddressEntry": oraPumpListenAddressEntry,
       "oraPumpListenAddressIndex": oraPumpListenAddressIndex,
       "oraPumpListenAddress": oraPumpListenAddress,
       "oraPumpFailedAddressTable": oraPumpFailedAddressTable,
       "oraPumpFailedAddressEntry": oraPumpFailedAddressEntry,
       "oraPumpFailedAddressIndex": oraPumpFailedAddressIndex,
       "oraPumpFailedAddress": oraPumpFailedAddress,
       "oraConnectionTable": oraConnectionTable,
       "oraConnectionEntry": oraConnectionEntry,
       "oraConnectionIndex": oraConnectionIndex,
       "oraConnectionPumpID": oraConnectionPumpID,
       "oraConnectionIdleTime": oraConnectionIdleTime,
       "oraConnectionDuration": oraConnectionDuration,
       "oraConnectionSourceAddress": oraConnectionSourceAddress,
       "oraConnectionDestinationAddress": oraConnectionDestinationAddress,
       "oraInterchgTraps": oraInterchgTraps,
       "oraNavigatorStateChange": oraNavigatorStateChange,
       "oraCmanagerStateChange": oraCmanagerStateChange}
)
