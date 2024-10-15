# SNMP MIB module (A3COM-IPEXTNS-R5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-IPEXTNS-R5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:34 2024
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



class SMDSAddress(OctetString):
    """Custom type SMDSAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





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
_A3ComIPextns_ObjectIdentity = ObjectIdentity
a3ComIPextns = _A3ComIPextns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 6)
)


class _A3IPextMode_Type(Integer32):
    """Custom type a3IPextMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleNet", 1),
          ("singleNet", 2))
    )


_A3IPextMode_Type.__name__ = "Integer32"
_A3IPextMode_Object = MibScalar
a3IPextMode = _A3IPextMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 1),
    _A3IPextMode_Type()
)
a3IPextMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPextMode.setStatus("mandatory")


class _A3IPextFlushCtl_Type(Integer32):
    """Custom type a3IPextFlushCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flushARP", 3),
          ("flushRoutes", 2),
          ("other", 1))
    )


_A3IPextFlushCtl_Type.__name__ = "Integer32"
_A3IPextFlushCtl_Object = MibScalar
a3IPextFlushCtl = _A3IPextFlushCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 2),
    _A3IPextFlushCtl_Type()
)
a3IPextFlushCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPextFlushCtl.setStatus("mandatory")


class _A3IPextRelaySrcRteCtl_Type(Integer32):
    """Custom type a3IPextRelaySrcRteCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("relay", 1))
    )


_A3IPextRelaySrcRteCtl_Type.__name__ = "Integer32"
_A3IPextRelaySrcRteCtl_Object = MibScalar
a3IPextRelaySrcRteCtl = _A3IPextRelaySrcRteCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 3),
    _A3IPextRelaySrcRteCtl_Type()
)
a3IPextRelaySrcRteCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPextRelaySrcRteCtl.setStatus("mandatory")


class _A3IPextSplitLoadCtl_Type(Integer32):
    """Custom type a3IPextSplitLoadCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSplit", 2),
          ("split", 1))
    )


_A3IPextSplitLoadCtl_Type.__name__ = "Integer32"
_A3IPextSplitLoadCtl_Object = MibScalar
a3IPextSplitLoadCtl = _A3IPextSplitLoadCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 4),
    _A3IPextSplitLoadCtl_Type()
)
a3IPextSplitLoadCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPextSplitLoadCtl.setStatus("mandatory")


class _A3IPicmpInfoCtl_Type(Integer32):
    """Custom type a3IPicmpInfoCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("info", 1),
          ("noInfo", 2))
    )


_A3IPicmpInfoCtl_Type.__name__ = "Integer32"
_A3IPicmpInfoCtl_Object = MibScalar
a3IPicmpInfoCtl = _A3IPicmpInfoCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 5),
    _A3IPicmpInfoCtl_Type()
)
a3IPicmpInfoCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPicmpInfoCtl.setStatus("mandatory")


class _A3IPicmpMaskCtl_Type(Integer32):
    """Custom type a3IPicmpMaskCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("noMask", 2))
    )


_A3IPicmpMaskCtl_Type.__name__ = "Integer32"
_A3IPicmpMaskCtl_Object = MibScalar
a3IPicmpMaskCtl = _A3IPicmpMaskCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 6),
    _A3IPicmpMaskCtl_Type()
)
a3IPicmpMaskCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPicmpMaskCtl.setStatus("mandatory")
_A3IPntmExtTable_Object = MibTable
a3IPntmExtTable = _A3IPntmExtTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 7)
)
if mibBuilder.loadTexts:
    a3IPntmExtTable.setStatus("mandatory")
_A3IPntmExtEntry_Object = MibTableRow
a3IPntmExtEntry = _A3IPntmExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1)
)
a3IPntmExtEntry.setIndexNames(
    (0, "A3COM-IPEXTNS-R5-MIB", "a3IPntmIfIndex"),
    (0, "A3COM-IPEXTNS-R5-MIB", "a3IPntmNetAddress"),
)
if mibBuilder.loadTexts:
    a3IPntmExtEntry.setStatus("mandatory")
_A3IPntmIfIndex_Type = Integer32
_A3IPntmIfIndex_Object = MibTableColumn
a3IPntmIfIndex = _A3IPntmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1, 1),
    _A3IPntmIfIndex_Type()
)
a3IPntmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPntmIfIndex.setStatus("mandatory")
_A3IPntmNetAddress_Type = IpAddress
_A3IPntmNetAddress_Object = MibTableColumn
a3IPntmNetAddress = _A3IPntmNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1, 2),
    _A3IPntmNetAddress_Type()
)
a3IPntmNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPntmNetAddress.setStatus("mandatory")


class _A3IPntmHdrFormat_Type(Integer32):
    """Custom type a3IPntmHdrFormat based on Integer32"""
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
        *(("ethernet", 2),
          ("ieee", 3),
          ("other", 1),
          ("snap", 4))
    )


_A3IPntmHdrFormat_Type.__name__ = "Integer32"
_A3IPntmHdrFormat_Object = MibTableColumn
a3IPntmHdrFormat = _A3IPntmHdrFormat_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1, 3),
    _A3IPntmHdrFormat_Type()
)
a3IPntmHdrFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPntmHdrFormat.setStatus("mandatory")


class _A3IPntmProxyArp_Type(Integer32):
    """Custom type a3IPntmProxyArp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noProxy", 2),
          ("proxy", 1))
    )


_A3IPntmProxyArp_Type.__name__ = "Integer32"
_A3IPntmProxyArp_Object = MibTableColumn
a3IPntmProxyArp = _A3IPntmProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1, 4),
    _A3IPntmProxyArp_Type()
)
a3IPntmProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPntmProxyArp.setStatus("mandatory")
_A3IPaddrConfigTable_Object = MibTable
a3IPaddrConfigTable = _A3IPaddrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 8)
)
if mibBuilder.loadTexts:
    a3IPaddrConfigTable.setStatus("mandatory")
_A3IPaddrConfigEntry_Object = MibTableRow
a3IPaddrConfigEntry = _A3IPaddrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1)
)
a3IPaddrConfigEntry.setIndexNames(
    (0, "A3COM-IPEXTNS-R5-MIB", "a3IPaddrConfigPort"),
    (0, "A3COM-IPEXTNS-R5-MIB", "a3IPaddrConfigAddr"),
)
if mibBuilder.loadTexts:
    a3IPaddrConfigEntry.setStatus("mandatory")
_A3IPaddrConfigPort_Type = Integer32
_A3IPaddrConfigPort_Object = MibTableColumn
a3IPaddrConfigPort = _A3IPaddrConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 1),
    _A3IPaddrConfigPort_Type()
)
a3IPaddrConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPaddrConfigPort.setStatus("mandatory")
_A3IPaddrConfigAddr_Type = IpAddress
_A3IPaddrConfigAddr_Object = MibTableColumn
a3IPaddrConfigAddr = _A3IPaddrConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 2),
    _A3IPaddrConfigAddr_Type()
)
a3IPaddrConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPaddrConfigAddr.setStatus("mandatory")


class _A3IPaddrConfigType_Type(Integer32):
    """Custom type a3IPaddrConfigType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_A3IPaddrConfigType_Type.__name__ = "Integer32"
_A3IPaddrConfigType_Object = MibTableColumn
a3IPaddrConfigType = _A3IPaddrConfigType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 3),
    _A3IPaddrConfigType_Type()
)
a3IPaddrConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPaddrConfigType.setStatus("mandatory")
_A3IPaddrConfigNetMask_Type = IpAddress
_A3IPaddrConfigNetMask_Object = MibTableColumn
a3IPaddrConfigNetMask = _A3IPaddrConfigNetMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 4),
    _A3IPaddrConfigNetMask_Type()
)
a3IPaddrConfigNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPaddrConfigNetMask.setStatus("mandatory")


class _A3IPaddrConfigBcastAddr_Type(Integer32):
    """Custom type a3IPaddrConfigBcastAddr based on Integer32"""
    defaultValue = 1


_A3IPaddrConfigBcastAddr_Object = MibTableColumn
a3IPaddrConfigBcastAddr = _A3IPaddrConfigBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 5),
    _A3IPaddrConfigBcastAddr_Type()
)
a3IPaddrConfigBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPaddrConfigBcastAddr.setStatus("mandatory")


class _A3IPaddrConfigMtu_Type(Integer32):
    """Custom type a3IPaddrConfigMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 32767),
    )


_A3IPaddrConfigMtu_Type.__name__ = "Integer32"
_A3IPaddrConfigMtu_Object = MibTableColumn
a3IPaddrConfigMtu = _A3IPaddrConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 6),
    _A3IPaddrConfigMtu_Type()
)
a3IPaddrConfigMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPaddrConfigMtu.setStatus("mandatory")
_A3IPaddrConfigStatus_Type = RowStatus
_A3IPaddrConfigStatus_Object = MibTableColumn
a3IPaddrConfigStatus = _A3IPaddrConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 7),
    _A3IPaddrConfigStatus_Type()
)
a3IPaddrConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPaddrConfigStatus.setStatus("mandatory")
_A3IPforwardExtTable_Object = MibTable
a3IPforwardExtTable = _A3IPforwardExtTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 9)
)
if mibBuilder.loadTexts:
    a3IPforwardExtTable.setStatus("mandatory")
_A3IPforwardExtEntry_Object = MibTableRow
a3IPforwardExtEntry = _A3IPforwardExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1)
)
a3IPforwardExtEntry.setIndexNames(
    (0, "A3COM-IPEXTNS-R5-MIB", "a3IPforwardExtDest"),
    (0, "A3COM-IPEXTNS-R5-MIB", "a3IPforwardExtProto"),
    (0, "A3COM-IPEXTNS-R5-MIB", "a3IPforwardExtPolicy"),
    (0, "A3COM-IPEXTNS-R5-MIB", "a3IPforwardExtNextHop"),
)
if mibBuilder.loadTexts:
    a3IPforwardExtEntry.setStatus("mandatory")
_A3IPforwardExtDest_Type = IpAddress
_A3IPforwardExtDest_Object = MibTableColumn
a3IPforwardExtDest = _A3IPforwardExtDest_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 1),
    _A3IPforwardExtDest_Type()
)
a3IPforwardExtDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPforwardExtDest.setStatus("mandatory")


class _A3IPforwardExtProto_Type(Integer32):
    """Custom type a3IPforwardExtProto based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("es-is", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("idpr", 15),
          ("is-is", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_A3IPforwardExtProto_Type.__name__ = "Integer32"
_A3IPforwardExtProto_Object = MibTableColumn
a3IPforwardExtProto = _A3IPforwardExtProto_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 2),
    _A3IPforwardExtProto_Type()
)
a3IPforwardExtProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPforwardExtProto.setStatus("mandatory")
_A3IPforwardExtPolicy_Type = Integer32
_A3IPforwardExtPolicy_Object = MibTableColumn
a3IPforwardExtPolicy = _A3IPforwardExtPolicy_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 3),
    _A3IPforwardExtPolicy_Type()
)
a3IPforwardExtPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPforwardExtPolicy.setStatus("mandatory")
_A3IPforwardExtNextHop_Type = IpAddress
_A3IPforwardExtNextHop_Object = MibTableColumn
a3IPforwardExtNextHop = _A3IPforwardExtNextHop_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 4),
    _A3IPforwardExtNextHop_Type()
)
a3IPforwardExtNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPforwardExtNextHop.setStatus("mandatory")


class _A3IPforwardExtOverride_Type(Integer32):
    """Custom type a3IPforwardExtOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOverride", 2),
          ("override", 1))
    )


_A3IPforwardExtOverride_Type.__name__ = "Integer32"
_A3IPforwardExtOverride_Object = MibTableColumn
a3IPforwardExtOverride = _A3IPforwardExtOverride_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 5),
    _A3IPforwardExtOverride_Type()
)
a3IPforwardExtOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPforwardExtOverride.setStatus("mandatory")


class _A3IParpOverBlocked_Type(Integer32):
    """Custom type a3IParpOverBlocked based on Integer32"""
    defaultValue = 2

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


_A3IParpOverBlocked_Type.__name__ = "Integer32"
_A3IParpOverBlocked_Object = MibScalar
a3IParpOverBlocked = _A3IParpOverBlocked_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 10),
    _A3IParpOverBlocked_Type()
)
a3IParpOverBlocked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IParpOverBlocked.setStatus("mandatory")


class _A3IPrarpClientCtl_Type(Integer32):
    """Custom type a3IPrarpClientCtl based on Integer32"""
    defaultValue = 2

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


_A3IPrarpClientCtl_Type.__name__ = "Integer32"
_A3IPrarpClientCtl_Object = MibScalar
a3IPrarpClientCtl = _A3IPrarpClientCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 11),
    _A3IPrarpClientCtl_Type()
)
a3IPrarpClientCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPrarpClientCtl.setStatus("mandatory")


class _A3IPrarpServerCtl_Type(Integer32):
    """Custom type a3IPrarpServerCtl based on Integer32"""
    defaultValue = 2

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


_A3IPrarpServerCtl_Type.__name__ = "Integer32"
_A3IPrarpServerCtl_Object = MibScalar
a3IPrarpServerCtl = _A3IPrarpServerCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 12),
    _A3IPrarpServerCtl_Type()
)
a3IPrarpServerCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPrarpServerCtl.setStatus("mandatory")
_A3IParpConfigTable_Object = MibTable
a3IParpConfigTable = _A3IParpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 13)
)
if mibBuilder.loadTexts:
    a3IParpConfigTable.setStatus("mandatory")
_A3IParpConfigEntry_Object = MibTableRow
a3IParpConfigEntry = _A3IParpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1)
)
a3IParpConfigEntry.setIndexNames(
    (0, "A3COM-IPEXTNS-R5-MIB", "a3IParpPortIndex"),
)
if mibBuilder.loadTexts:
    a3IParpConfigEntry.setStatus("mandatory")
_A3IParpPortIndex_Type = Integer32
_A3IParpPortIndex_Object = MibTableColumn
a3IParpPortIndex = _A3IParpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 1),
    _A3IParpPortIndex_Type()
)
a3IParpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IParpPortIndex.setStatus("mandatory")


class _A3IParpProxyCtl_Type(Integer32):
    """Custom type a3IParpProxyCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noProxy", 2),
          ("proxy", 1))
    )


_A3IParpProxyCtl_Type.__name__ = "Integer32"
_A3IParpProxyCtl_Object = MibTableColumn
a3IParpProxyCtl = _A3IParpProxyCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 2),
    _A3IParpProxyCtl_Type()
)
a3IParpProxyCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IParpProxyCtl.setStatus("mandatory")


class _A3IParpHoldTime_Type(Integer32):
    """Custom type a3IParpHoldTime based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_A3IParpHoldTime_Type.__name__ = "Integer32"
_A3IParpHoldTime_Object = MibTableColumn
a3IParpHoldTime = _A3IParpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 3),
    _A3IParpHoldTime_Type()
)
a3IParpHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IParpHoldTime.setStatus("mandatory")


class _A3IParpReqFormat_Type(Integer32):
    """Custom type a3IParpReqFormat based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              128,
              129,
              130,
              131)
        )
    )
    namedValues = NamedValues(
        *(("auto", 128),
          ("both", 3),
          ("bothAuto", 131),
          ("ethAuto", 129),
          ("ethernet", 1),
          ("snap", 2),
          ("snapAuto", 130))
    )


_A3IParpReqFormat_Type.__name__ = "Integer32"
_A3IParpReqFormat_Object = MibTableColumn
a3IParpReqFormat = _A3IParpReqFormat_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 4),
    _A3IParpReqFormat_Type()
)
a3IParpReqFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IParpReqFormat.setStatus("mandatory")
_A3IParpRemAddr_Type = IpAddress
_A3IParpRemAddr_Object = MibTableColumn
a3IParpRemAddr = _A3IParpRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 5),
    _A3IParpRemAddr_Type()
)
a3IParpRemAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IParpRemAddr.setStatus("mandatory")


class _A3IParpInvCtl_Type(Integer32):
    """Custom type a3IParpInvCtl based on Integer32"""
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


_A3IParpInvCtl_Type.__name__ = "Integer32"
_A3IParpInvCtl_Object = MibTableColumn
a3IParpInvCtl = _A3IParpInvCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 6),
    _A3IParpInvCtl_Type()
)
a3IParpInvCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IParpInvCtl.setStatus("mandatory")
_A3IPsmdsGaTable_Object = MibTable
a3IPsmdsGaTable = _A3IPsmdsGaTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 14)
)
if mibBuilder.loadTexts:
    a3IPsmdsGaTable.setStatus("mandatory")
_A3IPsmdsGaEntry_Object = MibTableRow
a3IPsmdsGaEntry = _A3IPsmdsGaEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 14, 1)
)
a3IPsmdsGaEntry.setIndexNames(
    (0, "A3COM-IPEXTNS-R5-MIB", "a3IPsmdsGaIpNet"),
)
if mibBuilder.loadTexts:
    a3IPsmdsGaEntry.setStatus("mandatory")
_A3IPsmdsGaIpNet_Type = IpAddress
_A3IPsmdsGaIpNet_Object = MibTableColumn
a3IPsmdsGaIpNet = _A3IPsmdsGaIpNet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 14, 1, 1),
    _A3IPsmdsGaIpNet_Type()
)
a3IPsmdsGaIpNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPsmdsGaIpNet.setStatus("mandatory")
_A3IPsmdsGa_Type = SMDSAddress
_A3IPsmdsGa_Object = MibTableColumn
a3IPsmdsGa = _A3IPsmdsGa_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 14, 1, 2),
    _A3IPsmdsGa_Type()
)
a3IPsmdsGa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsmdsGa.setStatus("mandatory")
_A3IPsmdsGaStatus_Type = RowStatus
_A3IPsmdsGaStatus_Object = MibTableColumn
a3IPsmdsGaStatus = _A3IPsmdsGaStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 14, 1, 3),
    _A3IPsmdsGaStatus_Type()
)
a3IPsmdsGaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsmdsGaStatus.setStatus("mandatory")
_A3IPx25configTable_Object = MibTable
a3IPx25configTable = _A3IPx25configTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 15)
)
if mibBuilder.loadTexts:
    a3IPx25configTable.setStatus("mandatory")
_A3IPx25configEntry_Object = MibTableRow
a3IPx25configEntry = _A3IPx25configEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1)
)
a3IPx25configEntry.setIndexNames(
    (0, "A3COM-IPEXTNS-R5-MIB", "a3IPx25configPort"),
)
if mibBuilder.loadTexts:
    a3IPx25configEntry.setStatus("mandatory")
_A3IPx25configPort_Type = Integer32
_A3IPx25configPort_Object = MibTableColumn
a3IPx25configPort = _A3IPx25configPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 1),
    _A3IPx25configPort_Type()
)
a3IPx25configPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPx25configPort.setStatus("mandatory")


class _A3IPx25configPID_Type(Integer32):
    """Custom type a3IPx25configPID based on Integer32"""
    defaultHexValue = 204

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A3IPx25configPID_Type.__name__ = "Integer32"
_A3IPx25configPID_Object = MibTableColumn
a3IPx25configPID = _A3IPx25configPID_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 2),
    _A3IPx25configPID_Type()
)
a3IPx25configPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPx25configPID.setStatus("mandatory")


class _A3IPx25configQueueSize_Type(Integer32):
    """Custom type a3IPx25configQueueSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_A3IPx25configQueueSize_Type.__name__ = "Integer32"
_A3IPx25configQueueSize_Object = MibTableColumn
a3IPx25configQueueSize = _A3IPx25configQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 3),
    _A3IPx25configQueueSize_Type()
)
a3IPx25configQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPx25configQueueSize.setStatus("deprecated")


class _A3IPx25configVClimit_Type(Integer32):
    """Custom type a3IPx25configVClimit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3IPx25configVClimit_Type.__name__ = "Integer32"
_A3IPx25configVClimit_Object = MibTableColumn
a3IPx25configVClimit = _A3IPx25configVClimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 4),
    _A3IPx25configVClimit_Type()
)
a3IPx25configVClimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPx25configVClimit.setStatus("deprecated")


class _A3IPx25configVCtimer_Type(Integer32):
    """Custom type a3IPx25configVCtimer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_A3IPx25configVCtimer_Type.__name__ = "Integer32"
_A3IPx25configVCtimer_Object = MibTableColumn
a3IPx25configVCtimer = _A3IPx25configVCtimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 5),
    _A3IPx25configVCtimer_Type()
)
a3IPx25configVCtimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPx25configVCtimer.setStatus("deprecated")


class _A3IPx25configProfID_Type(Integer32):
    """Custom type a3IPx25configProfID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A3IPx25configProfID_Type.__name__ = "Integer32"
_A3IPx25configProfID_Object = MibTableColumn
a3IPx25configProfID = _A3IPx25configProfID_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 6),
    _A3IPx25configProfID_Type()
)
a3IPx25configProfID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPx25configProfID.setStatus("mandatory")


class _A3IPqueuePriority_Type(Integer32):
    """Custom type a3IPqueuePriority based on Integer32"""
    defaultValue = 2

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
        *(("default", 4),
          ("high", 1),
          ("low", 3),
          ("medium", 2),
          ("unknown", 5))
    )


_A3IPqueuePriority_Type.__name__ = "Integer32"
_A3IPqueuePriority_Object = MibScalar
a3IPqueuePriority = _A3IPqueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 16),
    _A3IPqueuePriority_Type()
)
a3IPqueuePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPqueuePriority.setStatus("mandatory")


class _A3IPfwdSubnetBcast_Type(Integer32):
    """Custom type a3IPfwdSubnetBcast based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fwdSubnetBcast", 1),
          ("noFwdSubnetBcast", 2))
    )


_A3IPfwdSubnetBcast_Type.__name__ = "Integer32"
_A3IPfwdSubnetBcast_Object = MibScalar
a3IPfwdSubnetBcast = _A3IPfwdSubnetBcast_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 17),
    _A3IPfwdSubnetBcast_Type()
)
a3IPfwdSubnetBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPfwdSubnetBcast.setStatus("mandatory")
_A3IPicmpGenTable_Object = MibTable
a3IPicmpGenTable = _A3IPicmpGenTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 18)
)
if mibBuilder.loadTexts:
    a3IPicmpGenTable.setStatus("mandatory")
_A3IPicmpGenEntry_Object = MibTableRow
a3IPicmpGenEntry = _A3IPicmpGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1)
)
a3IPicmpGenEntry.setIndexNames(
    (0, "A3COM-IPEXTNS-R5-MIB", "a3IPicmpGenIfIndex"),
)
if mibBuilder.loadTexts:
    a3IPicmpGenEntry.setStatus("mandatory")
_A3IPicmpGenIfIndex_Type = Integer32
_A3IPicmpGenIfIndex_Object = MibTableColumn
a3IPicmpGenIfIndex = _A3IPicmpGenIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1, 1),
    _A3IPicmpGenIfIndex_Type()
)
a3IPicmpGenIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPicmpGenIfIndex.setStatus("mandatory")


class _A3IPicmpGenRedirect_Type(Integer32):
    """Custom type a3IPicmpGenRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRedirect", 2),
          ("redirect", 1))
    )


_A3IPicmpGenRedirect_Type.__name__ = "Integer32"
_A3IPicmpGenRedirect_Object = MibTableColumn
a3IPicmpGenRedirect = _A3IPicmpGenRedirect_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1, 2),
    _A3IPicmpGenRedirect_Type()
)
a3IPicmpGenRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPicmpGenRedirect.setStatus("mandatory")


class _A3IPicmpGenDestUnreach_Type(Integer32):
    """Custom type a3IPicmpGenDestUnreach based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destUnreachable", 1),
          ("noDestUnreachable", 2))
    )


_A3IPicmpGenDestUnreach_Type.__name__ = "Integer32"
_A3IPicmpGenDestUnreach_Object = MibTableColumn
a3IPicmpGenDestUnreach = _A3IPicmpGenDestUnreach_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1, 3),
    _A3IPicmpGenDestUnreach_Type()
)
a3IPicmpGenDestUnreach.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPicmpGenDestUnreach.setStatus("mandatory")


class _A3IPicmpGenTimeExceed_Type(Integer32):
    """Custom type a3IPicmpGenTimeExceed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTimeExceed", 2),
          ("timeExceed", 1))
    )


_A3IPicmpGenTimeExceed_Type.__name__ = "Integer32"
_A3IPicmpGenTimeExceed_Object = MibTableColumn
a3IPicmpGenTimeExceed = _A3IPicmpGenTimeExceed_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1, 4),
    _A3IPicmpGenTimeExceed_Type()
)
a3IPicmpGenTimeExceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPicmpGenTimeExceed.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-IPEXTNS-R5-MIB",
    **{"SMDSAddress": SMDSAddress,
       "RowStatus": RowStatus,
       "a3Com": a3Com,
       "brouterMIB": brouterMIB,
       "a3ComIPextns": a3ComIPextns,
       "a3IPextMode": a3IPextMode,
       "a3IPextFlushCtl": a3IPextFlushCtl,
       "a3IPextRelaySrcRteCtl": a3IPextRelaySrcRteCtl,
       "a3IPextSplitLoadCtl": a3IPextSplitLoadCtl,
       "a3IPicmpInfoCtl": a3IPicmpInfoCtl,
       "a3IPicmpMaskCtl": a3IPicmpMaskCtl,
       "a3IPntmExtTable": a3IPntmExtTable,
       "a3IPntmExtEntry": a3IPntmExtEntry,
       "a3IPntmIfIndex": a3IPntmIfIndex,
       "a3IPntmNetAddress": a3IPntmNetAddress,
       "a3IPntmHdrFormat": a3IPntmHdrFormat,
       "a3IPntmProxyArp": a3IPntmProxyArp,
       "a3IPaddrConfigTable": a3IPaddrConfigTable,
       "a3IPaddrConfigEntry": a3IPaddrConfigEntry,
       "a3IPaddrConfigPort": a3IPaddrConfigPort,
       "a3IPaddrConfigAddr": a3IPaddrConfigAddr,
       "a3IPaddrConfigType": a3IPaddrConfigType,
       "a3IPaddrConfigNetMask": a3IPaddrConfigNetMask,
       "a3IPaddrConfigBcastAddr": a3IPaddrConfigBcastAddr,
       "a3IPaddrConfigMtu": a3IPaddrConfigMtu,
       "a3IPaddrConfigStatus": a3IPaddrConfigStatus,
       "a3IPforwardExtTable": a3IPforwardExtTable,
       "a3IPforwardExtEntry": a3IPforwardExtEntry,
       "a3IPforwardExtDest": a3IPforwardExtDest,
       "a3IPforwardExtProto": a3IPforwardExtProto,
       "a3IPforwardExtPolicy": a3IPforwardExtPolicy,
       "a3IPforwardExtNextHop": a3IPforwardExtNextHop,
       "a3IPforwardExtOverride": a3IPforwardExtOverride,
       "a3IParpOverBlocked": a3IParpOverBlocked,
       "a3IPrarpClientCtl": a3IPrarpClientCtl,
       "a3IPrarpServerCtl": a3IPrarpServerCtl,
       "a3IParpConfigTable": a3IParpConfigTable,
       "a3IParpConfigEntry": a3IParpConfigEntry,
       "a3IParpPortIndex": a3IParpPortIndex,
       "a3IParpProxyCtl": a3IParpProxyCtl,
       "a3IParpHoldTime": a3IParpHoldTime,
       "a3IParpReqFormat": a3IParpReqFormat,
       "a3IParpRemAddr": a3IParpRemAddr,
       "a3IParpInvCtl": a3IParpInvCtl,
       "a3IPsmdsGaTable": a3IPsmdsGaTable,
       "a3IPsmdsGaEntry": a3IPsmdsGaEntry,
       "a3IPsmdsGaIpNet": a3IPsmdsGaIpNet,
       "a3IPsmdsGa": a3IPsmdsGa,
       "a3IPsmdsGaStatus": a3IPsmdsGaStatus,
       "a3IPx25configTable": a3IPx25configTable,
       "a3IPx25configEntry": a3IPx25configEntry,
       "a3IPx25configPort": a3IPx25configPort,
       "a3IPx25configPID": a3IPx25configPID,
       "a3IPx25configQueueSize": a3IPx25configQueueSize,
       "a3IPx25configVClimit": a3IPx25configVClimit,
       "a3IPx25configVCtimer": a3IPx25configVCtimer,
       "a3IPx25configProfID": a3IPx25configProfID,
       "a3IPqueuePriority": a3IPqueuePriority,
       "a3IPfwdSubnetBcast": a3IPfwdSubnetBcast,
       "a3IPicmpGenTable": a3IPicmpGenTable,
       "a3IPicmpGenEntry": a3IPicmpGenEntry,
       "a3IPicmpGenIfIndex": a3IPicmpGenIfIndex,
       "a3IPicmpGenRedirect": a3IPicmpGenRedirect,
       "a3IPicmpGenDestUnreach": a3IPicmpGenDestUnreach,
       "a3IPicmpGenTimeExceed": a3IPicmpGenTimeExceed}
)
