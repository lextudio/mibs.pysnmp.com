# SNMP MIB module (CL-PKTC-EUE-DEV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CL-PKTC-EUE-DEV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:29 2024
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

(PktcEUETCCreds,
 PktcEUETCCredsType) = mibBuilder.importSymbols(
    "CL-PKTC-EUE-TC-MIB",
    "PktcEUETCCreds",
    "PktcEUETCCredsType")

(pktcEUEMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcEUEMibs")

(InetAddress,
 InetAddressDNS,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressDNS",
    "InetAddressType",
    "InetPortNumber")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcEUEDevMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PktcEUEDevNotification_ObjectIdentity = ObjectIdentity
pktcEUEDevNotification = _PktcEUEDevNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 0)
)
_PktcEUEDevObjects_ObjectIdentity = ObjectIdentity
pktcEUEDevObjects = _PktcEUEDevObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1)
)
_PktcEUEDevProfile_ObjectIdentity = ObjectIdentity
pktcEUEDevProfile = _PktcEUEDevProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1)
)


class _PktcEUEDevProfileVersion_Type(SnmpAdminString):
    """Custom type pktcEUEDevProfileVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_PktcEUEDevProfileVersion_Type.__name__ = "SnmpAdminString"
_PktcEUEDevProfileVersion_Object = MibScalar
pktcEUEDevProfileVersion = _PktcEUEDevProfileVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 1),
    _PktcEUEDevProfileVersion_Type()
)
pktcEUEDevProfileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDevProfileVersion.setStatus("current")
_PktcEUEDevOpTable_Object = MibTable
pktcEUEDevOpTable = _PktcEUEDevOpTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pktcEUEDevOpTable.setStatus("current")
_PktcEUEDevOpEntry_Object = MibTableRow
pktcEUEDevOpEntry = _PktcEUEDevOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1)
)
pktcEUEDevOpEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEDevOpEntry.setStatus("current")


class _PktcEUEDevOpIndex_Type(Unsigned32):
    """Custom type pktcEUEDevOpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PktcEUEDevOpIndex_Type.__name__ = "Unsigned32"
_PktcEUEDevOpIndex_Object = MibTableColumn
pktcEUEDevOpIndex = _PktcEUEDevOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 1),
    _PktcEUEDevOpIndex_Type()
)
pktcEUEDevOpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEDevOpIndex.setStatus("current")
_PktcEUEDevOpDomain_Type = InetAddressDNS
_PktcEUEDevOpDomain_Object = MibTableColumn
pktcEUEDevOpDomain = _PktcEUEDevOpDomain_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 2),
    _PktcEUEDevOpDomain_Type()
)
pktcEUEDevOpDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpDomain.setStatus("current")


class _PktcEUEDevOpSTUNAddrType_Type(InetAddressType):
    """Custom type pktcEUEDevOpSTUNAddrType based on InetAddressType"""


_PktcEUEDevOpSTUNAddrType_Object = MibTableColumn
pktcEUEDevOpSTUNAddrType = _PktcEUEDevOpSTUNAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 3),
    _PktcEUEDevOpSTUNAddrType_Type()
)
pktcEUEDevOpSTUNAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpSTUNAddrType.setStatus("current")
_PktcEUEDevOpSTUNAddr_Type = InetAddress
_PktcEUEDevOpSTUNAddr_Object = MibTableColumn
pktcEUEDevOpSTUNAddr = _PktcEUEDevOpSTUNAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 4),
    _PktcEUEDevOpSTUNAddr_Type()
)
pktcEUEDevOpSTUNAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpSTUNAddr.setStatus("current")


class _PktcEUEDevOpSTUNAddrPort_Type(InetPortNumber):
    """Custom type pktcEUEDevOpSTUNAddrPort based on InetPortNumber"""
    defaultValue = 0


_PktcEUEDevOpSTUNAddrPort_Object = MibTableColumn
pktcEUEDevOpSTUNAddrPort = _PktcEUEDevOpSTUNAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 5),
    _PktcEUEDevOpSTUNAddrPort_Type()
)
pktcEUEDevOpSTUNAddrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpSTUNAddrPort.setStatus("current")


class _PktcEUEDevOpSTUNRelayAddrType_Type(InetAddressType):
    """Custom type pktcEUEDevOpSTUNRelayAddrType based on InetAddressType"""


_PktcEUEDevOpSTUNRelayAddrType_Object = MibTableColumn
pktcEUEDevOpSTUNRelayAddrType = _PktcEUEDevOpSTUNRelayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 6),
    _PktcEUEDevOpSTUNRelayAddrType_Type()
)
pktcEUEDevOpSTUNRelayAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpSTUNRelayAddrType.setStatus("current")
_PktcEUEDevOpSTUNRelayAddr_Type = InetAddress
_PktcEUEDevOpSTUNRelayAddr_Object = MibTableColumn
pktcEUEDevOpSTUNRelayAddr = _PktcEUEDevOpSTUNRelayAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 7),
    _PktcEUEDevOpSTUNRelayAddr_Type()
)
pktcEUEDevOpSTUNRelayAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpSTUNRelayAddr.setStatus("current")


class _PktcEUEDevOpSTUNRelayAddrPort_Type(InetPortNumber):
    """Custom type pktcEUEDevOpSTUNRelayAddrPort based on InetPortNumber"""
    defaultValue = 0


_PktcEUEDevOpSTUNRelayAddrPort_Object = MibTableColumn
pktcEUEDevOpSTUNRelayAddrPort = _PktcEUEDevOpSTUNRelayAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 8),
    _PktcEUEDevOpSTUNRelayAddrPort_Type()
)
pktcEUEDevOpSTUNRelayAddrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpSTUNRelayAddrPort.setStatus("current")


class _PktcEUEDevOpSTUNRelayCredsType_Type(PktcEUETCCredsType):
    """Custom type pktcEUEDevOpSTUNRelayCredsType based on PktcEUETCCredsType"""


_PktcEUEDevOpSTUNRelayCredsType_Object = MibTableColumn
pktcEUEDevOpSTUNRelayCredsType = _PktcEUEDevOpSTUNRelayCredsType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 9),
    _PktcEUEDevOpSTUNRelayCredsType_Type()
)
pktcEUEDevOpSTUNRelayCredsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpSTUNRelayCredsType.setStatus("current")
_PktcEUEDevOpSTUNRelayCreds_Type = PktcEUETCCreds
_PktcEUEDevOpSTUNRelayCreds_Object = MibTableColumn
pktcEUEDevOpSTUNRelayCreds = _PktcEUEDevOpSTUNRelayCreds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 10),
    _PktcEUEDevOpSTUNRelayCreds_Type()
)
pktcEUEDevOpSTUNRelayCreds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpSTUNRelayCreds.setStatus("current")


class _PktcEUEDevOpTimerT1_Type(Unsigned32):
    """Custom type pktcEUEDevOpTimerT1 based on Unsigned32"""
    defaultValue = 2000


_PktcEUEDevOpTimerT1_Object = MibTableColumn
pktcEUEDevOpTimerT1 = _PktcEUEDevOpTimerT1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 11),
    _PktcEUEDevOpTimerT1_Type()
)
pktcEUEDevOpTimerT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDevOpTimerT1.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUEDevOpTimerT1.setUnits("milliseconds")


class _PktcEUEDevOpTimerT2_Type(Unsigned32):
    """Custom type pktcEUEDevOpTimerT2 based on Unsigned32"""
    defaultValue = 1600


_PktcEUEDevOpTimerT2_Object = MibTableColumn
pktcEUEDevOpTimerT2 = _PktcEUEDevOpTimerT2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 12),
    _PktcEUEDevOpTimerT2_Type()
)
pktcEUEDevOpTimerT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDevOpTimerT2.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUEDevOpTimerT2.setUnits("milliseconds")


class _PktcEUEDevOpTimerT4_Type(Unsigned32):
    """Custom type pktcEUEDevOpTimerT4 based on Unsigned32"""
    defaultValue = 1700


_PktcEUEDevOpTimerT4_Object = MibTableColumn
pktcEUEDevOpTimerT4 = _PktcEUEDevOpTimerT4_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 13),
    _PktcEUEDevOpTimerT4_Type()
)
pktcEUEDevOpTimerT4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDevOpTimerT4.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUEDevOpTimerT4.setUnits("milliseconds")
_PktcEUEDevOpRowStatus_Type = RowStatus
_PktcEUEDevOpRowStatus_Object = MibTableColumn
pktcEUEDevOpRowStatus = _PktcEUEDevOpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 2, 1, 14),
    _PktcEUEDevOpRowStatus_Type()
)
pktcEUEDevOpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpRowStatus.setStatus("current")
_PktcEUEDevDnsTable_Object = MibTable
pktcEUEDevDnsTable = _PktcEUEDevDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pktcEUEDevDnsTable.setStatus("current")
_PktcEUEDevDnsEntry_Object = MibTableRow
pktcEUEDevDnsEntry = _PktcEUEDevDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 3, 1)
)
pktcEUEDevDnsEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEDevDnsEntry.setStatus("current")


class _PktcEUEDevDnsIndex_Type(Unsigned32):
    """Custom type pktcEUEDevDnsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PktcEUEDevDnsIndex_Type.__name__ = "Unsigned32"
_PktcEUEDevDnsIndex_Object = MibTableColumn
pktcEUEDevDnsIndex = _PktcEUEDevDnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 3, 1, 1),
    _PktcEUEDevDnsIndex_Type()
)
pktcEUEDevDnsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEDevDnsIndex.setStatus("current")


class _PktcEUEDevDnsAddrType_Type(InetAddressType):
    """Custom type pktcEUEDevDnsAddrType based on InetAddressType"""


_PktcEUEDevDnsAddrType_Object = MibTableColumn
pktcEUEDevDnsAddrType = _PktcEUEDevDnsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 3, 1, 2),
    _PktcEUEDevDnsAddrType_Type()
)
pktcEUEDevDnsAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevDnsAddrType.setStatus("current")
_PktcEUEDevDnsAddr_Type = InetAddress
_PktcEUEDevDnsAddr_Object = MibTableColumn
pktcEUEDevDnsAddr = _PktcEUEDevDnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 3, 1, 3),
    _PktcEUEDevDnsAddr_Type()
)
pktcEUEDevDnsAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevDnsAddr.setStatus("current")
_PktcEUEDevDnsRowStatus_Type = RowStatus
_PktcEUEDevDnsRowStatus_Object = MibTableColumn
pktcEUEDevDnsRowStatus = _PktcEUEDevDnsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 3, 1, 4),
    _PktcEUEDevDnsRowStatus_Type()
)
pktcEUEDevDnsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevDnsRowStatus.setStatus("current")
_PktcEUEDevPCSCFTable_Object = MibTable
pktcEUEDevPCSCFTable = _PktcEUEDevPCSCFTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFTable.setStatus("current")
_PktcEUEDevPCSCFEntry_Object = MibTableRow
pktcEUEDevPCSCFEntry = _PktcEUEDevPCSCFEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 4, 1)
)
pktcEUEDevPCSCFEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFEntry.setStatus("current")


class _PktcEUEDevPCSCFIndex_Type(Unsigned32):
    """Custom type pktcEUEDevPCSCFIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PktcEUEDevPCSCFIndex_Type.__name__ = "Unsigned32"
_PktcEUEDevPCSCFIndex_Object = MibTableColumn
pktcEUEDevPCSCFIndex = _PktcEUEDevPCSCFIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 4, 1, 1),
    _PktcEUEDevPCSCFIndex_Type()
)
pktcEUEDevPCSCFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFIndex.setStatus("current")


class _PktcEUEDevPCSCFAddrType_Type(InetAddressType):
    """Custom type pktcEUEDevPCSCFAddrType based on InetAddressType"""


_PktcEUEDevPCSCFAddrType_Object = MibTableColumn
pktcEUEDevPCSCFAddrType = _PktcEUEDevPCSCFAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 4, 1, 2),
    _PktcEUEDevPCSCFAddrType_Type()
)
pktcEUEDevPCSCFAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFAddrType.setStatus("current")
_PktcEUEDevPCSCFAddr_Type = InetAddress
_PktcEUEDevPCSCFAddr_Object = MibTableColumn
pktcEUEDevPCSCFAddr = _PktcEUEDevPCSCFAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 4, 1, 3),
    _PktcEUEDevPCSCFAddr_Type()
)
pktcEUEDevPCSCFAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFAddr.setStatus("current")
_PktcEUEDevPCSCFRowStatus_Type = RowStatus
_PktcEUEDevPCSCFRowStatus_Object = MibTableColumn
pktcEUEDevPCSCFRowStatus = _PktcEUEDevPCSCFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 4, 1, 4),
    _PktcEUEDevPCSCFRowStatus_Type()
)
pktcEUEDevPCSCFRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFRowStatus.setStatus("current")
_PktcEUEDevBSFTable_Object = MibTable
pktcEUEDevBSFTable = _PktcEUEDevBSFTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    pktcEUEDevBSFTable.setStatus("current")
_PktcEUEDevBSFEntry_Object = MibTableRow
pktcEUEDevBSFEntry = _PktcEUEDevBSFEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5, 1)
)
pktcEUEDevBSFEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFASType"),
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEDevBSFEntry.setStatus("current")
_PktcEUEDevBSFASType_Type = SnmpAdminString
_PktcEUEDevBSFASType_Object = MibTableColumn
pktcEUEDevBSFASType = _PktcEUEDevBSFASType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5, 1, 1),
    _PktcEUEDevBSFASType_Type()
)
pktcEUEDevBSFASType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEDevBSFASType.setStatus("current")


class _PktcEUEDevBSFIndex_Type(Unsigned32):
    """Custom type pktcEUEDevBSFIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PktcEUEDevBSFIndex_Type.__name__ = "Unsigned32"
_PktcEUEDevBSFIndex_Object = MibTableColumn
pktcEUEDevBSFIndex = _PktcEUEDevBSFIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5, 1, 2),
    _PktcEUEDevBSFIndex_Type()
)
pktcEUEDevBSFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEDevBSFIndex.setStatus("current")


class _PktcEUEDevBSFAddrType_Type(InetAddressType):
    """Custom type pktcEUEDevBSFAddrType based on InetAddressType"""


_PktcEUEDevBSFAddrType_Object = MibTableColumn
pktcEUEDevBSFAddrType = _PktcEUEDevBSFAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5, 1, 3),
    _PktcEUEDevBSFAddrType_Type()
)
pktcEUEDevBSFAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDevBSFAddrType.setStatus("current")
_PktcEUEDevBSFAddr_Type = InetAddress
_PktcEUEDevBSFAddr_Object = MibTableColumn
pktcEUEDevBSFAddr = _PktcEUEDevBSFAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5, 1, 4),
    _PktcEUEDevBSFAddr_Type()
)
pktcEUEDevBSFAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDevBSFAddr.setStatus("current")
_PktcEUEDevBSFRowStatus_Type = RowStatus
_PktcEUEDevBSFRowStatus_Object = MibTableColumn
pktcEUEDevBSFRowStatus = _PktcEUEDevBSFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 5, 1, 5),
    _PktcEUEDevBSFRowStatus_Type()
)
pktcEUEDevBSFRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevBSFRowStatus.setStatus("current")
_PktcEUECBSupport_Type = TruthValue
_PktcEUECBSupport_Object = MibScalar
pktcEUECBSupport = _PktcEUECBSupport_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 6),
    _PktcEUECBSupport_Type()
)
pktcEUECBSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUECBSupport.setStatus("current")


class _PktcEUECBEnable_Type(TruthValue):
    """Custom type pktcEUECBEnable based on TruthValue"""


_PktcEUECBEnable_Object = MibScalar
pktcEUECBEnable = _PktcEUECBEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 7),
    _PktcEUECBEnable_Type()
)
pktcEUECBEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUECBEnable.setStatus("current")


class _PktcEUECBData_Type(OctetString):
    """Custom type pktcEUECBData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_PktcEUECBData_Type.__name__ = "OctetString"
_PktcEUECBData_Object = MibScalar
pktcEUECBData = _PktcEUECBData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1, 8),
    _PktcEUECBData_Type()
)
pktcEUECBData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUECBData.setStatus("current")
_PktcEUEDevConformance_ObjectIdentity = ObjectIdentity
pktcEUEDevConformance = _PktcEUEDevConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2)
)
_PktcEUEDevCompliances_ObjectIdentity = ObjectIdentity
pktcEUEDevCompliances = _PktcEUEDevCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 1)
)
_PktcEUEDevMIBCompliances_ObjectIdentity = ObjectIdentity
pktcEUEDevMIBCompliances = _PktcEUEDevMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 1)
)
_PktcEUEDevGroups_ObjectIdentity = ObjectIdentity
pktcEUEDevGroups = _PktcEUEDevGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2)
)
_PktcEUEDevMIBGroups_ObjectIdentity = ObjectIdentity
pktcEUEDevMIBGroups = _PktcEUEDevMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2)
)

# Managed Objects groups

pktcEUEDevProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2, 1)
)
pktcEUEDevProfileGroup.setObjects(
    ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevProfileVersion")
)
if mibBuilder.loadTexts:
    pktcEUEDevProfileGroup.setStatus("current")

pktcEUEDevOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2, 2)
)
pktcEUEDevOpGroup.setObjects(
      *(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpDomain"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNAddrType"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNAddr"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNAddrPort"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNRelayAddrType"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNRelayAddr"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNRelayAddrPort"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNRelayCredsType"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNRelayCreds"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpTimerT1"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpTimerT2"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpTimerT4"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpRowStatus"))
)
if mibBuilder.loadTexts:
    pktcEUEDevOpGroup.setStatus("current")

pktcEUEDevDnsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2, 3)
)
pktcEUEDevDnsGroup.setObjects(
      *(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsAddrType"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsAddr"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsRowStatus"))
)
if mibBuilder.loadTexts:
    pktcEUEDevDnsGroup.setStatus("current")

pktcEUEDevPCSCFGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2, 4)
)
pktcEUEDevPCSCFGroup.setObjects(
      *(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFAddrType"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFAddr"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFRowStatus"))
)
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFGroup.setStatus("current")

pktcEUEDevBSFGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2, 5)
)
pktcEUEDevBSFGroup.setObjects(
      *(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFAddrType"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFAddr"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFRowStatus"))
)
if mibBuilder.loadTexts:
    pktcEUEDevBSFGroup.setStatus("current")

pktcEUEDevCBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2, 6)
)
pktcEUEDevCBGroup.setObjects(
      *(("CL-PKTC-EUE-DEV-MIB", "pktcEUECBSupport"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUECBEnable"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUECBData"))
)
if mibBuilder.loadTexts:
    pktcEUEDevCBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcPACM2UEMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcPACM2UEMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PKTC-EUE-DEV-MIB",
    **{"pktcEUEDevMIB": pktcEUEDevMIB,
       "pktcEUEDevNotification": pktcEUEDevNotification,
       "pktcEUEDevObjects": pktcEUEDevObjects,
       "pktcEUEDevProfile": pktcEUEDevProfile,
       "pktcEUEDevProfileVersion": pktcEUEDevProfileVersion,
       "pktcEUEDevOpTable": pktcEUEDevOpTable,
       "pktcEUEDevOpEntry": pktcEUEDevOpEntry,
       "pktcEUEDevOpIndex": pktcEUEDevOpIndex,
       "pktcEUEDevOpDomain": pktcEUEDevOpDomain,
       "pktcEUEDevOpSTUNAddrType": pktcEUEDevOpSTUNAddrType,
       "pktcEUEDevOpSTUNAddr": pktcEUEDevOpSTUNAddr,
       "pktcEUEDevOpSTUNAddrPort": pktcEUEDevOpSTUNAddrPort,
       "pktcEUEDevOpSTUNRelayAddrType": pktcEUEDevOpSTUNRelayAddrType,
       "pktcEUEDevOpSTUNRelayAddr": pktcEUEDevOpSTUNRelayAddr,
       "pktcEUEDevOpSTUNRelayAddrPort": pktcEUEDevOpSTUNRelayAddrPort,
       "pktcEUEDevOpSTUNRelayCredsType": pktcEUEDevOpSTUNRelayCredsType,
       "pktcEUEDevOpSTUNRelayCreds": pktcEUEDevOpSTUNRelayCreds,
       "pktcEUEDevOpTimerT1": pktcEUEDevOpTimerT1,
       "pktcEUEDevOpTimerT2": pktcEUEDevOpTimerT2,
       "pktcEUEDevOpTimerT4": pktcEUEDevOpTimerT4,
       "pktcEUEDevOpRowStatus": pktcEUEDevOpRowStatus,
       "pktcEUEDevDnsTable": pktcEUEDevDnsTable,
       "pktcEUEDevDnsEntry": pktcEUEDevDnsEntry,
       "pktcEUEDevDnsIndex": pktcEUEDevDnsIndex,
       "pktcEUEDevDnsAddrType": pktcEUEDevDnsAddrType,
       "pktcEUEDevDnsAddr": pktcEUEDevDnsAddr,
       "pktcEUEDevDnsRowStatus": pktcEUEDevDnsRowStatus,
       "pktcEUEDevPCSCFTable": pktcEUEDevPCSCFTable,
       "pktcEUEDevPCSCFEntry": pktcEUEDevPCSCFEntry,
       "pktcEUEDevPCSCFIndex": pktcEUEDevPCSCFIndex,
       "pktcEUEDevPCSCFAddrType": pktcEUEDevPCSCFAddrType,
       "pktcEUEDevPCSCFAddr": pktcEUEDevPCSCFAddr,
       "pktcEUEDevPCSCFRowStatus": pktcEUEDevPCSCFRowStatus,
       "pktcEUEDevBSFTable": pktcEUEDevBSFTable,
       "pktcEUEDevBSFEntry": pktcEUEDevBSFEntry,
       "pktcEUEDevBSFASType": pktcEUEDevBSFASType,
       "pktcEUEDevBSFIndex": pktcEUEDevBSFIndex,
       "pktcEUEDevBSFAddrType": pktcEUEDevBSFAddrType,
       "pktcEUEDevBSFAddr": pktcEUEDevBSFAddr,
       "pktcEUEDevBSFRowStatus": pktcEUEDevBSFRowStatus,
       "pktcEUECBSupport": pktcEUECBSupport,
       "pktcEUECBEnable": pktcEUECBEnable,
       "pktcEUECBData": pktcEUECBData,
       "pktcEUEDevConformance": pktcEUEDevConformance,
       "pktcEUEDevCompliances": pktcEUEDevCompliances,
       "pktcEUEDevMIBCompliances": pktcEUEDevMIBCompliances,
       "pktcPACM2UEMIBCompliance": pktcPACM2UEMIBCompliance,
       "pktcEUEDevGroups": pktcEUEDevGroups,
       "pktcEUEDevMIBGroups": pktcEUEDevMIBGroups,
       "pktcEUEDevProfileGroup": pktcEUEDevProfileGroup,
       "pktcEUEDevOpGroup": pktcEUEDevOpGroup,
       "pktcEUEDevDnsGroup": pktcEUEDevDnsGroup,
       "pktcEUEDevPCSCFGroup": pktcEUEDevPCSCFGroup,
       "pktcEUEDevBSFGroup": pktcEUEDevBSFGroup,
       "pktcEUEDevCBGroup": pktcEUEDevCBGroup}
)
