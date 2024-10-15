# SNMP MIB module (IP-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IP-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:38 2024
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

(cjnProtocol,) = mibBuilder.importSymbols(
    "Cajun-ROOT",
    "cjnProtocol")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cjnIpv4Serv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnIpIRDPGblGroup_ObjectIdentity = ObjectIdentity
cjnIpIRDPGblGroup = _CjnIpIRDPGblGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1)
)
_CjnIpIRDPIfTable_Object = MibTable
cjnIpIRDPIfTable = _CjnIpIRDPIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    cjnIpIRDPIfTable.setStatus("current")
_CjnIpIRDPIfEntry_Object = MibTableRow
cjnIpIRDPIfEntry = _CjnIpIRDPIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1)
)
cjnIpIRDPIfEntry.setIndexNames(
    (0, "IP-SERVICES-MIB", "cjnIpIRDPIfIndex"),
)
if mibBuilder.loadTexts:
    cjnIpIRDPIfEntry.setStatus("current")
_CjnIpIRDPIfIndex_Type = Integer32
_CjnIpIRDPIfIndex_Object = MibTableColumn
cjnIpIRDPIfIndex = _CjnIpIRDPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 1),
    _CjnIpIRDPIfIndex_Type()
)
cjnIpIRDPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpIRDPIfIndex.setStatus("current")


class _CjnIpIfIRDPEnabled_Type(Integer32):
    """Custom type cjnIpIfIRDPEnabled based on Integer32"""
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


_CjnIpIfIRDPEnabled_Type.__name__ = "Integer32"
_CjnIpIfIRDPEnabled_Object = MibTableColumn
cjnIpIfIRDPEnabled = _CjnIpIfIRDPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 2),
    _CjnIpIfIRDPEnabled_Type()
)
cjnIpIfIRDPEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfIRDPEnabled.setStatus("current")


class _CjnIpIfIRDPTxType_Type(Integer32):
    """Custom type cjnIpIfIRDPTxType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("multicast", 1))
    )


_CjnIpIfIRDPTxType_Type.__name__ = "Integer32"
_CjnIpIfIRDPTxType_Object = MibTableColumn
cjnIpIfIRDPTxType = _CjnIpIfIRDPTxType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 3),
    _CjnIpIfIRDPTxType_Type()
)
cjnIpIfIRDPTxType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfIRDPTxType.setStatus("current")


class _CjnIpIfIRDPPref_Type(Integer32):
    """Custom type cjnIpIfIRDPPref based on Integer32"""
    defaultValue = 0


_CjnIpIfIRDPPref_Object = MibTableColumn
cjnIpIfIRDPPref = _CjnIpIfIRDPPref_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 4),
    _CjnIpIfIRDPPref_Type()
)
cjnIpIfIRDPPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfIRDPPref.setStatus("current")


class _CjnIpIRDPTimerMax_Type(Integer32):
    """Custom type cjnIpIRDPTimerMax based on Integer32"""
    defaultValue = 600


_CjnIpIRDPTimerMax_Object = MibTableColumn
cjnIpIRDPTimerMax = _CjnIpIRDPTimerMax_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 5),
    _CjnIpIRDPTimerMax_Type()
)
cjnIpIRDPTimerMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIRDPTimerMax.setStatus("current")


class _CjnIpIRDPTimerMin_Type(Integer32):
    """Custom type cjnIpIRDPTimerMin based on Integer32"""
    defaultValue = 450


_CjnIpIRDPTimerMin_Object = MibTableColumn
cjnIpIRDPTimerMin = _CjnIpIRDPTimerMin_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 6),
    _CjnIpIRDPTimerMin_Type()
)
cjnIpIRDPTimerMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIRDPTimerMin.setStatus("current")


class _CjnIpIRDPLifetime_Type(Integer32):
    """Custom type cjnIpIRDPLifetime based on Integer32"""
    defaultValue = 900


_CjnIpIRDPLifetime_Object = MibTableColumn
cjnIpIRDPLifetime = _CjnIpIRDPLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 7),
    _CjnIpIRDPLifetime_Type()
)
cjnIpIRDPLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIRDPLifetime.setStatus("current")
_CjnIpBootpRelayGroup_ObjectIdentity = ObjectIdentity
cjnIpBootpRelayGroup = _CjnIpBootpRelayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 2)
)


class _CjnBootpRelayEnabled_Type(Integer32):
    """Custom type cjnBootpRelayEnabled based on Integer32"""
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


_CjnBootpRelayEnabled_Type.__name__ = "Integer32"
_CjnBootpRelayEnabled_Object = MibScalar
cjnBootpRelayEnabled = _CjnBootpRelayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 2, 1),
    _CjnBootpRelayEnabled_Type()
)
cjnBootpRelayEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnBootpRelayEnabled.setStatus("current")
_CjnBootpRelayTable_Object = MibTable
cjnBootpRelayTable = _CjnBootpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    cjnBootpRelayTable.setStatus("current")
_CjnBootpRelayEntry_Object = MibTableRow
cjnBootpRelayEntry = _CjnBootpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 2, 2, 1)
)
cjnBootpRelayEntry.setIndexNames(
    (0, "IP-SERVICES-MIB", "cjnBootpRelayServAddr"),
)
if mibBuilder.loadTexts:
    cjnBootpRelayEntry.setStatus("current")
_CjnBootpRelayServAddr_Type = IpAddress
_CjnBootpRelayServAddr_Object = MibTableColumn
cjnBootpRelayServAddr = _CjnBootpRelayServAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 2, 2, 1, 1),
    _CjnBootpRelayServAddr_Type()
)
cjnBootpRelayServAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnBootpRelayServAddr.setStatus("current")
_CjnBootpRelayRowStatus_Type = RowStatus
_CjnBootpRelayRowStatus_Object = MibTableColumn
cjnBootpRelayRowStatus = _CjnBootpRelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 2, 2, 1, 2),
    _CjnBootpRelayRowStatus_Type()
)
cjnBootpRelayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnBootpRelayRowStatus.setStatus("current")
_CjnIpBootpServStats_ObjectIdentity = ObjectIdentity
cjnIpBootpServStats = _CjnIpBootpServStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3)
)
_CjnBtprInReqs_Type = Integer32
_CjnBtprInReqs_Object = MibScalar
cjnBtprInReqs = _CjnBtprInReqs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3, 1),
    _CjnBtprInReqs_Type()
)
cjnBtprInReqs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnBtprInReqs.setStatus("current")
_CjnBtprInRsps_Type = Integer32
_CjnBtprInRsps_Object = MibScalar
cjnBtprInRsps = _CjnBtprInRsps_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3, 2),
    _CjnBtprInRsps_Type()
)
cjnBtprInRsps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnBtprInRsps.setStatus("current")
_CjnBtprInDiscards_Type = Integer32
_CjnBtprInDiscards_Object = MibScalar
cjnBtprInDiscards = _CjnBtprInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3, 3),
    _CjnBtprInDiscards_Type()
)
cjnBtprInDiscards.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnBtprInDiscards.setStatus("current")
_CjnBtprInHopsExceededs_Type = Integer32
_CjnBtprInHopsExceededs_Object = MibScalar
cjnBtprInHopsExceededs = _CjnBtprInHopsExceededs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3, 4),
    _CjnBtprInHopsExceededs_Type()
)
cjnBtprInHopsExceededs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnBtprInHopsExceededs.setStatus("current")
_CjnBtprOutReqs_Type = Integer32
_CjnBtprOutReqs_Object = MibScalar
cjnBtprOutReqs = _CjnBtprOutReqs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3, 5),
    _CjnBtprOutReqs_Type()
)
cjnBtprOutReqs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnBtprOutReqs.setStatus("current")
_CjnBtprOutRsps_Type = Integer32
_CjnBtprOutRsps_Object = MibScalar
cjnBtprOutRsps = _CjnBtprOutRsps_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3, 6),
    _CjnBtprOutRsps_Type()
)
cjnBtprOutRsps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnBtprOutRsps.setStatus("current")
_CjnIpHelperAddressGroup_ObjectIdentity = ObjectIdentity
cjnIpHelperAddressGroup = _CjnIpHelperAddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4)
)
_CjnIpHelperAddressTable_Object = MibTable
cjnIpHelperAddressTable = _CjnIpHelperAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    cjnIpHelperAddressTable.setStatus("current")
_CjnIpHelperAddressEntry_Object = MibTableRow
cjnIpHelperAddressEntry = _CjnIpHelperAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1)
)
cjnIpHelperAddressEntry.setIndexNames(
    (0, "IP-SERVICES-MIB", "cjnIpHelperAddressIfIndex"),
    (0, "IP-SERVICES-MIB", "cjnIpHelperAddressAddr"),
)
if mibBuilder.loadTexts:
    cjnIpHelperAddressEntry.setStatus("current")
_CjnIpHelperAddressIfIndex_Type = Integer32
_CjnIpHelperAddressIfIndex_Object = MibTableColumn
cjnIpHelperAddressIfIndex = _CjnIpHelperAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 1),
    _CjnIpHelperAddressIfIndex_Type()
)
cjnIpHelperAddressIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpHelperAddressIfIndex.setStatus("current")
_CjnIpHelperAddressAddr_Type = IpAddress
_CjnIpHelperAddressAddr_Object = MibTableColumn
cjnIpHelperAddressAddr = _CjnIpHelperAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 2),
    _CjnIpHelperAddressAddr_Type()
)
cjnIpHelperAddressAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpHelperAddressAddr.setStatus("current")


class _CjnIpHelperAddressTFTP_Type(Integer32):
    """Custom type cjnIpHelperAddressTFTP based on Integer32"""
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


_CjnIpHelperAddressTFTP_Type.__name__ = "Integer32"
_CjnIpHelperAddressTFTP_Object = MibTableColumn
cjnIpHelperAddressTFTP = _CjnIpHelperAddressTFTP_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 4),
    _CjnIpHelperAddressTFTP_Type()
)
cjnIpHelperAddressTFTP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpHelperAddressTFTP.setStatus("current")


class _CjnIpHelperAddressDNS_Type(Integer32):
    """Custom type cjnIpHelperAddressDNS based on Integer32"""
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


_CjnIpHelperAddressDNS_Type.__name__ = "Integer32"
_CjnIpHelperAddressDNS_Object = MibTableColumn
cjnIpHelperAddressDNS = _CjnIpHelperAddressDNS_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 5),
    _CjnIpHelperAddressDNS_Type()
)
cjnIpHelperAddressDNS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpHelperAddressDNS.setStatus("current")


class _CjnIpHelperAddressTime_Type(Integer32):
    """Custom type cjnIpHelperAddressTime based on Integer32"""
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


_CjnIpHelperAddressTime_Type.__name__ = "Integer32"
_CjnIpHelperAddressTime_Object = MibTableColumn
cjnIpHelperAddressTime = _CjnIpHelperAddressTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 6),
    _CjnIpHelperAddressTime_Type()
)
cjnIpHelperAddressTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpHelperAddressTime.setStatus("current")


class _CjnIpHelperAddressNetBiosName_Type(Integer32):
    """Custom type cjnIpHelperAddressNetBiosName based on Integer32"""
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


_CjnIpHelperAddressNetBiosName_Type.__name__ = "Integer32"
_CjnIpHelperAddressNetBiosName_Object = MibTableColumn
cjnIpHelperAddressNetBiosName = _CjnIpHelperAddressNetBiosName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 7),
    _CjnIpHelperAddressNetBiosName_Type()
)
cjnIpHelperAddressNetBiosName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpHelperAddressNetBiosName.setStatus("current")


class _CjnIpHelperAddressNetBiosData_Type(Integer32):
    """Custom type cjnIpHelperAddressNetBiosData based on Integer32"""
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


_CjnIpHelperAddressNetBiosData_Type.__name__ = "Integer32"
_CjnIpHelperAddressNetBiosData_Object = MibTableColumn
cjnIpHelperAddressNetBiosData = _CjnIpHelperAddressNetBiosData_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 8),
    _CjnIpHelperAddressNetBiosData_Type()
)
cjnIpHelperAddressNetBiosData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpHelperAddressNetBiosData.setStatus("current")


class _CjnIpHelperAddressBootpServ_Type(Integer32):
    """Custom type cjnIpHelperAddressBootpServ based on Integer32"""
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


_CjnIpHelperAddressBootpServ_Type.__name__ = "Integer32"
_CjnIpHelperAddressBootpServ_Object = MibTableColumn
cjnIpHelperAddressBootpServ = _CjnIpHelperAddressBootpServ_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 9),
    _CjnIpHelperAddressBootpServ_Type()
)
cjnIpHelperAddressBootpServ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpHelperAddressBootpServ.setStatus("current")


class _CjnIpHelperAddressBootpClient_Type(Integer32):
    """Custom type cjnIpHelperAddressBootpClient based on Integer32"""
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


_CjnIpHelperAddressBootpClient_Type.__name__ = "Integer32"
_CjnIpHelperAddressBootpClient_Object = MibTableColumn
cjnIpHelperAddressBootpClient = _CjnIpHelperAddressBootpClient_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 10),
    _CjnIpHelperAddressBootpClient_Type()
)
cjnIpHelperAddressBootpClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpHelperAddressBootpClient.setStatus("current")


class _CjnIpHelperAddressTacacs_Type(Integer32):
    """Custom type cjnIpHelperAddressTacacs based on Integer32"""
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


_CjnIpHelperAddressTacacs_Type.__name__ = "Integer32"
_CjnIpHelperAddressTacacs_Object = MibTableColumn
cjnIpHelperAddressTacacs = _CjnIpHelperAddressTacacs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 11),
    _CjnIpHelperAddressTacacs_Type()
)
cjnIpHelperAddressTacacs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpHelperAddressTacacs.setStatus("current")
_CjnIpDHCPOption82Group_ObjectIdentity = ObjectIdentity
cjnIpDHCPOption82Group = _CjnIpDHCPOption82Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 5)
)


class _CjnDHCPOpt82Sub1Enabled_Type(Integer32):
    """Custom type cjnDHCPOpt82Sub1Enabled based on Integer32"""
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


_CjnDHCPOpt82Sub1Enabled_Type.__name__ = "Integer32"
_CjnDHCPOpt82Sub1Enabled_Object = MibScalar
cjnDHCPOpt82Sub1Enabled = _CjnDHCPOpt82Sub1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 5, 1),
    _CjnDHCPOpt82Sub1Enabled_Type()
)
cjnDHCPOpt82Sub1Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDHCPOpt82Sub1Enabled.setStatus("current")


class _CjnDHCPOpt82Sub2Enabled_Type(Integer32):
    """Custom type cjnDHCPOpt82Sub2Enabled based on Integer32"""
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


_CjnDHCPOpt82Sub2Enabled_Type.__name__ = "Integer32"
_CjnDHCPOpt82Sub2Enabled_Object = MibScalar
cjnDHCPOpt82Sub2Enabled = _CjnDHCPOpt82Sub2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 5, 2),
    _CjnDHCPOpt82Sub2Enabled_Type()
)
cjnDHCPOpt82Sub2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnDHCPOpt82Sub2Enabled.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IP-SERVICES-MIB",
    **{"cjnIpv4Serv": cjnIpv4Serv,
       "cjnIpIRDPGblGroup": cjnIpIRDPGblGroup,
       "cjnIpIRDPIfTable": cjnIpIRDPIfTable,
       "cjnIpIRDPIfEntry": cjnIpIRDPIfEntry,
       "cjnIpIRDPIfIndex": cjnIpIRDPIfIndex,
       "cjnIpIfIRDPEnabled": cjnIpIfIRDPEnabled,
       "cjnIpIfIRDPTxType": cjnIpIfIRDPTxType,
       "cjnIpIfIRDPPref": cjnIpIfIRDPPref,
       "cjnIpIRDPTimerMax": cjnIpIRDPTimerMax,
       "cjnIpIRDPTimerMin": cjnIpIRDPTimerMin,
       "cjnIpIRDPLifetime": cjnIpIRDPLifetime,
       "cjnIpBootpRelayGroup": cjnIpBootpRelayGroup,
       "cjnBootpRelayEnabled": cjnBootpRelayEnabled,
       "cjnBootpRelayTable": cjnBootpRelayTable,
       "cjnBootpRelayEntry": cjnBootpRelayEntry,
       "cjnBootpRelayServAddr": cjnBootpRelayServAddr,
       "cjnBootpRelayRowStatus": cjnBootpRelayRowStatus,
       "cjnIpBootpServStats": cjnIpBootpServStats,
       "cjnBtprInReqs": cjnBtprInReqs,
       "cjnBtprInRsps": cjnBtprInRsps,
       "cjnBtprInDiscards": cjnBtprInDiscards,
       "cjnBtprInHopsExceededs": cjnBtprInHopsExceededs,
       "cjnBtprOutReqs": cjnBtprOutReqs,
       "cjnBtprOutRsps": cjnBtprOutRsps,
       "cjnIpHelperAddressGroup": cjnIpHelperAddressGroup,
       "cjnIpHelperAddressTable": cjnIpHelperAddressTable,
       "cjnIpHelperAddressEntry": cjnIpHelperAddressEntry,
       "cjnIpHelperAddressIfIndex": cjnIpHelperAddressIfIndex,
       "cjnIpHelperAddressAddr": cjnIpHelperAddressAddr,
       "cjnIpHelperAddressTFTP": cjnIpHelperAddressTFTP,
       "cjnIpHelperAddressDNS": cjnIpHelperAddressDNS,
       "cjnIpHelperAddressTime": cjnIpHelperAddressTime,
       "cjnIpHelperAddressNetBiosName": cjnIpHelperAddressNetBiosName,
       "cjnIpHelperAddressNetBiosData": cjnIpHelperAddressNetBiosData,
       "cjnIpHelperAddressBootpServ": cjnIpHelperAddressBootpServ,
       "cjnIpHelperAddressBootpClient": cjnIpHelperAddressBootpClient,
       "cjnIpHelperAddressTacacs": cjnIpHelperAddressTacacs,
       "cjnIpDHCPOption82Group": cjnIpDHCPOption82Group,
       "cjnDHCPOpt82Sub1Enabled": cjnDHCPOpt82Sub1Enabled,
       "cjnDHCPOpt82Sub2Enabled": cjnDHCPOpt82Sub2Enabled}
)
