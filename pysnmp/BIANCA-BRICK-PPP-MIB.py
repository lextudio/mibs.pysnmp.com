# SNMP MIB module (BIANCA-BRICK-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:20 2024
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



class BitValue(Integer32):
    """Custom type BitValue based on Integer32"""




class Date(Integer32):
    """Custom type Date based on Integer32"""



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
_Ppp_ObjectIdentity = ObjectIdentity
ppp = _Ppp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 3)
)
_BiboPPPTable_Object = MibTable
biboPPPTable = _BiboPPPTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1)
)
if mibBuilder.loadTexts:
    biboPPPTable.setStatus("mandatory")
_BiboPPPEntry_Object = MibTableRow
biboPPPEntry = _BiboPPPEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1)
)
biboPPPEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPP-MIB", "biboPPPType"),
)
if mibBuilder.loadTexts:
    biboPPPEntry.setStatus("mandatory")
_BiboPPPIfIndex_Type = Integer32
_BiboPPPIfIndex_Object = MibTableColumn
biboPPPIfIndex = _BiboPPPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 1),
    _BiboPPPIfIndex_Type()
)
biboPPPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPIfIndex.setStatus("mandatory")


class _BiboPPPType_Type(Integer32):
    """Custom type biboPPPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("isdn-dialin-only", 3),
          ("isdn-dialup", 1),
          ("leased", 2),
          ("multiuser", 5))
    )


_BiboPPPType_Type.__name__ = "Integer32"
_BiboPPPType_Object = MibTableColumn
biboPPPType = _BiboPPPType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 2),
    _BiboPPPType_Type()
)
biboPPPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPType.setStatus("mandatory")


class _BiboPPPEncapsulation_Type(Integer32):
    """Custom type biboPPPEncapsulation based on Integer32"""
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
        *(("delete", 5),
          ("frame-relay", 9),
          ("ip-hdlc", 6),
          ("ip-lapb", 4),
          ("mpr-hdlc", 8),
          ("mpr-lapb", 7),
          ("ppp", 1),
          ("x25", 2),
          ("x25-noconfig", 16),
          ("x25-noconfig-nosig", 17),
          ("x25-nosig", 13),
          ("x25-pad", 15),
          ("x25-ppp", 3),
          ("x25-ppp-opt", 14),
          ("x31-bchan", 10),
          ("x75-ppp", 11),
          ("x75btx-ppp", 12))
    )


_BiboPPPEncapsulation_Type.__name__ = "Integer32"
_BiboPPPEncapsulation_Object = MibTableColumn
biboPPPEncapsulation = _BiboPPPEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 3),
    _BiboPPPEncapsulation_Type()
)
biboPPPEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPEncapsulation.setStatus("mandatory")


class _BiboPPPKeepalive_Type(Integer32):
    """Custom type biboPPPKeepalive based on Integer32"""
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


_BiboPPPKeepalive_Type.__name__ = "Integer32"
_BiboPPPKeepalive_Object = MibTableColumn
biboPPPKeepalive = _BiboPPPKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 4),
    _BiboPPPKeepalive_Type()
)
biboPPPKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPKeepalive.setStatus("mandatory")


class _BiboPPPTimeout_Type(Integer32):
    """Custom type biboPPPTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_BiboPPPTimeout_Type.__name__ = "Integer32"
_BiboPPPTimeout_Object = MibTableColumn
biboPPPTimeout = _BiboPPPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 5),
    _BiboPPPTimeout_Type()
)
biboPPPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPTimeout.setStatus("mandatory")


class _BiboPPPCompression_Type(Integer32):
    """Custom type biboPPPCompression based on Integer32"""
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
        *(("mppc", 5),
          ("ms-stac", 4),
          ("none", 1),
          ("stac", 3),
          ("v42bis", 2))
    )


_BiboPPPCompression_Type.__name__ = "Integer32"
_BiboPPPCompression_Object = MibTableColumn
biboPPPCompression = _BiboPPPCompression_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 6),
    _BiboPPPCompression_Type()
)
biboPPPCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPCompression.setStatus("mandatory")


class _BiboPPPAuthentication_Type(Integer32):
    """Custom type biboPPPAuthentication based on Integer32"""
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
        *(("all", 7),
          ("both", 4),
          ("chap", 3),
          ("ms-chap", 6),
          ("ms-chapv2", 8),
          ("none", 1),
          ("pap", 2),
          ("radius", 5))
    )


_BiboPPPAuthentication_Type.__name__ = "Integer32"
_BiboPPPAuthentication_Object = MibTableColumn
biboPPPAuthentication = _BiboPPPAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 7),
    _BiboPPPAuthentication_Type()
)
biboPPPAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPAuthentication.setStatus("mandatory")


class _BiboPPPAuthIdent_Type(DisplayString):
    """Custom type biboPPPAuthIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BiboPPPAuthIdent_Type.__name__ = "DisplayString"
_BiboPPPAuthIdent_Object = MibTableColumn
biboPPPAuthIdent = _BiboPPPAuthIdent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 8),
    _BiboPPPAuthIdent_Type()
)
biboPPPAuthIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPAuthIdent.setStatus("mandatory")


class _BiboPPPAuthSecret_Type(DisplayString):
    """Custom type biboPPPAuthSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BiboPPPAuthSecret_Type.__name__ = "DisplayString"
_BiboPPPAuthSecret_Object = MibTableColumn
biboPPPAuthSecret = _BiboPPPAuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 9),
    _BiboPPPAuthSecret_Type()
)
biboPPPAuthSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPAuthSecret.setStatus("mandatory")


class _BiboPPPIpAddress_Type(Integer32):
    """Custom type biboPPPIpAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic-client", 3),
          ("dynamic-server", 2),
          ("static", 1))
    )


_BiboPPPIpAddress_Type.__name__ = "Integer32"
_BiboPPPIpAddress_Object = MibTableColumn
biboPPPIpAddress = _BiboPPPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 10),
    _BiboPPPIpAddress_Type()
)
biboPPPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPIpAddress.setStatus("mandatory")


class _BiboPPPRetryTime_Type(Integer32):
    """Custom type biboPPPRetryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_BiboPPPRetryTime_Type.__name__ = "Integer32"
_BiboPPPRetryTime_Object = MibTableColumn
biboPPPRetryTime = _BiboPPPRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 11),
    _BiboPPPRetryTime_Type()
)
biboPPPRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPRetryTime.setStatus("mandatory")
_BiboPPPBlockTime_Type = Integer32
_BiboPPPBlockTime_Object = MibTableColumn
biboPPPBlockTime = _BiboPPPBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 12),
    _BiboPPPBlockTime_Type()
)
biboPPPBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPBlockTime.setStatus("mandatory")


class _BiboPPPMaxRetries_Type(Integer32):
    """Custom type biboPPPMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BiboPPPMaxRetries_Type.__name__ = "Integer32"
_BiboPPPMaxRetries_Object = MibTableColumn
biboPPPMaxRetries = _BiboPPPMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 13),
    _BiboPPPMaxRetries_Type()
)
biboPPPMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPMaxRetries.setStatus("mandatory")


class _BiboPPPShortHold_Type(Integer32):
    """Custom type biboPPPShortHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3600),
    )


_BiboPPPShortHold_Type.__name__ = "Integer32"
_BiboPPPShortHold_Object = MibTableColumn
biboPPPShortHold = _BiboPPPShortHold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 14),
    _BiboPPPShortHold_Type()
)
biboPPPShortHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPShortHold.setStatus("mandatory")


class _BiboPPPInitConn_Type(Integer32):
    """Custom type biboPPPInitConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_BiboPPPInitConn_Type.__name__ = "Integer32"
_BiboPPPInitConn_Object = MibTableColumn
biboPPPInitConn = _BiboPPPInitConn_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 15),
    _BiboPPPInitConn_Type()
)
biboPPPInitConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPInitConn.setStatus("mandatory")


class _BiboPPPMaxConn_Type(Integer32):
    """Custom type biboPPPMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_BiboPPPMaxConn_Type.__name__ = "Integer32"
_BiboPPPMaxConn_Object = MibTableColumn
biboPPPMaxConn = _BiboPPPMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 16),
    _BiboPPPMaxConn_Type()
)
biboPPPMaxConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPMaxConn.setStatus("mandatory")


class _BiboPPPMinConn_Type(Integer32):
    """Custom type biboPPPMinConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_BiboPPPMinConn_Type.__name__ = "Integer32"
_BiboPPPMinConn_Object = MibTableColumn
biboPPPMinConn = _BiboPPPMinConn_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 17),
    _BiboPPPMinConn_Type()
)
biboPPPMinConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPMinConn.setStatus("mandatory")


class _BiboPPPCallback_Type(Integer32):
    """Custom type biboPPPCallback based on Integer32"""
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
        *(("delayed", 5),
          ("disabled", 2),
          ("enabled", 1),
          ("expected", 3),
          ("ppp-callback-optional", 6),
          ("ppp-offered", 4))
    )


_BiboPPPCallback_Type.__name__ = "Integer32"
_BiboPPPCallback_Object = MibTableColumn
biboPPPCallback = _BiboPPPCallback_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 18),
    _BiboPPPCallback_Type()
)
biboPPPCallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPCallback.setStatus("mandatory")


class _BiboPPPLayer1Protocol_Type(Integer32):
    """Custom type biboPPPLayer1Protocol based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("aodi", 22),
          ("data-56k", 2),
          ("data-64k", 1),
          ("dovb", 4),
          ("modem", 3),
          ("modem-profile-1", 12),
          ("modem-profile-2", 13),
          ("modem-profile-3", 14),
          ("modem-profile-4", 15),
          ("modem-profile-5", 16),
          ("modem-profile-6", 17),
          ("modem-profile-7", 18),
          ("modem-profile-8", 19),
          ("pppoe", 21),
          ("pptp-pac", 23),
          ("pptp-pns", 20),
          ("v110-1200", 5),
          ("v110-14400", 9),
          ("v110-19200", 10),
          ("v110-2400", 6),
          ("v110-38400", 11),
          ("v110-4800", 7),
          ("v110-9600", 8))
    )


_BiboPPPLayer1Protocol_Type.__name__ = "Integer32"
_BiboPPPLayer1Protocol_Object = MibTableColumn
biboPPPLayer1Protocol = _BiboPPPLayer1Protocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 19),
    _BiboPPPLayer1Protocol_Type()
)
biboPPPLayer1Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPLayer1Protocol.setStatus("mandatory")


class _BiboPPPLoginString_Type(DisplayString):
    """Custom type biboPPPLoginString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BiboPPPLoginString_Type.__name__ = "DisplayString"
_BiboPPPLoginString_Object = MibTableColumn
biboPPPLoginString = _BiboPPPLoginString_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 20),
    _BiboPPPLoginString_Type()
)
biboPPPLoginString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPLoginString.setStatus("mandatory")


class _BiboPPPVJHeaderComp_Type(Integer32):
    """Custom type biboPPPVJHeaderComp based on Integer32"""
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


_BiboPPPVJHeaderComp_Type.__name__ = "Integer32"
_BiboPPPVJHeaderComp_Object = MibTableColumn
biboPPPVJHeaderComp = _BiboPPPVJHeaderComp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 21),
    _BiboPPPVJHeaderComp_Type()
)
biboPPPVJHeaderComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPVJHeaderComp.setStatus("mandatory")


class _BiboPPPLayer2Mode_Type(Integer32):
    """Custom type biboPPPLayer2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("dce", 3),
          ("dte", 2))
    )


_BiboPPPLayer2Mode_Type.__name__ = "Integer32"
_BiboPPPLayer2Mode_Object = MibTableColumn
biboPPPLayer2Mode = _BiboPPPLayer2Mode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 22),
    _BiboPPPLayer2Mode_Type()
)
biboPPPLayer2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPLayer2Mode.setStatus("mandatory")


class _BiboPPPDynShortHold_Type(Integer32):
    """Custom type biboPPPDynShortHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BiboPPPDynShortHold_Type.__name__ = "Integer32"
_BiboPPPDynShortHold_Object = MibTableColumn
biboPPPDynShortHold = _BiboPPPDynShortHold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 23),
    _BiboPPPDynShortHold_Type()
)
biboPPPDynShortHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPDynShortHold.setStatus("mandatory")


class _BiboPPPLocalIdent_Type(DisplayString):
    """Custom type biboPPPLocalIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BiboPPPLocalIdent_Type.__name__ = "DisplayString"
_BiboPPPLocalIdent_Object = MibTableColumn
biboPPPLocalIdent = _BiboPPPLocalIdent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 24),
    _BiboPPPLocalIdent_Type()
)
biboPPPLocalIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPLocalIdent.setStatus("mandatory")


class _BiboPPPDNSNegotiation_Type(Integer32):
    """Custom type biboPPPDNSNegotiation based on Integer32"""
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
        *(("disabled", 1),
          ("dynamic-client", 3),
          ("dynamic-server", 4),
          ("enabled", 2))
    )


_BiboPPPDNSNegotiation_Type.__name__ = "Integer32"
_BiboPPPDNSNegotiation_Object = MibTableColumn
biboPPPDNSNegotiation = _BiboPPPDNSNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 25),
    _BiboPPPDNSNegotiation_Type()
)
biboPPPDNSNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPDNSNegotiation.setStatus("mandatory")


class _BiboPPPEncryption_Type(Integer32):
    """Custom type biboPPPEncryption based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("blowfish-168", 6),
          ("blowfish-56", 11),
          ("des-56", 4),
          ("mppe-128", 3),
          ("mppe-40", 2),
          ("mppe-56", 7),
          ("mppev2-128", 10),
          ("mppev2-40", 8),
          ("mppev2-56", 9),
          ("none", 1),
          ("triple-des-168", 5))
    )


_BiboPPPEncryption_Type.__name__ = "Integer32"
_BiboPPPEncryption_Object = MibTableColumn
biboPPPEncryption = _BiboPPPEncryption_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 26),
    _BiboPPPEncryption_Type()
)
biboPPPEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPEncryption.setStatus("mandatory")


class _BiboPPPLQMonitoring_Type(Integer32):
    """Custom type biboPPPLQMonitoring based on Integer32"""
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


_BiboPPPLQMonitoring_Type.__name__ = "Integer32"
_BiboPPPLQMonitoring_Object = MibTableColumn
biboPPPLQMonitoring = _BiboPPPLQMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 27),
    _BiboPPPLQMonitoring_Type()
)
biboPPPLQMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPLQMonitoring.setStatus("mandatory")
_BiboPPPIpPoolId_Type = Integer32
_BiboPPPIpPoolId_Object = MibTableColumn
biboPPPIpPoolId = _BiboPPPIpPoolId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 28),
    _BiboPPPIpPoolId_Type()
)
biboPPPIpPoolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPIpPoolId.setStatus("mandatory")
_BiboPPPSessionTimeout_Type = Integer32
_BiboPPPSessionTimeout_Object = MibTableColumn
biboPPPSessionTimeout = _BiboPPPSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 1, 1, 29),
    _BiboPPPSessionTimeout_Type()
)
biboPPPSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPSessionTimeout.setStatus("mandatory")
_BiboPPPStatTable_Object = MibTable
biboPPPStatTable = _BiboPPPStatTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2)
)
if mibBuilder.loadTexts:
    biboPPPStatTable.setStatus("mandatory")
_BiboPPPStatEntry_Object = MibTableRow
biboPPPStatEntry = _BiboPPPStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1)
)
biboPPPStatEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPP-MIB", "biboPPPConnIfIndex"),
)
if mibBuilder.loadTexts:
    biboPPPStatEntry.setStatus("mandatory")
_BiboPPPConnIfIndex_Type = Integer32
_BiboPPPConnIfIndex_Object = MibTableColumn
biboPPPConnIfIndex = _BiboPPPConnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 1),
    _BiboPPPConnIfIndex_Type()
)
biboPPPConnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPConnIfIndex.setStatus("mandatory")


class _BiboPPPConnActive_Type(Integer32):
    """Custom type biboPPPConnActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_BiboPPPConnActive_Type.__name__ = "Integer32"
_BiboPPPConnActive_Object = MibTableColumn
biboPPPConnActive = _BiboPPPConnActive_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 2),
    _BiboPPPConnActive_Type()
)
biboPPPConnActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPConnActive.setStatus("mandatory")
_BiboPPPConnProtocols_Type = Integer32
_BiboPPPConnProtocols_Object = MibTableColumn
biboPPPConnProtocols = _BiboPPPConnProtocols_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 3),
    _BiboPPPConnProtocols_Type()
)
biboPPPConnProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPConnProtocols.setStatus("mandatory")


class _BiboPPPConnState_Type(Integer32):
    """Custom type biboPPPConnState based on Integer32"""
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
        *(("connected", 4),
          ("dataxfer", 5),
          ("disconnect", 6),
          ("idle", 1),
          ("incoming", 2),
          ("outgoing", 3))
    )


_BiboPPPConnState_Type.__name__ = "Integer32"
_BiboPPPConnState_Object = MibTableColumn
biboPPPConnState = _BiboPPPConnState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 4),
    _BiboPPPConnState_Type()
)
biboPPPConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPConnState.setStatus("mandatory")
_BiboPPPConnDuration_Type = Integer32
_BiboPPPConnDuration_Object = MibTableColumn
biboPPPConnDuration = _BiboPPPConnDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 5),
    _BiboPPPConnDuration_Type()
)
biboPPPConnDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPConnDuration.setStatus("mandatory")
_BiboPPPConnUnits_Type = Counter32
_BiboPPPConnUnits_Object = MibTableColumn
biboPPPConnUnits = _BiboPPPConnUnits_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 6),
    _BiboPPPConnUnits_Type()
)
biboPPPConnUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPConnUnits.setStatus("mandatory")
_BiboPPPConnTransmitOctets_Type = Counter32
_BiboPPPConnTransmitOctets_Object = MibTableColumn
biboPPPConnTransmitOctets = _BiboPPPConnTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 7),
    _BiboPPPConnTransmitOctets_Type()
)
biboPPPConnTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPConnTransmitOctets.setStatus("mandatory")
_BiboPPPConnReceivedOctets_Type = Counter32
_BiboPPPConnReceivedOctets_Object = MibTableColumn
biboPPPConnReceivedOctets = _BiboPPPConnReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 8),
    _BiboPPPConnReceivedOctets_Type()
)
biboPPPConnReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPConnReceivedOctets.setStatus("mandatory")
_BiboPPPConnOutgoingCalls_Type = Counter32
_BiboPPPConnOutgoingCalls_Object = MibTableColumn
biboPPPConnOutgoingCalls = _BiboPPPConnOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 9),
    _BiboPPPConnOutgoingCalls_Type()
)
biboPPPConnOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPConnOutgoingCalls.setStatus("mandatory")
_BiboPPPConnOutgoingFails_Type = Counter32
_BiboPPPConnOutgoingFails_Object = MibTableColumn
biboPPPConnOutgoingFails = _BiboPPPConnOutgoingFails_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 10),
    _BiboPPPConnOutgoingFails_Type()
)
biboPPPConnOutgoingFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPConnOutgoingFails.setStatus("mandatory")
_BiboPPPConnIncomingCalls_Type = Counter32
_BiboPPPConnIncomingCalls_Object = MibTableColumn
biboPPPConnIncomingCalls = _BiboPPPConnIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 11),
    _BiboPPPConnIncomingCalls_Type()
)
biboPPPConnIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPConnIncomingCalls.setStatus("mandatory")
_BiboPPPConnIncomingFails_Type = Counter32
_BiboPPPConnIncomingFails_Object = MibTableColumn
biboPPPConnIncomingFails = _BiboPPPConnIncomingFails_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 12),
    _BiboPPPConnIncomingFails_Type()
)
biboPPPConnIncomingFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPConnIncomingFails.setStatus("mandatory")
_BiboPPPTotalDuration_Type = Integer32
_BiboPPPTotalDuration_Object = MibTableColumn
biboPPPTotalDuration = _BiboPPPTotalDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 13),
    _BiboPPPTotalDuration_Type()
)
biboPPPTotalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPTotalDuration.setStatus("mandatory")
_BiboPPPTotalUnits_Type = Counter32
_BiboPPPTotalUnits_Object = MibTableColumn
biboPPPTotalUnits = _BiboPPPTotalUnits_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 14),
    _BiboPPPTotalUnits_Type()
)
biboPPPTotalUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPTotalUnits.setStatus("mandatory")
_BiboPPPTotalTransmitOctets_Type = Counter32
_BiboPPPTotalTransmitOctets_Object = MibTableColumn
biboPPPTotalTransmitOctets = _BiboPPPTotalTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 15),
    _BiboPPPTotalTransmitOctets_Type()
)
biboPPPTotalTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPTotalTransmitOctets.setStatus("mandatory")
_BiboPPPTotalReceivedOctets_Type = Counter32
_BiboPPPTotalReceivedOctets_Object = MibTableColumn
biboPPPTotalReceivedOctets = _BiboPPPTotalReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 16),
    _BiboPPPTotalReceivedOctets_Type()
)
biboPPPTotalReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPTotalReceivedOctets.setStatus("mandatory")
_BiboPPPTotalOutgoingCalls_Type = Counter32
_BiboPPPTotalOutgoingCalls_Object = MibTableColumn
biboPPPTotalOutgoingCalls = _BiboPPPTotalOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 17),
    _BiboPPPTotalOutgoingCalls_Type()
)
biboPPPTotalOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPTotalOutgoingCalls.setStatus("mandatory")
_BiboPPPTotalOutgoingFails_Type = Counter32
_BiboPPPTotalOutgoingFails_Object = MibTableColumn
biboPPPTotalOutgoingFails = _BiboPPPTotalOutgoingFails_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 18),
    _BiboPPPTotalOutgoingFails_Type()
)
biboPPPTotalOutgoingFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPTotalOutgoingFails.setStatus("mandatory")
_BiboPPPTotalIncomingCalls_Type = Counter32
_BiboPPPTotalIncomingCalls_Object = MibTableColumn
biboPPPTotalIncomingCalls = _BiboPPPTotalIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 19),
    _BiboPPPTotalIncomingCalls_Type()
)
biboPPPTotalIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPTotalIncomingCalls.setStatus("mandatory")
_BiboPPPTotalIncomingFails_Type = Counter32
_BiboPPPTotalIncomingFails_Object = MibTableColumn
biboPPPTotalIncomingFails = _BiboPPPTotalIncomingFails_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 20),
    _BiboPPPTotalIncomingFails_Type()
)
biboPPPTotalIncomingFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPTotalIncomingFails.setStatus("mandatory")
_BiboPPPThroughput_Type = Counter32
_BiboPPPThroughput_Object = MibTableColumn
biboPPPThroughput = _BiboPPPThroughput_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 21),
    _BiboPPPThroughput_Type()
)
biboPPPThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPThroughput.setStatus("mandatory")


class _BiboPPPCompressionMode_Type(Integer32):
    """Custom type biboPPPCompressionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_BiboPPPCompressionMode_Type.__name__ = "Integer32"
_BiboPPPCompressionMode_Object = MibTableColumn
biboPPPCompressionMode = _BiboPPPCompressionMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 22),
    _BiboPPPCompressionMode_Type()
)
biboPPPCompressionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPCompressionMode.setStatus("mandatory")


class _BiboPPPChargeInterval_Type(Integer32):
    """Custom type biboPPPChargeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_BiboPPPChargeInterval_Type.__name__ = "Integer32"
_BiboPPPChargeInterval_Object = MibTableColumn
biboPPPChargeInterval = _BiboPPPChargeInterval_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 23),
    _BiboPPPChargeInterval_Type()
)
biboPPPChargeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPChargeInterval.setStatus("mandatory")


class _BiboPPPIdleTime_Type(Integer32):
    """Custom type biboPPPIdleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_BiboPPPIdleTime_Type.__name__ = "Integer32"
_BiboPPPIdleTime_Object = MibTableColumn
biboPPPIdleTime = _BiboPPPIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 24),
    _BiboPPPIdleTime_Type()
)
biboPPPIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPIdleTime.setStatus("mandatory")
_BiboPPPConnCharge_Type = Counter32
_BiboPPPConnCharge_Object = MibTableColumn
biboPPPConnCharge = _BiboPPPConnCharge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 25),
    _BiboPPPConnCharge_Type()
)
biboPPPConnCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPConnCharge.setStatus("mandatory")
_BiboPPPTotalCharge_Type = Counter32
_BiboPPPTotalCharge_Object = MibTableColumn
biboPPPTotalCharge = _BiboPPPTotalCharge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 2, 1, 26),
    _BiboPPPTotalCharge_Type()
)
biboPPPTotalCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPTotalCharge.setStatus("mandatory")
_BiboPPPLinkTable_Object = MibTable
biboPPPLinkTable = _BiboPPPLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3)
)
if mibBuilder.loadTexts:
    biboPPPLinkTable.setStatus("mandatory")
_BiboPPPLinkEntry_Object = MibTableRow
biboPPPLinkEntry = _BiboPPPLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1)
)
biboPPPLinkEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPP-MIB", "biboPPPLinkIfIndex"),
)
if mibBuilder.loadTexts:
    biboPPPLinkEntry.setStatus("mandatory")
_BiboPPPLinkIfIndex_Type = Integer32
_BiboPPPLinkIfIndex_Object = MibTableColumn
biboPPPLinkIfIndex = _BiboPPPLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 1),
    _BiboPPPLinkIfIndex_Type()
)
biboPPPLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkIfIndex.setStatus("mandatory")
_BiboPPPLinkEstablished_Type = Date
_BiboPPPLinkEstablished_Object = MibTableColumn
biboPPPLinkEstablished = _BiboPPPLinkEstablished_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 2),
    _BiboPPPLinkEstablished_Type()
)
biboPPPLinkEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkEstablished.setStatus("mandatory")


class _BiboPPPLinkDirection_Type(Integer32):
    """Custom type biboPPPLinkDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming-dce", 1),
          ("outgoing-dte", 2))
    )


_BiboPPPLinkDirection_Type.__name__ = "Integer32"
_BiboPPPLinkDirection_Object = MibTableColumn
biboPPPLinkDirection = _BiboPPPLinkDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 3),
    _BiboPPPLinkDirection_Type()
)
biboPPPLinkDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkDirection.setStatus("mandatory")
_BiboPPPLinkProtocols_Type = Integer32
_BiboPPPLinkProtocols_Object = MibTableColumn
biboPPPLinkProtocols = _BiboPPPLinkProtocols_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 4),
    _BiboPPPLinkProtocols_Type()
)
biboPPPLinkProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkProtocols.setStatus("mandatory")


class _BiboPPPLinkState_Type(Integer32):
    """Custom type biboPPPLinkState based on Integer32"""
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
        *(("dialing", 5),
          ("down", 2),
          ("loopbacked", 4),
          ("retry-wait", 6),
          ("starting", 3),
          ("up", 1))
    )


_BiboPPPLinkState_Type.__name__ = "Integer32"
_BiboPPPLinkState_Object = MibTableColumn
biboPPPLinkState = _BiboPPPLinkState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 5),
    _BiboPPPLinkState_Type()
)
biboPPPLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkState.setStatus("mandatory")
_BiboPPPLinkUnits_Type = Counter32
_BiboPPPLinkUnits_Object = MibTableColumn
biboPPPLinkUnits = _BiboPPPLinkUnits_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 6),
    _BiboPPPLinkUnits_Type()
)
biboPPPLinkUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkUnits.setStatus("mandatory")
_BiboPPPLinkRetries_Type = Counter32
_BiboPPPLinkRetries_Object = MibTableColumn
biboPPPLinkRetries = _BiboPPPLinkRetries_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 7),
    _BiboPPPLinkRetries_Type()
)
biboPPPLinkRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkRetries.setStatus("mandatory")
_BiboPPPLinkKeepaliveSent_Type = Counter32
_BiboPPPLinkKeepaliveSent_Object = MibTableColumn
biboPPPLinkKeepaliveSent = _BiboPPPLinkKeepaliveSent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 8),
    _BiboPPPLinkKeepaliveSent_Type()
)
biboPPPLinkKeepaliveSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkKeepaliveSent.setStatus("mandatory")
_BiboPPPLinkKeepalivePending_Type = Counter32
_BiboPPPLinkKeepalivePending_Object = MibTableColumn
biboPPPLinkKeepalivePending = _BiboPPPLinkKeepalivePending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 9),
    _BiboPPPLinkKeepalivePending_Type()
)
biboPPPLinkKeepalivePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkKeepalivePending.setStatus("mandatory")
_BiboPPPLinkDeviceIndex_Type = Integer32
_BiboPPPLinkDeviceIndex_Object = MibTableColumn
biboPPPLinkDeviceIndex = _BiboPPPLinkDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 10),
    _BiboPPPLinkDeviceIndex_Type()
)
biboPPPLinkDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkDeviceIndex.setStatus("mandatory")
_BiboPPPLinkSpeed_Type = Integer32
_BiboPPPLinkSpeed_Object = MibTableColumn
biboPPPLinkSpeed = _BiboPPPLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 11),
    _BiboPPPLinkSpeed_Type()
)
biboPPPLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkSpeed.setStatus("mandatory")


class _BiboPPPLinkStkNumber_Type(Integer32):
    """Custom type biboPPPLinkStkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_BiboPPPLinkStkNumber_Type.__name__ = "Integer32"
_BiboPPPLinkStkNumber_Object = MibTableColumn
biboPPPLinkStkNumber = _BiboPPPLinkStkNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 13),
    _BiboPPPLinkStkNumber_Type()
)
biboPPPLinkStkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkStkNumber.setStatus("mandatory")


class _BiboPPPLinkCallType_Type(Integer32):
    """Custom type biboPPPLinkCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2),
          ("undef", 3))
    )


_BiboPPPLinkCallType_Type.__name__ = "Integer32"
_BiboPPPLinkCallType_Object = MibScalar
biboPPPLinkCallType = _BiboPPPLinkCallType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 14),
    _BiboPPPLinkCallType_Type()
)
biboPPPLinkCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkCallType.setStatus("mandatory")
_BiboPPPLinkCallReference_Type = Integer32
_BiboPPPLinkCallReference_Object = MibTableColumn
biboPPPLinkCallReference = _BiboPPPLinkCallReference_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 15),
    _BiboPPPLinkCallReference_Type()
)
biboPPPLinkCallReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkCallReference.setStatus("mandatory")
_BiboPPPLinkCharge_Type = Counter32
_BiboPPPLinkCharge_Object = MibTableColumn
biboPPPLinkCharge = _BiboPPPLinkCharge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 16),
    _BiboPPPLinkCharge_Type()
)
biboPPPLinkCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkCharge.setStatus("mandatory")


class _BiboPPPLinkAccm_Type(OctetString):
    """Custom type biboPPPLinkAccm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BiboPPPLinkAccm_Type.__name__ = "OctetString"
_BiboPPPLinkAccm_Object = MibTableColumn
biboPPPLinkAccm = _BiboPPPLinkAccm_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 17),
    _BiboPPPLinkAccm_Type()
)
biboPPPLinkAccm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkAccm.setStatus("mandatory")


class _BiboPPPLinkLqm_Type(Integer32):
    """Custom type biboPPPLinkLqm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negotiated", 2),
          ("none", 1))
    )


_BiboPPPLinkLqm_Type.__name__ = "Integer32"
_BiboPPPLinkLqm_Object = MibTableColumn
biboPPPLinkLqm = _BiboPPPLinkLqm_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 18),
    _BiboPPPLinkLqm_Type()
)
biboPPPLinkLqm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkLqm.setStatus("mandatory")


class _BiboPPPLinkLcpComp_Type(Integer32):
    """Custom type biboPPPLinkLcpComp based on Integer32"""
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
        *(("addr", 2),
          ("both", 4),
          ("none", 1),
          ("prot", 3))
    )


_BiboPPPLinkLcpComp_Type.__name__ = "Integer32"
_BiboPPPLinkLcpComp_Object = MibTableColumn
biboPPPLinkLcpComp = _BiboPPPLinkLcpComp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 19),
    _BiboPPPLinkLcpComp_Type()
)
biboPPPLinkLcpComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkLcpComp.setStatus("mandatory")


class _BiboPPPLinkLocDiscr_Type(OctetString):
    """Custom type biboPPPLinkLocDiscr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_BiboPPPLinkLocDiscr_Type.__name__ = "OctetString"
_BiboPPPLinkLocDiscr_Object = MibTableColumn
biboPPPLinkLocDiscr = _BiboPPPLinkLocDiscr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 20),
    _BiboPPPLinkLocDiscr_Type()
)
biboPPPLinkLocDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkLocDiscr.setStatus("mandatory")


class _BiboPPPLinkRemDiscr_Type(OctetString):
    """Custom type biboPPPLinkRemDiscr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_BiboPPPLinkRemDiscr_Type.__name__ = "OctetString"
_BiboPPPLinkRemDiscr_Object = MibTableColumn
biboPPPLinkRemDiscr = _BiboPPPLinkRemDiscr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 3, 1, 21),
    _BiboPPPLinkRemDiscr_Type()
)
biboPPPLinkRemDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPLinkRemDiscr.setStatus("mandatory")
_BiboPPPIpAssignTable_Object = MibTable
biboPPPIpAssignTable = _BiboPPPIpAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 4)
)
if mibBuilder.loadTexts:
    biboPPPIpAssignTable.setStatus("mandatory")
_BiboPPPIpAssignEntry_Object = MibTableRow
biboPPPIpAssignEntry = _BiboPPPIpAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 4, 1)
)
biboPPPIpAssignEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPP-MIB", "biboPPPIpAssignAddress"),
)
if mibBuilder.loadTexts:
    biboPPPIpAssignEntry.setStatus("mandatory")
_BiboPPPIpAssignAddress_Type = IpAddress
_BiboPPPIpAssignAddress_Object = MibTableColumn
biboPPPIpAssignAddress = _BiboPPPIpAssignAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 4, 1, 1),
    _BiboPPPIpAssignAddress_Type()
)
biboPPPIpAssignAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPIpAssignAddress.setStatus("mandatory")


class _BiboPPPIpAssignState_Type(Integer32):
    """Custom type biboPPPIpAssignState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 2),
          ("delete", 3),
          ("unused", 1))
    )


_BiboPPPIpAssignState_Type.__name__ = "Integer32"
_BiboPPPIpAssignState_Object = MibTableColumn
biboPPPIpAssignState = _BiboPPPIpAssignState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 4, 1, 2),
    _BiboPPPIpAssignState_Type()
)
biboPPPIpAssignState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPIpAssignState.setStatus("mandatory")
_BiboPPPIpAssignPoolId_Type = Integer32
_BiboPPPIpAssignPoolId_Object = MibTableColumn
biboPPPIpAssignPoolId = _BiboPPPIpAssignPoolId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 4, 1, 3),
    _BiboPPPIpAssignPoolId_Type()
)
biboPPPIpAssignPoolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPIpAssignPoolId.setStatus("mandatory")
_BiboPPPIpAssignRange_Type = Integer32
_BiboPPPIpAssignRange_Object = MibTableColumn
biboPPPIpAssignRange = _BiboPPPIpAssignRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 4, 1, 4),
    _BiboPPPIpAssignRange_Type()
)
biboPPPIpAssignRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPIpAssignRange.setStatus("mandatory")
_BiboPPPProfileTable_Object = MibTable
biboPPPProfileTable = _BiboPPPProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 5)
)
if mibBuilder.loadTexts:
    biboPPPProfileTable.setStatus("mandatory")
_BiboPPPProfileEntry_Object = MibTableRow
biboPPPProfileEntry = _BiboPPPProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 5, 1)
)
biboPPPProfileEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPP-MIB", "biboPPPProfileName"),
)
if mibBuilder.loadTexts:
    biboPPPProfileEntry.setStatus("mandatory")


class _BiboPPPProfileName_Type(Integer32):
    """Custom type biboPPPProfileName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("profile-1", 1),
          ("profile-2", 2),
          ("profile-3", 3))
    )


_BiboPPPProfileName_Type.__name__ = "Integer32"
_BiboPPPProfileName_Object = MibTableColumn
biboPPPProfileName = _BiboPPPProfileName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 5, 1, 1),
    _BiboPPPProfileName_Type()
)
biboPPPProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPPPProfileName.setStatus("mandatory")


class _BiboPPPProfileAuthProtocol_Type(Integer32):
    """Custom type biboPPPProfileAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("all", 7),
          ("both", 4),
          ("chap", 3),
          ("ms-chap", 6),
          ("ms-chapv2", 8),
          ("none", 1),
          ("pap", 2))
    )


_BiboPPPProfileAuthProtocol_Type.__name__ = "Integer32"
_BiboPPPProfileAuthProtocol_Object = MibTableColumn
biboPPPProfileAuthProtocol = _BiboPPPProfileAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 5, 1, 2),
    _BiboPPPProfileAuthProtocol_Type()
)
biboPPPProfileAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPProfileAuthProtocol.setStatus("mandatory")


class _BiboPPPProfileAuthRadius_Type(Integer32):
    """Custom type biboPPPProfileAuthRadius based on Integer32"""
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
        *(("both", 4),
          ("inband", 2),
          ("none", 1),
          ("outband", 3),
          ("radius-only", 5))
    )


_BiboPPPProfileAuthRadius_Type.__name__ = "Integer32"
_BiboPPPProfileAuthRadius_Object = MibTableColumn
biboPPPProfileAuthRadius = _BiboPPPProfileAuthRadius_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 5, 1, 3),
    _BiboPPPProfileAuthRadius_Type()
)
biboPPPProfileAuthRadius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPProfileAuthRadius.setStatus("mandatory")


class _BiboPPPProfileLQMonitoring_Type(Integer32):
    """Custom type biboPPPProfileLQMonitoring based on Integer32"""
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


_BiboPPPProfileLQMonitoring_Type.__name__ = "Integer32"
_BiboPPPProfileLQMonitoring_Object = MibTableColumn
biboPPPProfileLQMonitoring = _BiboPPPProfileLQMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 5, 1, 4),
    _BiboPPPProfileLQMonitoring_Type()
)
biboPPPProfileLQMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPProfileLQMonitoring.setStatus("mandatory")
_BiboPPPProfilePPPoEDevIfIndex_Type = Integer32
_BiboPPPProfilePPPoEDevIfIndex_Object = MibTableColumn
biboPPPProfilePPPoEDevIfIndex = _BiboPPPProfilePPPoEDevIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 5, 1, 5),
    _BiboPPPProfilePPPoEDevIfIndex_Type()
)
biboPPPProfilePPPoEDevIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPProfilePPPoEDevIfIndex.setStatus("mandatory")


class _BiboPPPProfileCallbackNegotiation_Type(Integer32):
    """Custom type biboPPPProfileCallbackNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbcp-optional", 3),
          ("disabled", 1),
          ("enabled", 2))
    )


_BiboPPPProfileCallbackNegotiation_Type.__name__ = "Integer32"
_BiboPPPProfileCallbackNegotiation_Object = MibTableColumn
biboPPPProfileCallbackNegotiation = _BiboPPPProfileCallbackNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 5, 1, 7),
    _BiboPPPProfileCallbackNegotiation_Type()
)
biboPPPProfileCallbackNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPPPProfileCallbackNegotiation.setStatus("mandatory")
_PppLqmTable_Object = MibTable
pppLqmTable = _PppLqmTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6)
)
if mibBuilder.loadTexts:
    pppLqmTable.setStatus("mandatory")
_PppLqmEntry_Object = MibTableRow
pppLqmEntry = _PppLqmEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1)
)
pppLqmEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPP-MIB", "pppLqmIfIndex"),
)
if mibBuilder.loadTexts:
    pppLqmEntry.setStatus("mandatory")
_PppLqmIfIndex_Type = Integer32
_PppLqmIfIndex_Object = MibTableColumn
pppLqmIfIndex = _PppLqmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 1),
    _PppLqmIfIndex_Type()
)
pppLqmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmIfIndex.setStatus("mandatory")
_PppLqmCallReference_Type = Integer32
_PppLqmCallReference_Object = MibTableColumn
pppLqmCallReference = _PppLqmCallReference_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 2),
    _PppLqmCallReference_Type()
)
pppLqmCallReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmCallReference.setStatus("mandatory")
_PppLqmReportingPeriod_Type = Integer32
_PppLqmReportingPeriod_Object = MibTableColumn
pppLqmReportingPeriod = _PppLqmReportingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 3),
    _PppLqmReportingPeriod_Type()
)
pppLqmReportingPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmReportingPeriod.setStatus("mandatory")
_PppLqmOutLQRs_Type = Counter32
_PppLqmOutLQRs_Object = MibTableColumn
pppLqmOutLQRs = _PppLqmOutLQRs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 4),
    _PppLqmOutLQRs_Type()
)
pppLqmOutLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmOutLQRs.setStatus("mandatory")
_PppLqmOutPackets_Type = Counter32
_PppLqmOutPackets_Object = MibTableColumn
pppLqmOutPackets = _PppLqmOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 5),
    _PppLqmOutPackets_Type()
)
pppLqmOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmOutPackets.setStatus("mandatory")
_PppLqmOutOctets_Type = Counter32
_PppLqmOutOctets_Object = MibTableColumn
pppLqmOutOctets = _PppLqmOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 6),
    _PppLqmOutOctets_Type()
)
pppLqmOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmOutOctets.setStatus("mandatory")
_PppLqmInLQRs_Type = Counter32
_PppLqmInLQRs_Object = MibTableColumn
pppLqmInLQRs = _PppLqmInLQRs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 7),
    _PppLqmInLQRs_Type()
)
pppLqmInLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmInLQRs.setStatus("mandatory")
_PppLqmInPackets_Type = Counter32
_PppLqmInPackets_Object = MibTableColumn
pppLqmInPackets = _PppLqmInPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 8),
    _PppLqmInPackets_Type()
)
pppLqmInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmInPackets.setStatus("mandatory")
_PppLqmInOctets_Type = Counter32
_PppLqmInOctets_Object = MibTableColumn
pppLqmInOctets = _PppLqmInOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 9),
    _PppLqmInOctets_Type()
)
pppLqmInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmInOctets.setStatus("mandatory")
_PppLqmInDiscards_Type = Counter32
_PppLqmInDiscards_Object = MibTableColumn
pppLqmInDiscards = _PppLqmInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 10),
    _PppLqmInDiscards_Type()
)
pppLqmInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmInDiscards.setStatus("mandatory")
_PppLqmInErrors_Type = Counter32
_PppLqmInErrors_Object = MibTableColumn
pppLqmInErrors = _PppLqmInErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 11),
    _PppLqmInErrors_Type()
)
pppLqmInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmInErrors.setStatus("mandatory")
_PppLqmPeerOutLQRs_Type = Counter32
_PppLqmPeerOutLQRs_Object = MibTableColumn
pppLqmPeerOutLQRs = _PppLqmPeerOutLQRs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 12),
    _PppLqmPeerOutLQRs_Type()
)
pppLqmPeerOutLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmPeerOutLQRs.setStatus("mandatory")
_PppLqmPeerOutPackets_Type = Counter32
_PppLqmPeerOutPackets_Object = MibTableColumn
pppLqmPeerOutPackets = _PppLqmPeerOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 13),
    _PppLqmPeerOutPackets_Type()
)
pppLqmPeerOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmPeerOutPackets.setStatus("mandatory")
_PppLqmPeerOutOctets_Type = Counter32
_PppLqmPeerOutOctets_Object = MibTableColumn
pppLqmPeerOutOctets = _PppLqmPeerOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 14),
    _PppLqmPeerOutOctets_Type()
)
pppLqmPeerOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmPeerOutOctets.setStatus("mandatory")
_PppLqmPeerInLQRs_Type = Counter32
_PppLqmPeerInLQRs_Object = MibTableColumn
pppLqmPeerInLQRs = _PppLqmPeerInLQRs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 15),
    _PppLqmPeerInLQRs_Type()
)
pppLqmPeerInLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmPeerInLQRs.setStatus("mandatory")
_PppLqmPeerInPackets_Type = Counter32
_PppLqmPeerInPackets_Object = MibTableColumn
pppLqmPeerInPackets = _PppLqmPeerInPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 16),
    _PppLqmPeerInPackets_Type()
)
pppLqmPeerInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmPeerInPackets.setStatus("mandatory")
_PppLqmPeerInOctets_Type = Counter32
_PppLqmPeerInOctets_Object = MibTableColumn
pppLqmPeerInOctets = _PppLqmPeerInOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 17),
    _PppLqmPeerInOctets_Type()
)
pppLqmPeerInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmPeerInOctets.setStatus("mandatory")
_PppLqmPeerInDiscards_Type = Counter32
_PppLqmPeerInDiscards_Object = MibTableColumn
pppLqmPeerInDiscards = _PppLqmPeerInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 18),
    _PppLqmPeerInDiscards_Type()
)
pppLqmPeerInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmPeerInDiscards.setStatus("mandatory")
_PppLqmPeerInErrors_Type = Counter32
_PppLqmPeerInErrors_Object = MibScalar
pppLqmPeerInErrors = _PppLqmPeerInErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 19),
    _PppLqmPeerInErrors_Type()
)
pppLqmPeerInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmPeerInErrors.setStatus("mandatory")
_PppLqmLostOutLQRs_Type = Counter32
_PppLqmLostOutLQRs_Object = MibTableColumn
pppLqmLostOutLQRs = _PppLqmLostOutLQRs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 20),
    _PppLqmLostOutLQRs_Type()
)
pppLqmLostOutLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmLostOutLQRs.setStatus("mandatory")
_PppLqmLostOutPackets_Type = Counter32
_PppLqmLostOutPackets_Object = MibTableColumn
pppLqmLostOutPackets = _PppLqmLostOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 21),
    _PppLqmLostOutPackets_Type()
)
pppLqmLostOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmLostOutPackets.setStatus("mandatory")
_PppLqmLostOutOctets_Type = Counter32
_PppLqmLostOutOctets_Object = MibTableColumn
pppLqmLostOutOctets = _PppLqmLostOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 22),
    _PppLqmLostOutOctets_Type()
)
pppLqmLostOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmLostOutOctets.setStatus("mandatory")
_PppLqmLostPeerOutLQRs_Type = Counter32
_PppLqmLostPeerOutLQRs_Object = MibTableColumn
pppLqmLostPeerOutLQRs = _PppLqmLostPeerOutLQRs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 23),
    _PppLqmLostPeerOutLQRs_Type()
)
pppLqmLostPeerOutLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmLostPeerOutLQRs.setStatus("mandatory")
_PppLqmLostPeerOutPkts_Type = Counter32
_PppLqmLostPeerOutPkts_Object = MibTableColumn
pppLqmLostPeerOutPkts = _PppLqmLostPeerOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 24),
    _PppLqmLostPeerOutPkts_Type()
)
pppLqmLostPeerOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmLostPeerOutPkts.setStatus("mandatory")
_PppLqmLostPeerOutOcts_Type = Counter32
_PppLqmLostPeerOutOcts_Object = MibTableColumn
pppLqmLostPeerOutOcts = _PppLqmLostPeerOutOcts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 6, 1, 25),
    _PppLqmLostPeerOutOcts_Type()
)
pppLqmLostPeerOutOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmLostPeerOutOcts.setStatus("mandatory")
_PppIpInUseTable_Object = MibTable
pppIpInUseTable = _PppIpInUseTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 7)
)
if mibBuilder.loadTexts:
    pppIpInUseTable.setStatus("mandatory")
_PppIpInUseEntry_Object = MibTableRow
pppIpInUseEntry = _PppIpInUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 7, 1)
)
pppIpInUseEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPP-MIB", "pppIpInUseAddress"),
)
if mibBuilder.loadTexts:
    pppIpInUseEntry.setStatus("mandatory")
_PppIpInUseAddress_Type = IpAddress
_PppIpInUseAddress_Object = MibScalar
pppIpInUseAddress = _PppIpInUseAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 7, 1, 1),
    _PppIpInUseAddress_Type()
)
pppIpInUseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpInUseAddress.setStatus("mandatory")
_PppIpInUsePoolId_Type = Integer32
_PppIpInUsePoolId_Object = MibScalar
pppIpInUsePoolId = _PppIpInUsePoolId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 7, 1, 2),
    _PppIpInUsePoolId_Type()
)
pppIpInUsePoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpInUsePoolId.setStatus("mandatory")
_PppIpInUseIfIndex_Type = Integer32
_PppIpInUseIfIndex_Object = MibScalar
pppIpInUseIfIndex = _PppIpInUseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 7, 1, 3),
    _PppIpInUseIfIndex_Type()
)
pppIpInUseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpInUseIfIndex.setStatus("mandatory")


class _PppIpInUseIdent_Type(DisplayString):
    """Custom type pppIpInUseIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PppIpInUseIdent_Type.__name__ = "DisplayString"
_PppIpInUseIdent_Object = MibScalar
pppIpInUseIdent = _PppIpInUseIdent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 7, 1, 4),
    _PppIpInUseIdent_Type()
)
pppIpInUseIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpInUseIdent.setStatus("mandatory")


class _PppIpInUseState_Type(Integer32):
    """Custom type pppIpInUseState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 1),
          ("reserved", 2))
    )


_PppIpInUseState_Type.__name__ = "Integer32"
_PppIpInUseState_Object = MibScalar
pppIpInUseState = _PppIpInUseState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 7, 1, 5),
    _PppIpInUseState_Type()
)
pppIpInUseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpInUseState.setStatus("mandatory")
_PppIpInUseAge_Type = Integer32
_PppIpInUseAge_Object = MibScalar
pppIpInUseAge = _PppIpInUseAge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 7, 1, 6),
    _PppIpInUseAge_Type()
)
pppIpInUseAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpInUseAge.setStatus("mandatory")
_PppExtIfTable_Object = MibTable
pppExtIfTable = _PppExtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9)
)
if mibBuilder.loadTexts:
    pppExtIfTable.setStatus("mandatory")
_PppExtIfEntry_Object = MibTableRow
pppExtIfEntry = _PppExtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1)
)
pppExtIfEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPP-MIB", "pppExtIfIndex"),
)
if mibBuilder.loadTexts:
    pppExtIfEntry.setStatus("mandatory")
_PppExtIfIndex_Type = Integer32
_PppExtIfIndex_Object = MibTableColumn
pppExtIfIndex = _PppExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 1),
    _PppExtIfIndex_Type()
)
pppExtIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfIndex.setStatus("mandatory")


class _PppExtIfBodMode_Type(Integer32):
    """Custom type pppExtIfBodMode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("bap-active", 5),
          ("bap-both", 8),
          ("bap-first", 9),
          ("bap-passive", 6),
          ("bod-active", 3),
          ("bod-passive", 4),
          ("delete", 7),
          ("disabled", 1))
    )


_PppExtIfBodMode_Type.__name__ = "Integer32"
_PppExtIfBodMode_Object = MibTableColumn
pppExtIfBodMode = _PppExtIfBodMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 2),
    _PppExtIfBodMode_Type()
)
pppExtIfBodMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfBodMode.setStatus("mandatory")


class _PppExtIfAlgorithm_Type(Integer32):
    """Custom type pppExtIfAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("proportional", 2))
    )


_PppExtIfAlgorithm_Type.__name__ = "Integer32"
_PppExtIfAlgorithm_Object = MibTableColumn
pppExtIfAlgorithm = _PppExtIfAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 3),
    _PppExtIfAlgorithm_Type()
)
pppExtIfAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfAlgorithm.setStatus("mandatory")


class _PppExtIfInterval_Type(Integer32):
    """Custom type pppExtIfInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_PppExtIfInterval_Type.__name__ = "Integer32"
_PppExtIfInterval_Object = MibTableColumn
pppExtIfInterval = _PppExtIfInterval_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 4),
    _PppExtIfInterval_Type()
)
pppExtIfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfInterval.setStatus("mandatory")


class _PppExtIfLoad_Type(Integer32):
    """Custom type pppExtIfLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PppExtIfLoad_Type.__name__ = "Integer32"
_PppExtIfLoad_Object = MibTableColumn
pppExtIfLoad = _PppExtIfLoad_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 5),
    _PppExtIfLoad_Type()
)
pppExtIfLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppExtIfLoad.setStatus("mandatory")


class _PppExtIfMlpFragmentation_Type(Integer32):
    """Custom type pppExtIfMlpFragmentation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("interleave", 3),
          ("proportional", 1))
    )


_PppExtIfMlpFragmentation_Type.__name__ = "Integer32"
_PppExtIfMlpFragmentation_Object = MibTableColumn
pppExtIfMlpFragmentation = _PppExtIfMlpFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 6),
    _PppExtIfMlpFragmentation_Type()
)
pppExtIfMlpFragmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfMlpFragmentation.setStatus("mandatory")


class _PppExtIfMlpFragSize_Type(Integer32):
    """Custom type pppExtIfMlpFragSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1500),
    )


_PppExtIfMlpFragSize_Type.__name__ = "Integer32"
_PppExtIfMlpFragSize_Object = MibTableColumn
pppExtIfMlpFragSize = _PppExtIfMlpFragSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 7),
    _PppExtIfMlpFragSize_Type()
)
pppExtIfMlpFragSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfMlpFragSize.setStatus("mandatory")


class _PppExtIfPPPoEService_Type(DisplayString):
    """Custom type pppExtIfPPPoEService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PppExtIfPPPoEService_Type.__name__ = "DisplayString"
_PppExtIfPPPoEService_Object = MibTableColumn
pppExtIfPPPoEService = _PppExtIfPPPoEService_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 8),
    _PppExtIfPPPoEService_Type()
)
pppExtIfPPPoEService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfPPPoEService.setStatus("mandatory")


class _PppExtIfPPPoEAcServer_Type(DisplayString):
    """Custom type pppExtIfPPPoEAcServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PppExtIfPPPoEAcServer_Type.__name__ = "DisplayString"
_PppExtIfPPPoEAcServer_Object = MibTableColumn
pppExtIfPPPoEAcServer = _PppExtIfPPPoEAcServer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 9),
    _PppExtIfPPPoEAcServer_Type()
)
pppExtIfPPPoEAcServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfPPPoEAcServer.setStatus("mandatory")


class _PppExtIfEncKeyNegotiation_Type(Integer32):
    """Custom type pppExtIfEncKeyNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authentication", 2),
          ("static", 1))
    )


_PppExtIfEncKeyNegotiation_Type.__name__ = "Integer32"
_PppExtIfEncKeyNegotiation_Object = MibTableColumn
pppExtIfEncKeyNegotiation = _PppExtIfEncKeyNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 10),
    _PppExtIfEncKeyNegotiation_Type()
)
pppExtIfEncKeyNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfEncKeyNegotiation.setStatus("mandatory")
_PppExtIfEncTxKey_Type = OctetString
_PppExtIfEncTxKey_Object = MibTableColumn
pppExtIfEncTxKey = _PppExtIfEncTxKey_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 11),
    _PppExtIfEncTxKey_Type()
)
pppExtIfEncTxKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfEncTxKey.setStatus("mandatory")
_PppExtIfEncRxKey_Type = OctetString
_PppExtIfEncRxKey_Object = MibTableColumn
pppExtIfEncRxKey = _PppExtIfEncRxKey_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 12),
    _PppExtIfEncRxKey_Type()
)
pppExtIfEncRxKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfEncRxKey.setStatus("mandatory")


class _PppExtIfGearUpThreshold_Type(Integer32):
    """Custom type pppExtIfGearUpThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PppExtIfGearUpThreshold_Type.__name__ = "Integer32"
_PppExtIfGearUpThreshold_Object = MibTableColumn
pppExtIfGearUpThreshold = _PppExtIfGearUpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 13),
    _PppExtIfGearUpThreshold_Type()
)
pppExtIfGearUpThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfGearUpThreshold.setStatus("mandatory")


class _PppExtIfGearDownThreshold_Type(Integer32):
    """Custom type pppExtIfGearDownThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PppExtIfGearDownThreshold_Type.__name__ = "Integer32"
_PppExtIfGearDownThreshold_Object = MibTableColumn
pppExtIfGearDownThreshold = _PppExtIfGearDownThreshold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 14),
    _PppExtIfGearDownThreshold_Type()
)
pppExtIfGearDownThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfGearDownThreshold.setStatus("mandatory")
_PppExtIfAodiDChanQlen_Type = Integer32
_PppExtIfAodiDChanQlen_Object = MibTableColumn
pppExtIfAodiDChanQlen = _PppExtIfAodiDChanQlen_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 15),
    _PppExtIfAodiDChanQlen_Type()
)
pppExtIfAodiDChanQlen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfAodiDChanQlen.setStatus("mandatory")
_PppExtIfAodiGearDownTxRate_Type = Integer32
_PppExtIfAodiGearDownTxRate_Object = MibTableColumn
pppExtIfAodiGearDownTxRate = _PppExtIfAodiGearDownTxRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 16),
    _PppExtIfAodiGearDownTxRate_Type()
)
pppExtIfAodiGearDownTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfAodiGearDownTxRate.setStatus("mandatory")


class _PppExtIfGearUpPersistance_Type(Integer32):
    """Custom type pppExtIfGearUpPersistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PppExtIfGearUpPersistance_Type.__name__ = "Integer32"
_PppExtIfGearUpPersistance_Object = MibTableColumn
pppExtIfGearUpPersistance = _PppExtIfGearUpPersistance_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 17),
    _PppExtIfGearUpPersistance_Type()
)
pppExtIfGearUpPersistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfGearUpPersistance.setStatus("mandatory")


class _PppExtIfGearDownPersistance_Type(Integer32):
    """Custom type pppExtIfGearDownPersistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PppExtIfGearDownPersistance_Type.__name__ = "Integer32"
_PppExtIfGearDownPersistance_Object = MibTableColumn
pppExtIfGearDownPersistance = _PppExtIfGearDownPersistance_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 18),
    _PppExtIfGearDownPersistance_Type()
)
pppExtIfGearDownPersistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfGearDownPersistance.setStatus("mandatory")
_PppExtIfL1Speed_Type = Integer32
_PppExtIfL1Speed_Object = MibTableColumn
pppExtIfL1Speed = _PppExtIfL1Speed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 19),
    _PppExtIfL1Speed_Type()
)
pppExtIfL1Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfL1Speed.setStatus("mandatory")


class _PppExtIfCurrentRetryTime_Type(Integer32):
    """Custom type pppExtIfCurrentRetryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36000),
    )


_PppExtIfCurrentRetryTime_Type.__name__ = "Integer32"
_PppExtIfCurrentRetryTime_Object = MibTableColumn
pppExtIfCurrentRetryTime = _PppExtIfCurrentRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 20),
    _PppExtIfCurrentRetryTime_Type()
)
pppExtIfCurrentRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfCurrentRetryTime.setStatus("mandatory")


class _PppExtIfMaxRetryTime_Type(Integer32):
    """Custom type pppExtIfMaxRetryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36000),
    )


_PppExtIfMaxRetryTime_Type.__name__ = "Integer32"
_PppExtIfMaxRetryTime_Object = MibTableColumn
pppExtIfMaxRetryTime = _PppExtIfMaxRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 21),
    _PppExtIfMaxRetryTime_Type()
)
pppExtIfMaxRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfMaxRetryTime.setStatus("mandatory")


class _PppExtIfMtu_Type(Integer32):
    """Custom type pppExtIfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_PppExtIfMtu_Type.__name__ = "Integer32"
_PppExtIfMtu_Object = MibTableColumn
pppExtIfMtu = _PppExtIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 22),
    _PppExtIfMtu_Type()
)
pppExtIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfMtu.setStatus("mandatory")


class _PppExtIfMru_Type(Integer32):
    """Custom type pppExtIfMru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_PppExtIfMru_Type.__name__ = "Integer32"
_PppExtIfMru_Object = MibTableColumn
pppExtIfMru = _PppExtIfMru_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 23),
    _PppExtIfMru_Type()
)
pppExtIfMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfMru.setStatus("mandatory")


class _PppExtIfAuthMutual_Type(Integer32):
    """Custom type pppExtIfAuthMutual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PppExtIfAuthMutual_Type.__name__ = "Integer32"
_PppExtIfAuthMutual_Object = MibTableColumn
pppExtIfAuthMutual = _PppExtIfAuthMutual_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 9, 1, 24),
    _PppExtIfAuthMutual_Type()
)
pppExtIfAuthMutual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtIfAuthMutual.setStatus("mandatory")
_PppSessionTable_Object = MibTable
pppSessionTable = _PppSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10)
)
if mibBuilder.loadTexts:
    pppSessionTable.setStatus("mandatory")
_PppSessionEntry_Object = MibTableRow
pppSessionEntry = _PppSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1)
)
pppSessionEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPP-MIB", "pppSessionIfIndex"),
)
if mibBuilder.loadTexts:
    pppSessionEntry.setStatus("mandatory")
_PppSessionIfIndex_Type = Integer32
_PppSessionIfIndex_Object = MibTableColumn
pppSessionIfIndex = _PppSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 1),
    _PppSessionIfIndex_Type()
)
pppSessionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionIfIndex.setStatus("mandatory")


class _PppSessionMlp_Type(Integer32):
    """Custom type pppSessionMlp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negotiated", 2),
          ("none", 1))
    )


_PppSessionMlp_Type.__name__ = "Integer32"
_PppSessionMlp_Object = MibTableColumn
pppSessionMlp = _PppSessionMlp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 2),
    _PppSessionMlp_Type()
)
pppSessionMlp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionMlp.setStatus("mandatory")
_PppSessionMru_Type = Counter32
_PppSessionMru_Object = MibTableColumn
pppSessionMru = _PppSessionMru_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 3),
    _PppSessionMru_Type()
)
pppSessionMru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionMru.setStatus("mandatory")


class _PppSessionLcpCallback_Type(Integer32):
    """Custom type pppSessionLcpCallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbcp", 3),
          ("lcp", 2),
          ("none", 1))
    )


_PppSessionLcpCallback_Type.__name__ = "Integer32"
_PppSessionLcpCallback_Object = MibTableColumn
pppSessionLcpCallback = _PppSessionLcpCallback_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 4),
    _PppSessionLcpCallback_Type()
)
pppSessionLcpCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionLcpCallback.setStatus("mandatory")


class _PppSessionAuthProt_Type(Integer32):
    """Custom type pppSessionAuthProt based on Integer32"""
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
        *(("chap", 3),
          ("ms-chapv1", 4),
          ("ms-chapv2", 5),
          ("none", 1),
          ("pap", 2))
    )


_PppSessionAuthProt_Type.__name__ = "Integer32"
_PppSessionAuthProt_Object = MibTableColumn
pppSessionAuthProt = _PppSessionAuthProt_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 5),
    _PppSessionAuthProt_Type()
)
pppSessionAuthProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionAuthProt.setStatus("mandatory")


class _PppSessionCompression_Type(Integer32):
    """Custom type pppSessionCompression based on Integer32"""
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
        *(("mppc", 4),
          ("ms-stac", 3),
          ("none", 1),
          ("stac", 2))
    )


_PppSessionCompression_Type.__name__ = "Integer32"
_PppSessionCompression_Object = MibTableColumn
pppSessionCompression = _PppSessionCompression_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 6),
    _PppSessionCompression_Type()
)
pppSessionCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionCompression.setStatus("mandatory")


class _PppSessionEncryption_Type(Integer32):
    """Custom type pppSessionEncryption based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("blowfish-168", 6),
          ("blowfish-56", 11),
          ("des-56", 4),
          ("mppe-128", 3),
          ("mppe-40", 2),
          ("mppe-56", 7),
          ("mppev2-128", 10),
          ("mppev2-40", 8),
          ("mppev2-56", 9),
          ("none", 1),
          ("triple-des-168", 5))
    )


_PppSessionEncryption_Type.__name__ = "Integer32"
_PppSessionEncryption_Object = MibTableColumn
pppSessionEncryption = _PppSessionEncryption_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 7),
    _PppSessionEncryption_Type()
)
pppSessionEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionEncryption.setStatus("mandatory")


class _PppSessionCbcpMode_Type(Integer32):
    """Custom type pppSessionCbcpMode based on Integer32"""
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
        *(("no-callback", 2),
          ("none", 1),
          ("pre-specified", 4),
          ("user-specified", 3))
    )


_PppSessionCbcpMode_Type.__name__ = "Integer32"
_PppSessionCbcpMode_Object = MibTableColumn
pppSessionCbcpMode = _PppSessionCbcpMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 8),
    _PppSessionCbcpMode_Type()
)
pppSessionCbcpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionCbcpMode.setStatus("mandatory")


class _PppSessionCbcpDelay_Type(Integer32):
    """Custom type pppSessionCbcpDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_PppSessionCbcpDelay_Type.__name__ = "Integer32"
_PppSessionCbcpDelay_Object = MibTableColumn
pppSessionCbcpDelay = _PppSessionCbcpDelay_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 9),
    _PppSessionCbcpDelay_Type()
)
pppSessionCbcpDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionCbcpDelay.setStatus("mandatory")
_PppSessionLocIpAddr_Type = IpAddress
_PppSessionLocIpAddr_Object = MibTableColumn
pppSessionLocIpAddr = _PppSessionLocIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 10),
    _PppSessionLocIpAddr_Type()
)
pppSessionLocIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionLocIpAddr.setStatus("mandatory")
_PppSessionRemIpAddr_Type = IpAddress
_PppSessionRemIpAddr_Object = MibTableColumn
pppSessionRemIpAddr = _PppSessionRemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 11),
    _PppSessionRemIpAddr_Type()
)
pppSessionRemIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionRemIpAddr.setStatus("mandatory")
_PppSessionDNS1_Type = IpAddress
_PppSessionDNS1_Object = MibTableColumn
pppSessionDNS1 = _PppSessionDNS1_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 12),
    _PppSessionDNS1_Type()
)
pppSessionDNS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionDNS1.setStatus("mandatory")
_PppSessionDNS2_Type = IpAddress
_PppSessionDNS2_Object = MibTableColumn
pppSessionDNS2 = _PppSessionDNS2_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 13),
    _PppSessionDNS2_Type()
)
pppSessionDNS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionDNS2.setStatus("mandatory")
_PppSessionWINS1_Type = IpAddress
_PppSessionWINS1_Object = MibTableColumn
pppSessionWINS1 = _PppSessionWINS1_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 14),
    _PppSessionWINS1_Type()
)
pppSessionWINS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionWINS1.setStatus("mandatory")
_PppSessionWINS2_Type = IpAddress
_PppSessionWINS2_Object = MibTableColumn
pppSessionWINS2 = _PppSessionWINS2_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 15),
    _PppSessionWINS2_Type()
)
pppSessionWINS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionWINS2.setStatus("mandatory")


class _PppSessionVJHeaderComp_Type(Integer32):
    """Custom type pppSessionVJHeaderComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negotiated", 2),
          ("none", 1))
    )


_PppSessionVJHeaderComp_Type.__name__ = "Integer32"
_PppSessionVJHeaderComp_Object = MibTableColumn
pppSessionVJHeaderComp = _PppSessionVJHeaderComp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 16),
    _PppSessionVJHeaderComp_Type()
)
pppSessionVJHeaderComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionVJHeaderComp.setStatus("mandatory")


class _PppSessionIpxcpNodeNumber_Type(OctetString):
    """Custom type pppSessionIpxcpNodeNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PppSessionIpxcpNodeNumber_Type.__name__ = "OctetString"
_PppSessionIpxcpNodeNumber_Object = MibTableColumn
pppSessionIpxcpNodeNumber = _PppSessionIpxcpNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 17),
    _PppSessionIpxcpNodeNumber_Type()
)
pppSessionIpxcpNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionIpxcpNodeNumber.setStatus("mandatory")


class _PppSessionBacpFavoredPeer_Type(Integer32):
    """Custom type pppSessionBacpFavoredPeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("none", 1),
          ("remote", 3))
    )


_PppSessionBacpFavoredPeer_Type.__name__ = "Integer32"
_PppSessionBacpFavoredPeer_Object = MibTableColumn
pppSessionBacpFavoredPeer = _PppSessionBacpFavoredPeer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 3, 10, 1, 18),
    _PppSessionBacpFavoredPeer_Type()
)
pppSessionBacpFavoredPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSessionBacpFavoredPeer.setStatus("mandatory")
_Dialmap_ObjectIdentity = ObjectIdentity
dialmap = _Dialmap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 4)
)
_BiboDialTable_Object = MibTable
biboDialTable = _BiboDialTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 4, 1)
)
if mibBuilder.loadTexts:
    biboDialTable.setStatus("mandatory")
_BiboDialEntry_Object = MibTableRow
biboDialEntry = _BiboDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 4, 1, 1)
)
biboDialEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPP-MIB", "biboDialIfIndex"),
)
if mibBuilder.loadTexts:
    biboDialEntry.setStatus("mandatory")
_BiboDialIfIndex_Type = Integer32
_BiboDialIfIndex_Object = MibTableColumn
biboDialIfIndex = _BiboDialIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 4, 1, 1, 1),
    _BiboDialIfIndex_Type()
)
biboDialIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboDialIfIndex.setStatus("mandatory")


class _BiboDialType_Type(Integer32):
    """Custom type biboDialType based on Integer32"""
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
        *(("delete", 3),
          ("ip", 7),
          ("isdn", 1),
          ("isdn-spv", 2),
          ("ppp-callback", 4),
          ("ppp-negotiated", 5),
          ("x25", 8),
          ("x25-dialout", 6))
    )


_BiboDialType_Type.__name__ = "Integer32"
_BiboDialType_Object = MibTableColumn
biboDialType = _BiboDialType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 4, 1, 1, 2),
    _BiboDialType_Type()
)
biboDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboDialType.setStatus("mandatory")


class _BiboDialDirection_Type(Integer32):
    """Custom type biboDialDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("incoming", 1),
          ("outgoing", 2))
    )


_BiboDialDirection_Type.__name__ = "Integer32"
_BiboDialDirection_Object = MibTableColumn
biboDialDirection = _BiboDialDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 4, 1, 1, 3),
    _BiboDialDirection_Type()
)
biboDialDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboDialDirection.setStatus("mandatory")


class _BiboDialNumber_Type(DisplayString):
    """Custom type biboDialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_BiboDialNumber_Type.__name__ = "DisplayString"
_BiboDialNumber_Object = MibTableColumn
biboDialNumber = _BiboDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 4, 1, 1, 4),
    _BiboDialNumber_Type()
)
biboDialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboDialNumber.setStatus("mandatory")
_BiboDialSubaddress_Type = OctetString
_BiboDialSubaddress_Object = MibTableColumn
biboDialSubaddress = _BiboDialSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 4, 1, 1, 5),
    _BiboDialSubaddress_Type()
)
biboDialSubaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboDialSubaddress.setStatus("mandatory")


class _BiboDialClosedUserGroup_Type(Integer32):
    """Custom type biboDialClosedUserGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_BiboDialClosedUserGroup_Type.__name__ = "Integer32"
_BiboDialClosedUserGroup_Object = MibTableColumn
biboDialClosedUserGroup = _BiboDialClosedUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 4, 1, 1, 6),
    _BiboDialClosedUserGroup_Type()
)
biboDialClosedUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboDialClosedUserGroup.setStatus("mandatory")
_BiboDialStkMask_Type = BitValue
_BiboDialStkMask_Object = MibTableColumn
biboDialStkMask = _BiboDialStkMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 4, 1, 1, 7),
    _BiboDialStkMask_Type()
)
biboDialStkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboDialStkMask.setStatus("mandatory")


class _BiboDialScreening_Type(Integer32):
    """Custom type biboDialScreening based on Integer32"""
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
        *(("dont-care", 5),
          ("network", 4),
          ("user", 1),
          ("user-failed", 3),
          ("user-verified", 2))
    )


_BiboDialScreening_Type.__name__ = "Integer32"
_BiboDialScreening_Object = MibTableColumn
biboDialScreening = _BiboDialScreening_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 4, 1, 1, 8),
    _BiboDialScreening_Type()
)
biboDialScreening.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboDialScreening.setStatus("mandatory")
_BiboDialCallingSubaddress_Type = OctetString
_BiboDialCallingSubaddress_Object = MibTableColumn
biboDialCallingSubaddress = _BiboDialCallingSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 4, 1, 1, 9),
    _BiboDialCallingSubaddress_Type()
)
biboDialCallingSubaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboDialCallingSubaddress.setStatus("mandatory")


class _BiboDialTypeOfCallingSubAdd_Type(Integer32):
    """Custom type biboDialTypeOfCallingSubAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nsap", 1),
          ("reserved", 3),
          ("user-specified", 2))
    )


_BiboDialTypeOfCallingSubAdd_Type.__name__ = "Integer32"
_BiboDialTypeOfCallingSubAdd_Object = MibTableColumn
biboDialTypeOfCallingSubAdd = _BiboDialTypeOfCallingSubAdd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 4, 1, 1, 10),
    _BiboDialTypeOfCallingSubAdd_Type()
)
biboDialTypeOfCallingSubAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboDialTypeOfCallingSubAdd.setStatus("mandatory")


class _BiboDialTypeOfCalledSubAdd_Type(Integer32):
    """Custom type biboDialTypeOfCalledSubAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nsap", 1),
          ("reserved", 3),
          ("user-specified", 2))
    )


_BiboDialTypeOfCalledSubAdd_Type.__name__ = "Integer32"
_BiboDialTypeOfCalledSubAdd_Object = MibTableColumn
biboDialTypeOfCalledSubAdd = _BiboDialTypeOfCalledSubAdd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 4, 1, 1, 11),
    _BiboDialTypeOfCalledSubAdd_Type()
)
biboDialTypeOfCalledSubAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboDialTypeOfCalledSubAdd.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-PPP-MIB",
    **{"BitValue": BitValue,
       "Date": Date,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "ppp": ppp,
       "biboPPPTable": biboPPPTable,
       "biboPPPEntry": biboPPPEntry,
       "biboPPPIfIndex": biboPPPIfIndex,
       "biboPPPType": biboPPPType,
       "biboPPPEncapsulation": biboPPPEncapsulation,
       "biboPPPKeepalive": biboPPPKeepalive,
       "biboPPPTimeout": biboPPPTimeout,
       "biboPPPCompression": biboPPPCompression,
       "biboPPPAuthentication": biboPPPAuthentication,
       "biboPPPAuthIdent": biboPPPAuthIdent,
       "biboPPPAuthSecret": biboPPPAuthSecret,
       "biboPPPIpAddress": biboPPPIpAddress,
       "biboPPPRetryTime": biboPPPRetryTime,
       "biboPPPBlockTime": biboPPPBlockTime,
       "biboPPPMaxRetries": biboPPPMaxRetries,
       "biboPPPShortHold": biboPPPShortHold,
       "biboPPPInitConn": biboPPPInitConn,
       "biboPPPMaxConn": biboPPPMaxConn,
       "biboPPPMinConn": biboPPPMinConn,
       "biboPPPCallback": biboPPPCallback,
       "biboPPPLayer1Protocol": biboPPPLayer1Protocol,
       "biboPPPLoginString": biboPPPLoginString,
       "biboPPPVJHeaderComp": biboPPPVJHeaderComp,
       "biboPPPLayer2Mode": biboPPPLayer2Mode,
       "biboPPPDynShortHold": biboPPPDynShortHold,
       "biboPPPLocalIdent": biboPPPLocalIdent,
       "biboPPPDNSNegotiation": biboPPPDNSNegotiation,
       "biboPPPEncryption": biboPPPEncryption,
       "biboPPPLQMonitoring": biboPPPLQMonitoring,
       "biboPPPIpPoolId": biboPPPIpPoolId,
       "biboPPPSessionTimeout": biboPPPSessionTimeout,
       "biboPPPStatTable": biboPPPStatTable,
       "biboPPPStatEntry": biboPPPStatEntry,
       "biboPPPConnIfIndex": biboPPPConnIfIndex,
       "biboPPPConnActive": biboPPPConnActive,
       "biboPPPConnProtocols": biboPPPConnProtocols,
       "biboPPPConnState": biboPPPConnState,
       "biboPPPConnDuration": biboPPPConnDuration,
       "biboPPPConnUnits": biboPPPConnUnits,
       "biboPPPConnTransmitOctets": biboPPPConnTransmitOctets,
       "biboPPPConnReceivedOctets": biboPPPConnReceivedOctets,
       "biboPPPConnOutgoingCalls": biboPPPConnOutgoingCalls,
       "biboPPPConnOutgoingFails": biboPPPConnOutgoingFails,
       "biboPPPConnIncomingCalls": biboPPPConnIncomingCalls,
       "biboPPPConnIncomingFails": biboPPPConnIncomingFails,
       "biboPPPTotalDuration": biboPPPTotalDuration,
       "biboPPPTotalUnits": biboPPPTotalUnits,
       "biboPPPTotalTransmitOctets": biboPPPTotalTransmitOctets,
       "biboPPPTotalReceivedOctets": biboPPPTotalReceivedOctets,
       "biboPPPTotalOutgoingCalls": biboPPPTotalOutgoingCalls,
       "biboPPPTotalOutgoingFails": biboPPPTotalOutgoingFails,
       "biboPPPTotalIncomingCalls": biboPPPTotalIncomingCalls,
       "biboPPPTotalIncomingFails": biboPPPTotalIncomingFails,
       "biboPPPThroughput": biboPPPThroughput,
       "biboPPPCompressionMode": biboPPPCompressionMode,
       "biboPPPChargeInterval": biboPPPChargeInterval,
       "biboPPPIdleTime": biboPPPIdleTime,
       "biboPPPConnCharge": biboPPPConnCharge,
       "biboPPPTotalCharge": biboPPPTotalCharge,
       "biboPPPLinkTable": biboPPPLinkTable,
       "biboPPPLinkEntry": biboPPPLinkEntry,
       "biboPPPLinkIfIndex": biboPPPLinkIfIndex,
       "biboPPPLinkEstablished": biboPPPLinkEstablished,
       "biboPPPLinkDirection": biboPPPLinkDirection,
       "biboPPPLinkProtocols": biboPPPLinkProtocols,
       "biboPPPLinkState": biboPPPLinkState,
       "biboPPPLinkUnits": biboPPPLinkUnits,
       "biboPPPLinkRetries": biboPPPLinkRetries,
       "biboPPPLinkKeepaliveSent": biboPPPLinkKeepaliveSent,
       "biboPPPLinkKeepalivePending": biboPPPLinkKeepalivePending,
       "biboPPPLinkDeviceIndex": biboPPPLinkDeviceIndex,
       "biboPPPLinkSpeed": biboPPPLinkSpeed,
       "biboPPPLinkStkNumber": biboPPPLinkStkNumber,
       "biboPPPLinkCallType": biboPPPLinkCallType,
       "biboPPPLinkCallReference": biboPPPLinkCallReference,
       "biboPPPLinkCharge": biboPPPLinkCharge,
       "biboPPPLinkAccm": biboPPPLinkAccm,
       "biboPPPLinkLqm": biboPPPLinkLqm,
       "biboPPPLinkLcpComp": biboPPPLinkLcpComp,
       "biboPPPLinkLocDiscr": biboPPPLinkLocDiscr,
       "biboPPPLinkRemDiscr": biboPPPLinkRemDiscr,
       "biboPPPIpAssignTable": biboPPPIpAssignTable,
       "biboPPPIpAssignEntry": biboPPPIpAssignEntry,
       "biboPPPIpAssignAddress": biboPPPIpAssignAddress,
       "biboPPPIpAssignState": biboPPPIpAssignState,
       "biboPPPIpAssignPoolId": biboPPPIpAssignPoolId,
       "biboPPPIpAssignRange": biboPPPIpAssignRange,
       "biboPPPProfileTable": biboPPPProfileTable,
       "biboPPPProfileEntry": biboPPPProfileEntry,
       "biboPPPProfileName": biboPPPProfileName,
       "biboPPPProfileAuthProtocol": biboPPPProfileAuthProtocol,
       "biboPPPProfileAuthRadius": biboPPPProfileAuthRadius,
       "biboPPPProfileLQMonitoring": biboPPPProfileLQMonitoring,
       "biboPPPProfilePPPoEDevIfIndex": biboPPPProfilePPPoEDevIfIndex,
       "biboPPPProfileCallbackNegotiation": biboPPPProfileCallbackNegotiation,
       "pppLqmTable": pppLqmTable,
       "pppLqmEntry": pppLqmEntry,
       "pppLqmIfIndex": pppLqmIfIndex,
       "pppLqmCallReference": pppLqmCallReference,
       "pppLqmReportingPeriod": pppLqmReportingPeriod,
       "pppLqmOutLQRs": pppLqmOutLQRs,
       "pppLqmOutPackets": pppLqmOutPackets,
       "pppLqmOutOctets": pppLqmOutOctets,
       "pppLqmInLQRs": pppLqmInLQRs,
       "pppLqmInPackets": pppLqmInPackets,
       "pppLqmInOctets": pppLqmInOctets,
       "pppLqmInDiscards": pppLqmInDiscards,
       "pppLqmInErrors": pppLqmInErrors,
       "pppLqmPeerOutLQRs": pppLqmPeerOutLQRs,
       "pppLqmPeerOutPackets": pppLqmPeerOutPackets,
       "pppLqmPeerOutOctets": pppLqmPeerOutOctets,
       "pppLqmPeerInLQRs": pppLqmPeerInLQRs,
       "pppLqmPeerInPackets": pppLqmPeerInPackets,
       "pppLqmPeerInOctets": pppLqmPeerInOctets,
       "pppLqmPeerInDiscards": pppLqmPeerInDiscards,
       "pppLqmPeerInErrors": pppLqmPeerInErrors,
       "pppLqmLostOutLQRs": pppLqmLostOutLQRs,
       "pppLqmLostOutPackets": pppLqmLostOutPackets,
       "pppLqmLostOutOctets": pppLqmLostOutOctets,
       "pppLqmLostPeerOutLQRs": pppLqmLostPeerOutLQRs,
       "pppLqmLostPeerOutPkts": pppLqmLostPeerOutPkts,
       "pppLqmLostPeerOutOcts": pppLqmLostPeerOutOcts,
       "pppIpInUseTable": pppIpInUseTable,
       "pppIpInUseEntry": pppIpInUseEntry,
       "pppIpInUseAddress": pppIpInUseAddress,
       "pppIpInUsePoolId": pppIpInUsePoolId,
       "pppIpInUseIfIndex": pppIpInUseIfIndex,
       "pppIpInUseIdent": pppIpInUseIdent,
       "pppIpInUseState": pppIpInUseState,
       "pppIpInUseAge": pppIpInUseAge,
       "pppExtIfTable": pppExtIfTable,
       "pppExtIfEntry": pppExtIfEntry,
       "pppExtIfIndex": pppExtIfIndex,
       "pppExtIfBodMode": pppExtIfBodMode,
       "pppExtIfAlgorithm": pppExtIfAlgorithm,
       "pppExtIfInterval": pppExtIfInterval,
       "pppExtIfLoad": pppExtIfLoad,
       "pppExtIfMlpFragmentation": pppExtIfMlpFragmentation,
       "pppExtIfMlpFragSize": pppExtIfMlpFragSize,
       "pppExtIfPPPoEService": pppExtIfPPPoEService,
       "pppExtIfPPPoEAcServer": pppExtIfPPPoEAcServer,
       "pppExtIfEncKeyNegotiation": pppExtIfEncKeyNegotiation,
       "pppExtIfEncTxKey": pppExtIfEncTxKey,
       "pppExtIfEncRxKey": pppExtIfEncRxKey,
       "pppExtIfGearUpThreshold": pppExtIfGearUpThreshold,
       "pppExtIfGearDownThreshold": pppExtIfGearDownThreshold,
       "pppExtIfAodiDChanQlen": pppExtIfAodiDChanQlen,
       "pppExtIfAodiGearDownTxRate": pppExtIfAodiGearDownTxRate,
       "pppExtIfGearUpPersistance": pppExtIfGearUpPersistance,
       "pppExtIfGearDownPersistance": pppExtIfGearDownPersistance,
       "pppExtIfL1Speed": pppExtIfL1Speed,
       "pppExtIfCurrentRetryTime": pppExtIfCurrentRetryTime,
       "pppExtIfMaxRetryTime": pppExtIfMaxRetryTime,
       "pppExtIfMtu": pppExtIfMtu,
       "pppExtIfMru": pppExtIfMru,
       "pppExtIfAuthMutual": pppExtIfAuthMutual,
       "pppSessionTable": pppSessionTable,
       "pppSessionEntry": pppSessionEntry,
       "pppSessionIfIndex": pppSessionIfIndex,
       "pppSessionMlp": pppSessionMlp,
       "pppSessionMru": pppSessionMru,
       "pppSessionLcpCallback": pppSessionLcpCallback,
       "pppSessionAuthProt": pppSessionAuthProt,
       "pppSessionCompression": pppSessionCompression,
       "pppSessionEncryption": pppSessionEncryption,
       "pppSessionCbcpMode": pppSessionCbcpMode,
       "pppSessionCbcpDelay": pppSessionCbcpDelay,
       "pppSessionLocIpAddr": pppSessionLocIpAddr,
       "pppSessionRemIpAddr": pppSessionRemIpAddr,
       "pppSessionDNS1": pppSessionDNS1,
       "pppSessionDNS2": pppSessionDNS2,
       "pppSessionWINS1": pppSessionWINS1,
       "pppSessionWINS2": pppSessionWINS2,
       "pppSessionVJHeaderComp": pppSessionVJHeaderComp,
       "pppSessionIpxcpNodeNumber": pppSessionIpxcpNodeNumber,
       "pppSessionBacpFavoredPeer": pppSessionBacpFavoredPeer,
       "dialmap": dialmap,
       "biboDialTable": biboDialTable,
       "biboDialEntry": biboDialEntry,
       "biboDialIfIndex": biboDialIfIndex,
       "biboDialType": biboDialType,
       "biboDialDirection": biboDialDirection,
       "biboDialNumber": biboDialNumber,
       "biboDialSubaddress": biboDialSubaddress,
       "biboDialClosedUserGroup": biboDialClosedUserGroup,
       "biboDialStkMask": biboDialStkMask,
       "biboDialScreening": biboDialScreening,
       "biboDialCallingSubaddress": biboDialCallingSubaddress,
       "biboDialTypeOfCallingSubAdd": biboDialTypeOfCallingSubAdd,
       "biboDialTypeOfCalledSubAdd": biboDialTypeOfCalledSubAdd}
)
