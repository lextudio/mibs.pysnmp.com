# SNMP MIB module (A3COM-BRIDGE-R3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-BRIDGE-R3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:10 2024
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





class X121Address(OctetString):
    """Custom type X121Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
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
_A3ComBridge_ObjectIdentity = ObjectIdentity
a3ComBridge = _A3ComBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 9)
)
_A3ComBrgGen_ObjectIdentity = ObjectIdentity
a3ComBrgGen = _A3ComBrgGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1)
)


class _A3ComBrgCtl_Type(Integer32):
    """Custom type a3ComBrgCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 1),
          ("noBridging", 2))
    )


_A3ComBrgCtl_Type.__name__ = "Integer32"
_A3ComBrgCtl_Object = MibScalar
a3ComBrgCtl = _A3ComBrgCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 1),
    _A3ComBrgCtl_Type()
)
a3ComBrgCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgCtl.setStatus("mandatory")


class _A3ComBrgAgeCtl_Type(Integer32):
    """Custom type a3ComBrgAgeCtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aging", 1),
          ("noAging", 2))
    )


_A3ComBrgAgeCtl_Type.__name__ = "Integer32"
_A3ComBrgAgeCtl_Object = MibScalar
a3ComBrgAgeCtl = _A3ComBrgAgeCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 2),
    _A3ComBrgAgeCtl_Type()
)
a3ComBrgAgeCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgAgeCtl.setStatus("mandatory")


class _A3ComBrgFwallCtl_Type(Integer32):
    """Custom type a3ComBrgFwallCtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("firewall", 1),
          ("noFirewall", 2))
    )


_A3ComBrgFwallCtl_Type.__name__ = "Integer32"
_A3ComBrgFwallCtl_Object = MibScalar
a3ComBrgFwallCtl = _A3ComBrgFwallCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 3),
    _A3ComBrgFwallCtl_Type()
)
a3ComBrgFwallCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgFwallCtl.setStatus("mandatory")


class _A3ComBrgLearnCtl_Type(Integer32):
    """Custom type a3ComBrgLearnCtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learn", 1),
          ("noLearn", 2))
    )


_A3ComBrgLearnCtl_Type.__name__ = "Integer32"
_A3ComBrgLearnCtl_Object = MibScalar
a3ComBrgLearnCtl = _A3ComBrgLearnCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 4),
    _A3ComBrgLearnCtl_Type()
)
a3ComBrgLearnCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgLearnCtl.setStatus("mandatory")


class _A3ComBrgForwardCtl_Type(Integer32):
    """Custom type a3ComBrgForwardCtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("noForward", 2))
    )


_A3ComBrgForwardCtl_Type.__name__ = "Integer32"
_A3ComBrgForwardCtl_Object = MibScalar
a3ComBrgForwardCtl = _A3ComBrgForwardCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 5),
    _A3ComBrgForwardCtl_Type()
)
a3ComBrgForwardCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgForwardCtl.setStatus("mandatory")


class _A3ComBrgAppleCtl_Type(Integer32):
    """Custom type a3ComBrgAppleCtl based on Integer32"""
    defaultValue = 1

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


_A3ComBrgAppleCtl_Type.__name__ = "Integer32"
_A3ComBrgAppleCtl_Object = MibScalar
a3ComBrgAppleCtl = _A3ComBrgAppleCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 6),
    _A3ComBrgAppleCtl_Type()
)
a3ComBrgAppleCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgAppleCtl.setStatus("mandatory")


class _A3ComBrgFwTblCtl_Type(Integer32):
    """Custom type a3ComBrgFwTblCtl based on Integer32"""
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
        *(("delDyn", 4),
          ("delStatic", 3),
          ("dynToStatic", 2),
          ("other", 1))
    )


_A3ComBrgFwTblCtl_Type.__name__ = "Integer32"
_A3ComBrgFwTblCtl_Object = MibScalar
a3ComBrgFwTblCtl = _A3ComBrgFwTblCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 7),
    _A3ComBrgFwTblCtl_Type()
)
a3ComBrgFwTblCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgFwTblCtl.setStatus("mandatory")


class _A3ComBrgFwTblSize_Type(Integer32):
    """Custom type a3ComBrgFwTblSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_A3ComBrgFwTblSize_Type.__name__ = "Integer32"
_A3ComBrgFwTblSize_Object = MibScalar
a3ComBrgFwTblSize = _A3ComBrgFwTblSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 8),
    _A3ComBrgFwTblSize_Type()
)
a3ComBrgFwTblSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgFwTblSize.setStatus("mandatory")


class _A3ComBrgBLimitTimer_Type(Integer32):
    """Custom type a3ComBrgBLimitTimer based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 1),
          ("timer1000ms", 5),
          ("timer400ms", 2),
          ("timer600ms", 3),
          ("timer800ms", 4))
    )


_A3ComBrgBLimitTimer_Type.__name__ = "Integer32"
_A3ComBrgBLimitTimer_Object = MibScalar
a3ComBrgBLimitTimer = _A3ComBrgBLimitTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 9),
    _A3ComBrgBLimitTimer_Type()
)
a3ComBrgBLimitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgBLimitTimer.setStatus("mandatory")
_A3ComBrgStExtTable_Object = MibTable
a3ComBrgStExtTable = _A3ComBrgStExtTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 10)
)
if mibBuilder.loadTexts:
    a3ComBrgStExtTable.setStatus("mandatory")
_A3ComBrgStExtEntry_Object = MibTableRow
a3ComBrgStExtEntry = _A3ComBrgStExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 10, 1)
)
a3ComBrgStExtEntry.setIndexNames(
    (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgStExtAdd"),
    (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgStExtRcvPort"),
)
if mibBuilder.loadTexts:
    a3ComBrgStExtEntry.setStatus("mandatory")
_A3ComBrgStExtAdd_Type = MacAddress
_A3ComBrgStExtAdd_Object = MibTableColumn
a3ComBrgStExtAdd = _A3ComBrgStExtAdd_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 10, 1, 1),
    _A3ComBrgStExtAdd_Type()
)
a3ComBrgStExtAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgStExtAdd.setStatus("mandatory")
_A3ComBrgStExtRcvPort_Type = Integer32
_A3ComBrgStExtRcvPort_Object = MibTableColumn
a3ComBrgStExtRcvPort = _A3ComBrgStExtRcvPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 10, 1, 2),
    _A3ComBrgStExtRcvPort_Type()
)
a3ComBrgStExtRcvPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgStExtRcvPort.setStatus("mandatory")
_A3ComBrgStExtWaAddress_Type = OctetString
_A3ComBrgStExtWaAddress_Object = MibTableColumn
a3ComBrgStExtWaAddress = _A3ComBrgStExtWaAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 10, 1, 3),
    _A3ComBrgStExtWaAddress_Type()
)
a3ComBrgStExtWaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgStExtWaAddress.setStatus("mandatory")
_A3ComBrgFdbExtTable_Object = MibTable
a3ComBrgFdbExtTable = _A3ComBrgFdbExtTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 11)
)
if mibBuilder.loadTexts:
    a3ComBrgFdbExtTable.setStatus("mandatory")
_A3ComBrgFdbExtEntry_Object = MibTableRow
a3ComBrgFdbExtEntry = _A3ComBrgFdbExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 11, 1)
)
a3ComBrgFdbExtEntry.setIndexNames(
    (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgFdbExtAdd"),
)
if mibBuilder.loadTexts:
    a3ComBrgFdbExtEntry.setStatus("mandatory")
_A3ComBrgFdbExtAdd_Type = MacAddress
_A3ComBrgFdbExtAdd_Object = MibTableColumn
a3ComBrgFdbExtAdd = _A3ComBrgFdbExtAdd_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 11, 1, 1),
    _A3ComBrgFdbExtAdd_Type()
)
a3ComBrgFdbExtAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgFdbExtAdd.setStatus("mandatory")
_A3ComBrgFdbExtWaAddress_Type = OctetString
_A3ComBrgFdbExtWaAddress_Object = MibTableColumn
a3ComBrgFdbExtWaAddress = _A3ComBrgFdbExtWaAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 11, 1, 2),
    _A3ComBrgFdbExtWaAddress_Type()
)
a3ComBrgFdbExtWaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgFdbExtWaAddress.setStatus("mandatory")
_A3ComBrgPortTable_Object = MibTable
a3ComBrgPortTable = _A3ComBrgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12)
)
if mibBuilder.loadTexts:
    a3ComBrgPortTable.setStatus("mandatory")
_A3ComBrgPortEntry_Object = MibTableRow
a3ComBrgPortEntry = _A3ComBrgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1)
)
a3ComBrgPortEntry.setIndexNames(
    (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgPortIndex"),
)
if mibBuilder.loadTexts:
    a3ComBrgPortEntry.setStatus("mandatory")
_A3ComBrgPortIndex_Type = Integer32
_A3ComBrgPortIndex_Object = MibTableColumn
a3ComBrgPortIndex = _A3ComBrgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 1),
    _A3ComBrgPortIndex_Type()
)
a3ComBrgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgPortIndex.setStatus("mandatory")


class _A3ComBrgPortCtl_Type(Integer32):
    """Custom type a3ComBrgPortCtl based on Integer32"""
    defaultValue = 4

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
        *(("noBridging", 4),
          ("sourceRoute", 2),
          ("srtEnabled", 3),
          ("transparent", 1))
    )


_A3ComBrgPortCtl_Type.__name__ = "Integer32"
_A3ComBrgPortCtl_Object = MibTableColumn
a3ComBrgPortCtl = _A3ComBrgPortCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 2),
    _A3ComBrgPortCtl_Type()
)
a3ComBrgPortCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgPortCtl.setStatus("mandatory")


class _A3ComBrgDstSecCtl_Type(Integer32):
    """Custom type a3ComBrgDstSecCtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 3),
          ("forward", 2),
          ("none", 1))
    )


_A3ComBrgDstSecCtl_Type.__name__ = "Integer32"
_A3ComBrgDstSecCtl_Object = MibTableColumn
a3ComBrgDstSecCtl = _A3ComBrgDstSecCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 3),
    _A3ComBrgDstSecCtl_Type()
)
a3ComBrgDstSecCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgDstSecCtl.setStatus("mandatory")


class _A3ComBrgSrcSecCtl_Type(Integer32):
    """Custom type a3ComBrgSrcSecCtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 3),
          ("forward", 2),
          ("none", 1))
    )


_A3ComBrgSrcSecCtl_Type.__name__ = "Integer32"
_A3ComBrgSrcSecCtl_Object = MibTableColumn
a3ComBrgSrcSecCtl = _A3ComBrgSrcSecCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 4),
    _A3ComBrgSrcSecCtl_Type()
)
a3ComBrgSrcSecCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrcSecCtl.setStatus("mandatory")


class _A3ComBrgX25Pid_Type(Integer32):
    """Custom type a3ComBrgX25Pid based on Integer32"""
    defaultValue = 221

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A3ComBrgX25Pid_Type.__name__ = "Integer32"
_A3ComBrgX25Pid_Object = MibTableColumn
a3ComBrgX25Pid = _A3ComBrgX25Pid_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 5),
    _A3ComBrgX25Pid_Type()
)
a3ComBrgX25Pid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgX25Pid.setStatus("mandatory")


class _A3ComBrgX25Qsize_Type(Integer32):
    """Custom type a3ComBrgX25Qsize based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_A3ComBrgX25Qsize_Type.__name__ = "Integer32"
_A3ComBrgX25Qsize_Object = MibTableColumn
a3ComBrgX25Qsize = _A3ComBrgX25Qsize_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 6),
    _A3ComBrgX25Qsize_Type()
)
a3ComBrgX25Qsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgX25Qsize.setStatus("deprecated")


class _A3ComBrgX25VcLimit_Type(Integer32):
    """Custom type a3ComBrgX25VcLimit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3ComBrgX25VcLimit_Type.__name__ = "Integer32"
_A3ComBrgX25VcLimit_Object = MibTableColumn
a3ComBrgX25VcLimit = _A3ComBrgX25VcLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 7),
    _A3ComBrgX25VcLimit_Type()
)
a3ComBrgX25VcLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgX25VcLimit.setStatus("deprecated")


class _A3ComBrgX25VcTimer_Type(Integer32):
    """Custom type a3ComBrgX25VcTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_A3ComBrgX25VcTimer_Type.__name__ = "Integer32"
_A3ComBrgX25VcTimer_Object = MibTableColumn
a3ComBrgX25VcTimer = _A3ComBrgX25VcTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 8),
    _A3ComBrgX25VcTimer_Type()
)
a3ComBrgX25VcTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgX25VcTimer.setStatus("deprecated")


class _A3ComBrgBroadCastLimit_Type(Integer32):
    """Custom type a3ComBrgBroadCastLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_A3ComBrgBroadCastLimit_Type.__name__ = "Integer32"
_A3ComBrgBroadCastLimit_Object = MibTableColumn
a3ComBrgBroadCastLimit = _A3ComBrgBroadCastLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 9),
    _A3ComBrgBroadCastLimit_Type()
)
a3ComBrgBroadCastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgBroadCastLimit.setStatus("mandatory")
_A3ComBrgSmdsGroupAddr_Type = SMDSAddress
_A3ComBrgSmdsGroupAddr_Object = MibTableColumn
a3ComBrgSmdsGroupAddr = _A3ComBrgSmdsGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 10),
    _A3ComBrgSmdsGroupAddr_Type()
)
a3ComBrgSmdsGroupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSmdsGroupAddr.setStatus("mandatory")


class _A3ComBrgX25ProfId_Type(Integer32):
    """Custom type a3ComBrgX25ProfId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A3ComBrgX25ProfId_Type.__name__ = "Integer32"
_A3ComBrgX25ProfId_Object = MibTableColumn
a3ComBrgX25ProfId = _A3ComBrgX25ProfId_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 14),
    _A3ComBrgX25ProfId_Type()
)
a3ComBrgX25ProfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgX25ProfId.setStatus("mandatory")
_A3ComBrgX25NbrTable_Object = MibTable
a3ComBrgX25NbrTable = _A3ComBrgX25NbrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 13)
)
if mibBuilder.loadTexts:
    a3ComBrgX25NbrTable.setStatus("mandatory")
_A3ComBrgX25NbrEntry_Object = MibTableRow
a3ComBrgX25NbrEntry = _A3ComBrgX25NbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 13, 1)
)
a3ComBrgX25NbrEntry.setIndexNames(
    (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgX25NbrPort"),
    (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgX25NbrDTE"),
)
if mibBuilder.loadTexts:
    a3ComBrgX25NbrEntry.setStatus("mandatory")
_A3ComBrgX25NbrPort_Type = Integer32
_A3ComBrgX25NbrPort_Object = MibTableColumn
a3ComBrgX25NbrPort = _A3ComBrgX25NbrPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 13, 1, 1),
    _A3ComBrgX25NbrPort_Type()
)
a3ComBrgX25NbrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgX25NbrPort.setStatus("mandatory")
_A3ComBrgX25NbrDTE_Type = X121Address
_A3ComBrgX25NbrDTE_Object = MibTableColumn
a3ComBrgX25NbrDTE = _A3ComBrgX25NbrDTE_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 13, 1, 2),
    _A3ComBrgX25NbrDTE_Type()
)
a3ComBrgX25NbrDTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgX25NbrDTE.setStatus("mandatory")
_A3ComBrgX25NbrStatus_Type = RowStatus
_A3ComBrgX25NbrStatus_Object = MibTableColumn
a3ComBrgX25NbrStatus = _A3ComBrgX25NbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 13, 1, 3),
    _A3ComBrgX25NbrStatus_Type()
)
a3ComBrgX25NbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgX25NbrStatus.setStatus("mandatory")
_A3ComBrgStp_ObjectIdentity = ObjectIdentity
a3ComBrgStp = _A3ComBrgStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 2)
)
_A3ComBrgStpMultAdd_Type = MacAddress
_A3ComBrgStpMultAdd_Object = MibScalar
a3ComBrgStpMultAdd = _A3ComBrgStpMultAdd_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 2, 1),
    _A3ComBrgStpMultAdd_Type()
)
a3ComBrgStpMultAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgStpMultAdd.setStatus("mandatory")


class _A3ComBrgStpCtl_Type(Integer32):
    """Custom type a3ComBrgStpCtl based on Integer32"""
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


_A3ComBrgStpCtl_Type.__name__ = "Integer32"
_A3ComBrgStpCtl_Object = MibScalar
a3ComBrgStpCtl = _A3ComBrgStpCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 2, 2),
    _A3ComBrgStpCtl_Type()
)
a3ComBrgStpCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgStpCtl.setStatus("mandatory")


class _A3ComBrgStpHopCtl_Type(Integer32):
    """Custom type a3ComBrgStpHopCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hopReduce", 1),
          ("noHopReduce", 2))
    )


_A3ComBrgStpHopCtl_Type.__name__ = "Integer32"
_A3ComBrgStpHopCtl_Object = MibScalar
a3ComBrgStpHopCtl = _A3ComBrgStpHopCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 2, 3),
    _A3ComBrgStpHopCtl_Type()
)
a3ComBrgStpHopCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgStpHopCtl.setStatus("mandatory")
_A3ComBrgSr_ObjectIdentity = ObjectIdentity
a3ComBrgSr = _A3ComBrgSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3)
)


class _A3ComBrgSrMode_Type(Integer32):
    """Custom type a3ComBrgSrMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee", 1),
          ("passiveBridging", 2))
    )


_A3ComBrgSrMode_Type.__name__ = "Integer32"
_A3ComBrgSrMode_Object = MibScalar
a3ComBrgSrMode = _A3ComBrgSrMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 1),
    _A3ComBrgSrMode_Type()
)
a3ComBrgSrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrMode.setStatus("mandatory")
_A3ComBrgSrPortTable_Object = MibTable
a3ComBrgSrPortTable = _A3ComBrgSrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2)
)
if mibBuilder.loadTexts:
    a3ComBrgSrPortTable.setStatus("mandatory")
_A3ComBrgSrPortEntry_Object = MibTableRow
a3ComBrgSrPortEntry = _A3ComBrgSrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2, 1)
)
a3ComBrgSrPortEntry.setIndexNames(
    (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgSrPort"),
)
if mibBuilder.loadTexts:
    a3ComBrgSrPortEntry.setStatus("mandatory")
_A3ComBrgSrPort_Type = Integer32
_A3ComBrgSrPort_Object = MibTableColumn
a3ComBrgSrPort = _A3ComBrgSrPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2, 1, 1),
    _A3ComBrgSrPort_Type()
)
a3ComBrgSrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgSrPort.setStatus("mandatory")
_A3ComBrgSrPortSTEHopCount_Type = Integer32
_A3ComBrgSrPortSTEHopCount_Object = MibTableColumn
a3ComBrgSrPortSTEHopCount = _A3ComBrgSrPortSTEHopCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2, 1, 2),
    _A3ComBrgSrPortSTEHopCount_Type()
)
a3ComBrgSrPortSTEHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrPortSTEHopCount.setStatus("mandatory")
_A3ComBrgSrPortAREHopCount_Type = Integer32
_A3ComBrgSrPortAREHopCount_Object = MibTableColumn
a3ComBrgSrPortAREHopCount = _A3ComBrgSrPortAREHopCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2, 1, 3),
    _A3ComBrgSrPortAREHopCount_Type()
)
a3ComBrgSrPortAREHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrPortAREHopCount.setStatus("mandatory")


class _A3ComBrgSrPortHoldTime_Type(Integer32):
    """Custom type a3ComBrgSrPortHoldTime based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_A3ComBrgSrPortHoldTime_Type.__name__ = "Integer32"
_A3ComBrgSrPortHoldTime_Object = MibTableColumn
a3ComBrgSrPortHoldTime = _A3ComBrgSrPortHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2, 1, 4),
    _A3ComBrgSrPortHoldTime_Type()
)
a3ComBrgSrPortHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrPortHoldTime.setStatus("mandatory")


class _A3ComBrgSrPortMinAccessPrior_Type(Integer32):
    """Custom type a3ComBrgSrPortMinAccessPrior based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_A3ComBrgSrPortMinAccessPrior_Type.__name__ = "Integer32"
_A3ComBrgSrPortMinAccessPrior_Object = MibTableColumn
a3ComBrgSrPortMinAccessPrior = _A3ComBrgSrPortMinAccessPrior_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2, 1, 5),
    _A3ComBrgSrPortMinAccessPrior_Type()
)
a3ComBrgSrPortMinAccessPrior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrPortMinAccessPrior.setStatus("mandatory")
_A3ComBrgSrWanAddrTable_Object = MibTable
a3ComBrgSrWanAddrTable = _A3ComBrgSrWanAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 3)
)
if mibBuilder.loadTexts:
    a3ComBrgSrWanAddrTable.setStatus("mandatory")
_A3ComBrgSrWanAddrEntry_Object = MibTableRow
a3ComBrgSrWanAddrEntry = _A3ComBrgSrWanAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 3, 1)
)
a3ComBrgSrWanAddrEntry.setIndexNames(
    (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgSrWAportIndex"),
    (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgSrWAringNum"),
    (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgSrWAbrgNum"),
)
if mibBuilder.loadTexts:
    a3ComBrgSrWanAddrEntry.setStatus("mandatory")
_A3ComBrgSrWAportIndex_Type = Integer32
_A3ComBrgSrWAportIndex_Object = MibTableColumn
a3ComBrgSrWAportIndex = _A3ComBrgSrWAportIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 3, 1, 1),
    _A3ComBrgSrWAportIndex_Type()
)
a3ComBrgSrWAportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgSrWAportIndex.setStatus("mandatory")
_A3ComBrgSrWAringNum_Type = Integer32
_A3ComBrgSrWAringNum_Object = MibTableColumn
a3ComBrgSrWAringNum = _A3ComBrgSrWAringNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 3, 1, 2),
    _A3ComBrgSrWAringNum_Type()
)
a3ComBrgSrWAringNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgSrWAringNum.setStatus("mandatory")
_A3ComBrgSrWAbrgNum_Type = Integer32
_A3ComBrgSrWAbrgNum_Object = MibTableColumn
a3ComBrgSrWAbrgNum = _A3ComBrgSrWAbrgNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 3, 1, 3),
    _A3ComBrgSrWAbrgNum_Type()
)
a3ComBrgSrWAbrgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgSrWAbrgNum.setStatus("mandatory")
_A3ComBrgSrWAddress_Type = OctetString
_A3ComBrgSrWAddress_Object = MibTableColumn
a3ComBrgSrWAddress = _A3ComBrgSrWAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 3, 1, 4),
    _A3ComBrgSrWAddress_Type()
)
a3ComBrgSrWAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgSrWAddress.setStatus("mandatory")


class _A3ComBrgSrGwVirRing_Type(Integer32):
    """Custom type a3ComBrgSrGwVirRing based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_A3ComBrgSrGwVirRing_Type.__name__ = "Integer32"
_A3ComBrgSrGwVirRing_Object = MibScalar
a3ComBrgSrGwVirRing = _A3ComBrgSrGwVirRing_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 4),
    _A3ComBrgSrGwVirRing_Type()
)
a3ComBrgSrGwVirRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrGwVirRing.setStatus("mandatory")
_A3ComBrgSrGwContTable_Object = MibTable
a3ComBrgSrGwContTable = _A3ComBrgSrGwContTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 5)
)
if mibBuilder.loadTexts:
    a3ComBrgSrGwContTable.setStatus("mandatory")
_A3ComBrgSrGwContEntry_Object = MibTableRow
a3ComBrgSrGwContEntry = _A3ComBrgSrGwContEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 5, 1)
)
a3ComBrgSrGwContEntry.setIndexNames(
    (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgSrGwContPort"),
)
if mibBuilder.loadTexts:
    a3ComBrgSrGwContEntry.setStatus("mandatory")
_A3ComBrgSrGwContPort_Type = Integer32
_A3ComBrgSrGwContPort_Object = MibTableColumn
a3ComBrgSrGwContPort = _A3ComBrgSrGwContPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 5, 1, 1),
    _A3ComBrgSrGwContPort_Type()
)
a3ComBrgSrGwContPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgSrGwContPort.setStatus("mandatory")


class _A3ComBrgSrGwCont_Type(Integer32):
    """Custom type a3ComBrgSrGwCont based on Integer32"""
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


_A3ComBrgSrGwCont_Type.__name__ = "Integer32"
_A3ComBrgSrGwCont_Object = MibTableColumn
a3ComBrgSrGwCont = _A3ComBrgSrGwCont_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 5, 1, 2),
    _A3ComBrgSrGwCont_Type()
)
a3ComBrgSrGwCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrGwCont.setStatus("mandatory")


class _A3ComBrgSrGwContEncapMode_Type(Integer32):
    """Custom type a3ComBrgSrGwContEncapMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("etherMode", 2),
          ("ieeeMode", 1))
    )


_A3ComBrgSrGwContEncapMode_Type.__name__ = "Integer32"
_A3ComBrgSrGwContEncapMode_Object = MibTableColumn
a3ComBrgSrGwContEncapMode = _A3ComBrgSrGwContEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 5, 1, 3),
    _A3ComBrgSrGwContEncapMode_Type()
)
a3ComBrgSrGwContEncapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrGwContEncapMode.setStatus("mandatory")


class _A3ComBrgSrGwContAutoMode_Type(Integer32):
    """Custom type a3ComBrgSrGwContAutoMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoMode", 1),
          ("noAutoMode", 2))
    )


_A3ComBrgSrGwContAutoMode_Type.__name__ = "Integer32"
_A3ComBrgSrGwContAutoMode_Object = MibTableColumn
a3ComBrgSrGwContAutoMode = _A3ComBrgSrGwContAutoMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 5, 1, 4),
    _A3ComBrgSrGwContAutoMode_Type()
)
a3ComBrgSrGwContAutoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrGwContAutoMode.setStatus("mandatory")
_A3ComBrgSrRDTable_Object = MibTable
a3ComBrgSrRDTable = _A3ComBrgSrRDTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6)
)
if mibBuilder.loadTexts:
    a3ComBrgSrRDTable.setStatus("mandatory")
_A3ComBrgSrRDEntry_Object = MibTableRow
a3ComBrgSrRDEntry = _A3ComBrgSrRDEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1)
)
a3ComBrgSrRDEntry.setIndexNames(
    (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgSrRDPort"),
)
if mibBuilder.loadTexts:
    a3ComBrgSrRDEntry.setStatus("mandatory")
_A3ComBrgSrRDPort_Type = Integer32
_A3ComBrgSrRDPort_Object = MibTableColumn
a3ComBrgSrRDPort = _A3ComBrgSrRDPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 1),
    _A3ComBrgSrRDPort_Type()
)
a3ComBrgSrRDPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgSrRDPort.setStatus("mandatory")


class _A3ComBrgSrRDAppleTalk_Type(Integer32):
    """Custom type a3ComBrgSrRDAppleTalk based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 1),
          ("noAppleTalk", 2))
    )


_A3ComBrgSrRDAppleTalk_Type.__name__ = "Integer32"
_A3ComBrgSrRDAppleTalk_Object = MibTableColumn
a3ComBrgSrRDAppleTalk = _A3ComBrgSrRDAppleTalk_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 2),
    _A3ComBrgSrRDAppleTalk_Type()
)
a3ComBrgSrRDAppleTalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrRDAppleTalk.setStatus("mandatory")


class _A3ComBrgSrRDClnp_Type(Integer32):
    """Custom type a3ComBrgSrRDClnp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clnp", 1),
          ("noClnp", 2))
    )


_A3ComBrgSrRDClnp_Type.__name__ = "Integer32"
_A3ComBrgSrRDClnp_Object = MibTableColumn
a3ComBrgSrRDClnp = _A3ComBrgSrRDClnp_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 3),
    _A3ComBrgSrRDClnp_Type()
)
a3ComBrgSrRDClnp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrRDClnp.setStatus("mandatory")


class _A3ComBrgSrRDDecNet_Type(Integer32):
    """Custom type a3ComBrgSrRDDecNet based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("decNet", 1),
          ("noDecNet", 2))
    )


_A3ComBrgSrRDDecNet_Type.__name__ = "Integer32"
_A3ComBrgSrRDDecNet_Object = MibTableColumn
a3ComBrgSrRDDecNet = _A3ComBrgSrRDDecNet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 4),
    _A3ComBrgSrRDDecNet_Type()
)
a3ComBrgSrRDDecNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrRDDecNet.setStatus("mandatory")


class _A3ComBrgSrRDDlTest_Type(Integer32):
    """Custom type a3ComBrgSrRDDlTest based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dlTest", 1),
          ("noDlTest", 2))
    )


_A3ComBrgSrRDDlTest_Type.__name__ = "Integer32"
_A3ComBrgSrRDDlTest_Object = MibTableColumn
a3ComBrgSrRDDlTest = _A3ComBrgSrRDDlTest_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 5),
    _A3ComBrgSrRDDlTest_Type()
)
a3ComBrgSrRDDlTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrRDDlTest.setStatus("mandatory")


class _A3ComBrgSrRDIp_Type(Integer32):
    """Custom type a3ComBrgSrRDIp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("noIp", 2))
    )


_A3ComBrgSrRDIp_Type.__name__ = "Integer32"
_A3ComBrgSrRDIp_Object = MibTableColumn
a3ComBrgSrRDIp = _A3ComBrgSrRDIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 6),
    _A3ComBrgSrRDIp_Type()
)
a3ComBrgSrRDIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrRDIp.setStatus("mandatory")


class _A3ComBrgSrRDIpx_Type(Integer32):
    """Custom type a3ComBrgSrRDIpx based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipx", 1),
          ("noIpx", 2))
    )


_A3ComBrgSrRDIpx_Type.__name__ = "Integer32"
_A3ComBrgSrRDIpx_Object = MibTableColumn
a3ComBrgSrRDIpx = _A3ComBrgSrRDIpx_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 7),
    _A3ComBrgSrRDIpx_Type()
)
a3ComBrgSrRDIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrRDIpx.setStatus("mandatory")


class _A3ComBrgSrRDLlc2_Type(Integer32):
    """Custom type a3ComBrgSrRDLlc2 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc2", 1),
          ("noLlc2", 2))
    )


_A3ComBrgSrRDLlc2_Type.__name__ = "Integer32"
_A3ComBrgSrRDLlc2_Object = MibTableColumn
a3ComBrgSrRDLlc2 = _A3ComBrgSrRDLlc2_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 8),
    _A3ComBrgSrRDLlc2_Type()
)
a3ComBrgSrRDLlc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrRDLlc2.setStatus("mandatory")


class _A3ComBrgSrRDVines_Type(Integer32):
    """Custom type a3ComBrgSrRDVines based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noVines", 2),
          ("vines", 1))
    )


_A3ComBrgSrRDVines_Type.__name__ = "Integer32"
_A3ComBrgSrRDVines_Object = MibTableColumn
a3ComBrgSrRDVines = _A3ComBrgSrRDVines_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 9),
    _A3ComBrgSrRDVines_Type()
)
a3ComBrgSrRDVines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrgSrRDVines.setStatus("mandatory")
_A3ComBrgSrTunVRing_Type = Integer32
_A3ComBrgSrTunVRing_Object = MibScalar
a3ComBrgSrTunVRing = _A3ComBrgSrTunVRing_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 7),
    _A3ComBrgSrTunVRing_Type()
)
a3ComBrgSrTunVRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgSrTunVRing.setStatus("deprecated")
_A3ComBrgSrCNodeAddr_Type = OctetString
_A3ComBrgSrCNodeAddr_Object = MibScalar
a3ComBrgSrCNodeAddr = _A3ComBrgSrCNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 8),
    _A3ComBrgSrCNodeAddr_Type()
)
a3ComBrgSrCNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBrgSrCNodeAddr.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-BRIDGE-R3-MIB",
    **{"SMDSAddress": SMDSAddress,
       "RowStatus": RowStatus,
       "X121Address": X121Address,
       "a3Com": a3Com,
       "brouterMIB": brouterMIB,
       "a3ComBridge": a3ComBridge,
       "a3ComBrgGen": a3ComBrgGen,
       "a3ComBrgCtl": a3ComBrgCtl,
       "a3ComBrgAgeCtl": a3ComBrgAgeCtl,
       "a3ComBrgFwallCtl": a3ComBrgFwallCtl,
       "a3ComBrgLearnCtl": a3ComBrgLearnCtl,
       "a3ComBrgForwardCtl": a3ComBrgForwardCtl,
       "a3ComBrgAppleCtl": a3ComBrgAppleCtl,
       "a3ComBrgFwTblCtl": a3ComBrgFwTblCtl,
       "a3ComBrgFwTblSize": a3ComBrgFwTblSize,
       "a3ComBrgBLimitTimer": a3ComBrgBLimitTimer,
       "a3ComBrgStExtTable": a3ComBrgStExtTable,
       "a3ComBrgStExtEntry": a3ComBrgStExtEntry,
       "a3ComBrgStExtAdd": a3ComBrgStExtAdd,
       "a3ComBrgStExtRcvPort": a3ComBrgStExtRcvPort,
       "a3ComBrgStExtWaAddress": a3ComBrgStExtWaAddress,
       "a3ComBrgFdbExtTable": a3ComBrgFdbExtTable,
       "a3ComBrgFdbExtEntry": a3ComBrgFdbExtEntry,
       "a3ComBrgFdbExtAdd": a3ComBrgFdbExtAdd,
       "a3ComBrgFdbExtWaAddress": a3ComBrgFdbExtWaAddress,
       "a3ComBrgPortTable": a3ComBrgPortTable,
       "a3ComBrgPortEntry": a3ComBrgPortEntry,
       "a3ComBrgPortIndex": a3ComBrgPortIndex,
       "a3ComBrgPortCtl": a3ComBrgPortCtl,
       "a3ComBrgDstSecCtl": a3ComBrgDstSecCtl,
       "a3ComBrgSrcSecCtl": a3ComBrgSrcSecCtl,
       "a3ComBrgX25Pid": a3ComBrgX25Pid,
       "a3ComBrgX25Qsize": a3ComBrgX25Qsize,
       "a3ComBrgX25VcLimit": a3ComBrgX25VcLimit,
       "a3ComBrgX25VcTimer": a3ComBrgX25VcTimer,
       "a3ComBrgBroadCastLimit": a3ComBrgBroadCastLimit,
       "a3ComBrgSmdsGroupAddr": a3ComBrgSmdsGroupAddr,
       "a3ComBrgX25ProfId": a3ComBrgX25ProfId,
       "a3ComBrgX25NbrTable": a3ComBrgX25NbrTable,
       "a3ComBrgX25NbrEntry": a3ComBrgX25NbrEntry,
       "a3ComBrgX25NbrPort": a3ComBrgX25NbrPort,
       "a3ComBrgX25NbrDTE": a3ComBrgX25NbrDTE,
       "a3ComBrgX25NbrStatus": a3ComBrgX25NbrStatus,
       "a3ComBrgStp": a3ComBrgStp,
       "a3ComBrgStpMultAdd": a3ComBrgStpMultAdd,
       "a3ComBrgStpCtl": a3ComBrgStpCtl,
       "a3ComBrgStpHopCtl": a3ComBrgStpHopCtl,
       "a3ComBrgSr": a3ComBrgSr,
       "a3ComBrgSrMode": a3ComBrgSrMode,
       "a3ComBrgSrPortTable": a3ComBrgSrPortTable,
       "a3ComBrgSrPortEntry": a3ComBrgSrPortEntry,
       "a3ComBrgSrPort": a3ComBrgSrPort,
       "a3ComBrgSrPortSTEHopCount": a3ComBrgSrPortSTEHopCount,
       "a3ComBrgSrPortAREHopCount": a3ComBrgSrPortAREHopCount,
       "a3ComBrgSrPortHoldTime": a3ComBrgSrPortHoldTime,
       "a3ComBrgSrPortMinAccessPrior": a3ComBrgSrPortMinAccessPrior,
       "a3ComBrgSrWanAddrTable": a3ComBrgSrWanAddrTable,
       "a3ComBrgSrWanAddrEntry": a3ComBrgSrWanAddrEntry,
       "a3ComBrgSrWAportIndex": a3ComBrgSrWAportIndex,
       "a3ComBrgSrWAringNum": a3ComBrgSrWAringNum,
       "a3ComBrgSrWAbrgNum": a3ComBrgSrWAbrgNum,
       "a3ComBrgSrWAddress": a3ComBrgSrWAddress,
       "a3ComBrgSrGwVirRing": a3ComBrgSrGwVirRing,
       "a3ComBrgSrGwContTable": a3ComBrgSrGwContTable,
       "a3ComBrgSrGwContEntry": a3ComBrgSrGwContEntry,
       "a3ComBrgSrGwContPort": a3ComBrgSrGwContPort,
       "a3ComBrgSrGwCont": a3ComBrgSrGwCont,
       "a3ComBrgSrGwContEncapMode": a3ComBrgSrGwContEncapMode,
       "a3ComBrgSrGwContAutoMode": a3ComBrgSrGwContAutoMode,
       "a3ComBrgSrRDTable": a3ComBrgSrRDTable,
       "a3ComBrgSrRDEntry": a3ComBrgSrRDEntry,
       "a3ComBrgSrRDPort": a3ComBrgSrRDPort,
       "a3ComBrgSrRDAppleTalk": a3ComBrgSrRDAppleTalk,
       "a3ComBrgSrRDClnp": a3ComBrgSrRDClnp,
       "a3ComBrgSrRDDecNet": a3ComBrgSrRDDecNet,
       "a3ComBrgSrRDDlTest": a3ComBrgSrRDDlTest,
       "a3ComBrgSrRDIp": a3ComBrgSrRDIp,
       "a3ComBrgSrRDIpx": a3ComBrgSrRDIpx,
       "a3ComBrgSrRDLlc2": a3ComBrgSrRDLlc2,
       "a3ComBrgSrRDVines": a3ComBrgSrRDVines,
       "a3ComBrgSrTunVRing": a3ComBrgSrTunVRing,
       "a3ComBrgSrCNodeAddr": a3ComBrgSrCNodeAddr}
)
