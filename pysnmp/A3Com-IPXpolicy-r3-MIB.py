# SNMP MIB module (A3COM-IPXPOLICY-R3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-IPXPOLICY-R3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:36 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "RFC1286-MIB",
    "MacAddress")

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



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class IPXNET(OctetString):
    """Custom type IPXNET based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_A3ComIPXpol_ObjectIdentity = ObjectIdentity
a3ComIPXpol = _A3ComIPXpol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 11)
)
_A3ipxPolControlTable_Object = MibTable
a3ipxPolControlTable = _A3ipxPolControlTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1)
)
if mibBuilder.loadTexts:
    a3ipxPolControlTable.setStatus("mandatory")
_A3ipxPolControlEntry_Object = MibTableRow
a3ipxPolControlEntry = _A3ipxPolControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1)
)
a3ipxPolControlEntry.setIndexNames(
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPCPort"),
)
if mibBuilder.loadTexts:
    a3ipxPolControlEntry.setStatus("mandatory")
_A3ipxPCPort_Type = Integer32
_A3ipxPCPort_Object = MibTableColumn
a3ipxPCPort = _A3ipxPCPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 1),
    _A3ipxPCPort_Type()
)
a3ipxPCPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPCPort.setStatus("mandatory")


class _A3ipxPCRteAdvCtl_Type(Integer32):
    """Custom type a3ipxPCRteAdvCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_A3ipxPCRteAdvCtl_Type.__name__ = "Integer32"
_A3ipxPCRteAdvCtl_Object = MibTableColumn
a3ipxPCRteAdvCtl = _A3ipxPCRteAdvCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 2),
    _A3ipxPCRteAdvCtl_Type()
)
a3ipxPCRteAdvCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCRteAdvCtl.setStatus("mandatory")


class _A3ipxPCRteAdvType_Type(Integer32):
    """Custom type a3ipxPCRteAdvType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverse", 2),
          ("normal", 1))
    )


_A3ipxPCRteAdvType_Type.__name__ = "Integer32"
_A3ipxPCRteAdvType_Object = MibTableColumn
a3ipxPCRteAdvType = _A3ipxPCRteAdvType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 3),
    _A3ipxPCRteAdvType_Type()
)
a3ipxPCRteAdvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCRteAdvType.setStatus("mandatory")


class _A3ipxPCRteRcvCtl_Type(Integer32):
    """Custom type a3ipxPCRteRcvCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_A3ipxPCRteRcvCtl_Type.__name__ = "Integer32"
_A3ipxPCRteRcvCtl_Object = MibTableColumn
a3ipxPCRteRcvCtl = _A3ipxPCRteRcvCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 4),
    _A3ipxPCRteRcvCtl_Type()
)
a3ipxPCRteRcvCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCRteRcvCtl.setStatus("mandatory")


class _A3ipxPCRteRcvType_Type(Integer32):
    """Custom type a3ipxPCRteRcvType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverse", 2),
          ("normal", 1))
    )


_A3ipxPCRteRcvType_Type.__name__ = "Integer32"
_A3ipxPCRteRcvType_Object = MibTableColumn
a3ipxPCRteRcvType = _A3ipxPCRteRcvType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 5),
    _A3ipxPCRteRcvType_Type()
)
a3ipxPCRteRcvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCRteRcvType.setStatus("mandatory")


class _A3ipxPCSvcAdvCtl_Type(Integer32):
    """Custom type a3ipxPCSvcAdvCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_A3ipxPCSvcAdvCtl_Type.__name__ = "Integer32"
_A3ipxPCSvcAdvCtl_Object = MibTableColumn
a3ipxPCSvcAdvCtl = _A3ipxPCSvcAdvCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 6),
    _A3ipxPCSvcAdvCtl_Type()
)
a3ipxPCSvcAdvCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCSvcAdvCtl.setStatus("mandatory")


class _A3ipxPCSvcAdvType_Type(Integer32):
    """Custom type a3ipxPCSvcAdvType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverse", 2),
          ("normal", 1))
    )


_A3ipxPCSvcAdvType_Type.__name__ = "Integer32"
_A3ipxPCSvcAdvType_Object = MibTableColumn
a3ipxPCSvcAdvType = _A3ipxPCSvcAdvType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 7),
    _A3ipxPCSvcAdvType_Type()
)
a3ipxPCSvcAdvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCSvcAdvType.setStatus("mandatory")


class _A3ipxPCSvcRcvCtl_Type(Integer32):
    """Custom type a3ipxPCSvcRcvCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_A3ipxPCSvcRcvCtl_Type.__name__ = "Integer32"
_A3ipxPCSvcRcvCtl_Object = MibTableColumn
a3ipxPCSvcRcvCtl = _A3ipxPCSvcRcvCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 8),
    _A3ipxPCSvcRcvCtl_Type()
)
a3ipxPCSvcRcvCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCSvcRcvCtl.setStatus("mandatory")


class _A3ipxPCSvcRcvType_Type(Integer32):
    """Custom type a3ipxPCSvcRcvType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverse", 2),
          ("normal", 1))
    )


_A3ipxPCSvcRcvType_Type.__name__ = "Integer32"
_A3ipxPCSvcRcvType_Object = MibTableColumn
a3ipxPCSvcRcvType = _A3ipxPCSvcRcvType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 9),
    _A3ipxPCSvcRcvType_Type()
)
a3ipxPCSvcRcvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCSvcRcvType.setStatus("mandatory")


class _A3ipxPCNbrAdvCtl_Type(Integer32):
    """Custom type a3ipxPCNbrAdvCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_A3ipxPCNbrAdvCtl_Type.__name__ = "Integer32"
_A3ipxPCNbrAdvCtl_Object = MibTableColumn
a3ipxPCNbrAdvCtl = _A3ipxPCNbrAdvCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 10),
    _A3ipxPCNbrAdvCtl_Type()
)
a3ipxPCNbrAdvCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCNbrAdvCtl.setStatus("deprecated")


class _A3ipxPCNbrRcvCtl_Type(Integer32):
    """Custom type a3ipxPCNbrRcvCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_A3ipxPCNbrRcvCtl_Type.__name__ = "Integer32"
_A3ipxPCNbrRcvCtl_Object = MibTableColumn
a3ipxPCNbrRcvCtl = _A3ipxPCNbrRcvCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 11),
    _A3ipxPCNbrRcvCtl_Type()
)
a3ipxPCNbrRcvCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCNbrRcvCtl.setStatus("deprecated")


class _A3ipxPCNbrRcvType_Type(Integer32):
    """Custom type a3ipxPCNbrRcvType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverse", 2),
          ("normal", 1))
    )


_A3ipxPCNbrRcvType_Type.__name__ = "Integer32"
_A3ipxPCNbrRcvType_Object = MibTableColumn
a3ipxPCNbrRcvType = _A3ipxPCNbrRcvType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 12),
    _A3ipxPCNbrRcvType_Type()
)
a3ipxPCNbrRcvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCNbrRcvType.setStatus("deprecated")


class _A3ipxPCPolicyOverride_Type(Integer32):
    """Custom type a3ipxPCPolicyOverride based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPolicyOverride", 2),
          ("policyOverride", 1))
    )


_A3ipxPCPolicyOverride_Type.__name__ = "Integer32"
_A3ipxPCPolicyOverride_Object = MibTableColumn
a3ipxPCPolicyOverride = _A3ipxPCPolicyOverride_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 13),
    _A3ipxPCPolicyOverride_Type()
)
a3ipxPCPolicyOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCPolicyOverride.setStatus("deprecated")


class _A3ipxPCSvrRplyCtl_Type(Integer32):
    """Custom type a3ipxPCSvrRplyCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bestSvrReply", 1),
          ("noBestSvrReply", 2))
    )


_A3ipxPCSvrRplyCtl_Type.__name__ = "Integer32"
_A3ipxPCSvrRplyCtl_Object = MibTableColumn
a3ipxPCSvrRplyCtl = _A3ipxPCSvrRplyCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 14),
    _A3ipxPCSvrRplyCtl_Type()
)
a3ipxPCSvrRplyCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCSvrRplyCtl.setStatus("mandatory")


class _A3ipxPCRipPolOverride_Type(Integer32):
    """Custom type a3ipxPCRipPolOverride based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPolicyOverride", 2),
          ("policyOverride", 1))
    )


_A3ipxPCRipPolOverride_Type.__name__ = "Integer32"
_A3ipxPCRipPolOverride_Object = MibTableColumn
a3ipxPCRipPolOverride = _A3ipxPCRipPolOverride_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 15),
    _A3ipxPCRipPolOverride_Type()
)
a3ipxPCRipPolOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCRipPolOverride.setStatus("mandatory")


class _A3ipxPCSapPolOverride_Type(Integer32):
    """Custom type a3ipxPCSapPolOverride based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPolicyOverride", 2),
          ("policyOverride", 1))
    )


_A3ipxPCSapPolOverride_Type.__name__ = "Integer32"
_A3ipxPCSapPolOverride_Object = MibTableColumn
a3ipxPCSapPolOverride = _A3ipxPCSapPolOverride_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 1, 1, 16),
    _A3ipxPCSapPolOverride_Type()
)
a3ipxPCSapPolOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPCSapPolOverride.setStatus("mandatory")
_A3ipxPolRteTable_Object = MibTable
a3ipxPolRteTable = _A3ipxPolRteTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 2)
)
if mibBuilder.loadTexts:
    a3ipxPolRteTable.setStatus("mandatory")
_A3ipxPolRteEntry_Object = MibTableRow
a3ipxPolRteEntry = _A3ipxPolRteEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 2, 1)
)
a3ipxPolRteEntry.setIndexNames(
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolRtePort"),
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolRteNet1"),
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolRteNet2"),
)
if mibBuilder.loadTexts:
    a3ipxPolRteEntry.setStatus("mandatory")
_A3ipxPolRtePort_Type = Integer32
_A3ipxPolRtePort_Object = MibTableColumn
a3ipxPolRtePort = _A3ipxPolRtePort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 2, 1, 1),
    _A3ipxPolRtePort_Type()
)
a3ipxPolRtePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolRtePort.setStatus("mandatory")


class _A3ipxPolRteType_Type(Integer32):
    """Custom type a3ipxPolRteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 1),
          ("both", 3),
          ("receive", 2))
    )


_A3ipxPolRteType_Type.__name__ = "Integer32"
_A3ipxPolRteType_Object = MibTableColumn
a3ipxPolRteType = _A3ipxPolRteType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 2, 1, 2),
    _A3ipxPolRteType_Type()
)
a3ipxPolRteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolRteType.setStatus("mandatory")
_A3ipxPolRteNet1_Type = IPXNET
_A3ipxPolRteNet1_Object = MibTableColumn
a3ipxPolRteNet1 = _A3ipxPolRteNet1_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 2, 1, 3),
    _A3ipxPolRteNet1_Type()
)
a3ipxPolRteNet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolRteNet1.setStatus("mandatory")
_A3ipxPolRteNet2_Type = IPXNET
_A3ipxPolRteNet2_Object = MibTableColumn
a3ipxPolRteNet2 = _A3ipxPolRteNet2_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 2, 1, 4),
    _A3ipxPolRteNet2_Type()
)
a3ipxPolRteNet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolRteNet2.setStatus("mandatory")
_A3ipxPolRteStatus_Type = RowStatus
_A3ipxPolRteStatus_Object = MibTableColumn
a3ipxPolRteStatus = _A3ipxPolRteStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 2, 1, 5),
    _A3ipxPolRteStatus_Type()
)
a3ipxPolRteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolRteStatus.setStatus("mandatory")
_A3ipxPolSvcTable_Object = MibTable
a3ipxPolSvcTable = _A3ipxPolSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 3)
)
if mibBuilder.loadTexts:
    a3ipxPolSvcTable.setStatus("mandatory")
_A3ipxPolSvcEntry_Object = MibTableRow
a3ipxPolSvcEntry = _A3ipxPolSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 3, 1)
)
a3ipxPolSvcEntry.setIndexNames(
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolSvcPort"),
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolSvcSvrName"),
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolSvcType"),
)
if mibBuilder.loadTexts:
    a3ipxPolSvcEntry.setStatus("mandatory")
_A3ipxPolSvcPort_Type = Integer32
_A3ipxPolSvcPort_Object = MibTableColumn
a3ipxPolSvcPort = _A3ipxPolSvcPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 3, 1, 1),
    _A3ipxPolSvcPort_Type()
)
a3ipxPolSvcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolSvcPort.setStatus("mandatory")


class _A3ipxPolSvcEntryType_Type(Integer32):
    """Custom type a3ipxPolSvcEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 1),
          ("both", 3),
          ("receive", 2))
    )


_A3ipxPolSvcEntryType_Type.__name__ = "Integer32"
_A3ipxPolSvcEntryType_Object = MibTableColumn
a3ipxPolSvcEntryType = _A3ipxPolSvcEntryType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 3, 1, 2),
    _A3ipxPolSvcEntryType_Type()
)
a3ipxPolSvcEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolSvcEntryType.setStatus("mandatory")


class _A3ipxPolSvcSvrName_Type(DisplayString):
    """Custom type a3ipxPolSvcSvrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_A3ipxPolSvcSvrName_Type.__name__ = "DisplayString"
_A3ipxPolSvcSvrName_Object = MibTableColumn
a3ipxPolSvcSvrName = _A3ipxPolSvcSvrName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 3, 1, 3),
    _A3ipxPolSvcSvrName_Type()
)
a3ipxPolSvcSvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolSvcSvrName.setStatus("mandatory")


class _A3ipxPolSvcType_Type(OctetString):
    """Custom type a3ipxPolSvcType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_A3ipxPolSvcType_Type.__name__ = "OctetString"
_A3ipxPolSvcType_Object = MibTableColumn
a3ipxPolSvcType = _A3ipxPolSvcType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 3, 1, 4),
    _A3ipxPolSvcType_Type()
)
a3ipxPolSvcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolSvcType.setStatus("mandatory")
_A3ipxPolSvcStatus_Type = RowStatus
_A3ipxPolSvcStatus_Object = MibTableColumn
a3ipxPolSvcStatus = _A3ipxPolSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 3, 1, 5),
    _A3ipxPolSvcStatus_Type()
)
a3ipxPolSvcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolSvcStatus.setStatus("mandatory")
_A3ipxPolNbrTable_Object = MibTable
a3ipxPolNbrTable = _A3ipxPolNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 4)
)
if mibBuilder.loadTexts:
    a3ipxPolNbrTable.setStatus("deprecated")
_A3ipxPolNbrEntry_Object = MibTableRow
a3ipxPolNbrEntry = _A3ipxPolNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 4, 1)
)
a3ipxPolNbrEntry.setIndexNames(
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolNbrPort"),
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolNbrNet"),
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolNbrAddress"),
)
if mibBuilder.loadTexts:
    a3ipxPolNbrEntry.setStatus("deprecated")
_A3ipxPolNbrPort_Type = Integer32
_A3ipxPolNbrPort_Object = MibTableColumn
a3ipxPolNbrPort = _A3ipxPolNbrPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 4, 1, 1),
    _A3ipxPolNbrPort_Type()
)
a3ipxPolNbrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolNbrPort.setStatus("deprecated")


class _A3ipxPolNbrType_Type(Integer32):
    """Custom type a3ipxPolNbrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 1),
          ("both", 3),
          ("receive", 2))
    )


_A3ipxPolNbrType_Type.__name__ = "Integer32"
_A3ipxPolNbrType_Object = MibTableColumn
a3ipxPolNbrType = _A3ipxPolNbrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 4, 1, 2),
    _A3ipxPolNbrType_Type()
)
a3ipxPolNbrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolNbrType.setStatus("deprecated")
_A3ipxPolNbrNet_Type = IPXNET
_A3ipxPolNbrNet_Object = MibTableColumn
a3ipxPolNbrNet = _A3ipxPolNbrNet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 4, 1, 3),
    _A3ipxPolNbrNet_Type()
)
a3ipxPolNbrNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolNbrNet.setStatus("deprecated")
_A3ipxPolNbrAddress_Type = MacAddress
_A3ipxPolNbrAddress_Object = MibTableColumn
a3ipxPolNbrAddress = _A3ipxPolNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 4, 1, 4),
    _A3ipxPolNbrAddress_Type()
)
a3ipxPolNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolNbrAddress.setStatus("deprecated")
_A3ipxPolNbrStatus_Type = RowStatus
_A3ipxPolNbrStatus_Object = MibTableColumn
a3ipxPolNbrStatus = _A3ipxPolNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 4, 1, 5),
    _A3ipxPolNbrStatus_Type()
)
a3ipxPolNbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolNbrStatus.setStatus("deprecated")
_A3ipxPolNbr_ObjectIdentity = ObjectIdentity
a3ipxPolNbr = _A3ipxPolNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5)
)
_A3ipxPolRipNbrCtlTable_Object = MibTable
a3ipxPolRipNbrCtlTable = _A3ipxPolRipNbrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 1)
)
if mibBuilder.loadTexts:
    a3ipxPolRipNbrCtlTable.setStatus("mandatory")
_A3ipxPolRipNbrCtlEntry_Object = MibTableRow
a3ipxPolRipNbrCtlEntry = _A3ipxPolRipNbrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 1, 1)
)
a3ipxPolRipNbrCtlEntry.setIndexNames(
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolRipNbrCtlPort"),
)
if mibBuilder.loadTexts:
    a3ipxPolRipNbrCtlEntry.setStatus("mandatory")
_A3ipxPolRipNbrCtlPort_Type = Integer32
_A3ipxPolRipNbrCtlPort_Object = MibTableColumn
a3ipxPolRipNbrCtlPort = _A3ipxPolRipNbrCtlPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 1, 1, 1),
    _A3ipxPolRipNbrCtlPort_Type()
)
a3ipxPolRipNbrCtlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolRipNbrCtlPort.setStatus("mandatory")


class _A3ipxPolRipNbrCtlAdvCtl_Type(Integer32):
    """Custom type a3ipxPolRipNbrCtlAdvCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_A3ipxPolRipNbrCtlAdvCtl_Type.__name__ = "Integer32"
_A3ipxPolRipNbrCtlAdvCtl_Object = MibTableColumn
a3ipxPolRipNbrCtlAdvCtl = _A3ipxPolRipNbrCtlAdvCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 1, 1, 2),
    _A3ipxPolRipNbrCtlAdvCtl_Type()
)
a3ipxPolRipNbrCtlAdvCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolRipNbrCtlAdvCtl.setStatus("mandatory")


class _A3ipxPolRipNbrCtlRcvCtl_Type(Integer32):
    """Custom type a3ipxPolRipNbrCtlRcvCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_A3ipxPolRipNbrCtlRcvCtl_Type.__name__ = "Integer32"
_A3ipxPolRipNbrCtlRcvCtl_Object = MibTableColumn
a3ipxPolRipNbrCtlRcvCtl = _A3ipxPolRipNbrCtlRcvCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 1, 1, 3),
    _A3ipxPolRipNbrCtlRcvCtl_Type()
)
a3ipxPolRipNbrCtlRcvCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolRipNbrCtlRcvCtl.setStatus("mandatory")


class _A3ipxPolRipNbrCtlRcvType_Type(Integer32):
    """Custom type a3ipxPolRipNbrCtlRcvType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverse", 2),
          ("normal", 1))
    )


_A3ipxPolRipNbrCtlRcvType_Type.__name__ = "Integer32"
_A3ipxPolRipNbrCtlRcvType_Object = MibTableColumn
a3ipxPolRipNbrCtlRcvType = _A3ipxPolRipNbrCtlRcvType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 1, 1, 4),
    _A3ipxPolRipNbrCtlRcvType_Type()
)
a3ipxPolRipNbrCtlRcvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolRipNbrCtlRcvType.setStatus("mandatory")
_A3ipxPolRipNbrTable_Object = MibTable
a3ipxPolRipNbrTable = _A3ipxPolRipNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 2)
)
if mibBuilder.loadTexts:
    a3ipxPolRipNbrTable.setStatus("mandatory")
_A3ipxPolRipNbrEntry_Object = MibTableRow
a3ipxPolRipNbrEntry = _A3ipxPolRipNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 2, 1)
)
a3ipxPolRipNbrEntry.setIndexNames(
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolRipNbrPort"),
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolRipNbrNet"),
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolRipNbrAddress"),
)
if mibBuilder.loadTexts:
    a3ipxPolRipNbrEntry.setStatus("mandatory")
_A3ipxPolRipNbrPort_Type = Integer32
_A3ipxPolRipNbrPort_Object = MibTableColumn
a3ipxPolRipNbrPort = _A3ipxPolRipNbrPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 2, 1, 1),
    _A3ipxPolRipNbrPort_Type()
)
a3ipxPolRipNbrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolRipNbrPort.setStatus("mandatory")


class _A3ipxPolRipNbrType_Type(Integer32):
    """Custom type a3ipxPolRipNbrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 1),
          ("both", 3),
          ("receive", 2))
    )


_A3ipxPolRipNbrType_Type.__name__ = "Integer32"
_A3ipxPolRipNbrType_Object = MibTableColumn
a3ipxPolRipNbrType = _A3ipxPolRipNbrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 2, 1, 2),
    _A3ipxPolRipNbrType_Type()
)
a3ipxPolRipNbrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolRipNbrType.setStatus("mandatory")
_A3ipxPolRipNbrNet_Type = IPXNET
_A3ipxPolRipNbrNet_Object = MibTableColumn
a3ipxPolRipNbrNet = _A3ipxPolRipNbrNet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 2, 1, 3),
    _A3ipxPolRipNbrNet_Type()
)
a3ipxPolRipNbrNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolRipNbrNet.setStatus("mandatory")
_A3ipxPolRipNbrAddress_Type = MacAddress
_A3ipxPolRipNbrAddress_Object = MibTableColumn
a3ipxPolRipNbrAddress = _A3ipxPolRipNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 2, 1, 4),
    _A3ipxPolRipNbrAddress_Type()
)
a3ipxPolRipNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolRipNbrAddress.setStatus("mandatory")
_A3ipxPolRipNbrStatus_Type = RowStatus
_A3ipxPolRipNbrStatus_Object = MibTableColumn
a3ipxPolRipNbrStatus = _A3ipxPolRipNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 2, 1, 5),
    _A3ipxPolRipNbrStatus_Type()
)
a3ipxPolRipNbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolRipNbrStatus.setStatus("mandatory")
_A3ipxPolSapNbrCtlTable_Object = MibTable
a3ipxPolSapNbrCtlTable = _A3ipxPolSapNbrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 3)
)
if mibBuilder.loadTexts:
    a3ipxPolSapNbrCtlTable.setStatus("mandatory")
_A3ipxPolSapNbrCtlEntry_Object = MibTableRow
a3ipxPolSapNbrCtlEntry = _A3ipxPolSapNbrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 3, 1)
)
a3ipxPolSapNbrCtlEntry.setIndexNames(
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolSapNbrCtlPort"),
)
if mibBuilder.loadTexts:
    a3ipxPolSapNbrCtlEntry.setStatus("mandatory")
_A3ipxPolSapNbrCtlPort_Type = Integer32
_A3ipxPolSapNbrCtlPort_Object = MibTableColumn
a3ipxPolSapNbrCtlPort = _A3ipxPolSapNbrCtlPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 3, 1, 1),
    _A3ipxPolSapNbrCtlPort_Type()
)
a3ipxPolSapNbrCtlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolSapNbrCtlPort.setStatus("mandatory")


class _A3ipxPolSapNbrCtlAdvCtl_Type(Integer32):
    """Custom type a3ipxPolSapNbrCtlAdvCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_A3ipxPolSapNbrCtlAdvCtl_Type.__name__ = "Integer32"
_A3ipxPolSapNbrCtlAdvCtl_Object = MibTableColumn
a3ipxPolSapNbrCtlAdvCtl = _A3ipxPolSapNbrCtlAdvCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 3, 1, 2),
    _A3ipxPolSapNbrCtlAdvCtl_Type()
)
a3ipxPolSapNbrCtlAdvCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolSapNbrCtlAdvCtl.setStatus("mandatory")


class _A3ipxPolSapNbrCtlRcvCtl_Type(Integer32):
    """Custom type a3ipxPolSapNbrCtlRcvCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_A3ipxPolSapNbrCtlRcvCtl_Type.__name__ = "Integer32"
_A3ipxPolSapNbrCtlRcvCtl_Object = MibTableColumn
a3ipxPolSapNbrCtlRcvCtl = _A3ipxPolSapNbrCtlRcvCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 3, 1, 3),
    _A3ipxPolSapNbrCtlRcvCtl_Type()
)
a3ipxPolSapNbrCtlRcvCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolSapNbrCtlRcvCtl.setStatus("mandatory")


class _A3ipxPolSapNbrCtlRcvType_Type(Integer32):
    """Custom type a3ipxPolSapNbrCtlRcvType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverse", 2),
          ("normal", 1))
    )


_A3ipxPolSapNbrCtlRcvType_Type.__name__ = "Integer32"
_A3ipxPolSapNbrCtlRcvType_Object = MibTableColumn
a3ipxPolSapNbrCtlRcvType = _A3ipxPolSapNbrCtlRcvType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 3, 1, 4),
    _A3ipxPolSapNbrCtlRcvType_Type()
)
a3ipxPolSapNbrCtlRcvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolSapNbrCtlRcvType.setStatus("mandatory")
_A3ipxPolSapNbrTable_Object = MibTable
a3ipxPolSapNbrTable = _A3ipxPolSapNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 4)
)
if mibBuilder.loadTexts:
    a3ipxPolSapNbrTable.setStatus("mandatory")
_A3ipxPolSapNbrEntry_Object = MibTableRow
a3ipxPolSapNbrEntry = _A3ipxPolSapNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 4, 1)
)
a3ipxPolSapNbrEntry.setIndexNames(
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolSapNbrPort"),
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolSapNbrNet"),
    (0, "A3COM-IPXPOLICY-R3-MIB", "a3ipxPolSapNbrAddress"),
)
if mibBuilder.loadTexts:
    a3ipxPolSapNbrEntry.setStatus("mandatory")
_A3ipxPolSapNbrPort_Type = Integer32
_A3ipxPolSapNbrPort_Object = MibTableColumn
a3ipxPolSapNbrPort = _A3ipxPolSapNbrPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 4, 1, 1),
    _A3ipxPolSapNbrPort_Type()
)
a3ipxPolSapNbrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolSapNbrPort.setStatus("mandatory")


class _A3ipxPolSapNbrType_Type(Integer32):
    """Custom type a3ipxPolSapNbrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 1),
          ("both", 3),
          ("receive", 2))
    )


_A3ipxPolSapNbrType_Type.__name__ = "Integer32"
_A3ipxPolSapNbrType_Object = MibTableColumn
a3ipxPolSapNbrType = _A3ipxPolSapNbrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 4, 1, 2),
    _A3ipxPolSapNbrType_Type()
)
a3ipxPolSapNbrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolSapNbrType.setStatus("mandatory")
_A3ipxPolSapNbrNet_Type = IPXNET
_A3ipxPolSapNbrNet_Object = MibTableColumn
a3ipxPolSapNbrNet = _A3ipxPolSapNbrNet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 4, 1, 3),
    _A3ipxPolSapNbrNet_Type()
)
a3ipxPolSapNbrNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolSapNbrNet.setStatus("mandatory")
_A3ipxPolSapNbrAddress_Type = MacAddress
_A3ipxPolSapNbrAddress_Object = MibTableColumn
a3ipxPolSapNbrAddress = _A3ipxPolSapNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 4, 1, 4),
    _A3ipxPolSapNbrAddress_Type()
)
a3ipxPolSapNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPolSapNbrAddress.setStatus("mandatory")
_A3ipxPolSapNbrStatus_Type = RowStatus
_A3ipxPolSapNbrStatus_Object = MibTableColumn
a3ipxPolSapNbrStatus = _A3ipxPolSapNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 11, 5, 4, 1, 5),
    _A3ipxPolSapNbrStatus_Type()
)
a3ipxPolSapNbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPolSapNbrStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-IPXPOLICY-R3-MIB",
    **{"RowStatus": RowStatus,
       "IPXNET": IPXNET,
       "a3Com": a3Com,
       "brouterMIB": brouterMIB,
       "a3ComIPXpol": a3ComIPXpol,
       "a3ipxPolControlTable": a3ipxPolControlTable,
       "a3ipxPolControlEntry": a3ipxPolControlEntry,
       "a3ipxPCPort": a3ipxPCPort,
       "a3ipxPCRteAdvCtl": a3ipxPCRteAdvCtl,
       "a3ipxPCRteAdvType": a3ipxPCRteAdvType,
       "a3ipxPCRteRcvCtl": a3ipxPCRteRcvCtl,
       "a3ipxPCRteRcvType": a3ipxPCRteRcvType,
       "a3ipxPCSvcAdvCtl": a3ipxPCSvcAdvCtl,
       "a3ipxPCSvcAdvType": a3ipxPCSvcAdvType,
       "a3ipxPCSvcRcvCtl": a3ipxPCSvcRcvCtl,
       "a3ipxPCSvcRcvType": a3ipxPCSvcRcvType,
       "a3ipxPCNbrAdvCtl": a3ipxPCNbrAdvCtl,
       "a3ipxPCNbrRcvCtl": a3ipxPCNbrRcvCtl,
       "a3ipxPCNbrRcvType": a3ipxPCNbrRcvType,
       "a3ipxPCPolicyOverride": a3ipxPCPolicyOverride,
       "a3ipxPCSvrRplyCtl": a3ipxPCSvrRplyCtl,
       "a3ipxPCRipPolOverride": a3ipxPCRipPolOverride,
       "a3ipxPCSapPolOverride": a3ipxPCSapPolOverride,
       "a3ipxPolRteTable": a3ipxPolRteTable,
       "a3ipxPolRteEntry": a3ipxPolRteEntry,
       "a3ipxPolRtePort": a3ipxPolRtePort,
       "a3ipxPolRteType": a3ipxPolRteType,
       "a3ipxPolRteNet1": a3ipxPolRteNet1,
       "a3ipxPolRteNet2": a3ipxPolRteNet2,
       "a3ipxPolRteStatus": a3ipxPolRteStatus,
       "a3ipxPolSvcTable": a3ipxPolSvcTable,
       "a3ipxPolSvcEntry": a3ipxPolSvcEntry,
       "a3ipxPolSvcPort": a3ipxPolSvcPort,
       "a3ipxPolSvcEntryType": a3ipxPolSvcEntryType,
       "a3ipxPolSvcSvrName": a3ipxPolSvcSvrName,
       "a3ipxPolSvcType": a3ipxPolSvcType,
       "a3ipxPolSvcStatus": a3ipxPolSvcStatus,
       "a3ipxPolNbrTable": a3ipxPolNbrTable,
       "a3ipxPolNbrEntry": a3ipxPolNbrEntry,
       "a3ipxPolNbrPort": a3ipxPolNbrPort,
       "a3ipxPolNbrType": a3ipxPolNbrType,
       "a3ipxPolNbrNet": a3ipxPolNbrNet,
       "a3ipxPolNbrAddress": a3ipxPolNbrAddress,
       "a3ipxPolNbrStatus": a3ipxPolNbrStatus,
       "a3ipxPolNbr": a3ipxPolNbr,
       "a3ipxPolRipNbrCtlTable": a3ipxPolRipNbrCtlTable,
       "a3ipxPolRipNbrCtlEntry": a3ipxPolRipNbrCtlEntry,
       "a3ipxPolRipNbrCtlPort": a3ipxPolRipNbrCtlPort,
       "a3ipxPolRipNbrCtlAdvCtl": a3ipxPolRipNbrCtlAdvCtl,
       "a3ipxPolRipNbrCtlRcvCtl": a3ipxPolRipNbrCtlRcvCtl,
       "a3ipxPolRipNbrCtlRcvType": a3ipxPolRipNbrCtlRcvType,
       "a3ipxPolRipNbrTable": a3ipxPolRipNbrTable,
       "a3ipxPolRipNbrEntry": a3ipxPolRipNbrEntry,
       "a3ipxPolRipNbrPort": a3ipxPolRipNbrPort,
       "a3ipxPolRipNbrType": a3ipxPolRipNbrType,
       "a3ipxPolRipNbrNet": a3ipxPolRipNbrNet,
       "a3ipxPolRipNbrAddress": a3ipxPolRipNbrAddress,
       "a3ipxPolRipNbrStatus": a3ipxPolRipNbrStatus,
       "a3ipxPolSapNbrCtlTable": a3ipxPolSapNbrCtlTable,
       "a3ipxPolSapNbrCtlEntry": a3ipxPolSapNbrCtlEntry,
       "a3ipxPolSapNbrCtlPort": a3ipxPolSapNbrCtlPort,
       "a3ipxPolSapNbrCtlAdvCtl": a3ipxPolSapNbrCtlAdvCtl,
       "a3ipxPolSapNbrCtlRcvCtl": a3ipxPolSapNbrCtlRcvCtl,
       "a3ipxPolSapNbrCtlRcvType": a3ipxPolSapNbrCtlRcvType,
       "a3ipxPolSapNbrTable": a3ipxPolSapNbrTable,
       "a3ipxPolSapNbrEntry": a3ipxPolSapNbrEntry,
       "a3ipxPolSapNbrPort": a3ipxPolSapNbrPort,
       "a3ipxPolSapNbrType": a3ipxPolSapNbrType,
       "a3ipxPolSapNbrNet": a3ipxPolSapNbrNet,
       "a3ipxPolSapNbrAddress": a3ipxPolSapNbrAddress,
       "a3ipxPolSapNbrStatus": a3ipxPolSapNbrStatus}
)
