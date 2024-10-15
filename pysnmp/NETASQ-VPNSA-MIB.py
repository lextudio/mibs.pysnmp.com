# SNMP MIB module (NETASQ-VPNSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETASQ-VPNSA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:34 2024
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

(ntqVPN,) = mibBuilder.importSymbols(
    "NETASQ-SMI-MIB",
    "ntqVPN")

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

_NtqVPNSATable_Object = MibTable
ntqVPNSATable = _NtqVPNSATable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ntqVPNSATable.setStatus("current")
_NtqVPNSAEntry_Object = MibTableRow
ntqVPNSAEntry = _NtqVPNSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1)
)
ntqVPNSAEntry.setIndexNames(
    (0, "NETASQ-VPNSA-MIB", "ntqVPNSAIndex"),
)
if mibBuilder.loadTexts:
    ntqVPNSAEntry.setStatus("current")
_NtqVPNSAIndex_Type = Integer32
_NtqVPNSAIndex_Object = MibTableColumn
ntqVPNSAIndex = _NtqVPNSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 1),
    _NtqVPNSAIndex_Type()
)
ntqVPNSAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNSAIndex.setStatus("current")
_NtqVPNIPSrc_Type = DisplayString
_NtqVPNIPSrc_Object = MibTableColumn
ntqVPNIPSrc = _NtqVPNIPSrc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 2),
    _NtqVPNIPSrc_Type()
)
ntqVPNIPSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNIPSrc.setStatus("current")
_NtqVPNIPDst_Type = DisplayString
_NtqVPNIPDst_Object = MibTableColumn
ntqVPNIPDst = _NtqVPNIPDst_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 3),
    _NtqVPNIPDst_Type()
)
ntqVPNIPDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNIPDst.setStatus("current")


class _NtqVPNType_Type(Integer32):
    """Custom type ntqVPNType based on Integer32"""
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
        *(("ah", 2),
          ("esp", 3),
          ("ipcomp", 8),
          ("mip", 7),
          ("ospfv2", 5),
          ("ripv2", 6),
          ("rsvp", 4),
          ("unknown", 1),
          ("unspec", 0))
    )


_NtqVPNType_Type.__name__ = "Integer32"
_NtqVPNType_Object = MibTableColumn
ntqVPNType = _NtqVPNType_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 4),
    _NtqVPNType_Type()
)
ntqVPNType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNType.setStatus("current")


class _NtqVPNMode_Type(Integer32):
    """Custom type ntqVPNMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("transport", 1),
          ("tunnel", 2))
    )


_NtqVPNMode_Type.__name__ = "Integer32"
_NtqVPNMode_Object = MibTableColumn
ntqVPNMode = _NtqVPNMode_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 5),
    _NtqVPNMode_Type()
)
ntqVPNMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNMode.setStatus("current")
_NtqVPNSpi_Type = Integer32
_NtqVPNSpi_Object = MibTableColumn
ntqVPNSpi = _NtqVPNSpi_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 6),
    _NtqVPNSpi_Type()
)
ntqVPNSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNSpi.setStatus("current")
_NtqVPNPeerSpi_Type = Integer32
_NtqVPNPeerSpi_Object = MibTableColumn
ntqVPNPeerSpi = _NtqVPNPeerSpi_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 7),
    _NtqVPNPeerSpi_Type()
)
ntqVPNPeerSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNPeerSpi.setStatus("current")
_NtqVPNReqID_Type = Integer32
_NtqVPNReqID_Object = MibTableColumn
ntqVPNReqID = _NtqVPNReqID_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 8),
    _NtqVPNReqID_Type()
)
ntqVPNReqID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNReqID.setStatus("current")
_NtqVPNEnc_Type = DisplayString
_NtqVPNEnc_Object = MibTableColumn
ntqVPNEnc = _NtqVPNEnc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 9),
    _NtqVPNEnc_Type()
)
ntqVPNEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNEnc.setStatus("current")


class _NtqVPNAuth_Type(Integer32):
    """Custom type ntqVPNAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("hmac-md5", 1),
          ("hmac-sha1", 2),
          ("md5", 3),
          ("none", 0),
          ("null", 5),
          ("sha", 4))
    )


_NtqVPNAuth_Type.__name__ = "Integer32"
_NtqVPNAuth_Object = MibTableColumn
ntqVPNAuth = _NtqVPNAuth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 10),
    _NtqVPNAuth_Type()
)
ntqVPNAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNAuth.setStatus("current")


class _NtqVPNState_Type(Integer32):
    """Custom type ntqVPNState based on Integer32"""
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
        *(("dead", 3),
          ("dying", 2),
          ("larval", 0),
          ("mature", 1))
    )


_NtqVPNState_Type.__name__ = "Integer32"
_NtqVPNState_Object = MibTableColumn
ntqVPNState = _NtqVPNState_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 11),
    _NtqVPNState_Type()
)
ntqVPNState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNState.setStatus("current")
_NtqVPNLifetime_Type = Counter64
_NtqVPNLifetime_Object = MibTableColumn
ntqVPNLifetime = _NtqVPNLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 12),
    _NtqVPNLifetime_Type()
)
ntqVPNLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNLifetime.setStatus("current")
_NtqVPNBytes_Type = Counter64
_NtqVPNBytes_Object = MibTableColumn
ntqVPNBytes = _NtqVPNBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 13),
    _NtqVPNBytes_Type()
)
ntqVPNBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNBytes.setStatus("current")
_NtqVPNMaxLifetime_Type = Counter64
_NtqVPNMaxLifetime_Object = MibTableColumn
ntqVPNMaxLifetime = _NtqVPNMaxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 14),
    _NtqVPNMaxLifetime_Type()
)
ntqVPNMaxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNMaxLifetime.setStatus("current")
_NtqVPNMaxBytes_Type = Counter64
_NtqVPNMaxBytes_Object = MibTableColumn
ntqVPNMaxBytes = _NtqVPNMaxBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 15),
    _NtqVPNMaxBytes_Type()
)
ntqVPNMaxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqVPNMaxBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETASQ-VPNSA-MIB",
    **{"ntqVPNSATable": ntqVPNSATable,
       "ntqVPNSAEntry": ntqVPNSAEntry,
       "ntqVPNSAIndex": ntqVPNSAIndex,
       "ntqVPNIPSrc": ntqVPNIPSrc,
       "ntqVPNIPDst": ntqVPNIPDst,
       "ntqVPNType": ntqVPNType,
       "ntqVPNMode": ntqVPNMode,
       "ntqVPNSpi": ntqVPNSpi,
       "ntqVPNPeerSpi": ntqVPNPeerSpi,
       "ntqVPNReqID": ntqVPNReqID,
       "ntqVPNEnc": ntqVPNEnc,
       "ntqVPNAuth": ntqVPNAuth,
       "ntqVPNState": ntqVPNState,
       "ntqVPNLifetime": ntqVPNLifetime,
       "ntqVPNBytes": ntqVPNBytes,
       "ntqVPNMaxLifetime": ntqVPNMaxLifetime,
       "ntqVPNMaxBytes": ntqVPNMaxBytes}
)
