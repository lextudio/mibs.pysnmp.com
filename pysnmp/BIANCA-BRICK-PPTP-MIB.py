# SNMP MIB module (BIANCA-BRICK-PPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-PPTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:42 2024
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

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Vpn_ObjectIdentity = ObjectIdentity
vpn = _Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 23)
)
_PptpProfileTable_Object = MibTable
pptpProfileTable = _PptpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1)
)
if mibBuilder.loadTexts:
    pptpProfileTable.setStatus("mandatory")
_PptpProfileEntry_Object = MibTableRow
pptpProfileEntry = _PptpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1)
)
pptpProfileEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPTP-MIB", "pptpProfileId"),
)
if mibBuilder.loadTexts:
    pptpProfileEntry.setStatus("mandatory")
_PptpProfileId_Type = Integer32
_PptpProfileId_Object = MibTableColumn
pptpProfileId = _PptpProfileId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 1),
    _PptpProfileId_Type()
)
pptpProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileId.setStatus("mandatory")


class _PptpProfileKeepalive_Type(Integer32):
    """Custom type pptpProfileKeepalive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("off", 2),
          ("on", 1))
    )


_PptpProfileKeepalive_Type.__name__ = "Integer32"
_PptpProfileKeepalive_Object = MibTableColumn
pptpProfileKeepalive = _PptpProfileKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 2),
    _PptpProfileKeepalive_Type()
)
pptpProfileKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileKeepalive.setStatus("mandatory")


class _PptpProfileMaxRequests_Type(Integer32):
    """Custom type pptpProfileMaxRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PptpProfileMaxRequests_Type.__name__ = "Integer32"
_PptpProfileMaxRequests_Object = MibTableColumn
pptpProfileMaxRequests = _PptpProfileMaxRequests_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 3),
    _PptpProfileMaxRequests_Type()
)
pptpProfileMaxRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileMaxRequests.setStatus("mandatory")


class _PptpProfileMaxBlockTime_Type(Integer32):
    """Custom type pptpProfileMaxBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_PptpProfileMaxBlockTime_Type.__name__ = "Integer32"
_PptpProfileMaxBlockTime_Object = MibTableColumn
pptpProfileMaxBlockTime = _PptpProfileMaxBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 4),
    _PptpProfileMaxBlockTime_Type()
)
pptpProfileMaxBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileMaxBlockTime.setStatus("mandatory")


class _PptpProfileMaxAckTimeout_Type(Integer32):
    """Custom type pptpProfileMaxAckTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 5000),
    )


_PptpProfileMaxAckTimeout_Type.__name__ = "Integer32"
_PptpProfileMaxAckTimeout_Object = MibTableColumn
pptpProfileMaxAckTimeout = _PptpProfileMaxAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 5),
    _PptpProfileMaxAckTimeout_Type()
)
pptpProfileMaxAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileMaxAckTimeout.setStatus("mandatory")


class _PptpProfileReassemblyTimeout_Type(Integer32):
    """Custom type pptpProfileReassemblyTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_PptpProfileReassemblyTimeout_Type.__name__ = "Integer32"
_PptpProfileReassemblyTimeout_Object = MibTableColumn
pptpProfileReassemblyTimeout = _PptpProfileReassemblyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 6),
    _PptpProfileReassemblyTimeout_Type()
)
pptpProfileReassemblyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileReassemblyTimeout.setStatus("mandatory")
_PptpCtlConnTable_Object = MibTable
pptpCtlConnTable = _PptpCtlConnTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2)
)
if mibBuilder.loadTexts:
    pptpCtlConnTable.setStatus("mandatory")
_PptpCtlConnEntry_Object = MibTableRow
pptpCtlConnEntry = _PptpCtlConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1)
)
pptpCtlConnEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPTP-MIB", "pptpCtlConnOriginator"),
)
if mibBuilder.loadTexts:
    pptpCtlConnEntry.setStatus("mandatory")


class _PptpCtlConnOriginator_Type(Integer32):
    """Custom type pptpCtlConnOriginator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_PptpCtlConnOriginator_Type.__name__ = "Integer32"
_PptpCtlConnOriginator_Object = MibTableColumn
pptpCtlConnOriginator = _PptpCtlConnOriginator_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 1),
    _PptpCtlConnOriginator_Type()
)
pptpCtlConnOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnOriginator.setStatus("mandatory")
_PptpCtlConnAge_Type = TimeTicks
_PptpCtlConnAge_Object = MibTableColumn
pptpCtlConnAge = _PptpCtlConnAge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 2),
    _PptpCtlConnAge_Type()
)
pptpCtlConnAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnAge.setStatus("mandatory")


class _PptpCtlConnState_Type(Integer32):
    """Custom type pptpCtlConnState based on Integer32"""
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
        *(("established", 3),
          ("idle", 1),
          ("wait-ctl-reply", 2),
          ("wait-stop-reply", 4))
    )


_PptpCtlConnState_Type.__name__ = "Integer32"
_PptpCtlConnState_Object = MibTableColumn
pptpCtlConnState = _PptpCtlConnState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 3),
    _PptpCtlConnState_Type()
)
pptpCtlConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCtlConnState.setStatus("mandatory")
_PptpCtlConnRemoteIpAddress_Type = IpAddress
_PptpCtlConnRemoteIpAddress_Object = MibTableColumn
pptpCtlConnRemoteIpAddress = _PptpCtlConnRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 4),
    _PptpCtlConnRemoteIpAddress_Type()
)
pptpCtlConnRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnRemoteIpAddress.setStatus("mandatory")
_PptpCtlConnLocalIpAddress_Type = IpAddress
_PptpCtlConnLocalIpAddress_Object = MibTableColumn
pptpCtlConnLocalIpAddress = _PptpCtlConnLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 5),
    _PptpCtlConnLocalIpAddress_Type()
)
pptpCtlConnLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnLocalIpAddress.setStatus("mandatory")
_PptpCtlConnVersion_Type = Integer32
_PptpCtlConnVersion_Object = MibTableColumn
pptpCtlConnVersion = _PptpCtlConnVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 6),
    _PptpCtlConnVersion_Type()
)
pptpCtlConnVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnVersion.setStatus("mandatory")
_PptpCtlConnHost_Type = DisplayString
_PptpCtlConnHost_Object = MibTableColumn
pptpCtlConnHost = _PptpCtlConnHost_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 7),
    _PptpCtlConnHost_Type()
)
pptpCtlConnHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnHost.setStatus("mandatory")
_PptpCtlConnVendor_Type = DisplayString
_PptpCtlConnVendor_Object = MibTableColumn
pptpCtlConnVendor = _PptpCtlConnVendor_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 8),
    _PptpCtlConnVendor_Type()
)
pptpCtlConnVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnVendor.setStatus("mandatory")
_PptpCtlConnFirmRev_Type = Integer32
_PptpCtlConnFirmRev_Object = MibTableColumn
pptpCtlConnFirmRev = _PptpCtlConnFirmRev_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 9),
    _PptpCtlConnFirmRev_Type()
)
pptpCtlConnFirmRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnFirmRev.setStatus("mandatory")
_PptpCallTable_Object = MibTable
pptpCallTable = _PptpCallTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3)
)
if mibBuilder.loadTexts:
    pptpCallTable.setStatus("mandatory")
_PptpCallEntry_Object = MibTableRow
pptpCallEntry = _PptpCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1)
)
pptpCallEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPTP-MIB", "pptpCallType"),
)
if mibBuilder.loadTexts:
    pptpCallEntry.setStatus("mandatory")


class _PptpCallType_Type(Integer32):
    """Custom type pptpCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pac", 1),
          ("pns", 2))
    )


_PptpCallType_Type.__name__ = "Integer32"
_PptpCallType_Object = MibTableColumn
pptpCallType = _PptpCallType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 1),
    _PptpCallType_Type()
)
pptpCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallType.setStatus("mandatory")


class _PptpCallDirection_Type(Integer32):
    """Custom type pptpCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_PptpCallDirection_Type.__name__ = "Integer32"
_PptpCallDirection_Object = MibTableColumn
pptpCallDirection = _PptpCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 2),
    _PptpCallDirection_Type()
)
pptpCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallDirection.setStatus("mandatory")
_PptpCallAge_Type = TimeTicks
_PptpCallAge_Object = MibTableColumn
pptpCallAge = _PptpCallAge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 3),
    _PptpCallAge_Type()
)
pptpCallAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallAge.setStatus("mandatory")


class _PptpCallState_Type(Integer32):
    """Custom type pptpCallState based on Integer32"""
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
        *(("established", 5),
          ("idle", 1),
          ("wait-connect", 4),
          ("wait-cs-ans", 2),
          ("wait-disc", 6),
          ("wait-reply", 3))
    )


_PptpCallState_Type.__name__ = "Integer32"
_PptpCallState_Object = MibTableColumn
pptpCallState = _PptpCallState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 4),
    _PptpCallState_Type()
)
pptpCallState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCallState.setStatus("mandatory")
_PptpCallRemoteIpAddress_Type = IpAddress
_PptpCallRemoteIpAddress_Object = MibTableColumn
pptpCallRemoteIpAddress = _PptpCallRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 5),
    _PptpCallRemoteIpAddress_Type()
)
pptpCallRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallRemoteIpAddress.setStatus("mandatory")
_PptpCallLocalIpAddress_Type = IpAddress
_PptpCallLocalIpAddress_Object = MibTableColumn
pptpCallLocalIpAddress = _PptpCallLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 6),
    _PptpCallLocalIpAddress_Type()
)
pptpCallLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallLocalIpAddress.setStatus("mandatory")
_PptpCallReceivedPackets_Type = Counter32
_PptpCallReceivedPackets_Object = MibTableColumn
pptpCallReceivedPackets = _PptpCallReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 7),
    _PptpCallReceivedPackets_Type()
)
pptpCallReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallReceivedPackets.setStatus("mandatory")
_PptpCallReceivedOctets_Type = Counter32
_PptpCallReceivedOctets_Object = MibTableColumn
pptpCallReceivedOctets = _PptpCallReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 8),
    _PptpCallReceivedOctets_Type()
)
pptpCallReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallReceivedOctets.setStatus("mandatory")
_PptpCallReceivedErrors_Type = Counter32
_PptpCallReceivedErrors_Object = MibTableColumn
pptpCallReceivedErrors = _PptpCallReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 9),
    _PptpCallReceivedErrors_Type()
)
pptpCallReceivedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallReceivedErrors.setStatus("mandatory")
_PptpCallTransmitPackets_Type = Counter32
_PptpCallTransmitPackets_Object = MibTableColumn
pptpCallTransmitPackets = _PptpCallTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 10),
    _PptpCallTransmitPackets_Type()
)
pptpCallTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallTransmitPackets.setStatus("mandatory")
_PptpCallTransmitOctets_Type = Counter32
_PptpCallTransmitOctets_Object = MibTableColumn
pptpCallTransmitOctets = _PptpCallTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 11),
    _PptpCallTransmitOctets_Type()
)
pptpCallTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallTransmitOctets.setStatus("mandatory")
_PptpCallTransmitErrors_Type = Counter32
_PptpCallTransmitErrors_Object = MibTableColumn
pptpCallTransmitErrors = _PptpCallTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 12),
    _PptpCallTransmitErrors_Type()
)
pptpCallTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallTransmitErrors.setStatus("mandatory")
_PptpCallInfo_Type = DisplayString
_PptpCallInfo_Object = MibTableColumn
pptpCallInfo = _PptpCallInfo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 13),
    _PptpCallInfo_Type()
)
pptpCallInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallInfo.setStatus("mandatory")
_PptpCreditsTable_Object = MibTable
pptpCreditsTable = _PptpCreditsTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4)
)
if mibBuilder.loadTexts:
    pptpCreditsTable.setStatus("mandatory")
_PptpCreditsEntry_Object = MibTableRow
pptpCreditsEntry = _PptpCreditsEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1)
)
pptpCreditsEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPTP-MIB", "pptpCreditsSubsysNumber"),
)
if mibBuilder.loadTexts:
    pptpCreditsEntry.setStatus("mandatory")


class _PptpCreditsSubsysNumber_Type(Integer32):
    """Custom type pptpCreditsSubsysNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 2),
          ("ppp", 1))
    )


_PptpCreditsSubsysNumber_Type.__name__ = "Integer32"
_PptpCreditsSubsysNumber_Object = MibTableColumn
pptpCreditsSubsysNumber = _PptpCreditsSubsysNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 1),
    _PptpCreditsSubsysNumber_Type()
)
pptpCreditsSubsysNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCreditsSubsysNumber.setStatus("mandatory")


class _PptpCreditsSurveillance_Type(Integer32):
    """Custom type pptpCreditsSurveillance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_PptpCreditsSurveillance_Type.__name__ = "Integer32"
_PptpCreditsSurveillance_Object = MibTableColumn
pptpCreditsSurveillance = _PptpCreditsSurveillance_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 2),
    _PptpCreditsSurveillance_Type()
)
pptpCreditsSurveillance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCreditsSurveillance.setStatus("mandatory")
_PptpCreditsMeasuretime_Type = Integer32
_PptpCreditsMeasuretime_Object = MibTableColumn
pptpCreditsMeasuretime = _PptpCreditsMeasuretime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 3),
    _PptpCreditsMeasuretime_Type()
)
pptpCreditsMeasuretime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCreditsMeasuretime.setStatus("mandatory")
_PptpCreditsMaxInCon_Type = Integer32
_PptpCreditsMaxInCon_Object = MibTableColumn
pptpCreditsMaxInCon = _PptpCreditsMaxInCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 4),
    _PptpCreditsMaxInCon_Type()
)
pptpCreditsMaxInCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCreditsMaxInCon.setStatus("mandatory")
_PptpCreditsMaxOutCon_Type = Integer32
_PptpCreditsMaxOutCon_Object = MibTableColumn
pptpCreditsMaxOutCon = _PptpCreditsMaxOutCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 5),
    _PptpCreditsMaxOutCon_Type()
)
pptpCreditsMaxOutCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCreditsMaxOutCon.setStatus("mandatory")
_PptpCreditsMaxInDuration_Type = Integer32
_PptpCreditsMaxInDuration_Object = MibTableColumn
pptpCreditsMaxInDuration = _PptpCreditsMaxInDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 6),
    _PptpCreditsMaxInDuration_Type()
)
pptpCreditsMaxInDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCreditsMaxInDuration.setStatus("mandatory")
_PptpCreditsMaxOutDuration_Type = Integer32
_PptpCreditsMaxOutDuration_Object = MibTableColumn
pptpCreditsMaxOutDuration = _PptpCreditsMaxOutDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 7),
    _PptpCreditsMaxOutDuration_Type()
)
pptpCreditsMaxOutDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCreditsMaxOutDuration.setStatus("mandatory")
_PptpCreditsTimeleft_Type = Integer32
_PptpCreditsTimeleft_Object = MibTableColumn
pptpCreditsTimeleft = _PptpCreditsTimeleft_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 8),
    _PptpCreditsTimeleft_Type()
)
pptpCreditsTimeleft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCreditsTimeleft.setStatus("mandatory")
_PptpCreditsCurrentInCon_Type = Integer32
_PptpCreditsCurrentInCon_Object = MibTableColumn
pptpCreditsCurrentInCon = _PptpCreditsCurrentInCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 9),
    _PptpCreditsCurrentInCon_Type()
)
pptpCreditsCurrentInCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCreditsCurrentInCon.setStatus("mandatory")
_PptpCreditsCurrentOutCon_Type = Integer32
_PptpCreditsCurrentOutCon_Object = MibTableColumn
pptpCreditsCurrentOutCon = _PptpCreditsCurrentOutCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 10),
    _PptpCreditsCurrentOutCon_Type()
)
pptpCreditsCurrentOutCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCreditsCurrentOutCon.setStatus("mandatory")
_PptpCreditsTotalInCon_Type = Integer32
_PptpCreditsTotalInCon_Object = MibTableColumn
pptpCreditsTotalInCon = _PptpCreditsTotalInCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 11),
    _PptpCreditsTotalInCon_Type()
)
pptpCreditsTotalInCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCreditsTotalInCon.setStatus("mandatory")
_PptpCreditsTotalOutCon_Type = Integer32
_PptpCreditsTotalOutCon_Object = MibTableColumn
pptpCreditsTotalOutCon = _PptpCreditsTotalOutCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 12),
    _PptpCreditsTotalOutCon_Type()
)
pptpCreditsTotalOutCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCreditsTotalOutCon.setStatus("mandatory")
_PptpCreditsTotalMaxCon_Type = Integer32
_PptpCreditsTotalMaxCon_Object = MibTableColumn
pptpCreditsTotalMaxCon = _PptpCreditsTotalMaxCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 13),
    _PptpCreditsTotalMaxCon_Type()
)
pptpCreditsTotalMaxCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCreditsTotalMaxCon.setStatus("mandatory")
_PptpCreditsTotalInDuration_Type = Integer32
_PptpCreditsTotalInDuration_Object = MibTableColumn
pptpCreditsTotalInDuration = _PptpCreditsTotalInDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 14),
    _PptpCreditsTotalInDuration_Type()
)
pptpCreditsTotalInDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCreditsTotalInDuration.setStatus("mandatory")
_PptpCreditsTotalOutDuration_Type = Integer32
_PptpCreditsTotalOutDuration_Object = MibTableColumn
pptpCreditsTotalOutDuration = _PptpCreditsTotalOutDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 15),
    _PptpCreditsTotalOutDuration_Type()
)
pptpCreditsTotalOutDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCreditsTotalOutDuration.setStatus("mandatory")
_PptpCreditsMaxCurrentInCon_Type = Integer32
_PptpCreditsMaxCurrentInCon_Object = MibTableColumn
pptpCreditsMaxCurrentInCon = _PptpCreditsMaxCurrentInCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 16),
    _PptpCreditsMaxCurrentInCon_Type()
)
pptpCreditsMaxCurrentInCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCreditsMaxCurrentInCon.setStatus("mandatory")
_PptpCreditsMaxCurrentOutCon_Type = Integer32
_PptpCreditsMaxCurrentOutCon_Object = MibTableColumn
pptpCreditsMaxCurrentOutCon = _PptpCreditsMaxCurrentOutCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 17),
    _PptpCreditsMaxCurrentOutCon_Type()
)
pptpCreditsMaxCurrentOutCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCreditsMaxCurrentOutCon.setStatus("mandatory")
_PptpCreditsMaxCurrentCon_Type = Integer32
_PptpCreditsMaxCurrentCon_Object = MibTableColumn
pptpCreditsMaxCurrentCon = _PptpCreditsMaxCurrentCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 18),
    _PptpCreditsMaxCurrentCon_Type()
)
pptpCreditsMaxCurrentCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCreditsMaxCurrentCon.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-PPTP-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "vpn": vpn,
       "pptpProfileTable": pptpProfileTable,
       "pptpProfileEntry": pptpProfileEntry,
       "pptpProfileId": pptpProfileId,
       "pptpProfileKeepalive": pptpProfileKeepalive,
       "pptpProfileMaxRequests": pptpProfileMaxRequests,
       "pptpProfileMaxBlockTime": pptpProfileMaxBlockTime,
       "pptpProfileMaxAckTimeout": pptpProfileMaxAckTimeout,
       "pptpProfileReassemblyTimeout": pptpProfileReassemblyTimeout,
       "pptpCtlConnTable": pptpCtlConnTable,
       "pptpCtlConnEntry": pptpCtlConnEntry,
       "pptpCtlConnOriginator": pptpCtlConnOriginator,
       "pptpCtlConnAge": pptpCtlConnAge,
       "pptpCtlConnState": pptpCtlConnState,
       "pptpCtlConnRemoteIpAddress": pptpCtlConnRemoteIpAddress,
       "pptpCtlConnLocalIpAddress": pptpCtlConnLocalIpAddress,
       "pptpCtlConnVersion": pptpCtlConnVersion,
       "pptpCtlConnHost": pptpCtlConnHost,
       "pptpCtlConnVendor": pptpCtlConnVendor,
       "pptpCtlConnFirmRev": pptpCtlConnFirmRev,
       "pptpCallTable": pptpCallTable,
       "pptpCallEntry": pptpCallEntry,
       "pptpCallType": pptpCallType,
       "pptpCallDirection": pptpCallDirection,
       "pptpCallAge": pptpCallAge,
       "pptpCallState": pptpCallState,
       "pptpCallRemoteIpAddress": pptpCallRemoteIpAddress,
       "pptpCallLocalIpAddress": pptpCallLocalIpAddress,
       "pptpCallReceivedPackets": pptpCallReceivedPackets,
       "pptpCallReceivedOctets": pptpCallReceivedOctets,
       "pptpCallReceivedErrors": pptpCallReceivedErrors,
       "pptpCallTransmitPackets": pptpCallTransmitPackets,
       "pptpCallTransmitOctets": pptpCallTransmitOctets,
       "pptpCallTransmitErrors": pptpCallTransmitErrors,
       "pptpCallInfo": pptpCallInfo,
       "pptpCreditsTable": pptpCreditsTable,
       "pptpCreditsEntry": pptpCreditsEntry,
       "pptpCreditsSubsysNumber": pptpCreditsSubsysNumber,
       "pptpCreditsSurveillance": pptpCreditsSurveillance,
       "pptpCreditsMeasuretime": pptpCreditsMeasuretime,
       "pptpCreditsMaxInCon": pptpCreditsMaxInCon,
       "pptpCreditsMaxOutCon": pptpCreditsMaxOutCon,
       "pptpCreditsMaxInDuration": pptpCreditsMaxInDuration,
       "pptpCreditsMaxOutDuration": pptpCreditsMaxOutDuration,
       "pptpCreditsTimeleft": pptpCreditsTimeleft,
       "pptpCreditsCurrentInCon": pptpCreditsCurrentInCon,
       "pptpCreditsCurrentOutCon": pptpCreditsCurrentOutCon,
       "pptpCreditsTotalInCon": pptpCreditsTotalInCon,
       "pptpCreditsTotalOutCon": pptpCreditsTotalOutCon,
       "pptpCreditsTotalMaxCon": pptpCreditsTotalMaxCon,
       "pptpCreditsTotalInDuration": pptpCreditsTotalInDuration,
       "pptpCreditsTotalOutDuration": pptpCreditsTotalOutDuration,
       "pptpCreditsMaxCurrentInCon": pptpCreditsMaxCurrentInCon,
       "pptpCreditsMaxCurrentOutCon": pptpCreditsMaxCurrentOutCon,
       "pptpCreditsMaxCurrentCon": pptpCreditsMaxCurrentCon}
)
