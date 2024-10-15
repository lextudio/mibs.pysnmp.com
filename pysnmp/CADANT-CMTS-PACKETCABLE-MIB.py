# SNMP MIB module (CADANT-CMTS-PACKETCABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-PACKETCABLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:42 2024
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

(cadIfCmtsCardNumber,) = mibBuilder.importSymbols(
    "CADANT-CMTS-DOWNCHANNEL-MIB",
    "cadIfCmtsCardNumber")

(cadOvSysCpuStatus,) = mibBuilder.importSymbols(
    "CADANT-CMTS-PROCESS-MIB",
    "cadOvSysCpuStatus")

(cadCable,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadCable")

(AdminState,
 CardId) = mibBuilder.importSymbols(
    "CADANT-TC",
    "AdminState",
    "CardId")

(IfDirection,) = mibBuilder.importSymbols(
    "DOCS-QOS3-MIB",
    "IfDirection")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cadPCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115)
)
cadPCMIB.setRevisions(
        ("2015-12-21 00:00",
         "2011-08-04 00:00",
         "2011-07-26 00:00",
         "2009-02-26 00:00",
         "2007-11-12 00:00",
         "2007-10-24 00:00",
         "2007-09-06 00:00",
         "2005-08-10 00:00",
         "2005-05-16 00:00",
         "2004-11-10 00:00",
         "2004-10-04 00:00",
         "2004-02-19 00:00",
         "2004-02-18 00:00",
         "2004-02-15 00:00",
         "2003-09-04 00:00",
         "2003-07-28 00:00",
         "2003-05-20 00:00",
         "2002-08-26 00:00",
         "2001-07-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CadPCAnomalyCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              127,
              65535,
              65537,
              65538,
              65539,
              65540,
              65541,
              65542,
              65543,
              65663,
              131072,
              196608,
              262144,
              327680,
              393216,
              458752,
              8323072)
        )
    )
    namedValues = NamedValues(
        *(("closedLackOfReservationMaintenance", 65538),
          ("closedMTADeregistration", 65539),
          ("closedPreemptionOfResources", 65537),
          ("closedTimerT0Expiry", 65540),
          ("closedTimerT1Rxpiry", 65541),
          ("closedTimerT7Rxpiry", 65542),
          ("closedTimerT8Rxpiry", 65543),
          ("closedUnknownReason", 65663),
          ("deletedLocalGateCloseFailure", 5),
          ("deletedLocalGateCoordinationFailure", 1),
          ("deletedRemoteGateCoordinationFailure", 2),
          ("deletedRevokedAuthorization", 3),
          ("deletedUnexpectedGateOpen", 4),
          ("deletedUnknownReason", 127),
          ("failedGateAlreadySet", 327680),
          ("failedIllegalSessionClassValue", 196608),
          ("failedInvalidObject", 458752),
          ("failedMTAExceededGateLimit", 262144),
          ("failedMissingRequiredObject", 393216),
          ("failedNoGatesAvailable", 65535),
          ("failedUnknownGateId", 131072),
          ("failedUnknownReason", 8323072))
    )



class CadPCAdmCtlPriority(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("eightPriority", 1),
          ("fifthPriority", 4),
          ("firstPriority", 8),
          ("fourthPriority", 5),
          ("secondPriority", 7),
          ("seventhPriority", 2),
          ("sixthPriority", 3),
          ("thirdPriority", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CadPCMibObjects_ObjectIdentity = ObjectIdentity
cadPCMibObjects = _CadPCMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1)
)
_CadPCMibBase_ObjectIdentity = ObjectIdentity
cadPCMibBase = _CadPCMibBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1)
)


class _CadPCPreemptionAllowed_Type(TruthValue):
    """Custom type cadPCPreemptionAllowed based on TruthValue"""


_CadPCPreemptionAllowed_Object = MibScalar
cadPCPreemptionAllowed = _CadPCPreemptionAllowed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 3),
    _CadPCPreemptionAllowed_Type()
)
cadPCPreemptionAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCPreemptionAllowed.setStatus("current")


class _CadPCUpNormAllowedUsage_Type(Integer32):
    """Custom type cadPCUpNormAllowedUsage based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadPCUpNormAllowedUsage_Type.__name__ = "Integer32"
_CadPCUpNormAllowedUsage_Object = MibScalar
cadPCUpNormAllowedUsage = _CadPCUpNormAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 4),
    _CadPCUpNormAllowedUsage_Type()
)
cadPCUpNormAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCUpNormAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCUpNormAllowedUsage.setUnits("percent")


class _CadPCUpNormResUsage_Type(Integer32):
    """Custom type cadPCUpNormResUsage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadPCUpNormResUsage_Type.__name__ = "Integer32"
_CadPCUpNormResUsage_Object = MibScalar
cadPCUpNormResUsage = _CadPCUpNormResUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 5),
    _CadPCUpNormResUsage_Type()
)
cadPCUpNormResUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCUpNormResUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCUpNormResUsage.setUnits("percent")


class _CadPCUpEmerAllowedUsage_Type(Integer32):
    """Custom type cadPCUpEmerAllowedUsage based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadPCUpEmerAllowedUsage_Type.__name__ = "Integer32"
_CadPCUpEmerAllowedUsage_Object = MibScalar
cadPCUpEmerAllowedUsage = _CadPCUpEmerAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 6),
    _CadPCUpEmerAllowedUsage_Type()
)
cadPCUpEmerAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCUpEmerAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCUpEmerAllowedUsage.setUnits("percent")


class _CadPCUpEmerResUsage_Type(Integer32):
    """Custom type cadPCUpEmerResUsage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadPCUpEmerResUsage_Type.__name__ = "Integer32"
_CadPCUpEmerResUsage_Object = MibScalar
cadPCUpEmerResUsage = _CadPCUpEmerResUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 7),
    _CadPCUpEmerResUsage_Type()
)
cadPCUpEmerResUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCUpEmerResUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCUpEmerResUsage.setUnits("percent")


class _CadPCDownNormAllowedUsage_Type(Integer32):
    """Custom type cadPCDownNormAllowedUsage based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadPCDownNormAllowedUsage_Type.__name__ = "Integer32"
_CadPCDownNormAllowedUsage_Object = MibScalar
cadPCDownNormAllowedUsage = _CadPCDownNormAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 8),
    _CadPCDownNormAllowedUsage_Type()
)
cadPCDownNormAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCDownNormAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCDownNormAllowedUsage.setUnits("percent")


class _CadPCDownNormResUsage_Type(Integer32):
    """Custom type cadPCDownNormResUsage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadPCDownNormResUsage_Type.__name__ = "Integer32"
_CadPCDownNormResUsage_Object = MibScalar
cadPCDownNormResUsage = _CadPCDownNormResUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 9),
    _CadPCDownNormResUsage_Type()
)
cadPCDownNormResUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCDownNormResUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCDownNormResUsage.setUnits("percent")


class _CadPCDownEmerAllowedUsage_Type(Integer32):
    """Custom type cadPCDownEmerAllowedUsage based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadPCDownEmerAllowedUsage_Type.__name__ = "Integer32"
_CadPCDownEmerAllowedUsage_Object = MibScalar
cadPCDownEmerAllowedUsage = _CadPCDownEmerAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 10),
    _CadPCDownEmerAllowedUsage_Type()
)
cadPCDownEmerAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCDownEmerAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCDownEmerAllowedUsage.setUnits("percent")


class _CadPCDownEmerResUsage_Type(Integer32):
    """Custom type cadPCDownEmerResUsage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadPCDownEmerResUsage_Type.__name__ = "Integer32"
_CadPCDownEmerResUsage_Object = MibScalar
cadPCDownEmerResUsage = _CadPCDownEmerResUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 11),
    _CadPCDownEmerResUsage_Type()
)
cadPCDownEmerResUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCDownEmerResUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCDownEmerResUsage.setUnits("percent")
_CadPCCAMTable_Object = MibTable
cadPCCAMTable = _CadPCCAMTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cadPCCAMTable.setStatus("current")
_CadPCCAMEntry_Object = MibTableRow
cadPCCAMEntry = _CadPCCAMEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 12, 1)
)
cadPCCAMEntry.setIndexNames(
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCCardId"),
)
if mibBuilder.loadTexts:
    cadPCCAMEntry.setStatus("current")


class _CadFreeDSxAllowed_Type(TruthValue):
    """Custom type cadFreeDSxAllowed based on TruthValue"""


_CadFreeDSxAllowed_Object = MibTableColumn
cadFreeDSxAllowed = _CadFreeDSxAllowed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 12, 1, 1),
    _CadFreeDSxAllowed_Type()
)
cadFreeDSxAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadFreeDSxAllowed.setStatus("current")


class _CadPCMaxOverloadDSaCalls_Type(Unsigned32):
    """Custom type cadPCMaxOverloadDSaCalls based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CadPCMaxOverloadDSaCalls_Type.__name__ = "Unsigned32"
_CadPCMaxOverloadDSaCalls_Object = MibTableColumn
cadPCMaxOverloadDSaCalls = _CadPCMaxOverloadDSaCalls_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 12, 1, 2),
    _CadPCMaxOverloadDSaCalls_Type()
)
cadPCMaxOverloadDSaCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCMaxOverloadDSaCalls.setStatus("current")
if mibBuilder.loadTexts:
    cadPCMaxOverloadDSaCalls.setUnits("connections per 10 seconds")


class _CadPCMaxYellowOverloadDSaCalls_Type(Unsigned32):
    """Custom type cadPCMaxYellowOverloadDSaCalls based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CadPCMaxYellowOverloadDSaCalls_Type.__name__ = "Unsigned32"
_CadPCMaxYellowOverloadDSaCalls_Object = MibTableColumn
cadPCMaxYellowOverloadDSaCalls = _CadPCMaxYellowOverloadDSaCalls_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 12, 1, 3),
    _CadPCMaxYellowOverloadDSaCalls_Type()
)
cadPCMaxYellowOverloadDSaCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCMaxYellowOverloadDSaCalls.setStatus("current")
if mibBuilder.loadTexts:
    cadPCMaxYellowOverloadDSaCalls.setUnits("connections per 10 seconds")


class _CadPCMaxRedOverloadDSaCalls_Type(Unsigned32):
    """Custom type cadPCMaxRedOverloadDSaCalls based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CadPCMaxRedOverloadDSaCalls_Type.__name__ = "Unsigned32"
_CadPCMaxRedOverloadDSaCalls_Object = MibTableColumn
cadPCMaxRedOverloadDSaCalls = _CadPCMaxRedOverloadDSaCalls_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 12, 1, 4),
    _CadPCMaxRedOverloadDSaCalls_Type()
)
cadPCMaxRedOverloadDSaCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCMaxRedOverloadDSaCalls.setStatus("current")
if mibBuilder.loadTexts:
    cadPCMaxRedOverloadDSaCalls.setUnits("connections per 10 seconds")
_CadPCCardId_Type = CardId
_CadPCCardId_Object = MibTableColumn
cadPCCardId = _CadPCCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 12, 1, 5),
    _CadPCCardId_Type()
)
cadPCCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCCardId.setStatus("current")


class _CadPCAdminState_Type(AdminState):
    """Custom type cadPCAdminState based on AdminState"""


_CadPCAdminState_Object = MibScalar
cadPCAdminState = _CadPCAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 13),
    _CadPCAdminState_Type()
)
cadPCAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCAdminState.setStatus("current")


class _CadPCMaxOverloadCalls_Type(Unsigned32):
    """Custom type cadPCMaxOverloadCalls based on Unsigned32"""
    defaultValue = 450

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CadPCMaxOverloadCalls_Type.__name__ = "Unsigned32"
_CadPCMaxOverloadCalls_Object = MibScalar
cadPCMaxOverloadCalls = _CadPCMaxOverloadCalls_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 14),
    _CadPCMaxOverloadCalls_Type()
)
cadPCMaxOverloadCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCMaxOverloadCalls.setStatus("obsolete")
if mibBuilder.loadTexts:
    cadPCMaxOverloadCalls.setUnits("connections per 10 seconds")


class _CadPCMaxYellowOverloadCalls_Type(Unsigned32):
    """Custom type cadPCMaxYellowOverloadCalls based on Unsigned32"""
    defaultValue = 450

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CadPCMaxYellowOverloadCalls_Type.__name__ = "Unsigned32"
_CadPCMaxYellowOverloadCalls_Object = MibScalar
cadPCMaxYellowOverloadCalls = _CadPCMaxYellowOverloadCalls_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 15),
    _CadPCMaxYellowOverloadCalls_Type()
)
cadPCMaxYellowOverloadCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCMaxYellowOverloadCalls.setStatus("obsolete")
if mibBuilder.loadTexts:
    cadPCMaxYellowOverloadCalls.setUnits("connections per 10 seconds")


class _CadPCMaxRedOverloadCalls_Type(Unsigned32):
    """Custom type cadPCMaxRedOverloadCalls based on Unsigned32"""
    defaultValue = 41

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CadPCMaxRedOverloadCalls_Type.__name__ = "Unsigned32"
_CadPCMaxRedOverloadCalls_Object = MibScalar
cadPCMaxRedOverloadCalls = _CadPCMaxRedOverloadCalls_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 16),
    _CadPCMaxRedOverloadCalls_Type()
)
cadPCMaxRedOverloadCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCMaxRedOverloadCalls.setStatus("obsolete")
if mibBuilder.loadTexts:
    cadPCMaxRedOverloadCalls.setUnits("connections per 10 seconds")


class _CadPCDownTotalAllowedUsage_Type(Integer32):
    """Custom type cadPCDownTotalAllowedUsage based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadPCDownTotalAllowedUsage_Type.__name__ = "Integer32"
_CadPCDownTotalAllowedUsage_Object = MibScalar
cadPCDownTotalAllowedUsage = _CadPCDownTotalAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 17),
    _CadPCDownTotalAllowedUsage_Type()
)
cadPCDownTotalAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCDownTotalAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCDownTotalAllowedUsage.setUnits("percent")


class _CadPCUpTotalAllowedUsage_Type(Integer32):
    """Custom type cadPCUpTotalAllowedUsage based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadPCUpTotalAllowedUsage_Type.__name__ = "Integer32"
_CadPCUpTotalAllowedUsage_Object = MibScalar
cadPCUpTotalAllowedUsage = _CadPCUpTotalAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 18),
    _CadPCUpTotalAllowedUsage_Type()
)
cadPCUpTotalAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCUpTotalAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCUpTotalAllowedUsage.setUnits("percent")


class _CadPCMaxOverloadGateMsgs_Type(Unsigned32):
    """Custom type cadPCMaxOverloadGateMsgs based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CadPCMaxOverloadGateMsgs_Type.__name__ = "Unsigned32"
_CadPCMaxOverloadGateMsgs_Object = MibScalar
cadPCMaxOverloadGateMsgs = _CadPCMaxOverloadGateMsgs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 19),
    _CadPCMaxOverloadGateMsgs_Type()
)
cadPCMaxOverloadGateMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCMaxOverloadGateMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cadPCMaxOverloadGateMsgs.setUnits("gate messages per 10 seconds")


class _CadPCMaxYellowOverloadGateMsgs_Type(Unsigned32):
    """Custom type cadPCMaxYellowOverloadGateMsgs based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CadPCMaxYellowOverloadGateMsgs_Type.__name__ = "Unsigned32"
_CadPCMaxYellowOverloadGateMsgs_Object = MibScalar
cadPCMaxYellowOverloadGateMsgs = _CadPCMaxYellowOverloadGateMsgs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 20),
    _CadPCMaxYellowOverloadGateMsgs_Type()
)
cadPCMaxYellowOverloadGateMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCMaxYellowOverloadGateMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cadPCMaxYellowOverloadGateMsgs.setUnits("gate messages per 10 seconds")


class _CadPCMaxRedOverloadGateMsgs_Type(Unsigned32):
    """Custom type cadPCMaxRedOverloadGateMsgs based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CadPCMaxRedOverloadGateMsgs_Type.__name__ = "Unsigned32"
_CadPCMaxRedOverloadGateMsgs_Object = MibScalar
cadPCMaxRedOverloadGateMsgs = _CadPCMaxRedOverloadGateMsgs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 21),
    _CadPCMaxRedOverloadGateMsgs_Type()
)
cadPCMaxRedOverloadGateMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCMaxRedOverloadGateMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cadPCMaxRedOverloadGateMsgs.setUnits("gate messages per 10 seconds")


class _CadPCClearGateCounts_Type(TruthValue):
    """Custom type cadPCClearGateCounts based on TruthValue"""


_CadPCClearGateCounts_Object = MibScalar
cadPCClearGateCounts = _CadPCClearGateCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 25),
    _CadPCClearGateCounts_Type()
)
cadPCClearGateCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCClearGateCounts.setStatus("current")


class _CadPCClearAnomalyCounts_Type(TruthValue):
    """Custom type cadPCClearAnomalyCounts based on TruthValue"""


_CadPCClearAnomalyCounts_Object = MibScalar
cadPCClearAnomalyCounts = _CadPCClearAnomalyCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 26),
    _CadPCClearAnomalyCounts_Type()
)
cadPCClearAnomalyCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCClearAnomalyCounts.setStatus("current")


class _CadPCClearConnRateOverloadCounts_Type(TruthValue):
    """Custom type cadPCClearConnRateOverloadCounts based on TruthValue"""


_CadPCClearConnRateOverloadCounts_Object = MibScalar
cadPCClearConnRateOverloadCounts = _CadPCClearConnRateOverloadCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 27),
    _CadPCClearConnRateOverloadCounts_Type()
)
cadPCClearConnRateOverloadCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCClearConnRateOverloadCounts.setStatus("current")


class _CadPCClearEvMsgCounts_Type(TruthValue):
    """Custom type cadPCClearEvMsgCounts based on TruthValue"""


_CadPCClearEvMsgCounts_Object = MibScalar
cadPCClearEvMsgCounts = _CadPCClearEvMsgCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 28),
    _CadPCClearEvMsgCounts_Type()
)
cadPCClearEvMsgCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCClearEvMsgCounts.setStatus("current")


class _CadPCClearCopsCounts_Type(TruthValue):
    """Custom type cadPCClearCopsCounts based on TruthValue"""


_CadPCClearCopsCounts_Object = MibScalar
cadPCClearCopsCounts = _CadPCClearCopsCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 29),
    _CadPCClearCopsCounts_Type()
)
cadPCClearCopsCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCClearCopsCounts.setStatus("current")


class _CadPCClearGateCtlCounts_Type(TruthValue):
    """Custom type cadPCClearGateCtlCounts based on TruthValue"""


_CadPCClearGateCtlCounts_Object = MibScalar
cadPCClearGateCtlCounts = _CadPCClearGateCtlCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 30),
    _CadPCClearGateCtlCounts_Type()
)
cadPCClearGateCtlCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCClearGateCtlCounts.setStatus("current")
_CadPCMibGateCounts_ObjectIdentity = ObjectIdentity
cadPCMibGateCounts = _CadPCMibGateCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 40)
)
_CadPCTotalGateCount_Type = Counter32
_CadPCTotalGateCount_Object = MibScalar
cadPCTotalGateCount = _CadPCTotalGateCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 40, 1),
    _CadPCTotalGateCount_Type()
)
cadPCTotalGateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCTotalGateCount.setStatus("current")
if mibBuilder.loadTexts:
    cadPCTotalGateCount.setUnits("gates")
_CadPCGateAllocatedStateCount_Type = Counter32
_CadPCGateAllocatedStateCount_Object = MibScalar
cadPCGateAllocatedStateCount = _CadPCGateAllocatedStateCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 40, 2),
    _CadPCGateAllocatedStateCount_Type()
)
cadPCGateAllocatedStateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCGateAllocatedStateCount.setStatus("current")
if mibBuilder.loadTexts:
    cadPCGateAllocatedStateCount.setUnits("gates")
_CadPCGateAuthorizedStateCount_Type = Counter32
_CadPCGateAuthorizedStateCount_Object = MibScalar
cadPCGateAuthorizedStateCount = _CadPCGateAuthorizedStateCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 40, 3),
    _CadPCGateAuthorizedStateCount_Type()
)
cadPCGateAuthorizedStateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCGateAuthorizedStateCount.setStatus("current")
if mibBuilder.loadTexts:
    cadPCGateAuthorizedStateCount.setUnits("gates")
_CadPCGateReservedStateCount_Type = Counter32
_CadPCGateReservedStateCount_Object = MibScalar
cadPCGateReservedStateCount = _CadPCGateReservedStateCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 40, 4),
    _CadPCGateReservedStateCount_Type()
)
cadPCGateReservedStateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCGateReservedStateCount.setStatus("current")
if mibBuilder.loadTexts:
    cadPCGateReservedStateCount.setUnits("gates")
_CadPCGateCommittedStateCount_Type = Counter32
_CadPCGateCommittedStateCount_Object = MibScalar
cadPCGateCommittedStateCount = _CadPCGateCommittedStateCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 40, 5),
    _CadPCGateCommittedStateCount_Type()
)
cadPCGateCommittedStateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCGateCommittedStateCount.setStatus("current")
if mibBuilder.loadTexts:
    cadPCGateCommittedStateCount.setUnits("gates")


class _CadPCGateLastCleared_Type(TimeStamp):
    """Custom type cadPCGateLastCleared based on TimeStamp"""
    defaultValue = 0


_CadPCGateLastCleared_Object = MibScalar
cadPCGateLastCleared = _CadPCGateLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 40, 6),
    _CadPCGateLastCleared_Type()
)
cadPCGateLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCGateLastCleared.setStatus("current")
_CadPCAnomalyCountTable_Object = MibTable
cadPCAnomalyCountTable = _CadPCAnomalyCountTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 45)
)
if mibBuilder.loadTexts:
    cadPCAnomalyCountTable.setStatus("current")
_CadPCAnomalyCountEntry_Object = MibTableRow
cadPCAnomalyCountEntry = _CadPCAnomalyCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 45, 1)
)
cadPCAnomalyCountEntry.setIndexNames(
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCAnomalyCode"),
)
if mibBuilder.loadTexts:
    cadPCAnomalyCountEntry.setStatus("current")
_CadPCAnomalyCode_Type = CadPCAnomalyCode
_CadPCAnomalyCode_Object = MibTableColumn
cadPCAnomalyCode = _CadPCAnomalyCode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 45, 1, 1),
    _CadPCAnomalyCode_Type()
)
cadPCAnomalyCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCAnomalyCode.setStatus("current")
_CadPCAnomalyCount_Type = Counter32
_CadPCAnomalyCount_Object = MibTableColumn
cadPCAnomalyCount = _CadPCAnomalyCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 45, 1, 2),
    _CadPCAnomalyCount_Type()
)
cadPCAnomalyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCAnomalyCount.setStatus("current")


class _CadPCAnomalyLastCleared_Type(TimeStamp):
    """Custom type cadPCAnomalyLastCleared based on TimeStamp"""
    defaultValue = 0


_CadPCAnomalyLastCleared_Object = MibScalar
cadPCAnomalyLastCleared = _CadPCAnomalyLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 46),
    _CadPCAnomalyLastCleared_Type()
)
cadPCAnomalyLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCAnomalyLastCleared.setStatus("current")


class _CadPCSendSubId_Type(TruthValue):
    """Custom type cadPCSendSubId based on TruthValue"""


_CadPCSendSubId_Object = MibScalar
cadPCSendSubId = _CadPCSendSubId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 47),
    _CadPCSendSubId_Type()
)
cadPCSendSubId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCSendSubId.setStatus("current")
_CadPCConnRateReqHistoryTable_Object = MibTable
cadPCConnRateReqHistoryTable = _CadPCConnRateReqHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 50)
)
if mibBuilder.loadTexts:
    cadPCConnRateReqHistoryTable.setStatus("current")
_CadPCConnRateReqHistoryEntry_Object = MibTableRow
cadPCConnRateReqHistoryEntry = _CadPCConnRateReqHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 50, 1)
)
cadPCConnRateReqHistoryEntry.setIndexNames(
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCConnRateReqHistoryTimeStamp"),
)
if mibBuilder.loadTexts:
    cadPCConnRateReqHistoryEntry.setStatus("current")
_CadPCConnRateReqHistoryTimeStamp_Type = TimeStamp
_CadPCConnRateReqHistoryTimeStamp_Object = MibTableColumn
cadPCConnRateReqHistoryTimeStamp = _CadPCConnRateReqHistoryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 50, 1, 1),
    _CadPCConnRateReqHistoryTimeStamp_Type()
)
cadPCConnRateReqHistoryTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCConnRateReqHistoryTimeStamp.setStatus("current")
_CadPCConnRateReqHistoryCount_Type = Counter32
_CadPCConnRateReqHistoryCount_Object = MibTableColumn
cadPCConnRateReqHistoryCount = _CadPCConnRateReqHistoryCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 50, 1, 2),
    _CadPCConnRateReqHistoryCount_Type()
)
cadPCConnRateReqHistoryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCConnRateReqHistoryCount.setStatus("current")
_CadPCConnReqMaxHistRate_Type = Counter32
_CadPCConnReqMaxHistRate_Object = MibScalar
cadPCConnReqMaxHistRate = _CadPCConnReqMaxHistRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 51),
    _CadPCConnReqMaxHistRate_Type()
)
cadPCConnReqMaxHistRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCConnReqMaxHistRate.setStatus("current")
if mibBuilder.loadTexts:
    cadPCConnReqMaxHistRate.setUnits("gates")
_CadPCConnRateOverloadRejTable_Object = MibTable
cadPCConnRateOverloadRejTable = _CadPCConnRateOverloadRejTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 55)
)
if mibBuilder.loadTexts:
    cadPCConnRateOverloadRejTable.setStatus("current")
_CadPCConnRateOverloadRejEntry_Object = MibTableRow
cadPCConnRateOverloadRejEntry = _CadPCConnRateOverloadRejEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 55, 1)
)
cadPCConnRateOverloadRejEntry.setIndexNames(
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCConnRateOverloadRejCardId"),
    (0, "CADANT-CMTS-PROCESS-MIB", "cadOvSysCpuStatus"),
)
if mibBuilder.loadTexts:
    cadPCConnRateOverloadRejEntry.setStatus("current")
_CadPCConnRateOverloadRejCount_Type = Counter32
_CadPCConnRateOverloadRejCount_Object = MibTableColumn
cadPCConnRateOverloadRejCount = _CadPCConnRateOverloadRejCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 55, 1, 1),
    _CadPCConnRateOverloadRejCount_Type()
)
cadPCConnRateOverloadRejCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCConnRateOverloadRejCount.setStatus("current")
if mibBuilder.loadTexts:
    cadPCConnRateOverloadRejCount.setUnits("connections")
_CadPCConnRateOverloadRejCardId_Type = CardId
_CadPCConnRateOverloadRejCardId_Object = MibTableColumn
cadPCConnRateOverloadRejCardId = _CadPCConnRateOverloadRejCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 55, 1, 2),
    _CadPCConnRateOverloadRejCardId_Type()
)
cadPCConnRateOverloadRejCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCConnRateOverloadRejCardId.setStatus("current")


class _CadPCConnRateOverloadLastCleared_Type(TimeStamp):
    """Custom type cadPCConnRateOverloadLastCleared based on TimeStamp"""
    defaultValue = 0


_CadPCConnRateOverloadLastCleared_Object = MibScalar
cadPCConnRateOverloadLastCleared = _CadPCConnRateOverloadLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 56),
    _CadPCConnRateOverloadLastCleared_Type()
)
cadPCConnRateOverloadLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCConnRateOverloadLastCleared.setStatus("current")
_CadPCEvMsgCountTable_Object = MibTable
cadPCEvMsgCountTable = _CadPCEvMsgCountTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 60)
)
if mibBuilder.loadTexts:
    cadPCEvMsgCountTable.setStatus("current")
_CadPCEvMsgCountEntry_Object = MibTableRow
cadPCEvMsgCountEntry = _CadPCEvMsgCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 60, 1)
)
cadPCEvMsgCountEntry.setIndexNames(
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCEvMsgCountServer"),
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCEvMsgServerIsDF"),
)
if mibBuilder.loadTexts:
    cadPCEvMsgCountEntry.setStatus("current")
_CadPCEvMsgCountServer_Type = IpAddress
_CadPCEvMsgCountServer_Object = MibTableColumn
cadPCEvMsgCountServer = _CadPCEvMsgCountServer_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 60, 1, 1),
    _CadPCEvMsgCountServer_Type()
)
cadPCEvMsgCountServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCEvMsgCountServer.setStatus("current")


class _CadPCEvMsgServerIsDF_Type(TruthValue):
    """Custom type cadPCEvMsgServerIsDF based on TruthValue"""


_CadPCEvMsgServerIsDF_Object = MibTableColumn
cadPCEvMsgServerIsDF = _CadPCEvMsgServerIsDF_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 60, 1, 2),
    _CadPCEvMsgServerIsDF_Type()
)
cadPCEvMsgServerIsDF.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCEvMsgServerIsDF.setStatus("current")


class _CadPCEvMsgType_Type(Integer32):
    """Custom type cadPCEvMsgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              17,
              19,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("qos-commit", 19),
          ("qos-release", 8),
          ("qos-reserve", 7),
          ("time-change", 17),
          ("total-packets", 9999))
    )


_CadPCEvMsgType_Type.__name__ = "Integer32"
_CadPCEvMsgType_Object = MibTableColumn
cadPCEvMsgType = _CadPCEvMsgType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 60, 1, 3),
    _CadPCEvMsgType_Type()
)
cadPCEvMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCEvMsgType.setStatus("current")
_CadPCEvMsgCount_Type = Counter32
_CadPCEvMsgCount_Object = MibTableColumn
cadPCEvMsgCount = _CadPCEvMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 60, 1, 4),
    _CadPCEvMsgCount_Type()
)
cadPCEvMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCEvMsgCount.setStatus("current")


class _CadPCEvMsgCountLastCleared_Type(TimeStamp):
    """Custom type cadPCEvMsgCountLastCleared based on TimeStamp"""
    defaultValue = 0


_CadPCEvMsgCountLastCleared_Object = MibScalar
cadPCEvMsgCountLastCleared = _CadPCEvMsgCountLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 61),
    _CadPCEvMsgCountLastCleared_Type()
)
cadPCEvMsgCountLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCEvMsgCountLastCleared.setStatus("current")
_CadPCCopsCountTable_Object = MibTable
cadPCCopsCountTable = _CadPCCopsCountTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 65)
)
if mibBuilder.loadTexts:
    cadPCCopsCountTable.setStatus("current")
_CadPCCopsCountEntry_Object = MibTableRow
cadPCCopsCountEntry = _CadPCCopsCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 65, 1)
)
cadPCCopsCountEntry.setIndexNames(
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCCopsServer"),
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCCopsDirection"),
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCCopsOpcode"),
)
if mibBuilder.loadTexts:
    cadPCCopsCountEntry.setStatus("current")
_CadPCCopsServer_Type = IpAddress
_CadPCCopsServer_Object = MibTableColumn
cadPCCopsServer = _CadPCCopsServer_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 65, 1, 1),
    _CadPCCopsServer_Type()
)
cadPCCopsServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCCopsServer.setStatus("current")


class _CadPCCopsDirection_Type(Integer32):
    """Custom type cadPCCopsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receive", 1),
          ("transmit", 2))
    )


_CadPCCopsDirection_Type.__name__ = "Integer32"
_CadPCCopsDirection_Object = MibTableColumn
cadPCCopsDirection = _CadPCCopsDirection_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 65, 1, 2),
    _CadPCCopsDirection_Type()
)
cadPCCopsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCCopsDirection.setStatus("current")


class _CadPCCopsOpcode_Type(Integer32):
    """Custom type cadPCCopsOpcode based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("copsCC", 8),
          ("copsCat", 7),
          ("copsDec", 2),
          ("copsDrq", 4),
          ("copsKa", 9),
          ("copsOpn", 6),
          ("copsReq", 1),
          ("copsRpt", 3),
          ("copsSsc", 10),
          ("copsSsq", 5),
          ("tcpCxt", 0))
    )


_CadPCCopsOpcode_Type.__name__ = "Integer32"
_CadPCCopsOpcode_Object = MibTableColumn
cadPCCopsOpcode = _CadPCCopsOpcode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 65, 1, 3),
    _CadPCCopsOpcode_Type()
)
cadPCCopsOpcode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCCopsOpcode.setStatus("current")
_CadPCCopsCount_Type = Counter32
_CadPCCopsCount_Object = MibTableColumn
cadPCCopsCount = _CadPCCopsCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 65, 1, 4),
    _CadPCCopsCount_Type()
)
cadPCCopsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCCopsCount.setStatus("current")


class _CadPCCopsCountLastCleared_Type(TimeStamp):
    """Custom type cadPCCopsCountLastCleared based on TimeStamp"""
    defaultValue = 0


_CadPCCopsCountLastCleared_Object = MibScalar
cadPCCopsCountLastCleared = _CadPCCopsCountLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 66),
    _CadPCCopsCountLastCleared_Type()
)
cadPCCopsCountLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCCopsCountLastCleared.setStatus("current")
_CadPCGateCtlCountTable_Object = MibTable
cadPCGateCtlCountTable = _CadPCGateCtlCountTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 70)
)
if mibBuilder.loadTexts:
    cadPCGateCtlCountTable.setStatus("current")
_CadPCGateCtlCountEntry_Object = MibTableRow
cadPCGateCtlCountEntry = _CadPCGateCtlCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 70, 1)
)
cadPCGateCtlCountEntry.setIndexNames(
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCCopsServer"),
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCGateCtlOpcode"),
)
if mibBuilder.loadTexts:
    cadPCGateCtlCountEntry.setStatus("current")


class _CadPCGateCtlOpcode_Type(Integer32):
    """Custom type cadPCGateCtlOpcode based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("gateAllocAck", 2),
          ("gateAllocErr", 3),
          ("gateAllocReq", 1),
          ("gateClose", 14),
          ("gateDeleteAck", 11),
          ("gateDeleteErr", 12),
          ("gateDeleteReq", 10),
          ("gateInfoAck", 8),
          ("gateInfoErr", 9),
          ("gateInfoReq", 7),
          ("gateOpen", 13),
          ("gateReportState", 15),
          ("gateSetAck", 5),
          ("gateSetErr", 6),
          ("gateSetReq", 4))
    )


_CadPCGateCtlOpcode_Type.__name__ = "Integer32"
_CadPCGateCtlOpcode_Object = MibTableColumn
cadPCGateCtlOpcode = _CadPCGateCtlOpcode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 70, 1, 1),
    _CadPCGateCtlOpcode_Type()
)
cadPCGateCtlOpcode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCGateCtlOpcode.setStatus("current")
_CadPCGateCtlCount_Type = Counter32
_CadPCGateCtlCount_Object = MibTableColumn
cadPCGateCtlCount = _CadPCGateCtlCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 70, 1, 2),
    _CadPCGateCtlCount_Type()
)
cadPCGateCtlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCGateCtlCount.setStatus("current")


class _CadPCGateCtlCountLastCleared_Type(TimeStamp):
    """Custom type cadPCGateCtlCountLastCleared based on TimeStamp"""
    defaultValue = 0


_CadPCGateCtlCountLastCleared_Object = MibScalar
cadPCGateCtlCountLastCleared = _CadPCGateCtlCountLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 71),
    _CadPCGateCtlCountLastCleared_Type()
)
cadPCGateCtlCountLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCGateCtlCountLastCleared.setStatus("current")
_CadPCDefAdmCtlTable_Object = MibTable
cadPCDefAdmCtlTable = _CadPCDefAdmCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 75)
)
if mibBuilder.loadTexts:
    cadPCDefAdmCtlTable.setStatus("current")
_CadPCDefAdmCtlEntry_Object = MibTableRow
cadPCDefAdmCtlEntry = _CadPCDefAdmCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 75, 1)
)
cadPCDefAdmCtlEntry.setIndexNames(
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCDefAdmCtlDirection"),
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCDefAdmCtlPriority"),
)
if mibBuilder.loadTexts:
    cadPCDefAdmCtlEntry.setStatus("current")
_CadPCDefAdmCtlDirection_Type = IfDirection
_CadPCDefAdmCtlDirection_Object = MibTableColumn
cadPCDefAdmCtlDirection = _CadPCDefAdmCtlDirection_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 75, 1, 1),
    _CadPCDefAdmCtlDirection_Type()
)
cadPCDefAdmCtlDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCDefAdmCtlDirection.setStatus("current")
_CadPCDefAdmCtlPriority_Type = CadPCAdmCtlPriority
_CadPCDefAdmCtlPriority_Object = MibTableColumn
cadPCDefAdmCtlPriority = _CadPCDefAdmCtlPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 75, 1, 2),
    _CadPCDefAdmCtlPriority_Type()
)
cadPCDefAdmCtlPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCDefAdmCtlPriority.setStatus("current")


class _CadPCDefAdmCtlAllowedUsage_Type(Integer32):
    """Custom type cadPCDefAdmCtlAllowedUsage based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_CadPCDefAdmCtlAllowedUsage_Type.__name__ = "Integer32"
_CadPCDefAdmCtlAllowedUsage_Object = MibTableColumn
cadPCDefAdmCtlAllowedUsage = _CadPCDefAdmCtlAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 75, 1, 3),
    _CadPCDefAdmCtlAllowedUsage_Type()
)
cadPCDefAdmCtlAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCDefAdmCtlAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCDefAdmCtlAllowedUsage.setUnits("percent")


class _CadPCDefAdmCtlReservedUsage_Type(Integer32):
    """Custom type cadPCDefAdmCtlReservedUsage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_CadPCDefAdmCtlReservedUsage_Type.__name__ = "Integer32"
_CadPCDefAdmCtlReservedUsage_Object = MibTableColumn
cadPCDefAdmCtlReservedUsage = _CadPCDefAdmCtlReservedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 75, 1, 4),
    _CadPCDefAdmCtlReservedUsage_Type()
)
cadPCDefAdmCtlReservedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCDefAdmCtlReservedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCDefAdmCtlReservedUsage.setUnits("percent")
_CadPC1xAdmCtlMapTable_Object = MibTable
cadPC1xAdmCtlMapTable = _CadPC1xAdmCtlMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 80)
)
if mibBuilder.loadTexts:
    cadPC1xAdmCtlMapTable.setStatus("current")
_CadPC1xAdmCtlMapEntry_Object = MibTableRow
cadPC1xAdmCtlMapEntry = _CadPC1xAdmCtlMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 80, 1)
)
cadPC1xAdmCtlMapEntry.setIndexNames(
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPC1xAdmCtlMapPriority"),
)
if mibBuilder.loadTexts:
    cadPC1xAdmCtlMapEntry.setStatus("current")


class _CadPC1xAdmCtlMapPriority_Type(Integer32):
    """Custom type cadPC1xAdmCtlMapPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 3),
          ("normal", 2),
          ("undefined", 1))
    )


_CadPC1xAdmCtlMapPriority_Type.__name__ = "Integer32"
_CadPC1xAdmCtlMapPriority_Object = MibTableColumn
cadPC1xAdmCtlMapPriority = _CadPC1xAdmCtlMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 80, 1, 1),
    _CadPC1xAdmCtlMapPriority_Type()
)
cadPC1xAdmCtlMapPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPC1xAdmCtlMapPriority.setStatus("current")
_CadPCAdmCtlMapPriority_Type = CadPCAdmCtlPriority
_CadPCAdmCtlMapPriority_Object = MibTableColumn
cadPCAdmCtlMapPriority = _CadPCAdmCtlMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 80, 1, 2),
    _CadPCAdmCtlMapPriority_Type()
)
cadPCAdmCtlMapPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPCAdmCtlMapPriority.setStatus("current")
_CadPCInterfaceAdmCtlTable_Object = MibTable
cadPCInterfaceAdmCtlTable = _CadPCInterfaceAdmCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 85)
)
if mibBuilder.loadTexts:
    cadPCInterfaceAdmCtlTable.setStatus("current")
_CadPCInterfaceAdmCtlEntry_Object = MibTableRow
cadPCInterfaceAdmCtlEntry = _CadPCInterfaceAdmCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 85, 1)
)
cadPCInterfaceAdmCtlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCInterfaceAdmCtlPriority"),
)
if mibBuilder.loadTexts:
    cadPCInterfaceAdmCtlEntry.setStatus("current")
_CadPCInterfaceAdmCtlPriority_Type = CadPCAdmCtlPriority
_CadPCInterfaceAdmCtlPriority_Object = MibTableColumn
cadPCInterfaceAdmCtlPriority = _CadPCInterfaceAdmCtlPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 85, 1, 1),
    _CadPCInterfaceAdmCtlPriority_Type()
)
cadPCInterfaceAdmCtlPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCInterfaceAdmCtlPriority.setStatus("current")


class _CadPCInterfaceAdmCtlAllowedUsage_Type(Integer32):
    """Custom type cadPCInterfaceAdmCtlAllowedUsage based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_CadPCInterfaceAdmCtlAllowedUsage_Type.__name__ = "Integer32"
_CadPCInterfaceAdmCtlAllowedUsage_Object = MibTableColumn
cadPCInterfaceAdmCtlAllowedUsage = _CadPCInterfaceAdmCtlAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 85, 1, 2),
    _CadPCInterfaceAdmCtlAllowedUsage_Type()
)
cadPCInterfaceAdmCtlAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCInterfaceAdmCtlAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCInterfaceAdmCtlAllowedUsage.setUnits("percent")


class _CadPCInterfaceAdmCtlReservedUsage_Type(Integer32):
    """Custom type cadPCInterfaceAdmCtlReservedUsage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_CadPCInterfaceAdmCtlReservedUsage_Type.__name__ = "Integer32"
_CadPCInterfaceAdmCtlReservedUsage_Object = MibTableColumn
cadPCInterfaceAdmCtlReservedUsage = _CadPCInterfaceAdmCtlReservedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 85, 1, 3),
    _CadPCInterfaceAdmCtlReservedUsage_Type()
)
cadPCInterfaceAdmCtlReservedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCInterfaceAdmCtlReservedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadPCInterfaceAdmCtlReservedUsage.setUnits("percent")
_CadPCCAMCblMacTable_Object = MibTable
cadPCCAMCblMacTable = _CadPCCAMCblMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 86)
)
if mibBuilder.loadTexts:
    cadPCCAMCblMacTable.setStatus("current")
_CadPCCAMCblMacEntry_Object = MibTableRow
cadPCCAMCblMacEntry = _CadPCCAMCblMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 86, 1)
)
cadPCCAMCblMacEntry.setIndexNames(
    (0, "CADANT-CMTS-PACKETCABLE-MIB", "cadPCCAMCblMacIfIndex"),
)
if mibBuilder.loadTexts:
    cadPCCAMCblMacEntry.setStatus("current")
_CadPCCAMCblMacIfIndex_Type = InterfaceIndex
_CadPCCAMCblMacIfIndex_Object = MibTableColumn
cadPCCAMCblMacIfIndex = _CadPCCAMCblMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 86, 1, 1),
    _CadPCCAMCblMacIfIndex_Type()
)
cadPCCAMCblMacIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPCCAMCblMacIfIndex.setStatus("current")


class _CadPCCAMCblMacFreeDSxAllowed_Type(TruthValue):
    """Custom type cadPCCAMCblMacFreeDSxAllowed based on TruthValue"""


_CadPCCAMCblMacFreeDSxAllowed_Object = MibTableColumn
cadPCCAMCblMacFreeDSxAllowed = _CadPCCAMCblMacFreeDSxAllowed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 86, 1, 2),
    _CadPCCAMCblMacFreeDSxAllowed_Type()
)
cadPCCAMCblMacFreeDSxAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCCAMCblMacFreeDSxAllowed.setStatus("current")


class _CadPCCblMacMaxOverloadDSaCalls_Type(Unsigned32):
    """Custom type cadPCCblMacMaxOverloadDSaCalls based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CadPCCblMacMaxOverloadDSaCalls_Type.__name__ = "Unsigned32"
_CadPCCblMacMaxOverloadDSaCalls_Object = MibTableColumn
cadPCCblMacMaxOverloadDSaCalls = _CadPCCblMacMaxOverloadDSaCalls_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 86, 1, 3),
    _CadPCCblMacMaxOverloadDSaCalls_Type()
)
cadPCCblMacMaxOverloadDSaCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCCblMacMaxOverloadDSaCalls.setStatus("current")
if mibBuilder.loadTexts:
    cadPCCblMacMaxOverloadDSaCalls.setUnits("connections per 10 seconds")


class _CadPCCblMacMaxYellowOverloadDSaCalls_Type(Unsigned32):
    """Custom type cadPCCblMacMaxYellowOverloadDSaCalls based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CadPCCblMacMaxYellowOverloadDSaCalls_Type.__name__ = "Unsigned32"
_CadPCCblMacMaxYellowOverloadDSaCalls_Object = MibTableColumn
cadPCCblMacMaxYellowOverloadDSaCalls = _CadPCCblMacMaxYellowOverloadDSaCalls_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 86, 1, 4),
    _CadPCCblMacMaxYellowOverloadDSaCalls_Type()
)
cadPCCblMacMaxYellowOverloadDSaCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCCblMacMaxYellowOverloadDSaCalls.setStatus("current")
if mibBuilder.loadTexts:
    cadPCCblMacMaxYellowOverloadDSaCalls.setUnits("connections per 10 seconds")


class _CadPCCblMacMaxRedOverloadDSaCalls_Type(Unsigned32):
    """Custom type cadPCCblMacMaxRedOverloadDSaCalls based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CadPCCblMacMaxRedOverloadDSaCalls_Type.__name__ = "Unsigned32"
_CadPCCblMacMaxRedOverloadDSaCalls_Object = MibTableColumn
cadPCCblMacMaxRedOverloadDSaCalls = _CadPCCblMacMaxRedOverloadDSaCalls_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 86, 1, 5),
    _CadPCCblMacMaxRedOverloadDSaCalls_Type()
)
cadPCCblMacMaxRedOverloadDSaCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCCblMacMaxRedOverloadDSaCalls.setStatus("current")
if mibBuilder.loadTexts:
    cadPCCblMacMaxRedOverloadDSaCalls.setUnits("connections per 10 seconds")


class _CadPCPEPIDHostname_Type(TruthValue):
    """Custom type cadPCPEPIDHostname based on TruthValue"""


_CadPCPEPIDHostname_Object = MibScalar
cadPCPEPIDHostname = _CadPCPEPIDHostname_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 1, 90),
    _CadPCPEPIDHostname_Type()
)
cadPCPEPIDHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCPEPIDHostname.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-PACKETCABLE-MIB",
    **{"CadPCAnomalyCode": CadPCAnomalyCode,
       "CadPCAdmCtlPriority": CadPCAdmCtlPriority,
       "cadPCMIB": cadPCMIB,
       "cadPCMibObjects": cadPCMibObjects,
       "cadPCMibBase": cadPCMibBase,
       "cadPCPreemptionAllowed": cadPCPreemptionAllowed,
       "cadPCUpNormAllowedUsage": cadPCUpNormAllowedUsage,
       "cadPCUpNormResUsage": cadPCUpNormResUsage,
       "cadPCUpEmerAllowedUsage": cadPCUpEmerAllowedUsage,
       "cadPCUpEmerResUsage": cadPCUpEmerResUsage,
       "cadPCDownNormAllowedUsage": cadPCDownNormAllowedUsage,
       "cadPCDownNormResUsage": cadPCDownNormResUsage,
       "cadPCDownEmerAllowedUsage": cadPCDownEmerAllowedUsage,
       "cadPCDownEmerResUsage": cadPCDownEmerResUsage,
       "cadPCCAMTable": cadPCCAMTable,
       "cadPCCAMEntry": cadPCCAMEntry,
       "cadFreeDSxAllowed": cadFreeDSxAllowed,
       "cadPCMaxOverloadDSaCalls": cadPCMaxOverloadDSaCalls,
       "cadPCMaxYellowOverloadDSaCalls": cadPCMaxYellowOverloadDSaCalls,
       "cadPCMaxRedOverloadDSaCalls": cadPCMaxRedOverloadDSaCalls,
       "cadPCCardId": cadPCCardId,
       "cadPCAdminState": cadPCAdminState,
       "cadPCMaxOverloadCalls": cadPCMaxOverloadCalls,
       "cadPCMaxYellowOverloadCalls": cadPCMaxYellowOverloadCalls,
       "cadPCMaxRedOverloadCalls": cadPCMaxRedOverloadCalls,
       "cadPCDownTotalAllowedUsage": cadPCDownTotalAllowedUsage,
       "cadPCUpTotalAllowedUsage": cadPCUpTotalAllowedUsage,
       "cadPCMaxOverloadGateMsgs": cadPCMaxOverloadGateMsgs,
       "cadPCMaxYellowOverloadGateMsgs": cadPCMaxYellowOverloadGateMsgs,
       "cadPCMaxRedOverloadGateMsgs": cadPCMaxRedOverloadGateMsgs,
       "cadPCClearGateCounts": cadPCClearGateCounts,
       "cadPCClearAnomalyCounts": cadPCClearAnomalyCounts,
       "cadPCClearConnRateOverloadCounts": cadPCClearConnRateOverloadCounts,
       "cadPCClearEvMsgCounts": cadPCClearEvMsgCounts,
       "cadPCClearCopsCounts": cadPCClearCopsCounts,
       "cadPCClearGateCtlCounts": cadPCClearGateCtlCounts,
       "cadPCMibGateCounts": cadPCMibGateCounts,
       "cadPCTotalGateCount": cadPCTotalGateCount,
       "cadPCGateAllocatedStateCount": cadPCGateAllocatedStateCount,
       "cadPCGateAuthorizedStateCount": cadPCGateAuthorizedStateCount,
       "cadPCGateReservedStateCount": cadPCGateReservedStateCount,
       "cadPCGateCommittedStateCount": cadPCGateCommittedStateCount,
       "cadPCGateLastCleared": cadPCGateLastCleared,
       "cadPCAnomalyCountTable": cadPCAnomalyCountTable,
       "cadPCAnomalyCountEntry": cadPCAnomalyCountEntry,
       "cadPCAnomalyCode": cadPCAnomalyCode,
       "cadPCAnomalyCount": cadPCAnomalyCount,
       "cadPCAnomalyLastCleared": cadPCAnomalyLastCleared,
       "cadPCSendSubId": cadPCSendSubId,
       "cadPCConnRateReqHistoryTable": cadPCConnRateReqHistoryTable,
       "cadPCConnRateReqHistoryEntry": cadPCConnRateReqHistoryEntry,
       "cadPCConnRateReqHistoryTimeStamp": cadPCConnRateReqHistoryTimeStamp,
       "cadPCConnRateReqHistoryCount": cadPCConnRateReqHistoryCount,
       "cadPCConnReqMaxHistRate": cadPCConnReqMaxHistRate,
       "cadPCConnRateOverloadRejTable": cadPCConnRateOverloadRejTable,
       "cadPCConnRateOverloadRejEntry": cadPCConnRateOverloadRejEntry,
       "cadPCConnRateOverloadRejCount": cadPCConnRateOverloadRejCount,
       "cadPCConnRateOverloadRejCardId": cadPCConnRateOverloadRejCardId,
       "cadPCConnRateOverloadLastCleared": cadPCConnRateOverloadLastCleared,
       "cadPCEvMsgCountTable": cadPCEvMsgCountTable,
       "cadPCEvMsgCountEntry": cadPCEvMsgCountEntry,
       "cadPCEvMsgCountServer": cadPCEvMsgCountServer,
       "cadPCEvMsgServerIsDF": cadPCEvMsgServerIsDF,
       "cadPCEvMsgType": cadPCEvMsgType,
       "cadPCEvMsgCount": cadPCEvMsgCount,
       "cadPCEvMsgCountLastCleared": cadPCEvMsgCountLastCleared,
       "cadPCCopsCountTable": cadPCCopsCountTable,
       "cadPCCopsCountEntry": cadPCCopsCountEntry,
       "cadPCCopsServer": cadPCCopsServer,
       "cadPCCopsDirection": cadPCCopsDirection,
       "cadPCCopsOpcode": cadPCCopsOpcode,
       "cadPCCopsCount": cadPCCopsCount,
       "cadPCCopsCountLastCleared": cadPCCopsCountLastCleared,
       "cadPCGateCtlCountTable": cadPCGateCtlCountTable,
       "cadPCGateCtlCountEntry": cadPCGateCtlCountEntry,
       "cadPCGateCtlOpcode": cadPCGateCtlOpcode,
       "cadPCGateCtlCount": cadPCGateCtlCount,
       "cadPCGateCtlCountLastCleared": cadPCGateCtlCountLastCleared,
       "cadPCDefAdmCtlTable": cadPCDefAdmCtlTable,
       "cadPCDefAdmCtlEntry": cadPCDefAdmCtlEntry,
       "cadPCDefAdmCtlDirection": cadPCDefAdmCtlDirection,
       "cadPCDefAdmCtlPriority": cadPCDefAdmCtlPriority,
       "cadPCDefAdmCtlAllowedUsage": cadPCDefAdmCtlAllowedUsage,
       "cadPCDefAdmCtlReservedUsage": cadPCDefAdmCtlReservedUsage,
       "cadPC1xAdmCtlMapTable": cadPC1xAdmCtlMapTable,
       "cadPC1xAdmCtlMapEntry": cadPC1xAdmCtlMapEntry,
       "cadPC1xAdmCtlMapPriority": cadPC1xAdmCtlMapPriority,
       "cadPCAdmCtlMapPriority": cadPCAdmCtlMapPriority,
       "cadPCInterfaceAdmCtlTable": cadPCInterfaceAdmCtlTable,
       "cadPCInterfaceAdmCtlEntry": cadPCInterfaceAdmCtlEntry,
       "cadPCInterfaceAdmCtlPriority": cadPCInterfaceAdmCtlPriority,
       "cadPCInterfaceAdmCtlAllowedUsage": cadPCInterfaceAdmCtlAllowedUsage,
       "cadPCInterfaceAdmCtlReservedUsage": cadPCInterfaceAdmCtlReservedUsage,
       "cadPCCAMCblMacTable": cadPCCAMCblMacTable,
       "cadPCCAMCblMacEntry": cadPCCAMCblMacEntry,
       "cadPCCAMCblMacIfIndex": cadPCCAMCblMacIfIndex,
       "cadPCCAMCblMacFreeDSxAllowed": cadPCCAMCblMacFreeDSxAllowed,
       "cadPCCblMacMaxOverloadDSaCalls": cadPCCblMacMaxOverloadDSaCalls,
       "cadPCCblMacMaxYellowOverloadDSaCalls": cadPCCblMacMaxYellowOverloadDSaCalls,
       "cadPCCblMacMaxRedOverloadDSaCalls": cadPCCblMacMaxRedOverloadDSaCalls,
       "cadPCPEPIDHostname": cadPCPEPIDHostname}
)
