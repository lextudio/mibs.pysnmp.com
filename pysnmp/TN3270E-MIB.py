# SNMP MIB module (TN3270E-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TN3270E-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:28 2024
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

(IANATn3270DeviceType,
 IANATn3270Functions,
 IANATn3270ResourceType,
 IANATn3270eAddrType,
 IANATn3270eAddress,
 IANATn3270eClientType,
 IANATn3270eLogData) = mibBuilder.importSymbols(
    "IANATn3270eTC-MIB",
    "IANATn3270DeviceType",
    "IANATn3270Functions",
    "IANATn3270ResourceType",
    "IANATn3270eAddrType",
    "IANATn3270eAddress",
    "IANATn3270eClientType",
    "IANATn3270eLogData")

(snanauMIB,) = mibBuilder.importSymbols(
    "SNA-NAU-MIB",
    "snanauMIB")

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
 TestAndIncr,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp")

(Utf8String,) = mibBuilder.importSymbols(
    "SYSAPPL-MIB",
    "Utf8String")


# MODULE-IDENTITY

tn3270eMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 34, 8)
)
tn3270eMIB.setRevisions(
        ("2006-01-13 00:00",
         "1998-07-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SnaResourceName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )



class Tn3270eTraceData(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 4096),
    )



# MIB Managed Objects in the order of their OIDs

_Tn3270eNotifications_ObjectIdentity = ObjectIdentity
tn3270eNotifications = _Tn3270eNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 8, 0)
)
_Tn3270eObjects_ObjectIdentity = ObjectIdentity
tn3270eObjects = _Tn3270eObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 8, 1)
)
_Tn3270eSrvrConfTable_Object = MibTable
tn3270eSrvrConfTable = _Tn3270eSrvrConfTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1)
)
if mibBuilder.loadTexts:
    tn3270eSrvrConfTable.setStatus("current")
_Tn3270eSrvrConfEntry_Object = MibTableRow
tn3270eSrvrConfEntry = _Tn3270eSrvrConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1)
)
tn3270eSrvrConfEntry.setIndexNames(
    (0, "TN3270E-MIB", "tn3270eSrvrConfIndex"),
)
if mibBuilder.loadTexts:
    tn3270eSrvrConfEntry.setStatus("current")


class _Tn3270eSrvrConfIndex_Type(Unsigned32):
    """Custom type tn3270eSrvrConfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Tn3270eSrvrConfIndex_Type.__name__ = "Unsigned32"
_Tn3270eSrvrConfIndex_Object = MibTableColumn
tn3270eSrvrConfIndex = _Tn3270eSrvrConfIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 1),
    _Tn3270eSrvrConfIndex_Type()
)
tn3270eSrvrConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eSrvrConfIndex.setStatus("current")


class _Tn3270eSrvrConfInactivityTimeout_Type(Unsigned32):
    """Custom type tn3270eSrvrConfInactivityTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999999),
    )


_Tn3270eSrvrConfInactivityTimeout_Type.__name__ = "Unsigned32"
_Tn3270eSrvrConfInactivityTimeout_Object = MibTableColumn
tn3270eSrvrConfInactivityTimeout = _Tn3270eSrvrConfInactivityTimeout_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 2),
    _Tn3270eSrvrConfInactivityTimeout_Type()
)
tn3270eSrvrConfInactivityTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eSrvrConfInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrConfInactivityTimeout.setUnits("seconds")


class _Tn3270eSrvrConfConnectivityChk_Type(Integer32):
    """Custom type tn3270eSrvrConfConnectivityChk based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noCheck", 3),
          ("nop", 2),
          ("timingMark", 1))
    )


_Tn3270eSrvrConfConnectivityChk_Type.__name__ = "Integer32"
_Tn3270eSrvrConfConnectivityChk_Object = MibTableColumn
tn3270eSrvrConfConnectivityChk = _Tn3270eSrvrConfConnectivityChk_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 3),
    _Tn3270eSrvrConfConnectivityChk_Type()
)
tn3270eSrvrConfConnectivityChk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eSrvrConfConnectivityChk.setStatus("current")


class _Tn3270eSrvrConfTmNopInactTime_Type(Unsigned32):
    """Custom type tn3270eSrvrConfTmNopInactTime based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_Tn3270eSrvrConfTmNopInactTime_Type.__name__ = "Unsigned32"
_Tn3270eSrvrConfTmNopInactTime_Object = MibTableColumn
tn3270eSrvrConfTmNopInactTime = _Tn3270eSrvrConfTmNopInactTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 4),
    _Tn3270eSrvrConfTmNopInactTime_Type()
)
tn3270eSrvrConfTmNopInactTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eSrvrConfTmNopInactTime.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrConfTmNopInactTime.setUnits("seconds")


class _Tn3270eSrvrConfTmNopInterval_Type(Unsigned32):
    """Custom type tn3270eSrvrConfTmNopInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_Tn3270eSrvrConfTmNopInterval_Type.__name__ = "Unsigned32"
_Tn3270eSrvrConfTmNopInterval_Object = MibTableColumn
tn3270eSrvrConfTmNopInterval = _Tn3270eSrvrConfTmNopInterval_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 5),
    _Tn3270eSrvrConfTmNopInterval_Type()
)
tn3270eSrvrConfTmNopInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eSrvrConfTmNopInterval.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrConfTmNopInterval.setUnits("seconds")


class _Tn3270eSrvrFunctionsSupported_Type(IANATn3270Functions):
    """Custom type tn3270eSrvrFunctionsSupported based on IANATn3270Functions"""
    defaultBinValue = "0000011111"


_Tn3270eSrvrFunctionsSupported_Object = MibTableColumn
tn3270eSrvrFunctionsSupported = _Tn3270eSrvrFunctionsSupported_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 6),
    _Tn3270eSrvrFunctionsSupported_Type()
)
tn3270eSrvrFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrFunctionsSupported.setStatus("current")


class _Tn3270eSrvrConfAdminStatus_Type(Integer32):
    """Custom type tn3270eSrvrConfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("stopImmediate", 3),
          ("up", 1))
    )


_Tn3270eSrvrConfAdminStatus_Type.__name__ = "Integer32"
_Tn3270eSrvrConfAdminStatus_Object = MibTableColumn
tn3270eSrvrConfAdminStatus = _Tn3270eSrvrConfAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 7),
    _Tn3270eSrvrConfAdminStatus_Type()
)
tn3270eSrvrConfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eSrvrConfAdminStatus.setStatus("current")


class _Tn3270eSrvrConfOperStatus_Type(Integer32):
    """Custom type tn3270eSrvrConfOperStatus based on Integer32"""
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
        *(("busy", 3),
          ("down", 2),
          ("shuttingDown", 4),
          ("up", 1))
    )


_Tn3270eSrvrConfOperStatus_Type.__name__ = "Integer32"
_Tn3270eSrvrConfOperStatus_Object = MibTableColumn
tn3270eSrvrConfOperStatus = _Tn3270eSrvrConfOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 8),
    _Tn3270eSrvrConfOperStatus_Type()
)
tn3270eSrvrConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrConfOperStatus.setStatus("current")


class _Tn3270eSrvrConfSessionTermState_Type(Integer32):
    """Custom type tn3270eSrvrConfSessionTermState based on Integer32"""
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
        *(("luSessionPend", 2),
          ("queueSession", 3),
          ("terminate", 1))
    )


_Tn3270eSrvrConfSessionTermState_Type.__name__ = "Integer32"
_Tn3270eSrvrConfSessionTermState_Object = MibTableColumn
tn3270eSrvrConfSessionTermState = _Tn3270eSrvrConfSessionTermState_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 9),
    _Tn3270eSrvrConfSessionTermState_Type()
)
tn3270eSrvrConfSessionTermState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eSrvrConfSessionTermState.setStatus("current")


class _Tn3270eSrvrConfSrvrType_Type(Integer32):
    """Custom type tn3270eSrvrConfSrvrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gateway", 2),
          ("host", 1))
    )


_Tn3270eSrvrConfSrvrType_Type.__name__ = "Integer32"
_Tn3270eSrvrConfSrvrType_Object = MibTableColumn
tn3270eSrvrConfSrvrType = _Tn3270eSrvrConfSrvrType_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 10),
    _Tn3270eSrvrConfSrvrType_Type()
)
tn3270eSrvrConfSrvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrConfSrvrType.setStatus("current")


class _Tn3270eSrvrConfContact_Type(SnmpAdminString):
    """Custom type tn3270eSrvrConfContact based on SnmpAdminString"""
    defaultHexValue = ""


_Tn3270eSrvrConfContact_Object = MibTableColumn
tn3270eSrvrConfContact = _Tn3270eSrvrConfContact_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 11),
    _Tn3270eSrvrConfContact_Type()
)
tn3270eSrvrConfContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eSrvrConfContact.setStatus("current")
_Tn3270eSrvrConfRowStatus_Type = RowStatus
_Tn3270eSrvrConfRowStatus_Object = MibTableColumn
tn3270eSrvrConfRowStatus = _Tn3270eSrvrConfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 12),
    _Tn3270eSrvrConfRowStatus_Type()
)
tn3270eSrvrConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eSrvrConfRowStatus.setStatus("current")


class _Tn3270eSrvrConfLastActTime_Type(DateAndTime):
    """Custom type tn3270eSrvrConfLastActTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_Tn3270eSrvrConfLastActTime_Object = MibTableColumn
tn3270eSrvrConfLastActTime = _Tn3270eSrvrConfLastActTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 13),
    _Tn3270eSrvrConfLastActTime_Type()
)
tn3270eSrvrConfLastActTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrConfLastActTime.setStatus("current")


class _Tn3270eSrvrConfTmTimeout_Type(Unsigned32):
    """Custom type tn3270eSrvrConfTmTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_Tn3270eSrvrConfTmTimeout_Type.__name__ = "Unsigned32"
_Tn3270eSrvrConfTmTimeout_Object = MibTableColumn
tn3270eSrvrConfTmTimeout = _Tn3270eSrvrConfTmTimeout_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 14),
    _Tn3270eSrvrConfTmTimeout_Type()
)
tn3270eSrvrConfTmTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eSrvrConfTmTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrConfTmTimeout.setUnits("seconds")
_Tn3270eSrvrPortTable_Object = MibTable
tn3270eSrvrPortTable = _Tn3270eSrvrPortTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 2)
)
if mibBuilder.loadTexts:
    tn3270eSrvrPortTable.setStatus("current")
_Tn3270eSrvrPortEntry_Object = MibTableRow
tn3270eSrvrPortEntry = _Tn3270eSrvrPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1)
)
tn3270eSrvrPortEntry.setIndexNames(
    (0, "TN3270E-MIB", "tn3270eSrvrConfIndex"),
    (0, "TN3270E-MIB", "tn3270eSrvrPort"),
    (0, "TN3270E-MIB", "tn3270eSrvrPortAddrType"),
    (0, "TN3270E-MIB", "tn3270eSrvrPortAddress"),
)
if mibBuilder.loadTexts:
    tn3270eSrvrPortEntry.setStatus("current")


class _Tn3270eSrvrPort_Type(Unsigned32):
    """Custom type tn3270eSrvrPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tn3270eSrvrPort_Type.__name__ = "Unsigned32"
_Tn3270eSrvrPort_Object = MibTableColumn
tn3270eSrvrPort = _Tn3270eSrvrPort_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1, 1),
    _Tn3270eSrvrPort_Type()
)
tn3270eSrvrPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eSrvrPort.setStatus("current")
_Tn3270eSrvrPortAddrType_Type = IANATn3270eAddrType
_Tn3270eSrvrPortAddrType_Object = MibTableColumn
tn3270eSrvrPortAddrType = _Tn3270eSrvrPortAddrType_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1, 2),
    _Tn3270eSrvrPortAddrType_Type()
)
tn3270eSrvrPortAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eSrvrPortAddrType.setStatus("current")
_Tn3270eSrvrPortAddress_Type = IANATn3270eAddress
_Tn3270eSrvrPortAddress_Object = MibTableColumn
tn3270eSrvrPortAddress = _Tn3270eSrvrPortAddress_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1, 3),
    _Tn3270eSrvrPortAddress_Type()
)
tn3270eSrvrPortAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eSrvrPortAddress.setStatus("current")
_Tn3270eSrvrPortRowStatus_Type = RowStatus
_Tn3270eSrvrPortRowStatus_Object = MibTableColumn
tn3270eSrvrPortRowStatus = _Tn3270eSrvrPortRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1, 4),
    _Tn3270eSrvrPortRowStatus_Type()
)
tn3270eSrvrPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eSrvrPortRowStatus.setStatus("current")
_Tn3270eSrvrStatsTable_Object = MibTable
tn3270eSrvrStatsTable = _Tn3270eSrvrStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3)
)
if mibBuilder.loadTexts:
    tn3270eSrvrStatsTable.setStatus("current")
_Tn3270eSrvrStatsEntry_Object = MibTableRow
tn3270eSrvrStatsEntry = _Tn3270eSrvrStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1)
)
tn3270eSrvrStatsEntry.setIndexNames(
    (0, "TN3270E-MIB", "tn3270eSrvrConfIndex"),
    (0, "TN3270E-MIB", "tn3270eSrvrPort"),
    (0, "TN3270E-MIB", "tn3270eSrvrPortAddrType"),
    (0, "TN3270E-MIB", "tn3270eSrvrPortAddress"),
)
if mibBuilder.loadTexts:
    tn3270eSrvrStatsEntry.setStatus("current")
_Tn3270eSrvrStatsUpTime_Type = TimeStamp
_Tn3270eSrvrStatsUpTime_Object = MibTableColumn
tn3270eSrvrStatsUpTime = _Tn3270eSrvrStatsUpTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 2),
    _Tn3270eSrvrStatsUpTime_Type()
)
tn3270eSrvrStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsUpTime.setStatus("current")
_Tn3270eSrvrStatsMaxTerms_Type = Unsigned32
_Tn3270eSrvrStatsMaxTerms_Object = MibTableColumn
tn3270eSrvrStatsMaxTerms = _Tn3270eSrvrStatsMaxTerms_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 3),
    _Tn3270eSrvrStatsMaxTerms_Type()
)
tn3270eSrvrStatsMaxTerms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsMaxTerms.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsMaxTerms.setUnits("LUs")
_Tn3270eSrvrStatsInUseTerms_Type = Gauge32
_Tn3270eSrvrStatsInUseTerms_Object = MibTableColumn
tn3270eSrvrStatsInUseTerms = _Tn3270eSrvrStatsInUseTerms_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 4),
    _Tn3270eSrvrStatsInUseTerms_Type()
)
tn3270eSrvrStatsInUseTerms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsInUseTerms.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsInUseTerms.setUnits("LUs")
_Tn3270eSrvrStatsSpareTerms_Type = Gauge32
_Tn3270eSrvrStatsSpareTerms_Object = MibTableColumn
tn3270eSrvrStatsSpareTerms = _Tn3270eSrvrStatsSpareTerms_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 5),
    _Tn3270eSrvrStatsSpareTerms_Type()
)
tn3270eSrvrStatsSpareTerms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsSpareTerms.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsSpareTerms.setUnits("LUs")
_Tn3270eSrvrStatsMaxPtrs_Type = Unsigned32
_Tn3270eSrvrStatsMaxPtrs_Object = MibTableColumn
tn3270eSrvrStatsMaxPtrs = _Tn3270eSrvrStatsMaxPtrs_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 6),
    _Tn3270eSrvrStatsMaxPtrs_Type()
)
tn3270eSrvrStatsMaxPtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsMaxPtrs.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsMaxPtrs.setUnits("Printer Resources")
_Tn3270eSrvrStatsInUsePtrs_Type = Gauge32
_Tn3270eSrvrStatsInUsePtrs_Object = MibTableColumn
tn3270eSrvrStatsInUsePtrs = _Tn3270eSrvrStatsInUsePtrs_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 7),
    _Tn3270eSrvrStatsInUsePtrs_Type()
)
tn3270eSrvrStatsInUsePtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsInUsePtrs.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsInUsePtrs.setUnits("Printer Resources")
_Tn3270eSrvrStatsSparePtrs_Type = Gauge32
_Tn3270eSrvrStatsSparePtrs_Object = MibTableColumn
tn3270eSrvrStatsSparePtrs = _Tn3270eSrvrStatsSparePtrs_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 8),
    _Tn3270eSrvrStatsSparePtrs_Type()
)
tn3270eSrvrStatsSparePtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsSparePtrs.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsSparePtrs.setUnits("Spare Printer Resources")
_Tn3270eSrvrStatsInConnects_Type = Counter32
_Tn3270eSrvrStatsInConnects_Object = MibTableColumn
tn3270eSrvrStatsInConnects = _Tn3270eSrvrStatsInConnects_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 9),
    _Tn3270eSrvrStatsInConnects_Type()
)
tn3270eSrvrStatsInConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsInConnects.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsInConnects.setUnits("connections")
_Tn3270eSrvrStatsConnResrceRejs_Type = Counter32
_Tn3270eSrvrStatsConnResrceRejs_Object = MibTableColumn
tn3270eSrvrStatsConnResrceRejs = _Tn3270eSrvrStatsConnResrceRejs_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 10),
    _Tn3270eSrvrStatsConnResrceRejs_Type()
)
tn3270eSrvrStatsConnResrceRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsConnResrceRejs.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsConnResrceRejs.setUnits("connection attempts")
_Tn3270eSrvrStatsDisconnects_Type = Counter32
_Tn3270eSrvrStatsDisconnects_Object = MibTableColumn
tn3270eSrvrStatsDisconnects = _Tn3270eSrvrStatsDisconnects_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 11),
    _Tn3270eSrvrStatsDisconnects_Type()
)
tn3270eSrvrStatsDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsDisconnects.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsDisconnects.setUnits("disconnections")
_Tn3270eSrvrStatsHCInOctets_Type = Counter64
_Tn3270eSrvrStatsHCInOctets_Object = MibTableColumn
tn3270eSrvrStatsHCInOctets = _Tn3270eSrvrStatsHCInOctets_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 12),
    _Tn3270eSrvrStatsHCInOctets_Type()
)
tn3270eSrvrStatsHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsHCInOctets.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsHCInOctets.setUnits("octets")
_Tn3270eSrvrStatsInOctets_Type = Counter32
_Tn3270eSrvrStatsInOctets_Object = MibTableColumn
tn3270eSrvrStatsInOctets = _Tn3270eSrvrStatsInOctets_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 13),
    _Tn3270eSrvrStatsInOctets_Type()
)
tn3270eSrvrStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsInOctets.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsInOctets.setUnits("octets")
_Tn3270eSrvrStatsHCOutOctets_Type = Counter64
_Tn3270eSrvrStatsHCOutOctets_Object = MibTableColumn
tn3270eSrvrStatsHCOutOctets = _Tn3270eSrvrStatsHCOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 14),
    _Tn3270eSrvrStatsHCOutOctets_Type()
)
tn3270eSrvrStatsHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsHCOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsHCOutOctets.setUnits("octets")
_Tn3270eSrvrStatsOutOctets_Type = Counter32
_Tn3270eSrvrStatsOutOctets_Object = MibTableColumn
tn3270eSrvrStatsOutOctets = _Tn3270eSrvrStatsOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 15),
    _Tn3270eSrvrStatsOutOctets_Type()
)
tn3270eSrvrStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsOutOctets.setUnits("octets")
_Tn3270eSrvrStatsConnErrorRejs_Type = Counter32
_Tn3270eSrvrStatsConnErrorRejs_Object = MibTableColumn
tn3270eSrvrStatsConnErrorRejs = _Tn3270eSrvrStatsConnErrorRejs_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 16),
    _Tn3270eSrvrStatsConnErrorRejs_Type()
)
tn3270eSrvrStatsConnErrorRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsConnErrorRejs.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eSrvrStatsConnErrorRejs.setUnits("connection attempts")
_Tn3270eClientGroupTable_Object = MibTable
tn3270eClientGroupTable = _Tn3270eClientGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 4)
)
if mibBuilder.loadTexts:
    tn3270eClientGroupTable.setStatus("current")
_Tn3270eClientGroupEntry_Object = MibTableRow
tn3270eClientGroupEntry = _Tn3270eClientGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1)
)
tn3270eClientGroupEntry.setIndexNames(
    (0, "TN3270E-MIB", "tn3270eSrvrConfIndex"),
    (0, "TN3270E-MIB", "tn3270eClientGroupName"),
    (0, "TN3270E-MIB", "tn3270eClientGroupAddrType"),
    (0, "TN3270E-MIB", "tn3270eClientGroupAddress"),
)
if mibBuilder.loadTexts:
    tn3270eClientGroupEntry.setStatus("current")


class _Tn3270eClientGroupName_Type(Utf8String):
    """Custom type tn3270eClientGroupName based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Tn3270eClientGroupName_Type.__name__ = "Utf8String"
_Tn3270eClientGroupName_Object = MibTableColumn
tn3270eClientGroupName = _Tn3270eClientGroupName_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 1),
    _Tn3270eClientGroupName_Type()
)
tn3270eClientGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eClientGroupName.setStatus("current")
_Tn3270eClientGroupAddrType_Type = IANATn3270eAddrType
_Tn3270eClientGroupAddrType_Object = MibTableColumn
tn3270eClientGroupAddrType = _Tn3270eClientGroupAddrType_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 2),
    _Tn3270eClientGroupAddrType_Type()
)
tn3270eClientGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eClientGroupAddrType.setStatus("current")
_Tn3270eClientGroupAddress_Type = IANATn3270eAddress
_Tn3270eClientGroupAddress_Object = MibTableColumn
tn3270eClientGroupAddress = _Tn3270eClientGroupAddress_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 3),
    _Tn3270eClientGroupAddress_Type()
)
tn3270eClientGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eClientGroupAddress.setStatus("current")


class _Tn3270eClientGroupSubnetMask_Type(IpAddress):
    """Custom type tn3270eClientGroupSubnetMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_Tn3270eClientGroupSubnetMask_Object = MibTableColumn
tn3270eClientGroupSubnetMask = _Tn3270eClientGroupSubnetMask_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 4),
    _Tn3270eClientGroupSubnetMask_Type()
)
tn3270eClientGroupSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eClientGroupSubnetMask.setStatus("current")


class _Tn3270eClientGroupPfxLength_Type(Unsigned32):
    """Custom type tn3270eClientGroupPfxLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Tn3270eClientGroupPfxLength_Type.__name__ = "Unsigned32"
_Tn3270eClientGroupPfxLength_Object = MibTableColumn
tn3270eClientGroupPfxLength = _Tn3270eClientGroupPfxLength_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 5),
    _Tn3270eClientGroupPfxLength_Type()
)
tn3270eClientGroupPfxLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eClientGroupPfxLength.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eClientGroupPfxLength.setUnits("bits")
_Tn3270eClientGroupRowStatus_Type = RowStatus
_Tn3270eClientGroupRowStatus_Object = MibTableColumn
tn3270eClientGroupRowStatus = _Tn3270eClientGroupRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 6),
    _Tn3270eClientGroupRowStatus_Type()
)
tn3270eClientGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eClientGroupRowStatus.setStatus("current")
_Tn3270eResPoolTable_Object = MibTable
tn3270eResPoolTable = _Tn3270eResPoolTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 5)
)
if mibBuilder.loadTexts:
    tn3270eResPoolTable.setStatus("current")
_Tn3270eResPoolEntry_Object = MibTableRow
tn3270eResPoolEntry = _Tn3270eResPoolEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1)
)
tn3270eResPoolEntry.setIndexNames(
    (0, "TN3270E-MIB", "tn3270eSrvrConfIndex"),
    (0, "TN3270E-MIB", "tn3270eResPoolName"),
    (0, "TN3270E-MIB", "tn3270eResPoolElementName"),
)
if mibBuilder.loadTexts:
    tn3270eResPoolEntry.setStatus("current")


class _Tn3270eResPoolName_Type(Utf8String):
    """Custom type tn3270eResPoolName based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Tn3270eResPoolName_Type.__name__ = "Utf8String"
_Tn3270eResPoolName_Object = MibTableColumn
tn3270eResPoolName = _Tn3270eResPoolName_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1, 1),
    _Tn3270eResPoolName_Type()
)
tn3270eResPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eResPoolName.setStatus("current")
_Tn3270eResPoolElementName_Type = SnaResourceName
_Tn3270eResPoolElementName_Object = MibTableColumn
tn3270eResPoolElementName = _Tn3270eResPoolElementName_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1, 2),
    _Tn3270eResPoolElementName_Type()
)
tn3270eResPoolElementName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eResPoolElementName.setStatus("current")
_Tn3270eResPoolElementType_Type = IANATn3270ResourceType
_Tn3270eResPoolElementType_Object = MibTableColumn
tn3270eResPoolElementType = _Tn3270eResPoolElementType_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1, 3),
    _Tn3270eResPoolElementType_Type()
)
tn3270eResPoolElementType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eResPoolElementType.setStatus("current")
_Tn3270eResPoolRowStatus_Type = RowStatus
_Tn3270eResPoolRowStatus_Object = MibTableColumn
tn3270eResPoolRowStatus = _Tn3270eResPoolRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1, 4),
    _Tn3270eResPoolRowStatus_Type()
)
tn3270eResPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eResPoolRowStatus.setStatus("current")
_Tn3270eSnaMapTable_Object = MibTable
tn3270eSnaMapTable = _Tn3270eSnaMapTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 6)
)
if mibBuilder.loadTexts:
    tn3270eSnaMapTable.setStatus("current")
_Tn3270eSnaMapEntry_Object = MibTableRow
tn3270eSnaMapEntry = _Tn3270eSnaMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 6, 1)
)
tn3270eSnaMapEntry.setIndexNames(
    (0, "TN3270E-MIB", "tn3270eSrvrConfIndex"),
    (0, "TN3270E-MIB", "tn3270eSnaMapSscpSuppliedName"),
)
if mibBuilder.loadTexts:
    tn3270eSnaMapEntry.setStatus("current")
_Tn3270eSnaMapSscpSuppliedName_Type = SnaResourceName
_Tn3270eSnaMapSscpSuppliedName_Object = MibTableColumn
tn3270eSnaMapSscpSuppliedName = _Tn3270eSnaMapSscpSuppliedName_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 6, 1, 1),
    _Tn3270eSnaMapSscpSuppliedName_Type()
)
tn3270eSnaMapSscpSuppliedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eSnaMapSscpSuppliedName.setStatus("current")
_Tn3270eSnaMapLocalName_Type = SnaResourceName
_Tn3270eSnaMapLocalName_Object = MibTableColumn
tn3270eSnaMapLocalName = _Tn3270eSnaMapLocalName_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 6, 1, 2),
    _Tn3270eSnaMapLocalName_Type()
)
tn3270eSnaMapLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSnaMapLocalName.setStatus("current")
_Tn3270eSnaMapPrimaryLuName_Type = SnaResourceName
_Tn3270eSnaMapPrimaryLuName_Object = MibTableColumn
tn3270eSnaMapPrimaryLuName = _Tn3270eSnaMapPrimaryLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 6, 1, 3),
    _Tn3270eSnaMapPrimaryLuName_Type()
)
tn3270eSnaMapPrimaryLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eSnaMapPrimaryLuName.setStatus("current")
_Tn3270eClientResMapTable_Object = MibTable
tn3270eClientResMapTable = _Tn3270eClientResMapTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 7)
)
if mibBuilder.loadTexts:
    tn3270eClientResMapTable.setStatus("current")
_Tn3270eClientResMapEntry_Object = MibTableRow
tn3270eClientResMapEntry = _Tn3270eClientResMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1)
)
tn3270eClientResMapEntry.setIndexNames(
    (0, "TN3270E-MIB", "tn3270eSrvrConfIndex"),
    (0, "TN3270E-MIB", "tn3270eClientResMapPoolName"),
    (0, "TN3270E-MIB", "tn3270eClientResMapClientGroupName"),
    (0, "TN3270E-MIB", "tn3270eClientResMapClientPort"),
)
if mibBuilder.loadTexts:
    tn3270eClientResMapEntry.setStatus("current")


class _Tn3270eClientResMapPoolName_Type(Utf8String):
    """Custom type tn3270eClientResMapPoolName based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Tn3270eClientResMapPoolName_Type.__name__ = "Utf8String"
_Tn3270eClientResMapPoolName_Object = MibTableColumn
tn3270eClientResMapPoolName = _Tn3270eClientResMapPoolName_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1, 1),
    _Tn3270eClientResMapPoolName_Type()
)
tn3270eClientResMapPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eClientResMapPoolName.setStatus("current")


class _Tn3270eClientResMapClientGroupName_Type(Utf8String):
    """Custom type tn3270eClientResMapClientGroupName based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Tn3270eClientResMapClientGroupName_Type.__name__ = "Utf8String"
_Tn3270eClientResMapClientGroupName_Object = MibTableColumn
tn3270eClientResMapClientGroupName = _Tn3270eClientResMapClientGroupName_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1, 2),
    _Tn3270eClientResMapClientGroupName_Type()
)
tn3270eClientResMapClientGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eClientResMapClientGroupName.setStatus("current")


class _Tn3270eClientResMapClientPort_Type(Unsigned32):
    """Custom type tn3270eClientResMapClientPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tn3270eClientResMapClientPort_Type.__name__ = "Unsigned32"
_Tn3270eClientResMapClientPort_Object = MibTableColumn
tn3270eClientResMapClientPort = _Tn3270eClientResMapClientPort_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1, 3),
    _Tn3270eClientResMapClientPort_Type()
)
tn3270eClientResMapClientPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eClientResMapClientPort.setStatus("current")
_Tn3270eClientResMapRowStatus_Type = RowStatus
_Tn3270eClientResMapRowStatus_Object = MibTableColumn
tn3270eClientResMapRowStatus = _Tn3270eClientResMapRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1, 4),
    _Tn3270eClientResMapRowStatus_Type()
)
tn3270eClientResMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eClientResMapRowStatus.setStatus("current")
_Tn3270eResMapTable_Object = MibTable
tn3270eResMapTable = _Tn3270eResMapTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 8)
)
if mibBuilder.loadTexts:
    tn3270eResMapTable.setStatus("current")
_Tn3270eResMapEntry_Object = MibTableRow
tn3270eResMapEntry = _Tn3270eResMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1)
)
tn3270eResMapEntry.setIndexNames(
    (0, "TN3270E-MIB", "tn3270eSrvrConfIndex"),
    (0, "TN3270E-MIB", "tn3270eResMapElementName"),
)
if mibBuilder.loadTexts:
    tn3270eResMapEntry.setStatus("current")
_Tn3270eResMapElementName_Type = SnaResourceName
_Tn3270eResMapElementName_Object = MibTableColumn
tn3270eResMapElementName = _Tn3270eResMapElementName_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 1),
    _Tn3270eResMapElementName_Type()
)
tn3270eResMapElementName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eResMapElementName.setStatus("current")
_Tn3270eResMapAddrType_Type = IANATn3270eAddrType
_Tn3270eResMapAddrType_Object = MibTableColumn
tn3270eResMapAddrType = _Tn3270eResMapAddrType_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 2),
    _Tn3270eResMapAddrType_Type()
)
tn3270eResMapAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eResMapAddrType.setStatus("current")
_Tn3270eResMapAddress_Type = IANATn3270eAddress
_Tn3270eResMapAddress_Object = MibTableColumn
tn3270eResMapAddress = _Tn3270eResMapAddress_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 3),
    _Tn3270eResMapAddress_Type()
)
tn3270eResMapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eResMapAddress.setStatus("current")


class _Tn3270eResMapPort_Type(Unsigned32):
    """Custom type tn3270eResMapPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tn3270eResMapPort_Type.__name__ = "Unsigned32"
_Tn3270eResMapPort_Object = MibTableColumn
tn3270eResMapPort = _Tn3270eResMapPort_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 4),
    _Tn3270eResMapPort_Type()
)
tn3270eResMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eResMapPort.setStatus("current")
_Tn3270eResMapElementType_Type = IANATn3270ResourceType
_Tn3270eResMapElementType_Object = MibTableColumn
tn3270eResMapElementType = _Tn3270eResMapElementType_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 5),
    _Tn3270eResMapElementType_Type()
)
tn3270eResMapElementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eResMapElementType.setStatus("current")
_Tn3270eResMapSscpSuppliedName_Type = SnaResourceName
_Tn3270eResMapSscpSuppliedName_Object = MibTableColumn
tn3270eResMapSscpSuppliedName = _Tn3270eResMapSscpSuppliedName_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 6),
    _Tn3270eResMapSscpSuppliedName_Type()
)
tn3270eResMapSscpSuppliedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eResMapSscpSuppliedName.setStatus("current")
_Tn3270eTcpConnTable_Object = MibTable
tn3270eTcpConnTable = _Tn3270eTcpConnTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9)
)
if mibBuilder.loadTexts:
    tn3270eTcpConnTable.setStatus("current")
_Tn3270eTcpConnEntry_Object = MibTableRow
tn3270eTcpConnEntry = _Tn3270eTcpConnEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1)
)
tn3270eTcpConnEntry.setIndexNames(
    (0, "TN3270E-MIB", "tn3270eTcpConnRemAddrType"),
    (0, "TN3270E-MIB", "tn3270eTcpConnRemAddress"),
    (0, "TN3270E-MIB", "tn3270eTcpConnRemPort"),
    (0, "TN3270E-MIB", "tn3270eTcpConnLocalAddrType"),
    (0, "TN3270E-MIB", "tn3270eTcpConnLocalAddress"),
    (0, "TN3270E-MIB", "tn3270eTcpConnLocalPort"),
)
if mibBuilder.loadTexts:
    tn3270eTcpConnEntry.setStatus("current")
_Tn3270eTcpConnRemAddrType_Type = IANATn3270eAddrType
_Tn3270eTcpConnRemAddrType_Object = MibTableColumn
tn3270eTcpConnRemAddrType = _Tn3270eTcpConnRemAddrType_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 1),
    _Tn3270eTcpConnRemAddrType_Type()
)
tn3270eTcpConnRemAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eTcpConnRemAddrType.setStatus("current")
_Tn3270eTcpConnRemAddress_Type = IANATn3270eAddress
_Tn3270eTcpConnRemAddress_Object = MibTableColumn
tn3270eTcpConnRemAddress = _Tn3270eTcpConnRemAddress_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 2),
    _Tn3270eTcpConnRemAddress_Type()
)
tn3270eTcpConnRemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eTcpConnRemAddress.setStatus("current")


class _Tn3270eTcpConnRemPort_Type(Unsigned32):
    """Custom type tn3270eTcpConnRemPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tn3270eTcpConnRemPort_Type.__name__ = "Unsigned32"
_Tn3270eTcpConnRemPort_Object = MibTableColumn
tn3270eTcpConnRemPort = _Tn3270eTcpConnRemPort_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 3),
    _Tn3270eTcpConnRemPort_Type()
)
tn3270eTcpConnRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eTcpConnRemPort.setStatus("current")
_Tn3270eTcpConnLocalAddrType_Type = IANATn3270eAddrType
_Tn3270eTcpConnLocalAddrType_Object = MibTableColumn
tn3270eTcpConnLocalAddrType = _Tn3270eTcpConnLocalAddrType_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 4),
    _Tn3270eTcpConnLocalAddrType_Type()
)
tn3270eTcpConnLocalAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eTcpConnLocalAddrType.setStatus("current")
_Tn3270eTcpConnLocalAddress_Type = IANATn3270eAddress
_Tn3270eTcpConnLocalAddress_Object = MibTableColumn
tn3270eTcpConnLocalAddress = _Tn3270eTcpConnLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 5),
    _Tn3270eTcpConnLocalAddress_Type()
)
tn3270eTcpConnLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eTcpConnLocalAddress.setStatus("current")


class _Tn3270eTcpConnLocalPort_Type(Unsigned32):
    """Custom type tn3270eTcpConnLocalPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Tn3270eTcpConnLocalPort_Type.__name__ = "Unsigned32"
_Tn3270eTcpConnLocalPort_Object = MibTableColumn
tn3270eTcpConnLocalPort = _Tn3270eTcpConnLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 6),
    _Tn3270eTcpConnLocalPort_Type()
)
tn3270eTcpConnLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eTcpConnLocalPort.setStatus("current")


class _Tn3270eTcpConnLastActivity_Type(TimeTicks):
    """Custom type tn3270eTcpConnLastActivity based on TimeTicks"""
    defaultValue = 0


_Tn3270eTcpConnLastActivity_Object = MibTableColumn
tn3270eTcpConnLastActivity = _Tn3270eTcpConnLastActivity_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 7),
    _Tn3270eTcpConnLastActivity_Type()
)
tn3270eTcpConnLastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnLastActivity.setStatus("current")
_Tn3270eTcpConnBytesIn_Type = Counter32
_Tn3270eTcpConnBytesIn_Object = MibTableColumn
tn3270eTcpConnBytesIn = _Tn3270eTcpConnBytesIn_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 8),
    _Tn3270eTcpConnBytesIn_Type()
)
tn3270eTcpConnBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eTcpConnBytesIn.setUnits("octets")
_Tn3270eTcpConnBytesOut_Type = Counter32
_Tn3270eTcpConnBytesOut_Object = MibTableColumn
tn3270eTcpConnBytesOut = _Tn3270eTcpConnBytesOut_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 9),
    _Tn3270eTcpConnBytesOut_Type()
)
tn3270eTcpConnBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eTcpConnBytesOut.setUnits("octets")
_Tn3270eTcpConnResourceElement_Type = SnaResourceName
_Tn3270eTcpConnResourceElement_Object = MibTableColumn
tn3270eTcpConnResourceElement = _Tn3270eTcpConnResourceElement_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 10),
    _Tn3270eTcpConnResourceElement_Type()
)
tn3270eTcpConnResourceElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnResourceElement.setStatus("current")
_Tn3270eTcpConnResourceType_Type = IANATn3270ResourceType
_Tn3270eTcpConnResourceType_Object = MibTableColumn
tn3270eTcpConnResourceType = _Tn3270eTcpConnResourceType_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 11),
    _Tn3270eTcpConnResourceType_Type()
)
tn3270eTcpConnResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnResourceType.setStatus("current")
_Tn3270eTcpConnDeviceType_Type = IANATn3270DeviceType
_Tn3270eTcpConnDeviceType_Object = MibTableColumn
tn3270eTcpConnDeviceType = _Tn3270eTcpConnDeviceType_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 12),
    _Tn3270eTcpConnDeviceType_Type()
)
tn3270eTcpConnDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnDeviceType.setStatus("current")
_Tn3270eTcpConnFunctions_Type = IANATn3270Functions
_Tn3270eTcpConnFunctions_Object = MibTableColumn
tn3270eTcpConnFunctions = _Tn3270eTcpConnFunctions_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 13),
    _Tn3270eTcpConnFunctions_Type()
)
tn3270eTcpConnFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnFunctions.setStatus("current")
_Tn3270eTcpConnId_Type = Unsigned32
_Tn3270eTcpConnId_Object = MibTableColumn
tn3270eTcpConnId = _Tn3270eTcpConnId_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 14),
    _Tn3270eTcpConnId_Type()
)
tn3270eTcpConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnId.setStatus("current")
_Tn3270eTcpConnClientIdFormat_Type = IANATn3270eClientType
_Tn3270eTcpConnClientIdFormat_Object = MibTableColumn
tn3270eTcpConnClientIdFormat = _Tn3270eTcpConnClientIdFormat_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 15),
    _Tn3270eTcpConnClientIdFormat_Type()
)
tn3270eTcpConnClientIdFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnClientIdFormat.setStatus("current")


class _Tn3270eTcpConnClientId_Type(OctetString):
    """Custom type tn3270eTcpConnClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Tn3270eTcpConnClientId_Type.__name__ = "OctetString"
_Tn3270eTcpConnClientId_Object = MibTableColumn
tn3270eTcpConnClientId = _Tn3270eTcpConnClientId_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 16),
    _Tn3270eTcpConnClientId_Type()
)
tn3270eTcpConnClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnClientId.setStatus("current")
_Tn3270eTcpConnTraceData_Type = Tn3270eTraceData
_Tn3270eTcpConnTraceData_Object = MibTableColumn
tn3270eTcpConnTraceData = _Tn3270eTcpConnTraceData_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 17),
    _Tn3270eTcpConnTraceData_Type()
)
tn3270eTcpConnTraceData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnTraceData.setStatus("current")
_Tn3270eTcpConnLogInfo_Type = IANATn3270eLogData
_Tn3270eTcpConnLogInfo_Object = MibTableColumn
tn3270eTcpConnLogInfo = _Tn3270eTcpConnLogInfo_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 18),
    _Tn3270eTcpConnLogInfo_Type()
)
tn3270eTcpConnLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnLogInfo.setStatus("current")


class _Tn3270eTcpConnLuLuBindImage_Type(OctetString):
    """Custom type tn3270eTcpConnLuLuBindImage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Tn3270eTcpConnLuLuBindImage_Type.__name__ = "OctetString"
_Tn3270eTcpConnLuLuBindImage_Object = MibTableColumn
tn3270eTcpConnLuLuBindImage = _Tn3270eTcpConnLuLuBindImage_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 19),
    _Tn3270eTcpConnLuLuBindImage_Type()
)
tn3270eTcpConnLuLuBindImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnLuLuBindImage.setStatus("current")


class _Tn3270eTcpConnSnaState_Type(Integer32):
    """Custom type tn3270eTcpConnSnaState based on Integer32"""
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
        *(("luLuSession", 4),
          ("noSluSession", 2),
          ("sscpLuSession", 3),
          ("sscpLuSessionAndLuLuSession", 5),
          ("unknown", 1))
    )


_Tn3270eTcpConnSnaState_Type.__name__ = "Integer32"
_Tn3270eTcpConnSnaState_Object = MibTableColumn
tn3270eTcpConnSnaState = _Tn3270eTcpConnSnaState_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 20),
    _Tn3270eTcpConnSnaState_Type()
)
tn3270eTcpConnSnaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnSnaState.setStatus("current")


class _Tn3270eTcpConnStateLastDiscReason_Type(Integer32):
    """Custom type tn3270eTcpConnStateLastDiscReason based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("clientNotResponding", 10),
          ("clientProtocolError", 5),
          ("deviceInUse", 7),
          ("hostDontAcceptConnection", 3),
          ("hostNotResponding", 9),
          ("hostSendsUnbind", 2),
          ("inactivityTimeout", 8),
          ("invalidDeviceName", 6),
          ("outOfResource", 4),
          ("serverClose", 11),
          ("serverSpecificHexCode", 13),
          ("sysreqLogoff", 12),
          ("unknown", 1))
    )


_Tn3270eTcpConnStateLastDiscReason_Type.__name__ = "Integer32"
_Tn3270eTcpConnStateLastDiscReason_Object = MibTableColumn
tn3270eTcpConnStateLastDiscReason = _Tn3270eTcpConnStateLastDiscReason_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 21),
    _Tn3270eTcpConnStateLastDiscReason_Type()
)
tn3270eTcpConnStateLastDiscReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnStateLastDiscReason.setStatus("current")


class _Tn3270eTcpConnSrvrConfIndex_Type(Unsigned32):
    """Custom type tn3270eTcpConnSrvrConfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Tn3270eTcpConnSrvrConfIndex_Type.__name__ = "Unsigned32"
_Tn3270eTcpConnSrvrConfIndex_Object = MibTableColumn
tn3270eTcpConnSrvrConfIndex = _Tn3270eTcpConnSrvrConfIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 22),
    _Tn3270eTcpConnSrvrConfIndex_Type()
)
tn3270eTcpConnSrvrConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnSrvrConfIndex.setStatus("current")
_Tn3270eTcpConnActivationTime_Type = TimeStamp
_Tn3270eTcpConnActivationTime_Object = MibTableColumn
tn3270eTcpConnActivationTime = _Tn3270eTcpConnActivationTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 23),
    _Tn3270eTcpConnActivationTime_Type()
)
tn3270eTcpConnActivationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eTcpConnActivationTime.setStatus("current")
_Tn3270eConfSpinLock_Type = TestAndIncr
_Tn3270eConfSpinLock_Object = MibScalar
tn3270eConfSpinLock = _Tn3270eConfSpinLock_Object(
    (1, 3, 6, 1, 2, 1, 34, 8, 1, 10),
    _Tn3270eConfSpinLock_Type()
)
tn3270eConfSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270eConfSpinLock.setStatus("current")
_Tn3270eConformance_ObjectIdentity = ObjectIdentity
tn3270eConformance = _Tn3270eConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 8, 3)
)
_Tn3270eGroups_ObjectIdentity = ObjectIdentity
tn3270eGroups = _Tn3270eGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 8, 3, 1)
)
_Tn3270eCompliances_ObjectIdentity = ObjectIdentity
tn3270eCompliances = _Tn3270eCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 8, 3, 2)
)

# Managed Objects groups

tn3270eBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 8, 3, 1, 1)
)
tn3270eBasicGroup.setObjects(
      *(("TN3270E-MIB", "tn3270eSrvrConfInactivityTimeout"),
        ("TN3270E-MIB", "tn3270eSrvrConfConnectivityChk"),
        ("TN3270E-MIB", "tn3270eSrvrConfTmNopInactTime"),
        ("TN3270E-MIB", "tn3270eSrvrConfTmNopInterval"),
        ("TN3270E-MIB", "tn3270eSrvrFunctionsSupported"),
        ("TN3270E-MIB", "tn3270eSrvrConfAdminStatus"),
        ("TN3270E-MIB", "tn3270eSrvrConfOperStatus"),
        ("TN3270E-MIB", "tn3270eSrvrConfSessionTermState"),
        ("TN3270E-MIB", "tn3270eSrvrConfSrvrType"),
        ("TN3270E-MIB", "tn3270eSrvrConfContact"),
        ("TN3270E-MIB", "tn3270eSrvrConfRowStatus"),
        ("TN3270E-MIB", "tn3270eSrvrConfLastActTime"),
        ("TN3270E-MIB", "tn3270eSrvrConfTmTimeout"),
        ("TN3270E-MIB", "tn3270eSrvrPortRowStatus"),
        ("TN3270E-MIB", "tn3270eSrvrStatsUpTime"),
        ("TN3270E-MIB", "tn3270eSrvrStatsMaxTerms"),
        ("TN3270E-MIB", "tn3270eSrvrStatsInUseTerms"),
        ("TN3270E-MIB", "tn3270eSrvrStatsSpareTerms"),
        ("TN3270E-MIB", "tn3270eSrvrStatsMaxPtrs"),
        ("TN3270E-MIB", "tn3270eSrvrStatsInUsePtrs"),
        ("TN3270E-MIB", "tn3270eSrvrStatsSparePtrs"),
        ("TN3270E-MIB", "tn3270eSrvrStatsInConnects"),
        ("TN3270E-MIB", "tn3270eSrvrStatsConnResrceRejs"),
        ("TN3270E-MIB", "tn3270eSrvrStatsDisconnects"),
        ("TN3270E-MIB", "tn3270eSrvrStatsInOctets"),
        ("TN3270E-MIB", "tn3270eSrvrStatsOutOctets"),
        ("TN3270E-MIB", "tn3270eSrvrStatsConnErrorRejs"),
        ("TN3270E-MIB", "tn3270eClientGroupSubnetMask"),
        ("TN3270E-MIB", "tn3270eClientGroupPfxLength"),
        ("TN3270E-MIB", "tn3270eClientGroupRowStatus"),
        ("TN3270E-MIB", "tn3270eSnaMapLocalName"),
        ("TN3270E-MIB", "tn3270eSnaMapPrimaryLuName"),
        ("TN3270E-MIB", "tn3270eConfSpinLock"))
)
if mibBuilder.loadTexts:
    tn3270eBasicGroup.setStatus("current")

tn3270eSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 8, 3, 1, 2)
)
tn3270eSessionGroup.setObjects(
      *(("TN3270E-MIB", "tn3270eResMapAddrType"),
        ("TN3270E-MIB", "tn3270eResMapAddress"),
        ("TN3270E-MIB", "tn3270eResMapPort"),
        ("TN3270E-MIB", "tn3270eResMapElementType"),
        ("TN3270E-MIB", "tn3270eResMapSscpSuppliedName"),
        ("TN3270E-MIB", "tn3270eTcpConnLastActivity"),
        ("TN3270E-MIB", "tn3270eTcpConnBytesIn"),
        ("TN3270E-MIB", "tn3270eTcpConnBytesOut"),
        ("TN3270E-MIB", "tn3270eTcpConnResourceElement"),
        ("TN3270E-MIB", "tn3270eTcpConnResourceType"),
        ("TN3270E-MIB", "tn3270eTcpConnDeviceType"),
        ("TN3270E-MIB", "tn3270eTcpConnFunctions"),
        ("TN3270E-MIB", "tn3270eTcpConnSrvrConfIndex"),
        ("TN3270E-MIB", "tn3270eTcpConnActivationTime"))
)
if mibBuilder.loadTexts:
    tn3270eSessionGroup.setStatus("current")

tn3270eResMapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 8, 3, 1, 3)
)
tn3270eResMapGroup.setObjects(
      *(("TN3270E-MIB", "tn3270eResPoolElementType"),
        ("TN3270E-MIB", "tn3270eResPoolRowStatus"),
        ("TN3270E-MIB", "tn3270eClientResMapRowStatus"),
        ("TN3270E-MIB", "tn3270eTcpConnId"),
        ("TN3270E-MIB", "tn3270eTcpConnClientIdFormat"),
        ("TN3270E-MIB", "tn3270eTcpConnClientId"),
        ("TN3270E-MIB", "tn3270eTcpConnTraceData"),
        ("TN3270E-MIB", "tn3270eTcpConnLogInfo"),
        ("TN3270E-MIB", "tn3270eTcpConnLuLuBindImage"),
        ("TN3270E-MIB", "tn3270eTcpConnSnaState"),
        ("TN3270E-MIB", "tn3270eTcpConnStateLastDiscReason"))
)
if mibBuilder.loadTexts:
    tn3270eResMapGroup.setStatus("current")

tn3270eHiCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 8, 3, 1, 4)
)
tn3270eHiCapacityGroup.setObjects(
      *(("TN3270E-MIB", "tn3270eSrvrStatsHCInOctets"),
        ("TN3270E-MIB", "tn3270eSrvrStatsHCOutOctets"))
)
if mibBuilder.loadTexts:
    tn3270eHiCapacityGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tn3270eCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 34, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tn3270eCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN3270E-MIB",
    **{"SnaResourceName": SnaResourceName,
       "Tn3270eTraceData": Tn3270eTraceData,
       "tn3270eMIB": tn3270eMIB,
       "tn3270eNotifications": tn3270eNotifications,
       "tn3270eObjects": tn3270eObjects,
       "tn3270eSrvrConfTable": tn3270eSrvrConfTable,
       "tn3270eSrvrConfEntry": tn3270eSrvrConfEntry,
       "tn3270eSrvrConfIndex": tn3270eSrvrConfIndex,
       "tn3270eSrvrConfInactivityTimeout": tn3270eSrvrConfInactivityTimeout,
       "tn3270eSrvrConfConnectivityChk": tn3270eSrvrConfConnectivityChk,
       "tn3270eSrvrConfTmNopInactTime": tn3270eSrvrConfTmNopInactTime,
       "tn3270eSrvrConfTmNopInterval": tn3270eSrvrConfTmNopInterval,
       "tn3270eSrvrFunctionsSupported": tn3270eSrvrFunctionsSupported,
       "tn3270eSrvrConfAdminStatus": tn3270eSrvrConfAdminStatus,
       "tn3270eSrvrConfOperStatus": tn3270eSrvrConfOperStatus,
       "tn3270eSrvrConfSessionTermState": tn3270eSrvrConfSessionTermState,
       "tn3270eSrvrConfSrvrType": tn3270eSrvrConfSrvrType,
       "tn3270eSrvrConfContact": tn3270eSrvrConfContact,
       "tn3270eSrvrConfRowStatus": tn3270eSrvrConfRowStatus,
       "tn3270eSrvrConfLastActTime": tn3270eSrvrConfLastActTime,
       "tn3270eSrvrConfTmTimeout": tn3270eSrvrConfTmTimeout,
       "tn3270eSrvrPortTable": tn3270eSrvrPortTable,
       "tn3270eSrvrPortEntry": tn3270eSrvrPortEntry,
       "tn3270eSrvrPort": tn3270eSrvrPort,
       "tn3270eSrvrPortAddrType": tn3270eSrvrPortAddrType,
       "tn3270eSrvrPortAddress": tn3270eSrvrPortAddress,
       "tn3270eSrvrPortRowStatus": tn3270eSrvrPortRowStatus,
       "tn3270eSrvrStatsTable": tn3270eSrvrStatsTable,
       "tn3270eSrvrStatsEntry": tn3270eSrvrStatsEntry,
       "tn3270eSrvrStatsUpTime": tn3270eSrvrStatsUpTime,
       "tn3270eSrvrStatsMaxTerms": tn3270eSrvrStatsMaxTerms,
       "tn3270eSrvrStatsInUseTerms": tn3270eSrvrStatsInUseTerms,
       "tn3270eSrvrStatsSpareTerms": tn3270eSrvrStatsSpareTerms,
       "tn3270eSrvrStatsMaxPtrs": tn3270eSrvrStatsMaxPtrs,
       "tn3270eSrvrStatsInUsePtrs": tn3270eSrvrStatsInUsePtrs,
       "tn3270eSrvrStatsSparePtrs": tn3270eSrvrStatsSparePtrs,
       "tn3270eSrvrStatsInConnects": tn3270eSrvrStatsInConnects,
       "tn3270eSrvrStatsConnResrceRejs": tn3270eSrvrStatsConnResrceRejs,
       "tn3270eSrvrStatsDisconnects": tn3270eSrvrStatsDisconnects,
       "tn3270eSrvrStatsHCInOctets": tn3270eSrvrStatsHCInOctets,
       "tn3270eSrvrStatsInOctets": tn3270eSrvrStatsInOctets,
       "tn3270eSrvrStatsHCOutOctets": tn3270eSrvrStatsHCOutOctets,
       "tn3270eSrvrStatsOutOctets": tn3270eSrvrStatsOutOctets,
       "tn3270eSrvrStatsConnErrorRejs": tn3270eSrvrStatsConnErrorRejs,
       "tn3270eClientGroupTable": tn3270eClientGroupTable,
       "tn3270eClientGroupEntry": tn3270eClientGroupEntry,
       "tn3270eClientGroupName": tn3270eClientGroupName,
       "tn3270eClientGroupAddrType": tn3270eClientGroupAddrType,
       "tn3270eClientGroupAddress": tn3270eClientGroupAddress,
       "tn3270eClientGroupSubnetMask": tn3270eClientGroupSubnetMask,
       "tn3270eClientGroupPfxLength": tn3270eClientGroupPfxLength,
       "tn3270eClientGroupRowStatus": tn3270eClientGroupRowStatus,
       "tn3270eResPoolTable": tn3270eResPoolTable,
       "tn3270eResPoolEntry": tn3270eResPoolEntry,
       "tn3270eResPoolName": tn3270eResPoolName,
       "tn3270eResPoolElementName": tn3270eResPoolElementName,
       "tn3270eResPoolElementType": tn3270eResPoolElementType,
       "tn3270eResPoolRowStatus": tn3270eResPoolRowStatus,
       "tn3270eSnaMapTable": tn3270eSnaMapTable,
       "tn3270eSnaMapEntry": tn3270eSnaMapEntry,
       "tn3270eSnaMapSscpSuppliedName": tn3270eSnaMapSscpSuppliedName,
       "tn3270eSnaMapLocalName": tn3270eSnaMapLocalName,
       "tn3270eSnaMapPrimaryLuName": tn3270eSnaMapPrimaryLuName,
       "tn3270eClientResMapTable": tn3270eClientResMapTable,
       "tn3270eClientResMapEntry": tn3270eClientResMapEntry,
       "tn3270eClientResMapPoolName": tn3270eClientResMapPoolName,
       "tn3270eClientResMapClientGroupName": tn3270eClientResMapClientGroupName,
       "tn3270eClientResMapClientPort": tn3270eClientResMapClientPort,
       "tn3270eClientResMapRowStatus": tn3270eClientResMapRowStatus,
       "tn3270eResMapTable": tn3270eResMapTable,
       "tn3270eResMapEntry": tn3270eResMapEntry,
       "tn3270eResMapElementName": tn3270eResMapElementName,
       "tn3270eResMapAddrType": tn3270eResMapAddrType,
       "tn3270eResMapAddress": tn3270eResMapAddress,
       "tn3270eResMapPort": tn3270eResMapPort,
       "tn3270eResMapElementType": tn3270eResMapElementType,
       "tn3270eResMapSscpSuppliedName": tn3270eResMapSscpSuppliedName,
       "tn3270eTcpConnTable": tn3270eTcpConnTable,
       "tn3270eTcpConnEntry": tn3270eTcpConnEntry,
       "tn3270eTcpConnRemAddrType": tn3270eTcpConnRemAddrType,
       "tn3270eTcpConnRemAddress": tn3270eTcpConnRemAddress,
       "tn3270eTcpConnRemPort": tn3270eTcpConnRemPort,
       "tn3270eTcpConnLocalAddrType": tn3270eTcpConnLocalAddrType,
       "tn3270eTcpConnLocalAddress": tn3270eTcpConnLocalAddress,
       "tn3270eTcpConnLocalPort": tn3270eTcpConnLocalPort,
       "tn3270eTcpConnLastActivity": tn3270eTcpConnLastActivity,
       "tn3270eTcpConnBytesIn": tn3270eTcpConnBytesIn,
       "tn3270eTcpConnBytesOut": tn3270eTcpConnBytesOut,
       "tn3270eTcpConnResourceElement": tn3270eTcpConnResourceElement,
       "tn3270eTcpConnResourceType": tn3270eTcpConnResourceType,
       "tn3270eTcpConnDeviceType": tn3270eTcpConnDeviceType,
       "tn3270eTcpConnFunctions": tn3270eTcpConnFunctions,
       "tn3270eTcpConnId": tn3270eTcpConnId,
       "tn3270eTcpConnClientIdFormat": tn3270eTcpConnClientIdFormat,
       "tn3270eTcpConnClientId": tn3270eTcpConnClientId,
       "tn3270eTcpConnTraceData": tn3270eTcpConnTraceData,
       "tn3270eTcpConnLogInfo": tn3270eTcpConnLogInfo,
       "tn3270eTcpConnLuLuBindImage": tn3270eTcpConnLuLuBindImage,
       "tn3270eTcpConnSnaState": tn3270eTcpConnSnaState,
       "tn3270eTcpConnStateLastDiscReason": tn3270eTcpConnStateLastDiscReason,
       "tn3270eTcpConnSrvrConfIndex": tn3270eTcpConnSrvrConfIndex,
       "tn3270eTcpConnActivationTime": tn3270eTcpConnActivationTime,
       "tn3270eConfSpinLock": tn3270eConfSpinLock,
       "tn3270eConformance": tn3270eConformance,
       "tn3270eGroups": tn3270eGroups,
       "tn3270eBasicGroup": tn3270eBasicGroup,
       "tn3270eSessionGroup": tn3270eSessionGroup,
       "tn3270eResMapGroup": tn3270eResMapGroup,
       "tn3270eHiCapacityGroup": tn3270eHiCapacityGroup,
       "tn3270eCompliances": tn3270eCompliances,
       "tn3270eCompliance": tn3270eCompliance}
)
