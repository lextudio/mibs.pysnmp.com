# SNMP MIB module (ACC-ARP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-ARP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:44 2024
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

(DLCI,
 frCircuitDlci) = mibBuilder.importSymbols(
    "ACC-FAKE",
    "DLCI",
    "frCircuitDlci")

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

(ipAdEntAddr,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAdEntAddr")

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

_AccArp_ObjectIdentity = ObjectIdentity
accArp = _AccArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11)
)


class _AccArpTimeout_Type(Integer32):
    """Custom type accArpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_AccArpTimeout_Type.__name__ = "Integer32"
_AccArpTimeout_Object = MibScalar
accArpTimeout = _AccArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 1),
    _AccArpTimeout_Type()
)
accArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accArpTimeout.setStatus("mandatory")
_AccArpTable_Object = MibTable
accArpTable = _AccArpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    accArpTable.setStatus("mandatory")
_AccArpEntry_Object = MibTableRow
accArpEntry = _AccArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 2, 1)
)
accArpEntry.setIndexNames(
    (0, "ACC-ARP", "accArpNetAddress"),
)
if mibBuilder.loadTexts:
    accArpEntry.setStatus("mandatory")
_AccArpPhysAddress_Type = OctetString
_AccArpPhysAddress_Object = MibTableColumn
accArpPhysAddress = _AccArpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 2, 1, 1),
    _AccArpPhysAddress_Type()
)
accArpPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpPhysAddress.setStatus("mandatory")
_AccArpNetAddress_Type = IpAddress
_AccArpNetAddress_Object = MibTableColumn
accArpNetAddress = _AccArpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 2, 1, 2),
    _AccArpNetAddress_Type()
)
accArpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpNetAddress.setStatus("mandatory")


class _AccArpEntStatus_Type(Integer32):
    """Custom type accArpEntStatus based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("apepending", 16),
          ("confirmpending", 64),
          ("confirmsrpending", 128),
          ("dynamic", 2),
          ("pending", 1),
          ("permanent", 8),
          ("static", 4),
          ("stepending", 32))
    )


_AccArpEntStatus_Type.__name__ = "Integer32"
_AccArpEntStatus_Object = MibTableColumn
accArpEntStatus = _AccArpEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 2, 1, 3),
    _AccArpEntStatus_Type()
)
accArpEntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpEntStatus.setStatus("mandatory")


class _AccArpType_Type(Integer32):
    """Custom type accArpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("proxy", 2))
    )


_AccArpType_Type.__name__ = "Integer32"
_AccArpType_Object = MibScalar
accArpType = _AccArpType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 3),
    _AccArpType_Type()
)
accArpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accArpType.setStatus("mandatory")
_AccArpReqRcvds_Type = Counter32
_AccArpReqRcvds_Object = MibScalar
accArpReqRcvds = _AccArpReqRcvds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 4),
    _AccArpReqRcvds_Type()
)
accArpReqRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpReqRcvds.setStatus("mandatory")
_AccArpReqSents_Type = Counter32
_AccArpReqSents_Object = MibScalar
accArpReqSents = _AccArpReqSents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 5),
    _AccArpReqSents_Type()
)
accArpReqSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpReqSents.setStatus("mandatory")
_AccArpRspRcvds_Type = Counter32
_AccArpRspRcvds_Object = MibScalar
accArpRspRcvds = _AccArpRspRcvds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 6),
    _AccArpRspRcvds_Type()
)
accArpRspRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpRspRcvds.setStatus("mandatory")
_AccArpRspSents_Type = Counter32
_AccArpRspSents_Object = MibScalar
accArpRspSents = _AccArpRspSents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 7),
    _AccArpRspSents_Type()
)
accArpRspSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpRspSents.setStatus("mandatory")
_AccArpInErrs_Type = Counter32
_AccArpInErrs_Object = MibScalar
accArpInErrs = _AccArpInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 8),
    _AccArpInErrs_Type()
)
accArpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpInErrs.setStatus("mandatory")
_AccArpOutErrs_Type = Counter32
_AccArpOutErrs_Object = MibScalar
accArpOutErrs = _AccArpOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 9),
    _AccArpOutErrs_Type()
)
accArpOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpOutErrs.setStatus("mandatory")
_AccArpUnknownProtos_Type = Counter32
_AccArpUnknownProtos_Object = MibScalar
accArpUnknownProtos = _AccArpUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 10),
    _AccArpUnknownProtos_Type()
)
accArpUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpUnknownProtos.setStatus("mandatory")


class _AccArpPromiscuous_Type(Integer32):
    """Custom type accArpPromiscuous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonpromiscuous", 2),
          ("promiscuous", 1))
    )


_AccArpPromiscuous_Type.__name__ = "Integer32"
_AccArpPromiscuous_Object = MibScalar
accArpPromiscuous = _AccArpPromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 11),
    _AccArpPromiscuous_Type()
)
accArpPromiscuous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accArpPromiscuous.setStatus("mandatory")


class _AccArpRefresh_Type(Integer32):
    """Custom type accArpRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norefresh", 2),
          ("refresh", 1))
    )


_AccArpRefresh_Type.__name__ = "Integer32"
_AccArpRefresh_Object = MibScalar
accArpRefresh = _AccArpRefresh_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 12),
    _AccArpRefresh_Type()
)
accArpRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accArpRefresh.setStatus("mandatory")
_AccArpAddressCheck_ObjectIdentity = ObjectIdentity
accArpAddressCheck = _AccArpAddressCheck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 13)
)
_AccArpTraps_ObjectIdentity = ObjectIdentity
accArpTraps = _AccArpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 14)
)
_AccArpTrapMsg_Type = DisplayString
_AccArpTrapMsg_Object = MibScalar
accArpTrapMsg = _AccArpTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 14, 1),
    _AccArpTrapMsg_Type()
)
accArpTrapMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accArpTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accArpDuplicateAddrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 14, 0, 1)
)
accArpDuplicateAddrTrap.setObjects(
      *(("ACC-ARP", "accArpTrapMsg"),
        ("IP-MIB", "ipAdEntAddr"),
        ("ACC-FAKE", "frCircuitDlci"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accArpDuplicateAddrTrap.setStatus(
        ""
    )

accArpInvDevTypeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 14, 0, 2)
)
accArpInvDevTypeTrap.setObjects(
      *(("ACC-ARP", "accArpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accArpInvDevTypeTrap.setStatus(
        ""
    )

accArpDuplIpOnMacTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 14, 0, 3)
)
accArpDuplIpOnMacTrap.setObjects(
      *(("ACC-ARP", "accArpTrapMsg"),
        ("ACC-ARP", "accArpNetAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accArpDuplIpOnMacTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-ARP",
    **{"accArp": accArp,
       "accArpTimeout": accArpTimeout,
       "accArpTable": accArpTable,
       "accArpEntry": accArpEntry,
       "accArpPhysAddress": accArpPhysAddress,
       "accArpNetAddress": accArpNetAddress,
       "accArpEntStatus": accArpEntStatus,
       "accArpType": accArpType,
       "accArpReqRcvds": accArpReqRcvds,
       "accArpReqSents": accArpReqSents,
       "accArpRspRcvds": accArpRspRcvds,
       "accArpRspSents": accArpRspSents,
       "accArpInErrs": accArpInErrs,
       "accArpOutErrs": accArpOutErrs,
       "accArpUnknownProtos": accArpUnknownProtos,
       "accArpPromiscuous": accArpPromiscuous,
       "accArpRefresh": accArpRefresh,
       "accArpAddressCheck": accArpAddressCheck,
       "accArpTraps": accArpTraps,
       "accArpDuplicateAddrTrap": accArpDuplicateAddrTrap,
       "accArpInvDevTypeTrap": accArpInvDevTypeTrap,
       "accArpDuplIpOnMacTrap": accArpDuplIpOnMacTrap,
       "accArpTrapMsg": accArpTrapMsg}
)
