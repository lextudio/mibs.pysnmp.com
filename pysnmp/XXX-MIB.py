# SNMP MIB module (XXX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XXX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:50 2024
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

company = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6688)
)
company.setRevisions(
        ("2009-03-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpProduct_ObjectIdentity = ObjectIdentity
ipProduct = _IpProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1)
)
if mibBuilder.loadTexts:
    ipProduct.setStatus("current")
_Height2HU_ObjectIdentity = ObjectIdentity
height2HU = _Height2HU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1)
)
_SystemMIB_ObjectIdentity = ObjectIdentity
systemMIB = _SystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1)
)


class _ShelfNum_Type(Integer32):
    """Custom type shelfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ShelfNum_Type.__name__ = "Integer32"
_ShelfNum_Object = MibScalar
shelfNum = _ShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 1),
    _ShelfNum_Type()
)
shelfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfNum.setStatus("current")
_ShelfTable_Object = MibTable
shelfTable = _ShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    shelfTable.setStatus("current")
_ShelfEntry_Object = MibTableRow
shelfEntry = _ShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 2, 1)
)
shelfEntry.setIndexNames(
    (0, "XXX-MIB", "shelfName"),
)
if mibBuilder.loadTexts:
    shelfEntry.setStatus("current")


class _ShelfName_Type(Integer32):
    """Custom type shelfName based on Integer32"""
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
        *(("master", 1),
          ("slave1", 2),
          ("slave2", 3),
          ("slave3", 4))
    )


_ShelfName_Type.__name__ = "Integer32"
_ShelfName_Object = MibTableColumn
shelfName = _ShelfName_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 2, 1, 1),
    _ShelfName_Type()
)
shelfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfName.setStatus("current")


class _PsuA_Type(Integer32):
    """Custom type psuA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nc", 3),
          ("off", 2),
          ("on", 1))
    )


_PsuA_Type.__name__ = "Integer32"
_PsuA_Object = MibTableColumn
psuA = _PsuA_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 2, 1, 2),
    _PsuA_Type()
)
psuA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuA.setStatus("current")


class _PsuB_Type(Integer32):
    """Custom type psuB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nc", 3),
          ("off", 2),
          ("on", 1))
    )


_PsuB_Type.__name__ = "Integer32"
_PsuB_Object = MibTableColumn
psuB = _PsuB_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 2, 1, 3),
    _PsuB_Type()
)
psuB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuB.setStatus("current")


class _VolA_Type(Integer32):
    """Custom type volA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("nc", 3),
          ("normal", 1))
    )


_VolA_Type.__name__ = "Integer32"
_VolA_Object = MibTableColumn
volA = _VolA_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 2, 1, 4),
    _VolA_Type()
)
volA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volA.setStatus("current")


class _VolB_Type(Integer32):
    """Custom type volB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("nc", 3),
          ("normal", 1))
    )


_VolB_Type.__name__ = "Integer32"
_VolB_Object = MibTableColumn
volB = _VolB_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 2, 1, 5),
    _VolB_Type()
)
volB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volB.setStatus("current")


class _Fan_Type(Integer32):
    """Custom type fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nc", 3),
          ("off", 2),
          ("on", 1))
    )


_Fan_Type.__name__ = "Integer32"
_Fan_Object = MibTableColumn
fan = _Fan_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 2, 1, 6),
    _Fan_Type()
)
fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan.setStatus("current")
_Temperature_Type = Integer32
_Temperature_Object = MibTableColumn
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 2, 1, 7),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")
if mibBuilder.loadTexts:
    temperature.setUnits(" oC")


class _CoCardNum_Type(Integer32):
    """Custom type coCardNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CoCardNum_Type.__name__ = "Integer32"
_CoCardNum_Object = MibTableColumn
coCardNum = _CoCardNum_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 2, 1, 8),
    _CoCardNum_Type()
)
coCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCardNum.setStatus("current")


class _RmtCardNum_Type(Integer32):
    """Custom type rmtCardNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RmtCardNum_Type.__name__ = "Integer32"
_RmtCardNum_Object = MibTableColumn
rmtCardNum = _RmtCardNum_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 2, 1, 9),
    _RmtCardNum_Type()
)
rmtCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtCardNum.setStatus("current")
_SlotObjects_ObjectIdentity = ObjectIdentity
slotObjects = _SlotObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 3)
)
_SlotTable_Object = MibTable
slotTable = _SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    slotTable.setStatus("current")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 3, 1, 1)
)
slotEntry.setIndexNames(
    (0, "XXX-MIB", "shelfIdx"),
    (0, "XXX-MIB", "slotIdx"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("current")


class _ShelfIdx_Type(Integer32):
    """Custom type shelfIdx based on Integer32"""
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
        *(("master", 1),
          ("slave1", 2),
          ("slave2", 3),
          ("slave3", 4))
    )


_ShelfIdx_Type.__name__ = "Integer32"
_ShelfIdx_Object = MibTableColumn
shelfIdx = _ShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 3, 1, 1, 1),
    _ShelfIdx_Type()
)
shelfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfIdx.setStatus("current")


class _SlotIdx_Type(Integer32):
    """Custom type slotIdx based on Integer32"""
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
        *(("slot01", 1),
          ("slot02", 2),
          ("slot03", 3),
          ("slot04", 4),
          ("slot05", 5),
          ("slot06", 6),
          ("slot07", 7),
          ("slot08", 8),
          ("slot09", 9),
          ("slot10", 10),
          ("slot11", 11),
          ("slot12", 12),
          ("slot13", 13),
          ("slot14", 14),
          ("slot15", 15),
          ("slot16", 16),
          ("slot17", 17))
    )


_SlotIdx_Type.__name__ = "Integer32"
_SlotIdx_Object = MibTableColumn
slotIdx = _SlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 3, 1, 1, 2),
    _SlotIdx_Type()
)
slotIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIdx.setStatus("current")


class _CoCardType_Type(Integer32):
    """Custom type coCardType based on Integer32"""
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
              100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("fr600f-mm", 100),
          ("fr600f-ms", 101),
          ("ip113f", 2),
          ("ip113s", 1),
          ("mc-100m-sfp", 20),
          ("mc-10g-oee", 8),
          ("mc-10g-oeo", 7),
          ("mc-10g-oeo-1r", 10),
          ("mc-10g-oeo-2r", 24),
          ("mc-1g-e2o", 3),
          ("mc-1g-e2o-backup", 17),
          ("mc-1g-o2o", 4),
          ("mc-1g-o2o-backup", 21),
          ("mc-2-5g", 11),
          ("mc-2-5g-f", 14),
          ("mc-2-5g-mux-f", 16),
          ("mc-2-5g-mux-t", 15),
          ("mc-2-5g-t", 13),
          ("mc-4-25g-oeo", 5),
          ("mc-40g-oeo", 12),
          ("mc-FAN", 9),
          ("mc-cwdm-4", 22),
          ("mc-cwdm-8", 23),
          ("mc-e1-1sfp", 18),
          ("mc-e1-2sfp", 19),
          ("mc-e1t1", 26),
          ("mc-ip175d", 6),
          ("mc-qca8334", 25),
          ("no-card", 0),
          ("not-support", 102))
    )


_CoCardType_Type.__name__ = "Integer32"
_CoCardType_Object = MibTableColumn
coCardType = _CoCardType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 3, 1, 1, 3),
    _CoCardType_Type()
)
coCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coCardType.setStatus("current")
_CoCardDesc_Type = DisplayString
_CoCardDesc_Object = MibTableColumn
coCardDesc = _CoCardDesc_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 3, 1, 1, 4),
    _CoCardDesc_Type()
)
coCardDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coCardDesc.setStatus("current")


class _RmtCardType_Type(Integer32):
    """Custom type rmtCardType based on Integer32"""
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
              100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("fr600f-mm", 100),
          ("fr600f-ms", 101),
          ("ip113f", 2),
          ("ip113sr", 1),
          ("mc-100m-sfpr", 20),
          ("mc-10g-oeer", 8),
          ("mc-10g-oeo-1rr", 10),
          ("mc-10g-oeo-2rr", 24),
          ("mc-10g-oeor", 7),
          ("mc-1g-e2o", 3),
          ("mc-1g-e2o-backupr", 17),
          ("mc-1g-o2o", 4),
          ("mc-1g-o2o-backupr", 21),
          ("mc-2-5g-fr", 14),
          ("mc-2-5g-mux-fr", 16),
          ("mc-2-5g-mux-tr", 15),
          ("mc-2-5g-tr", 13),
          ("mc-2-5gr", 11),
          ("mc-4-25g-oeor", 5),
          ("mc-40g-oeor", 12),
          ("mc-FANr", 9),
          ("mc-cwdmr-4", 22),
          ("mc-cwdmr-8", 23),
          ("mc-e1-1sfpr", 18),
          ("mc-e1-2sfpr", 19),
          ("mc-e1t1r", 26),
          ("mc-ip175dr", 6),
          ("mc-qca8334r", 25),
          ("no-card", 0),
          ("not-support", 102))
    )


_RmtCardType_Type.__name__ = "Integer32"
_RmtCardType_Object = MibTableColumn
rmtCardType = _RmtCardType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 3, 1, 1, 5),
    _RmtCardType_Type()
)
rmtCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtCardType.setStatus("current")
_RmtCardDesc_Type = DisplayString
_RmtCardDesc_Object = MibTableColumn
rmtCardDesc = _RmtCardDesc_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 3, 1, 1, 6),
    _RmtCardDesc_Type()
)
rmtCardDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtCardDesc.setStatus("current")
_CardObjects_ObjectIdentity = ObjectIdentity
cardObjects = _CardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4)
)
_NmuObjects_ObjectIdentity = ObjectIdentity
nmuObjects = _NmuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 1)
)
_NmuConfig_ObjectIdentity = ObjectIdentity
nmuConfig = _NmuConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 1, 1)
)


class _NmuType_Type(Integer32):
    """Custom type nmuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("fr600f-mm", 100),
          ("fr600f-ms", 101),
          ("not-support", 102))
    )


_NmuType_Type.__name__ = "Integer32"
_NmuType_Object = MibScalar
nmuType = _NmuType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 1, 1, 1),
    _NmuType_Type()
)
nmuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmuType.setStatus("current")
_Ipaddr_Type = IpAddress
_Ipaddr_Object = MibScalar
ipaddr = _Ipaddr_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 1, 1, 2),
    _Ipaddr_Type()
)
ipaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddr.setStatus("current")
_Subnet_Type = IpAddress
_Subnet_Object = MibScalar
subnet = _Subnet_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 1, 1, 3),
    _Subnet_Type()
)
subnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnet.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 1, 1, 4),
    _Gateway_Type()
)
gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_SysContact_Type = DisplayString
_SysContact_Object = MibScalar
sysContact = _SysContact_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 1, 1, 5),
    _SysContact_Type()
)
sysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContact.setStatus("current")
_SysName_Type = DisplayString
_SysName_Object = MibScalar
sysName = _SysName_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 1, 1, 6),
    _SysName_Type()
)
sysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysName.setStatus("current")
_SysLocation_Type = DisplayString
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 1, 1, 7),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocation.setStatus("current")
_TrapHost1_Type = IpAddress
_TrapHost1_Object = MibScalar
trapHost1 = _TrapHost1_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 1, 1, 8),
    _TrapHost1_Type()
)
trapHost1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapHost1.setStatus("current")
_TrapHost2_Type = IpAddress
_TrapHost2_Object = MibScalar
trapHost2 = _TrapHost2_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 1, 1, 9),
    _TrapHost2_Type()
)
trapHost2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapHost2.setStatus("current")
_TrapHost3_Type = IpAddress
_TrapHost3_Object = MibScalar
trapHost3 = _TrapHost3_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 1, 1, 10),
    _TrapHost3_Type()
)
trapHost3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapHost3.setStatus("current")
_TrapHost4_Type = IpAddress
_TrapHost4_Object = MibScalar
trapHost4 = _TrapHost4_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 1, 1, 11),
    _TrapHost4_Type()
)
trapHost4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapHost4.setStatus("current")
_McCmObjects_ObjectIdentity = ObjectIdentity
mcCmObjects = _McCmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2)
)
_McCmTable_Object = MibTable
mcCmTable = _McCmTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mcCmTable.setStatus("current")
_McCmEntry_Object = MibTableRow
mcCmEntry = _McCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1)
)
mcCmEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mcCmEntry.setStatus("current")


class _McShelfIdx_Type(Integer32):
    """Custom type mcShelfIdx based on Integer32"""
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
        *(("master", 1),
          ("slave1", 2),
          ("slave2", 3),
          ("slave3", 4))
    )


_McShelfIdx_Type.__name__ = "Integer32"
_McShelfIdx_Object = MibTableColumn
mcShelfIdx = _McShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 1),
    _McShelfIdx_Type()
)
mcShelfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcShelfIdx.setStatus("current")


class _McCardIdx_Type(Integer32):
    """Custom type mcCardIdx based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15),
          ("card16", 16))
    )


_McCardIdx_Type.__name__ = "Integer32"
_McCardIdx_Object = MibTableColumn
mcCardIdx = _McCardIdx_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 2),
    _McCardIdx_Type()
)
mcCardIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcCardIdx.setStatus("current")


class _McType_Type(Integer32):
    """Custom type mcType based on Integer32"""
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
              26)
        )
    )
    namedValues = NamedValues(
        *(("ip113f", 2),
          ("ip113s", 1),
          ("mc-100m-sfp", 20),
          ("mc-10g-oee", 8),
          ("mc-10g-oeo", 7),
          ("mc-10g-oeo-1r", 10),
          ("mc-10g-oeo-2r", 24),
          ("mc-1g-e2o", 3),
          ("mc-1g-e2o-backup", 17),
          ("mc-1g-o2o", 4),
          ("mc-1g-o2o-backup", 21),
          ("mc-2-5g", 11),
          ("mc-2-5g-f", 14),
          ("mc-2-5g-mux-f", 16),
          ("mc-2-5g-mux-t", 15),
          ("mc-2-5g-t", 13),
          ("mc-4-25g-oeo", 5),
          ("mc-40g-oeo", 12),
          ("mc-FAN", 9),
          ("mc-cwdm-4", 22),
          ("mc-cwdm-8", 23),
          ("mc-e1-1sfp", 18),
          ("mc-e1-2sfp", 19),
          ("mc-e1t1", 26),
          ("mc-ip175d", 6),
          ("mc-qca8334", 25),
          ("no-card", 0))
    )


_McType_Type.__name__ = "Integer32"
_McType_Object = MibTableColumn
mcType = _McType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 3),
    _McType_Type()
)
mcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcType.setStatus("current")


class _McTransceiverMode_Type(Integer32):
    """Custom type mcTransceiverMode based on Integer32"""
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
        *(("bidi", 1),
          ("duplex-fiber", 2),
          ("not-support", 4),
          ("sfp", 3))
    )


_McTransceiverMode_Type.__name__ = "Integer32"
_McTransceiverMode_Object = MibTableColumn
mcTransceiverMode = _McTransceiverMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 4),
    _McTransceiverMode_Type()
)
mcTransceiverMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTransceiverMode.setStatus("current")


class _McTransceiverDist_Type(Integer32):
    """Custom type mcTransceiverDist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_McTransceiverDist_Type.__name__ = "Integer32"
_McTransceiverDist_Object = MibTableColumn
mcTransceiverDist = _McTransceiverDist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 5),
    _McTransceiverDist_Type()
)
mcTransceiverDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTransceiverDist.setStatus("current")


class _McPortState_Type(Integer32):
    """Custom type mcPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("not-support", 3),
          ("unlocked", 2))
    )


_McPortState_Type.__name__ = "Integer32"
_McPortState_Object = MibTableColumn
mcPortState = _McPortState_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 6),
    _McPortState_Type()
)
mcPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcPortState.setStatus("current")


class _McTransmitMode_Type(Integer32):
    """Custom type mcTransmitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cut-through", 1),
          ("not-support", 3),
          ("store-forward", 2))
    )


_McTransmitMode_Type.__name__ = "Integer32"
_McTransmitMode_Object = MibTableColumn
mcTransmitMode = _McTransmitMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 7),
    _McTransmitMode_Type()
)
mcTransmitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcTransmitMode.setStatus("current")


class _McCurWorkMode_Type(Integer32):
    """Custom type mcCurWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("not-support", 7))
    )


_McCurWorkMode_Type.__name__ = "Integer32"
_McCurWorkMode_Object = MibTableColumn
mcCurWorkMode = _McCurWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 8),
    _McCurWorkMode_Type()
)
mcCurWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcCurWorkMode.setStatus("mandatory")


class _McCfgWorkMode_Type(Integer32):
    """Custom type mcCfgWorkMode based on Integer32"""
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
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("mAuto", 1),
          ("not-support", 7))
    )


_McCfgWorkMode_Type.__name__ = "Integer32"
_McCfgWorkMode_Object = MibTableColumn
mcCfgWorkMode = _McCfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 9),
    _McCfgWorkMode_Type()
)
mcCfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcCfgWorkMode.setStatus("mandatory")


class _McLFPCfg_Type(Integer32):
    """Custom type mcLFPCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_McLFPCfg_Type.__name__ = "Integer32"
_McLFPCfg_Object = MibTableColumn
mcLFPCfg = _McLFPCfg_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 10),
    _McLFPCfg_Type()
)
mcLFPCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcLFPCfg.setStatus("current")
_McUpStream_Type = Gauge32
_McUpStream_Object = MibTableColumn
mcUpStream = _McUpStream_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 11),
    _McUpStream_Type()
)
mcUpStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcUpStream.setStatus("current")
_McDownStream_Type = Gauge32
_McDownStream_Object = MibTableColumn
mcDownStream = _McDownStream_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 12),
    _McDownStream_Type()
)
mcDownStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcDownStream.setStatus("current")


class _McTxlink_Type(Integer32):
    """Custom type mcTxlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_McTxlink_Type.__name__ = "Integer32"
_McTxlink_Object = MibTableColumn
mcTxlink = _McTxlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 13),
    _McTxlink_Type()
)
mcTxlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTxlink.setStatus("current")


class _McFxlink_Type(Integer32):
    """Custom type mcFxlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_McFxlink_Type.__name__ = "Integer32"
_McFxlink_Object = MibTableColumn
mcFxlink = _McFxlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 14),
    _McFxlink_Type()
)
mcFxlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcFxlink.setStatus("current")


class _McHWLFP_Type(Integer32):
    """Custom type mcHWLFP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_McHWLFP_Type.__name__ = "Integer32"
_McHWLFP_Object = MibTableColumn
mcHWLFP = _McHWLFP_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 15),
    _McHWLFP_Type()
)
mcHWLFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcHWLFP.setStatus("current")


class _McHWTransmitMode_Type(Integer32):
    """Custom type mcHWTransmitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cut-through", 1),
          ("not-support", 3),
          ("store-forward", 2))
    )


_McHWTransmitMode_Type.__name__ = "Integer32"
_McHWTransmitMode_Object = MibTableColumn
mcHWTransmitMode = _McHWTransmitMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 16),
    _McHWTransmitMode_Type()
)
mcHWTransmitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcHWTransmitMode.setStatus("current")


class _McHWWorkMode_Type(Integer32):
    """Custom type mcHWWorkMode based on Integer32"""
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
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("mAuto", 1),
          ("not-support", 7))
    )


_McHWWorkMode_Type.__name__ = "Integer32"
_McHWWorkMode_Object = MibTableColumn
mcHWWorkMode = _McHWWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 17),
    _McHWWorkMode_Type()
)
mcHWWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcHWWorkMode.setStatus("current")


class _McHWRmtCtrlMode_Type(Integer32):
    """Custom type mcHWRmtCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_McHWRmtCtrlMode_Type.__name__ = "Integer32"
_McHWRmtCtrlMode_Object = MibTableColumn
mcHWRmtCtrlMode = _McHWRmtCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 18),
    _McHWRmtCtrlMode_Type()
)
mcHWRmtCtrlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcHWRmtCtrlMode.setStatus("current")


class _McNtwSfpExist_Type(Integer32):
    """Custom type mcNtwSfpExist based on Integer32"""
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
        *(("inserted", 1),
          ("na", 3),
          ("not-support", 4),
          ("removed", 2))
    )


_McNtwSfpExist_Type.__name__ = "Integer32"
_McNtwSfpExist_Object = MibTableColumn
mcNtwSfpExist = _McNtwSfpExist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 19),
    _McNtwSfpExist_Type()
)
mcNtwSfpExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcNtwSfpExist.setStatus("current")


class _McAccSfpExist_Type(Integer32):
    """Custom type mcAccSfpExist based on Integer32"""
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
        *(("inserted", 1),
          ("na", 3),
          ("not-support", 4),
          ("removed", 2))
    )


_McAccSfpExist_Type.__name__ = "Integer32"
_McAccSfpExist_Object = MibTableColumn
mcAccSfpExist = _McAccSfpExist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 20),
    _McAccSfpExist_Type()
)
mcAccSfpExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcAccSfpExist.setStatus("current")


class _McUtility_Type(Integer32):
    """Custom type mcUtility based on Integer32"""
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
        *(("default", 3),
          ("idle", 1),
          ("not-support", 5),
          ("reset", 2),
          ("set2hw", 4))
    )


_McUtility_Type.__name__ = "Integer32"
_McUtility_Object = MibTableColumn
mcUtility = _McUtility_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 21),
    _McUtility_Type()
)
mcUtility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcUtility.setStatus("current")


class _McRmtDetect_Type(Integer32):
    """Custom type mcRmtDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-remote", 0),
          ("not-support", 2),
          ("yes", 1))
    )


_McRmtDetect_Type.__name__ = "Integer32"
_McRmtDetect_Object = MibTableColumn
mcRmtDetect = _McRmtDetect_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 22),
    _McRmtDetect_Type()
)
mcRmtDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtDetect.setStatus("current")


class _McRmtType_Type(Integer32):
    """Custom type mcRmtType based on Integer32"""
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
              26)
        )
    )
    namedValues = NamedValues(
        *(("ip113f", 2),
          ("ip113sr", 1),
          ("mc-100m-sfpr", 20),
          ("mc-10g-oeer", 8),
          ("mc-10g-oeo-1rr", 10),
          ("mc-10g-oeo-2rr", 24),
          ("mc-10g-oeor", 7),
          ("mc-1g-e2o-backupr", 17),
          ("mc-1g-e2or", 3),
          ("mc-1g-o2o-backupr", 21),
          ("mc-1g-o2or", 4),
          ("mc-2-5g-fr", 14),
          ("mc-2-5g-mux-fr", 16),
          ("mc-2-5g-mux-tr", 15),
          ("mc-2-5g-tr", 13),
          ("mc-2-5gr", 11),
          ("mc-4-25g-oeor", 5),
          ("mc-40g-oeor", 12),
          ("mc-FANr", 9),
          ("mc-cwdmr-4", 22),
          ("mc-cwdmr-8", 23),
          ("mc-e1-1sfpr", 18),
          ("mc-e1-2sfpr", 19),
          ("mc-e1t1r", 26),
          ("mc-ip175dr", 6),
          ("mc-qca8334r", 25),
          ("no-card", 0))
    )


_McRmtType_Type.__name__ = "Integer32"
_McRmtType_Object = MibTableColumn
mcRmtType = _McRmtType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 23),
    _McRmtType_Type()
)
mcRmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtType.setStatus("current")


class _McRmtTransmitMode_Type(Integer32):
    """Custom type mcRmtTransmitMode based on Integer32"""
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
        *(("cut-through", 1),
          ("no-card", 0),
          ("not-support", 3),
          ("store-forward", 2))
    )


_McRmtTransmitMode_Type.__name__ = "Integer32"
_McRmtTransmitMode_Object = MibTableColumn
mcRmtTransmitMode = _McRmtTransmitMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 24),
    _McRmtTransmitMode_Type()
)
mcRmtTransmitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmtTransmitMode.setStatus("current")


class _McRmtCurWorkMode_Type(Integer32):
    """Custom type mcRmtCurWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("no-card", 0),
          ("not-support", 7))
    )


_McRmtCurWorkMode_Type.__name__ = "Integer32"
_McRmtCurWorkMode_Object = MibTableColumn
mcRmtCurWorkMode = _McRmtCurWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 25),
    _McRmtCurWorkMode_Type()
)
mcRmtCurWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtCurWorkMode.setStatus("mandatory")


class _McRmtCfgWorkMode_Type(Integer32):
    """Custom type mcRmtCfgWorkMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("mAuto", 1),
          ("no-card", 0),
          ("not-support", 7))
    )


_McRmtCfgWorkMode_Type.__name__ = "Integer32"
_McRmtCfgWorkMode_Object = MibTableColumn
mcRmtCfgWorkMode = _McRmtCfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 26),
    _McRmtCfgWorkMode_Type()
)
mcRmtCfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmtCfgWorkMode.setStatus("mandatory")


class _McRmtLFP_Type(Integer32):
    """Custom type mcRmtLFP based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("no-card", 0),
          ("not-support", 3))
    )


_McRmtLFP_Type.__name__ = "Integer32"
_McRmtLFP_Object = MibTableColumn
mcRmtLFP = _McRmtLFP_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 27),
    _McRmtLFP_Type()
)
mcRmtLFP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmtLFP.setStatus("current")


class _McRmtTxlink_Type(Integer32):
    """Custom type mcRmtTxlink based on Integer32"""
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
        *(("down", 2),
          ("no-card", 0),
          ("not-support", 3),
          ("up", 1))
    )


_McRmtTxlink_Type.__name__ = "Integer32"
_McRmtTxlink_Object = MibTableColumn
mcRmtTxlink = _McRmtTxlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 28),
    _McRmtTxlink_Type()
)
mcRmtTxlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtTxlink.setStatus("current")


class _McRmtHWLFP_Type(Integer32):
    """Custom type mcRmtHWLFP based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("no-card", 0),
          ("not-support", 3))
    )


_McRmtHWLFP_Type.__name__ = "Integer32"
_McRmtHWLFP_Object = MibTableColumn
mcRmtHWLFP = _McRmtHWLFP_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 29),
    _McRmtHWLFP_Type()
)
mcRmtHWLFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtHWLFP.setStatus("current")


class _McRmtHWTransmitMode_Type(Integer32):
    """Custom type mcRmtHWTransmitMode based on Integer32"""
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
        *(("cut-through", 1),
          ("no-card", 0),
          ("not-support", 3),
          ("store-forward", 2))
    )


_McRmtHWTransmitMode_Type.__name__ = "Integer32"
_McRmtHWTransmitMode_Object = MibTableColumn
mcRmtHWTransmitMode = _McRmtHWTransmitMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 30),
    _McRmtHWTransmitMode_Type()
)
mcRmtHWTransmitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtHWTransmitMode.setStatus("current")


class _McRmtHWWorkMode_Type(Integer32):
    """Custom type mcRmtHWWorkMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("mAuto", 1),
          ("no-card", 0),
          ("not-support", 7))
    )


_McRmtHWWorkMode_Type.__name__ = "Integer32"
_McRmtHWWorkMode_Object = MibTableColumn
mcRmtHWWorkMode = _McRmtHWWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 31),
    _McRmtHWWorkMode_Type()
)
mcRmtHWWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtHWWorkMode.setStatus("current")


class _McRmtLoopback_Type(Integer32):
    """Custom type mcRmtLoopback based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("no-card", 0),
          ("not-support", 3))
    )


_McRmtLoopback_Type.__name__ = "Integer32"
_McRmtLoopback_Object = MibTableColumn
mcRmtLoopback = _McRmtLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 32),
    _McRmtLoopback_Type()
)
mcRmtLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmtLoopback.setStatus("current")


class _McRmtPwrDown_Type(Integer32):
    """Custom type mcRmtPwrDown based on Integer32"""
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
        *(("no-card", 0),
          ("normal", 2),
          ("not-support", 3),
          ("powerdown", 1))
    )


_McRmtPwrDown_Type.__name__ = "Integer32"
_McRmtPwrDown_Object = MibTableColumn
mcRmtPwrDown = _McRmtPwrDown_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 33),
    _McRmtPwrDown_Type()
)
mcRmtPwrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtPwrDown.setStatus("current")


class _McRmtAccSfpExist_Type(Integer32):
    """Custom type mcRmtAccSfpExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("na", 3),
          ("no-card", 0),
          ("removed", 2),
          ("support", 4))
    )


_McRmtAccSfpExist_Type.__name__ = "Integer32"
_McRmtAccSfpExist_Object = MibTableColumn
mcRmtAccSfpExist = _McRmtAccSfpExist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 34),
    _McRmtAccSfpExist_Type()
)
mcRmtAccSfpExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtAccSfpExist.setStatus("current")


class _McRmtUtility_Type(Integer32):
    """Custom type mcRmtUtility based on Integer32"""
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
        *(("default", 3),
          ("idle", 1),
          ("no-card", 0),
          ("not-support", 5),
          ("reset", 2),
          ("set2hw", 4))
    )


_McRmtUtility_Type.__name__ = "Integer32"
_McRmtUtility_Object = MibTableColumn
mcRmtUtility = _McRmtUtility_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 1, 1, 35),
    _McRmtUtility_Type()
)
mcRmtUtility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmtUtility.setStatus("current")
_McCm1gSpecificObjects_ObjectIdentity = ObjectIdentity
mcCm1gSpecificObjects = _McCm1gSpecificObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2)
)
_McCm1gIpObjects_ObjectIdentity = ObjectIdentity
mcCm1gIpObjects = _McCm1gIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 1)
)
_McCm1gIpTable_Object = MibTable
mcCm1gIpTable = _McCm1gIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mcCm1gIpTable.setStatus("current")
_McCm1gIpEntry_Object = MibTableRow
mcCm1gIpEntry = _McCm1gIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 1, 1, 1)
)
mcCm1gIpEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
    (0, "XXX-MIB", "mcLoOrRmtFg"),
)
if mibBuilder.loadTexts:
    mcCm1gIpEntry.setStatus("current")


class _McLoOrRmtFg_Type(Integer32):
    """Custom type mcLoOrRmtFg based on Integer32"""
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


_McLoOrRmtFg_Type.__name__ = "Integer32"
_McLoOrRmtFg_Object = MibTableColumn
mcLoOrRmtFg = _McLoOrRmtFg_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 1, 1, 1, 1),
    _McLoOrRmtFg_Type()
)
mcLoOrRmtFg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcLoOrRmtFg.setStatus("current")
_McIpAddr_Type = IpAddress
_McIpAddr_Object = MibTableColumn
mcIpAddr = _McIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 1, 1, 1, 2),
    _McIpAddr_Type()
)
mcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcIpAddr.setStatus("current")
_McCm1gSfpObjects_ObjectIdentity = ObjectIdentity
mcCm1gSfpObjects = _McCm1gSfpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2)
)
_McCm1gSfpTable_Object = MibTable
mcCm1gSfpTable = _McCm1gSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mcCm1gSfpTable.setStatus("current")
_McCm1gSfpEntry_Object = MibTableRow
mcCm1gSfpEntry = _McCm1gSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1)
)
mcCm1gSfpEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
    (0, "XXX-MIB", "mcLoOrRmtFg"),
)
if mibBuilder.loadTexts:
    mcCm1gSfpEntry.setStatus("current")


class _GetSfpCmd_Type(Integer32):
    """Custom type getSfpCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("na", 0),
          ("remote", 2))
    )


_GetSfpCmd_Type.__name__ = "Integer32"
_GetSfpCmd_Object = MibTableColumn
getSfpCmd = _GetSfpCmd_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1, 1),
    _GetSfpCmd_Type()
)
getSfpCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getSfpCmd.setStatus("current")
_SfpCompliance_Type = Integer32
_SfpCompliance_Object = MibTableColumn
sfpCompliance = _SfpCompliance_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1, 2),
    _SfpCompliance_Type()
)
sfpCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpCompliance.setStatus("current")
_SfpConnector_Type = Integer32
_SfpConnector_Object = MibTableColumn
sfpConnector = _SfpConnector_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1, 3),
    _SfpConnector_Type()
)
sfpConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConnector.setStatus("current")
_SfpTransCode_Type = Integer32
_SfpTransCode_Object = MibTableColumn
sfpTransCode = _SfpTransCode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1, 4),
    _SfpTransCode_Type()
)
sfpTransCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTransCode.setStatus("current")
_SfpSmLength_Type = Integer32
_SfpSmLength_Object = MibTableColumn
sfpSmLength = _SfpSmLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1, 5),
    _SfpSmLength_Type()
)
sfpSmLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpSmLength.setStatus("current")
_SfpMmLength_Type = Integer32
_SfpMmLength_Object = MibTableColumn
sfpMmLength = _SfpMmLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1, 6),
    _SfpMmLength_Type()
)
sfpMmLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpMmLength.setStatus("current")
_SfpCopperLength_Type = Integer32
_SfpCopperLength_Object = MibTableColumn
sfpCopperLength = _SfpCopperLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1, 7),
    _SfpCopperLength_Type()
)
sfpCopperLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpCopperLength.setStatus("current")
_SfpBrSpeed_Type = Integer32
_SfpBrSpeed_Object = MibTableColumn
sfpBrSpeed = _SfpBrSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1, 8),
    _SfpBrSpeed_Type()
)
sfpBrSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpBrSpeed.setStatus("current")
_SfpWavelength_Type = Integer32
_SfpWavelength_Object = MibTableColumn
sfpWavelength = _SfpWavelength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1, 9),
    _SfpWavelength_Type()
)
sfpWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpWavelength.setStatus("current")
_SfpTemperature_Type = Integer32
_SfpTemperature_Object = MibTableColumn
sfpTemperature = _SfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1, 10),
    _SfpTemperature_Type()
)
sfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTemperature.setStatus("current")
_SfpTranPower_Type = Integer32
_SfpTranPower_Object = MibTableColumn
sfpTranPower = _SfpTranPower_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1, 11),
    _SfpTranPower_Type()
)
sfpTranPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTranPower.setStatus("current")
_SfpRecvPower_Type = Integer32
_SfpRecvPower_Object = MibTableColumn
sfpRecvPower = _SfpRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1, 12),
    _SfpRecvPower_Type()
)
sfpRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRecvPower.setStatus("current")
_SfpVoltage_Type = Integer32
_SfpVoltage_Object = MibTableColumn
sfpVoltage = _SfpVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 2, 1, 1, 13),
    _SfpVoltage_Type()
)
sfpVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVoltage.setStatus("current")
_McCm1gAccSfpObjects_ObjectIdentity = ObjectIdentity
mcCm1gAccSfpObjects = _McCm1gAccSfpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3)
)
_McCm1gAccSfpTable_Object = MibTable
mcCm1gAccSfpTable = _McCm1gAccSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mcCm1gAccSfpTable.setStatus("current")
_McCm1gAccSfpEntry_Object = MibTableRow
mcCm1gAccSfpEntry = _McCm1gAccSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1)
)
mcCm1gAccSfpEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
    (0, "XXX-MIB", "mcLoOrRmtFg"),
)
if mibBuilder.loadTexts:
    mcCm1gAccSfpEntry.setStatus("current")


class _GetAccSfpCmd_Type(Integer32):
    """Custom type getAccSfpCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("na", 0),
          ("remote", 2))
    )


_GetAccSfpCmd_Type.__name__ = "Integer32"
_GetAccSfpCmd_Object = MibTableColumn
getAccSfpCmd = _GetAccSfpCmd_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1, 1),
    _GetAccSfpCmd_Type()
)
getAccSfpCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getAccSfpCmd.setStatus("current")
_AccsfpCompliance_Type = Integer32
_AccsfpCompliance_Object = MibTableColumn
accsfpCompliance = _AccsfpCompliance_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1, 2),
    _AccsfpCompliance_Type()
)
accsfpCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accsfpCompliance.setStatus("current")
_AccsfpConnector_Type = Integer32
_AccsfpConnector_Object = MibTableColumn
accsfpConnector = _AccsfpConnector_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1, 3),
    _AccsfpConnector_Type()
)
accsfpConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accsfpConnector.setStatus("current")
_AccsfpTransCode_Type = Integer32
_AccsfpTransCode_Object = MibTableColumn
accsfpTransCode = _AccsfpTransCode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1, 4),
    _AccsfpTransCode_Type()
)
accsfpTransCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accsfpTransCode.setStatus("current")
_AccsfpSmLength_Type = Integer32
_AccsfpSmLength_Object = MibTableColumn
accsfpSmLength = _AccsfpSmLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1, 5),
    _AccsfpSmLength_Type()
)
accsfpSmLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accsfpSmLength.setStatus("current")
_AccsfpMmLength_Type = Integer32
_AccsfpMmLength_Object = MibTableColumn
accsfpMmLength = _AccsfpMmLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1, 6),
    _AccsfpMmLength_Type()
)
accsfpMmLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accsfpMmLength.setStatus("current")
_AccsfpCopperLength_Type = Integer32
_AccsfpCopperLength_Object = MibTableColumn
accsfpCopperLength = _AccsfpCopperLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1, 7),
    _AccsfpCopperLength_Type()
)
accsfpCopperLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accsfpCopperLength.setStatus("current")
_AccsfpBrSpeed_Type = Integer32
_AccsfpBrSpeed_Object = MibTableColumn
accsfpBrSpeed = _AccsfpBrSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1, 8),
    _AccsfpBrSpeed_Type()
)
accsfpBrSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accsfpBrSpeed.setStatus("current")
_AccsfpWavelength_Type = Integer32
_AccsfpWavelength_Object = MibTableColumn
accsfpWavelength = _AccsfpWavelength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1, 9),
    _AccsfpWavelength_Type()
)
accsfpWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accsfpWavelength.setStatus("current")
_AccsfpTemperature_Type = Integer32
_AccsfpTemperature_Object = MibTableColumn
accsfpTemperature = _AccsfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1, 10),
    _AccsfpTemperature_Type()
)
accsfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accsfpTemperature.setStatus("current")
_AccsfpTranPower_Type = Integer32
_AccsfpTranPower_Object = MibTableColumn
accsfpTranPower = _AccsfpTranPower_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1, 11),
    _AccsfpTranPower_Type()
)
accsfpTranPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accsfpTranPower.setStatus("current")
_AccsfpRecvPower_Type = Integer32
_AccsfpRecvPower_Object = MibTableColumn
accsfpRecvPower = _AccsfpRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1, 12),
    _AccsfpRecvPower_Type()
)
accsfpRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accsfpRecvPower.setStatus("current")
_AccsfpVoltage_Type = Integer32
_AccsfpVoltage_Object = MibTableColumn
accsfpVoltage = _AccsfpVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 2, 3, 1, 1, 13),
    _AccsfpVoltage_Type()
)
accsfpVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accsfpVoltage.setStatus("current")
_McIP175DObjects_ObjectIdentity = ObjectIdentity
mcIP175DObjects = _McIP175DObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3)
)
_McIP175DCardObjects_ObjectIdentity = ObjectIdentity
mcIP175DCardObjects = _McIP175DCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 1)
)
_McIP175DCardTable_Object = MibTable
mcIP175DCardTable = _McIP175DCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mcIP175DCardTable.setStatus("current")
_McIP175DCardEntry_Object = MibTableRow
mcIP175DCardEntry = _McIP175DCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 1, 1, 1)
)
mcIP175DCardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mcIP175DCardEntry.setStatus("current")


class _McIP175DVlanMode_Type(Integer32):
    """Custom type mcIP175DVlanMode based on Integer32"""
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
        *(("Normal", 1),
          ("mode1", 2),
          ("mode2", 3),
          ("not-support", 4))
    )


_McIP175DVlanMode_Type.__name__ = "Integer32"
_McIP175DVlanMode_Object = MibTableColumn
mcIP175DVlanMode = _McIP175DVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 1, 1, 1, 1),
    _McIP175DVlanMode_Type()
)
mcIP175DVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcIP175DVlanMode.setStatus("current")
_McIP175DPortObjects_ObjectIdentity = ObjectIdentity
mcIP175DPortObjects = _McIP175DPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 2)
)
_McIP175DPortTable_Object = MibTable
mcIP175DPortTable = _McIP175DPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mcIP175DPortTable.setStatus("current")
_McIP175DPortEntry_Object = MibTableRow
mcIP175DPortEntry = _McIP175DPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 2, 1, 1)
)
mcIP175DPortEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
    (0, "XXX-MIB", "mcIP175DPortIdx"),
)
if mibBuilder.loadTexts:
    mcIP175DPortEntry.setStatus("current")


class _McIP175DPortIdx_Type(Integer32):
    """Custom type mcIP175DPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port1", 1),
          ("port2", 2))
    )


_McIP175DPortIdx_Type.__name__ = "Integer32"
_McIP175DPortIdx_Object = MibTableColumn
mcIP175DPortIdx = _McIP175DPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 2, 1, 1, 1),
    _McIP175DPortIdx_Type()
)
mcIP175DPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcIP175DPortIdx.setStatus("current")


class _McIP175DCurWorkMode_Type(Integer32):
    """Custom type mcIP175DCurWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("not-support", 7))
    )


_McIP175DCurWorkMode_Type.__name__ = "Integer32"
_McIP175DCurWorkMode_Object = MibTableColumn
mcIP175DCurWorkMode = _McIP175DCurWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 2, 1, 1, 2),
    _McIP175DCurWorkMode_Type()
)
mcIP175DCurWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcIP175DCurWorkMode.setStatus("mandatory")


class _McIP175DCfgWorkMode_Type(Integer32):
    """Custom type mcIP175DCfgWorkMode based on Integer32"""
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
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("mAuto", 1),
          ("not-support", 7))
    )


_McIP175DCfgWorkMode_Type.__name__ = "Integer32"
_McIP175DCfgWorkMode_Object = MibTableColumn
mcIP175DCfgWorkMode = _McIP175DCfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 2, 1, 1, 3),
    _McIP175DCfgWorkMode_Type()
)
mcIP175DCfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcIP175DCfgWorkMode.setStatus("mandatory")


class _McIP175DUpStream_Type(Gauge32):
    """Custom type mcIP175DUpStream based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 100000),
    )


_McIP175DUpStream_Type.__name__ = "Gauge32"
_McIP175DUpStream_Object = MibTableColumn
mcIP175DUpStream = _McIP175DUpStream_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 2, 1, 1, 4),
    _McIP175DUpStream_Type()
)
mcIP175DUpStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcIP175DUpStream.setStatus("current")


class _McIP175DDownStream_Type(Gauge32):
    """Custom type mcIP175DDownStream based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 100000),
    )


_McIP175DDownStream_Type.__name__ = "Gauge32"
_McIP175DDownStream_Object = MibTableColumn
mcIP175DDownStream = _McIP175DDownStream_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 2, 1, 1, 5),
    _McIP175DDownStream_Type()
)
mcIP175DDownStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcIP175DDownStream.setStatus("current")


class _McIP175DTxlink_Type(Integer32):
    """Custom type mcIP175DTxlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_McIP175DTxlink_Type.__name__ = "Integer32"
_McIP175DTxlink_Object = MibTableColumn
mcIP175DTxlink = _McIP175DTxlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 2, 1, 1, 6),
    _McIP175DTxlink_Type()
)
mcIP175DTxlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcIP175DTxlink.setStatus("current")


class _McIP175DRmtCurWorkMode_Type(Integer32):
    """Custom type mcIP175DRmtCurWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("no-card", 0),
          ("not-support", 7))
    )


_McIP175DRmtCurWorkMode_Type.__name__ = "Integer32"
_McIP175DRmtCurWorkMode_Object = MibTableColumn
mcIP175DRmtCurWorkMode = _McIP175DRmtCurWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 2, 1, 1, 7),
    _McIP175DRmtCurWorkMode_Type()
)
mcIP175DRmtCurWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcIP175DRmtCurWorkMode.setStatus("mandatory")


class _McIP175DRmtCfgWorkMode_Type(Integer32):
    """Custom type mcIP175DRmtCfgWorkMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("mAuto", 1),
          ("no-card", 0),
          ("not-support", 7))
    )


_McIP175DRmtCfgWorkMode_Type.__name__ = "Integer32"
_McIP175DRmtCfgWorkMode_Object = MibTableColumn
mcIP175DRmtCfgWorkMode = _McIP175DRmtCfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 2, 1, 1, 8),
    _McIP175DRmtCfgWorkMode_Type()
)
mcIP175DRmtCfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcIP175DRmtCfgWorkMode.setStatus("mandatory")


class _McIP175DRmtTxlink_Type(Integer32):
    """Custom type mcIP175DRmtTxlink based on Integer32"""
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
        *(("down", 2),
          ("no-card", 0),
          ("not-support", 3),
          ("up", 1))
    )


_McIP175DRmtTxlink_Type.__name__ = "Integer32"
_McIP175DRmtTxlink_Object = MibTableColumn
mcIP175DRmtTxlink = _McIP175DRmtTxlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 3, 2, 1, 1, 9),
    _McIP175DRmtTxlink_Type()
)
mcIP175DRmtTxlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcIP175DRmtTxlink.setStatus("current")
_Mc4_25G_OEOObjects_ObjectIdentity = ObjectIdentity
mc4_25G_OEOObjects = _Mc4_25G_OEOObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4)
)
_Mc4_25G_OEOCardObjects_ObjectIdentity = ObjectIdentity
mc4_25G_OEOCardObjects = _Mc4_25G_OEOCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1)
)
_Mc4_25G_OEOCardTable_Object = MibTable
mc4_25G_OEOCardTable = _Mc4_25G_OEOCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    mc4_25G_OEOCardTable.setStatus("current")
_Mc4_25G_OEOCardEntry_Object = MibTableRow
mc4_25G_OEOCardEntry = _Mc4_25G_OEOCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1)
)
mc4_25G_OEOCardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mc4_25G_OEOCardEntry.setStatus("current")


class _Mc4_25G_OEOCurSpdMode_Type(Integer32):
    """Custom type mc4_25G_OEOCurSpdMode based on Integer32"""
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
        *(("ESCOM", 10),
          ("FCx1", 7),
          ("FCx2", 6),
          ("FCx4", 5),
          ("FE", 9),
          ("GE", 8),
          ("Infini", 1),
          ("STM1", 4),
          ("STM16", 2),
          ("STM4", 3),
          ("not-support", 11))
    )


_Mc4_25G_OEOCurSpdMode_Type.__name__ = "Integer32"
_Mc4_25G_OEOCurSpdMode_Object = MibScalar
mc4_25G_OEOCurSpdMode = _Mc4_25G_OEOCurSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 1),
    _Mc4_25G_OEOCurSpdMode_Type()
)
mc4_25G_OEOCurSpdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc4_25G_OEOCurSpdMode.setStatus("mandatory")


class _Mc4_25G_OEOCfgSpdMode_Type(Integer32):
    """Custom type mc4_25G_OEOCfgSpdMode based on Integer32"""
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
        *(("ESCOM", 10),
          ("FCx1", 7),
          ("FCx2", 6),
          ("FCx4", 5),
          ("FE", 9),
          ("GE", 8),
          ("Infini", 1),
          ("STM1", 4),
          ("STM16", 2),
          ("STM4", 3),
          ("not-support", 11))
    )


_Mc4_25G_OEOCfgSpdMode_Type.__name__ = "Integer32"
_Mc4_25G_OEOCfgSpdMode_Object = MibScalar
mc4_25G_OEOCfgSpdMode = _Mc4_25G_OEOCfgSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 2),
    _Mc4_25G_OEOCfgSpdMode_Type()
)
mc4_25G_OEOCfgSpdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc4_25G_OEOCfgSpdMode.setStatus("mandatory")


class _Mc4_25G_OEOLoopback_Type(Integer32):
    """Custom type mc4_25G_OEOLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_Mc4_25G_OEOLoopback_Type.__name__ = "Integer32"
_Mc4_25G_OEOLoopback_Object = MibScalar
mc4_25G_OEOLoopback = _Mc4_25G_OEOLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 3),
    _Mc4_25G_OEOLoopback_Type()
)
mc4_25G_OEOLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc4_25G_OEOLoopback.setStatus("current")


class _Mc4_25G_OEOWorkMode_Type(Integer32):
    """Custom type mc4_25G_OEOWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 3),
          ("repeater", 1),
          ("retimer", 2))
    )


_Mc4_25G_OEOWorkMode_Type.__name__ = "Integer32"
_Mc4_25G_OEOWorkMode_Object = MibScalar
mc4_25G_OEOWorkMode = _Mc4_25G_OEOWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 4),
    _Mc4_25G_OEOWorkMode_Type()
)
mc4_25G_OEOWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc4_25G_OEOWorkMode.setStatus("current")


class _Mc4_25G_OEONtwPD_Type(Integer32):
    """Custom type mc4_25G_OEONtwPD based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc4_25G_OEONtwPD_Type.__name__ = "Integer32"
_Mc4_25G_OEONtwPD_Object = MibScalar
mc4_25G_OEONtwPD = _Mc4_25G_OEONtwPD_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 5),
    _Mc4_25G_OEONtwPD_Type()
)
mc4_25G_OEONtwPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc4_25G_OEONtwPD.setStatus("current")


class _Mc4_25G_OEOAccPD_Type(Integer32):
    """Custom type mc4_25G_OEOAccPD based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc4_25G_OEOAccPD_Type.__name__ = "Integer32"
_Mc4_25G_OEOAccPD_Object = MibScalar
mc4_25G_OEOAccPD = _Mc4_25G_OEOAccPD_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 6),
    _Mc4_25G_OEOAccPD_Type()
)
mc4_25G_OEOAccPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc4_25G_OEOAccPD.setStatus("current")


class _Mc4_25G_OEOHWSpdMode_Type(Integer32):
    """Custom type mc4_25G_OEOHWSpdMode based on Integer32"""
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
        *(("ESCOM", 10),
          ("FCx1", 7),
          ("FCx2", 6),
          ("FCx4", 5),
          ("FE", 9),
          ("GE", 8),
          ("Infini", 1),
          ("STM1", 4),
          ("STM16", 2),
          ("STM4", 3),
          ("not-support", 11))
    )


_Mc4_25G_OEOHWSpdMode_Type.__name__ = "Integer32"
_Mc4_25G_OEOHWSpdMode_Object = MibScalar
mc4_25G_OEOHWSpdMode = _Mc4_25G_OEOHWSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 7),
    _Mc4_25G_OEOHWSpdMode_Type()
)
mc4_25G_OEOHWSpdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc4_25G_OEOHWSpdMode.setStatus("current")


class _Mc4_25G_OEOHWLoopback_Type(Integer32):
    """Custom type mc4_25G_OEOHWLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_Mc4_25G_OEOHWLoopback_Type.__name__ = "Integer32"
_Mc4_25G_OEOHWLoopback_Object = MibScalar
mc4_25G_OEOHWLoopback = _Mc4_25G_OEOHWLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 8),
    _Mc4_25G_OEOHWLoopback_Type()
)
mc4_25G_OEOHWLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc4_25G_OEOHWLoopback.setStatus("current")


class _Mc4_25G_OEOHWWorkMode_Type(Integer32):
    """Custom type mc4_25G_OEOHWWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 3),
          ("repeater", 1),
          ("retimer", 2))
    )


_Mc4_25G_OEOHWWorkMode_Type.__name__ = "Integer32"
_Mc4_25G_OEOHWWorkMode_Object = MibScalar
mc4_25G_OEOHWWorkMode = _Mc4_25G_OEOHWWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 9),
    _Mc4_25G_OEOHWWorkMode_Type()
)
mc4_25G_OEOHWWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc4_25G_OEOHWWorkMode.setStatus("current")


class _Mc4_25G_OEO_Test_Lock_Type(Integer32):
    """Custom type mc4_25G_OEO_Test_Lock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Lock", 1),
          ("Unlock", 2))
    )


_Mc4_25G_OEO_Test_Lock_Type.__name__ = "Integer32"
_Mc4_25G_OEO_Test_Lock_Object = MibScalar
mc4_25G_OEO_Test_Lock = _Mc4_25G_OEO_Test_Lock_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 10),
    _Mc4_25G_OEO_Test_Lock_Type()
)
mc4_25G_OEO_Test_Lock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc4_25G_OEO_Test_Lock.setStatus("current")
_Mc4_25G_OEO_Test_Error_Counter_Type = Integer32
_Mc4_25G_OEO_Test_Error_Counter_Object = MibScalar
mc4_25G_OEO_Test_Error_Counter = _Mc4_25G_OEO_Test_Error_Counter_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 11),
    _Mc4_25G_OEO_Test_Error_Counter_Type()
)
mc4_25G_OEO_Test_Error_Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc4_25G_OEO_Test_Error_Counter.setStatus("current")
_Mc4_25G_OEO_Test_Continue_Time_Type = Integer32
_Mc4_25G_OEO_Test_Continue_Time_Object = MibScalar
mc4_25G_OEO_Test_Continue_Time = _Mc4_25G_OEO_Test_Continue_Time_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 12),
    _Mc4_25G_OEO_Test_Continue_Time_Type()
)
mc4_25G_OEO_Test_Continue_Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc4_25G_OEO_Test_Continue_Time.setStatus("current")


class _Mc4_25G_OEO_Test_Result_Type(Integer32):
    """Custom type mc4_25G_OEO_Test_Result based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Error", 2),
          ("Pass", 1))
    )


_Mc4_25G_OEO_Test_Result_Type.__name__ = "Integer32"
_Mc4_25G_OEO_Test_Result_Object = MibScalar
mc4_25G_OEO_Test_Result = _Mc4_25G_OEO_Test_Result_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 13),
    _Mc4_25G_OEO_Test_Result_Type()
)
mc4_25G_OEO_Test_Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc4_25G_OEO_Test_Result.setStatus("current")


class _Mc4_25G_OEO_Start_Test_Type(Integer32):
    """Custom type mc4_25G_OEO_Start_Test based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Start", 1),
          ("Stop", 2))
    )


_Mc4_25G_OEO_Start_Test_Type.__name__ = "Integer32"
_Mc4_25G_OEO_Start_Test_Object = MibScalar
mc4_25G_OEO_Start_Test = _Mc4_25G_OEO_Start_Test_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 14),
    _Mc4_25G_OEO_Start_Test_Type()
)
mc4_25G_OEO_Start_Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc4_25G_OEO_Start_Test.setStatus("current")


class _Mc4_25G_OEO_Get_Test_Rst_Type(Integer32):
    """Custom type mc4_25G_OEO_Get_Test_Rst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("Get", 1)
    )


_Mc4_25G_OEO_Get_Test_Rst_Type.__name__ = "Integer32"
_Mc4_25G_OEO_Get_Test_Rst_Object = MibScalar
mc4_25G_OEO_Get_Test_Rst = _Mc4_25G_OEO_Get_Test_Rst_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 15),
    _Mc4_25G_OEO_Get_Test_Rst_Type()
)
mc4_25G_OEO_Get_Test_Rst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc4_25G_OEO_Get_Test_Rst.setStatus("current")


class _McRmt4_25G_OEOCurSpdMode_Type(Integer32):
    """Custom type mcRmt4_25G_OEOCurSpdMode based on Integer32"""
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
        *(("ESCOM", 10),
          ("FCx1", 7),
          ("FCx2", 6),
          ("FCx4", 5),
          ("FE", 9),
          ("GE", 8),
          ("Infini", 1),
          ("STM1", 4),
          ("STM16", 2),
          ("STM4", 3),
          ("not-support", 11))
    )


_McRmt4_25G_OEOCurSpdMode_Type.__name__ = "Integer32"
_McRmt4_25G_OEOCurSpdMode_Object = MibScalar
mcRmt4_25G_OEOCurSpdMode = _McRmt4_25G_OEOCurSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 16),
    _McRmt4_25G_OEOCurSpdMode_Type()
)
mcRmt4_25G_OEOCurSpdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmt4_25G_OEOCurSpdMode.setStatus("mandatory")


class _McRmt4_25G_OEOCfgSpdMode_Type(Integer32):
    """Custom type mcRmt4_25G_OEOCfgSpdMode based on Integer32"""
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
        *(("ESCOM", 10),
          ("FCx1", 7),
          ("FCx2", 6),
          ("FCx4", 5),
          ("FE", 9),
          ("GE", 8),
          ("Infini", 1),
          ("STM1", 4),
          ("STM16", 2),
          ("STM4", 3),
          ("not-support", 11))
    )


_McRmt4_25G_OEOCfgSpdMode_Type.__name__ = "Integer32"
_McRmt4_25G_OEOCfgSpdMode_Object = MibScalar
mcRmt4_25G_OEOCfgSpdMode = _McRmt4_25G_OEOCfgSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 17),
    _McRmt4_25G_OEOCfgSpdMode_Type()
)
mcRmt4_25G_OEOCfgSpdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmt4_25G_OEOCfgSpdMode.setStatus("mandatory")


class _McRmt4_25G_OEOLoopback_Type(Integer32):
    """Custom type mcRmt4_25G_OEOLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_McRmt4_25G_OEOLoopback_Type.__name__ = "Integer32"
_McRmt4_25G_OEOLoopback_Object = MibScalar
mcRmt4_25G_OEOLoopback = _McRmt4_25G_OEOLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 18),
    _McRmt4_25G_OEOLoopback_Type()
)
mcRmt4_25G_OEOLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmt4_25G_OEOLoopback.setStatus("current")


class _McRmt4_25G_OEOWorkMode_Type(Integer32):
    """Custom type mcRmt4_25G_OEOWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 3),
          ("repeater", 1),
          ("retimer", 2))
    )


_McRmt4_25G_OEOWorkMode_Type.__name__ = "Integer32"
_McRmt4_25G_OEOWorkMode_Object = MibScalar
mcRmt4_25G_OEOWorkMode = _McRmt4_25G_OEOWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 19),
    _McRmt4_25G_OEOWorkMode_Type()
)
mcRmt4_25G_OEOWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmt4_25G_OEOWorkMode.setStatus("current")


class _McRmt4_25G_OEOHWSpdMode_Type(Integer32):
    """Custom type mcRmt4_25G_OEOHWSpdMode based on Integer32"""
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
        *(("ESCOM", 10),
          ("FCx1", 7),
          ("FCx2", 6),
          ("FCx4", 5),
          ("FE", 9),
          ("GE", 8),
          ("Infini", 1),
          ("STM1", 4),
          ("STM16", 2),
          ("STM4", 3),
          ("not-support", 11))
    )


_McRmt4_25G_OEOHWSpdMode_Type.__name__ = "Integer32"
_McRmt4_25G_OEOHWSpdMode_Object = MibScalar
mcRmt4_25G_OEOHWSpdMode = _McRmt4_25G_OEOHWSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 20),
    _McRmt4_25G_OEOHWSpdMode_Type()
)
mcRmt4_25G_OEOHWSpdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmt4_25G_OEOHWSpdMode.setStatus("current")


class _McRmt4_25G_OEOHWLoopback_Type(Integer32):
    """Custom type mcRmt4_25G_OEOHWLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_McRmt4_25G_OEOHWLoopback_Type.__name__ = "Integer32"
_McRmt4_25G_OEOHWLoopback_Object = MibScalar
mcRmt4_25G_OEOHWLoopback = _McRmt4_25G_OEOHWLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 21),
    _McRmt4_25G_OEOHWLoopback_Type()
)
mcRmt4_25G_OEOHWLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmt4_25G_OEOHWLoopback.setStatus("current")


class _McRmt4_25G_OEOHWWorkMode_Type(Integer32):
    """Custom type mcRmt4_25G_OEOHWWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 3),
          ("repeater", 1),
          ("retimer", 2))
    )


_McRmt4_25G_OEOHWWorkMode_Type.__name__ = "Integer32"
_McRmt4_25G_OEOHWWorkMode_Object = MibScalar
mcRmt4_25G_OEOHWWorkMode = _McRmt4_25G_OEOHWWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 4, 1, 1, 1, 22),
    _McRmt4_25G_OEOHWWorkMode_Type()
)
mcRmt4_25G_OEOHWWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmt4_25G_OEOHWWorkMode.setStatus("current")
_Mc10G_OEOObjects_ObjectIdentity = ObjectIdentity
mc10G_OEOObjects = _Mc10G_OEOObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5)
)
_Mc10G_OEOCardObjects_ObjectIdentity = ObjectIdentity
mc10G_OEOCardObjects = _Mc10G_OEOCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1)
)
_Mc10G_OEOCardTable_Object = MibTable
mc10G_OEOCardTable = _Mc10G_OEOCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    mc10G_OEOCardTable.setStatus("current")
_Mc10G_OEOCardEntry_Object = MibTableRow
mc10G_OEOCardEntry = _Mc10G_OEOCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1)
)
mc10G_OEOCardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mc10G_OEOCardEntry.setStatus("current")


class _Mc10G_OEOCurSpdMode_Type(Integer32):
    """Custom type mc10G_OEOCurSpdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("LAN", 1),
          ("WAN", 2),
          ("not-support", 4))
    )


_Mc10G_OEOCurSpdMode_Type.__name__ = "Integer32"
_Mc10G_OEOCurSpdMode_Object = MibScalar
mc10G_OEOCurSpdMode = _Mc10G_OEOCurSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 1),
    _Mc10G_OEOCurSpdMode_Type()
)
mc10G_OEOCurSpdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEOCurSpdMode.setStatus("mandatory")


class _Mc10G_OEOCfgSpdMode_Type(Integer32):
    """Custom type mc10G_OEOCfgSpdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("LAN", 1),
          ("WAN", 2),
          ("not-support", 4))
    )


_Mc10G_OEOCfgSpdMode_Type.__name__ = "Integer32"
_Mc10G_OEOCfgSpdMode_Object = MibScalar
mc10G_OEOCfgSpdMode = _Mc10G_OEOCfgSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 2),
    _Mc10G_OEOCfgSpdMode_Type()
)
mc10G_OEOCfgSpdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc10G_OEOCfgSpdMode.setStatus("mandatory")


class _Mc10G_OEOLoopback_Type(Integer32):
    """Custom type mc10G_OEOLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_Mc10G_OEOLoopback_Type.__name__ = "Integer32"
_Mc10G_OEOLoopback_Object = MibScalar
mc10G_OEOLoopback = _Mc10G_OEOLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 3),
    _Mc10G_OEOLoopback_Type()
)
mc10G_OEOLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc10G_OEOLoopback.setStatus("current")


class _Mc10G_OEOSFP1_Type(Integer32):
    """Custom type mc10G_OEOSFP1 based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc10G_OEOSFP1_Type.__name__ = "Integer32"
_Mc10G_OEOSFP1_Object = MibScalar
mc10G_OEOSFP1 = _Mc10G_OEOSFP1_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 4),
    _Mc10G_OEOSFP1_Type()
)
mc10G_OEOSFP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEOSFP1.setStatus("current")


class _Mc10G_OEOSFP2_Type(Integer32):
    """Custom type mc10G_OEOSFP2 based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc10G_OEOSFP2_Type.__name__ = "Integer32"
_Mc10G_OEOSFP2_Object = MibScalar
mc10G_OEOSFP2 = _Mc10G_OEOSFP2_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 5),
    _Mc10G_OEOSFP2_Type()
)
mc10G_OEOSFP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEOSFP2.setStatus("current")


class _Mc10G_OEOHWSpdMode_Type(Integer32):
    """Custom type mc10G_OEOHWSpdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("LAN", 1),
          ("WAN", 2),
          ("not-support", 4))
    )


_Mc10G_OEOHWSpdMode_Type.__name__ = "Integer32"
_Mc10G_OEOHWSpdMode_Object = MibScalar
mc10G_OEOHWSpdMode = _Mc10G_OEOHWSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 6),
    _Mc10G_OEOHWSpdMode_Type()
)
mc10G_OEOHWSpdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEOHWSpdMode.setStatus("current")


class _Mc10G_OEOHWLoopback_Type(Integer32):
    """Custom type mc10G_OEOHWLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_Mc10G_OEOHWLoopback_Type.__name__ = "Integer32"
_Mc10G_OEOHWLoopback_Object = MibScalar
mc10G_OEOHWLoopback = _Mc10G_OEOHWLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 7),
    _Mc10G_OEOHWLoopback_Type()
)
mc10G_OEOHWLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEOHWLoopback.setStatus("current")


class _Mc10G_OEO_Test_Lock_Type(Integer32):
    """Custom type mc10G_OEO_Test_Lock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Lock", 1),
          ("Unlock", 2))
    )


_Mc10G_OEO_Test_Lock_Type.__name__ = "Integer32"
_Mc10G_OEO_Test_Lock_Object = MibScalar
mc10G_OEO_Test_Lock = _Mc10G_OEO_Test_Lock_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 8),
    _Mc10G_OEO_Test_Lock_Type()
)
mc10G_OEO_Test_Lock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO_Test_Lock.setStatus("current")
_Mc10G_OEO_Test_Error_Counter_Type = Integer32
_Mc10G_OEO_Test_Error_Counter_Object = MibScalar
mc10G_OEO_Test_Error_Counter = _Mc10G_OEO_Test_Error_Counter_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 9),
    _Mc10G_OEO_Test_Error_Counter_Type()
)
mc10G_OEO_Test_Error_Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO_Test_Error_Counter.setStatus("current")
_Mc10G_OEO_Test_Continue_Time_Type = Integer32
_Mc10G_OEO_Test_Continue_Time_Object = MibScalar
mc10G_OEO_Test_Continue_Time = _Mc10G_OEO_Test_Continue_Time_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 10),
    _Mc10G_OEO_Test_Continue_Time_Type()
)
mc10G_OEO_Test_Continue_Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO_Test_Continue_Time.setStatus("current")


class _Mc10G_OEO_Test_Result_Type(Integer32):
    """Custom type mc10G_OEO_Test_Result based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Error", 2),
          ("Pass", 1))
    )


_Mc10G_OEO_Test_Result_Type.__name__ = "Integer32"
_Mc10G_OEO_Test_Result_Object = MibScalar
mc10G_OEO_Test_Result = _Mc10G_OEO_Test_Result_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 11),
    _Mc10G_OEO_Test_Result_Type()
)
mc10G_OEO_Test_Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO_Test_Result.setStatus("current")


class _Mc10G_OEO_Start_Test_Type(Integer32):
    """Custom type mc10G_OEO_Start_Test based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Start", 1),
          ("Stop", 2))
    )


_Mc10G_OEO_Start_Test_Type.__name__ = "Integer32"
_Mc10G_OEO_Start_Test_Object = MibScalar
mc10G_OEO_Start_Test = _Mc10G_OEO_Start_Test_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 12),
    _Mc10G_OEO_Start_Test_Type()
)
mc10G_OEO_Start_Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc10G_OEO_Start_Test.setStatus("current")


class _Mc10G_OEO_Get_Test_Rst_Type(Integer32):
    """Custom type mc10G_OEO_Get_Test_Rst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("Get", 1)
    )


_Mc10G_OEO_Get_Test_Rst_Type.__name__ = "Integer32"
_Mc10G_OEO_Get_Test_Rst_Object = MibScalar
mc10G_OEO_Get_Test_Rst = _Mc10G_OEO_Get_Test_Rst_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 13),
    _Mc10G_OEO_Get_Test_Rst_Type()
)
mc10G_OEO_Get_Test_Rst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc10G_OEO_Get_Test_Rst.setStatus("current")


class _McRmt10G_OEOCurSpdMode_Type(Integer32):
    """Custom type mcRmt10G_OEOCurSpdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("LAN", 1),
          ("WAN", 2),
          ("not-support", 4))
    )


_McRmt10G_OEOCurSpdMode_Type.__name__ = "Integer32"
_McRmt10G_OEOCurSpdMode_Object = MibScalar
mcRmt10G_OEOCurSpdMode = _McRmt10G_OEOCurSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 14),
    _McRmt10G_OEOCurSpdMode_Type()
)
mcRmt10G_OEOCurSpdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmt10G_OEOCurSpdMode.setStatus("mandatory")


class _McRmt10G_OEOCfgSpdMode_Type(Integer32):
    """Custom type mcRmt10G_OEOCfgSpdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("LAN", 1),
          ("WAN", 2),
          ("not-support", 4))
    )


_McRmt10G_OEOCfgSpdMode_Type.__name__ = "Integer32"
_McRmt10G_OEOCfgSpdMode_Object = MibScalar
mcRmt10G_OEOCfgSpdMode = _McRmt10G_OEOCfgSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 15),
    _McRmt10G_OEOCfgSpdMode_Type()
)
mcRmt10G_OEOCfgSpdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmt10G_OEOCfgSpdMode.setStatus("mandatory")


class _McRmt10G_OEOLoopback_Type(Integer32):
    """Custom type mcRmt10G_OEOLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_McRmt10G_OEOLoopback_Type.__name__ = "Integer32"
_McRmt10G_OEOLoopback_Object = MibScalar
mcRmt10G_OEOLoopback = _McRmt10G_OEOLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 16),
    _McRmt10G_OEOLoopback_Type()
)
mcRmt10G_OEOLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmt10G_OEOLoopback.setStatus("current")


class _McRmt10G_OEOHWSpdMode_Type(Integer32):
    """Custom type mcRmt10G_OEOHWSpdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("LAN", 1),
          ("WAN", 2),
          ("not-support", 4))
    )


_McRmt10G_OEOHWSpdMode_Type.__name__ = "Integer32"
_McRmt10G_OEOHWSpdMode_Object = MibScalar
mcRmt10G_OEOHWSpdMode = _McRmt10G_OEOHWSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 17),
    _McRmt10G_OEOHWSpdMode_Type()
)
mcRmt10G_OEOHWSpdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmt10G_OEOHWSpdMode.setStatus("current")


class _McRmt10G_OEOHWLoopback_Type(Integer32):
    """Custom type mcRmt10G_OEOHWLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_McRmt10G_OEOHWLoopback_Type.__name__ = "Integer32"
_McRmt10G_OEOHWLoopback_Object = MibScalar
mcRmt10G_OEOHWLoopback = _McRmt10G_OEOHWLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 18),
    _McRmt10G_OEOHWLoopback_Type()
)
mcRmt10G_OEOHWLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmt10G_OEOHWLoopback.setStatus("current")


class _McRmt10G_OEOSFP1_Type(Integer32):
    """Custom type mcRmt10G_OEOSFP1 based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_McRmt10G_OEOSFP1_Type.__name__ = "Integer32"
_McRmt10G_OEOSFP1_Object = MibScalar
mcRmt10G_OEOSFP1 = _McRmt10G_OEOSFP1_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 19),
    _McRmt10G_OEOSFP1_Type()
)
mcRmt10G_OEOSFP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmt10G_OEOSFP1.setStatus("current")


class _Mc10G_OEO_accType_Type(Integer32):
    """Custom type mc10G_OEO_accType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("SFP", 2),
          ("XFP", 1),
          ("unknow", 3))
    )


_Mc10G_OEO_accType_Type.__name__ = "Integer32"
_Mc10G_OEO_accType_Object = MibScalar
mc10G_OEO_accType = _Mc10G_OEO_accType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 20),
    _Mc10G_OEO_accType_Type()
)
mc10G_OEO_accType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO_accType.setStatus("current")


class _Mc10G_OEO_ntwType_Type(Integer32):
    """Custom type mc10G_OEO_ntwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("SFP", 2),
          ("XFP", 1),
          ("unknow", 3))
    )


_Mc10G_OEO_ntwType_Type.__name__ = "Integer32"
_Mc10G_OEO_ntwType_Object = MibScalar
mc10G_OEO_ntwType = _Mc10G_OEO_ntwType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 21),
    _Mc10G_OEO_ntwType_Type()
)
mc10G_OEO_ntwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO_ntwType.setStatus("current")


class _McRmt10G_OEO_accType_Type(Integer32):
    """Custom type mcRmt10G_OEO_accType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("SFP", 2),
          ("XFP", 1),
          ("unknow", 3))
    )


_McRmt10G_OEO_accType_Type.__name__ = "Integer32"
_McRmt10G_OEO_accType_Object = MibScalar
mcRmt10G_OEO_accType = _McRmt10G_OEO_accType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 22),
    _McRmt10G_OEO_accType_Type()
)
mcRmt10G_OEO_accType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmt10G_OEO_accType.setStatus("current")


class _McRmt10G_OEO_ntwType_Type(Integer32):
    """Custom type mcRmt10G_OEO_ntwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("SFP", 2),
          ("XFP", 1),
          ("unknow", 3))
    )


_McRmt10G_OEO_ntwType_Type.__name__ = "Integer32"
_McRmt10G_OEO_ntwType_Object = MibScalar
mcRmt10G_OEO_ntwType = _McRmt10G_OEO_ntwType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 5, 1, 1, 1, 23),
    _McRmt10G_OEO_ntwType_Type()
)
mcRmt10G_OEO_ntwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmt10G_OEO_ntwType.setStatus("current")
_Mc10G_OEEObjects_ObjectIdentity = ObjectIdentity
mc10G_OEEObjects = _Mc10G_OEEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 6)
)
_Mc10G_OEECardObjects_ObjectIdentity = ObjectIdentity
mc10G_OEECardObjects = _Mc10G_OEECardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 6, 1)
)
_Mc10G_OEECardTable_Object = MibTable
mc10G_OEECardTable = _Mc10G_OEECardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    mc10G_OEECardTable.setStatus("current")
_Mc10G_OEECardEntry_Object = MibTableRow
mc10G_OEECardEntry = _Mc10G_OEECardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 6, 1, 1, 1)
)
mc10G_OEECardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mc10G_OEECardEntry.setStatus("current")


class _Mc10G_OEETxlink_Type(Integer32):
    """Custom type mc10G_OEETxlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc10G_OEETxlink_Type.__name__ = "Integer32"
_Mc10G_OEETxlink_Object = MibScalar
mc10G_OEETxlink = _Mc10G_OEETxlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 6, 1, 1, 1, 1),
    _Mc10G_OEETxlink_Type()
)
mc10G_OEETxlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEETxlink.setStatus("mandatory")


class _Mc10G_OEEFxlink_Type(Integer32):
    """Custom type mc10G_OEEFxlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc10G_OEEFxlink_Type.__name__ = "Integer32"
_Mc10G_OEEFxlink_Object = MibScalar
mc10G_OEEFxlink = _Mc10G_OEEFxlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 6, 1, 1, 1, 2),
    _Mc10G_OEEFxlink_Type()
)
mc10G_OEEFxlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEEFxlink.setStatus("mandatory")


class _Mc10G_OEECurSpd_Type(Integer32):
    """Custom type mc10G_OEECurSpd based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m10G-Master", 7),
          ("m10G-Slave", 8),
          ("m1G-full", 6),
          ("mAuto", 1),
          ("no-card", 0),
          ("not-support", 9))
    )


_Mc10G_OEECurSpd_Type.__name__ = "Integer32"
_Mc10G_OEECurSpd_Object = MibScalar
mc10G_OEECurSpd = _Mc10G_OEECurSpd_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 6, 1, 1, 1, 3),
    _Mc10G_OEECurSpd_Type()
)
mc10G_OEECurSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEECurSpd.setStatus("mandatory")


class _Mc10G_OEELoopMode_Type(Integer32):
    """Custom type mc10G_OEELoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_Mc10G_OEELoopMode_Type.__name__ = "Integer32"
_Mc10G_OEELoopMode_Object = MibScalar
mc10G_OEELoopMode = _Mc10G_OEELoopMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 6, 1, 1, 1, 4),
    _Mc10G_OEELoopMode_Type()
)
mc10G_OEELoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc10G_OEELoopMode.setStatus("current")


class _Mc10G_OEESpdMode_Type(Integer32):
    """Custom type mc10G_OEESpdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("m10G-Master", 7),
          ("m10G-Slave", 8))
    )


_Mc10G_OEESpdMode_Type.__name__ = "Integer32"
_Mc10G_OEESpdMode_Object = MibScalar
mc10G_OEESpdMode = _Mc10G_OEESpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 6, 1, 1, 1, 5),
    _Mc10G_OEESpdMode_Type()
)
mc10G_OEESpdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc10G_OEESpdMode.setStatus("current")


class _Mc10G_OEEHWLoopback_Type(Integer32):
    """Custom type mc10G_OEEHWLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_Mc10G_OEEHWLoopback_Type.__name__ = "Integer32"
_Mc10G_OEEHWLoopback_Object = MibScalar
mc10G_OEEHWLoopback = _Mc10G_OEEHWLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 6, 1, 1, 1, 6),
    _Mc10G_OEEHWLoopback_Type()
)
mc10G_OEEHWLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEEHWLoopback.setStatus("current")


class _Mc10G_OEE_ntwType_Type(Integer32):
    """Custom type mc10G_OEE_ntwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("SFP", 2),
          ("XFP", 1),
          ("unknow", 3))
    )


_Mc10G_OEE_ntwType_Type.__name__ = "Integer32"
_Mc10G_OEE_ntwType_Object = MibScalar
mc10G_OEE_ntwType = _Mc10G_OEE_ntwType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 6, 1, 1, 1, 7),
    _Mc10G_OEE_ntwType_Type()
)
mc10G_OEE_ntwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEE_ntwType.setStatus("current")
_Mc10G_OEE_checkResult_Type = Integer32
_Mc10G_OEE_checkResult_Object = MibScalar
mc10G_OEE_checkResult = _Mc10G_OEE_checkResult_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 6, 1, 1, 1, 8),
    _Mc10G_OEE_checkResult_Type()
)
mc10G_OEE_checkResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEE_checkResult.setStatus("current")
_McFanObjects_ObjectIdentity = ObjectIdentity
mcFanObjects = _McFanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 7)
)
_McFanCardObjects_ObjectIdentity = ObjectIdentity
mcFanCardObjects = _McFanCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 7, 1)
)
_McFanCardTable_Object = MibTable
mcFanCardTable = _McFanCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    mcFanCardTable.setStatus("current")
_McFanCardEntry_Object = MibTableRow
mcFanCardEntry = _McFanCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 7, 1, 1, 1)
)
mcFanCardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mcFanCardEntry.setStatus("current")


class _McFanStatus_Type(Integer32):
    """Custom type mcFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Abnormal", 2),
          ("Normal", 1),
          ("not-support", 3))
    )


_McFanStatus_Type.__name__ = "Integer32"
_McFanStatus_Object = MibTableColumn
mcFanStatus = _McFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 7, 1, 1, 1, 1),
    _McFanStatus_Type()
)
mcFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcFanStatus.setStatus("mandatory")
_Mc40G_OEOObjects_ObjectIdentity = ObjectIdentity
mc40G_OEOObjects = _Mc40G_OEOObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8)
)
_Mc40G_OEOCardObjects_ObjectIdentity = ObjectIdentity
mc40G_OEOCardObjects = _Mc40G_OEOCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1)
)
_Mc40G_OEOCardTable_Object = MibTable
mc40G_OEOCardTable = _Mc40G_OEOCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    mc40G_OEOCardTable.setStatus("current")
_Mc40G_OEOCardEntry_Object = MibTableRow
mc40G_OEOCardEntry = _Mc40G_OEOCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1)
)
mc40G_OEOCardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mc40G_OEOCardEntry.setStatus("current")


class _Mc40G_OEOQsfp1Lane1_link_Type(Integer32):
    """Custom type mc40G_OEOQsfp1Lane1_link based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc40G_OEOQsfp1Lane1_link_Type.__name__ = "Integer32"
_Mc40G_OEOQsfp1Lane1_link_Object = MibScalar
mc40G_OEOQsfp1Lane1_link = _Mc40G_OEOQsfp1Lane1_link_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 1),
    _Mc40G_OEOQsfp1Lane1_link_Type()
)
mc40G_OEOQsfp1Lane1_link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc40G_OEOQsfp1Lane1_link.setStatus("mandatory")


class _Mc40G_OEOQsfp1Lane2_link_Type(Integer32):
    """Custom type mc40G_OEOQsfp1Lane2_link based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc40G_OEOQsfp1Lane2_link_Type.__name__ = "Integer32"
_Mc40G_OEOQsfp1Lane2_link_Object = MibScalar
mc40G_OEOQsfp1Lane2_link = _Mc40G_OEOQsfp1Lane2_link_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 2),
    _Mc40G_OEOQsfp1Lane2_link_Type()
)
mc40G_OEOQsfp1Lane2_link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc40G_OEOQsfp1Lane2_link.setStatus("mandatory")


class _Mc40G_OEOQsfp1Lane3_link_Type(Integer32):
    """Custom type mc40G_OEOQsfp1Lane3_link based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc40G_OEOQsfp1Lane3_link_Type.__name__ = "Integer32"
_Mc40G_OEOQsfp1Lane3_link_Object = MibScalar
mc40G_OEOQsfp1Lane3_link = _Mc40G_OEOQsfp1Lane3_link_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 3),
    _Mc40G_OEOQsfp1Lane3_link_Type()
)
mc40G_OEOQsfp1Lane3_link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc40G_OEOQsfp1Lane3_link.setStatus("mandatory")


class _Mc40G_OEOQsfp1Lane4_link_Type(Integer32):
    """Custom type mc40G_OEOQsfp1Lane4_link based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc40G_OEOQsfp1Lane4_link_Type.__name__ = "Integer32"
_Mc40G_OEOQsfp1Lane4_link_Object = MibScalar
mc40G_OEOQsfp1Lane4_link = _Mc40G_OEOQsfp1Lane4_link_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 4),
    _Mc40G_OEOQsfp1Lane4_link_Type()
)
mc40G_OEOQsfp1Lane4_link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc40G_OEOQsfp1Lane4_link.setStatus("mandatory")


class _Mc40G_OEOQsfp2Lane1_link_Type(Integer32):
    """Custom type mc40G_OEOQsfp2Lane1_link based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc40G_OEOQsfp2Lane1_link_Type.__name__ = "Integer32"
_Mc40G_OEOQsfp2Lane1_link_Object = MibScalar
mc40G_OEOQsfp2Lane1_link = _Mc40G_OEOQsfp2Lane1_link_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 5),
    _Mc40G_OEOQsfp2Lane1_link_Type()
)
mc40G_OEOQsfp2Lane1_link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc40G_OEOQsfp2Lane1_link.setStatus("mandatory")


class _Mc40G_OEOQsfp2Lane2_link_Type(Integer32):
    """Custom type mc40G_OEOQsfp2Lane2_link based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc40G_OEOQsfp2Lane2_link_Type.__name__ = "Integer32"
_Mc40G_OEOQsfp2Lane2_link_Object = MibScalar
mc40G_OEOQsfp2Lane2_link = _Mc40G_OEOQsfp2Lane2_link_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 6),
    _Mc40G_OEOQsfp2Lane2_link_Type()
)
mc40G_OEOQsfp2Lane2_link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc40G_OEOQsfp2Lane2_link.setStatus("mandatory")


class _Mc40G_OEOQsfp2Lane3_link_Type(Integer32):
    """Custom type mc40G_OEOQsfp2Lane3_link based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc40G_OEOQsfp2Lane3_link_Type.__name__ = "Integer32"
_Mc40G_OEOQsfp2Lane3_link_Object = MibScalar
mc40G_OEOQsfp2Lane3_link = _Mc40G_OEOQsfp2Lane3_link_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 7),
    _Mc40G_OEOQsfp2Lane3_link_Type()
)
mc40G_OEOQsfp2Lane3_link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc40G_OEOQsfp2Lane3_link.setStatus("mandatory")


class _Mc40G_OEOQsfp2Lane4_link_Type(Integer32):
    """Custom type mc40G_OEOQsfp2Lane4_link based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc40G_OEOQsfp2Lane4_link_Type.__name__ = "Integer32"
_Mc40G_OEOQsfp2Lane4_link_Object = MibScalar
mc40G_OEOQsfp2Lane4_link = _Mc40G_OEOQsfp2Lane4_link_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 8),
    _Mc40G_OEOQsfp2Lane4_link_Type()
)
mc40G_OEOQsfp2Lane4_link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc40G_OEOQsfp2Lane4_link.setStatus("mandatory")


class _Mc40G_OEOLane1LoopMode_Type(Integer32):
    """Custom type mc40G_OEOLane1LoopMode based on Integer32"""
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
        *(("disable", 3),
          ("host-side-enable", 2),
          ("line-side-enable", 1),
          ("not-support", 4))
    )


_Mc40G_OEOLane1LoopMode_Type.__name__ = "Integer32"
_Mc40G_OEOLane1LoopMode_Object = MibScalar
mc40G_OEOLane1LoopMode = _Mc40G_OEOLane1LoopMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 9),
    _Mc40G_OEOLane1LoopMode_Type()
)
mc40G_OEOLane1LoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc40G_OEOLane1LoopMode.setStatus("current")


class _Mc40G_OEOLane2LoopMode_Type(Integer32):
    """Custom type mc40G_OEOLane2LoopMode based on Integer32"""
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
        *(("disable", 3),
          ("host-side-enable", 2),
          ("line-side-enable", 1),
          ("not-support", 4))
    )


_Mc40G_OEOLane2LoopMode_Type.__name__ = "Integer32"
_Mc40G_OEOLane2LoopMode_Object = MibScalar
mc40G_OEOLane2LoopMode = _Mc40G_OEOLane2LoopMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 10),
    _Mc40G_OEOLane2LoopMode_Type()
)
mc40G_OEOLane2LoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc40G_OEOLane2LoopMode.setStatus("current")


class _Mc40G_OEOLane3LoopMode_Type(Integer32):
    """Custom type mc40G_OEOLane3LoopMode based on Integer32"""
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
        *(("disable", 3),
          ("host-side-enable", 2),
          ("line-side-enable", 1),
          ("not-support", 4))
    )


_Mc40G_OEOLane3LoopMode_Type.__name__ = "Integer32"
_Mc40G_OEOLane3LoopMode_Object = MibScalar
mc40G_OEOLane3LoopMode = _Mc40G_OEOLane3LoopMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 11),
    _Mc40G_OEOLane3LoopMode_Type()
)
mc40G_OEOLane3LoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc40G_OEOLane3LoopMode.setStatus("current")


class _Mc40G_OEOLane4LoopMode_Type(Integer32):
    """Custom type mc40G_OEOLane4LoopMode based on Integer32"""
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
        *(("disable", 3),
          ("host-side-enable", 2),
          ("line-side-enable", 1),
          ("not-support", 4))
    )


_Mc40G_OEOLane4LoopMode_Type.__name__ = "Integer32"
_Mc40G_OEOLane4LoopMode_Object = MibScalar
mc40G_OEOLane4LoopMode = _Mc40G_OEOLane4LoopMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 12),
    _Mc40G_OEOLane4LoopMode_Type()
)
mc40G_OEOLane4LoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc40G_OEOLane4LoopMode.setStatus("current")


class _Mc40G_OEOLoopMode_Type(Integer32):
    """Custom type mc40G_OEOLoopMode based on Integer32"""
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
        *(("all", 1),
          ("disable", 4),
          ("host-side-enable", 3),
          ("line-side-enable", 2),
          ("not-support", 5))
    )


_Mc40G_OEOLoopMode_Type.__name__ = "Integer32"
_Mc40G_OEOLoopMode_Object = MibScalar
mc40G_OEOLoopMode = _Mc40G_OEOLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 13),
    _Mc40G_OEOLoopMode_Type()
)
mc40G_OEOLoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc40G_OEOLoopMode.setStatus("current")


class _Mc40G_OEOSpeedMode_Type(Integer32):
    """Custom type mc40G_OEOSpeedMode based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("mc40GSpeed-1", 1),
          ("mc40GSpeed-10", 10),
          ("mc40GSpeed-11", 11),
          ("mc40GSpeed-12", 12),
          ("mc40GSpeed-13", 13),
          ("mc40GSpeed-2", 2),
          ("mc40GSpeed-3", 3),
          ("mc40GSpeed-4", 4),
          ("mc40GSpeed-5", 5),
          ("mc40GSpeed-6", 6),
          ("mc40GSpeed-7", 7),
          ("mc40GSpeed-8", 8),
          ("mc40GSpeed-9", 9),
          ("no-card", 0),
          ("not-support", 14))
    )


_Mc40G_OEOSpeedMode_Type.__name__ = "Integer32"
_Mc40G_OEOSpeedMode_Object = MibScalar
mc40G_OEOSpeedMode = _Mc40G_OEOSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 14),
    _Mc40G_OEOSpeedMode_Type()
)
mc40G_OEOSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc40G_OEOSpeedMode.setStatus("mandatory")


class _Mc40G_OEOHWLoopMode_Type(Integer32):
    """Custom type mc40G_OEOHWLoopMode based on Integer32"""
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
        *(("disable", 3),
          ("host-side-enable", 2),
          ("line-side-enable", 1),
          ("not-support", 4))
    )


_Mc40G_OEOHWLoopMode_Type.__name__ = "Integer32"
_Mc40G_OEOHWLoopMode_Object = MibScalar
mc40G_OEOHWLoopMode = _Mc40G_OEOHWLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 15),
    _Mc40G_OEOHWLoopMode_Type()
)
mc40G_OEOHWLoopMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc40G_OEOHWLoopMode.setStatus("current")


class _Mc40G_OEOHWSpeedMode_Type(Integer32):
    """Custom type mc40G_OEOHWSpeedMode based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("mc40GSpeed-1", 1),
          ("mc40GSpeed-10", 10),
          ("mc40GSpeed-11", 11),
          ("mc40GSpeed-12", 12),
          ("mc40GSpeed-2", 2),
          ("mc40GSpeed-3", 3),
          ("mc40GSpeed-4", 4),
          ("mc40GSpeed-5", 5),
          ("mc40GSpeed-6", 6),
          ("mc40GSpeed-7", 7),
          ("mc40GSpeed-8", 8),
          ("mc40GSpeed-9", 9),
          ("no-card", 0),
          ("not-support", 13))
    )


_Mc40G_OEOHWSpeedMode_Type.__name__ = "Integer32"
_Mc40G_OEOHWSpeedMode_Object = MibScalar
mc40G_OEOHWSpeedMode = _Mc40G_OEOHWSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 8, 1, 1, 1, 16),
    _Mc40G_OEOHWSpeedMode_Type()
)
mc40G_OEOHWSpeedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc40G_OEOHWSpeedMode.setStatus("mandatory")
_McQsfpSpecificObjects_ObjectIdentity = ObjectIdentity
mcQsfpSpecificObjects = _McQsfpSpecificObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9)
)
_McNtwQSfpObjects_ObjectIdentity = ObjectIdentity
mcNtwQSfpObjects = _McNtwQSfpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1)
)
_McNtwQSfpTable_Object = MibTable
mcNtwQSfpTable = _McNtwQSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    mcNtwQSfpTable.setStatus("current")
_McNtwQSfpEntry_Object = MibTableRow
mcNtwQSfpEntry = _McNtwQSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1, 1, 1)
)
mcNtwQSfpEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mcNtwQSfpEntry.setStatus("current")


class _GetNtwQSfpCmd_Type(Integer32):
    """Custom type getNtwQSfpCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("na", 0),
          ("remote", 2))
    )


_GetNtwQSfpCmd_Type.__name__ = "Integer32"
_GetNtwQSfpCmd_Object = MibTableColumn
getNtwQSfpCmd = _GetNtwQSfpCmd_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1, 1, 1, 1),
    _GetNtwQSfpCmd_Type()
)
getNtwQSfpCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getNtwQSfpCmd.setStatus("current")
_QsfpNtwConnector_Type = Integer32
_QsfpNtwConnector_Object = MibTableColumn
qsfpNtwConnector = _QsfpNtwConnector_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1, 1, 1, 2),
    _QsfpNtwConnector_Type()
)
qsfpNtwConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpNtwConnector.setStatus("current")
_QsfpNtwTemperature_Type = Integer32
_QsfpNtwTemperature_Object = MibTableColumn
qsfpNtwTemperature = _QsfpNtwTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1, 1, 1, 3),
    _QsfpNtwTemperature_Type()
)
qsfpNtwTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpNtwTemperature.setStatus("current")
_QsfpNtwTxPower1_Type = Integer32
_QsfpNtwTxPower1_Object = MibTableColumn
qsfpNtwTxPower1 = _QsfpNtwTxPower1_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1, 1, 1, 4),
    _QsfpNtwTxPower1_Type()
)
qsfpNtwTxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpNtwTxPower1.setStatus("current")
_QsfpNtwTxPower2_Type = Integer32
_QsfpNtwTxPower2_Object = MibTableColumn
qsfpNtwTxPower2 = _QsfpNtwTxPower2_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1, 1, 1, 5),
    _QsfpNtwTxPower2_Type()
)
qsfpNtwTxPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpNtwTxPower2.setStatus("current")
_QsfpNtwTxPower3_Type = Integer32
_QsfpNtwTxPower3_Object = MibTableColumn
qsfpNtwTxPower3 = _QsfpNtwTxPower3_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1, 1, 1, 6),
    _QsfpNtwTxPower3_Type()
)
qsfpNtwTxPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpNtwTxPower3.setStatus("current")
_QsfpNtwTxPower4_Type = Integer32
_QsfpNtwTxPower4_Object = MibTableColumn
qsfpNtwTxPower4 = _QsfpNtwTxPower4_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1, 1, 1, 7),
    _QsfpNtwTxPower4_Type()
)
qsfpNtwTxPower4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpNtwTxPower4.setStatus("current")
_QsfpNtwRxPower1_Type = Integer32
_QsfpNtwRxPower1_Object = MibTableColumn
qsfpNtwRxPower1 = _QsfpNtwRxPower1_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1, 1, 1, 8),
    _QsfpNtwRxPower1_Type()
)
qsfpNtwRxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpNtwRxPower1.setStatus("current")
_QsfpNtwRxPower2_Type = Integer32
_QsfpNtwRxPower2_Object = MibTableColumn
qsfpNtwRxPower2 = _QsfpNtwRxPower2_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1, 1, 1, 9),
    _QsfpNtwRxPower2_Type()
)
qsfpNtwRxPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpNtwRxPower2.setStatus("current")
_QsfpNtwRxPower3_Type = Integer32
_QsfpNtwRxPower3_Object = MibTableColumn
qsfpNtwRxPower3 = _QsfpNtwRxPower3_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1, 1, 1, 10),
    _QsfpNtwRxPower3_Type()
)
qsfpNtwRxPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpNtwRxPower3.setStatus("current")
_QsfpNtwRxPower4_Type = Integer32
_QsfpNtwRxPower4_Object = MibTableColumn
qsfpNtwRxPower4 = _QsfpNtwRxPower4_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 1, 1, 1, 11),
    _QsfpNtwRxPower4_Type()
)
qsfpNtwRxPower4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpNtwRxPower4.setStatus("current")
_McAccQSfpObjects_ObjectIdentity = ObjectIdentity
mcAccQSfpObjects = _McAccQSfpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2)
)
_McAccQSfpTable_Object = MibTable
mcAccQSfpTable = _McAccQSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2, 1)
)
if mibBuilder.loadTexts:
    mcAccQSfpTable.setStatus("current")
_McAccQSfpEntry_Object = MibTableRow
mcAccQSfpEntry = _McAccQSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2, 1, 1)
)
mcAccQSfpEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mcAccQSfpEntry.setStatus("current")


class _GetAccQSfpCmd_Type(Integer32):
    """Custom type getAccQSfpCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("na", 0),
          ("remote", 2))
    )


_GetAccQSfpCmd_Type.__name__ = "Integer32"
_GetAccQSfpCmd_Object = MibTableColumn
getAccQSfpCmd = _GetAccQSfpCmd_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2, 1, 1, 1),
    _GetAccQSfpCmd_Type()
)
getAccQSfpCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getAccQSfpCmd.setStatus("current")
_QsfpAccConnector_Type = Integer32
_QsfpAccConnector_Object = MibTableColumn
qsfpAccConnector = _QsfpAccConnector_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2, 1, 1, 2),
    _QsfpAccConnector_Type()
)
qsfpAccConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpAccConnector.setStatus("current")
_QsfpAccTemperature_Type = Integer32
_QsfpAccTemperature_Object = MibTableColumn
qsfpAccTemperature = _QsfpAccTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2, 1, 1, 3),
    _QsfpAccTemperature_Type()
)
qsfpAccTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpAccTemperature.setStatus("current")
_QsfpAccTxPower1_Type = Integer32
_QsfpAccTxPower1_Object = MibTableColumn
qsfpAccTxPower1 = _QsfpAccTxPower1_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2, 1, 1, 4),
    _QsfpAccTxPower1_Type()
)
qsfpAccTxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpAccTxPower1.setStatus("current")
_QsfpAccTxPower2_Type = Integer32
_QsfpAccTxPower2_Object = MibTableColumn
qsfpAccTxPower2 = _QsfpAccTxPower2_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2, 1, 1, 5),
    _QsfpAccTxPower2_Type()
)
qsfpAccTxPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpAccTxPower2.setStatus("current")
_QsfpAccTxPower3_Type = Integer32
_QsfpAccTxPower3_Object = MibTableColumn
qsfpAccTxPower3 = _QsfpAccTxPower3_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2, 1, 1, 6),
    _QsfpAccTxPower3_Type()
)
qsfpAccTxPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpAccTxPower3.setStatus("current")
_QsfpAccTxPower4_Type = Integer32
_QsfpAccTxPower4_Object = MibTableColumn
qsfpAccTxPower4 = _QsfpAccTxPower4_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2, 1, 1, 7),
    _QsfpAccTxPower4_Type()
)
qsfpAccTxPower4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpAccTxPower4.setStatus("current")
_QsfpAccRxPower1_Type = Integer32
_QsfpAccRxPower1_Object = MibTableColumn
qsfpAccRxPower1 = _QsfpAccRxPower1_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2, 1, 1, 8),
    _QsfpAccRxPower1_Type()
)
qsfpAccRxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpAccRxPower1.setStatus("current")
_QsfpAccRxPower2_Type = Integer32
_QsfpAccRxPower2_Object = MibTableColumn
qsfpAccRxPower2 = _QsfpAccRxPower2_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2, 1, 1, 9),
    _QsfpAccRxPower2_Type()
)
qsfpAccRxPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpAccRxPower2.setStatus("current")
_QsfpAccRxPower3_Type = Integer32
_QsfpAccRxPower3_Object = MibTableColumn
qsfpAccRxPower3 = _QsfpAccRxPower3_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2, 1, 1, 10),
    _QsfpAccRxPower3_Type()
)
qsfpAccRxPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpAccRxPower3.setStatus("current")
_QsfpAccRxPower4_Type = Integer32
_QsfpAccRxPower4_Object = MibTableColumn
qsfpAccRxPower4 = _QsfpAccRxPower4_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 9, 2, 1, 1, 11),
    _QsfpAccRxPower4_Type()
)
qsfpAccRxPower4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsfpAccRxPower4.setStatus("current")
_Mc2_5GMCObjects_ObjectIdentity = ObjectIdentity
mc2_5GMCObjects = _Mc2_5GMCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10)
)
_Mc2_5GMCSFP3Objects_ObjectIdentity = ObjectIdentity
mc2_5GMCSFP3Objects = _Mc2_5GMCSFP3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1)
)
_Mc2_5Cm1gSfpTable_Object = MibTable
mc2_5Cm1gSfpTable = _Mc2_5Cm1gSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    mc2_5Cm1gSfpTable.setStatus("current")
_Mc2_5Cm1gSfpEntry_Object = MibTableRow
mc2_5Cm1gSfpEntry = _Mc2_5Cm1gSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1)
)
mc2_5Cm1gSfpEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
    (0, "XXX-MIB", "mcLoOrRmtFg"),
)
if mibBuilder.loadTexts:
    mc2_5Cm1gSfpEntry.setStatus("current")


class _Mc2_5g_getSfpCmd_Type(Integer32):
    """Custom type mc2_5g_getSfpCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("na", 0),
          ("remote", 2))
    )


_Mc2_5g_getSfpCmd_Type.__name__ = "Integer32"
_Mc2_5g_getSfpCmd_Object = MibScalar
mc2_5g_getSfpCmd = _Mc2_5g_getSfpCmd_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1, 1),
    _Mc2_5g_getSfpCmd_Type()
)
mc2_5g_getSfpCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2_5g_getSfpCmd.setStatus("current")
_Mc2_5g_sfpCompliance_Type = Integer32
_Mc2_5g_sfpCompliance_Object = MibScalar
mc2_5g_sfpCompliance = _Mc2_5g_sfpCompliance_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1, 2),
    _Mc2_5g_sfpCompliance_Type()
)
mc2_5g_sfpCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5g_sfpCompliance.setStatus("current")
_Mc2_5g_sfpConnector_Type = Integer32
_Mc2_5g_sfpConnector_Object = MibScalar
mc2_5g_sfpConnector = _Mc2_5g_sfpConnector_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1, 3),
    _Mc2_5g_sfpConnector_Type()
)
mc2_5g_sfpConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5g_sfpConnector.setStatus("current")
_Mc2_5g_sfpTransCode_Type = Integer32
_Mc2_5g_sfpTransCode_Object = MibScalar
mc2_5g_sfpTransCode = _Mc2_5g_sfpTransCode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1, 4),
    _Mc2_5g_sfpTransCode_Type()
)
mc2_5g_sfpTransCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5g_sfpTransCode.setStatus("current")
_Mc2_5g_sfpSmLength_Type = Integer32
_Mc2_5g_sfpSmLength_Object = MibScalar
mc2_5g_sfpSmLength = _Mc2_5g_sfpSmLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1, 5),
    _Mc2_5g_sfpSmLength_Type()
)
mc2_5g_sfpSmLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5g_sfpSmLength.setStatus("current")
_Mc2_5g_sfpMmLength_Type = Integer32
_Mc2_5g_sfpMmLength_Object = MibScalar
mc2_5g_sfpMmLength = _Mc2_5g_sfpMmLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1, 6),
    _Mc2_5g_sfpMmLength_Type()
)
mc2_5g_sfpMmLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5g_sfpMmLength.setStatus("current")
_Mc2_5g_sfpCopperLength_Type = Integer32
_Mc2_5g_sfpCopperLength_Object = MibScalar
mc2_5g_sfpCopperLength = _Mc2_5g_sfpCopperLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1, 7),
    _Mc2_5g_sfpCopperLength_Type()
)
mc2_5g_sfpCopperLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5g_sfpCopperLength.setStatus("current")
_Mc2_5g_sfpBrSpeed_Type = Integer32
_Mc2_5g_sfpBrSpeed_Object = MibScalar
mc2_5g_sfpBrSpeed = _Mc2_5g_sfpBrSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1, 8),
    _Mc2_5g_sfpBrSpeed_Type()
)
mc2_5g_sfpBrSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5g_sfpBrSpeed.setStatus("current")
_Mc2_5g_sfpWavelength_Type = Integer32
_Mc2_5g_sfpWavelength_Object = MibScalar
mc2_5g_sfpWavelength = _Mc2_5g_sfpWavelength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1, 9),
    _Mc2_5g_sfpWavelength_Type()
)
mc2_5g_sfpWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5g_sfpWavelength.setStatus("current")
_Mc2_5g_sfpTemperature_Type = Integer32
_Mc2_5g_sfpTemperature_Object = MibScalar
mc2_5g_sfpTemperature = _Mc2_5g_sfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1, 10),
    _Mc2_5g_sfpTemperature_Type()
)
mc2_5g_sfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5g_sfpTemperature.setStatus("current")
_Mc2_5g_sfpTranPower_Type = Integer32
_Mc2_5g_sfpTranPower_Object = MibScalar
mc2_5g_sfpTranPower = _Mc2_5g_sfpTranPower_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1, 11),
    _Mc2_5g_sfpTranPower_Type()
)
mc2_5g_sfpTranPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5g_sfpTranPower.setStatus("current")
_Mc2_5g_sfpRecvPower_Type = Integer32
_Mc2_5g_sfpRecvPower_Object = MibScalar
mc2_5g_sfpRecvPower = _Mc2_5g_sfpRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1, 12),
    _Mc2_5g_sfpRecvPower_Type()
)
mc2_5g_sfpRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5g_sfpRecvPower.setStatus("current")
_Mc2_5g_sfpVoltage_Type = Integer32
_Mc2_5g_sfpVoltage_Object = MibScalar
mc2_5g_sfpVoltage = _Mc2_5g_sfpVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 1, 1, 1, 13),
    _Mc2_5g_sfpVoltage_Type()
)
mc2_5g_sfpVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5g_sfpVoltage.setStatus("current")
_Mc2_5GMCCardObjects_ObjectIdentity = ObjectIdentity
mc2_5GMCCardObjects = _Mc2_5GMCCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 2)
)
_Mc2_5GMCCardTable_Object = MibTable
mc2_5GMCCardTable = _Mc2_5GMCCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    mc2_5GMCCardTable.setStatus("current")
_Mc2_5GMCCardEntry_Object = MibTableRow
mc2_5GMCCardEntry = _Mc2_5GMCCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 2, 1, 1)
)
mc2_5GMCCardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mc2_5GMCCardEntry.setStatus("current")


class _Mc2_5GMCSfp3Exist_Type(Integer32):
    """Custom type mc2_5GMCSfp3Exist based on Integer32"""
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
        *(("inserted", 1),
          ("na", 3),
          ("not-support", 4),
          ("removed", 2))
    )


_Mc2_5GMCSfp3Exist_Type.__name__ = "Integer32"
_Mc2_5GMCSfp3Exist_Object = MibScalar
mc2_5GMCSfp3Exist = _Mc2_5GMCSfp3Exist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 2, 1, 1, 1),
    _Mc2_5GMCSfp3Exist_Type()
)
mc2_5GMCSfp3Exist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5GMCSfp3Exist.setStatus("current")


class _Mc2_5GMCPort1link_Type(Integer32):
    """Custom type mc2_5GMCPort1link based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc2_5GMCPort1link_Type.__name__ = "Integer32"
_Mc2_5GMCPort1link_Object = MibScalar
mc2_5GMCPort1link = _Mc2_5GMCPort1link_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 2, 1, 1, 2),
    _Mc2_5GMCPort1link_Type()
)
mc2_5GMCPort1link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5GMCPort1link.setStatus("current")


class _Mc2_5GMCPort2link_Type(Integer32):
    """Custom type mc2_5GMCPort2link based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc2_5GMCPort2link_Type.__name__ = "Integer32"
_Mc2_5GMCPort2link_Object = MibScalar
mc2_5GMCPort2link = _Mc2_5GMCPort2link_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 2, 1, 1, 3),
    _Mc2_5GMCPort2link_Type()
)
mc2_5GMCPort2link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5GMCPort2link.setStatus("current")


class _Mc2_5GMCPort3link_Type(Integer32):
    """Custom type mc2_5GMCPort3link based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc2_5GMCPort3link_Type.__name__ = "Integer32"
_Mc2_5GMCPort3link_Object = MibScalar
mc2_5GMCPort3link = _Mc2_5GMCPort3link_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 10, 2, 1, 1, 4),
    _Mc2_5GMCPort3link_Type()
)
mc2_5GMCPort3link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2_5GMCPort3link.setStatus("current")
_McE1Objects_ObjectIdentity = ObjectIdentity
mcE1Objects = _McE1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11)
)
_McE1CardObjects_ObjectIdentity = ObjectIdentity
mcE1CardObjects = _McE1CardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1)
)
_McE1CardTable_Object = MibTable
mcE1CardTable = _McE1CardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1)
)
if mibBuilder.loadTexts:
    mcE1CardTable.setStatus("current")
_McE1CardEntry_Object = MibTableRow
mcE1CardEntry = _McE1CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1)
)
mcE1CardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mcE1CardEntry.setStatus("current")


class _McE1Txlink_Type(Integer32):
    """Custom type mcE1Txlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_McE1Txlink_Type.__name__ = "Integer32"
_McE1Txlink_Object = MibTableColumn
mcE1Txlink = _McE1Txlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 1),
    _McE1Txlink_Type()
)
mcE1Txlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1Txlink.setStatus("mandatory")


class _McE1TxCurWorkMode_Type(Integer32):
    """Custom type mcE1TxCurWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("not-support", 7))
    )


_McE1TxCurWorkMode_Type.__name__ = "Integer32"
_McE1TxCurWorkMode_Object = MibTableColumn
mcE1TxCurWorkMode = _McE1TxCurWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 2),
    _McE1TxCurWorkMode_Type()
)
mcE1TxCurWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1TxCurWorkMode.setStatus("mandatory")


class _McE1SFP1Link_Type(Integer32):
    """Custom type mcE1SFP1Link based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_McE1SFP1Link_Type.__name__ = "Integer32"
_McE1SFP1Link_Object = MibTableColumn
mcE1SFP1Link = _McE1SFP1Link_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 3),
    _McE1SFP1Link_Type()
)
mcE1SFP1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1SFP1Link.setStatus("mandatory")


class _McE1Port1LOS_Type(Integer32):
    """Custom type mcE1Port1LOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("e1normal", 2),
          ("not-support", 3))
    )


_McE1Port1LOS_Type.__name__ = "Integer32"
_McE1Port1LOS_Object = MibTableColumn
mcE1Port1LOS = _McE1Port1LOS_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 4),
    _McE1Port1LOS_Type()
)
mcE1Port1LOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1Port1LOS.setStatus("current")


class _McE1Port1AIS_Type(Integer32):
    """Custom type mcE1Port1AIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("e1normal", 2),
          ("not-support", 3))
    )


_McE1Port1AIS_Type.__name__ = "Integer32"
_McE1Port1AIS_Object = MibTableColumn
mcE1Port1AIS = _McE1Port1AIS_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 5),
    _McE1Port1AIS_Type()
)
mcE1Port1AIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1Port1AIS.setStatus("current")


class _McE1Port1CV_Type(Integer32):
    """Custom type mcE1Port1CV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("e1normal", 2),
          ("not-support", 3))
    )


_McE1Port1CV_Type.__name__ = "Integer32"
_McE1Port1CV_Object = MibTableColumn
mcE1Port1CV = _McE1Port1CV_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 6),
    _McE1Port1CV_Type()
)
mcE1Port1CV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1Port1CV.setStatus("current")


class _McE1Port2LOS_Type(Integer32):
    """Custom type mcE1Port2LOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("e1normal", 2),
          ("not-support", 3))
    )


_McE1Port2LOS_Type.__name__ = "Integer32"
_McE1Port2LOS_Object = MibTableColumn
mcE1Port2LOS = _McE1Port2LOS_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 7),
    _McE1Port2LOS_Type()
)
mcE1Port2LOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1Port2LOS.setStatus("current")


class _McE1Port2AIS_Type(Integer32):
    """Custom type mcE1Port2AIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("e1normal", 2),
          ("not-support", 3))
    )


_McE1Port2AIS_Type.__name__ = "Integer32"
_McE1Port2AIS_Object = MibTableColumn
mcE1Port2AIS = _McE1Port2AIS_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 8),
    _McE1Port2AIS_Type()
)
mcE1Port2AIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1Port2AIS.setStatus("current")


class _McE1Port2CV_Type(Integer32):
    """Custom type mcE1Port2CV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("e1normal", 2),
          ("not-support", 3))
    )


_McE1Port2CV_Type.__name__ = "Integer32"
_McE1Port2CV_Object = MibTableColumn
mcE1Port2CV = _McE1Port2CV_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 9),
    _McE1Port2CV_Type()
)
mcE1Port2CV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1Port2CV.setStatus("current")


class _McE1Port1Loop_Type(Integer32):
    """Custom type mcE1Port1Loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("external", 1),
          ("internal", 2))
    )


_McE1Port1Loop_Type.__name__ = "Integer32"
_McE1Port1Loop_Object = MibTableColumn
mcE1Port1Loop = _McE1Port1Loop_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 10),
    _McE1Port1Loop_Type()
)
mcE1Port1Loop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcE1Port1Loop.setStatus("current")


class _McE1Port2Loop_Type(Integer32):
    """Custom type mcE1Port2Loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("external", 1),
          ("internal", 2))
    )


_McE1Port2Loop_Type.__name__ = "Integer32"
_McE1Port2Loop_Object = MibTableColumn
mcE1Port2Loop = _McE1Port2Loop_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 11),
    _McE1Port2Loop_Type()
)
mcE1Port2Loop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcE1Port2Loop.setStatus("current")


class _McRmtE1Txlink_Type(Integer32):
    """Custom type mcRmtE1Txlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_McRmtE1Txlink_Type.__name__ = "Integer32"
_McRmtE1Txlink_Object = MibTableColumn
mcRmtE1Txlink = _McRmtE1Txlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 12),
    _McRmtE1Txlink_Type()
)
mcRmtE1Txlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtE1Txlink.setStatus("mandatory")


class _McRmtE1TxCurWorkMode_Type(Integer32):
    """Custom type mcRmtE1TxCurWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("not-support", 7))
    )


_McRmtE1TxCurWorkMode_Type.__name__ = "Integer32"
_McRmtE1TxCurWorkMode_Object = MibTableColumn
mcRmtE1TxCurWorkMode = _McRmtE1TxCurWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 13),
    _McRmtE1TxCurWorkMode_Type()
)
mcRmtE1TxCurWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtE1TxCurWorkMode.setStatus("mandatory")


class _McRmtE1SFP1Link_Type(Integer32):
    """Custom type mcRmtE1SFP1Link based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_McRmtE1SFP1Link_Type.__name__ = "Integer32"
_McRmtE1SFP1Link_Object = MibTableColumn
mcRmtE1SFP1Link = _McRmtE1SFP1Link_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 14),
    _McRmtE1SFP1Link_Type()
)
mcRmtE1SFP1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtE1SFP1Link.setStatus("mandatory")


class _McRmtE1Port1LOS_Type(Integer32):
    """Custom type mcRmtE1Port1LOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("e1normal", 2),
          ("not-support", 3))
    )


_McRmtE1Port1LOS_Type.__name__ = "Integer32"
_McRmtE1Port1LOS_Object = MibTableColumn
mcRmtE1Port1LOS = _McRmtE1Port1LOS_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 15),
    _McRmtE1Port1LOS_Type()
)
mcRmtE1Port1LOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtE1Port1LOS.setStatus("current")


class _McRmtE1Port1AIS_Type(Integer32):
    """Custom type mcRmtE1Port1AIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("e1normal", 2),
          ("not-support", 3))
    )


_McRmtE1Port1AIS_Type.__name__ = "Integer32"
_McRmtE1Port1AIS_Object = MibTableColumn
mcRmtE1Port1AIS = _McRmtE1Port1AIS_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 16),
    _McRmtE1Port1AIS_Type()
)
mcRmtE1Port1AIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtE1Port1AIS.setStatus("current")


class _McRmtE1Port1CV_Type(Integer32):
    """Custom type mcRmtE1Port1CV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("e1normal", 2),
          ("not-support", 3))
    )


_McRmtE1Port1CV_Type.__name__ = "Integer32"
_McRmtE1Port1CV_Object = MibTableColumn
mcRmtE1Port1CV = _McRmtE1Port1CV_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 17),
    _McRmtE1Port1CV_Type()
)
mcRmtE1Port1CV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtE1Port1CV.setStatus("current")


class _McRmtE1Port2LOS_Type(Integer32):
    """Custom type mcRmtE1Port2LOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("e1normal", 2),
          ("not-support", 3))
    )


_McRmtE1Port2LOS_Type.__name__ = "Integer32"
_McRmtE1Port2LOS_Object = MibTableColumn
mcRmtE1Port2LOS = _McRmtE1Port2LOS_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 18),
    _McRmtE1Port2LOS_Type()
)
mcRmtE1Port2LOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtE1Port2LOS.setStatus("current")


class _McRmtE1Port2AIS_Type(Integer32):
    """Custom type mcRmtE1Port2AIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("e1normal", 2),
          ("not-support", 3))
    )


_McRmtE1Port2AIS_Type.__name__ = "Integer32"
_McRmtE1Port2AIS_Object = MibTableColumn
mcRmtE1Port2AIS = _McRmtE1Port2AIS_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 19),
    _McRmtE1Port2AIS_Type()
)
mcRmtE1Port2AIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtE1Port2AIS.setStatus("current")


class _McRmtE1Port2CV_Type(Integer32):
    """Custom type mcRmtE1Port2CV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("e1normal", 2),
          ("not-support", 3))
    )


_McRmtE1Port2CV_Type.__name__ = "Integer32"
_McRmtE1Port2CV_Object = MibTableColumn
mcRmtE1Port2CV = _McRmtE1Port2CV_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 20),
    _McRmtE1Port2CV_Type()
)
mcRmtE1Port2CV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRmtE1Port2CV.setStatus("current")


class _McRmtE1Port1Loop_Type(Integer32):
    """Custom type mcRmtE1Port1Loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("external", 1),
          ("internal", 2))
    )


_McRmtE1Port1Loop_Type.__name__ = "Integer32"
_McRmtE1Port1Loop_Object = MibTableColumn
mcRmtE1Port1Loop = _McRmtE1Port1Loop_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 21),
    _McRmtE1Port1Loop_Type()
)
mcRmtE1Port1Loop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmtE1Port1Loop.setStatus("current")


class _McRmtE1Port2Loop_Type(Integer32):
    """Custom type mcRmtE1Port2Loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("external", 1),
          ("internal", 2))
    )


_McRmtE1Port2Loop_Type.__name__ = "Integer32"
_McRmtE1Port2Loop_Object = MibTableColumn
mcRmtE1Port2Loop = _McRmtE1Port2Loop_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 11, 1, 1, 1, 22),
    _McRmtE1Port2Loop_Type()
)
mcRmtE1Port2Loop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRmtE1Port2Loop.setStatus("current")
_Mc1GE2OObjects_ObjectIdentity = ObjectIdentity
mc1GE2OObjects = _Mc1GE2OObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12)
)
_Mc1GE2OCardObjects_ObjectIdentity = ObjectIdentity
mc1GE2OCardObjects = _Mc1GE2OCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1)
)
_Mc1GE2OCardTable_Object = MibTable
mc1GE2OCardTable = _Mc1GE2OCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1)
)
if mibBuilder.loadTexts:
    mc1GE2OCardTable.setStatus("current")
_Mc1GE2OCardEntry_Object = MibTableRow
mc1GE2OCardEntry = _Mc1GE2OCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1)
)
mc1GE2OCardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mc1GE2OCardEntry.setStatus("current")


class _Mc1GE2OPort1SFPlink_Type(Integer32):
    """Custom type mc1GE2OPort1SFPlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc1GE2OPort1SFPlink_Type.__name__ = "Integer32"
_Mc1GE2OPort1SFPlink_Object = MibTableColumn
mc1GE2OPort1SFPlink = _Mc1GE2OPort1SFPlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1, 1),
    _Mc1GE2OPort1SFPlink_Type()
)
mc1GE2OPort1SFPlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GE2OPort1SFPlink.setStatus("mandatory")


class _Mc1GE2OPort2SFPlink_Type(Integer32):
    """Custom type mc1GE2OPort2SFPlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc1GE2OPort2SFPlink_Type.__name__ = "Integer32"
_Mc1GE2OPort2SFPlink_Object = MibTableColumn
mc1GE2OPort2SFPlink = _Mc1GE2OPort2SFPlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1, 2),
    _Mc1GE2OPort2SFPlink_Type()
)
mc1GE2OPort2SFPlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GE2OPort2SFPlink.setStatus("mandatory")


class _Mc1GE2OTxlink_Type(Integer32):
    """Custom type mc1GE2OTxlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc1GE2OTxlink_Type.__name__ = "Integer32"
_Mc1GE2OTxlink_Object = MibTableColumn
mc1GE2OTxlink = _Mc1GE2OTxlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1, 3),
    _Mc1GE2OTxlink_Type()
)
mc1GE2OTxlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GE2OTxlink.setStatus("mandatory")


class _Mc1GE2OPortPri_Type(Integer32):
    """Custom type mc1GE2OPortPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Port1", 1),
          ("Port2", 2),
          ("not-support", 3))
    )


_Mc1GE2OPortPri_Type.__name__ = "Integer32"
_Mc1GE2OPortPri_Object = MibTableColumn
mc1GE2OPortPri = _Mc1GE2OPortPri_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1, 4),
    _Mc1GE2OPortPri_Type()
)
mc1GE2OPortPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc1GE2OPortPri.setStatus("current")


class _Mc1GE2OPort1SFPExist_Type(Integer32):
    """Custom type mc1GE2OPort1SFPExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("na", 3),
          ("no-card", 0),
          ("removed", 2),
          ("support", 4))
    )


_Mc1GE2OPort1SFPExist_Type.__name__ = "Integer32"
_Mc1GE2OPort1SFPExist_Object = MibTableColumn
mc1GE2OPort1SFPExist = _Mc1GE2OPort1SFPExist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1, 5),
    _Mc1GE2OPort1SFPExist_Type()
)
mc1GE2OPort1SFPExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GE2OPort1SFPExist.setStatus("current")


class _Mc1GE2OPort2SFPExist_Type(Integer32):
    """Custom type mc1GE2OPort2SFPExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("na", 3),
          ("no-card", 0),
          ("removed", 2),
          ("support", 4))
    )


_Mc1GE2OPort2SFPExist_Type.__name__ = "Integer32"
_Mc1GE2OPort2SFPExist_Object = MibTableColumn
mc1GE2OPort2SFPExist = _Mc1GE2OPort2SFPExist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1, 6),
    _Mc1GE2OPort2SFPExist_Type()
)
mc1GE2OPort2SFPExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GE2OPort2SFPExist.setStatus("current")


class _Mc1GE2OPortHWPri_Type(Integer32):
    """Custom type mc1GE2OPortHWPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Port1", 1),
          ("Port2", 2),
          ("not-support", 3))
    )


_Mc1GE2OPortHWPri_Type.__name__ = "Integer32"
_Mc1GE2OPortHWPri_Object = MibTableColumn
mc1GE2OPortHWPri = _Mc1GE2OPortHWPri_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1, 7),
    _Mc1GE2OPortHWPri_Type()
)
mc1GE2OPortHWPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GE2OPortHWPri.setStatus("current")


class _Mc1GE2ORmtPort1SFPlink_Type(Integer32):
    """Custom type mc1GE2ORmtPort1SFPlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc1GE2ORmtPort1SFPlink_Type.__name__ = "Integer32"
_Mc1GE2ORmtPort1SFPlink_Object = MibTableColumn
mc1GE2ORmtPort1SFPlink = _Mc1GE2ORmtPort1SFPlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1, 8),
    _Mc1GE2ORmtPort1SFPlink_Type()
)
mc1GE2ORmtPort1SFPlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GE2ORmtPort1SFPlink.setStatus("mandatory")


class _Mc1GE2ORmtPort2SFPlink_Type(Integer32):
    """Custom type mc1GE2ORmtPort2SFPlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc1GE2ORmtPort2SFPlink_Type.__name__ = "Integer32"
_Mc1GE2ORmtPort2SFPlink_Object = MibTableColumn
mc1GE2ORmtPort2SFPlink = _Mc1GE2ORmtPort2SFPlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1, 9),
    _Mc1GE2ORmtPort2SFPlink_Type()
)
mc1GE2ORmtPort2SFPlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GE2ORmtPort2SFPlink.setStatus("mandatory")


class _Mc1GE2ORmtTxlink_Type(Integer32):
    """Custom type mc1GE2ORmtTxlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc1GE2ORmtTxlink_Type.__name__ = "Integer32"
_Mc1GE2ORmtTxlink_Object = MibTableColumn
mc1GE2ORmtTxlink = _Mc1GE2ORmtTxlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1, 10),
    _Mc1GE2ORmtTxlink_Type()
)
mc1GE2ORmtTxlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GE2ORmtTxlink.setStatus("mandatory")


class _Mc1GE2ORmtPort1SFPExist_Type(Integer32):
    """Custom type mc1GE2ORmtPort1SFPExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("na", 3),
          ("no-card", 0),
          ("removed", 2),
          ("support", 4))
    )


_Mc1GE2ORmtPort1SFPExist_Type.__name__ = "Integer32"
_Mc1GE2ORmtPort1SFPExist_Object = MibTableColumn
mc1GE2ORmtPort1SFPExist = _Mc1GE2ORmtPort1SFPExist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1, 11),
    _Mc1GE2ORmtPort1SFPExist_Type()
)
mc1GE2ORmtPort1SFPExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GE2ORmtPort1SFPExist.setStatus("current")


class _Mc1GE2ORmtPort2SFPExist_Type(Integer32):
    """Custom type mc1GE2ORmtPort2SFPExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("na", 3),
          ("no-card", 0),
          ("removed", 2),
          ("support", 4))
    )


_Mc1GE2ORmtPort2SFPExist_Type.__name__ = "Integer32"
_Mc1GE2ORmtPort2SFPExist_Object = MibTableColumn
mc1GE2ORmtPort2SFPExist = _Mc1GE2ORmtPort2SFPExist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1, 12),
    _Mc1GE2ORmtPort2SFPExist_Type()
)
mc1GE2ORmtPort2SFPExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GE2ORmtPort2SFPExist.setStatus("current")


class _Mc1GE2ORmtPortHWPri_Type(Integer32):
    """Custom type mc1GE2ORmtPortHWPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Port1", 1),
          ("Port2", 2),
          ("not-support", 3))
    )


_Mc1GE2ORmtPortHWPri_Type.__name__ = "Integer32"
_Mc1GE2ORmtPortHWPri_Object = MibTableColumn
mc1GE2ORmtPortHWPri = _Mc1GE2ORmtPortHWPri_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 12, 1, 1, 1, 13),
    _Mc1GE2ORmtPortHWPri_Type()
)
mc1GE2ORmtPortHWPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GE2ORmtPortHWPri.setStatus("current")
_Mc1GO2OObjects_ObjectIdentity = ObjectIdentity
mc1GO2OObjects = _Mc1GO2OObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13)
)
_Mc1GO2OCardObjects_ObjectIdentity = ObjectIdentity
mc1GO2OCardObjects = _Mc1GO2OCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1)
)
_Mc1GO2OCardTable_Object = MibTable
mc1GO2OCardTable = _Mc1GO2OCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1)
)
if mibBuilder.loadTexts:
    mc1GO2OCardTable.setStatus("current")
_Mc1GO2OCardEntry_Object = MibTableRow
mc1GO2OCardEntry = _Mc1GO2OCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1)
)
mc1GO2OCardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mc1GO2OCardEntry.setStatus("current")


class _Mc1GO2OPort1SFPlink_Type(Integer32):
    """Custom type mc1GO2OPort1SFPlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc1GO2OPort1SFPlink_Type.__name__ = "Integer32"
_Mc1GO2OPort1SFPlink_Object = MibTableColumn
mc1GO2OPort1SFPlink = _Mc1GO2OPort1SFPlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 1),
    _Mc1GO2OPort1SFPlink_Type()
)
mc1GO2OPort1SFPlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2OPort1SFPlink.setStatus("mandatory")


class _Mc1GO2OPort2SFPlink_Type(Integer32):
    """Custom type mc1GO2OPort2SFPlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc1GO2OPort2SFPlink_Type.__name__ = "Integer32"
_Mc1GO2OPort2SFPlink_Object = MibTableColumn
mc1GO2OPort2SFPlink = _Mc1GO2OPort2SFPlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 2),
    _Mc1GO2OPort2SFPlink_Type()
)
mc1GO2OPort2SFPlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2OPort2SFPlink.setStatus("mandatory")


class _Mc1GO2OPort3SFPlink_Type(Integer32):
    """Custom type mc1GO2OPort3SFPlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc1GO2OPort3SFPlink_Type.__name__ = "Integer32"
_Mc1GO2OPort3SFPlink_Object = MibTableColumn
mc1GO2OPort3SFPlink = _Mc1GO2OPort3SFPlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 3),
    _Mc1GO2OPort3SFPlink_Type()
)
mc1GO2OPort3SFPlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2OPort3SFPlink.setStatus("mandatory")


class _Mc1GO2OPortPri_Type(Integer32):
    """Custom type mc1GO2OPortPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Port1", 1),
          ("Port2", 2),
          ("not-support", 3))
    )


_Mc1GO2OPortPri_Type.__name__ = "Integer32"
_Mc1GO2OPortPri_Object = MibTableColumn
mc1GO2OPortPri = _Mc1GO2OPortPri_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 4),
    _Mc1GO2OPortPri_Type()
)
mc1GO2OPortPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc1GO2OPortPri.setStatus("current")


class _Mc1GO2OPort1SFPExist_Type(Integer32):
    """Custom type mc1GO2OPort1SFPExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("na", 3),
          ("no-card", 0),
          ("removed", 2),
          ("support", 4))
    )


_Mc1GO2OPort1SFPExist_Type.__name__ = "Integer32"
_Mc1GO2OPort1SFPExist_Object = MibTableColumn
mc1GO2OPort1SFPExist = _Mc1GO2OPort1SFPExist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 5),
    _Mc1GO2OPort1SFPExist_Type()
)
mc1GO2OPort1SFPExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2OPort1SFPExist.setStatus("current")


class _Mc1GO2OPort2SFPExist_Type(Integer32):
    """Custom type mc1GO2OPort2SFPExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("na", 3),
          ("no-card", 0),
          ("removed", 2),
          ("support", 4))
    )


_Mc1GO2OPort2SFPExist_Type.__name__ = "Integer32"
_Mc1GO2OPort2SFPExist_Object = MibTableColumn
mc1GO2OPort2SFPExist = _Mc1GO2OPort2SFPExist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 6),
    _Mc1GO2OPort2SFPExist_Type()
)
mc1GO2OPort2SFPExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2OPort2SFPExist.setStatus("current")


class _Mc1GO2OPort3SFPExist_Type(Integer32):
    """Custom type mc1GO2OPort3SFPExist based on Integer32"""
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
        *(("inserted", 1),
          ("na", 3),
          ("not-support", 4),
          ("removed", 2))
    )


_Mc1GO2OPort3SFPExist_Type.__name__ = "Integer32"
_Mc1GO2OPort3SFPExist_Object = MibTableColumn
mc1GO2OPort3SFPExist = _Mc1GO2OPort3SFPExist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 7),
    _Mc1GO2OPort3SFPExist_Type()
)
mc1GO2OPort3SFPExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2OPort3SFPExist.setStatus("current")


class _Mc1GO2OPortHWPri_Type(Integer32):
    """Custom type mc1GO2OPortHWPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Port1", 1),
          ("Port2", 2),
          ("not-support", 3))
    )


_Mc1GO2OPortHWPri_Type.__name__ = "Integer32"
_Mc1GO2OPortHWPri_Object = MibTableColumn
mc1GO2OPortHWPri = _Mc1GO2OPortHWPri_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 8),
    _Mc1GO2OPortHWPri_Type()
)
mc1GO2OPortHWPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2OPortHWPri.setStatus("current")


class _Mc1GO2OPort3HWSpd_Type(Integer32):
    """Custom type mc1GO2OPort3HWSpd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("M100", 1),
          ("M1000", 2),
          ("not-support", 3))
    )


_Mc1GO2OPort3HWSpd_Type.__name__ = "Integer32"
_Mc1GO2OPort3HWSpd_Object = MibTableColumn
mc1GO2OPort3HWSpd = _Mc1GO2OPort3HWSpd_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 9),
    _Mc1GO2OPort3HWSpd_Type()
)
mc1GO2OPort3HWSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2OPort3HWSpd.setStatus("current")


class _Mc1GO2ORmtPort1SFPlink_Type(Integer32):
    """Custom type mc1GO2ORmtPort1SFPlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc1GO2ORmtPort1SFPlink_Type.__name__ = "Integer32"
_Mc1GO2ORmtPort1SFPlink_Object = MibTableColumn
mc1GO2ORmtPort1SFPlink = _Mc1GO2ORmtPort1SFPlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 10),
    _Mc1GO2ORmtPort1SFPlink_Type()
)
mc1GO2ORmtPort1SFPlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2ORmtPort1SFPlink.setStatus("mandatory")


class _Mc1GO2ORmtPort2SFPlink_Type(Integer32):
    """Custom type mc1GO2ORmtPort2SFPlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc1GO2ORmtPort2SFPlink_Type.__name__ = "Integer32"
_Mc1GO2ORmtPort2SFPlink_Object = MibTableColumn
mc1GO2ORmtPort2SFPlink = _Mc1GO2ORmtPort2SFPlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 11),
    _Mc1GO2ORmtPort2SFPlink_Type()
)
mc1GO2ORmtPort2SFPlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2ORmtPort2SFPlink.setStatus("mandatory")


class _Mc1GO2ORmtPort3SFPlink_Type(Integer32):
    """Custom type mc1GO2ORmtPort3SFPlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc1GO2ORmtPort3SFPlink_Type.__name__ = "Integer32"
_Mc1GO2ORmtPort3SFPlink_Object = MibTableColumn
mc1GO2ORmtPort3SFPlink = _Mc1GO2ORmtPort3SFPlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 12),
    _Mc1GO2ORmtPort3SFPlink_Type()
)
mc1GO2ORmtPort3SFPlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2ORmtPort3SFPlink.setStatus("mandatory")


class _Mc1GO2ORmtPort1SFPExist_Type(Integer32):
    """Custom type mc1GO2ORmtPort1SFPExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("na", 3),
          ("no-card", 0),
          ("removed", 2),
          ("support", 4))
    )


_Mc1GO2ORmtPort1SFPExist_Type.__name__ = "Integer32"
_Mc1GO2ORmtPort1SFPExist_Object = MibTableColumn
mc1GO2ORmtPort1SFPExist = _Mc1GO2ORmtPort1SFPExist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 13),
    _Mc1GO2ORmtPort1SFPExist_Type()
)
mc1GO2ORmtPort1SFPExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2ORmtPort1SFPExist.setStatus("current")


class _Mc1GO2ORmtPort2SFPExist_Type(Integer32):
    """Custom type mc1GO2ORmtPort2SFPExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("na", 3),
          ("no-card", 0),
          ("removed", 2),
          ("support", 4))
    )


_Mc1GO2ORmtPort2SFPExist_Type.__name__ = "Integer32"
_Mc1GO2ORmtPort2SFPExist_Object = MibTableColumn
mc1GO2ORmtPort2SFPExist = _Mc1GO2ORmtPort2SFPExist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 14),
    _Mc1GO2ORmtPort2SFPExist_Type()
)
mc1GO2ORmtPort2SFPExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2ORmtPort2SFPExist.setStatus("current")


class _Mc1GO2ORmtPort3SFPExist_Type(Integer32):
    """Custom type mc1GO2ORmtPort3SFPExist based on Integer32"""
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
        *(("inserted", 1),
          ("na", 3),
          ("not-support", 4),
          ("removed", 2))
    )


_Mc1GO2ORmtPort3SFPExist_Type.__name__ = "Integer32"
_Mc1GO2ORmtPort3SFPExist_Object = MibTableColumn
mc1GO2ORmtPort3SFPExist = _Mc1GO2ORmtPort3SFPExist_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 15),
    _Mc1GO2ORmtPort3SFPExist_Type()
)
mc1GO2ORmtPort3SFPExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2ORmtPort3SFPExist.setStatus("current")


class _Mc1GO2ORmtPortHWPri_Type(Integer32):
    """Custom type mc1GO2ORmtPortHWPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Port1", 1),
          ("Port2", 2),
          ("not-support", 3))
    )


_Mc1GO2ORmtPortHWPri_Type.__name__ = "Integer32"
_Mc1GO2ORmtPortHWPri_Object = MibTableColumn
mc1GO2ORmtPortHWPri = _Mc1GO2ORmtPortHWPri_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 16),
    _Mc1GO2ORmtPortHWPri_Type()
)
mc1GO2ORmtPortHWPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2ORmtPortHWPri.setStatus("current")


class _Mc1GO2ORmtPort3HWSpd_Type(Integer32):
    """Custom type mc1GO2ORmtPort3HWSpd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("M100", 1),
          ("M1000", 2),
          ("not-support", 3))
    )


_Mc1GO2ORmtPort3HWSpd_Type.__name__ = "Integer32"
_Mc1GO2ORmtPort3HWSpd_Object = MibTableColumn
mc1GO2ORmtPort3HWSpd = _Mc1GO2ORmtPort3HWSpd_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 1, 1, 1, 17),
    _Mc1GO2ORmtPort3HWSpd_Type()
)
mc1GO2ORmtPort3HWSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1GO2ORmtPort3HWSpd.setStatus("current")
_Mc1GO2OSFP3Objects_ObjectIdentity = ObjectIdentity
mc1GO2OSFP3Objects = _Mc1GO2OSFP3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2)
)
_Mc1GO2OSfp3Table_Object = MibTable
mc1GO2OSfp3Table = _Mc1GO2OSfp3Table_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1)
)
if mibBuilder.loadTexts:
    mc1GO2OSfp3Table.setStatus("current")
_Mc1GO2OSfp3Entry_Object = MibTableRow
mc1GO2OSfp3Entry = _Mc1GO2OSfp3Entry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1)
)
mc1GO2OSfp3Entry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
    (0, "XXX-MIB", "mcLoOrRmtFg"),
)
if mibBuilder.loadTexts:
    mc1GO2OSfp3Entry.setStatus("current")


class _Mc1go2o_getSfpCmd_Type(Integer32):
    """Custom type mc1go2o_getSfpCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("na", 0),
          ("remote", 2))
    )


_Mc1go2o_getSfpCmd_Type.__name__ = "Integer32"
_Mc1go2o_getSfpCmd_Object = MibScalar
mc1go2o_getSfpCmd = _Mc1go2o_getSfpCmd_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1, 1),
    _Mc1go2o_getSfpCmd_Type()
)
mc1go2o_getSfpCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc1go2o_getSfpCmd.setStatus("current")
_Mc1go2o_sfpCompliance_Type = Integer32
_Mc1go2o_sfpCompliance_Object = MibScalar
mc1go2o_sfpCompliance = _Mc1go2o_sfpCompliance_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1, 2),
    _Mc1go2o_sfpCompliance_Type()
)
mc1go2o_sfpCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1go2o_sfpCompliance.setStatus("current")
_Mc1go2o_sfpConnector_Type = Integer32
_Mc1go2o_sfpConnector_Object = MibScalar
mc1go2o_sfpConnector = _Mc1go2o_sfpConnector_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1, 3),
    _Mc1go2o_sfpConnector_Type()
)
mc1go2o_sfpConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1go2o_sfpConnector.setStatus("current")
_Mc1go2o_sfpTransCode_Type = Integer32
_Mc1go2o_sfpTransCode_Object = MibScalar
mc1go2o_sfpTransCode = _Mc1go2o_sfpTransCode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1, 4),
    _Mc1go2o_sfpTransCode_Type()
)
mc1go2o_sfpTransCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1go2o_sfpTransCode.setStatus("current")
_Mc1go2o_sfpSmLength_Type = Integer32
_Mc1go2o_sfpSmLength_Object = MibScalar
mc1go2o_sfpSmLength = _Mc1go2o_sfpSmLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1, 5),
    _Mc1go2o_sfpSmLength_Type()
)
mc1go2o_sfpSmLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1go2o_sfpSmLength.setStatus("current")
_Mc1go2o_sfpMmLength_Type = Integer32
_Mc1go2o_sfpMmLength_Object = MibScalar
mc1go2o_sfpMmLength = _Mc1go2o_sfpMmLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1, 6),
    _Mc1go2o_sfpMmLength_Type()
)
mc1go2o_sfpMmLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1go2o_sfpMmLength.setStatus("current")
_Mc1go2o_sfpCopperLength_Type = Integer32
_Mc1go2o_sfpCopperLength_Object = MibScalar
mc1go2o_sfpCopperLength = _Mc1go2o_sfpCopperLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1, 7),
    _Mc1go2o_sfpCopperLength_Type()
)
mc1go2o_sfpCopperLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1go2o_sfpCopperLength.setStatus("current")
_Mc1go2o_sfpBrSpeed_Type = Integer32
_Mc1go2o_sfpBrSpeed_Object = MibScalar
mc1go2o_sfpBrSpeed = _Mc1go2o_sfpBrSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1, 8),
    _Mc1go2o_sfpBrSpeed_Type()
)
mc1go2o_sfpBrSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1go2o_sfpBrSpeed.setStatus("current")
_Mc1go2o_sfpWavelength_Type = Integer32
_Mc1go2o_sfpWavelength_Object = MibScalar
mc1go2o_sfpWavelength = _Mc1go2o_sfpWavelength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1, 9),
    _Mc1go2o_sfpWavelength_Type()
)
mc1go2o_sfpWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1go2o_sfpWavelength.setStatus("current")
_Mc1go2o_sfpTemperature_Type = Integer32
_Mc1go2o_sfpTemperature_Object = MibScalar
mc1go2o_sfpTemperature = _Mc1go2o_sfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1, 10),
    _Mc1go2o_sfpTemperature_Type()
)
mc1go2o_sfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1go2o_sfpTemperature.setStatus("current")
_Mc1go2o_sfpTranPower_Type = Integer32
_Mc1go2o_sfpTranPower_Object = MibScalar
mc1go2o_sfpTranPower = _Mc1go2o_sfpTranPower_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1, 11),
    _Mc1go2o_sfpTranPower_Type()
)
mc1go2o_sfpTranPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1go2o_sfpTranPower.setStatus("current")
_Mc1go2o_sfpRecvPower_Type = Integer32
_Mc1go2o_sfpRecvPower_Object = MibScalar
mc1go2o_sfpRecvPower = _Mc1go2o_sfpRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1, 12),
    _Mc1go2o_sfpRecvPower_Type()
)
mc1go2o_sfpRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1go2o_sfpRecvPower.setStatus("current")
_Mc1go2o_sfpVoltage_Type = Integer32
_Mc1go2o_sfpVoltage_Object = MibScalar
mc1go2o_sfpVoltage = _Mc1go2o_sfpVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 13, 2, 1, 1, 13),
    _Mc1go2o_sfpVoltage_Type()
)
mc1go2o_sfpVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc1go2o_sfpVoltage.setStatus("current")
_Mc10GOEO1RObjects_ObjectIdentity = ObjectIdentity
mc10GOEO1RObjects = _Mc10GOEO1RObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 14)
)
_Mc10GOEO1RCardObjects_ObjectIdentity = ObjectIdentity
mc10GOEO1RCardObjects = _Mc10GOEO1RCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 14, 1)
)
_Mc10GOEO1RCardTable_Object = MibTable
mc10GOEO1RCardTable = _Mc10GOEO1RCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    mc10GOEO1RCardTable.setStatus("current")
_Mc10GOEO1RCardEntry_Object = MibTableRow
mc10GOEO1RCardEntry = _Mc10GOEO1RCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 14, 1, 1, 1)
)
mc10GOEO1RCardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mc10GOEO1RCardEntry.setStatus("current")


class _McAccXFP1WaveLengthTunability_Type(Integer32):
    """Custom type mcAccXFP1WaveLengthTunability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Supported", 1),
          ("Unsupported", 2),
          ("not-support", 3))
    )


_McAccXFP1WaveLengthTunability_Type.__name__ = "Integer32"
_McAccXFP1WaveLengthTunability_Object = MibTableColumn
mcAccXFP1WaveLengthTunability = _McAccXFP1WaveLengthTunability_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 14, 1, 1, 1, 1),
    _McAccXFP1WaveLengthTunability_Type()
)
mcAccXFP1WaveLengthTunability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcAccXFP1WaveLengthTunability.setStatus("mandatory")


class _McAccXFP1WaveLengthTunable_Type(Integer32):
    """Custom type mcAccXFP1WaveLengthTunable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Completed", 2),
          ("Doing", 1),
          ("not-support", 3))
    )


_McAccXFP1WaveLengthTunable_Type.__name__ = "Integer32"
_McAccXFP1WaveLengthTunable_Object = MibTableColumn
mcAccXFP1WaveLengthTunable = _McAccXFP1WaveLengthTunable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 14, 1, 1, 1, 2),
    _McAccXFP1WaveLengthTunable_Type()
)
mcAccXFP1WaveLengthTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcAccXFP1WaveLengthTunable.setStatus("mandatory")
_McAccXFP1WaveLength_Type = Integer32
_McAccXFP1WaveLength_Object = MibTableColumn
mcAccXFP1WaveLength = _McAccXFP1WaveLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 14, 1, 1, 1, 3),
    _McAccXFP1WaveLength_Type()
)
mcAccXFP1WaveLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcAccXFP1WaveLength.setStatus("mandatory")


class _McNtwXFP2WaveLengthTunability_Type(Integer32):
    """Custom type mcNtwXFP2WaveLengthTunability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Supported", 1),
          ("Unsupported", 2),
          ("not-support", 3))
    )


_McNtwXFP2WaveLengthTunability_Type.__name__ = "Integer32"
_McNtwXFP2WaveLengthTunability_Object = MibTableColumn
mcNtwXFP2WaveLengthTunability = _McNtwXFP2WaveLengthTunability_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 14, 1, 1, 1, 4),
    _McNtwXFP2WaveLengthTunability_Type()
)
mcNtwXFP2WaveLengthTunability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcNtwXFP2WaveLengthTunability.setStatus("mandatory")


class _McNtwXFP2WaveLengthTunable_Type(Integer32):
    """Custom type mcNtwXFP2WaveLengthTunable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Completed", 2),
          ("Doing", 1),
          ("not-support", 3))
    )


_McNtwXFP2WaveLengthTunable_Type.__name__ = "Integer32"
_McNtwXFP2WaveLengthTunable_Object = MibTableColumn
mcNtwXFP2WaveLengthTunable = _McNtwXFP2WaveLengthTunable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 14, 1, 1, 1, 5),
    _McNtwXFP2WaveLengthTunable_Type()
)
mcNtwXFP2WaveLengthTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcNtwXFP2WaveLengthTunable.setStatus("mandatory")
_McNtwXFP2WaveLength_Type = Integer32
_McNtwXFP2WaveLength_Object = MibTableColumn
mcNtwXFP2WaveLength = _McNtwXFP2WaveLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 14, 1, 1, 1, 6),
    _McNtwXFP2WaveLength_Type()
)
mcNtwXFP2WaveLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcNtwXFP2WaveLength.setStatus("mandatory")


class _McAccXFP1TunableType_Type(Integer32):
    """Custom type mcAccXFP1TunableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("channel", 1),
          ("not-support", 3),
          ("wavelength", 2))
    )


_McAccXFP1TunableType_Type.__name__ = "Integer32"
_McAccXFP1TunableType_Object = MibTableColumn
mcAccXFP1TunableType = _McAccXFP1TunableType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 14, 1, 1, 1, 7),
    _McAccXFP1TunableType_Type()
)
mcAccXFP1TunableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcAccXFP1TunableType.setStatus("mandatory")


class _McNtwXFP2TunableType_Type(Integer32):
    """Custom type mcNtwXFP2TunableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("channel", 1),
          ("not-support", 3),
          ("wavelength", 2))
    )


_McNtwXFP2TunableType_Type.__name__ = "Integer32"
_McNtwXFP2TunableType_Object = MibTableColumn
mcNtwXFP2TunableType = _McNtwXFP2TunableType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 14, 1, 1, 1, 8),
    _McNtwXFP2TunableType_Type()
)
mcNtwXFP2TunableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcNtwXFP2TunableType.setStatus("mandatory")
_Mc10GOEO3RObjects_ObjectIdentity = ObjectIdentity
mc10GOEO3RObjects = _Mc10GOEO3RObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 15)
)
_Mc10GOEO3RCardObjects_ObjectIdentity = ObjectIdentity
mc10GOEO3RCardObjects = _Mc10GOEO3RCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 15, 1)
)
_Mc10GOEO3RCardTable_Object = MibTable
mc10GOEO3RCardTable = _Mc10GOEO3RCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 15, 1, 1)
)
if mibBuilder.loadTexts:
    mc10GOEO3RCardTable.setStatus("current")
_Mc10GOEO3RCardEntry_Object = MibTableRow
mc10GOEO3RCardEntry = _Mc10GOEO3RCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 15, 1, 1, 1)
)
mc10GOEO3RCardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mc10GOEO3RCardEntry.setStatus("current")


class _AccXFP1WaveLengthTunability_Type(Integer32):
    """Custom type accXFP1WaveLengthTunability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Supported", 1),
          ("Unsupported", 2),
          ("not-support", 3))
    )


_AccXFP1WaveLengthTunability_Type.__name__ = "Integer32"
_AccXFP1WaveLengthTunability_Object = MibTableColumn
accXFP1WaveLengthTunability = _AccXFP1WaveLengthTunability_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 15, 1, 1, 1, 1),
    _AccXFP1WaveLengthTunability_Type()
)
accXFP1WaveLengthTunability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXFP1WaveLengthTunability.setStatus("mandatory")


class _AccXFP1WaveLengthTunable_Type(Integer32):
    """Custom type accXFP1WaveLengthTunable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Completed", 2),
          ("Doing", 1),
          ("not-support", 3))
    )


_AccXFP1WaveLengthTunable_Type.__name__ = "Integer32"
_AccXFP1WaveLengthTunable_Object = MibTableColumn
accXFP1WaveLengthTunable = _AccXFP1WaveLengthTunable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 15, 1, 1, 1, 2),
    _AccXFP1WaveLengthTunable_Type()
)
accXFP1WaveLengthTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXFP1WaveLengthTunable.setStatus("mandatory")
_AccXFP1WaveLength_Type = Integer32
_AccXFP1WaveLength_Object = MibTableColumn
accXFP1WaveLength = _AccXFP1WaveLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 15, 1, 1, 1, 3),
    _AccXFP1WaveLength_Type()
)
accXFP1WaveLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXFP1WaveLength.setStatus("mandatory")


class _NtwXFP2WaveLengthTunability_Type(Integer32):
    """Custom type ntwXFP2WaveLengthTunability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Supported", 1),
          ("Unsupported", 2),
          ("not-support", 3))
    )


_NtwXFP2WaveLengthTunability_Type.__name__ = "Integer32"
_NtwXFP2WaveLengthTunability_Object = MibTableColumn
ntwXFP2WaveLengthTunability = _NtwXFP2WaveLengthTunability_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 15, 1, 1, 1, 4),
    _NtwXFP2WaveLengthTunability_Type()
)
ntwXFP2WaveLengthTunability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwXFP2WaveLengthTunability.setStatus("mandatory")


class _NtwXFP2WaveLengthTunable_Type(Integer32):
    """Custom type ntwXFP2WaveLengthTunable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Completed", 2),
          ("Doing", 1),
          ("not-support", 3))
    )


_NtwXFP2WaveLengthTunable_Type.__name__ = "Integer32"
_NtwXFP2WaveLengthTunable_Object = MibTableColumn
ntwXFP2WaveLengthTunable = _NtwXFP2WaveLengthTunable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 15, 1, 1, 1, 5),
    _NtwXFP2WaveLengthTunable_Type()
)
ntwXFP2WaveLengthTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwXFP2WaveLengthTunable.setStatus("mandatory")
_NtwXFP2WaveLength_Type = Integer32
_NtwXFP2WaveLength_Object = MibTableColumn
ntwXFP2WaveLength = _NtwXFP2WaveLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 15, 1, 1, 1, 6),
    _NtwXFP2WaveLength_Type()
)
ntwXFP2WaveLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntwXFP2WaveLength.setStatus("mandatory")


class _AccXFP1TunableType_Type(Integer32):
    """Custom type accXFP1TunableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("channel", 1),
          ("not-support", 3),
          ("wavelength", 2))
    )


_AccXFP1TunableType_Type.__name__ = "Integer32"
_AccXFP1TunableType_Object = MibTableColumn
accXFP1TunableType = _AccXFP1TunableType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 15, 1, 1, 1, 7),
    _AccXFP1TunableType_Type()
)
accXFP1TunableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXFP1TunableType.setStatus("mandatory")


class _NtwXFP2TunableType_Type(Integer32):
    """Custom type ntwXFP2TunableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("channel", 1),
          ("not-support", 3),
          ("wavelength", 2))
    )


_NtwXFP2TunableType_Type.__name__ = "Integer32"
_NtwXFP2TunableType_Object = MibTableColumn
ntwXFP2TunableType = _NtwXFP2TunableType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 15, 1, 1, 1, 8),
    _NtwXFP2TunableType_Type()
)
ntwXFP2TunableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwXFP2TunableType.setStatus("mandatory")
_McCWDMObjects_ObjectIdentity = ObjectIdentity
mcCWDMObjects = _McCWDMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 16)
)
_McCWDMCardObjects_ObjectIdentity = ObjectIdentity
mcCWDMCardObjects = _McCWDMCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 16, 1)
)
_McCWDMCardTable_Object = MibTable
mcCWDMCardTable = _McCWDMCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 16, 1, 1)
)
if mibBuilder.loadTexts:
    mcCWDMCardTable.setStatus("current")
_McCWDMCardEntry_Object = MibTableRow
mcCWDMCardEntry = _McCWDMCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 16, 1, 1, 1)
)
mcCWDMCardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mcCWDMCardEntry.setStatus("current")
_CwdmWavelengthCount_Type = Integer32
_CwdmWavelengthCount_Object = MibTableColumn
cwdmWavelengthCount = _CwdmWavelengthCount_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 16, 1, 1, 1, 1),
    _CwdmWavelengthCount_Type()
)
cwdmWavelengthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmWavelengthCount.setStatus("mandatory")
_CwdmWavelength1_Type = DisplayString
_CwdmWavelength1_Object = MibTableColumn
cwdmWavelength1 = _CwdmWavelength1_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 16, 1, 1, 1, 2),
    _CwdmWavelength1_Type()
)
cwdmWavelength1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmWavelength1.setStatus("mandatory")
_CwdmWavelength2_Type = DisplayString
_CwdmWavelength2_Object = MibTableColumn
cwdmWavelength2 = _CwdmWavelength2_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 16, 1, 1, 1, 3),
    _CwdmWavelength2_Type()
)
cwdmWavelength2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmWavelength2.setStatus("mandatory")
_CwdmWavelength3_Type = DisplayString
_CwdmWavelength3_Object = MibTableColumn
cwdmWavelength3 = _CwdmWavelength3_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 16, 1, 1, 1, 4),
    _CwdmWavelength3_Type()
)
cwdmWavelength3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmWavelength3.setStatus("mandatory")
_CwdmWavelength4_Type = DisplayString
_CwdmWavelength4_Object = MibTableColumn
cwdmWavelength4 = _CwdmWavelength4_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 16, 1, 1, 1, 5),
    _CwdmWavelength4_Type()
)
cwdmWavelength4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmWavelength4.setStatus("mandatory")
_CwdmWavelength5_Type = DisplayString
_CwdmWavelength5_Object = MibTableColumn
cwdmWavelength5 = _CwdmWavelength5_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 16, 1, 1, 1, 6),
    _CwdmWavelength5_Type()
)
cwdmWavelength5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmWavelength5.setStatus("mandatory")
_CwdmWavelength6_Type = DisplayString
_CwdmWavelength6_Object = MibTableColumn
cwdmWavelength6 = _CwdmWavelength6_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 16, 1, 1, 1, 7),
    _CwdmWavelength6_Type()
)
cwdmWavelength6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmWavelength6.setStatus("mandatory")
_CwdmWavelength7_Type = DisplayString
_CwdmWavelength7_Object = MibTableColumn
cwdmWavelength7 = _CwdmWavelength7_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 16, 1, 1, 1, 8),
    _CwdmWavelength7_Type()
)
cwdmWavelength7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmWavelength7.setStatus("mandatory")
_CwdmWavelength8_Type = DisplayString
_CwdmWavelength8_Object = MibTableColumn
cwdmWavelength8 = _CwdmWavelength8_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 16, 1, 1, 1, 9),
    _CwdmWavelength8_Type()
)
cwdmWavelength8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmWavelength8.setStatus("mandatory")
_Mc10G_OEO2RObjects_ObjectIdentity = ObjectIdentity
mc10G_OEO2RObjects = _Mc10G_OEO2RObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17)
)
_Mc10G_OEO2RCardObjects_ObjectIdentity = ObjectIdentity
mc10G_OEO2RCardObjects = _Mc10G_OEO2RCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1)
)
_Mc10G_OEO2RCardTable_Object = MibTable
mc10G_OEO2RCardTable = _Mc10G_OEO2RCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1)
)
if mibBuilder.loadTexts:
    mc10G_OEO2RCardTable.setStatus("current")
_Mc10G_OEO2RCardEntry_Object = MibTableRow
mc10G_OEO2RCardEntry = _Mc10G_OEO2RCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1)
)
mc10G_OEO2RCardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mc10G_OEO2RCardEntry.setStatus("current")


class _Mc10G_OEO2RCurSpdMode_Type(Integer32):
    """Custom type mc10G_OEO2RCurSpdMode based on Integer32"""
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
        *(("Speed103to117", 2),
          ("Speed85", 1),
          ("Speed995to113", 3),
          ("not-support", 4))
    )


_Mc10G_OEO2RCurSpdMode_Type.__name__ = "Integer32"
_Mc10G_OEO2RCurSpdMode_Object = MibScalar
mc10G_OEO2RCurSpdMode = _Mc10G_OEO2RCurSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 1),
    _Mc10G_OEO2RCurSpdMode_Type()
)
mc10G_OEO2RCurSpdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO2RCurSpdMode.setStatus("mandatory")


class _Mc10G_OEO2RCfgSpdMode_Type(Integer32):
    """Custom type mc10G_OEO2RCfgSpdMode based on Integer32"""
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
        *(("Speed103to117", 2),
          ("Speed85", 1),
          ("Speed995to113", 3),
          ("not-support", 4))
    )


_Mc10G_OEO2RCfgSpdMode_Type.__name__ = "Integer32"
_Mc10G_OEO2RCfgSpdMode_Object = MibScalar
mc10G_OEO2RCfgSpdMode = _Mc10G_OEO2RCfgSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 2),
    _Mc10G_OEO2RCfgSpdMode_Type()
)
mc10G_OEO2RCfgSpdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc10G_OEO2RCfgSpdMode.setStatus("mandatory")


class _Mc10G_OEO2RSFP1Loopback_Type(Integer32):
    """Custom type mc10G_OEO2RSFP1Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_Mc10G_OEO2RSFP1Loopback_Type.__name__ = "Integer32"
_Mc10G_OEO2RSFP1Loopback_Object = MibScalar
mc10G_OEO2RSFP1Loopback = _Mc10G_OEO2RSFP1Loopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 3),
    _Mc10G_OEO2RSFP1Loopback_Type()
)
mc10G_OEO2RSFP1Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc10G_OEO2RSFP1Loopback.setStatus("current")


class _Mc10G_OEO2RSFP2Loopback_Type(Integer32):
    """Custom type mc10G_OEO2RSFP2Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_Mc10G_OEO2RSFP2Loopback_Type.__name__ = "Integer32"
_Mc10G_OEO2RSFP2Loopback_Object = MibScalar
mc10G_OEO2RSFP2Loopback = _Mc10G_OEO2RSFP2Loopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 4),
    _Mc10G_OEO2RSFP2Loopback_Type()
)
mc10G_OEO2RSFP2Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc10G_OEO2RSFP2Loopback.setStatus("current")


class _Mc10G_OEO2RSFP1_Type(Integer32):
    """Custom type mc10G_OEO2RSFP1 based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc10G_OEO2RSFP1_Type.__name__ = "Integer32"
_Mc10G_OEO2RSFP1_Object = MibScalar
mc10G_OEO2RSFP1 = _Mc10G_OEO2RSFP1_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 5),
    _Mc10G_OEO2RSFP1_Type()
)
mc10G_OEO2RSFP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO2RSFP1.setStatus("current")


class _Mc10G_OEO2RSFP2_Type(Integer32):
    """Custom type mc10G_OEO2RSFP2 based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_Mc10G_OEO2RSFP2_Type.__name__ = "Integer32"
_Mc10G_OEO2RSFP2_Object = MibScalar
mc10G_OEO2RSFP2 = _Mc10G_OEO2RSFP2_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 6),
    _Mc10G_OEO2RSFP2_Type()
)
mc10G_OEO2RSFP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO2RSFP2.setStatus("current")


class _Mc10G_OEO2RHWSpdMode_Type(Integer32):
    """Custom type mc10G_OEO2RHWSpdMode based on Integer32"""
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
        *(("Speed103to117", 2),
          ("Speed85", 1),
          ("Speed995to113", 3),
          ("not-support", 4))
    )


_Mc10G_OEO2RHWSpdMode_Type.__name__ = "Integer32"
_Mc10G_OEO2RHWSpdMode_Object = MibScalar
mc10G_OEO2RHWSpdMode = _Mc10G_OEO2RHWSpdMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 7),
    _Mc10G_OEO2RHWSpdMode_Type()
)
mc10G_OEO2RHWSpdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO2RHWSpdMode.setStatus("current")


class _Mc10G_OEO2RHWSFP1Loopback_Type(Integer32):
    """Custom type mc10G_OEO2RHWSFP1Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_Mc10G_OEO2RHWSFP1Loopback_Type.__name__ = "Integer32"
_Mc10G_OEO2RHWSFP1Loopback_Object = MibScalar
mc10G_OEO2RHWSFP1Loopback = _Mc10G_OEO2RHWSFP1Loopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 8),
    _Mc10G_OEO2RHWSFP1Loopback_Type()
)
mc10G_OEO2RHWSFP1Loopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO2RHWSFP1Loopback.setStatus("current")


class _Mc10G_OEO2RHWSFP2Loopback_Type(Integer32):
    """Custom type mc10G_OEO2RHWSFP2Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_Mc10G_OEO2RHWSFP2Loopback_Type.__name__ = "Integer32"
_Mc10G_OEO2RHWSFP2Loopback_Object = MibScalar
mc10G_OEO2RHWSFP2Loopback = _Mc10G_OEO2RHWSFP2Loopback_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 9),
    _Mc10G_OEO2RHWSFP2Loopback_Type()
)
mc10G_OEO2RHWSFP2Loopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO2RHWSFP2Loopback.setStatus("current")
_Mc10G_OEO2RVersion_Type = DisplayString
_Mc10G_OEO2RVersion_Object = MibScalar
mc10G_OEO2RVersion = _Mc10G_OEO2RVersion_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 10),
    _Mc10G_OEO2RVersion_Type()
)
mc10G_OEO2RVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO2RVersion.setStatus("mandatory")


class _Mc10GXFP1WaveLengthTunability_Type(Integer32):
    """Custom type mc10GXFP1WaveLengthTunability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Supported", 1),
          ("Unsupported", 2),
          ("not-support", 3))
    )


_Mc10GXFP1WaveLengthTunability_Type.__name__ = "Integer32"
_Mc10GXFP1WaveLengthTunability_Object = MibTableColumn
mc10GXFP1WaveLengthTunability = _Mc10GXFP1WaveLengthTunability_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 11),
    _Mc10GXFP1WaveLengthTunability_Type()
)
mc10GXFP1WaveLengthTunability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10GXFP1WaveLengthTunability.setStatus("mandatory")


class _Mc10GXFP1WaveLengthTunable_Type(Integer32):
    """Custom type mc10GXFP1WaveLengthTunable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Completed", 2),
          ("Doing", 1),
          ("not-support", 3))
    )


_Mc10GXFP1WaveLengthTunable_Type.__name__ = "Integer32"
_Mc10GXFP1WaveLengthTunable_Object = MibTableColumn
mc10GXFP1WaveLengthTunable = _Mc10GXFP1WaveLengthTunable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 12),
    _Mc10GXFP1WaveLengthTunable_Type()
)
mc10GXFP1WaveLengthTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10GXFP1WaveLengthTunable.setStatus("mandatory")
_Mc10GXFP1WaveLength_Type = Integer32
_Mc10GXFP1WaveLength_Object = MibTableColumn
mc10GXFP1WaveLength = _Mc10GXFP1WaveLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 13),
    _Mc10GXFP1WaveLength_Type()
)
mc10GXFP1WaveLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc10GXFP1WaveLength.setStatus("mandatory")


class _Mc10GXFP2WaveLengthTunability_Type(Integer32):
    """Custom type mc10GXFP2WaveLengthTunability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Supported", 1),
          ("Unsupported", 2),
          ("not-support", 3))
    )


_Mc10GXFP2WaveLengthTunability_Type.__name__ = "Integer32"
_Mc10GXFP2WaveLengthTunability_Object = MibTableColumn
mc10GXFP2WaveLengthTunability = _Mc10GXFP2WaveLengthTunability_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 14),
    _Mc10GXFP2WaveLengthTunability_Type()
)
mc10GXFP2WaveLengthTunability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10GXFP2WaveLengthTunability.setStatus("mandatory")


class _Mc10GXFP2WaveLengthTunable_Type(Integer32):
    """Custom type mc10GXFP2WaveLengthTunable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Completed", 2),
          ("Doing", 1),
          ("not-support", 3))
    )


_Mc10GXFP2WaveLengthTunable_Type.__name__ = "Integer32"
_Mc10GXFP2WaveLengthTunable_Object = MibTableColumn
mc10GXFP2WaveLengthTunable = _Mc10GXFP2WaveLengthTunable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 15),
    _Mc10GXFP2WaveLengthTunable_Type()
)
mc10GXFP2WaveLengthTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10GXFP2WaveLengthTunable.setStatus("mandatory")
_Mc10GXFP2WaveLength_Type = Integer32
_Mc10GXFP2WaveLength_Object = MibTableColumn
mc10GXFP2WaveLength = _Mc10GXFP2WaveLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 16),
    _Mc10GXFP2WaveLength_Type()
)
mc10GXFP2WaveLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc10GXFP2WaveLength.setStatus("mandatory")


class _Mc10G_OEO2R_accType_Type(Integer32):
    """Custom type mc10G_OEO2R_accType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("SFP", 2),
          ("XFP", 1),
          ("unknow", 3))
    )


_Mc10G_OEO2R_accType_Type.__name__ = "Integer32"
_Mc10G_OEO2R_accType_Object = MibScalar
mc10G_OEO2R_accType = _Mc10G_OEO2R_accType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 17),
    _Mc10G_OEO2R_accType_Type()
)
mc10G_OEO2R_accType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO2R_accType.setStatus("current")


class _Mc10G_OEO2R_ntwType_Type(Integer32):
    """Custom type mc10G_OEO2R_ntwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("SFP", 2),
          ("XFP", 1),
          ("unknow", 3))
    )


_Mc10G_OEO2R_ntwType_Type.__name__ = "Integer32"
_Mc10G_OEO2R_ntwType_Object = MibScalar
mc10G_OEO2R_ntwType = _Mc10G_OEO2R_ntwType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 18),
    _Mc10G_OEO2R_ntwType_Type()
)
mc10G_OEO2R_ntwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO2R_ntwType.setStatus("current")


class _Mc10G_OEO2R_accTunableType_Type(Integer32):
    """Custom type mc10G_OEO2R_accTunableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("channel", 1),
          ("not-support", 3),
          ("wavelength", 2))
    )


_Mc10G_OEO2R_accTunableType_Type.__name__ = "Integer32"
_Mc10G_OEO2R_accTunableType_Object = MibScalar
mc10G_OEO2R_accTunableType = _Mc10G_OEO2R_accTunableType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 19),
    _Mc10G_OEO2R_accTunableType_Type()
)
mc10G_OEO2R_accTunableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO2R_accTunableType.setStatus("mandatory")


class _Mc10G_OEO2R_ntwTunableType_Type(Integer32):
    """Custom type mc10G_OEO2R_ntwTunableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("channel", 1),
          ("not-support", 3),
          ("wavelength", 2))
    )


_Mc10G_OEO2R_ntwTunableType_Type.__name__ = "Integer32"
_Mc10G_OEO2R_ntwTunableType_Object = MibScalar
mc10G_OEO2R_ntwTunableType = _Mc10G_OEO2R_ntwTunableType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 17, 1, 1, 1, 20),
    _Mc10G_OEO2R_ntwTunableType_Type()
)
mc10G_OEO2R_ntwTunableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc10G_OEO2R_ntwTunableType.setStatus("mandatory")
_McQCA8334Objects_ObjectIdentity = ObjectIdentity
mcQCA8334Objects = _McQCA8334Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18)
)
_McQCA8334CardObjects_ObjectIdentity = ObjectIdentity
mcQCA8334CardObjects = _McQCA8334CardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 1)
)
_McQCA8334CardTable_Object = MibTable
mcQCA8334CardTable = _McQCA8334CardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 1, 1)
)
if mibBuilder.loadTexts:
    mcQCA8334CardTable.setStatus("current")
_McQCA8334CardEntry_Object = MibTableRow
mcQCA8334CardEntry = _McQCA8334CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 1, 1, 1)
)
mcQCA8334CardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mcQCA8334CardEntry.setStatus("current")


class _McQCA8334VlanMode_Type(Integer32):
    """Custom type mcQCA8334VlanMode based on Integer32"""
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
        *(("Normal", 1),
          ("mode1", 2),
          ("mode2", 3),
          ("not-support", 4))
    )


_McQCA8334VlanMode_Type.__name__ = "Integer32"
_McQCA8334VlanMode_Object = MibTableColumn
mcQCA8334VlanMode = _McQCA8334VlanMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 1, 1, 1, 1),
    _McQCA8334VlanMode_Type()
)
mcQCA8334VlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcQCA8334VlanMode.setStatus("current")
_McQCA8334PortObjects_ObjectIdentity = ObjectIdentity
mcQCA8334PortObjects = _McQCA8334PortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 2)
)
_McQCA8334PortTable_Object = MibTable
mcQCA8334PortTable = _McQCA8334PortTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    mcQCA8334PortTable.setStatus("current")
_McQCA8334PortEntry_Object = MibTableRow
mcQCA8334PortEntry = _McQCA8334PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 2, 1, 1)
)
mcQCA8334PortEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
    (0, "XXX-MIB", "mcQCA8334PortIdx"),
)
if mibBuilder.loadTexts:
    mcQCA8334PortEntry.setStatus("current")


class _McQCA8334PortIdx_Type(Integer32):
    """Custom type mcQCA8334PortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port1", 1),
          ("port2", 2))
    )


_McQCA8334PortIdx_Type.__name__ = "Integer32"
_McQCA8334PortIdx_Object = MibTableColumn
mcQCA8334PortIdx = _McQCA8334PortIdx_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 2, 1, 1, 1),
    _McQCA8334PortIdx_Type()
)
mcQCA8334PortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcQCA8334PortIdx.setStatus("current")


class _McQCA8334CurWorkMode_Type(Integer32):
    """Custom type mcQCA8334CurWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("not-support", 7))
    )


_McQCA8334CurWorkMode_Type.__name__ = "Integer32"
_McQCA8334CurWorkMode_Object = MibTableColumn
mcQCA8334CurWorkMode = _McQCA8334CurWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 2, 1, 1, 2),
    _McQCA8334CurWorkMode_Type()
)
mcQCA8334CurWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcQCA8334CurWorkMode.setStatus("mandatory")


class _McQCA8334CfgWorkMode_Type(Integer32):
    """Custom type mcQCA8334CfgWorkMode based on Integer32"""
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
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("mAuto", 1),
          ("not-support", 7))
    )


_McQCA8334CfgWorkMode_Type.__name__ = "Integer32"
_McQCA8334CfgWorkMode_Object = MibTableColumn
mcQCA8334CfgWorkMode = _McQCA8334CfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 2, 1, 1, 3),
    _McQCA8334CfgWorkMode_Type()
)
mcQCA8334CfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcQCA8334CfgWorkMode.setStatus("mandatory")


class _McQCA8334UpStream_Type(Gauge32):
    """Custom type mcQCA8334UpStream based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1000000),
    )


_McQCA8334UpStream_Type.__name__ = "Gauge32"
_McQCA8334UpStream_Object = MibTableColumn
mcQCA8334UpStream = _McQCA8334UpStream_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 2, 1, 1, 4),
    _McQCA8334UpStream_Type()
)
mcQCA8334UpStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcQCA8334UpStream.setStatus("current")


class _McQCA8334DownStream_Type(Gauge32):
    """Custom type mcQCA8334DownStream based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1000000),
    )


_McQCA8334DownStream_Type.__name__ = "Gauge32"
_McQCA8334DownStream_Object = MibTableColumn
mcQCA8334DownStream = _McQCA8334DownStream_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 2, 1, 1, 5),
    _McQCA8334DownStream_Type()
)
mcQCA8334DownStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcQCA8334DownStream.setStatus("current")


class _McQCA8334Txlink_Type(Integer32):
    """Custom type mcQCA8334Txlink based on Integer32"""
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
          ("not-support", 3),
          ("up", 1))
    )


_McQCA8334Txlink_Type.__name__ = "Integer32"
_McQCA8334Txlink_Object = MibTableColumn
mcQCA8334Txlink = _McQCA8334Txlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 2, 1, 1, 6),
    _McQCA8334Txlink_Type()
)
mcQCA8334Txlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcQCA8334Txlink.setStatus("current")


class _McQCA8334RmtCurWorkMode_Type(Integer32):
    """Custom type mcQCA8334RmtCurWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("no-card", 0),
          ("not-support", 7))
    )


_McQCA8334RmtCurWorkMode_Type.__name__ = "Integer32"
_McQCA8334RmtCurWorkMode_Object = MibTableColumn
mcQCA8334RmtCurWorkMode = _McQCA8334RmtCurWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 2, 1, 1, 7),
    _McQCA8334RmtCurWorkMode_Type()
)
mcQCA8334RmtCurWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcQCA8334RmtCurWorkMode.setStatus("mandatory")


class _McQCA8334RmtCfgWorkMode_Type(Integer32):
    """Custom type mcQCA8334RmtCfgWorkMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("m10-full", 4),
          ("m10-half", 5),
          ("m100-full", 2),
          ("m100-half", 3),
          ("m1G-full", 6),
          ("mAuto", 1),
          ("no-card", 0),
          ("not-support", 7))
    )


_McQCA8334RmtCfgWorkMode_Type.__name__ = "Integer32"
_McQCA8334RmtCfgWorkMode_Object = MibTableColumn
mcQCA8334RmtCfgWorkMode = _McQCA8334RmtCfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 2, 1, 1, 8),
    _McQCA8334RmtCfgWorkMode_Type()
)
mcQCA8334RmtCfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcQCA8334RmtCfgWorkMode.setStatus("mandatory")


class _McQCA8334RmtTxlink_Type(Integer32):
    """Custom type mcQCA8334RmtTxlink based on Integer32"""
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
        *(("down", 2),
          ("no-card", 0),
          ("not-support", 3),
          ("up", 1))
    )


_McQCA8334RmtTxlink_Type.__name__ = "Integer32"
_McQCA8334RmtTxlink_Object = MibTableColumn
mcQCA8334RmtTxlink = _McQCA8334RmtTxlink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 18, 2, 1, 1, 9),
    _McQCA8334RmtTxlink_Type()
)
mcQCA8334RmtTxlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcQCA8334RmtTxlink.setStatus("current")
_McE1T1Objects_ObjectIdentity = ObjectIdentity
mcE1T1Objects = _McE1T1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19)
)
_McE1T1CardObjects_ObjectIdentity = ObjectIdentity
mcE1T1CardObjects = _McE1T1CardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1)
)
_McE1T1CardTable_Object = MibTable
mcE1T1CardTable = _McE1T1CardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    mcE1T1CardTable.setStatus("current")
_McE1T1CardEntry_Object = MibTableRow
mcE1T1CardEntry = _McE1T1CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1)
)
mcE1T1CardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mcE1T1CardEntry.setStatus("current")


class _McE1T1Type_Type(Integer32):
    """Custom type mcE1T1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("E1", 1),
          ("T1", 2),
          ("not-support", 3))
    )


_McE1T1Type_Type.__name__ = "Integer32"
_McE1T1Type_Object = MibTableColumn
mcE1T1Type = _McE1T1Type_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 1),
    _McE1T1Type_Type()
)
mcE1T1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1T1Type.setStatus("mandatory")


class _McE1T1FLink_Type(Integer32):
    """Custom type mcE1T1FLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Down", 2),
          ("Up", 1),
          ("not-support", 3))
    )


_McE1T1FLink_Type.__name__ = "Integer32"
_McE1T1FLink_Object = MibTableColumn
mcE1T1FLink = _McE1T1FLink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 2),
    _McE1T1FLink_Type()
)
mcE1T1FLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1T1FLink.setStatus("mandatory")


class _McE1T1FLossAlarm_Type(Integer32):
    """Custom type mcE1T1FLossAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Alarm", 1),
          ("Normal", 2),
          ("not-support", 3))
    )


_McE1T1FLossAlarm_Type.__name__ = "Integer32"
_McE1T1FLossAlarm_Object = MibTableColumn
mcE1T1FLossAlarm = _McE1T1FLossAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 3),
    _McE1T1FLossAlarm_Type()
)
mcE1T1FLossAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1T1FLossAlarm.setStatus("current")


class _McE1T1TLossAlarm_Type(Integer32):
    """Custom type mcE1T1TLossAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Alarm", 1),
          ("Normal", 2),
          ("not-support", 3))
    )


_McE1T1TLossAlarm_Type.__name__ = "Integer32"
_McE1T1TLossAlarm_Object = MibTableColumn
mcE1T1TLossAlarm = _McE1T1TLossAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 4),
    _McE1T1TLossAlarm_Type()
)
mcE1T1TLossAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1T1TLossAlarm.setStatus("current")


class _McE1T1AISAlarm_Type(Integer32):
    """Custom type mcE1T1AISAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Alarm", 1),
          ("Normal", 2),
          ("not-support", 3))
    )


_McE1T1AISAlarm_Type.__name__ = "Integer32"
_McE1T1AISAlarm_Object = MibTableColumn
mcE1T1AISAlarm = _McE1T1AISAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 5),
    _McE1T1AISAlarm_Type()
)
mcE1T1AISAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1T1AISAlarm.setStatus("current")


class _McE1T1TLoop_Type(Integer32):
    """Custom type mcE1T1TLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_McE1T1TLoop_Type.__name__ = "Integer32"
_McE1T1TLoop_Object = MibTableColumn
mcE1T1TLoop = _McE1T1TLoop_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 6),
    _McE1T1TLoop_Type()
)
mcE1T1TLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcE1T1TLoop.setStatus("current")


class _McE1T1FLoop_Type(Integer32):
    """Custom type mcE1T1FLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_McE1T1FLoop_Type.__name__ = "Integer32"
_McE1T1FLoop_Object = MibTableColumn
mcE1T1FLoop = _McE1T1FLoop_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 7),
    _McE1T1FLoop_Type()
)
mcE1T1FLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcE1T1FLoop.setStatus("current")


class _McE1T1CodeType_Type(Integer32):
    """Custom type mcE1T1CodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("AMI", 2),
          ("E1-HDB3-Or-T1-B8ZS", 1),
          ("not-support", 3))
    )


_McE1T1CodeType_Type.__name__ = "Integer32"
_McE1T1CodeType_Object = MibTableColumn
mcE1T1CodeType = _McE1T1CodeType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 8),
    _McE1T1CodeType_Type()
)
mcE1T1CodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcE1T1CodeType.setStatus("current")
_McE1T1Version_Type = DisplayString
_McE1T1Version_Object = MibTableColumn
mcE1T1Version = _McE1T1Version_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 9),
    _McE1T1Version_Type()
)
mcE1T1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1T1Version.setStatus("mandatory")


class _McE1T1RmtFLink_Type(Integer32):
    """Custom type mcE1T1RmtFLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Down", 2),
          ("Up", 1),
          ("not-support", 3))
    )


_McE1T1RmtFLink_Type.__name__ = "Integer32"
_McE1T1RmtFLink_Object = MibTableColumn
mcE1T1RmtFLink = _McE1T1RmtFLink_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 10),
    _McE1T1RmtFLink_Type()
)
mcE1T1RmtFLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1T1RmtFLink.setStatus("mandatory")


class _McE1T1RmtFLossAlarm_Type(Integer32):
    """Custom type mcE1T1RmtFLossAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Alarm", 1),
          ("Normal", 2),
          ("not-support", 3))
    )


_McE1T1RmtFLossAlarm_Type.__name__ = "Integer32"
_McE1T1RmtFLossAlarm_Object = MibTableColumn
mcE1T1RmtFLossAlarm = _McE1T1RmtFLossAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 11),
    _McE1T1RmtFLossAlarm_Type()
)
mcE1T1RmtFLossAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1T1RmtFLossAlarm.setStatus("current")


class _McE1T1RmtTLossAlarm_Type(Integer32):
    """Custom type mcE1T1RmtTLossAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Alarm", 1),
          ("Normal", 2),
          ("not-support", 3))
    )


_McE1T1RmtTLossAlarm_Type.__name__ = "Integer32"
_McE1T1RmtTLossAlarm_Object = MibTableColumn
mcE1T1RmtTLossAlarm = _McE1T1RmtTLossAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 12),
    _McE1T1RmtTLossAlarm_Type()
)
mcE1T1RmtTLossAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1T1RmtTLossAlarm.setStatus("current")


class _McE1T1RmtAISAlarm_Type(Integer32):
    """Custom type mcE1T1RmtAISAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Alarm", 1),
          ("Normal", 2),
          ("not-support", 3))
    )


_McE1T1RmtAISAlarm_Type.__name__ = "Integer32"
_McE1T1RmtAISAlarm_Object = MibTableColumn
mcE1T1RmtAISAlarm = _McE1T1RmtAISAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 13),
    _McE1T1RmtAISAlarm_Type()
)
mcE1T1RmtAISAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcE1T1RmtAISAlarm.setStatus("current")


class _McE1T1RmtTLoop_Type(Integer32):
    """Custom type mcE1T1RmtTLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_McE1T1RmtTLoop_Type.__name__ = "Integer32"
_McE1T1RmtTLoop_Object = MibTableColumn
mcE1T1RmtTLoop = _McE1T1RmtTLoop_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 14),
    _McE1T1RmtTLoop_Type()
)
mcE1T1RmtTLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcE1T1RmtTLoop.setStatus("current")


class _McE1T1RmtFLoop_Type(Integer32):
    """Custom type mcE1T1RmtFLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("not-support", 3))
    )


_McE1T1RmtFLoop_Type.__name__ = "Integer32"
_McE1T1RmtFLoop_Object = MibTableColumn
mcE1T1RmtFLoop = _McE1T1RmtFLoop_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 15),
    _McE1T1RmtFLoop_Type()
)
mcE1T1RmtFLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcE1T1RmtFLoop.setStatus("current")


class _McE1T1RmtCodeType_Type(Integer32):
    """Custom type mcE1T1RmtCodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("AMI", 2),
          ("E1-HDB3-Or-T1-B8ZS", 1),
          ("not-support", 3))
    )


_McE1T1RmtCodeType_Type.__name__ = "Integer32"
_McE1T1RmtCodeType_Object = MibTableColumn
mcE1T1RmtCodeType = _McE1T1RmtCodeType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 19, 1, 1, 1, 16),
    _McE1T1RmtCodeType_Type()
)
mcE1T1RmtCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcE1T1RmtCodeType.setStatus("current")
_Mc10GOEEXFPTunableObjects_ObjectIdentity = ObjectIdentity
mc10GOEEXFPTunableObjects = _Mc10GOEEXFPTunableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 20)
)
_Mc10GOEEXFPTunableCardObjects_ObjectIdentity = ObjectIdentity
mc10GOEEXFPTunableCardObjects = _Mc10GOEEXFPTunableCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 20, 1)
)
_Mc10GOEEXFPTunableCardTable_Object = MibTable
mc10GOEEXFPTunableCardTable = _Mc10GOEEXFPTunableCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 20, 1, 1)
)
if mibBuilder.loadTexts:
    mc10GOEEXFPTunableCardTable.setStatus("current")
_Mc10GOEEXFPTunableCardEntry_Object = MibTableRow
mc10GOEEXFPTunableCardEntry = _Mc10GOEEXFPTunableCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 20, 1, 1, 1)
)
mc10GOEEXFPTunableCardEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mc10GOEEXFPTunableCardEntry.setStatus("current")


class _XfpWaveLengthTunability_Type(Integer32):
    """Custom type xfpWaveLengthTunability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Supported", 1),
          ("Unsupported", 2),
          ("not-support", 3))
    )


_XfpWaveLengthTunability_Type.__name__ = "Integer32"
_XfpWaveLengthTunability_Object = MibTableColumn
xfpWaveLengthTunability = _XfpWaveLengthTunability_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 20, 1, 1, 1, 1),
    _XfpWaveLengthTunability_Type()
)
xfpWaveLengthTunability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfpWaveLengthTunability.setStatus("mandatory")


class _XfpWaveLengthTunable_Type(Integer32):
    """Custom type xfpWaveLengthTunable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Completed", 2),
          ("Doing", 1),
          ("not-support", 3))
    )


_XfpWaveLengthTunable_Type.__name__ = "Integer32"
_XfpWaveLengthTunable_Object = MibTableColumn
xfpWaveLengthTunable = _XfpWaveLengthTunable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 20, 1, 1, 1, 2),
    _XfpWaveLengthTunable_Type()
)
xfpWaveLengthTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfpWaveLengthTunable.setStatus("mandatory")
_XfpWaveLength_Type = Integer32
_XfpWaveLength_Object = MibTableColumn
xfpWaveLength = _XfpWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 20, 1, 1, 1, 3),
    _XfpWaveLength_Type()
)
xfpWaveLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfpWaveLength.setStatus("mandatory")


class _XfpTunableType_Type(Integer32):
    """Custom type xfpTunableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("channel", 1),
          ("not-support", 3),
          ("wavelength", 2))
    )


_XfpTunableType_Type.__name__ = "Integer32"
_XfpTunableType_Object = MibTableColumn
xfpTunableType = _XfpTunableType_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 2, 20, 1, 1, 1, 4),
    _XfpTunableType_Type()
)
xfpTunableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfpTunableType.setStatus("mandatory")
_McPmObjects_ObjectIdentity = ObjectIdentity
mcPmObjects = _McPmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 3)
)
_McPmTable_Object = MibTable
mcPmTable = _McPmTable_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mcPmTable.setStatus("current")
_McPmEntry_Object = MibTableRow
mcPmEntry = _McPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 3, 1, 1)
)
mcPmEntry.setIndexNames(
    (0, "XXX-MIB", "mcShelfIdx"),
    (0, "XXX-MIB", "mcCardIdx"),
)
if mibBuilder.loadTexts:
    mcPmEntry.setStatus("current")
_McRxByteHi_Type = Counter32
_McRxByteHi_Object = MibTableColumn
mcRxByteHi = _McRxByteHi_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 3, 1, 1, 1),
    _McRxByteHi_Type()
)
mcRxByteHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRxByteHi.setStatus("current")
_McRxByteLo_Type = Counter32
_McRxByteLo_Object = MibTableColumn
mcRxByteLo = _McRxByteLo_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 3, 1, 1, 2),
    _McRxByteLo_Type()
)
mcRxByteLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcRxByteLo.setStatus("current")
_McTxByteHi_Type = Counter32
_McTxByteHi_Object = MibTableColumn
mcTxByteHi = _McTxByteHi_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 3, 1, 1, 3),
    _McTxByteHi_Type()
)
mcTxByteHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTxByteHi.setStatus("current")
_McTxByteLo_Type = Counter32
_McTxByteLo_Object = MibTableColumn
mcTxByteLo = _McTxByteLo_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 3, 1, 1, 4),
    _McTxByteLo_Type()
)
mcTxByteLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTxByteLo.setStatus("current")


class _McPmRest_Type(Integer32):
    """Custom type mcPmRest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("not-support", 3),
          ("reset", 2))
    )


_McPmRest_Type.__name__ = "Integer32"
_McPmRest_Object = MibTableColumn
mcPmRest = _McPmRest_Object(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 1, 4, 3, 1, 1, 5),
    _McPmRest_Type()
)
mcPmRest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcPmRest.setStatus("current")
_AlarmMIB_ObjectIdentity = ObjectIdentity
alarmMIB = _AlarmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2)
)

# Managed Objects groups


# Notification objects

shelf_Detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 1)
)
shelf_Detected.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_Detected.setStatus(
        "current"
    )

shelf_Lost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 2)
)
shelf_Lost.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_Lost.setStatus(
        "current"
    )

shelf_psuA_On = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 3)
)
shelf_psuA_On.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_psuA_On.setStatus(
        "current"
    )

shelf_psuA_Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 4)
)
shelf_psuA_Off.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_psuA_Off.setStatus(
        "current"
    )

shelf_psuB_On = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 5)
)
shelf_psuB_On.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_psuB_On.setStatus(
        "current"
    )

shelf_psuB_Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 6)
)
shelf_psuB_Off.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_psuB_Off.setStatus(
        "current"
    )

shelf_fan_On = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 7)
)
shelf_fan_On.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_fan_On.setStatus(
        "current"
    )

shelf_fan_Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 8)
)
shelf_fan_Off.setObjects(
    ("XXX-MIB", "shelfIdx")
)
if mibBuilder.loadTexts:
    shelf_fan_Off.setStatus(
        "current"
    )

card_Detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 20)
)
card_Detected.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_Detected.setStatus(
        "current"
    )

card_Lost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 21)
)
card_Lost.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_Lost.setStatus(
        "current"
    )

card_MC_Co_Tx_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 30)
)
card_MC_Co_Tx_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Tx_Up.setStatus(
        "current"
    )

card_MC_Co_Tx_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 31)
)
card_MC_Co_Tx_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Tx_Down.setStatus(
        "current"
    )

card_MC_Co_Fx_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 32)
)
card_MC_Co_Fx_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Fx_Up.setStatus(
        "current"
    )

card_MC_Co_Fx_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 33)
)
card_MC_Co_Fx_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Fx_Down.setStatus(
        "current"
    )

card_MC_Rmt_Tx_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 34)
)
card_MC_Rmt_Tx_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_Tx_Up.setStatus(
        "current"
    )

card_MC_Rmt_Tx_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 35)
)
card_MC_Rmt_Tx_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_Tx_Down.setStatus(
        "current"
    )

card_MC_Rmt_PwrDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 36)
)
card_MC_Rmt_PwrDown.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_PwrDown.setStatus(
        "current"
    )

card_MC_Co_Ntw_SFP_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 37)
)
card_MC_Co_Ntw_SFP_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Ntw_SFP_Inserted.setStatus(
        "current"
    )

card_MC_Co_Ntw_SFP_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 38)
)
card_MC_Co_Ntw_SFP_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Ntw_SFP_Removed.setStatus(
        "current"
    )

card_MC_Co_Acc_SFP_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 39)
)
card_MC_Co_Acc_SFP_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Acc_SFP_Inserted.setStatus(
        "current"
    )

card_MC_Co_Acc_SFP_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 40)
)
card_MC_Co_Acc_SFP_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Acc_SFP_Removed.setStatus(
        "current"
    )

card_MC_Rmt_Acc_SFP_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 41)
)
card_MC_Rmt_Acc_SFP_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_Acc_SFP_Inserted.setStatus(
        "current"
    )

card_MC_Rmt_Acc_SFP_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 42)
)
card_MC_Rmt_Acc_SFP_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_Acc_SFP_Removed.setStatus(
        "current"
    )

card_MC_Co_Tx_Up1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 43)
)
card_MC_Co_Tx_Up1.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Tx_Up1.setStatus(
        "current"
    )

card_MC_Co_Tx_Down1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 44)
)
card_MC_Co_Tx_Down1.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Tx_Down1.setStatus(
        "current"
    )

card_MC_Co_Tx_Up2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 45)
)
card_MC_Co_Tx_Up2.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Tx_Up2.setStatus(
        "current"
    )

card_MC_Co_Tx_Down2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 46)
)
card_MC_Co_Tx_Down2.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Tx_Down2.setStatus(
        "current"
    )

card_MC_Rmt_Tx_Up1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 47)
)
card_MC_Rmt_Tx_Up1.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_Tx_Up1.setStatus(
        "current"
    )

card_MC_Rmt_Tx_Down1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 48)
)
card_MC_Rmt_Tx_Down1.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_Tx_Down1.setStatus(
        "current"
    )

card_MC_Rmt_Tx_Up2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 49)
)
card_MC_Rmt_Tx_Up2.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_Tx_Up2.setStatus(
        "current"
    )

card_MC_Rmt_Tx_Down2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 50)
)
card_MC_Rmt_Tx_Down2.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_Tx_Down2.setStatus(
        "current"
    )

card_MC_Co_SFP1_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 51)
)
card_MC_Co_SFP1_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFP1_Inserted.setStatus(
        "current"
    )

card_MC_Co_SFP1_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 52)
)
card_MC_Co_SFP1_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFP1_Removed.setStatus(
        "current"
    )

card_MC_Co_SFP2_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 53)
)
card_MC_Co_SFP2_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFP2_Inserted.setStatus(
        "current"
    )

card_MC_Co_SFP2_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 54)
)
card_MC_Co_SFP2_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFP2_Removed.setStatus(
        "current"
    )

card_MC_Co_SFP1_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 55)
)
card_MC_Co_SFP1_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFP1_Up.setStatus(
        "current"
    )

card_MC_Co_SFP1_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 56)
)
card_MC_Co_SFP1_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFP1_Down.setStatus(
        "current"
    )

card_MC_Co_SFP2_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 57)
)
card_MC_Co_SFP2_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFP2_Up.setStatus(
        "current"
    )

card_MC_Co_SFP2_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 58)
)
card_MC_Co_SFP2_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFP2_Down.setStatus(
        "current"
    )

card_MC_Rmt_SFP1_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 59)
)
card_MC_Rmt_SFP1_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFP1_Inserted.setStatus(
        "current"
    )

card_MC_Rmt_SFP1_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 60)
)
card_MC_Rmt_SFP1_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFP1_Removed.setStatus(
        "current"
    )

card_MC_Rmt_SFP1_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 61)
)
card_MC_Rmt_SFP1_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFP1_Up.setStatus(
        "current"
    )

card_MC_Rmt_SFP1_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 62)
)
card_MC_Rmt_SFP1_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFP1_Down.setStatus(
        "current"
    )

card_MC_Co_SFPSFP1_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 63)
)
card_MC_Co_SFPSFP1_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFPSFP1_Inserted.setStatus(
        "current"
    )

card_MC_Co_SFPSFP1_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 64)
)
card_MC_Co_SFPSFP1_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFPSFP1_Removed.setStatus(
        "current"
    )

card_MC_Co_SFPSFP2_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 65)
)
card_MC_Co_SFPSFP2_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFPSFP2_Inserted.setStatus(
        "current"
    )

card_MC_Co_SFPSFP2_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 66)
)
card_MC_Co_SFPSFP2_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFPSFP2_Removed.setStatus(
        "current"
    )

card_MC_Rmt_SFPSFP1_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 67)
)
card_MC_Rmt_SFPSFP1_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFPSFP1_Inserted.setStatus(
        "current"
    )

card_MC_Rmt_SFPSFP1_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 68)
)
card_MC_Rmt_SFPSFP1_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFPSFP1_Removed.setStatus(
        "current"
    )

card_MC_Co_XFP1_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 69)
)
card_MC_Co_XFP1_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_XFP1_Inserted.setStatus(
        "current"
    )

card_MC_Co_XFP1_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 70)
)
card_MC_Co_XFP1_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_XFP1_Removed.setStatus(
        "current"
    )

card_MC_Co_XFP2_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 71)
)
card_MC_Co_XFP2_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_XFP2_Inserted.setStatus(
        "current"
    )

card_MC_Co_XFP2_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 72)
)
card_MC_Co_XFP2_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_XFP2_Removed.setStatus(
        "current"
    )

card_MC_Rmt_XFP1_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 73)
)
card_MC_Rmt_XFP1_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_XFP1_Inserted.setStatus(
        "current"
    )

card_MC_Rmt_XFP1_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 74)
)
card_MC_Rmt_XFP1_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_XFP1_Removed.setStatus(
        "current"
    )

card_MC_Co_SFPSFP1_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 75)
)
card_MC_Co_SFPSFP1_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFPSFP1_Up.setStatus(
        "current"
    )

card_MC_Co_SFPSFP1_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 76)
)
card_MC_Co_SFPSFP1_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFPSFP1_Down.setStatus(
        "current"
    )

card_MC_Co_SFPSFP2_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 77)
)
card_MC_Co_SFPSFP2_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFPSFP2_Up.setStatus(
        "current"
    )

card_MC_Co_SFPSFP2_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 78)
)
card_MC_Co_SFPSFP2_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFPSFP2_Down.setStatus(
        "current"
    )

card_MC_Rmt_SFPSFP1_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 79)
)
card_MC_Rmt_SFPSFP1_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFPSFP1_Up.setStatus(
        "current"
    )

card_MC_Rmt_SFPSFP1_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 80)
)
card_MC_Rmt_SFPSFP1_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFPSFP1_Down.setStatus(
        "current"
    )

card_MC_Co_XFP1_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 81)
)
card_MC_Co_XFP1_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_XFP1_Up.setStatus(
        "current"
    )

card_MC_Co_XFP1_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 82)
)
card_MC_Co_XFP1_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_XFP1_Down.setStatus(
        "current"
    )

card_MC_Co_XFP2_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 83)
)
card_MC_Co_XFP2_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_XFP2_Up.setStatus(
        "current"
    )

card_MC_Co_XFP2_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 84)
)
card_MC_Co_XFP2_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_XFP2_Down.setStatus(
        "current"
    )

card_MC_Rmt_XFP1_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 85)
)
card_MC_Rmt_XFP1_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_XFP1_Up.setStatus(
        "current"
    )

card_MC_Rmt_XFP1_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 86)
)
card_MC_Rmt_XFP1_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_XFP1_Down.setStatus(
        "current"
    )

card_MC_Co_SFP3_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 87)
)
card_MC_Co_SFP3_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFP3_Inserted.setStatus(
        "current"
    )

card_MC_Co_SFP3_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 88)
)
card_MC_Co_SFP3_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFP3_Removed.setStatus(
        "current"
    )

card_MC_Co_Port1_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 89)
)
card_MC_Co_Port1_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Port1_Up.setStatus(
        "current"
    )

card_MC_Co_Port1_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 90)
)
card_MC_Co_Port1_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Port1_Down.setStatus(
        "current"
    )

card_MC_Co_Port2_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 91)
)
card_MC_Co_Port2_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Port2_Up.setStatus(
        "current"
    )

card_MC_Co_Port2_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 92)
)
card_MC_Co_Port2_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Port2_Down.setStatus(
        "current"
    )

card_MC_Co_Port3_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 93)
)
card_MC_Co_Port3_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Port3_Up.setStatus(
        "current"
    )

card_MC_Co_Port3_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 94)
)
card_MC_Co_Port3_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_Port3_Down.setStatus(
        "current"
    )

card_MC_FAN_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 100)
)
card_MC_FAN_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_FAN_Normal.setStatus(
        "current"
    )

card_MC_FAN_Abnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 101)
)
card_MC_FAN_Abnormal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_FAN_Abnormal.setStatus(
        "current"
    )

card_MC_Co_QSFP1_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 102)
)
card_MC_Co_QSFP1_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP1_Inserted.setStatus(
        "current"
    )

card_MC_Co_QSFP1_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 103)
)
card_MC_Co_QSFP1_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP1_Removed.setStatus(
        "current"
    )

card_MC_Co_QSFP2_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 104)
)
card_MC_Co_QSFP2_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP2_Inserted.setStatus(
        "current"
    )

card_MC_Co_QSFP2_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 105)
)
card_MC_Co_QSFP2_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP2_Removed.setStatus(
        "current"
    )

card_MC_Co_QSFP1_Lane1_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 106)
)
card_MC_Co_QSFP1_Lane1_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP1_Lane1_Up.setStatus(
        "current"
    )

card_MC_Co_QSFP1_Lane1_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 107)
)
card_MC_Co_QSFP1_Lane1_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP1_Lane1_Down.setStatus(
        "current"
    )

card_MC_Co_QSFP1_Lane2_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 108)
)
card_MC_Co_QSFP1_Lane2_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP1_Lane2_Up.setStatus(
        "current"
    )

card_MC_Co_QSFP1_Lane2_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 109)
)
card_MC_Co_QSFP1_Lane2_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP1_Lane2_Down.setStatus(
        "current"
    )

card_MC_Co_QSFP1_Lane3_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 110)
)
card_MC_Co_QSFP1_Lane3_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP1_Lane3_Up.setStatus(
        "current"
    )

card_MC_Co_QSFP1_Lane3_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 111)
)
card_MC_Co_QSFP1_Lane3_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP1_Lane3_Down.setStatus(
        "current"
    )

card_MC_Co_QSFP1_Lane4_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 112)
)
card_MC_Co_QSFP1_Lane4_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP1_Lane4_Up.setStatus(
        "current"
    )

card_MC_Co_QSFP1_Lane4_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 113)
)
card_MC_Co_QSFP1_Lane4_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP1_Lane4_Down.setStatus(
        "current"
    )

card_MC_Co_QSFP2_Lane1_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 114)
)
card_MC_Co_QSFP2_Lane1_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP2_Lane1_Up.setStatus(
        "current"
    )

card_MC_Co_QSFP2_Lane1_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 115)
)
card_MC_Co_QSFP2_Lane1_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP2_Lane1_Down.setStatus(
        "current"
    )

card_MC_Co_QSFP2_Lane2_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 116)
)
card_MC_Co_QSFP2_Lane2_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP2_Lane2_Up.setStatus(
        "current"
    )

card_MC_Co_QSFP2_Lane2_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 117)
)
card_MC_Co_QSFP2_Lane2_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP2_Lane2_Down.setStatus(
        "current"
    )

card_MC_Co_QSFP2_Lane3_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 118)
)
card_MC_Co_QSFP2_Lane3_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP2_Lane3_Up.setStatus(
        "current"
    )

card_MC_Co_QSFP2_Lane3_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 119)
)
card_MC_Co_QSFP2_Lane3_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP2_Lane3_Down.setStatus(
        "current"
    )

card_MC_Co_QSFP2_Lane4_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 120)
)
card_MC_Co_QSFP2_Lane4_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP2_Lane4_Up.setStatus(
        "current"
    )

card_MC_Co_QSFP2_Lane4_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 121)
)
card_MC_Co_QSFP2_Lane4_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_QSFP2_Lane4_Down.setStatus(
        "current"
    )

card_MC_Rmt_SFP2_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 122)
)
card_MC_Rmt_SFP2_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFP2_Inserted.setStatus(
        "current"
    )

card_MC_Rmt_SFP2_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 123)
)
card_MC_Rmt_SFP2_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFP2_Removed.setStatus(
        "current"
    )

card_MC_Rmt_SFP3_Inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 124)
)
card_MC_Rmt_SFP3_Inserted.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFP3_Inserted.setStatus(
        "current"
    )

card_MC_Rmt_SFP3_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 125)
)
card_MC_Rmt_SFP3_Removed.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFP3_Removed.setStatus(
        "current"
    )

card_MC_Rmt_SFP2_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 126)
)
card_MC_Rmt_SFP2_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFP2_Up.setStatus(
        "current"
    )

card_MC_Rmt_SFP2_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 127)
)
card_MC_Rmt_SFP2_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFP2_Down.setStatus(
        "current"
    )

card_MC_Rmt_SFP3_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 128)
)
card_MC_Rmt_SFP3_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFP3_Up.setStatus(
        "current"
    )

card_MC_Rmt_SFP3_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 129)
)
card_MC_Rmt_SFP3_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Rmt_SFP3_Down.setStatus(
        "current"
    )

card_MC_E1_Co_Port1_LOS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 130)
)
card_MC_E1_Co_Port1_LOS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Co_Port1_LOS_Alarm.setStatus(
        "current"
    )

card_MC_E1_Co_Port1_LOS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 131)
)
card_MC_E1_Co_Port1_LOS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Co_Port1_LOS_Normal.setStatus(
        "current"
    )

card_MC_E1_Co_Port1_AIS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 132)
)
card_MC_E1_Co_Port1_AIS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Co_Port1_AIS_Alarm.setStatus(
        "current"
    )

card_MC_E1_Co_Port1_AIS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 133)
)
card_MC_E1_Co_Port1_AIS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Co_Port1_AIS_Normal.setStatus(
        "current"
    )

card_MC_E1_Co_Port1_CV_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 134)
)
card_MC_E1_Co_Port1_CV_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Co_Port1_CV_Alarm.setStatus(
        "current"
    )

card_MC_E1_Co_Port1_CV_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 135)
)
card_MC_E1_Co_Port1_CV_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Co_Port1_CV_Normal.setStatus(
        "current"
    )

card_MC_E1_Co_Port2_LOS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 136)
)
card_MC_E1_Co_Port2_LOS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Co_Port2_LOS_Alarm.setStatus(
        "current"
    )

card_MC_E1_Co_Port2_LOS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 137)
)
card_MC_E1_Co_Port2_LOS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Co_Port2_LOS_Normal.setStatus(
        "current"
    )

card_MC_E1_Co_Port2_AIS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 138)
)
card_MC_E1_Co_Port2_AIS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Co_Port2_AIS_Alarm.setStatus(
        "current"
    )

card_MC_E1_Co_Port2_AIS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 139)
)
card_MC_E1_Co_Port2_AIS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Co_Port2_AIS_Normal.setStatus(
        "current"
    )

card_MC_E1_Co_Port2_CV_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 140)
)
card_MC_E1_Co_Port2_CV_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Co_Port2_CV_Alarm.setStatus(
        "current"
    )

card_MC_E1_Co_Port2_CV_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 141)
)
card_MC_E1_Co_Port2_CV_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Co_Port2_CV_Normal.setStatus(
        "current"
    )

card_MC_E1_Rmt_Port1_LOS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 142)
)
card_MC_E1_Rmt_Port1_LOS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Rmt_Port1_LOS_Alarm.setStatus(
        "current"
    )

card_MC_E1_Rmt_Port1_LOS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 143)
)
card_MC_E1_Rmt_Port1_LOS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Rmt_Port1_LOS_Normal.setStatus(
        "current"
    )

card_MC_E1_Rmt_Port1_AIS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 144)
)
card_MC_E1_Rmt_Port1_AIS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Rmt_Port1_AIS_Alarm.setStatus(
        "current"
    )

card_MC_E1_Rmt_Port1_AIS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 145)
)
card_MC_E1_Rmt_Port1_AIS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Rmt_Port1_AIS_Normal.setStatus(
        "current"
    )

card_MC_E1_Rmt_Port1_CV_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 146)
)
card_MC_E1_Rmt_Port1_CV_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Rmt_Port1_CV_Alarm.setStatus(
        "current"
    )

card_MC_E1_Rmt_Port1_CV_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 147)
)
card_MC_E1_Rmt_Port1_CV_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Rmt_Port1_CV_Normal.setStatus(
        "current"
    )

card_MC_E1_Rmt_Port2_LOS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 148)
)
card_MC_E1_Rmt_Port2_LOS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Rmt_Port2_LOS_Alarm.setStatus(
        "current"
    )

card_MC_E1_Rmt_Port2_LOS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 149)
)
card_MC_E1_Rmt_Port2_LOS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Rmt_Port2_LOS_Normal.setStatus(
        "current"
    )

card_MC_E1_Rmt_Port2_AIS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 150)
)
card_MC_E1_Rmt_Port2_AIS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Rmt_Port2_AIS_Alarm.setStatus(
        "current"
    )

card_MC_E1_Rmt_Port2_AIS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 151)
)
card_MC_E1_Rmt_Port2_AIS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Rmt_Port2_AIS_Normal.setStatus(
        "current"
    )

card_MC_E1_Rmt_Port2_CV_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 152)
)
card_MC_E1_Rmt_Port2_CV_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Rmt_Port2_CV_Alarm.setStatus(
        "current"
    )

card_MC_E1_Rmt_Port2_CV_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 153)
)
card_MC_E1_Rmt_Port2_CV_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1_Rmt_Port2_CV_Normal.setStatus(
        "current"
    )

card_MC_Co_SFP3_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 154)
)
card_MC_Co_SFP3_Up.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFP3_Up.setStatus(
        "current"
    )

card_MC_Co_SFP3_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 155)
)
card_MC_Co_SFP3_Down.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_Co_SFP3_Down.setStatus(
        "current"
    )

card_MC_E1T1_Co_TXLOS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 156)
)
card_MC_E1T1_Co_TXLOS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1T1_Co_TXLOS_Alarm.setStatus(
        "current"
    )

card_MC_E1T1_Co_TXLOS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 157)
)
card_MC_E1T1_Co_TXLOS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1T1_Co_TXLOS_Normal.setStatus(
        "current"
    )

card_MC_E1T1_Co_FXLOS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 158)
)
card_MC_E1T1_Co_FXLOS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1T1_Co_FXLOS_Alarm.setStatus(
        "current"
    )

card_MC_E1T1_Co_FXLOS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 159)
)
card_MC_E1T1_Co_FXLOS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1T1_Co_FXLOS_Normal.setStatus(
        "current"
    )

card_MC_E1T1_Co_AIS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 160)
)
card_MC_E1T1_Co_AIS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1T1_Co_AIS_Alarm.setStatus(
        "current"
    )

card_MC_E1T1_Co_AIS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 161)
)
card_MC_E1T1_Co_AIS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1T1_Co_AIS_Normal.setStatus(
        "current"
    )

card_MC_E1T1_Rmt_TXLOS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 162)
)
card_MC_E1T1_Rmt_TXLOS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1T1_Rmt_TXLOS_Alarm.setStatus(
        "current"
    )

card_MC_E1T1_Rmt_TXLOS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 163)
)
card_MC_E1T1_Rmt_TXLOS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1T1_Rmt_TXLOS_Normal.setStatus(
        "current"
    )

card_MC_E1T1_Rmt_FXLOS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 164)
)
card_MC_E1T1_Rmt_FXLOS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1T1_Rmt_FXLOS_Alarm.setStatus(
        "current"
    )

card_MC_E1T1_Rmt_FXLOS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 165)
)
card_MC_E1T1_Rmt_FXLOS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1T1_Rmt_FXLOS_Normal.setStatus(
        "current"
    )

card_MC_E1T1_Rmt_AIS_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 166)
)
card_MC_E1T1_Rmt_AIS_Alarm.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1T1_Rmt_AIS_Alarm.setStatus(
        "current"
    )

card_MC_E1T1_Rmt_AIS_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6688, 1, 1, 2, 167)
)
card_MC_E1T1_Rmt_AIS_Normal.setObjects(
      *(("XXX-MIB", "shelfIdx"),
        ("XXX-MIB", "slotIdx"))
)
if mibBuilder.loadTexts:
    card_MC_E1T1_Rmt_AIS_Normal.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XXX-MIB",
    **{"company": company,
       "ipProduct": ipProduct,
       "height2HU": height2HU,
       "systemMIB": systemMIB,
       "shelfNum": shelfNum,
       "shelfTable": shelfTable,
       "shelfEntry": shelfEntry,
       "shelfName": shelfName,
       "psuA": psuA,
       "psuB": psuB,
       "volA": volA,
       "volB": volB,
       "fan": fan,
       "temperature": temperature,
       "coCardNum": coCardNum,
       "rmtCardNum": rmtCardNum,
       "slotObjects": slotObjects,
       "slotTable": slotTable,
       "slotEntry": slotEntry,
       "shelfIdx": shelfIdx,
       "slotIdx": slotIdx,
       "coCardType": coCardType,
       "coCardDesc": coCardDesc,
       "rmtCardType": rmtCardType,
       "rmtCardDesc": rmtCardDesc,
       "cardObjects": cardObjects,
       "nmuObjects": nmuObjects,
       "nmuConfig": nmuConfig,
       "nmuType": nmuType,
       "ipaddr": ipaddr,
       "subnet": subnet,
       "gateway": gateway,
       "sysContact": sysContact,
       "sysName": sysName,
       "sysLocation": sysLocation,
       "trapHost1": trapHost1,
       "trapHost2": trapHost2,
       "trapHost3": trapHost3,
       "trapHost4": trapHost4,
       "mcCmObjects": mcCmObjects,
       "mcCmTable": mcCmTable,
       "mcCmEntry": mcCmEntry,
       "mcShelfIdx": mcShelfIdx,
       "mcCardIdx": mcCardIdx,
       "mcType": mcType,
       "mcTransceiverMode": mcTransceiverMode,
       "mcTransceiverDist": mcTransceiverDist,
       "mcPortState": mcPortState,
       "mcTransmitMode": mcTransmitMode,
       "mcCurWorkMode": mcCurWorkMode,
       "mcCfgWorkMode": mcCfgWorkMode,
       "mcLFPCfg": mcLFPCfg,
       "mcUpStream": mcUpStream,
       "mcDownStream": mcDownStream,
       "mcTxlink": mcTxlink,
       "mcFxlink": mcFxlink,
       "mcHWLFP": mcHWLFP,
       "mcHWTransmitMode": mcHWTransmitMode,
       "mcHWWorkMode": mcHWWorkMode,
       "mcHWRmtCtrlMode": mcHWRmtCtrlMode,
       "mcNtwSfpExist": mcNtwSfpExist,
       "mcAccSfpExist": mcAccSfpExist,
       "mcUtility": mcUtility,
       "mcRmtDetect": mcRmtDetect,
       "mcRmtType": mcRmtType,
       "mcRmtTransmitMode": mcRmtTransmitMode,
       "mcRmtCurWorkMode": mcRmtCurWorkMode,
       "mcRmtCfgWorkMode": mcRmtCfgWorkMode,
       "mcRmtLFP": mcRmtLFP,
       "mcRmtTxlink": mcRmtTxlink,
       "mcRmtHWLFP": mcRmtHWLFP,
       "mcRmtHWTransmitMode": mcRmtHWTransmitMode,
       "mcRmtHWWorkMode": mcRmtHWWorkMode,
       "mcRmtLoopback": mcRmtLoopback,
       "mcRmtPwrDown": mcRmtPwrDown,
       "mcRmtAccSfpExist": mcRmtAccSfpExist,
       "mcRmtUtility": mcRmtUtility,
       "mcCm1gSpecificObjects": mcCm1gSpecificObjects,
       "mcCm1gIpObjects": mcCm1gIpObjects,
       "mcCm1gIpTable": mcCm1gIpTable,
       "mcCm1gIpEntry": mcCm1gIpEntry,
       "mcLoOrRmtFg": mcLoOrRmtFg,
       "mcIpAddr": mcIpAddr,
       "mcCm1gSfpObjects": mcCm1gSfpObjects,
       "mcCm1gSfpTable": mcCm1gSfpTable,
       "mcCm1gSfpEntry": mcCm1gSfpEntry,
       "getSfpCmd": getSfpCmd,
       "sfpCompliance": sfpCompliance,
       "sfpConnector": sfpConnector,
       "sfpTransCode": sfpTransCode,
       "sfpSmLength": sfpSmLength,
       "sfpMmLength": sfpMmLength,
       "sfpCopperLength": sfpCopperLength,
       "sfpBrSpeed": sfpBrSpeed,
       "sfpWavelength": sfpWavelength,
       "sfpTemperature": sfpTemperature,
       "sfpTranPower": sfpTranPower,
       "sfpRecvPower": sfpRecvPower,
       "sfpVoltage": sfpVoltage,
       "mcCm1gAccSfpObjects": mcCm1gAccSfpObjects,
       "mcCm1gAccSfpTable": mcCm1gAccSfpTable,
       "mcCm1gAccSfpEntry": mcCm1gAccSfpEntry,
       "getAccSfpCmd": getAccSfpCmd,
       "accsfpCompliance": accsfpCompliance,
       "accsfpConnector": accsfpConnector,
       "accsfpTransCode": accsfpTransCode,
       "accsfpSmLength": accsfpSmLength,
       "accsfpMmLength": accsfpMmLength,
       "accsfpCopperLength": accsfpCopperLength,
       "accsfpBrSpeed": accsfpBrSpeed,
       "accsfpWavelength": accsfpWavelength,
       "accsfpTemperature": accsfpTemperature,
       "accsfpTranPower": accsfpTranPower,
       "accsfpRecvPower": accsfpRecvPower,
       "accsfpVoltage": accsfpVoltage,
       "mcIP175DObjects": mcIP175DObjects,
       "mcIP175DCardObjects": mcIP175DCardObjects,
       "mcIP175DCardTable": mcIP175DCardTable,
       "mcIP175DCardEntry": mcIP175DCardEntry,
       "mcIP175DVlanMode": mcIP175DVlanMode,
       "mcIP175DPortObjects": mcIP175DPortObjects,
       "mcIP175DPortTable": mcIP175DPortTable,
       "mcIP175DPortEntry": mcIP175DPortEntry,
       "mcIP175DPortIdx": mcIP175DPortIdx,
       "mcIP175DCurWorkMode": mcIP175DCurWorkMode,
       "mcIP175DCfgWorkMode": mcIP175DCfgWorkMode,
       "mcIP175DUpStream": mcIP175DUpStream,
       "mcIP175DDownStream": mcIP175DDownStream,
       "mcIP175DTxlink": mcIP175DTxlink,
       "mcIP175DRmtCurWorkMode": mcIP175DRmtCurWorkMode,
       "mcIP175DRmtCfgWorkMode": mcIP175DRmtCfgWorkMode,
       "mcIP175DRmtTxlink": mcIP175DRmtTxlink,
       "mc4-25G-OEOObjects": mc4_25G_OEOObjects,
       "mc4-25G-OEOCardObjects": mc4_25G_OEOCardObjects,
       "mc4-25G-OEOCardTable": mc4_25G_OEOCardTable,
       "mc4-25G-OEOCardEntry": mc4_25G_OEOCardEntry,
       "mc4-25G-OEOCurSpdMode": mc4_25G_OEOCurSpdMode,
       "mc4-25G-OEOCfgSpdMode": mc4_25G_OEOCfgSpdMode,
       "mc4-25G-OEOLoopback": mc4_25G_OEOLoopback,
       "mc4-25G-OEOWorkMode": mc4_25G_OEOWorkMode,
       "mc4-25G-OEONtwPD": mc4_25G_OEONtwPD,
       "mc4-25G-OEOAccPD": mc4_25G_OEOAccPD,
       "mc4-25G-OEOHWSpdMode": mc4_25G_OEOHWSpdMode,
       "mc4-25G-OEOHWLoopback": mc4_25G_OEOHWLoopback,
       "mc4-25G-OEOHWWorkMode": mc4_25G_OEOHWWorkMode,
       "mc4-25G-OEO-Test-Lock": mc4_25G_OEO_Test_Lock,
       "mc4-25G-OEO-Test-Error-Counter": mc4_25G_OEO_Test_Error_Counter,
       "mc4-25G-OEO-Test-Continue-Time": mc4_25G_OEO_Test_Continue_Time,
       "mc4-25G-OEO-Test-Result": mc4_25G_OEO_Test_Result,
       "mc4-25G-OEO-Start-Test": mc4_25G_OEO_Start_Test,
       "mc4-25G-OEO-Get-Test-Rst": mc4_25G_OEO_Get_Test_Rst,
       "mcRmt4-25G-OEOCurSpdMode": mcRmt4_25G_OEOCurSpdMode,
       "mcRmt4-25G-OEOCfgSpdMode": mcRmt4_25G_OEOCfgSpdMode,
       "mcRmt4-25G-OEOLoopback": mcRmt4_25G_OEOLoopback,
       "mcRmt4-25G-OEOWorkMode": mcRmt4_25G_OEOWorkMode,
       "mcRmt4-25G-OEOHWSpdMode": mcRmt4_25G_OEOHWSpdMode,
       "mcRmt4-25G-OEOHWLoopback": mcRmt4_25G_OEOHWLoopback,
       "mcRmt4-25G-OEOHWWorkMode": mcRmt4_25G_OEOHWWorkMode,
       "mc10G-OEOObjects": mc10G_OEOObjects,
       "mc10G-OEOCardObjects": mc10G_OEOCardObjects,
       "mc10G-OEOCardTable": mc10G_OEOCardTable,
       "mc10G-OEOCardEntry": mc10G_OEOCardEntry,
       "mc10G-OEOCurSpdMode": mc10G_OEOCurSpdMode,
       "mc10G-OEOCfgSpdMode": mc10G_OEOCfgSpdMode,
       "mc10G-OEOLoopback": mc10G_OEOLoopback,
       "mc10G-OEOSFP1": mc10G_OEOSFP1,
       "mc10G-OEOSFP2": mc10G_OEOSFP2,
       "mc10G-OEOHWSpdMode": mc10G_OEOHWSpdMode,
       "mc10G-OEOHWLoopback": mc10G_OEOHWLoopback,
       "mc10G-OEO-Test-Lock": mc10G_OEO_Test_Lock,
       "mc10G-OEO-Test-Error-Counter": mc10G_OEO_Test_Error_Counter,
       "mc10G-OEO-Test-Continue-Time": mc10G_OEO_Test_Continue_Time,
       "mc10G-OEO-Test-Result": mc10G_OEO_Test_Result,
       "mc10G-OEO-Start-Test": mc10G_OEO_Start_Test,
       "mc10G-OEO-Get-Test-Rst": mc10G_OEO_Get_Test_Rst,
       "mcRmt10G-OEOCurSpdMode": mcRmt10G_OEOCurSpdMode,
       "mcRmt10G-OEOCfgSpdMode": mcRmt10G_OEOCfgSpdMode,
       "mcRmt10G-OEOLoopback": mcRmt10G_OEOLoopback,
       "mcRmt10G-OEOHWSpdMode": mcRmt10G_OEOHWSpdMode,
       "mcRmt10G-OEOHWLoopback": mcRmt10G_OEOHWLoopback,
       "mcRmt10G-OEOSFP1": mcRmt10G_OEOSFP1,
       "mc10G-OEO-accType": mc10G_OEO_accType,
       "mc10G-OEO-ntwType": mc10G_OEO_ntwType,
       "mcRmt10G-OEO-accType": mcRmt10G_OEO_accType,
       "mcRmt10G-OEO-ntwType": mcRmt10G_OEO_ntwType,
       "mc10G-OEEObjects": mc10G_OEEObjects,
       "mc10G-OEECardObjects": mc10G_OEECardObjects,
       "mc10G-OEECardTable": mc10G_OEECardTable,
       "mc10G-OEECardEntry": mc10G_OEECardEntry,
       "mc10G-OEETxlink": mc10G_OEETxlink,
       "mc10G-OEEFxlink": mc10G_OEEFxlink,
       "mc10G-OEECurSpd": mc10G_OEECurSpd,
       "mc10G-OEELoopMode": mc10G_OEELoopMode,
       "mc10G-OEESpdMode": mc10G_OEESpdMode,
       "mc10G-OEEHWLoopback": mc10G_OEEHWLoopback,
       "mc10G-OEE-ntwType": mc10G_OEE_ntwType,
       "mc10G-OEE-checkResult": mc10G_OEE_checkResult,
       "mcFanObjects": mcFanObjects,
       "mcFanCardObjects": mcFanCardObjects,
       "mcFanCardTable": mcFanCardTable,
       "mcFanCardEntry": mcFanCardEntry,
       "mcFanStatus": mcFanStatus,
       "mc40G-OEOObjects": mc40G_OEOObjects,
       "mc40G-OEOCardObjects": mc40G_OEOCardObjects,
       "mc40G-OEOCardTable": mc40G_OEOCardTable,
       "mc40G-OEOCardEntry": mc40G_OEOCardEntry,
       "mc40G-OEOQsfp1Lane1-link": mc40G_OEOQsfp1Lane1_link,
       "mc40G-OEOQsfp1Lane2-link": mc40G_OEOQsfp1Lane2_link,
       "mc40G-OEOQsfp1Lane3-link": mc40G_OEOQsfp1Lane3_link,
       "mc40G-OEOQsfp1Lane4-link": mc40G_OEOQsfp1Lane4_link,
       "mc40G-OEOQsfp2Lane1-link": mc40G_OEOQsfp2Lane1_link,
       "mc40G-OEOQsfp2Lane2-link": mc40G_OEOQsfp2Lane2_link,
       "mc40G-OEOQsfp2Lane3-link": mc40G_OEOQsfp2Lane3_link,
       "mc40G-OEOQsfp2Lane4-link": mc40G_OEOQsfp2Lane4_link,
       "mc40G-OEOLane1LoopMode": mc40G_OEOLane1LoopMode,
       "mc40G-OEOLane2LoopMode": mc40G_OEOLane2LoopMode,
       "mc40G-OEOLane3LoopMode": mc40G_OEOLane3LoopMode,
       "mc40G-OEOLane4LoopMode": mc40G_OEOLane4LoopMode,
       "mc40G-OEOLoopMode": mc40G_OEOLoopMode,
       "mc40G-OEOSpeedMode": mc40G_OEOSpeedMode,
       "mc40G-OEOHWLoopMode": mc40G_OEOHWLoopMode,
       "mc40G-OEOHWSpeedMode": mc40G_OEOHWSpeedMode,
       "mcQsfpSpecificObjects": mcQsfpSpecificObjects,
       "mcNtwQSfpObjects": mcNtwQSfpObjects,
       "mcNtwQSfpTable": mcNtwQSfpTable,
       "mcNtwQSfpEntry": mcNtwQSfpEntry,
       "getNtwQSfpCmd": getNtwQSfpCmd,
       "qsfpNtwConnector": qsfpNtwConnector,
       "qsfpNtwTemperature": qsfpNtwTemperature,
       "qsfpNtwTxPower1": qsfpNtwTxPower1,
       "qsfpNtwTxPower2": qsfpNtwTxPower2,
       "qsfpNtwTxPower3": qsfpNtwTxPower3,
       "qsfpNtwTxPower4": qsfpNtwTxPower4,
       "qsfpNtwRxPower1": qsfpNtwRxPower1,
       "qsfpNtwRxPower2": qsfpNtwRxPower2,
       "qsfpNtwRxPower3": qsfpNtwRxPower3,
       "qsfpNtwRxPower4": qsfpNtwRxPower4,
       "mcAccQSfpObjects": mcAccQSfpObjects,
       "mcAccQSfpTable": mcAccQSfpTable,
       "mcAccQSfpEntry": mcAccQSfpEntry,
       "getAccQSfpCmd": getAccQSfpCmd,
       "qsfpAccConnector": qsfpAccConnector,
       "qsfpAccTemperature": qsfpAccTemperature,
       "qsfpAccTxPower1": qsfpAccTxPower1,
       "qsfpAccTxPower2": qsfpAccTxPower2,
       "qsfpAccTxPower3": qsfpAccTxPower3,
       "qsfpAccTxPower4": qsfpAccTxPower4,
       "qsfpAccRxPower1": qsfpAccRxPower1,
       "qsfpAccRxPower2": qsfpAccRxPower2,
       "qsfpAccRxPower3": qsfpAccRxPower3,
       "qsfpAccRxPower4": qsfpAccRxPower4,
       "mc2-5GMCObjects": mc2_5GMCObjects,
       "mc2-5GMCSFP3Objects": mc2_5GMCSFP3Objects,
       "mc2-5Cm1gSfpTable": mc2_5Cm1gSfpTable,
       "mc2-5Cm1gSfpEntry": mc2_5Cm1gSfpEntry,
       "mc2-5g-getSfpCmd": mc2_5g_getSfpCmd,
       "mc2-5g-sfpCompliance": mc2_5g_sfpCompliance,
       "mc2-5g-sfpConnector": mc2_5g_sfpConnector,
       "mc2-5g-sfpTransCode": mc2_5g_sfpTransCode,
       "mc2-5g-sfpSmLength": mc2_5g_sfpSmLength,
       "mc2-5g-sfpMmLength": mc2_5g_sfpMmLength,
       "mc2-5g-sfpCopperLength": mc2_5g_sfpCopperLength,
       "mc2-5g-sfpBrSpeed": mc2_5g_sfpBrSpeed,
       "mc2-5g-sfpWavelength": mc2_5g_sfpWavelength,
       "mc2-5g-sfpTemperature": mc2_5g_sfpTemperature,
       "mc2-5g-sfpTranPower": mc2_5g_sfpTranPower,
       "mc2-5g-sfpRecvPower": mc2_5g_sfpRecvPower,
       "mc2-5g-sfpVoltage": mc2_5g_sfpVoltage,
       "mc2-5GMCCardObjects": mc2_5GMCCardObjects,
       "mc2-5GMCCardTable": mc2_5GMCCardTable,
       "mc2-5GMCCardEntry": mc2_5GMCCardEntry,
       "mc2-5GMCSfp3Exist": mc2_5GMCSfp3Exist,
       "mc2-5GMCPort1link": mc2_5GMCPort1link,
       "mc2-5GMCPort2link": mc2_5GMCPort2link,
       "mc2-5GMCPort3link": mc2_5GMCPort3link,
       "mcE1Objects": mcE1Objects,
       "mcE1CardObjects": mcE1CardObjects,
       "mcE1CardTable": mcE1CardTable,
       "mcE1CardEntry": mcE1CardEntry,
       "mcE1Txlink": mcE1Txlink,
       "mcE1TxCurWorkMode": mcE1TxCurWorkMode,
       "mcE1SFP1Link": mcE1SFP1Link,
       "mcE1Port1LOS": mcE1Port1LOS,
       "mcE1Port1AIS": mcE1Port1AIS,
       "mcE1Port1CV": mcE1Port1CV,
       "mcE1Port2LOS": mcE1Port2LOS,
       "mcE1Port2AIS": mcE1Port2AIS,
       "mcE1Port2CV": mcE1Port2CV,
       "mcE1Port1Loop": mcE1Port1Loop,
       "mcE1Port2Loop": mcE1Port2Loop,
       "mcRmtE1Txlink": mcRmtE1Txlink,
       "mcRmtE1TxCurWorkMode": mcRmtE1TxCurWorkMode,
       "mcRmtE1SFP1Link": mcRmtE1SFP1Link,
       "mcRmtE1Port1LOS": mcRmtE1Port1LOS,
       "mcRmtE1Port1AIS": mcRmtE1Port1AIS,
       "mcRmtE1Port1CV": mcRmtE1Port1CV,
       "mcRmtE1Port2LOS": mcRmtE1Port2LOS,
       "mcRmtE1Port2AIS": mcRmtE1Port2AIS,
       "mcRmtE1Port2CV": mcRmtE1Port2CV,
       "mcRmtE1Port1Loop": mcRmtE1Port1Loop,
       "mcRmtE1Port2Loop": mcRmtE1Port2Loop,
       "mc1GE2OObjects": mc1GE2OObjects,
       "mc1GE2OCardObjects": mc1GE2OCardObjects,
       "mc1GE2OCardTable": mc1GE2OCardTable,
       "mc1GE2OCardEntry": mc1GE2OCardEntry,
       "mc1GE2OPort1SFPlink": mc1GE2OPort1SFPlink,
       "mc1GE2OPort2SFPlink": mc1GE2OPort2SFPlink,
       "mc1GE2OTxlink": mc1GE2OTxlink,
       "mc1GE2OPortPri": mc1GE2OPortPri,
       "mc1GE2OPort1SFPExist": mc1GE2OPort1SFPExist,
       "mc1GE2OPort2SFPExist": mc1GE2OPort2SFPExist,
       "mc1GE2OPortHWPri": mc1GE2OPortHWPri,
       "mc1GE2ORmtPort1SFPlink": mc1GE2ORmtPort1SFPlink,
       "mc1GE2ORmtPort2SFPlink": mc1GE2ORmtPort2SFPlink,
       "mc1GE2ORmtTxlink": mc1GE2ORmtTxlink,
       "mc1GE2ORmtPort1SFPExist": mc1GE2ORmtPort1SFPExist,
       "mc1GE2ORmtPort2SFPExist": mc1GE2ORmtPort2SFPExist,
       "mc1GE2ORmtPortHWPri": mc1GE2ORmtPortHWPri,
       "mc1GO2OObjects": mc1GO2OObjects,
       "mc1GO2OCardObjects": mc1GO2OCardObjects,
       "mc1GO2OCardTable": mc1GO2OCardTable,
       "mc1GO2OCardEntry": mc1GO2OCardEntry,
       "mc1GO2OPort1SFPlink": mc1GO2OPort1SFPlink,
       "mc1GO2OPort2SFPlink": mc1GO2OPort2SFPlink,
       "mc1GO2OPort3SFPlink": mc1GO2OPort3SFPlink,
       "mc1GO2OPortPri": mc1GO2OPortPri,
       "mc1GO2OPort1SFPExist": mc1GO2OPort1SFPExist,
       "mc1GO2OPort2SFPExist": mc1GO2OPort2SFPExist,
       "mc1GO2OPort3SFPExist": mc1GO2OPort3SFPExist,
       "mc1GO2OPortHWPri": mc1GO2OPortHWPri,
       "mc1GO2OPort3HWSpd": mc1GO2OPort3HWSpd,
       "mc1GO2ORmtPort1SFPlink": mc1GO2ORmtPort1SFPlink,
       "mc1GO2ORmtPort2SFPlink": mc1GO2ORmtPort2SFPlink,
       "mc1GO2ORmtPort3SFPlink": mc1GO2ORmtPort3SFPlink,
       "mc1GO2ORmtPort1SFPExist": mc1GO2ORmtPort1SFPExist,
       "mc1GO2ORmtPort2SFPExist": mc1GO2ORmtPort2SFPExist,
       "mc1GO2ORmtPort3SFPExist": mc1GO2ORmtPort3SFPExist,
       "mc1GO2ORmtPortHWPri": mc1GO2ORmtPortHWPri,
       "mc1GO2ORmtPort3HWSpd": mc1GO2ORmtPort3HWSpd,
       "mc1GO2OSFP3Objects": mc1GO2OSFP3Objects,
       "mc1GO2OSfp3Table": mc1GO2OSfp3Table,
       "mc1GO2OSfp3Entry": mc1GO2OSfp3Entry,
       "mc1go2o-getSfpCmd": mc1go2o_getSfpCmd,
       "mc1go2o-sfpCompliance": mc1go2o_sfpCompliance,
       "mc1go2o-sfpConnector": mc1go2o_sfpConnector,
       "mc1go2o-sfpTransCode": mc1go2o_sfpTransCode,
       "mc1go2o-sfpSmLength": mc1go2o_sfpSmLength,
       "mc1go2o-sfpMmLength": mc1go2o_sfpMmLength,
       "mc1go2o-sfpCopperLength": mc1go2o_sfpCopperLength,
       "mc1go2o-sfpBrSpeed": mc1go2o_sfpBrSpeed,
       "mc1go2o-sfpWavelength": mc1go2o_sfpWavelength,
       "mc1go2o-sfpTemperature": mc1go2o_sfpTemperature,
       "mc1go2o-sfpTranPower": mc1go2o_sfpTranPower,
       "mc1go2o-sfpRecvPower": mc1go2o_sfpRecvPower,
       "mc1go2o-sfpVoltage": mc1go2o_sfpVoltage,
       "mc10GOEO1RObjects": mc10GOEO1RObjects,
       "mc10GOEO1RCardObjects": mc10GOEO1RCardObjects,
       "mc10GOEO1RCardTable": mc10GOEO1RCardTable,
       "mc10GOEO1RCardEntry": mc10GOEO1RCardEntry,
       "mcAccXFP1WaveLengthTunability": mcAccXFP1WaveLengthTunability,
       "mcAccXFP1WaveLengthTunable": mcAccXFP1WaveLengthTunable,
       "mcAccXFP1WaveLength": mcAccXFP1WaveLength,
       "mcNtwXFP2WaveLengthTunability": mcNtwXFP2WaveLengthTunability,
       "mcNtwXFP2WaveLengthTunable": mcNtwXFP2WaveLengthTunable,
       "mcNtwXFP2WaveLength": mcNtwXFP2WaveLength,
       "mcAccXFP1TunableType": mcAccXFP1TunableType,
       "mcNtwXFP2TunableType": mcNtwXFP2TunableType,
       "mc10GOEO3RObjects": mc10GOEO3RObjects,
       "mc10GOEO3RCardObjects": mc10GOEO3RCardObjects,
       "mc10GOEO3RCardTable": mc10GOEO3RCardTable,
       "mc10GOEO3RCardEntry": mc10GOEO3RCardEntry,
       "accXFP1WaveLengthTunability": accXFP1WaveLengthTunability,
       "accXFP1WaveLengthTunable": accXFP1WaveLengthTunable,
       "accXFP1WaveLength": accXFP1WaveLength,
       "ntwXFP2WaveLengthTunability": ntwXFP2WaveLengthTunability,
       "ntwXFP2WaveLengthTunable": ntwXFP2WaveLengthTunable,
       "ntwXFP2WaveLength": ntwXFP2WaveLength,
       "accXFP1TunableType": accXFP1TunableType,
       "ntwXFP2TunableType": ntwXFP2TunableType,
       "mcCWDMObjects": mcCWDMObjects,
       "mcCWDMCardObjects": mcCWDMCardObjects,
       "mcCWDMCardTable": mcCWDMCardTable,
       "mcCWDMCardEntry": mcCWDMCardEntry,
       "cwdmWavelengthCount": cwdmWavelengthCount,
       "cwdmWavelength1": cwdmWavelength1,
       "cwdmWavelength2": cwdmWavelength2,
       "cwdmWavelength3": cwdmWavelength3,
       "cwdmWavelength4": cwdmWavelength4,
       "cwdmWavelength5": cwdmWavelength5,
       "cwdmWavelength6": cwdmWavelength6,
       "cwdmWavelength7": cwdmWavelength7,
       "cwdmWavelength8": cwdmWavelength8,
       "mc10G-OEO2RObjects": mc10G_OEO2RObjects,
       "mc10G-OEO2RCardObjects": mc10G_OEO2RCardObjects,
       "mc10G-OEO2RCardTable": mc10G_OEO2RCardTable,
       "mc10G-OEO2RCardEntry": mc10G_OEO2RCardEntry,
       "mc10G-OEO2RCurSpdMode": mc10G_OEO2RCurSpdMode,
       "mc10G-OEO2RCfgSpdMode": mc10G_OEO2RCfgSpdMode,
       "mc10G-OEO2RSFP1Loopback": mc10G_OEO2RSFP1Loopback,
       "mc10G-OEO2RSFP2Loopback": mc10G_OEO2RSFP2Loopback,
       "mc10G-OEO2RSFP1": mc10G_OEO2RSFP1,
       "mc10G-OEO2RSFP2": mc10G_OEO2RSFP2,
       "mc10G-OEO2RHWSpdMode": mc10G_OEO2RHWSpdMode,
       "mc10G-OEO2RHWSFP1Loopback": mc10G_OEO2RHWSFP1Loopback,
       "mc10G-OEO2RHWSFP2Loopback": mc10G_OEO2RHWSFP2Loopback,
       "mc10G-OEO2RVersion": mc10G_OEO2RVersion,
       "mc10GXFP1WaveLengthTunability": mc10GXFP1WaveLengthTunability,
       "mc10GXFP1WaveLengthTunable": mc10GXFP1WaveLengthTunable,
       "mc10GXFP1WaveLength": mc10GXFP1WaveLength,
       "mc10GXFP2WaveLengthTunability": mc10GXFP2WaveLengthTunability,
       "mc10GXFP2WaveLengthTunable": mc10GXFP2WaveLengthTunable,
       "mc10GXFP2WaveLength": mc10GXFP2WaveLength,
       "mc10G-OEO2R-accType": mc10G_OEO2R_accType,
       "mc10G-OEO2R-ntwType": mc10G_OEO2R_ntwType,
       "mc10G-OEO2R-accTunableType": mc10G_OEO2R_accTunableType,
       "mc10G-OEO2R-ntwTunableType": mc10G_OEO2R_ntwTunableType,
       "mcQCA8334Objects": mcQCA8334Objects,
       "mcQCA8334CardObjects": mcQCA8334CardObjects,
       "mcQCA8334CardTable": mcQCA8334CardTable,
       "mcQCA8334CardEntry": mcQCA8334CardEntry,
       "mcQCA8334VlanMode": mcQCA8334VlanMode,
       "mcQCA8334PortObjects": mcQCA8334PortObjects,
       "mcQCA8334PortTable": mcQCA8334PortTable,
       "mcQCA8334PortEntry": mcQCA8334PortEntry,
       "mcQCA8334PortIdx": mcQCA8334PortIdx,
       "mcQCA8334CurWorkMode": mcQCA8334CurWorkMode,
       "mcQCA8334CfgWorkMode": mcQCA8334CfgWorkMode,
       "mcQCA8334UpStream": mcQCA8334UpStream,
       "mcQCA8334DownStream": mcQCA8334DownStream,
       "mcQCA8334Txlink": mcQCA8334Txlink,
       "mcQCA8334RmtCurWorkMode": mcQCA8334RmtCurWorkMode,
       "mcQCA8334RmtCfgWorkMode": mcQCA8334RmtCfgWorkMode,
       "mcQCA8334RmtTxlink": mcQCA8334RmtTxlink,
       "mcE1T1Objects": mcE1T1Objects,
       "mcE1T1CardObjects": mcE1T1CardObjects,
       "mcE1T1CardTable": mcE1T1CardTable,
       "mcE1T1CardEntry": mcE1T1CardEntry,
       "mcE1T1Type": mcE1T1Type,
       "mcE1T1FLink": mcE1T1FLink,
       "mcE1T1FLossAlarm": mcE1T1FLossAlarm,
       "mcE1T1TLossAlarm": mcE1T1TLossAlarm,
       "mcE1T1AISAlarm": mcE1T1AISAlarm,
       "mcE1T1TLoop": mcE1T1TLoop,
       "mcE1T1FLoop": mcE1T1FLoop,
       "mcE1T1CodeType": mcE1T1CodeType,
       "mcE1T1Version": mcE1T1Version,
       "mcE1T1RmtFLink": mcE1T1RmtFLink,
       "mcE1T1RmtFLossAlarm": mcE1T1RmtFLossAlarm,
       "mcE1T1RmtTLossAlarm": mcE1T1RmtTLossAlarm,
       "mcE1T1RmtAISAlarm": mcE1T1RmtAISAlarm,
       "mcE1T1RmtTLoop": mcE1T1RmtTLoop,
       "mcE1T1RmtFLoop": mcE1T1RmtFLoop,
       "mcE1T1RmtCodeType": mcE1T1RmtCodeType,
       "mc10GOEEXFPTunableObjects": mc10GOEEXFPTunableObjects,
       "mc10GOEEXFPTunableCardObjects": mc10GOEEXFPTunableCardObjects,
       "mc10GOEEXFPTunableCardTable": mc10GOEEXFPTunableCardTable,
       "mc10GOEEXFPTunableCardEntry": mc10GOEEXFPTunableCardEntry,
       "xfpWaveLengthTunability": xfpWaveLengthTunability,
       "xfpWaveLengthTunable": xfpWaveLengthTunable,
       "xfpWaveLength": xfpWaveLength,
       "xfpTunableType": xfpTunableType,
       "mcPmObjects": mcPmObjects,
       "mcPmTable": mcPmTable,
       "mcPmEntry": mcPmEntry,
       "mcRxByteHi": mcRxByteHi,
       "mcRxByteLo": mcRxByteLo,
       "mcTxByteHi": mcTxByteHi,
       "mcTxByteLo": mcTxByteLo,
       "mcPmRest": mcPmRest,
       "alarmMIB": alarmMIB,
       "shelf-Detected": shelf_Detected,
       "shelf-Lost": shelf_Lost,
       "shelf-psuA-On": shelf_psuA_On,
       "shelf-psuA-Off": shelf_psuA_Off,
       "shelf-psuB-On": shelf_psuB_On,
       "shelf-psuB-Off": shelf_psuB_Off,
       "shelf-fan-On": shelf_fan_On,
       "shelf-fan-Off": shelf_fan_Off,
       "card-Detected": card_Detected,
       "card-Lost": card_Lost,
       "card-MC-Co-Tx-Up": card_MC_Co_Tx_Up,
       "card-MC-Co-Tx-Down": card_MC_Co_Tx_Down,
       "card-MC-Co-Fx-Up": card_MC_Co_Fx_Up,
       "card-MC-Co-Fx-Down": card_MC_Co_Fx_Down,
       "card-MC-Rmt-Tx-Up": card_MC_Rmt_Tx_Up,
       "card-MC-Rmt-Tx-Down": card_MC_Rmt_Tx_Down,
       "card-MC-Rmt-PwrDown": card_MC_Rmt_PwrDown,
       "card-MC-Co-Ntw-SFP-Inserted": card_MC_Co_Ntw_SFP_Inserted,
       "card-MC-Co-Ntw-SFP-Removed": card_MC_Co_Ntw_SFP_Removed,
       "card-MC-Co-Acc-SFP-Inserted": card_MC_Co_Acc_SFP_Inserted,
       "card-MC-Co-Acc-SFP-Removed": card_MC_Co_Acc_SFP_Removed,
       "card-MC-Rmt-Acc-SFP-Inserted": card_MC_Rmt_Acc_SFP_Inserted,
       "card-MC-Rmt-Acc-SFP-Removed": card_MC_Rmt_Acc_SFP_Removed,
       "card-MC-Co-Tx-Up1": card_MC_Co_Tx_Up1,
       "card-MC-Co-Tx-Down1": card_MC_Co_Tx_Down1,
       "card-MC-Co-Tx-Up2": card_MC_Co_Tx_Up2,
       "card-MC-Co-Tx-Down2": card_MC_Co_Tx_Down2,
       "card-MC-Rmt-Tx-Up1": card_MC_Rmt_Tx_Up1,
       "card-MC-Rmt-Tx-Down1": card_MC_Rmt_Tx_Down1,
       "card-MC-Rmt-Tx-Up2": card_MC_Rmt_Tx_Up2,
       "card-MC-Rmt-Tx-Down2": card_MC_Rmt_Tx_Down2,
       "card-MC-Co-SFP1-Inserted": card_MC_Co_SFP1_Inserted,
       "card-MC-Co-SFP1-Removed": card_MC_Co_SFP1_Removed,
       "card-MC-Co-SFP2-Inserted": card_MC_Co_SFP2_Inserted,
       "card-MC-Co-SFP2-Removed": card_MC_Co_SFP2_Removed,
       "card-MC-Co-SFP1-Up": card_MC_Co_SFP1_Up,
       "card-MC-Co-SFP1-Down": card_MC_Co_SFP1_Down,
       "card-MC-Co-SFP2-Up": card_MC_Co_SFP2_Up,
       "card-MC-Co-SFP2-Down": card_MC_Co_SFP2_Down,
       "card-MC-Rmt-SFP1-Inserted": card_MC_Rmt_SFP1_Inserted,
       "card-MC-Rmt-SFP1-Removed": card_MC_Rmt_SFP1_Removed,
       "card-MC-Rmt-SFP1-Up": card_MC_Rmt_SFP1_Up,
       "card-MC-Rmt-SFP1-Down": card_MC_Rmt_SFP1_Down,
       "card-MC-Co-SFPSFP1-Inserted": card_MC_Co_SFPSFP1_Inserted,
       "card-MC-Co-SFPSFP1-Removed": card_MC_Co_SFPSFP1_Removed,
       "card-MC-Co-SFPSFP2-Inserted": card_MC_Co_SFPSFP2_Inserted,
       "card-MC-Co-SFPSFP2-Removed": card_MC_Co_SFPSFP2_Removed,
       "card-MC-Rmt-SFPSFP1-Inserted": card_MC_Rmt_SFPSFP1_Inserted,
       "card-MC-Rmt-SFPSFP1-Removed": card_MC_Rmt_SFPSFP1_Removed,
       "card-MC-Co-XFP1-Inserted": card_MC_Co_XFP1_Inserted,
       "card-MC-Co-XFP1-Removed": card_MC_Co_XFP1_Removed,
       "card-MC-Co-XFP2-Inserted": card_MC_Co_XFP2_Inserted,
       "card-MC-Co-XFP2-Removed": card_MC_Co_XFP2_Removed,
       "card-MC-Rmt-XFP1-Inserted": card_MC_Rmt_XFP1_Inserted,
       "card-MC-Rmt-XFP1-Removed": card_MC_Rmt_XFP1_Removed,
       "card-MC-Co-SFPSFP1-Up": card_MC_Co_SFPSFP1_Up,
       "card-MC-Co-SFPSFP1-Down": card_MC_Co_SFPSFP1_Down,
       "card-MC-Co-SFPSFP2-Up": card_MC_Co_SFPSFP2_Up,
       "card-MC-Co-SFPSFP2-Down": card_MC_Co_SFPSFP2_Down,
       "card-MC-Rmt-SFPSFP1-Up": card_MC_Rmt_SFPSFP1_Up,
       "card-MC-Rmt-SFPSFP1-Down": card_MC_Rmt_SFPSFP1_Down,
       "card-MC-Co-XFP1-Up": card_MC_Co_XFP1_Up,
       "card-MC-Co-XFP1-Down": card_MC_Co_XFP1_Down,
       "card-MC-Co-XFP2-Up": card_MC_Co_XFP2_Up,
       "card-MC-Co-XFP2-Down": card_MC_Co_XFP2_Down,
       "card-MC-Rmt-XFP1-Up": card_MC_Rmt_XFP1_Up,
       "card-MC-Rmt-XFP1-Down": card_MC_Rmt_XFP1_Down,
       "card-MC-Co-SFP3-Inserted": card_MC_Co_SFP3_Inserted,
       "card-MC-Co-SFP3-Removed": card_MC_Co_SFP3_Removed,
       "card-MC-Co-Port1-Up": card_MC_Co_Port1_Up,
       "card-MC-Co-Port1-Down": card_MC_Co_Port1_Down,
       "card-MC-Co-Port2-Up": card_MC_Co_Port2_Up,
       "card-MC-Co-Port2-Down": card_MC_Co_Port2_Down,
       "card-MC-Co-Port3-Up": card_MC_Co_Port3_Up,
       "card-MC-Co-Port3-Down": card_MC_Co_Port3_Down,
       "card-MC-FAN-Normal": card_MC_FAN_Normal,
       "card-MC-FAN-Abnormal": card_MC_FAN_Abnormal,
       "card-MC-Co-QSFP1-Inserted": card_MC_Co_QSFP1_Inserted,
       "card-MC-Co-QSFP1-Removed": card_MC_Co_QSFP1_Removed,
       "card-MC-Co-QSFP2-Inserted": card_MC_Co_QSFP2_Inserted,
       "card-MC-Co-QSFP2-Removed": card_MC_Co_QSFP2_Removed,
       "card-MC-Co-QSFP1-Lane1-Up": card_MC_Co_QSFP1_Lane1_Up,
       "card-MC-Co-QSFP1-Lane1-Down": card_MC_Co_QSFP1_Lane1_Down,
       "card-MC-Co-QSFP1-Lane2-Up": card_MC_Co_QSFP1_Lane2_Up,
       "card-MC-Co-QSFP1-Lane2-Down": card_MC_Co_QSFP1_Lane2_Down,
       "card-MC-Co-QSFP1-Lane3-Up": card_MC_Co_QSFP1_Lane3_Up,
       "card-MC-Co-QSFP1-Lane3-Down": card_MC_Co_QSFP1_Lane3_Down,
       "card-MC-Co-QSFP1-Lane4-Up": card_MC_Co_QSFP1_Lane4_Up,
       "card-MC-Co-QSFP1-Lane4-Down": card_MC_Co_QSFP1_Lane4_Down,
       "card-MC-Co-QSFP2-Lane1-Up": card_MC_Co_QSFP2_Lane1_Up,
       "card-MC-Co-QSFP2-Lane1-Down": card_MC_Co_QSFP2_Lane1_Down,
       "card-MC-Co-QSFP2-Lane2-Up": card_MC_Co_QSFP2_Lane2_Up,
       "card-MC-Co-QSFP2-Lane2-Down": card_MC_Co_QSFP2_Lane2_Down,
       "card-MC-Co-QSFP2-Lane3-Up": card_MC_Co_QSFP2_Lane3_Up,
       "card-MC-Co-QSFP2-Lane3-Down": card_MC_Co_QSFP2_Lane3_Down,
       "card-MC-Co-QSFP2-Lane4-Up": card_MC_Co_QSFP2_Lane4_Up,
       "card-MC-Co-QSFP2-Lane4-Down": card_MC_Co_QSFP2_Lane4_Down,
       "card-MC-Rmt-SFP2-Inserted": card_MC_Rmt_SFP2_Inserted,
       "card-MC-Rmt-SFP2-Removed": card_MC_Rmt_SFP2_Removed,
       "card-MC-Rmt-SFP3-Inserted": card_MC_Rmt_SFP3_Inserted,
       "card-MC-Rmt-SFP3-Removed": card_MC_Rmt_SFP3_Removed,
       "card-MC-Rmt-SFP2-Up": card_MC_Rmt_SFP2_Up,
       "card-MC-Rmt-SFP2-Down": card_MC_Rmt_SFP2_Down,
       "card-MC-Rmt-SFP3-Up": card_MC_Rmt_SFP3_Up,
       "card-MC-Rmt-SFP3-Down": card_MC_Rmt_SFP3_Down,
       "card-MC-E1-Co-Port1-LOS-Alarm": card_MC_E1_Co_Port1_LOS_Alarm,
       "card-MC-E1-Co-Port1-LOS-Normal": card_MC_E1_Co_Port1_LOS_Normal,
       "card-MC-E1-Co-Port1-AIS-Alarm": card_MC_E1_Co_Port1_AIS_Alarm,
       "card-MC-E1-Co-Port1-AIS-Normal": card_MC_E1_Co_Port1_AIS_Normal,
       "card-MC-E1-Co-Port1-CV-Alarm": card_MC_E1_Co_Port1_CV_Alarm,
       "card-MC-E1-Co-Port1-CV-Normal": card_MC_E1_Co_Port1_CV_Normal,
       "card-MC-E1-Co-Port2-LOS-Alarm": card_MC_E1_Co_Port2_LOS_Alarm,
       "card-MC-E1-Co-Port2-LOS-Normal": card_MC_E1_Co_Port2_LOS_Normal,
       "card-MC-E1-Co-Port2-AIS-Alarm": card_MC_E1_Co_Port2_AIS_Alarm,
       "card-MC-E1-Co-Port2-AIS-Normal": card_MC_E1_Co_Port2_AIS_Normal,
       "card-MC-E1-Co-Port2-CV-Alarm": card_MC_E1_Co_Port2_CV_Alarm,
       "card-MC-E1-Co-Port2-CV-Normal": card_MC_E1_Co_Port2_CV_Normal,
       "card-MC-E1-Rmt-Port1-LOS-Alarm": card_MC_E1_Rmt_Port1_LOS_Alarm,
       "card-MC-E1-Rmt-Port1-LOS-Normal": card_MC_E1_Rmt_Port1_LOS_Normal,
       "card-MC-E1-Rmt-Port1-AIS-Alarm": card_MC_E1_Rmt_Port1_AIS_Alarm,
       "card-MC-E1-Rmt-Port1-AIS-Normal": card_MC_E1_Rmt_Port1_AIS_Normal,
       "card-MC-E1-Rmt-Port1-CV-Alarm": card_MC_E1_Rmt_Port1_CV_Alarm,
       "card-MC-E1-Rmt-Port1-CV-Normal": card_MC_E1_Rmt_Port1_CV_Normal,
       "card-MC-E1-Rmt-Port2-LOS-Alarm": card_MC_E1_Rmt_Port2_LOS_Alarm,
       "card-MC-E1-Rmt-Port2-LOS-Normal": card_MC_E1_Rmt_Port2_LOS_Normal,
       "card-MC-E1-Rmt-Port2-AIS-Alarm": card_MC_E1_Rmt_Port2_AIS_Alarm,
       "card-MC-E1-Rmt-Port2-AIS-Normal": card_MC_E1_Rmt_Port2_AIS_Normal,
       "card-MC-E1-Rmt-Port2-CV-Alarm": card_MC_E1_Rmt_Port2_CV_Alarm,
       "card-MC-E1-Rmt-Port2-CV-Normal": card_MC_E1_Rmt_Port2_CV_Normal,
       "card-MC-Co-SFP3-Up": card_MC_Co_SFP3_Up,
       "card-MC-Co-SFP3-Down": card_MC_Co_SFP3_Down,
       "card-MC-E1T1-Co-TXLOS-Alarm": card_MC_E1T1_Co_TXLOS_Alarm,
       "card-MC-E1T1-Co-TXLOS-Normal": card_MC_E1T1_Co_TXLOS_Normal,
       "card-MC-E1T1-Co-FXLOS-Alarm": card_MC_E1T1_Co_FXLOS_Alarm,
       "card-MC-E1T1-Co-FXLOS-Normal": card_MC_E1T1_Co_FXLOS_Normal,
       "card-MC-E1T1-Co-AIS-Alarm": card_MC_E1T1_Co_AIS_Alarm,
       "card-MC-E1T1-Co-AIS-Normal": card_MC_E1T1_Co_AIS_Normal,
       "card-MC-E1T1-Rmt-TXLOS-Alarm": card_MC_E1T1_Rmt_TXLOS_Alarm,
       "card-MC-E1T1-Rmt-TXLOS-Normal": card_MC_E1T1_Rmt_TXLOS_Normal,
       "card-MC-E1T1-Rmt-FXLOS-Alarm": card_MC_E1T1_Rmt_FXLOS_Alarm,
       "card-MC-E1T1-Rmt-FXLOS-Normal": card_MC_E1T1_Rmt_FXLOS_Normal,
       "card-MC-E1T1-Rmt-AIS-Alarm": card_MC_E1T1_Rmt_AIS_Alarm,
       "card-MC-E1T1-Rmt-AIS-Normal": card_MC_E1T1_Rmt_AIS_Normal}
)
