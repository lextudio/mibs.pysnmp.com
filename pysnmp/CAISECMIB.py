# SNMP MIB module (CAISECMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAISECMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:19 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cai_ObjectIdentity = ObjectIdentity
cai = _Cai_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791)
)
_CaiSysMgt_ObjectIdentity = ObjectIdentity
caiSysMgt = _CaiSysMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2)
)
_CaiSecurity_ObjectIdentity = ObjectIdentity
caiSecurity = _CaiSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 3)
)
_CaiACF2_ObjectIdentity = ObjectIdentity
caiACF2 = _CaiACF2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 3, 2)
)


class _CaiACF2LstMsg_Type(DisplayString):
    """Custom type caiACF2LstMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CaiACF2LstMsg_Type.__name__ = "DisplayString"
_CaiACF2LstMsg_Object = MibScalar
caiACF2LstMsg = _CaiACF2LstMsg_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 3, 2, 2),
    _CaiACF2LstMsg_Type()
)
caiACF2LstMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caiACF2LstMsg.setStatus("mandatory")
_CaiTSS_ObjectIdentity = ObjectIdentity
caiTSS = _CaiTSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 3, 3)
)


class _CaiTSSLstMsg_Type(DisplayString):
    """Custom type caiTSSLstMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CaiTSSLstMsg_Type.__name__ = "DisplayString"
_CaiTSSLstMsg_Object = MibScalar
caiTSSLstMsg = _CaiTSSLstMsg_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 3, 3, 2),
    _CaiTSSLstMsg_Type()
)
caiTSSLstMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caiTSSLstMsg.setStatus("mandatory")
_CaiDbMgt_ObjectIdentity = ObjectIdentity
caiDbMgt = _CaiDbMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 3)
)
_CaiAppSft_ObjectIdentity = ObjectIdentity
caiAppSft = _CaiAppSft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 4)
)

# Managed Objects groups


# Notification objects

caiACF2AVT1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 1000)
)
caiACF2AVT1.setObjects(
    ("CAISECMIB", "caiACF2LstMsg")
)
if mibBuilder.loadTexts:
    caiACF2AVT1.setStatus(
        ""
    )

caiACF2AVT2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 1001)
)
caiACF2AVT2.setObjects(
    ("CAISECMIB", "caiACF2LstMsg")
)
if mibBuilder.loadTexts:
    caiACF2AVT2.setStatus(
        ""
    )

caiACF2PVT1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 1020)
)
caiACF2PVT1.setObjects(
    ("CAISECMIB", "caiACF2LstMsg")
)
if mibBuilder.loadTexts:
    caiACF2PVT1.setStatus(
        ""
    )

caiACF2USP1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 1030)
)
caiACF2USP1.setObjects(
    ("CAISECMIB", "caiACF2LstMsg")
)
if mibBuilder.loadTexts:
    caiACF2USP1.setStatus(
        ""
    )

caiTSSAVT1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 1100)
)
caiTSSAVT1.setObjects(
    ("CAISECMIB", "caiTSSLstMsg")
)
if mibBuilder.loadTexts:
    caiTSSAVT1.setStatus(
        ""
    )

caiTSSAVT2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 1101)
)
caiTSSAVT2.setObjects(
    ("CAISECMIB", "caiTSSLstMsg")
)
if mibBuilder.loadTexts:
    caiTSSAVT2.setStatus(
        ""
    )

caiTSSAVT3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 1102)
)
caiTSSAVT3.setObjects(
    ("CAISECMIB", "caiTSSLstMsg")
)
if mibBuilder.loadTexts:
    caiTSSAVT3.setStatus(
        ""
    )

caiTSSPVT1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 1120)
)
caiTSSPVT1.setObjects(
    ("CAISECMIB", "caiTSSLstMsg")
)
if mibBuilder.loadTexts:
    caiTSSPVT1.setStatus(
        ""
    )

caiTSSUSP1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 1130)
)
caiTSSUSP1.setObjects(
    ("CAISECMIB", "caiTSSLstMsg")
)
if mibBuilder.loadTexts:
    caiTSSUSP1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAISECMIB",
    **{"cai": cai,
       "caiACF2AVT1": caiACF2AVT1,
       "caiACF2AVT2": caiACF2AVT2,
       "caiACF2PVT1": caiACF2PVT1,
       "caiACF2USP1": caiACF2USP1,
       "caiTSSAVT1": caiTSSAVT1,
       "caiTSSAVT2": caiTSSAVT2,
       "caiTSSAVT3": caiTSSAVT3,
       "caiTSSPVT1": caiTSSPVT1,
       "caiTSSUSP1": caiTSSUSP1,
       "caiSysMgt": caiSysMgt,
       "caiSecurity": caiSecurity,
       "caiACF2": caiACF2,
       "caiACF2LstMsg": caiACF2LstMsg,
       "caiTSS": caiTSS,
       "caiTSSLstMsg": caiTSSLstMsg,
       "caiDbMgt": caiDbMgt,
       "caiAppSft": caiAppSft}
)
