# SNMP MIB module (LANOPTICS-BRIDGE-OPTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANOPTICS-BRIDGE-OPTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:13 2024
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

_LanOptics_ObjectIdentity = ObjectIdentity
lanOptics = _LanOptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224)
)
_LanOpticsBridgeProxyAgent_ObjectIdentity = ObjectIdentity
lanOpticsBridgeProxyAgent = _LanOpticsBridgeProxyAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 6)
)
_LanOpticsLMGRAgent_ObjectIdentity = ObjectIdentity
lanOpticsLMGRAgent = _LanOpticsLMGRAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 6, 8)
)


class _LanOpticsLMGRLinkID_Type(Integer32):
    """Custom type lanOpticsLMGRLinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LanOpticsLMGRLinkID_Type.__name__ = "Integer32"
_LanOpticsLMGRLinkID_Object = MibScalar
lanOpticsLMGRLinkID = _LanOpticsLMGRLinkID_Object(
    (1, 3, 6, 1, 4, 1, 224, 6, 8, 1),
    _LanOpticsLMGRLinkID_Type()
)
lanOpticsLMGRLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanOpticsLMGRLinkID.setStatus("mandatory")


class _LanOpticsLMGRCaptCntrlLink_Type(Integer32):
    """Custom type lanOpticsLMGRCaptCntrlLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )


_LanOpticsLMGRCaptCntrlLink_Type.__name__ = "Integer32"
_LanOpticsLMGRCaptCntrlLink_Object = MibScalar
lanOpticsLMGRCaptCntrlLink = _LanOpticsLMGRCaptCntrlLink_Object(
    (1, 3, 6, 1, 4, 1, 224, 6, 8, 2),
    _LanOpticsLMGRCaptCntrlLink_Type()
)
lanOpticsLMGRCaptCntrlLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanOpticsLMGRCaptCntrlLink.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANOPTICS-BRIDGE-OPTION-MIB",
    **{"lanOptics": lanOptics,
       "lanOpticsBridgeProxyAgent": lanOpticsBridgeProxyAgent,
       "lanOpticsLMGRAgent": lanOpticsLMGRAgent,
       "lanOpticsLMGRLinkID": lanOpticsLMGRLinkID,
       "lanOpticsLMGRCaptCntrlLink": lanOpticsLMGRCaptCntrlLink}
)
