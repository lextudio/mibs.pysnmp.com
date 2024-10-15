# SNMP MIB module (CT-DS0ent-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-DS0ent-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:06 2024
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

(cabletron,) = mibBuilder.importSymbols(
    "CTRON-OIDS",
    "cabletron")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""




class IANActDs0ifType(Integer32):
    """Custom type IANActDs0ifType based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 49),
          ("arcnet", 35),
          ("arcnetPlus", 36),
          ("atm", 37),
          ("basicISDN", 20),
          ("ddnX25", 4),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("ethernet3Mbit", 26),
          ("ethernetCsmacd", 6),
          ("fddi", 15),
          ("frameRelay", 32),
          ("frameRelayService", 44),
          ("hdh1822", 3),
          ("hippi", 47),
          ("hssi", 46),
          ("hyperchannel", 14),
          ("iso88022llc", 41),
          ("iso88023Csmacd", 7),
          ("iso88024TokenBus", 8),
          ("iso88025TokenRing", 9),
          ("iso88026Man", 10),
          ("lapb", 16),
          ("localTalk", 42),
          ("miox25", 38),
          ("modem", 48),
          ("nsip", 27),
          ("other", 1),
          ("para", 34),
          ("ppp", 23),
          ("primaryISDN", 21),
          ("propMultiplexor", 54),
          ("propPointToPointSerial", 22),
          ("propVirtual", 53),
          ("proteon10Mbit", 12),
          ("proteon80Mbit", 13),
          ("regular1822", 2),
          ("rfc877x25", 5),
          ("rs232", 33),
          ("sdlc", 17),
          ("sip", 31),
          ("slip", 28),
          ("smdsDxi", 43),
          ("smdsIcip", 52),
          ("softwareLoopback", 24),
          ("sonet", 39),
          ("sonetPath", 50),
          ("sonetVT", 51),
          ("starLan", 11),
          ("ultra", 29),
          ("v35", 45),
          ("x25ple", 40))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtSSA_ObjectIdentity = ObjectIdentity
ctSSA = _CtSSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497)
)
_CtDs0Mib_ObjectIdentity = ObjectIdentity
ctDs0Mib = _CtDs0Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20)
)
_CtDs0ifNumber_Type = Integer32
_CtDs0ifNumber_Object = MibScalar
ctDs0ifNumber = _CtDs0ifNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 1),
    _CtDs0ifNumber_Type()
)
ctDs0ifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifNumber.setStatus("mandatory")
_CtDs0ifTable_Object = MibTable
ctDs0ifTable = _CtDs0ifTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2)
)
if mibBuilder.loadTexts:
    ctDs0ifTable.setStatus("mandatory")
_CtDs0ifEntry_Object = MibTableRow
ctDs0ifEntry = _CtDs0ifEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1)
)
ctDs0ifEntry.setIndexNames(
    (0, "CT-DS0ent-MIB", "ctDs0ifIndex"),
)
if mibBuilder.loadTexts:
    ctDs0ifEntry.setStatus("mandatory")


class _CtDs0ifIndex_Type(InterfaceIndex):
    """Custom type ctDs0ifIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CtDs0ifIndex_Type.__name__ = "InterfaceIndex"
_CtDs0ifIndex_Object = MibTableColumn
ctDs0ifIndex = _CtDs0ifIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 1),
    _CtDs0ifIndex_Type()
)
ctDs0ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifIndex.setStatus("mandatory")


class _CtDs0ifDescr_Type(DisplayString):
    """Custom type ctDs0ifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtDs0ifDescr_Type.__name__ = "DisplayString"
_CtDs0ifDescr_Object = MibTableColumn
ctDs0ifDescr = _CtDs0ifDescr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 2),
    _CtDs0ifDescr_Type()
)
ctDs0ifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifDescr.setStatus("mandatory")
_CtDs0ifType_Type = IANActDs0ifType
_CtDs0ifType_Object = MibTableColumn
ctDs0ifType = _CtDs0ifType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 3),
    _CtDs0ifType_Type()
)
ctDs0ifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifType.setStatus("mandatory")
_CtDs0ifMtu_Type = Integer32
_CtDs0ifMtu_Object = MibTableColumn
ctDs0ifMtu = _CtDs0ifMtu_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 4),
    _CtDs0ifMtu_Type()
)
ctDs0ifMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifMtu.setStatus("mandatory")
_CtDs0ifSpeed_Type = Gauge32
_CtDs0ifSpeed_Object = MibTableColumn
ctDs0ifSpeed = _CtDs0ifSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 5),
    _CtDs0ifSpeed_Type()
)
ctDs0ifSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifSpeed.setStatus("mandatory")
_CtDs0ifPhysAddress_Type = PhysAddress
_CtDs0ifPhysAddress_Object = MibTableColumn
ctDs0ifPhysAddress = _CtDs0ifPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 6),
    _CtDs0ifPhysAddress_Type()
)
ctDs0ifPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifPhysAddress.setStatus("mandatory")


class _CtDs0ifAdminStatus_Type(Integer32):
    """Custom type ctDs0ifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_CtDs0ifAdminStatus_Type.__name__ = "Integer32"
_CtDs0ifAdminStatus_Object = MibTableColumn
ctDs0ifAdminStatus = _CtDs0ifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 7),
    _CtDs0ifAdminStatus_Type()
)
ctDs0ifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDs0ifAdminStatus.setStatus("mandatory")


class _CtDs0ifOperStatus_Type(Integer32):
    """Custom type ctDs0ifOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_CtDs0ifOperStatus_Type.__name__ = "Integer32"
_CtDs0ifOperStatus_Object = MibTableColumn
ctDs0ifOperStatus = _CtDs0ifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 8),
    _CtDs0ifOperStatus_Type()
)
ctDs0ifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifOperStatus.setStatus("mandatory")
_CtDs0ifLastChange_Type = TimeTicks
_CtDs0ifLastChange_Object = MibTableColumn
ctDs0ifLastChange = _CtDs0ifLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 9),
    _CtDs0ifLastChange_Type()
)
ctDs0ifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifLastChange.setStatus("mandatory")
_CtDs0ifInOctets_Type = Counter32
_CtDs0ifInOctets_Object = MibTableColumn
ctDs0ifInOctets = _CtDs0ifInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 10),
    _CtDs0ifInOctets_Type()
)
ctDs0ifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifInOctets.setStatus("mandatory")
_CtDs0ifInUcastPkts_Type = Counter32
_CtDs0ifInUcastPkts_Object = MibTableColumn
ctDs0ifInUcastPkts = _CtDs0ifInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 11),
    _CtDs0ifInUcastPkts_Type()
)
ctDs0ifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifInUcastPkts.setStatus("mandatory")
_CtDs0ifInNUcastPkts_Type = Counter32
_CtDs0ifInNUcastPkts_Object = MibTableColumn
ctDs0ifInNUcastPkts = _CtDs0ifInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 12),
    _CtDs0ifInNUcastPkts_Type()
)
ctDs0ifInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifInNUcastPkts.setStatus("deprecated")
_CtDs0ifInDiscards_Type = Counter32
_CtDs0ifInDiscards_Object = MibTableColumn
ctDs0ifInDiscards = _CtDs0ifInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 13),
    _CtDs0ifInDiscards_Type()
)
ctDs0ifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifInDiscards.setStatus("mandatory")
_CtDs0ifInErrors_Type = Counter32
_CtDs0ifInErrors_Object = MibTableColumn
ctDs0ifInErrors = _CtDs0ifInErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 14),
    _CtDs0ifInErrors_Type()
)
ctDs0ifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifInErrors.setStatus("mandatory")
_CtDs0ifInUnknownProtos_Type = Counter32
_CtDs0ifInUnknownProtos_Object = MibTableColumn
ctDs0ifInUnknownProtos = _CtDs0ifInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 15),
    _CtDs0ifInUnknownProtos_Type()
)
ctDs0ifInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifInUnknownProtos.setStatus("mandatory")
_CtDs0ifOutOctets_Type = Counter32
_CtDs0ifOutOctets_Object = MibTableColumn
ctDs0ifOutOctets = _CtDs0ifOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 16),
    _CtDs0ifOutOctets_Type()
)
ctDs0ifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifOutOctets.setStatus("mandatory")
_CtDs0ifOutUcastPkts_Type = Counter32
_CtDs0ifOutUcastPkts_Object = MibTableColumn
ctDs0ifOutUcastPkts = _CtDs0ifOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 17),
    _CtDs0ifOutUcastPkts_Type()
)
ctDs0ifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifOutUcastPkts.setStatus("mandatory")
_CtDs0ifOutNUcastPkts_Type = Counter32
_CtDs0ifOutNUcastPkts_Object = MibTableColumn
ctDs0ifOutNUcastPkts = _CtDs0ifOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 18),
    _CtDs0ifOutNUcastPkts_Type()
)
ctDs0ifOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifOutNUcastPkts.setStatus("deprecated")
_CtDs0ifOutDiscards_Type = Counter32
_CtDs0ifOutDiscards_Object = MibTableColumn
ctDs0ifOutDiscards = _CtDs0ifOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 19),
    _CtDs0ifOutDiscards_Type()
)
ctDs0ifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifOutDiscards.setStatus("mandatory")
_CtDs0ifOutErrors_Type = Counter32
_CtDs0ifOutErrors_Object = MibTableColumn
ctDs0ifOutErrors = _CtDs0ifOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 20),
    _CtDs0ifOutErrors_Type()
)
ctDs0ifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifOutErrors.setStatus("mandatory")
_CtDs0ifOutQLen_Type = Gauge32
_CtDs0ifOutQLen_Object = MibTableColumn
ctDs0ifOutQLen = _CtDs0ifOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 21),
    _CtDs0ifOutQLen_Type()
)
ctDs0ifOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifOutQLen.setStatus("deprecated")
_CtDs0ifSpecific_Type = ObjectIdentifier
_CtDs0ifSpecific_Object = MibTableColumn
ctDs0ifSpecific = _CtDs0ifSpecific_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 20, 2, 1, 22),
    _CtDs0ifSpecific_Type()
)
ctDs0ifSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs0ifSpecific.setStatus("deprecated")
_CtDsx0Mib_ObjectIdentity = ObjectIdentity
ctDsx0Mib = _CtDsx0Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21)
)
_CtDsx0ConfigTable_Object = MibTable
ctDsx0ConfigTable = _CtDsx0ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1)
)
if mibBuilder.loadTexts:
    ctDsx0ConfigTable.setStatus("mandatory")
_CtDsx0ConfigEntry_Object = MibTableRow
ctDsx0ConfigEntry = _CtDsx0ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 1)
)
ctDsx0ConfigEntry.setIndexNames(
    (0, "CT-DS0ent-MIB", "ctDs0ifIndex"),
)
if mibBuilder.loadTexts:
    ctDsx0ConfigEntry.setStatus("mandatory")
_CtDsx0ConfigLineId_Type = DisplayString
_CtDsx0ConfigLineId_Object = MibTableColumn
ctDsx0ConfigLineId = _CtDsx0ConfigLineId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 1, 1),
    _CtDsx0ConfigLineId_Type()
)
ctDsx0ConfigLineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDsx0ConfigLineId.setStatus("mandatory")


class _CtDsx0ConfigAdminStatus_Type(Integer32):
    """Custom type ctDsx0ConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_CtDsx0ConfigAdminStatus_Type.__name__ = "Integer32"
_CtDsx0ConfigAdminStatus_Object = MibTableColumn
ctDsx0ConfigAdminStatus = _CtDsx0ConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 1, 2),
    _CtDsx0ConfigAdminStatus_Type()
)
ctDsx0ConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDsx0ConfigAdminStatus.setStatus("mandatory")


class _CtDsx0ConfigOperStatus_Type(Integer32):
    """Custom type ctDsx0ConfigOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_CtDsx0ConfigOperStatus_Type.__name__ = "Integer32"
_CtDsx0ConfigOperStatus_Object = MibTableColumn
ctDsx0ConfigOperStatus = _CtDsx0ConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 1, 3),
    _CtDsx0ConfigOperStatus_Type()
)
ctDsx0ConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDsx0ConfigOperStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-DS0ent-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "IANActDs0ifType": IANActDs0ifType,
       "ctSSA": ctSSA,
       "ctDs0Mib": ctDs0Mib,
       "ctDs0ifNumber": ctDs0ifNumber,
       "ctDs0ifTable": ctDs0ifTable,
       "ctDs0ifEntry": ctDs0ifEntry,
       "ctDs0ifIndex": ctDs0ifIndex,
       "ctDs0ifDescr": ctDs0ifDescr,
       "ctDs0ifType": ctDs0ifType,
       "ctDs0ifMtu": ctDs0ifMtu,
       "ctDs0ifSpeed": ctDs0ifSpeed,
       "ctDs0ifPhysAddress": ctDs0ifPhysAddress,
       "ctDs0ifAdminStatus": ctDs0ifAdminStatus,
       "ctDs0ifOperStatus": ctDs0ifOperStatus,
       "ctDs0ifLastChange": ctDs0ifLastChange,
       "ctDs0ifInOctets": ctDs0ifInOctets,
       "ctDs0ifInUcastPkts": ctDs0ifInUcastPkts,
       "ctDs0ifInNUcastPkts": ctDs0ifInNUcastPkts,
       "ctDs0ifInDiscards": ctDs0ifInDiscards,
       "ctDs0ifInErrors": ctDs0ifInErrors,
       "ctDs0ifInUnknownProtos": ctDs0ifInUnknownProtos,
       "ctDs0ifOutOctets": ctDs0ifOutOctets,
       "ctDs0ifOutUcastPkts": ctDs0ifOutUcastPkts,
       "ctDs0ifOutNUcastPkts": ctDs0ifOutNUcastPkts,
       "ctDs0ifOutDiscards": ctDs0ifOutDiscards,
       "ctDs0ifOutErrors": ctDs0ifOutErrors,
       "ctDs0ifOutQLen": ctDs0ifOutQLen,
       "ctDs0ifSpecific": ctDs0ifSpecific,
       "ctDsx0Mib": ctDsx0Mib,
       "ctDsx0ConfigTable": ctDsx0ConfigTable,
       "ctDsx0ConfigEntry": ctDsx0ConfigEntry,
       "ctDsx0ConfigLineId": ctDsx0ConfigLineId,
       "ctDsx0ConfigAdminStatus": ctDsx0ConfigAdminStatus,
       "ctDsx0ConfigOperStatus": ctDsx0ConfigOperStatus}
)
