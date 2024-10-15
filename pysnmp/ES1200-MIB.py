# SNMP MIB module (ES1200-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ES1200-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:42 2024
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

(MacAddress,
 dot1dBasePort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress",
    "dot1dBasePort")

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



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )





class VlanIndex(Integer32):
    """Custom type VlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )





class EnabledStatus(Integer32):
    """Custom type EnabledStatus based on Integer32"""
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





class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class TimeInterval(Integer32):
    """Custom type TimeInterval based on Integer32"""




class Unsigned32(Integer32):
    """Custom type Unsigned32 based on Integer32"""




class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )





class TimeFilter(Integer32):
    """Custom type TimeFilter based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fore_ObjectIdentity = ObjectIdentity
fore = _Fore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2)
)
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20)
)
_Edge_ObjectIdentity = ObjectIdentity
edge = _Edge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1)
)
_Edgecommon_ObjectIdentity = ObjectIdentity
edgecommon = _Edgecommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1)
)
_Golf_ObjectIdentity = ObjectIdentity
golf = _Golf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2)
)
_Golfproducts_ObjectIdentity = ObjectIdentity
golfproducts = _Golfproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1)
)
_Es1200_ObjectIdentity = ObjectIdentity
es1200 = _Es1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 2)
)
_Golfcommon_ObjectIdentity = ObjectIdentity
golfcommon = _Golfcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2)
)
_Fore_products_ObjectIdentity = ObjectIdentity
fore_products = _Fore_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1)
)
_Fore_es1200Prod_ObjectIdentity = ObjectIdentity
fore_es1200Prod = _Fore_es1200Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25)
)
_SwProperty_ObjectIdentity = ObjectIdentity
swProperty = _SwProperty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 1)
)
_SwModule_ObjectIdentity = ObjectIdentity
swModule = _SwModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 1, 1)
)
_Es1200DevRegistration_ObjectIdentity = ObjectIdentity
es1200DevRegistration = _Es1200DevRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 2)
)
_Es1200Device_ObjectIdentity = ObjectIdentity
es1200Device = _Es1200Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 2, 1)
)
_Es1200UnitRegistration_ObjectIdentity = ObjectIdentity
es1200UnitRegistration = _Es1200UnitRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 3)
)
_Es1200Master_ObjectIdentity = ObjectIdentity
es1200Master = _Es1200Master_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 3, 1)
)
_Es1210Slave1_ObjectIdentity = ObjectIdentity
es1210Slave1 = _Es1210Slave1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 3, 2)
)
_Es1210Slave2_ObjectIdentity = ObjectIdentity
es1210Slave2 = _Es1210Slave2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 3, 3)
)
_Es1210Slave3_ObjectIdentity = ObjectIdentity
es1210Slave3 = _Es1210Slave3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 3, 4)
)
_Es1200ModuleRegistration_ObjectIdentity = ObjectIdentity
es1200ModuleRegistration = _Es1200ModuleRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 4)
)
_Es1200ModuleMainboardTx_ObjectIdentity = ObjectIdentity
es1200ModuleMainboardTx = _Es1200ModuleMainboardTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 4, 1)
)
_Es1200ModuleTxTwoPort_ObjectIdentity = ObjectIdentity
es1200ModuleTxTwoPort = _Es1200ModuleTxTwoPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 4, 2)
)
_Es1200ModuleFxSC_ObjectIdentity = ObjectIdentity
es1200ModuleFxSC = _Es1200ModuleFxSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 4, 3)
)
_Es1200ModuleFxMTRJ_ObjectIdentity = ObjectIdentity
es1200ModuleFxMTRJ = _Es1200ModuleFxMTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 4, 4)
)
_Es1200ModuleSIO_ObjectIdentity = ObjectIdentity
es1200ModuleSIO = _Es1200ModuleSIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 4, 5)
)
_Es1200ModuleSXGIGAOnePort_ObjectIdentity = ObjectIdentity
es1200ModuleSXGIGAOnePort = _Es1200ModuleSXGIGAOnePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 4, 6)
)
_Es1200ModuleSXGIGATwoPort_ObjectIdentity = ObjectIdentity
es1200ModuleSXGIGATwoPort = _Es1200ModuleSXGIGATwoPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 4, 7)
)
_Es1200ModuleLXGIGAOnePort_ObjectIdentity = ObjectIdentity
es1200ModuleLXGIGAOnePort = _Es1200ModuleLXGIGAOnePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 4, 8)
)
_Es1200ModuleLXGIGATwoPort_ObjectIdentity = ObjectIdentity
es1200ModuleLXGIGATwoPort = _Es1200ModuleLXGIGATwoPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 4, 9)
)
_Es1200ModuleTXGIGAOnePort_ObjectIdentity = ObjectIdentity
es1200ModuleTXGIGAOnePort = _Es1200ModuleTXGIGAOnePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 4, 10)
)
_Es1200ModuleTXGIGATwoPort_ObjectIdentity = ObjectIdentity
es1200ModuleTXGIGATwoPort = _Es1200ModuleTXGIGATwoPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 4, 11)
)
_Es1200ModuleNone_ObjectIdentity = ObjectIdentity
es1200ModuleNone = _Es1200ModuleNone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 4, 12)
)
_Es1210ModuleRegistration_ObjectIdentity = ObjectIdentity
es1210ModuleRegistration = _Es1210ModuleRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 5)
)
_Es1210ModuleMainboardTx_ObjectIdentity = ObjectIdentity
es1210ModuleMainboardTx = _Es1210ModuleMainboardTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 5, 1)
)
_Es1210ModuleTxTwoPort_ObjectIdentity = ObjectIdentity
es1210ModuleTxTwoPort = _Es1210ModuleTxTwoPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 5, 2)
)
_Es1210ModuleFxSC_ObjectIdentity = ObjectIdentity
es1210ModuleFxSC = _Es1210ModuleFxSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 5, 3)
)
_Es1210ModuleFxMTRJ_ObjectIdentity = ObjectIdentity
es1210ModuleFxMTRJ = _Es1210ModuleFxMTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 5, 4)
)
_Es1210ModuleSIO_ObjectIdentity = ObjectIdentity
es1210ModuleSIO = _Es1210ModuleSIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 5, 5)
)
_Es1210ModuleNone_ObjectIdentity = ObjectIdentity
es1210ModuleNone = _Es1210ModuleNone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 5, 6)
)
_Es1200PortRegistration_ObjectIdentity = ObjectIdentity
es1200PortRegistration = _Es1200PortRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 6)
)
_Es1200Port_10_100TX_ObjectIdentity = ObjectIdentity
es1200Port_10_100TX = _Es1200Port_10_100TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 6, 1)
)
_Es1200Port_100_SC_ObjectIdentity = ObjectIdentity
es1200Port_100_SC = _Es1200Port_100_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 6, 2)
)
_Es1200Port_100_MTRJ_ObjectIdentity = ObjectIdentity
es1200Port_100_MTRJ = _Es1200Port_100_MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 6, 3)
)
_Es1200Port_1000_SX_ObjectIdentity = ObjectIdentity
es1200Port_1000_SX = _Es1200Port_1000_SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 6, 4)
)
_Es1200Port_1000_LX_ObjectIdentity = ObjectIdentity
es1200Port_1000_LX = _Es1200Port_1000_LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 6, 5)
)
_Es1200Port_1000_TX_ObjectIdentity = ObjectIdentity
es1200Port_1000_TX = _Es1200Port_1000_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 6, 6)
)
_Es1210PortRegistration_ObjectIdentity = ObjectIdentity
es1210PortRegistration = _Es1210PortRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 7)
)
_Es1210Port_10_100TX_ObjectIdentity = ObjectIdentity
es1210Port_10_100TX = _Es1210Port_10_100TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 7, 1)
)
_Es1210Port_100_SC_ObjectIdentity = ObjectIdentity
es1210Port_100_SC = _Es1210Port_100_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 7, 2)
)
_Es1210Port_100_MTRJ_ObjectIdentity = ObjectIdentity
es1210Port_100_MTRJ = _Es1210Port_100_MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 7, 3)
)
_Es1200PowerSupplyRegistration_ObjectIdentity = ObjectIdentity
es1200PowerSupplyRegistration = _Es1200PowerSupplyRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 8)
)
_Es1200PowerSupply_ObjectIdentity = ObjectIdentity
es1200PowerSupply = _Es1200PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 8, 1)
)
_Es1210PowerSupplyRegistration_ObjectIdentity = ObjectIdentity
es1210PowerSupplyRegistration = _Es1210PowerSupplyRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 9)
)
_Es1210PowerSupply_ObjectIdentity = ObjectIdentity
es1210PowerSupply = _Es1210PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 9, 1)
)
_Es1200FanRegistration_ObjectIdentity = ObjectIdentity
es1200FanRegistration = _Es1200FanRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 10)
)
_Es1200Fan_ObjectIdentity = ObjectIdentity
es1200Fan = _Es1200Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 10, 1)
)
_Es1210FanRegistration_ObjectIdentity = ObjectIdentity
es1210FanRegistration = _Es1210FanRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 11)
)
_Es1210Fan_ObjectIdentity = ObjectIdentity
es1210Fan = _Es1210Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 11, 1)
)
_Es1200SlotRegistration_ObjectIdentity = ObjectIdentity
es1200SlotRegistration = _Es1200SlotRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 12)
)
_Es1200Slot1_ObjectIdentity = ObjectIdentity
es1200Slot1 = _Es1200Slot1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 12, 1)
)
_Es1200Slot2_ObjectIdentity = ObjectIdentity
es1200Slot2 = _Es1200Slot2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 12, 2)
)
_Es1200Slot3_ObjectIdentity = ObjectIdentity
es1200Slot3 = _Es1200Slot3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 12, 3)
)
_Es1210SlotRegistration_ObjectIdentity = ObjectIdentity
es1210SlotRegistration = _Es1210SlotRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 13)
)
_Es1210Slot1_ObjectIdentity = ObjectIdentity
es1210Slot1 = _Es1210Slot1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 13, 1)
)
_Es1210Slot2_ObjectIdentity = ObjectIdentity
es1210Slot2 = _Es1210Slot2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 13, 2)
)
_Es1200SensorRegistration_ObjectIdentity = ObjectIdentity
es1200SensorRegistration = _Es1200SensorRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 14)
)
_Es1200BackplaneRegistration_ObjectIdentity = ObjectIdentity
es1200BackplaneRegistration = _Es1200BackplaneRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 25, 15)
)
_Fore_mgmt_ObjectIdentity = ObjectIdentity
fore_mgmt = _Fore_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)
)
_Es1200Mgmt_ObjectIdentity = ObjectIdentity
es1200Mgmt = _Es1200Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25)
)
_SwStructure_ObjectIdentity = ObjectIdentity
swStructure = _SwStructure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1)
)
_SwStructInfo_ObjectIdentity = ObjectIdentity
swStructInfo = _SwStructInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 1)
)
_SwStructDevType_Type = ObjectIdentifier
_SwStructDevType_Object = MibScalar
swStructDevType = _SwStructDevType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 1, 1),
    _SwStructDevType_Type()
)
swStructDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructDevType.setStatus("mandatory")


class _SwStructDevDescr_Type(DisplayString):
    """Custom type swStructDevDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwStructDevDescr_Type.__name__ = "DisplayString"
_SwStructDevDescr_Object = MibScalar
swStructDevDescr = _SwStructDevDescr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 1, 2),
    _SwStructDevDescr_Type()
)
swStructDevDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructDevDescr.setStatus("mandatory")
_SwStructPortEncodingFactor_Type = Integer32
_SwStructPortEncodingFactor_Object = MibScalar
swStructPortEncodingFactor = _SwStructPortEncodingFactor_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 1, 3),
    _SwStructPortEncodingFactor_Type()
)
swStructPortEncodingFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructPortEncodingFactor.setStatus("mandatory")
_SwStructUnitTable_Object = MibTable
swStructUnitTable = _SwStructUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 2)
)
if mibBuilder.loadTexts:
    swStructUnitTable.setStatus("mandatory")
_SwStructUnitEntry_Object = MibTableRow
swStructUnitEntry = _SwStructUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 2, 1)
)
swStructUnitEntry.setIndexNames(
    (0, "ES1200-MIB", "swStructUnitIndex"),
)
if mibBuilder.loadTexts:
    swStructUnitEntry.setStatus("mandatory")
_SwStructUnitIndex_Type = Integer32
_SwStructUnitIndex_Object = MibTableColumn
swStructUnitIndex = _SwStructUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 2, 1, 1),
    _SwStructUnitIndex_Type()
)
swStructUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructUnitIndex.setStatus("mandatory")
_SwStructUnitType_Type = ObjectIdentifier
_SwStructUnitType_Object = MibTableColumn
swStructUnitType = _SwStructUnitType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 2, 1, 2),
    _SwStructUnitType_Type()
)
swStructUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructUnitType.setStatus("mandatory")


class _SwStructUnitDescr_Type(DisplayString):
    """Custom type swStructUnitDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwStructUnitDescr_Type.__name__ = "DisplayString"
_SwStructUnitDescr_Object = MibTableColumn
swStructUnitDescr = _SwStructUnitDescr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 2, 1, 3),
    _SwStructUnitDescr_Type()
)
swStructUnitDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructUnitDescr.setStatus("mandatory")


class _SwStructUnitLedInfo_Type(OctetString):
    """Custom type swStructUnitLedInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SwStructUnitLedInfo_Type.__name__ = "OctetString"
_SwStructUnitLedInfo_Object = MibTableColumn
swStructUnitLedInfo = _SwStructUnitLedInfo_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 2, 1, 4),
    _SwStructUnitLedInfo_Type()
)
swStructUnitLedInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructUnitLedInfo.setStatus("mandatory")
_SwStructUnitMaxModuleNum_Type = Integer32
_SwStructUnitMaxModuleNum_Object = MibTableColumn
swStructUnitMaxModuleNum = _SwStructUnitMaxModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 2, 1, 5),
    _SwStructUnitMaxModuleNum_Type()
)
swStructUnitMaxModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructUnitMaxModuleNum.setStatus("mandatory")
_SwStructUnitMaxPortNum_Type = Integer32
_SwStructUnitMaxPortNum_Object = MibTableColumn
swStructUnitMaxPortNum = _SwStructUnitMaxPortNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 2, 1, 6),
    _SwStructUnitMaxPortNum_Type()
)
swStructUnitMaxPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructUnitMaxPortNum.setStatus("mandatory")
_SwStructUnitNumOfPortInUse_Type = Integer32
_SwStructUnitNumOfPortInUse_Object = MibTableColumn
swStructUnitNumOfPortInUse = _SwStructUnitNumOfPortInUse_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 2, 1, 7),
    _SwStructUnitNumOfPortInUse_Type()
)
swStructUnitNumOfPortInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructUnitNumOfPortInUse.setStatus("mandatory")


class _SwStructUnitOperStatus_Type(Integer32):
    """Custom type swStructUnitOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("fatalErr", 10),
          ("nonFatalErr", 9),
          ("normal", 5),
          ("notAvail", 2),
          ("other", 1),
          ("removed", 3))
    )


_SwStructUnitOperStatus_Type.__name__ = "Integer32"
_SwStructUnitOperStatus_Object = MibTableColumn
swStructUnitOperStatus = _SwStructUnitOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 2, 1, 8),
    _SwStructUnitOperStatus_Type()
)
swStructUnitOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructUnitOperStatus.setStatus("mandatory")
_SwStructUnitLastChange_Type = Integer32
_SwStructUnitLastChange_Object = MibTableColumn
swStructUnitLastChange = _SwStructUnitLastChange_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 2, 1, 9),
    _SwStructUnitLastChange_Type()
)
swStructUnitLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructUnitLastChange.setStatus("mandatory")
_SwStructModuleTable_Object = MibTable
swStructModuleTable = _SwStructModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 3)
)
if mibBuilder.loadTexts:
    swStructModuleTable.setStatus("mandatory")
_SwStructModuleEntry_Object = MibTableRow
swStructModuleEntry = _SwStructModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 3, 1)
)
swStructModuleEntry.setIndexNames(
    (0, "ES1200-MIB", "swStructModuleUnitIndex"),
    (0, "ES1200-MIB", "swStructModuleIndex"),
    (0, "ES1200-MIB", "swStructModuleSubMduIndex"),
)
if mibBuilder.loadTexts:
    swStructModuleEntry.setStatus("mandatory")
_SwStructModuleUnitIndex_Type = Integer32
_SwStructModuleUnitIndex_Object = MibTableColumn
swStructModuleUnitIndex = _SwStructModuleUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 3, 1, 1),
    _SwStructModuleUnitIndex_Type()
)
swStructModuleUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleUnitIndex.setStatus("mandatory")
_SwStructModuleIndex_Type = Integer32
_SwStructModuleIndex_Object = MibTableColumn
swStructModuleIndex = _SwStructModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 3, 1, 2),
    _SwStructModuleIndex_Type()
)
swStructModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleIndex.setStatus("mandatory")
_SwStructModuleSubMduIndex_Type = Integer32
_SwStructModuleSubMduIndex_Object = MibTableColumn
swStructModuleSubMduIndex = _SwStructModuleSubMduIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 3, 1, 3),
    _SwStructModuleSubMduIndex_Type()
)
swStructModuleSubMduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleSubMduIndex.setStatus("mandatory")
_SwStructModuleType_Type = ObjectIdentifier
_SwStructModuleType_Object = MibTableColumn
swStructModuleType = _SwStructModuleType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 3, 1, 4),
    _SwStructModuleType_Type()
)
swStructModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleType.setStatus("mandatory")


class _SwStructModuleDescr_Type(DisplayString):
    """Custom type swStructModuleDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwStructModuleDescr_Type.__name__ = "DisplayString"
_SwStructModuleDescr_Object = MibTableColumn
swStructModuleDescr = _SwStructModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 3, 1, 5),
    _SwStructModuleDescr_Type()
)
swStructModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleDescr.setStatus("mandatory")
_SwStructModuleVersion_Type = Integer32
_SwStructModuleVersion_Object = MibTableColumn
swStructModuleVersion = _SwStructModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 3, 1, 6),
    _SwStructModuleVersion_Type()
)
swStructModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleVersion.setStatus("mandatory")
_SwStructModuleMaxPortNum_Type = Integer32
_SwStructModuleMaxPortNum_Object = MibTableColumn
swStructModuleMaxPortNum = _SwStructModuleMaxPortNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 3, 1, 7),
    _SwStructModuleMaxPortNum_Type()
)
swStructModuleMaxPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleMaxPortNum.setStatus("mandatory")
_SwStructModuleEncodingOffset_Type = Integer32
_SwStructModuleEncodingOffset_Object = MibTableColumn
swStructModuleEncodingOffset = _SwStructModuleEncodingOffset_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 3, 1, 8),
    _SwStructModuleEncodingOffset_Type()
)
swStructModuleEncodingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleEncodingOffset.setStatus("mandatory")


class _SwStructModuleOperStatus_Type(Integer32):
    """Custom type swStructModuleOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("fatalErr", 10),
          ("nonFatalErr", 9),
          ("normal", 5),
          ("notAvail", 2),
          ("other", 1),
          ("removed", 3))
    )


_SwStructModuleOperStatus_Type.__name__ = "Integer32"
_SwStructModuleOperStatus_Object = MibTableColumn
swStructModuleOperStatus = _SwStructModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 3, 1, 9),
    _SwStructModuleOperStatus_Type()
)
swStructModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleOperStatus.setStatus("mandatory")
_SwStructModuleLastChange_Type = Integer32
_SwStructModuleLastChange_Object = MibTableColumn
swStructModuleLastChange = _SwStructModuleLastChange_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 3, 1, 10),
    _SwStructModuleLastChange_Type()
)
swStructModuleLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructModuleLastChange.setStatus("mandatory")
_SwStructPowerTable_Object = MibTable
swStructPowerTable = _SwStructPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 4)
)
if mibBuilder.loadTexts:
    swStructPowerTable.setStatus("mandatory")
_SwStructPowerEntry_Object = MibTableRow
swStructPowerEntry = _SwStructPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 4, 1)
)
swStructPowerEntry.setIndexNames(
    (0, "ES1200-MIB", "swStructPowerUnitIndex"),
    (0, "ES1200-MIB", "swStructPowerIndex"),
)
if mibBuilder.loadTexts:
    swStructPowerEntry.setStatus("mandatory")
_SwStructPowerUnitIndex_Type = Integer32
_SwStructPowerUnitIndex_Object = MibTableColumn
swStructPowerUnitIndex = _SwStructPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 4, 1, 1),
    _SwStructPowerUnitIndex_Type()
)
swStructPowerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructPowerUnitIndex.setStatus("mandatory")
_SwStructPowerIndex_Type = Integer32
_SwStructPowerIndex_Object = MibTableColumn
swStructPowerIndex = _SwStructPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 4, 1, 2),
    _SwStructPowerIndex_Type()
)
swStructPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructPowerIndex.setStatus("mandatory")


class _SwStructPowerOperStatus_Type(Integer32):
    """Custom type swStructPowerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("fatalErr", 10),
          ("nonFatalErr", 9),
          ("normal", 5),
          ("notAvail", 2),
          ("other", 1),
          ("removed", 3))
    )


_SwStructPowerOperStatus_Type.__name__ = "Integer32"
_SwStructPowerOperStatus_Object = MibTableColumn
swStructPowerOperStatus = _SwStructPowerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 4, 1, 3),
    _SwStructPowerOperStatus_Type()
)
swStructPowerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructPowerOperStatus.setStatus("mandatory")
_SwStructFanTable_Object = MibTable
swStructFanTable = _SwStructFanTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 5)
)
if mibBuilder.loadTexts:
    swStructFanTable.setStatus("mandatory")
_SwStructFanEntry_Object = MibTableRow
swStructFanEntry = _SwStructFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 5, 1)
)
swStructFanEntry.setIndexNames(
    (0, "ES1200-MIB", "swStructFanUnitIndex"),
    (0, "ES1200-MIB", "swStructFanIndex"),
)
if mibBuilder.loadTexts:
    swStructFanEntry.setStatus("mandatory")
_SwStructFanUnitIndex_Type = Integer32
_SwStructFanUnitIndex_Object = MibTableColumn
swStructFanUnitIndex = _SwStructFanUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 5, 1, 1),
    _SwStructFanUnitIndex_Type()
)
swStructFanUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructFanUnitIndex.setStatus("mandatory")
_SwStructFanIndex_Type = Integer32
_SwStructFanIndex_Object = MibTableColumn
swStructFanIndex = _SwStructFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 5, 1, 2),
    _SwStructFanIndex_Type()
)
swStructFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructFanIndex.setStatus("mandatory")


class _SwStructFanOperStatus_Type(Integer32):
    """Custom type swStructFanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("fatalErr", 10),
          ("nonFatalErr", 9),
          ("normal", 5),
          ("notAvail", 2),
          ("other", 1),
          ("removed", 3))
    )


_SwStructFanOperStatus_Type.__name__ = "Integer32"
_SwStructFanOperStatus_Object = MibTableColumn
swStructFanOperStatus = _SwStructFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 1, 5, 1, 3),
    _SwStructFanOperStatus_Type()
)
swStructFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStructFanOperStatus.setStatus("mandatory")
_SwL2Mgmt_ObjectIdentity = ObjectIdentity
swL2Mgmt = _SwL2Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2)
)
_SwL2DevMgmt_ObjectIdentity = ObjectIdentity
swL2DevMgmt = _SwL2DevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1)
)
_SwL2DevCtrl_ObjectIdentity = ObjectIdentity
swL2DevCtrl = _SwL2DevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 1)
)


class _SwL2DevCtrlStpState_Type(Integer32):
    """Custom type swL2DevCtrlStpState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevCtrlStpState_Type.__name__ = "Integer32"
_SwL2DevCtrlStpState_Object = MibScalar
swL2DevCtrlStpState = _SwL2DevCtrlStpState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 1, 1),
    _SwL2DevCtrlStpState_Type()
)
swL2DevCtrlStpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlStpState.setStatus("mandatory")


class _SwL2DevCtrlPartitionModeState_Type(Integer32):
    """Custom type swL2DevCtrlPartitionModeState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevCtrlPartitionModeState_Type.__name__ = "Integer32"
_SwL2DevCtrlPartitionModeState_Object = MibScalar
swL2DevCtrlPartitionModeState = _SwL2DevCtrlPartitionModeState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 1, 2),
    _SwL2DevCtrlPartitionModeState_Type()
)
swL2DevCtrlPartitionModeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlPartitionModeState.setStatus("mandatory")


class _SwL2DevCtrlTableLockState_Type(Integer32):
    """Custom type swL2DevCtrlTableLockState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevCtrlTableLockState_Type.__name__ = "Integer32"
_SwL2DevCtrlTableLockState_Object = MibScalar
swL2DevCtrlTableLockState = _SwL2DevCtrlTableLockState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 1, 3),
    _SwL2DevCtrlTableLockState_Type()
)
swL2DevCtrlTableLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlTableLockState.setStatus("mandatory")


class _SwL2DevCtrlHOLState_Type(Integer32):
    """Custom type swL2DevCtrlHOLState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevCtrlHOLState_Type.__name__ = "Integer32"
_SwL2DevCtrlHOLState_Object = MibScalar
swL2DevCtrlHOLState = _SwL2DevCtrlHOLState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 1, 4),
    _SwL2DevCtrlHOLState_Type()
)
swL2DevCtrlHOLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlHOLState.setStatus("mandatory")


class _SwL2DevCtrlAddrLookupModesAndHitRate_Type(Integer32):
    """Custom type swL2DevCtrlAddrLookupModesAndHitRate based on Integer32"""
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
        *(("level0", 1),
          ("level1", 2),
          ("level2", 3),
          ("level3", 4),
          ("level4", 5),
          ("level5", 6),
          ("level6", 7),
          ("level7", 8))
    )


_SwL2DevCtrlAddrLookupModesAndHitRate_Type.__name__ = "Integer32"
_SwL2DevCtrlAddrLookupModesAndHitRate_Object = MibScalar
swL2DevCtrlAddrLookupModesAndHitRate = _SwL2DevCtrlAddrLookupModesAndHitRate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 1, 5),
    _SwL2DevCtrlAddrLookupModesAndHitRate_Type()
)
swL2DevCtrlAddrLookupModesAndHitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlAddrLookupModesAndHitRate.setStatus("mandatory")


class _SwL2DevCtrlUploadImageFileName_Type(DisplayString):
    """Custom type swL2DevCtrlUploadImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwL2DevCtrlUploadImageFileName_Type.__name__ = "DisplayString"
_SwL2DevCtrlUploadImageFileName_Object = MibScalar
swL2DevCtrlUploadImageFileName = _SwL2DevCtrlUploadImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 1, 6),
    _SwL2DevCtrlUploadImageFileName_Type()
)
swL2DevCtrlUploadImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlUploadImageFileName.setStatus("mandatory")
_SwL2DevCtrlUploadImage_Type = Integer32
_SwL2DevCtrlUploadImage_Object = MibScalar
swL2DevCtrlUploadImage = _SwL2DevCtrlUploadImage_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 1, 7),
    _SwL2DevCtrlUploadImage_Type()
)
swL2DevCtrlUploadImage.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    swL2DevCtrlUploadImage.setStatus("mandatory")


class _SwL2DevCtrlClearAddressTable_Type(Integer32):
    """Custom type swL2DevCtrlClearAddressTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("other", 1))
    )


_SwL2DevCtrlClearAddressTable_Type.__name__ = "Integer32"
_SwL2DevCtrlClearAddressTable_Object = MibScalar
swL2DevCtrlClearAddressTable = _SwL2DevCtrlClearAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 1, 8),
    _SwL2DevCtrlClearAddressTable_Type()
)
swL2DevCtrlClearAddressTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlClearAddressTable.setStatus("mandatory")
_SwL2DevAlarm_ObjectIdentity = ObjectIdentity
swL2DevAlarm = _SwL2DevAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 2)
)


class _SwL2DevAlarmPartition_Type(Integer32):
    """Custom type swL2DevAlarmPartition based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevAlarmPartition_Type.__name__ = "Integer32"
_SwL2DevAlarmPartition_Object = MibScalar
swL2DevAlarmPartition = _SwL2DevAlarmPartition_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 2, 1),
    _SwL2DevAlarmPartition_Type()
)
swL2DevAlarmPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmPartition.setStatus("mandatory")


class _SwL2DevAlarmNewRoot_Type(Integer32):
    """Custom type swL2DevAlarmNewRoot based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevAlarmNewRoot_Type.__name__ = "Integer32"
_SwL2DevAlarmNewRoot_Object = MibScalar
swL2DevAlarmNewRoot = _SwL2DevAlarmNewRoot_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 2, 2),
    _SwL2DevAlarmNewRoot_Type()
)
swL2DevAlarmNewRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmNewRoot.setStatus("mandatory")


class _SwL2DevAlarmTopChange_Type(Integer32):
    """Custom type swL2DevAlarmTopChange based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevAlarmTopChange_Type.__name__ = "Integer32"
_SwL2DevAlarmTopChange_Object = MibScalar
swL2DevAlarmTopChange = _SwL2DevAlarmTopChange_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 2, 3),
    _SwL2DevAlarmTopChange_Type()
)
swL2DevAlarmTopChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmTopChange.setStatus("mandatory")


class _SwL2DevAlarmLinkChange_Type(Integer32):
    """Custom type swL2DevAlarmLinkChange based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevAlarmLinkChange_Type.__name__ = "Integer32"
_SwL2DevAlarmLinkChange_Object = MibScalar
swL2DevAlarmLinkChange = _SwL2DevAlarmLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 1, 2, 4),
    _SwL2DevAlarmLinkChange_Type()
)
swL2DevAlarmLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmLinkChange.setStatus("mandatory")
_SwL2PortMgmt_ObjectIdentity = ObjectIdentity
swL2PortMgmt = _SwL2PortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4)
)
_SwL2PortInfoTable_Object = MibTable
swL2PortInfoTable = _SwL2PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 1)
)
if mibBuilder.loadTexts:
    swL2PortInfoTable.setStatus("mandatory")
_SwL2PortInfoEntry_Object = MibTableRow
swL2PortInfoEntry = _SwL2PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 1, 1)
)
swL2PortInfoEntry.setIndexNames(
    (0, "ES1200-MIB", "swL2PortInfoUnitIndex"),
    (0, "ES1200-MIB", "swL2PortInfoModuleIndex"),
    (0, "ES1200-MIB", "swL2PortInfoIndex"),
)
if mibBuilder.loadTexts:
    swL2PortInfoEntry.setStatus("mandatory")
_SwL2PortInfoUnitIndex_Type = Integer32
_SwL2PortInfoUnitIndex_Object = MibTableColumn
swL2PortInfoUnitIndex = _SwL2PortInfoUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 1, 1, 1),
    _SwL2PortInfoUnitIndex_Type()
)
swL2PortInfoUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoUnitIndex.setStatus("mandatory")
_SwL2PortInfoModuleIndex_Type = Integer32
_SwL2PortInfoModuleIndex_Object = MibTableColumn
swL2PortInfoModuleIndex = _SwL2PortInfoModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 1, 1, 2),
    _SwL2PortInfoModuleIndex_Type()
)
swL2PortInfoModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoModuleIndex.setStatus("mandatory")
_SwL2PortInfoIndex_Type = Integer32
_SwL2PortInfoIndex_Object = MibTableColumn
swL2PortInfoIndex = _SwL2PortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 1, 1, 3),
    _SwL2PortInfoIndex_Type()
)
swL2PortInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoIndex.setStatus("mandatory")


class _SwL2PortInfoType_Type(Integer32):
    """Custom type swL2PortInfoType based on Integer32"""
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
        *(("other", 7),
          ("portType-100FXMTRJ", 3),
          ("portType-100FXSC", 2),
          ("portType-100TX", 1),
          ("portType-GIGALX", 5),
          ("portType-GIGASX", 4),
          ("portType-GIGATX", 6))
    )


_SwL2PortInfoType_Type.__name__ = "Integer32"
_SwL2PortInfoType_Object = MibTableColumn
swL2PortInfoType = _SwL2PortInfoType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 1, 1, 4),
    _SwL2PortInfoType_Type()
)
swL2PortInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoType.setStatus("mandatory")


class _SwL2PortInfoDescr_Type(DisplayString):
    """Custom type swL2PortInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwL2PortInfoDescr_Type.__name__ = "DisplayString"
_SwL2PortInfoDescr_Object = MibTableColumn
swL2PortInfoDescr = _SwL2PortInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 1, 1, 5),
    _SwL2PortInfoDescr_Type()
)
swL2PortInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoDescr.setStatus("mandatory")


class _SwL2PortInfoLinkStatus_Type(Integer32):
    """Custom type swL2PortInfoLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link-fail", 3),
          ("link-pass", 2),
          ("other", 1))
    )


_SwL2PortInfoLinkStatus_Type.__name__ = "Integer32"
_SwL2PortInfoLinkStatus_Object = MibTableColumn
swL2PortInfoLinkStatus = _SwL2PortInfoLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 1, 1, 6),
    _SwL2PortInfoLinkStatus_Type()
)
swL2PortInfoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoLinkStatus.setStatus("mandatory")


class _SwL2PortInfoNwayStatus_Type(Integer32):
    """Custom type swL2PortInfoNwayStatus based on Integer32"""
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
        *(("full-100Mbps", 5),
          ("full-10Mbps", 3),
          ("full-1Gigabps", 7),
          ("half-100Mbps", 4),
          ("half-10Mbps", 2),
          ("half-1Gigabps", 6),
          ("other", 1))
    )


_SwL2PortInfoNwayStatus_Type.__name__ = "Integer32"
_SwL2PortInfoNwayStatus_Object = MibTableColumn
swL2PortInfoNwayStatus = _SwL2PortInfoNwayStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 1, 1, 7),
    _SwL2PortInfoNwayStatus_Type()
)
swL2PortInfoNwayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoNwayStatus.setStatus("mandatory")
_SwL2PortCtrlTable_Object = MibTable
swL2PortCtrlTable = _SwL2PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2)
)
if mibBuilder.loadTexts:
    swL2PortCtrlTable.setStatus("mandatory")
_SwL2PortCtrlEntry_Object = MibTableRow
swL2PortCtrlEntry = _SwL2PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1)
)
swL2PortCtrlEntry.setIndexNames(
    (0, "ES1200-MIB", "swL2PortCtrlUnitIndex"),
    (0, "ES1200-MIB", "swL2PortCtrlModuleIndex"),
    (0, "ES1200-MIB", "swL2PortCtrlIndex"),
)
if mibBuilder.loadTexts:
    swL2PortCtrlEntry.setStatus("mandatory")
_SwL2PortCtrlUnitIndex_Type = Integer32
_SwL2PortCtrlUnitIndex_Object = MibTableColumn
swL2PortCtrlUnitIndex = _SwL2PortCtrlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 1),
    _SwL2PortCtrlUnitIndex_Type()
)
swL2PortCtrlUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlUnitIndex.setStatus("mandatory")
_SwL2PortCtrlModuleIndex_Type = Integer32
_SwL2PortCtrlModuleIndex_Object = MibTableColumn
swL2PortCtrlModuleIndex = _SwL2PortCtrlModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 2),
    _SwL2PortCtrlModuleIndex_Type()
)
swL2PortCtrlModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlModuleIndex.setStatus("mandatory")
_SwL2PortCtrlIndex_Type = Integer32
_SwL2PortCtrlIndex_Object = MibTableColumn
swL2PortCtrlIndex = _SwL2PortCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 3),
    _SwL2PortCtrlIndex_Type()
)
swL2PortCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlIndex.setStatus("mandatory")


class _SwL2PortCtrlAdminState_Type(Integer32):
    """Custom type swL2PortCtrlAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2PortCtrlAdminState_Type.__name__ = "Integer32"
_SwL2PortCtrlAdminState_Object = MibTableColumn
swL2PortCtrlAdminState = _SwL2PortCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 4),
    _SwL2PortCtrlAdminState_Type()
)
swL2PortCtrlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlAdminState.setStatus("mandatory")


class _SwL2PortCtrlLinkStatusAlarmState_Type(Integer32):
    """Custom type swL2PortCtrlLinkStatusAlarmState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2PortCtrlLinkStatusAlarmState_Type.__name__ = "Integer32"
_SwL2PortCtrlLinkStatusAlarmState_Object = MibTableColumn
swL2PortCtrlLinkStatusAlarmState = _SwL2PortCtrlLinkStatusAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 5),
    _SwL2PortCtrlLinkStatusAlarmState_Type()
)
swL2PortCtrlLinkStatusAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlLinkStatusAlarmState.setStatus("mandatory")


class _SwL2PortCtrlNwayState_Type(Integer32):
    """Custom type swL2PortCtrlNwayState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 10),
          ("nway-disabled-100Mbps-Full", 6),
          ("nway-disabled-100Mbps-Half", 5),
          ("nway-disabled-10Mbps-Full", 4),
          ("nway-disabled-10Mbps-Half", 3),
          ("nway-disabled-1Gigabps-Full", 8),
          ("nway-disabled-1Gigabps-Half", 7),
          ("nway-enabled", 2),
          ("other", 1))
    )


_SwL2PortCtrlNwayState_Type.__name__ = "Integer32"
_SwL2PortCtrlNwayState_Object = MibTableColumn
swL2PortCtrlNwayState = _SwL2PortCtrlNwayState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 6),
    _SwL2PortCtrlNwayState_Type()
)
swL2PortCtrlNwayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlNwayState.setStatus("mandatory")


class _SwL2PortCtrlFlowCtrlState_Type(Integer32):
    """Custom type swL2PortCtrlFlowCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2PortCtrlFlowCtrlState_Type.__name__ = "Integer32"
_SwL2PortCtrlFlowCtrlState_Object = MibTableColumn
swL2PortCtrlFlowCtrlState = _SwL2PortCtrlFlowCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 7),
    _SwL2PortCtrlFlowCtrlState_Type()
)
swL2PortCtrlFlowCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlFlowCtrlState.setStatus("mandatory")


class _SwL2PortCtrlBackPressState_Type(Integer32):
    """Custom type swL2PortCtrlBackPressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2PortCtrlBackPressState_Type.__name__ = "Integer32"
_SwL2PortCtrlBackPressState_Object = MibTableColumn
swL2PortCtrlBackPressState = _SwL2PortCtrlBackPressState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 8),
    _SwL2PortCtrlBackPressState_Type()
)
swL2PortCtrlBackPressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlBackPressState.setStatus("mandatory")


class _SwL2PortCtrlLockState_Type(Integer32):
    """Custom type swL2PortCtrlLockState based on Integer32"""
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
        *(("disable", 2),
          ("enable", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2PortCtrlLockState_Type.__name__ = "Integer32"
_SwL2PortCtrlLockState_Object = MibTableColumn
swL2PortCtrlLockState = _SwL2PortCtrlLockState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 9),
    _SwL2PortCtrlLockState_Type()
)
swL2PortCtrlLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlLockState.setStatus("mandatory")


class _SwL2PortCtrlPriority_Type(Integer32):
    """Custom type swL2PortCtrlPriority based on Integer32"""
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
        *(("default", 2),
          ("force-high-priority", 4),
          ("force-low-priority", 3),
          ("notAvailable", 5),
          ("other", 1))
    )


_SwL2PortCtrlPriority_Type.__name__ = "Integer32"
_SwL2PortCtrlPriority_Object = MibTableColumn
swL2PortCtrlPriority = _SwL2PortCtrlPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 10),
    _SwL2PortCtrlPriority_Type()
)
swL2PortCtrlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlPriority.setStatus("mandatory")


class _SwL2PortCtrlStpState_Type(Integer32):
    """Custom type swL2PortCtrlStpState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2PortCtrlStpState_Type.__name__ = "Integer32"
_SwL2PortCtrlStpState_Object = MibTableColumn
swL2PortCtrlStpState = _SwL2PortCtrlStpState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 11),
    _SwL2PortCtrlStpState_Type()
)
swL2PortCtrlStpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlStpState.setStatus("mandatory")


class _SwL2PortCtrlHOLState_Type(Integer32):
    """Custom type swL2PortCtrlHOLState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2PortCtrlHOLState_Type.__name__ = "Integer32"
_SwL2PortCtrlHOLState_Object = MibTableColumn
swL2PortCtrlHOLState = _SwL2PortCtrlHOLState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 12),
    _SwL2PortCtrlHOLState_Type()
)
swL2PortCtrlHOLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlHOLState.setStatus("mandatory")


class _SwL2PortCtrlBcastRisingAct_Type(Integer32):
    """Custom type swL2PortCtrlBcastRisingAct based on Integer32"""
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
        *(("blocking", 3),
          ("blocking-trap", 4),
          ("do-nothing", 2),
          ("notAvailable", 5),
          ("other", 1))
    )


_SwL2PortCtrlBcastRisingAct_Type.__name__ = "Integer32"
_SwL2PortCtrlBcastRisingAct_Object = MibTableColumn
swL2PortCtrlBcastRisingAct = _SwL2PortCtrlBcastRisingAct_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 13),
    _SwL2PortCtrlBcastRisingAct_Type()
)
swL2PortCtrlBcastRisingAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlBcastRisingAct.setStatus("mandatory")


class _SwL2PortCtrlBcastFallingAct_Type(Integer32):
    """Custom type swL2PortCtrlBcastFallingAct based on Integer32"""
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
        *(("do-nothing", 2),
          ("forwarding", 3),
          ("forwarding-trap", 4),
          ("notAvailable", 5),
          ("other", 1))
    )


_SwL2PortCtrlBcastFallingAct_Type.__name__ = "Integer32"
_SwL2PortCtrlBcastFallingAct_Object = MibTableColumn
swL2PortCtrlBcastFallingAct = _SwL2PortCtrlBcastFallingAct_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 2, 1, 14),
    _SwL2PortCtrlBcastFallingAct_Type()
)
swL2PortCtrlBcastFallingAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlBcastFallingAct.setStatus("mandatory")
_SwL2PortStTable_Object = MibTable
swL2PortStTable = _SwL2PortStTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3)
)
if mibBuilder.loadTexts:
    swL2PortStTable.setStatus("mandatory")
_SwL2PortStEntry_Object = MibTableRow
swL2PortStEntry = _SwL2PortStEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1)
)
swL2PortStEntry.setIndexNames(
    (0, "ES1200-MIB", "swL2PortStUnitIndex"),
    (0, "ES1200-MIB", "swL2PortStModuleIndex"),
    (0, "ES1200-MIB", "swL2PortStIndex"),
)
if mibBuilder.loadTexts:
    swL2PortStEntry.setStatus("mandatory")
_SwL2PortStUnitIndex_Type = Integer32
_SwL2PortStUnitIndex_Object = MibTableColumn
swL2PortStUnitIndex = _SwL2PortStUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 1),
    _SwL2PortStUnitIndex_Type()
)
swL2PortStUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStUnitIndex.setStatus("mandatory")
_SwL2PortStModuleIndex_Type = Integer32
_SwL2PortStModuleIndex_Object = MibTableColumn
swL2PortStModuleIndex = _SwL2PortStModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 2),
    _SwL2PortStModuleIndex_Type()
)
swL2PortStModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStModuleIndex.setStatus("mandatory")
_SwL2PortStIndex_Type = Integer32
_SwL2PortStIndex_Object = MibTableColumn
swL2PortStIndex = _SwL2PortStIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 3),
    _SwL2PortStIndex_Type()
)
swL2PortStIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStIndex.setStatus("mandatory")
_SwL2PortStByteRx_Type = Counter32
_SwL2PortStByteRx_Object = MibTableColumn
swL2PortStByteRx = _SwL2PortStByteRx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 4),
    _SwL2PortStByteRx_Type()
)
swL2PortStByteRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStByteRx.setStatus("mandatory")
_SwL2PortStByteTx_Type = Counter32
_SwL2PortStByteTx_Object = MibTableColumn
swL2PortStByteTx = _SwL2PortStByteTx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 5),
    _SwL2PortStByteTx_Type()
)
swL2PortStByteTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStByteTx.setStatus("mandatory")
_SwL2PortStFrameRx_Type = Counter32
_SwL2PortStFrameRx_Object = MibTableColumn
swL2PortStFrameRx = _SwL2PortStFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 6),
    _SwL2PortStFrameRx_Type()
)
swL2PortStFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrameRx.setStatus("mandatory")
_SwL2PortStFrameTx_Type = Counter32
_SwL2PortStFrameTx_Object = MibTableColumn
swL2PortStFrameTx = _SwL2PortStFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 7),
    _SwL2PortStFrameTx_Type()
)
swL2PortStFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrameTx.setStatus("mandatory")
_SwL2PortStTotalBytesRx_Type = Counter32
_SwL2PortStTotalBytesRx_Object = MibTableColumn
swL2PortStTotalBytesRx = _SwL2PortStTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 8),
    _SwL2PortStTotalBytesRx_Type()
)
swL2PortStTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStTotalBytesRx.setStatus("mandatory")
_SwL2PortStTotalFramesRx_Type = Counter32
_SwL2PortStTotalFramesRx_Object = MibTableColumn
swL2PortStTotalFramesRx = _SwL2PortStTotalFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 9),
    _SwL2PortStTotalFramesRx_Type()
)
swL2PortStTotalFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStTotalFramesRx.setStatus("mandatory")
_SwL2PortStBroadcastFramesRx_Type = Counter32
_SwL2PortStBroadcastFramesRx_Object = MibTableColumn
swL2PortStBroadcastFramesRx = _SwL2PortStBroadcastFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 10),
    _SwL2PortStBroadcastFramesRx_Type()
)
swL2PortStBroadcastFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStBroadcastFramesRx.setStatus("mandatory")
_SwL2PortStMulticastFramesRx_Type = Counter32
_SwL2PortStMulticastFramesRx_Object = MibTableColumn
swL2PortStMulticastFramesRx = _SwL2PortStMulticastFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 11),
    _SwL2PortStMulticastFramesRx_Type()
)
swL2PortStMulticastFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStMulticastFramesRx.setStatus("mandatory")
_SwL2PortStCRCError_Type = Counter32
_SwL2PortStCRCError_Object = MibTableColumn
swL2PortStCRCError = _SwL2PortStCRCError_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 12),
    _SwL2PortStCRCError_Type()
)
swL2PortStCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStCRCError.setStatus("mandatory")
_SwL2PortStOversizeFrames_Type = Counter32
_SwL2PortStOversizeFrames_Object = MibTableColumn
swL2PortStOversizeFrames = _SwL2PortStOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 13),
    _SwL2PortStOversizeFrames_Type()
)
swL2PortStOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStOversizeFrames.setStatus("mandatory")
_SwL2PortStFragments_Type = Counter32
_SwL2PortStFragments_Object = MibTableColumn
swL2PortStFragments = _SwL2PortStFragments_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 14),
    _SwL2PortStFragments_Type()
)
swL2PortStFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFragments.setStatus("mandatory")
_SwL2PortStJabber_Type = Counter32
_SwL2PortStJabber_Object = MibTableColumn
swL2PortStJabber = _SwL2PortStJabber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 15),
    _SwL2PortStJabber_Type()
)
swL2PortStJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStJabber.setStatus("mandatory")
_SwL2PortStCollision_Type = Counter32
_SwL2PortStCollision_Object = MibTableColumn
swL2PortStCollision = _SwL2PortStCollision_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 16),
    _SwL2PortStCollision_Type()
)
swL2PortStCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStCollision.setStatus("mandatory")
_SwL2PortStLateCollision_Type = Counter32
_SwL2PortStLateCollision_Object = MibTableColumn
swL2PortStLateCollision = _SwL2PortStLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 17),
    _SwL2PortStLateCollision_Type()
)
swL2PortStLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStLateCollision.setStatus("mandatory")
_SwL2PortStFrames_64_bytes_Type = Counter32
_SwL2PortStFrames_64_bytes_Object = MibScalar
swL2PortStFrames_64_bytes = _SwL2PortStFrames_64_bytes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 18),
    _SwL2PortStFrames_64_bytes_Type()
)
swL2PortStFrames_64_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrames_64_bytes.setStatus("mandatory")
_SwL2PortStFrames_65_127_bytes_Type = Counter32
_SwL2PortStFrames_65_127_bytes_Object = MibScalar
swL2PortStFrames_65_127_bytes = _SwL2PortStFrames_65_127_bytes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 19),
    _SwL2PortStFrames_65_127_bytes_Type()
)
swL2PortStFrames_65_127_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrames_65_127_bytes.setStatus("mandatory")
_SwL2PortStFrames_128_255_bytes_Type = Counter32
_SwL2PortStFrames_128_255_bytes_Object = MibScalar
swL2PortStFrames_128_255_bytes = _SwL2PortStFrames_128_255_bytes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 20),
    _SwL2PortStFrames_128_255_bytes_Type()
)
swL2PortStFrames_128_255_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrames_128_255_bytes.setStatus("mandatory")
_SwL2PortStFrames_256_511_bytes_Type = Counter32
_SwL2PortStFrames_256_511_bytes_Object = MibScalar
swL2PortStFrames_256_511_bytes = _SwL2PortStFrames_256_511_bytes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 21),
    _SwL2PortStFrames_256_511_bytes_Type()
)
swL2PortStFrames_256_511_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrames_256_511_bytes.setStatus("mandatory")
_SwL2PortStFrames_512_1023_bytes_Type = Counter32
_SwL2PortStFrames_512_1023_bytes_Object = MibScalar
swL2PortStFrames_512_1023_bytes = _SwL2PortStFrames_512_1023_bytes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 22),
    _SwL2PortStFrames_512_1023_bytes_Type()
)
swL2PortStFrames_512_1023_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrames_512_1023_bytes.setStatus("mandatory")
_SwL2PortStFrames_1024_1536_bytes_Type = Counter32
_SwL2PortStFrames_1024_1536_bytes_Object = MibScalar
swL2PortStFrames_1024_1536_bytes = _SwL2PortStFrames_1024_1536_bytes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 23),
    _SwL2PortStFrames_1024_1536_bytes_Type()
)
swL2PortStFrames_1024_1536_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFrames_1024_1536_bytes.setStatus("mandatory")
_SwL2PortStFramesDroppedFrames_Type = Counter32
_SwL2PortStFramesDroppedFrames_Object = MibTableColumn
swL2PortStFramesDroppedFrames = _SwL2PortStFramesDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 24),
    _SwL2PortStFramesDroppedFrames_Type()
)
swL2PortStFramesDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStFramesDroppedFrames.setStatus("mandatory")
_SwL2PortStMulticastFramesTx_Type = Counter32
_SwL2PortStMulticastFramesTx_Object = MibTableColumn
swL2PortStMulticastFramesTx = _SwL2PortStMulticastFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 25),
    _SwL2PortStMulticastFramesTx_Type()
)
swL2PortStMulticastFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStMulticastFramesTx.setStatus("mandatory")
_SwL2PortStBroadcastFramesTx_Type = Counter32
_SwL2PortStBroadcastFramesTx_Object = MibTableColumn
swL2PortStBroadcastFramesTx = _SwL2PortStBroadcastFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 26),
    _SwL2PortStBroadcastFramesTx_Type()
)
swL2PortStBroadcastFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStBroadcastFramesTx.setStatus("mandatory")
_SwL2PortStUndersizeFrames_Type = Counter32
_SwL2PortStUndersizeFrames_Object = MibTableColumn
swL2PortStUndersizeFrames = _SwL2PortStUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 4, 3, 1, 27),
    _SwL2PortStUndersizeFrames_Type()
)
swL2PortStUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStUndersizeFrames.setStatus("mandatory")
_SwPortSniff_ObjectIdentity = ObjectIdentity
swPortSniff = _SwPortSniff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 5)
)
_SwSniffCtrlTable_Object = MibTable
swSniffCtrlTable = _SwSniffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 5, 1)
)
if mibBuilder.loadTexts:
    swSniffCtrlTable.setStatus("mandatory")
_SwSniffCtrlEntry_Object = MibTableRow
swSniffCtrlEntry = _SwSniffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 5, 1, 1)
)
swSniffCtrlEntry.setIndexNames(
    (0, "ES1200-MIB", "swSniffIndex"),
)
if mibBuilder.loadTexts:
    swSniffCtrlEntry.setStatus("mandatory")
_SwSniffIndex_Type = Integer32
_SwSniffIndex_Object = MibTableColumn
swSniffIndex = _SwSniffIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 5, 1, 1, 1),
    _SwSniffIndex_Type()
)
swSniffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSniffIndex.setStatus("mandatory")


class _SwSniffSourcePort_Type(Integer32):
    """Custom type swSniffSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SwSniffSourcePort_Type.__name__ = "Integer32"
_SwSniffSourcePort_Object = MibTableColumn
swSniffSourcePort = _SwSniffSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 5, 1, 1, 2),
    _SwSniffSourcePort_Type()
)
swSniffSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSniffSourcePort.setStatus("mandatory")


class _SwSniffTargetPort_Type(Integer32):
    """Custom type swSniffTargetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SwSniffTargetPort_Type.__name__ = "Integer32"
_SwSniffTargetPort_Object = MibTableColumn
swSniffTargetPort = _SwSniffTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 5, 1, 1, 3),
    _SwSniffTargetPort_Type()
)
swSniffTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSniffTargetPort.setStatus("mandatory")


class _SwSniffState_Type(Integer32):
    """Custom type swSniffState based on Integer32"""
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
          ("enable", 3),
          ("other", 1))
    )


_SwSniffState_Type.__name__ = "Integer32"
_SwSniffState_Object = MibTableColumn
swSniffState = _SwSniffState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 5, 1, 1, 4),
    _SwSniffState_Type()
)
swSniffState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSniffState.setStatus("mandatory")
_SwPortTrunk_ObjectIdentity = ObjectIdentity
swPortTrunk = _SwPortTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6)
)
_SwPortTrunkCtrlTable_Object = MibTable
swPortTrunkCtrlTable = _SwPortTrunkCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 1)
)
if mibBuilder.loadTexts:
    swPortTrunkCtrlTable.setStatus("mandatory")
_SwPortTrunkCtrlEntry_Object = MibTableRow
swPortTrunkCtrlEntry = _SwPortTrunkCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 1, 1)
)
swPortTrunkCtrlEntry.setIndexNames(
    (0, "ES1200-MIB", "swPortTrunkCtrlIndex"),
)
if mibBuilder.loadTexts:
    swPortTrunkCtrlEntry.setStatus("mandatory")
_SwPortTrunkCtrlIndex_Type = Integer32
_SwPortTrunkCtrlIndex_Object = MibTableColumn
swPortTrunkCtrlIndex = _SwPortTrunkCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 1, 1, 1),
    _SwPortTrunkCtrlIndex_Type()
)
swPortTrunkCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkCtrlIndex.setStatus("mandatory")
_SwPortTrunkCtrlAnchorPort_Type = Integer32
_SwPortTrunkCtrlAnchorPort_Object = MibTableColumn
swPortTrunkCtrlAnchorPort = _SwPortTrunkCtrlAnchorPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 1, 1, 2),
    _SwPortTrunkCtrlAnchorPort_Type()
)
swPortTrunkCtrlAnchorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkCtrlAnchorPort.setStatus("mandatory")
_SwPortTrunkCtrlMasterPort_Type = Integer32
_SwPortTrunkCtrlMasterPort_Object = MibTableColumn
swPortTrunkCtrlMasterPort = _SwPortTrunkCtrlMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 1, 1, 3),
    _SwPortTrunkCtrlMasterPort_Type()
)
swPortTrunkCtrlMasterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkCtrlMasterPort.setStatus("mandatory")


class _SwPortTrunkCtrlName_Type(DisplayString):
    """Custom type swPortTrunkCtrlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwPortTrunkCtrlName_Type.__name__ = "DisplayString"
_SwPortTrunkCtrlName_Object = MibTableColumn
swPortTrunkCtrlName = _SwPortTrunkCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 1, 1, 4),
    _SwPortTrunkCtrlName_Type()
)
swPortTrunkCtrlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkCtrlName.setStatus("mandatory")
_SwPortTrunkCtrlMember_Type = PortList
_SwPortTrunkCtrlMember_Object = MibTableColumn
swPortTrunkCtrlMember = _SwPortTrunkCtrlMember_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 1, 1, 5),
    _SwPortTrunkCtrlMember_Type()
)
swPortTrunkCtrlMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkCtrlMember.setStatus("mandatory")


class _SwPortTrunkCtrlState_Type(Integer32):
    """Custom type swPortTrunkCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwPortTrunkCtrlState_Type.__name__ = "Integer32"
_SwPortTrunkCtrlState_Object = MibTableColumn
swPortTrunkCtrlState = _SwPortTrunkCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 1, 1, 6),
    _SwPortTrunkCtrlState_Type()
)
swPortTrunkCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkCtrlState.setStatus("mandatory")
_SwPortTrunkMemberTable_Object = MibTable
swPortTrunkMemberTable = _SwPortTrunkMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 2)
)
if mibBuilder.loadTexts:
    swPortTrunkMemberTable.setStatus("mandatory")
_SwPortTrunkMemberEntry_Object = MibTableRow
swPortTrunkMemberEntry = _SwPortTrunkMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 2, 1)
)
swPortTrunkMemberEntry.setIndexNames(
    (0, "ES1200-MIB", "swPortTrunkMemberIndex"),
    (0, "ES1200-MIB", "swPortTrunkMemberUnitIndex"),
    (0, "ES1200-MIB", "swPortTrunkMemberModuleIndex"),
    (0, "ES1200-MIB", "swPortTrunkMemberPortIndex"),
)
if mibBuilder.loadTexts:
    swPortTrunkMemberEntry.setStatus("mandatory")
_SwPortTrunkMemberIndex_Type = Integer32
_SwPortTrunkMemberIndex_Object = MibTableColumn
swPortTrunkMemberIndex = _SwPortTrunkMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 2, 1, 1),
    _SwPortTrunkMemberIndex_Type()
)
swPortTrunkMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMemberIndex.setStatus("mandatory")
_SwPortTrunkMemberUnitIndex_Type = Integer32
_SwPortTrunkMemberUnitIndex_Object = MibTableColumn
swPortTrunkMemberUnitIndex = _SwPortTrunkMemberUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 2, 1, 2),
    _SwPortTrunkMemberUnitIndex_Type()
)
swPortTrunkMemberUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMemberUnitIndex.setStatus("mandatory")
_SwPortTrunkMemberModuleIndex_Type = Integer32
_SwPortTrunkMemberModuleIndex_Object = MibTableColumn
swPortTrunkMemberModuleIndex = _SwPortTrunkMemberModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 2, 1, 3),
    _SwPortTrunkMemberModuleIndex_Type()
)
swPortTrunkMemberModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMemberModuleIndex.setStatus("mandatory")
_SwPortTrunkMemberPortIndex_Type = Integer32
_SwPortTrunkMemberPortIndex_Object = MibTableColumn
swPortTrunkMemberPortIndex = _SwPortTrunkMemberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 6, 2, 1, 4),
    _SwPortTrunkMemberPortIndex_Type()
)
swPortTrunkMemberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMemberPortIndex.setStatus("mandatory")
_SwIGMP_ObjectIdentity = ObjectIdentity
swIGMP = _SwIGMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7)
)
_SwIGMPCtrl_ObjectIdentity = ObjectIdentity
swIGMPCtrl = _SwIGMPCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 1)
)


class _SwIGMPAdminState_Type(Integer32):
    """Custom type swIGMPAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwIGMPAdminState_Type.__name__ = "Integer32"
_SwIGMPAdminState_Object = MibScalar
swIGMPAdminState = _SwIGMPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 1, 1),
    _SwIGMPAdminState_Type()
)
swIGMPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPAdminState.setStatus("mandatory")


class _SwIGMPTimeout_Type(Integer32):
    """Custom type swIGMPTimeout based on Integer32"""
    defaultValue = 300


_SwIGMPTimeout_Object = MibScalar
swIGMPTimeout = _SwIGMPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 1, 2),
    _SwIGMPTimeout_Type()
)
swIGMPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPTimeout.setStatus("mandatory")
_SwIGMPInfoTable_Object = MibTable
swIGMPInfoTable = _SwIGMPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 2)
)
if mibBuilder.loadTexts:
    swIGMPInfoTable.setStatus("mandatory")
_SwIGMPInfoEntry_Object = MibTableRow
swIGMPInfoEntry = _SwIGMPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 2, 1)
)
swIGMPInfoEntry.setIndexNames(
    (0, "ES1200-MIB", "swIGMPInfoIndex"),
)
if mibBuilder.loadTexts:
    swIGMPInfoEntry.setStatus("mandatory")


class _SwIGMPInfoIndex_Type(Integer32):
    """Custom type swIGMPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SwIGMPInfoIndex_Type.__name__ = "Integer32"
_SwIGMPInfoIndex_Object = MibTableColumn
swIGMPInfoIndex = _SwIGMPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 2, 1, 1),
    _SwIGMPInfoIndex_Type()
)
swIGMPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoIndex.setStatus("mandatory")
_SwIGMPInfoVid_Type = Integer32
_SwIGMPInfoVid_Object = MibTableColumn
swIGMPInfoVid = _SwIGMPInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 2, 1, 2),
    _SwIGMPInfoVid_Type()
)
swIGMPInfoVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoVid.setStatus("mandatory")
_SwIGMPInfoQueryCount_Type = Integer32
_SwIGMPInfoQueryCount_Object = MibTableColumn
swIGMPInfoQueryCount = _SwIGMPInfoQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 2, 1, 3),
    _SwIGMPInfoQueryCount_Type()
)
swIGMPInfoQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoQueryCount.setStatus("mandatory")
_SwIGMPInfoTxQueryCount_Type = Integer32
_SwIGMPInfoTxQueryCount_Object = MibTableColumn
swIGMPInfoTxQueryCount = _SwIGMPInfoTxQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 2, 1, 4),
    _SwIGMPInfoTxQueryCount_Type()
)
swIGMPInfoTxQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoTxQueryCount.setStatus("mandatory")
_SwIGMPTable_Object = MibTable
swIGMPTable = _SwIGMPTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 3)
)
if mibBuilder.loadTexts:
    swIGMPTable.setStatus("mandatory")
_SwIGMPEntry_Object = MibTableRow
swIGMPEntry = _SwIGMPEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 3, 1)
)
swIGMPEntry.setIndexNames(
    (0, "ES1200-MIB", "swIGMPVid"),
    (0, "ES1200-MIB", "swIGMPGroupIpAddr"),
)
if mibBuilder.loadTexts:
    swIGMPEntry.setStatus("mandatory")
_SwIGMPVid_Type = Integer32
_SwIGMPVid_Object = MibTableColumn
swIGMPVid = _SwIGMPVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 3, 1, 1),
    _SwIGMPVid_Type()
)
swIGMPVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPVid.setStatus("mandatory")
_SwIGMPGroupIpAddr_Type = IpAddress
_SwIGMPGroupIpAddr_Object = MibTableColumn
swIGMPGroupIpAddr = _SwIGMPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 3, 1, 2),
    _SwIGMPGroupIpAddr_Type()
)
swIGMPGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPGroupIpAddr.setStatus("mandatory")
_SwIGMPGroupMacAddr_Type = MacAddress
_SwIGMPGroupMacAddr_Object = MibTableColumn
swIGMPGroupMacAddr = _SwIGMPGroupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 3, 1, 3),
    _SwIGMPGroupMacAddr_Type()
)
swIGMPGroupMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPGroupMacAddr.setStatus("mandatory")
_SwIGMPPortMap_Type = PortList
_SwIGMPPortMap_Object = MibTableColumn
swIGMPPortMap = _SwIGMPPortMap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 3, 1, 4),
    _SwIGMPPortMap_Type()
)
swIGMPPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPPortMap.setStatus("mandatory")
_SwIGMPIpGroupReportCount_Type = Integer32
_SwIGMPIpGroupReportCount_Object = MibTableColumn
swIGMPIpGroupReportCount = _SwIGMPIpGroupReportCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 3, 1, 5),
    _SwIGMPIpGroupReportCount_Type()
)
swIGMPIpGroupReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPIpGroupReportCount.setStatus("mandatory")
_SwIGMPCtrlTable_Object = MibTable
swIGMPCtrlTable = _SwIGMPCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 4)
)
if mibBuilder.loadTexts:
    swIGMPCtrlTable.setStatus("mandatory")
_SwIGMPCtrlEntry_Object = MibTableRow
swIGMPCtrlEntry = _SwIGMPCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 4, 1)
)
swIGMPCtrlEntry.setIndexNames(
    (0, "ES1200-MIB", "swIGMPCtrlIndex"),
)
if mibBuilder.loadTexts:
    swIGMPCtrlEntry.setStatus("mandatory")


class _SwIGMPCtrlIndex_Type(Integer32):
    """Custom type swIGMPCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SwIGMPCtrlIndex_Type.__name__ = "Integer32"
_SwIGMPCtrlIndex_Object = MibTableColumn
swIGMPCtrlIndex = _SwIGMPCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 4, 1, 1),
    _SwIGMPCtrlIndex_Type()
)
swIGMPCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPCtrlIndex.setStatus("mandatory")


class _SwIGMPCtrlVid_Type(Integer32):
    """Custom type swIGMPCtrlVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwIGMPCtrlVid_Type.__name__ = "Integer32"
_SwIGMPCtrlVid_Object = MibTableColumn
swIGMPCtrlVid = _SwIGMPCtrlVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 4, 1, 2),
    _SwIGMPCtrlVid_Type()
)
swIGMPCtrlVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPCtrlVid.setStatus("mandatory")


class _SwIGMPCtrlTimer_Type(Integer32):
    """Custom type swIGMPCtrlTimer based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 9999),
    )


_SwIGMPCtrlTimer_Type.__name__ = "Integer32"
_SwIGMPCtrlTimer_Object = MibTableColumn
swIGMPCtrlTimer = _SwIGMPCtrlTimer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 4, 1, 3),
    _SwIGMPCtrlTimer_Type()
)
swIGMPCtrlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPCtrlTimer.setStatus("mandatory")


class _SwIGMPCtrlState_Type(Integer32):
    """Custom type swIGMPCtrlState based on Integer32"""
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
        *(("deleted", 4),
          ("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwIGMPCtrlState_Type.__name__ = "Integer32"
_SwIGMPCtrlState_Object = MibTableColumn
swIGMPCtrlState = _SwIGMPCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 7, 4, 1, 4),
    _SwIGMPCtrlState_Type()
)
swIGMPCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPCtrlState.setStatus("mandatory")
_SwVlan_ObjectIdentity = ObjectIdentity
swVlan = _SwVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8)
)
_SwVlanCtrl_ObjectIdentity = ObjectIdentity
swVlanCtrl = _SwVlanCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 1)
)


class _SwVlanCtrlMode_Type(Integer32):
    """Custom type swVlanCtrlMode based on Integer32"""
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
        *(("disabled", 2),
          ("ieee8021q", 4),
          ("mac-base", 3),
          ("other", 1),
          ("port-base", 5))
    )


_SwVlanCtrlMode_Type.__name__ = "Integer32"
_SwVlanCtrlMode_Object = MibScalar
swVlanCtrlMode = _SwVlanCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 1, 1),
    _SwVlanCtrlMode_Type()
)
swVlanCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swVlanCtrlMode.setStatus("mandatory")


class _SwVlanInfoStatus_Type(Integer32):
    """Custom type swVlanInfoStatus based on Integer32"""
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
        *(("disabled", 2),
          ("ieee8021q", 4),
          ("mac-base", 3),
          ("other", 1))
    )


_SwVlanInfoStatus_Type.__name__ = "Integer32"
_SwVlanInfoStatus_Object = MibScalar
swVlanInfoStatus = _SwVlanInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 1, 2),
    _SwVlanInfoStatus_Type()
)
swVlanInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVlanInfoStatus.setStatus("mandatory")
_SwVlanSnmpPortVlan_Type = VlanIndex
_SwVlanSnmpPortVlan_Object = MibScalar
swVlanSnmpPortVlan = _SwVlanSnmpPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 1, 3),
    _SwVlanSnmpPortVlan_Type()
)
swVlanSnmpPortVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swVlanSnmpPortVlan.setStatus("mandatory")
_SwMacBaseVlan_ObjectIdentity = ObjectIdentity
swMacBaseVlan = _SwMacBaseVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2)
)
_SwMacBaseVlanInfo_ObjectIdentity = ObjectIdentity
swMacBaseVlanInfo = _SwMacBaseVlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 1)
)
_SwMacBaseVlanMaxNum_Type = Integer32
_SwMacBaseVlanMaxNum_Object = MibScalar
swMacBaseVlanMaxNum = _SwMacBaseVlanMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 1, 1),
    _SwMacBaseVlanMaxNum_Type()
)
swMacBaseVlanMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBaseVlanMaxNum.setStatus("mandatory")
_SwMacBaseVlanAddrMaxNum_Type = Integer32
_SwMacBaseVlanAddrMaxNum_Object = MibScalar
swMacBaseVlanAddrMaxNum = _SwMacBaseVlanAddrMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 1, 2),
    _SwMacBaseVlanAddrMaxNum_Type()
)
swMacBaseVlanAddrMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBaseVlanAddrMaxNum.setStatus("mandatory")
_SwMacBaseVlanCtrlTable_Object = MibTable
swMacBaseVlanCtrlTable = _SwMacBaseVlanCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 2)
)
if mibBuilder.loadTexts:
    swMacBaseVlanCtrlTable.setStatus("mandatory")
_SwMacBaseVlanCtrlEntry_Object = MibTableRow
swMacBaseVlanCtrlEntry = _SwMacBaseVlanCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 2, 1)
)
swMacBaseVlanCtrlEntry.setIndexNames(
    (0, "ES1200-MIB", "swMacBaseVlanDesc"),
)
if mibBuilder.loadTexts:
    swMacBaseVlanCtrlEntry.setStatus("mandatory")


class _SwMacBaseVlanDesc_Type(DisplayString):
    """Custom type swMacBaseVlanDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwMacBaseVlanDesc_Type.__name__ = "DisplayString"
_SwMacBaseVlanDesc_Object = MibTableColumn
swMacBaseVlanDesc = _SwMacBaseVlanDesc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 2, 1, 1),
    _SwMacBaseVlanDesc_Type()
)
swMacBaseVlanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBaseVlanDesc.setStatus("mandatory")
_SwMacBaseVlanMacMember_Type = Integer32
_SwMacBaseVlanMacMember_Object = MibTableColumn
swMacBaseVlanMacMember = _SwMacBaseVlanMacMember_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 2, 1, 2),
    _SwMacBaseVlanMacMember_Type()
)
swMacBaseVlanMacMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBaseVlanMacMember.setStatus("mandatory")


class _SwMacBaseVlanCtrlState_Type(Integer32):
    """Custom type swMacBaseVlanCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwMacBaseVlanCtrlState_Type.__name__ = "Integer32"
_SwMacBaseVlanCtrlState_Object = MibTableColumn
swMacBaseVlanCtrlState = _SwMacBaseVlanCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 2, 1, 3),
    _SwMacBaseVlanCtrlState_Type()
)
swMacBaseVlanCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBaseVlanCtrlState.setStatus("mandatory")
_SwMacBaseVlanAddrTable_Object = MibTable
swMacBaseVlanAddrTable = _SwMacBaseVlanAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 3)
)
if mibBuilder.loadTexts:
    swMacBaseVlanAddrTable.setStatus("mandatory")
_SwMacBaseVlanAddrEntry_Object = MibTableRow
swMacBaseVlanAddrEntry = _SwMacBaseVlanAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 3, 1)
)
swMacBaseVlanAddrEntry.setIndexNames(
    (0, "ES1200-MIB", "swMacBaseVlanAddr"),
)
if mibBuilder.loadTexts:
    swMacBaseVlanAddrEntry.setStatus("mandatory")
_SwMacBaseVlanAddr_Type = MacAddress
_SwMacBaseVlanAddr_Object = MibTableColumn
swMacBaseVlanAddr = _SwMacBaseVlanAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 3, 1, 1),
    _SwMacBaseVlanAddr_Type()
)
swMacBaseVlanAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBaseVlanAddr.setStatus("mandatory")


class _SwMacBaseVlanAddrVlanDesc_Type(DisplayString):
    """Custom type swMacBaseVlanAddrVlanDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SwMacBaseVlanAddrVlanDesc_Type.__name__ = "DisplayString"
_SwMacBaseVlanAddrVlanDesc_Object = MibTableColumn
swMacBaseVlanAddrVlanDesc = _SwMacBaseVlanAddrVlanDesc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 3, 1, 2),
    _SwMacBaseVlanAddrVlanDesc_Type()
)
swMacBaseVlanAddrVlanDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBaseVlanAddrVlanDesc.setStatus("mandatory")


class _SwMacBaseVlanAddrState_Type(Integer32):
    """Custom type swMacBaseVlanAddrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwMacBaseVlanAddrState_Type.__name__ = "Integer32"
_SwMacBaseVlanAddrState_Object = MibTableColumn
swMacBaseVlanAddrState = _SwMacBaseVlanAddrState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 3, 1, 3),
    _SwMacBaseVlanAddrState_Type()
)
swMacBaseVlanAddrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBaseVlanAddrState.setStatus("mandatory")


class _SwMacBaseVlanAddrStatus_Type(Integer32):
    """Custom type swMacBaseVlanAddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apply", 2),
          ("not-apply", 3),
          ("other", 1))
    )


_SwMacBaseVlanAddrStatus_Type.__name__ = "Integer32"
_SwMacBaseVlanAddrStatus_Object = MibTableColumn
swMacBaseVlanAddrStatus = _SwMacBaseVlanAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 2, 3, 1, 4),
    _SwMacBaseVlanAddrStatus_Type()
)
swMacBaseVlanAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBaseVlanAddrStatus.setStatus("mandatory")
_SwPortBaseVlan_ObjectIdentity = ObjectIdentity
swPortBaseVlan = _SwPortBaseVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3)
)
_SwPortBaseVlanTotalNum_Type = Integer32
_SwPortBaseVlanTotalNum_Object = MibScalar
swPortBaseVlanTotalNum = _SwPortBaseVlanTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3, 1),
    _SwPortBaseVlanTotalNum_Type()
)
swPortBaseVlanTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanTotalNum.setStatus("mandatory")
_SwPortBaseVlanDefaultVlanTable_Object = MibTable
swPortBaseVlanDefaultVlanTable = _SwPortBaseVlanDefaultVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3, 2)
)
if mibBuilder.loadTexts:
    swPortBaseVlanDefaultVlanTable.setStatus("mandatory")
_SwPortBaseVlanDefaultVlanEntry_Object = MibTableRow
swPortBaseVlanDefaultVlanEntry = _SwPortBaseVlanDefaultVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3, 2, 1)
)
swPortBaseVlanDefaultVlanEntry.setIndexNames(
    (0, "ES1200-MIB", "swPortBaseVlanDefaultPvid"),
)
if mibBuilder.loadTexts:
    swPortBaseVlanDefaultVlanEntry.setStatus("mandatory")
_SwPortBaseVlanDefaultPvid_Type = Integer32
_SwPortBaseVlanDefaultPvid_Object = MibTableColumn
swPortBaseVlanDefaultPvid = _SwPortBaseVlanDefaultPvid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3, 2, 1, 1),
    _SwPortBaseVlanDefaultPvid_Type()
)
swPortBaseVlanDefaultPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanDefaultPvid.setStatus("mandatory")


class _SwPortBaseVlanDefaultDesc_Type(DisplayString):
    """Custom type swPortBaseVlanDefaultDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwPortBaseVlanDefaultDesc_Type.__name__ = "DisplayString"
_SwPortBaseVlanDefaultDesc_Object = MibTableColumn
swPortBaseVlanDefaultDesc = _SwPortBaseVlanDefaultDesc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3, 2, 1, 2),
    _SwPortBaseVlanDefaultDesc_Type()
)
swPortBaseVlanDefaultDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanDefaultDesc.setStatus("mandatory")
_SwPortBaseVlanDefaultPortList_Type = PortList
_SwPortBaseVlanDefaultPortList_Object = MibTableColumn
swPortBaseVlanDefaultPortList = _SwPortBaseVlanDefaultPortList_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3, 2, 1, 3),
    _SwPortBaseVlanDefaultPortList_Type()
)
swPortBaseVlanDefaultPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanDefaultPortList.setStatus("mandatory")
_SwPortBaseVlanDefaultPortNumber_Type = Integer32
_SwPortBaseVlanDefaultPortNumber_Object = MibTableColumn
swPortBaseVlanDefaultPortNumber = _SwPortBaseVlanDefaultPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3, 2, 1, 4),
    _SwPortBaseVlanDefaultPortNumber_Type()
)
swPortBaseVlanDefaultPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanDefaultPortNumber.setStatus("mandatory")
_SwPortBaseVlanConfigTable_Object = MibTable
swPortBaseVlanConfigTable = _SwPortBaseVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3, 3)
)
if mibBuilder.loadTexts:
    swPortBaseVlanConfigTable.setStatus("mandatory")
_SwPortBaseVlanConfigEntry_Object = MibTableRow
swPortBaseVlanConfigEntry = _SwPortBaseVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3, 3, 1)
)
swPortBaseVlanConfigEntry.setIndexNames(
    (0, "ES1200-MIB", "swPortBaseVlanConfigPvid"),
)
if mibBuilder.loadTexts:
    swPortBaseVlanConfigEntry.setStatus("mandatory")


class _SwPortBaseVlanConfigPvid_Type(Integer32):
    """Custom type swPortBaseVlanConfigPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 12),
    )


_SwPortBaseVlanConfigPvid_Type.__name__ = "Integer32"
_SwPortBaseVlanConfigPvid_Object = MibTableColumn
swPortBaseVlanConfigPvid = _SwPortBaseVlanConfigPvid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3, 3, 1, 1),
    _SwPortBaseVlanConfigPvid_Type()
)
swPortBaseVlanConfigPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanConfigPvid.setStatus("mandatory")


class _SwPortBaseVlanConfigDesc_Type(DisplayString):
    """Custom type swPortBaseVlanConfigDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwPortBaseVlanConfigDesc_Type.__name__ = "DisplayString"
_SwPortBaseVlanConfigDesc_Object = MibTableColumn
swPortBaseVlanConfigDesc = _SwPortBaseVlanConfigDesc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3, 3, 1, 2),
    _SwPortBaseVlanConfigDesc_Type()
)
swPortBaseVlanConfigDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortBaseVlanConfigDesc.setStatus("mandatory")
_SwPortBaseVlanConfigPortList_Type = PortList
_SwPortBaseVlanConfigPortList_Object = MibTableColumn
swPortBaseVlanConfigPortList = _SwPortBaseVlanConfigPortList_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3, 3, 1, 3),
    _SwPortBaseVlanConfigPortList_Type()
)
swPortBaseVlanConfigPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortBaseVlanConfigPortList.setStatus("mandatory")
_SwPortBaseVlanConfigPortNumber_Type = Integer32
_SwPortBaseVlanConfigPortNumber_Object = MibTableColumn
swPortBaseVlanConfigPortNumber = _SwPortBaseVlanConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 3, 3, 1, 4),
    _SwPortBaseVlanConfigPortNumber_Type()
)
swPortBaseVlanConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanConfigPortNumber.setStatus("mandatory")
_PBridgeMIBObjects_ObjectIdentity = ObjectIdentity
pBridgeMIBObjects = _PBridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4)
)
_Dot1dExtBase_ObjectIdentity = ObjectIdentity
dot1dExtBase = _Dot1dExtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 1)
)
_Dot1dDeviceCapabilities_Type = Integer32
_Dot1dDeviceCapabilities_Object = MibScalar
dot1dDeviceCapabilities = _Dot1dDeviceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 1, 1),
    _Dot1dDeviceCapabilities_Type()
)
dot1dDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dDeviceCapabilities.setStatus("mandatory")


class _Dot1dTrafficClassesEnabled_Type(TruthValue):
    """Custom type dot1dTrafficClassesEnabled based on TruthValue"""


_Dot1dTrafficClassesEnabled_Object = MibScalar
dot1dTrafficClassesEnabled = _Dot1dTrafficClassesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 1, 2),
    _Dot1dTrafficClassesEnabled_Type()
)
dot1dTrafficClassesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTrafficClassesEnabled.setStatus("mandatory")


class _Dot1dGmrpStatus_Type(EnabledStatus):
    """Custom type dot1dGmrpStatus based on EnabledStatus"""


_Dot1dGmrpStatus_Object = MibScalar
dot1dGmrpStatus = _Dot1dGmrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 1, 3),
    _Dot1dGmrpStatus_Type()
)
dot1dGmrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dGmrpStatus.setStatus("mandatory")
_Dot1dPortCapabilitiesTable_Object = MibTable
dot1dPortCapabilitiesTable = _Dot1dPortCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 1, 4)
)
if mibBuilder.loadTexts:
    dot1dPortCapabilitiesTable.setStatus("mandatory")
_Dot1dPortCapabilitiesEntry_Object = MibTableRow
dot1dPortCapabilitiesEntry = _Dot1dPortCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 1, 4, 1)
)
dot1dPortCapabilitiesEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dot1dPortCapabilitiesEntry.setStatus("mandatory")
_Dot1dPortCapabilities_Type = Integer32
_Dot1dPortCapabilities_Object = MibTableColumn
dot1dPortCapabilities = _Dot1dPortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 1, 4, 1, 1),
    _Dot1dPortCapabilities_Type()
)
dot1dPortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dPortCapabilities.setStatus("mandatory")
_Dot1dPriority_ObjectIdentity = ObjectIdentity
dot1dPriority = _Dot1dPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 2)
)
_Dot1dPortPriorityTable_Object = MibTable
dot1dPortPriorityTable = _Dot1dPortPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dot1dPortPriorityTable.setStatus("mandatory")
_Dot1dPortPriorityEntry_Object = MibTableRow
dot1dPortPriorityEntry = _Dot1dPortPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 2, 1, 1)
)
dot1dPortPriorityEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dot1dPortPriorityEntry.setStatus("mandatory")


class _Dot1dPortNumTrafficClasses_Type(Integer32):
    """Custom type dot1dPortNumTrafficClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Dot1dPortNumTrafficClasses_Type.__name__ = "Integer32"
_Dot1dPortNumTrafficClasses_Object = MibTableColumn
dot1dPortNumTrafficClasses = _Dot1dPortNumTrafficClasses_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 2, 1, 1, 1),
    _Dot1dPortNumTrafficClasses_Type()
)
dot1dPortNumTrafficClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dPortNumTrafficClasses.setStatus("mandatory")
_Dot1dGarp_ObjectIdentity = ObjectIdentity
dot1dGarp = _Dot1dGarp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 3)
)
_Dot1dPortGarpTable_Object = MibTable
dot1dPortGarpTable = _Dot1dPortGarpTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 3, 1)
)
if mibBuilder.loadTexts:
    dot1dPortGarpTable.setStatus("mandatory")
_Dot1dPortGarpEntry_Object = MibTableRow
dot1dPortGarpEntry = _Dot1dPortGarpEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 3, 1, 1)
)
dot1dPortGarpEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dot1dPortGarpEntry.setStatus("mandatory")


class _Dot1dPortGarpJoinTime_Type(TimeInterval):
    """Custom type dot1dPortGarpJoinTime based on TimeInterval"""
    defaultValue = 20

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 65535),
    )


_Dot1dPortGarpJoinTime_Type.__name__ = "TimeInterval"
_Dot1dPortGarpJoinTime_Object = MibTableColumn
dot1dPortGarpJoinTime = _Dot1dPortGarpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 3, 1, 1, 1),
    _Dot1dPortGarpJoinTime_Type()
)
dot1dPortGarpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortGarpJoinTime.setStatus("mandatory")


class _Dot1dPortGarpLeaveTime_Type(TimeInterval):
    """Custom type dot1dPortGarpLeaveTime based on TimeInterval"""
    defaultValue = 60

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 65535),
    )


_Dot1dPortGarpLeaveTime_Type.__name__ = "TimeInterval"
_Dot1dPortGarpLeaveTime_Object = MibTableColumn
dot1dPortGarpLeaveTime = _Dot1dPortGarpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 3, 1, 1, 2),
    _Dot1dPortGarpLeaveTime_Type()
)
dot1dPortGarpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortGarpLeaveTime.setStatus("mandatory")


class _Dot1dPortGarpLeaveAllTime_Type(TimeInterval):
    """Custom type dot1dPortGarpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 65535),
    )


_Dot1dPortGarpLeaveAllTime_Type.__name__ = "TimeInterval"
_Dot1dPortGarpLeaveAllTime_Object = MibTableColumn
dot1dPortGarpLeaveAllTime = _Dot1dPortGarpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 3, 1, 1, 3),
    _Dot1dPortGarpLeaveAllTime_Type()
)
dot1dPortGarpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortGarpLeaveAllTime.setStatus("mandatory")
_Dot1dGmrp_ObjectIdentity = ObjectIdentity
dot1dGmrp = _Dot1dGmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 4)
)
_Dot1dPortGmrpTable_Object = MibTable
dot1dPortGmrpTable = _Dot1dPortGmrpTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 4, 1)
)
if mibBuilder.loadTexts:
    dot1dPortGmrpTable.setStatus("mandatory")
_Dot1dPortGmrpEntry_Object = MibTableRow
dot1dPortGmrpEntry = _Dot1dPortGmrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 4, 1, 1)
)
dot1dPortGmrpEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dot1dPortGmrpEntry.setStatus("mandatory")


class _Dot1dPortGmrpStatus_Type(EnabledStatus):
    """Custom type dot1dPortGmrpStatus based on EnabledStatus"""


_Dot1dPortGmrpStatus_Object = MibTableColumn
dot1dPortGmrpStatus = _Dot1dPortGmrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 4, 1, 1, 1),
    _Dot1dPortGmrpStatus_Type()
)
dot1dPortGmrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortGmrpStatus.setStatus("mandatory")
_Dot1dPortGmrpFailedRegistrations_Type = Counter32
_Dot1dPortGmrpFailedRegistrations_Object = MibTableColumn
dot1dPortGmrpFailedRegistrations = _Dot1dPortGmrpFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 4, 1, 1, 2),
    _Dot1dPortGmrpFailedRegistrations_Type()
)
dot1dPortGmrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dPortGmrpFailedRegistrations.setStatus("mandatory")
_Dot1dPortGmrpLastPduOrigin_Type = MacAddress
_Dot1dPortGmrpLastPduOrigin_Object = MibTableColumn
dot1dPortGmrpLastPduOrigin = _Dot1dPortGmrpLastPduOrigin_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 4, 4, 1, 1, 3),
    _Dot1dPortGmrpLastPduOrigin_Type()
)
dot1dPortGmrpLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dPortGmrpLastPduOrigin.setStatus("mandatory")
_QBridgeMIBObjects_ObjectIdentity = ObjectIdentity
qBridgeMIBObjects = _QBridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5)
)
_Dot1qBase_ObjectIdentity = ObjectIdentity
dot1qBase = _Dot1qBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 1)
)


class _Dot1qVlanVersionNumber_Type(Integer32):
    """Custom type dot1qVlanVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version1", 1)
    )


_Dot1qVlanVersionNumber_Type.__name__ = "Integer32"
_Dot1qVlanVersionNumber_Object = MibScalar
dot1qVlanVersionNumber = _Dot1qVlanVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 1, 1),
    _Dot1qVlanVersionNumber_Type()
)
dot1qVlanVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanVersionNumber.setStatus("mandatory")
_Dot1qMaxVlanId_Type = VlanId
_Dot1qMaxVlanId_Object = MibScalar
dot1qMaxVlanId = _Dot1qMaxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 1, 2),
    _Dot1qMaxVlanId_Type()
)
dot1qMaxVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qMaxVlanId.setStatus("mandatory")
_Dot1qMaxSupportedVlans_Type = Unsigned32
_Dot1qMaxSupportedVlans_Object = MibScalar
dot1qMaxSupportedVlans = _Dot1qMaxSupportedVlans_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 1, 3),
    _Dot1qMaxSupportedVlans_Type()
)
dot1qMaxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qMaxSupportedVlans.setStatus("mandatory")
_Dot1qNumVlans_Type = Unsigned32
_Dot1qNumVlans_Object = MibScalar
dot1qNumVlans = _Dot1qNumVlans_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 1, 4),
    _Dot1qNumVlans_Type()
)
dot1qNumVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qNumVlans.setStatus("mandatory")


class _Dot1qGvrpStatus_Type(EnabledStatus):
    """Custom type dot1qGvrpStatus based on EnabledStatus"""


_Dot1qGvrpStatus_Object = MibScalar
dot1qGvrpStatus = _Dot1qGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 1, 5),
    _Dot1qGvrpStatus_Type()
)
dot1qGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qGvrpStatus.setStatus("mandatory")
_Dot1qTp_ObjectIdentity = ObjectIdentity
dot1qTp = _Dot1qTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2)
)
_Dot1qFdbTable_Object = MibTable
dot1qFdbTable = _Dot1qFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 1)
)
if mibBuilder.loadTexts:
    dot1qFdbTable.setStatus("mandatory")
_Dot1qFdbEntry_Object = MibTableRow
dot1qFdbEntry = _Dot1qFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 1, 1)
)
dot1qFdbEntry.setIndexNames(
    (0, "ES1200-MIB", "dot1qFdbId"),
)
if mibBuilder.loadTexts:
    dot1qFdbEntry.setStatus("mandatory")
_Dot1qFdbId_Type = Unsigned32
_Dot1qFdbId_Object = MibTableColumn
dot1qFdbId = _Dot1qFdbId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 1, 1, 1),
    _Dot1qFdbId_Type()
)
dot1qFdbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qFdbId.setStatus("mandatory")
_Dot1qFdbDynamicCount_Type = Counter32
_Dot1qFdbDynamicCount_Object = MibTableColumn
dot1qFdbDynamicCount = _Dot1qFdbDynamicCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 1, 1, 2),
    _Dot1qFdbDynamicCount_Type()
)
dot1qFdbDynamicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qFdbDynamicCount.setStatus("mandatory")
_Dot1qTpFdbTable_Object = MibTable
dot1qTpFdbTable = _Dot1qTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 2)
)
if mibBuilder.loadTexts:
    dot1qTpFdbTable.setStatus("mandatory")
_Dot1qTpFdbEntry_Object = MibTableRow
dot1qTpFdbEntry = _Dot1qTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 2, 1)
)
dot1qTpFdbEntry.setIndexNames(
    (0, "ES1200-MIB", "dot1qFdbId"),
    (0, "ES1200-MIB", "dot1qTpFdbAddress"),
)
if mibBuilder.loadTexts:
    dot1qTpFdbEntry.setStatus("mandatory")
_Dot1qTpFdbAddress_Type = MacAddress
_Dot1qTpFdbAddress_Object = MibTableColumn
dot1qTpFdbAddress = _Dot1qTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 2, 1, 1),
    _Dot1qTpFdbAddress_Type()
)
dot1qTpFdbAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qTpFdbAddress.setStatus("mandatory")


class _Dot1qTpFdbPort_Type(Integer32):
    """Custom type dot1qTpFdbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1qTpFdbPort_Type.__name__ = "Integer32"
_Dot1qTpFdbPort_Object = MibTableColumn
dot1qTpFdbPort = _Dot1qTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 2, 1, 2),
    _Dot1qTpFdbPort_Type()
)
dot1qTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpFdbPort.setStatus("mandatory")


class _Dot1qTpFdbStatus_Type(Integer32):
    """Custom type dot1qTpFdbStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_Dot1qTpFdbStatus_Type.__name__ = "Integer32"
_Dot1qTpFdbStatus_Object = MibTableColumn
dot1qTpFdbStatus = _Dot1qTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 2, 1, 3),
    _Dot1qTpFdbStatus_Type()
)
dot1qTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpFdbStatus.setStatus("mandatory")
_Dot1qTpGroupTable_Object = MibTable
dot1qTpGroupTable = _Dot1qTpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 3)
)
if mibBuilder.loadTexts:
    dot1qTpGroupTable.setStatus("mandatory")
_Dot1qTpGroupEntry_Object = MibTableRow
dot1qTpGroupEntry = _Dot1qTpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 3, 1)
)
dot1qTpGroupEntry.setIndexNames(
    (0, "ES1200-MIB", "dot1qVlanIndex"),
    (0, "ES1200-MIB", "dot1qTpGroupAddress"),
)
if mibBuilder.loadTexts:
    dot1qTpGroupEntry.setStatus("mandatory")
_Dot1qTpGroupAddress_Type = MacAddress
_Dot1qTpGroupAddress_Object = MibTableColumn
dot1qTpGroupAddress = _Dot1qTpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 3, 1, 1),
    _Dot1qTpGroupAddress_Type()
)
dot1qTpGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qTpGroupAddress.setStatus("mandatory")
_Dot1qTpGroupEgressPorts_Type = PortList
_Dot1qTpGroupEgressPorts_Object = MibTableColumn
dot1qTpGroupEgressPorts = _Dot1qTpGroupEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 3, 1, 2),
    _Dot1qTpGroupEgressPorts_Type()
)
dot1qTpGroupEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpGroupEgressPorts.setStatus("mandatory")
_Dot1qTpGroupLearnt_Type = PortList
_Dot1qTpGroupLearnt_Object = MibTableColumn
dot1qTpGroupLearnt = _Dot1qTpGroupLearnt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 2, 3, 1, 3),
    _Dot1qTpGroupLearnt_Type()
)
dot1qTpGroupLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpGroupLearnt.setStatus("mandatory")
_Dot1qStatic_ObjectIdentity = ObjectIdentity
dot1qStatic = _Dot1qStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 3)
)
_Dot1qStaticMulticastTable_Object = MibTable
dot1qStaticMulticastTable = _Dot1qStaticMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 3, 2)
)
if mibBuilder.loadTexts:
    dot1qStaticMulticastTable.setStatus("mandatory")
_Dot1qStaticMulticastEntry_Object = MibTableRow
dot1qStaticMulticastEntry = _Dot1qStaticMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 3, 2, 1)
)
dot1qStaticMulticastEntry.setIndexNames(
    (0, "ES1200-MIB", "dot1qVlanIndex"),
    (0, "ES1200-MIB", "dot1qStaticMulticastAddress"),
    (0, "ES1200-MIB", "dot1qStaticMulticastReceivePort"),
)
if mibBuilder.loadTexts:
    dot1qStaticMulticastEntry.setStatus("mandatory")
_Dot1qStaticMulticastAddress_Type = MacAddress
_Dot1qStaticMulticastAddress_Object = MibTableColumn
dot1qStaticMulticastAddress = _Dot1qStaticMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 3, 2, 1, 1),
    _Dot1qStaticMulticastAddress_Type()
)
dot1qStaticMulticastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qStaticMulticastAddress.setStatus("mandatory")


class _Dot1qStaticMulticastReceivePort_Type(Integer32):
    """Custom type dot1qStaticMulticastReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1qStaticMulticastReceivePort_Type.__name__ = "Integer32"
_Dot1qStaticMulticastReceivePort_Object = MibTableColumn
dot1qStaticMulticastReceivePort = _Dot1qStaticMulticastReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 3, 2, 1, 2),
    _Dot1qStaticMulticastReceivePort_Type()
)
dot1qStaticMulticastReceivePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qStaticMulticastReceivePort.setStatus("mandatory")
_Dot1qStaticMulticastStaticEgressPorts_Type = PortList
_Dot1qStaticMulticastStaticEgressPorts_Object = MibTableColumn
dot1qStaticMulticastStaticEgressPorts = _Dot1qStaticMulticastStaticEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 3, 2, 1, 3),
    _Dot1qStaticMulticastStaticEgressPorts_Type()
)
dot1qStaticMulticastStaticEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qStaticMulticastStaticEgressPorts.setStatus("mandatory")
_Dot1qStaticMulticastForbiddenEgressPorts_Type = PortList
_Dot1qStaticMulticastForbiddenEgressPorts_Object = MibTableColumn
dot1qStaticMulticastForbiddenEgressPorts = _Dot1qStaticMulticastForbiddenEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 3, 2, 1, 4),
    _Dot1qStaticMulticastForbiddenEgressPorts_Type()
)
dot1qStaticMulticastForbiddenEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qStaticMulticastForbiddenEgressPorts.setStatus("mandatory")


class _Dot1qStaticMulticastStatus_Type(Integer32):
    """Custom type dot1qStaticMulticastStatus based on Integer32"""
    defaultValue = 3

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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_Dot1qStaticMulticastStatus_Type.__name__ = "Integer32"
_Dot1qStaticMulticastStatus_Object = MibTableColumn
dot1qStaticMulticastStatus = _Dot1qStaticMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 3, 2, 1, 5),
    _Dot1qStaticMulticastStatus_Type()
)
dot1qStaticMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qStaticMulticastStatus.setStatus("mandatory")
_Dot1qVlan_ObjectIdentity = ObjectIdentity
dot1qVlan = _Dot1qVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4)
)
_Dot1qVlanNumDeletes_Type = Counter32
_Dot1qVlanNumDeletes_Object = MibScalar
dot1qVlanNumDeletes = _Dot1qVlanNumDeletes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 1),
    _Dot1qVlanNumDeletes_Type()
)
dot1qVlanNumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanNumDeletes.setStatus("mandatory")
_Dot1qVlanCurrentTable_Object = MibTable
dot1qVlanCurrentTable = _Dot1qVlanCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 2)
)
if mibBuilder.loadTexts:
    dot1qVlanCurrentTable.setStatus("mandatory")
_Dot1qVlanCurrentEntry_Object = MibTableRow
dot1qVlanCurrentEntry = _Dot1qVlanCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 2, 1)
)
dot1qVlanCurrentEntry.setIndexNames(
    (0, "ES1200-MIB", "dot1qVlanTimeMark"),
    (0, "ES1200-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dot1qVlanCurrentEntry.setStatus("mandatory")
_Dot1qVlanTimeMark_Type = TimeFilter
_Dot1qVlanTimeMark_Object = MibTableColumn
dot1qVlanTimeMark = _Dot1qVlanTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 2, 1, 1),
    _Dot1qVlanTimeMark_Type()
)
dot1qVlanTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qVlanTimeMark.setStatus("mandatory")
_Dot1qVlanIndex_Type = VlanIndex
_Dot1qVlanIndex_Object = MibTableColumn
dot1qVlanIndex = _Dot1qVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 2, 1, 2),
    _Dot1qVlanIndex_Type()
)
dot1qVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qVlanIndex.setStatus("mandatory")
_Dot1qVlanFdbId_Type = Unsigned32
_Dot1qVlanFdbId_Object = MibTableColumn
dot1qVlanFdbId = _Dot1qVlanFdbId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 2, 1, 3),
    _Dot1qVlanFdbId_Type()
)
dot1qVlanFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanFdbId.setStatus("mandatory")
_Dot1qVlanCurrentEgressPorts_Type = PortList
_Dot1qVlanCurrentEgressPorts_Object = MibTableColumn
dot1qVlanCurrentEgressPorts = _Dot1qVlanCurrentEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 2, 1, 4),
    _Dot1qVlanCurrentEgressPorts_Type()
)
dot1qVlanCurrentEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanCurrentEgressPorts.setStatus("mandatory")
_Dot1qVlanCurrentUntaggedPorts_Type = PortList
_Dot1qVlanCurrentUntaggedPorts_Object = MibTableColumn
dot1qVlanCurrentUntaggedPorts = _Dot1qVlanCurrentUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 2, 1, 5),
    _Dot1qVlanCurrentUntaggedPorts_Type()
)
dot1qVlanCurrentUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanCurrentUntaggedPorts.setStatus("mandatory")


class _Dot1qVlanStatus_Type(Integer32):
    """Custom type dot1qVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicGvrp", 3),
          ("other", 1),
          ("permanent", 2))
    )


_Dot1qVlanStatus_Type.__name__ = "Integer32"
_Dot1qVlanStatus_Object = MibTableColumn
dot1qVlanStatus = _Dot1qVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 2, 1, 6),
    _Dot1qVlanStatus_Type()
)
dot1qVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanStatus.setStatus("mandatory")
_Dot1qVlanCreationTime_Type = TimeTicks
_Dot1qVlanCreationTime_Object = MibTableColumn
dot1qVlanCreationTime = _Dot1qVlanCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 2, 1, 7),
    _Dot1qVlanCreationTime_Type()
)
dot1qVlanCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanCreationTime.setStatus("mandatory")
_Dot1qVlanStaticTable_Object = MibTable
dot1qVlanStaticTable = _Dot1qVlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 3)
)
if mibBuilder.loadTexts:
    dot1qVlanStaticTable.setStatus("mandatory")
_Dot1qVlanStaticEntry_Object = MibTableRow
dot1qVlanStaticEntry = _Dot1qVlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 3, 1)
)
dot1qVlanStaticEntry.setIndexNames(
    (0, "ES1200-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dot1qVlanStaticEntry.setStatus("mandatory")


class _Dot1qVlanStaticName_Type(DisplayString):
    """Custom type dot1qVlanStaticName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot1qVlanStaticName_Type.__name__ = "DisplayString"
_Dot1qVlanStaticName_Object = MibTableColumn
dot1qVlanStaticName = _Dot1qVlanStaticName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 3, 1, 1),
    _Dot1qVlanStaticName_Type()
)
dot1qVlanStaticName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanStaticName.setStatus("mandatory")
_Dot1qVlanStaticEgressPorts_Type = PortList
_Dot1qVlanStaticEgressPorts_Object = MibTableColumn
dot1qVlanStaticEgressPorts = _Dot1qVlanStaticEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 3, 1, 2),
    _Dot1qVlanStaticEgressPorts_Type()
)
dot1qVlanStaticEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanStaticEgressPorts.setStatus("mandatory")
_Dot1qVlanForbiddenEgressPorts_Type = PortList
_Dot1qVlanForbiddenEgressPorts_Object = MibTableColumn
dot1qVlanForbiddenEgressPorts = _Dot1qVlanForbiddenEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 3, 1, 3),
    _Dot1qVlanForbiddenEgressPorts_Type()
)
dot1qVlanForbiddenEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanForbiddenEgressPorts.setStatus("mandatory")
_Dot1qVlanStaticUntaggedPorts_Type = PortList
_Dot1qVlanStaticUntaggedPorts_Object = MibTableColumn
dot1qVlanStaticUntaggedPorts = _Dot1qVlanStaticUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 3, 1, 4),
    _Dot1qVlanStaticUntaggedPorts_Type()
)
dot1qVlanStaticUntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanStaticUntaggedPorts.setStatus("mandatory")


class _Dot1qVlanStaticRowState_Type(Integer32):
    """Custom type dot1qVlanStaticRowState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_Dot1qVlanStaticRowState_Type.__name__ = "Integer32"
_Dot1qVlanStaticRowState_Object = MibTableColumn
dot1qVlanStaticRowState = _Dot1qVlanStaticRowState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 3, 1, 5),
    _Dot1qVlanStaticRowState_Type()
)
dot1qVlanStaticRowState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanStaticRowState.setStatus("mandatory")
_Dot1qPortVlanTable_Object = MibTable
dot1qPortVlanTable = _Dot1qPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 4)
)
if mibBuilder.loadTexts:
    dot1qPortVlanTable.setStatus("mandatory")
_Dot1qPortVlanEntry_Object = MibTableRow
dot1qPortVlanEntry = _Dot1qPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 4, 1)
)
dot1qPortVlanEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dot1qPortVlanEntry.setStatus("mandatory")


class _Dot1qPvid_Type(VlanIndex):
    """Custom type dot1qPvid based on VlanIndex"""
    defaultValue = 1


_Dot1qPvid_Object = MibTableColumn
dot1qPvid = _Dot1qPvid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 4, 1, 1),
    _Dot1qPvid_Type()
)
dot1qPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPvid.setStatus("mandatory")


class _Dot1qPortIngressFiltering_Type(TruthValue):
    """Custom type dot1qPortIngressFiltering based on TruthValue"""


_Dot1qPortIngressFiltering_Object = MibTableColumn
dot1qPortIngressFiltering = _Dot1qPortIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 4, 1, 2),
    _Dot1qPortIngressFiltering_Type()
)
dot1qPortIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPortIngressFiltering.setStatus("mandatory")


class _Dot1qPortGvrpStatus_Type(EnabledStatus):
    """Custom type dot1qPortGvrpStatus based on EnabledStatus"""


_Dot1qPortGvrpStatus_Object = MibTableColumn
dot1qPortGvrpStatus = _Dot1qPortGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 4, 1, 3),
    _Dot1qPortGvrpStatus_Type()
)
dot1qPortGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPortGvrpStatus.setStatus("mandatory")
_Dot1qPortGvrpFailedRegistrations_Type = Counter32
_Dot1qPortGvrpFailedRegistrations_Object = MibTableColumn
dot1qPortGvrpFailedRegistrations = _Dot1qPortGvrpFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 4, 1, 4),
    _Dot1qPortGvrpFailedRegistrations_Type()
)
dot1qPortGvrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qPortGvrpFailedRegistrations.setStatus("mandatory")
_Dot1qPortGvrpLastPduOrigin_Type = MacAddress
_Dot1qPortGvrpLastPduOrigin_Object = MibTableColumn
dot1qPortGvrpLastPduOrigin = _Dot1qPortGvrpLastPduOrigin_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 8, 5, 4, 4, 1, 5),
    _Dot1qPortGvrpLastPduOrigin_Type()
)
dot1qPortGvrpLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qPortGvrpLastPduOrigin.setStatus("mandatory")
_SwFDB_ObjectIdentity = ObjectIdentity
swFDB = _SwFDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9)
)
_SwFdbStaticTable_Object = MibTable
swFdbStaticTable = _SwFdbStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 1)
)
if mibBuilder.loadTexts:
    swFdbStaticTable.setStatus("mandatory")
_SwFdbStaticEntry_Object = MibTableRow
swFdbStaticEntry = _SwFdbStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 1, 1)
)
swFdbStaticEntry.setIndexNames(
    (0, "ES1200-MIB", "swFdbStaticVid"),
    (0, "ES1200-MIB", "swFdbStaticAddress"),
)
if mibBuilder.loadTexts:
    swFdbStaticEntry.setStatus("mandatory")
_SwFdbStaticVid_Type = Integer32
_SwFdbStaticVid_Object = MibTableColumn
swFdbStaticVid = _SwFdbStaticVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 1, 1, 1),
    _SwFdbStaticVid_Type()
)
swFdbStaticVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticVid.setStatus("mandatory")
_SwFdbStaticAddress_Type = MacAddress
_SwFdbStaticAddress_Object = MibTableColumn
swFdbStaticAddress = _SwFdbStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 1, 1, 2),
    _SwFdbStaticAddress_Type()
)
swFdbStaticAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticAddress.setStatus("mandatory")
_SwFdbStaticPortMap_Type = PortList
_SwFdbStaticPortMap_Object = MibTableColumn
swFdbStaticPortMap = _SwFdbStaticPortMap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 1, 1, 3),
    _SwFdbStaticPortMap_Type()
)
swFdbStaticPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFdbStaticPortMap.setStatus("mandatory")


class _SwFdbStaticJoinIGMPSnooping_Type(Integer32):
    """Custom type swFdbStaticJoinIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwFdbStaticJoinIGMPSnooping_Type.__name__ = "Integer32"
_SwFdbStaticJoinIGMPSnooping_Object = MibTableColumn
swFdbStaticJoinIGMPSnooping = _SwFdbStaticJoinIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 1, 1, 4),
    _SwFdbStaticJoinIGMPSnooping_Type()
)
swFdbStaticJoinIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFdbStaticJoinIGMPSnooping.setStatus("mandatory")


class _SwFdbStaticState_Type(Integer32):
    """Custom type swFdbStaticState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwFdbStaticState_Type.__name__ = "Integer32"
_SwFdbStaticState_Object = MibTableColumn
swFdbStaticState = _SwFdbStaticState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 1, 1, 5),
    _SwFdbStaticState_Type()
)
swFdbStaticState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFdbStaticState.setStatus("mandatory")


class _SwFdbStaticStatus_Type(Integer32):
    """Custom type swFdbStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apply", 2),
          ("not-apply", 3),
          ("other", 1))
    )


_SwFdbStaticStatus_Type.__name__ = "Integer32"
_SwFdbStaticStatus_Object = MibTableColumn
swFdbStaticStatus = _SwFdbStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 1, 1, 6),
    _SwFdbStaticStatus_Type()
)
swFdbStaticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticStatus.setStatus("mandatory")
_SwFdbStaticMemberTable_Object = MibTable
swFdbStaticMemberTable = _SwFdbStaticMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 2)
)
if mibBuilder.loadTexts:
    swFdbStaticMemberTable.setStatus("mandatory")
_SwFdbStaticMemberEntry_Object = MibTableRow
swFdbStaticMemberEntry = _SwFdbStaticMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 2, 1)
)
swFdbStaticMemberEntry.setIndexNames(
    (0, "ES1200-MIB", "swFdbStaticMemberVid"),
    (0, "ES1200-MIB", "swFdbStaticMemberAddress"),
    (0, "ES1200-MIB", "swFdbStaticMemberUnitIndex"),
    (0, "ES1200-MIB", "swFdbStaticMemberModuleIndex"),
    (0, "ES1200-MIB", "swFdbStaticMemberPortIndex"),
)
if mibBuilder.loadTexts:
    swFdbStaticMemberEntry.setStatus("mandatory")
_SwFdbStaticMemberVid_Type = Integer32
_SwFdbStaticMemberVid_Object = MibTableColumn
swFdbStaticMemberVid = _SwFdbStaticMemberVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 2, 1, 1),
    _SwFdbStaticMemberVid_Type()
)
swFdbStaticMemberVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticMemberVid.setStatus("mandatory")
_SwFdbStaticMemberAddress_Type = MacAddress
_SwFdbStaticMemberAddress_Object = MibTableColumn
swFdbStaticMemberAddress = _SwFdbStaticMemberAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 2, 1, 2),
    _SwFdbStaticMemberAddress_Type()
)
swFdbStaticMemberAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticMemberAddress.setStatus("mandatory")
_SwFdbStaticMemberUnitIndex_Type = Integer32
_SwFdbStaticMemberUnitIndex_Object = MibTableColumn
swFdbStaticMemberUnitIndex = _SwFdbStaticMemberUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 2, 1, 3),
    _SwFdbStaticMemberUnitIndex_Type()
)
swFdbStaticMemberUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticMemberUnitIndex.setStatus("mandatory")
_SwFdbStaticMemberModuleIndex_Type = Integer32
_SwFdbStaticMemberModuleIndex_Object = MibTableColumn
swFdbStaticMemberModuleIndex = _SwFdbStaticMemberModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 2, 1, 4),
    _SwFdbStaticMemberModuleIndex_Type()
)
swFdbStaticMemberModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticMemberModuleIndex.setStatus("mandatory")
_SwFdbStaticMemberPortIndex_Type = Integer32
_SwFdbStaticMemberPortIndex_Object = MibTableColumn
swFdbStaticMemberPortIndex = _SwFdbStaticMemberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 2, 1, 5),
    _SwFdbStaticMemberPortIndex_Type()
)
swFdbStaticMemberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticMemberPortIndex.setStatus("mandatory")
_SwFdbFilterTable_Object = MibTable
swFdbFilterTable = _SwFdbFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 3)
)
if mibBuilder.loadTexts:
    swFdbFilterTable.setStatus("mandatory")
_SwFdbFilterEntry_Object = MibTableRow
swFdbFilterEntry = _SwFdbFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 3, 1)
)
swFdbFilterEntry.setIndexNames(
    (0, "ES1200-MIB", "swFdbFilterVid"),
    (0, "ES1200-MIB", "swFdbFilterAddress"),
)
if mibBuilder.loadTexts:
    swFdbFilterEntry.setStatus("mandatory")
_SwFdbFilterVid_Type = Integer32
_SwFdbFilterVid_Object = MibTableColumn
swFdbFilterVid = _SwFdbFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 3, 1, 1),
    _SwFdbFilterVid_Type()
)
swFdbFilterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbFilterVid.setStatus("mandatory")
_SwFdbFilterAddress_Type = MacAddress
_SwFdbFilterAddress_Object = MibTableColumn
swFdbFilterAddress = _SwFdbFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 3, 1, 2),
    _SwFdbFilterAddress_Type()
)
swFdbFilterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbFilterAddress.setStatus("mandatory")


class _SwFdbFilterState_Type(Integer32):
    """Custom type swFdbFilterState based on Integer32"""
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
        *(("dst-src-addr", 4),
          ("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwFdbFilterState_Type.__name__ = "Integer32"
_SwFdbFilterState_Object = MibTableColumn
swFdbFilterState = _SwFdbFilterState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 2, 9, 3, 1, 3),
    _SwFdbFilterState_Type()
)
swFdbFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFdbFilterState.setStatus("mandatory")
_EndOfMIB_Type = Integer32
_EndOfMIB_Object = MibScalar
endOfMIB = _EndOfMIB_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 25, 9999),
    _EndOfMIB_Type()
)
endOfMIB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfMIB.setStatus("optional")

# Managed Objects groups


# Notification objects

swEventPortPartition = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 2, 0, 1)
)
swEventPortPartition.setObjects(
      *(("ES1200-MIB", "swL2PortInfoUnitIndex"),
        ("ES1200-MIB", "swL2PortInfoModuleIndex"),
        ("ES1200-MIB", "swL2PortInfoIndex"))
)
if mibBuilder.loadTexts:
    swEventPortPartition.setStatus(
        ""
    )

swEventlinkChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 2, 0, 2)
)
swEventlinkChangeEvent.setObjects(
      *(("ES1200-MIB", "swL2PortInfoUnitIndex"),
        ("ES1200-MIB", "swL2PortInfoModuleIndex"),
        ("ES1200-MIB", "swL2PortInfoIndex"))
)
if mibBuilder.loadTexts:
    swEventlinkChangeEvent.setStatus(
        ""
    )

swEventBcastRisingStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 2, 0, 3)
)
swEventBcastRisingStorm.setObjects(
      *(("ES1200-MIB", "swL2PortInfoUnitIndex"),
        ("ES1200-MIB", "swL2PortInfoModuleIndex"),
        ("ES1200-MIB", "swL2PortInfoIndex"))
)
if mibBuilder.loadTexts:
    swEventBcastRisingStorm.setStatus(
        ""
    )

swEventBcastFallingStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 2, 0, 4)
)
swEventBcastFallingStorm.setObjects(
      *(("ES1200-MIB", "swL2PortInfoUnitIndex"),
        ("ES1200-MIB", "swL2PortInfoModuleIndex"),
        ("ES1200-MIB", "swL2PortInfoIndex"))
)
if mibBuilder.loadTexts:
    swEventBcastFallingStorm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ES1200-MIB",
    **{"PortList": PortList,
       "VlanIndex": VlanIndex,
       "EnabledStatus": EnabledStatus,
       "TruthValue": TruthValue,
       "TimeInterval": TimeInterval,
       "Unsigned32": Unsigned32,
       "VlanId": VlanId,
       "TimeFilter": TimeFilter,
       "fore": fore,
       "systems": systems,
       "ethernet": ethernet,
       "edge": edge,
       "edgecommon": edgecommon,
       "golf": golf,
       "golfproducts": golfproducts,
       "es1200": es1200,
       "swEventPortPartition": swEventPortPartition,
       "swEventlinkChangeEvent": swEventlinkChangeEvent,
       "swEventBcastRisingStorm": swEventBcastRisingStorm,
       "swEventBcastFallingStorm": swEventBcastFallingStorm,
       "golfcommon": golfcommon,
       "fore-products": fore_products,
       "fore-es1200Prod": fore_es1200Prod,
       "swProperty": swProperty,
       "swModule": swModule,
       "es1200DevRegistration": es1200DevRegistration,
       "es1200Device": es1200Device,
       "es1200UnitRegistration": es1200UnitRegistration,
       "es1200Master": es1200Master,
       "es1210Slave1": es1210Slave1,
       "es1210Slave2": es1210Slave2,
       "es1210Slave3": es1210Slave3,
       "es1200ModuleRegistration": es1200ModuleRegistration,
       "es1200ModuleMainboardTx": es1200ModuleMainboardTx,
       "es1200ModuleTxTwoPort": es1200ModuleTxTwoPort,
       "es1200ModuleFxSC": es1200ModuleFxSC,
       "es1200ModuleFxMTRJ": es1200ModuleFxMTRJ,
       "es1200ModuleSIO": es1200ModuleSIO,
       "es1200ModuleSXGIGAOnePort": es1200ModuleSXGIGAOnePort,
       "es1200ModuleSXGIGATwoPort": es1200ModuleSXGIGATwoPort,
       "es1200ModuleLXGIGAOnePort": es1200ModuleLXGIGAOnePort,
       "es1200ModuleLXGIGATwoPort": es1200ModuleLXGIGATwoPort,
       "es1200ModuleTXGIGAOnePort": es1200ModuleTXGIGAOnePort,
       "es1200ModuleTXGIGATwoPort": es1200ModuleTXGIGATwoPort,
       "es1200ModuleNone": es1200ModuleNone,
       "es1210ModuleRegistration": es1210ModuleRegistration,
       "es1210ModuleMainboardTx": es1210ModuleMainboardTx,
       "es1210ModuleTxTwoPort": es1210ModuleTxTwoPort,
       "es1210ModuleFxSC": es1210ModuleFxSC,
       "es1210ModuleFxMTRJ": es1210ModuleFxMTRJ,
       "es1210ModuleSIO": es1210ModuleSIO,
       "es1210ModuleNone": es1210ModuleNone,
       "es1200PortRegistration": es1200PortRegistration,
       "es1200Port-10-100TX": es1200Port_10_100TX,
       "es1200Port-100-SC": es1200Port_100_SC,
       "es1200Port-100-MTRJ": es1200Port_100_MTRJ,
       "es1200Port-1000-SX": es1200Port_1000_SX,
       "es1200Port-1000-LX": es1200Port_1000_LX,
       "es1200Port-1000-TX": es1200Port_1000_TX,
       "es1210PortRegistration": es1210PortRegistration,
       "es1210Port-10-100TX": es1210Port_10_100TX,
       "es1210Port-100-SC": es1210Port_100_SC,
       "es1210Port-100-MTRJ": es1210Port_100_MTRJ,
       "es1200PowerSupplyRegistration": es1200PowerSupplyRegistration,
       "es1200PowerSupply": es1200PowerSupply,
       "es1210PowerSupplyRegistration": es1210PowerSupplyRegistration,
       "es1210PowerSupply": es1210PowerSupply,
       "es1200FanRegistration": es1200FanRegistration,
       "es1200Fan": es1200Fan,
       "es1210FanRegistration": es1210FanRegistration,
       "es1210Fan": es1210Fan,
       "es1200SlotRegistration": es1200SlotRegistration,
       "es1200Slot1": es1200Slot1,
       "es1200Slot2": es1200Slot2,
       "es1200Slot3": es1200Slot3,
       "es1210SlotRegistration": es1210SlotRegistration,
       "es1210Slot1": es1210Slot1,
       "es1210Slot2": es1210Slot2,
       "es1200SensorRegistration": es1200SensorRegistration,
       "es1200BackplaneRegistration": es1200BackplaneRegistration,
       "fore-mgmt": fore_mgmt,
       "es1200Mgmt": es1200Mgmt,
       "swStructure": swStructure,
       "swStructInfo": swStructInfo,
       "swStructDevType": swStructDevType,
       "swStructDevDescr": swStructDevDescr,
       "swStructPortEncodingFactor": swStructPortEncodingFactor,
       "swStructUnitTable": swStructUnitTable,
       "swStructUnitEntry": swStructUnitEntry,
       "swStructUnitIndex": swStructUnitIndex,
       "swStructUnitType": swStructUnitType,
       "swStructUnitDescr": swStructUnitDescr,
       "swStructUnitLedInfo": swStructUnitLedInfo,
       "swStructUnitMaxModuleNum": swStructUnitMaxModuleNum,
       "swStructUnitMaxPortNum": swStructUnitMaxPortNum,
       "swStructUnitNumOfPortInUse": swStructUnitNumOfPortInUse,
       "swStructUnitOperStatus": swStructUnitOperStatus,
       "swStructUnitLastChange": swStructUnitLastChange,
       "swStructModuleTable": swStructModuleTable,
       "swStructModuleEntry": swStructModuleEntry,
       "swStructModuleUnitIndex": swStructModuleUnitIndex,
       "swStructModuleIndex": swStructModuleIndex,
       "swStructModuleSubMduIndex": swStructModuleSubMduIndex,
       "swStructModuleType": swStructModuleType,
       "swStructModuleDescr": swStructModuleDescr,
       "swStructModuleVersion": swStructModuleVersion,
       "swStructModuleMaxPortNum": swStructModuleMaxPortNum,
       "swStructModuleEncodingOffset": swStructModuleEncodingOffset,
       "swStructModuleOperStatus": swStructModuleOperStatus,
       "swStructModuleLastChange": swStructModuleLastChange,
       "swStructPowerTable": swStructPowerTable,
       "swStructPowerEntry": swStructPowerEntry,
       "swStructPowerUnitIndex": swStructPowerUnitIndex,
       "swStructPowerIndex": swStructPowerIndex,
       "swStructPowerOperStatus": swStructPowerOperStatus,
       "swStructFanTable": swStructFanTable,
       "swStructFanEntry": swStructFanEntry,
       "swStructFanUnitIndex": swStructFanUnitIndex,
       "swStructFanIndex": swStructFanIndex,
       "swStructFanOperStatus": swStructFanOperStatus,
       "swL2Mgmt": swL2Mgmt,
       "swL2DevMgmt": swL2DevMgmt,
       "swL2DevCtrl": swL2DevCtrl,
       "swL2DevCtrlStpState": swL2DevCtrlStpState,
       "swL2DevCtrlPartitionModeState": swL2DevCtrlPartitionModeState,
       "swL2DevCtrlTableLockState": swL2DevCtrlTableLockState,
       "swL2DevCtrlHOLState": swL2DevCtrlHOLState,
       "swL2DevCtrlAddrLookupModesAndHitRate": swL2DevCtrlAddrLookupModesAndHitRate,
       "swL2DevCtrlUploadImageFileName": swL2DevCtrlUploadImageFileName,
       "swL2DevCtrlUploadImage": swL2DevCtrlUploadImage,
       "swL2DevCtrlClearAddressTable": swL2DevCtrlClearAddressTable,
       "swL2DevAlarm": swL2DevAlarm,
       "swL2DevAlarmPartition": swL2DevAlarmPartition,
       "swL2DevAlarmNewRoot": swL2DevAlarmNewRoot,
       "swL2DevAlarmTopChange": swL2DevAlarmTopChange,
       "swL2DevAlarmLinkChange": swL2DevAlarmLinkChange,
       "swL2PortMgmt": swL2PortMgmt,
       "swL2PortInfoTable": swL2PortInfoTable,
       "swL2PortInfoEntry": swL2PortInfoEntry,
       "swL2PortInfoUnitIndex": swL2PortInfoUnitIndex,
       "swL2PortInfoModuleIndex": swL2PortInfoModuleIndex,
       "swL2PortInfoIndex": swL2PortInfoIndex,
       "swL2PortInfoType": swL2PortInfoType,
       "swL2PortInfoDescr": swL2PortInfoDescr,
       "swL2PortInfoLinkStatus": swL2PortInfoLinkStatus,
       "swL2PortInfoNwayStatus": swL2PortInfoNwayStatus,
       "swL2PortCtrlTable": swL2PortCtrlTable,
       "swL2PortCtrlEntry": swL2PortCtrlEntry,
       "swL2PortCtrlUnitIndex": swL2PortCtrlUnitIndex,
       "swL2PortCtrlModuleIndex": swL2PortCtrlModuleIndex,
       "swL2PortCtrlIndex": swL2PortCtrlIndex,
       "swL2PortCtrlAdminState": swL2PortCtrlAdminState,
       "swL2PortCtrlLinkStatusAlarmState": swL2PortCtrlLinkStatusAlarmState,
       "swL2PortCtrlNwayState": swL2PortCtrlNwayState,
       "swL2PortCtrlFlowCtrlState": swL2PortCtrlFlowCtrlState,
       "swL2PortCtrlBackPressState": swL2PortCtrlBackPressState,
       "swL2PortCtrlLockState": swL2PortCtrlLockState,
       "swL2PortCtrlPriority": swL2PortCtrlPriority,
       "swL2PortCtrlStpState": swL2PortCtrlStpState,
       "swL2PortCtrlHOLState": swL2PortCtrlHOLState,
       "swL2PortCtrlBcastRisingAct": swL2PortCtrlBcastRisingAct,
       "swL2PortCtrlBcastFallingAct": swL2PortCtrlBcastFallingAct,
       "swL2PortStTable": swL2PortStTable,
       "swL2PortStEntry": swL2PortStEntry,
       "swL2PortStUnitIndex": swL2PortStUnitIndex,
       "swL2PortStModuleIndex": swL2PortStModuleIndex,
       "swL2PortStIndex": swL2PortStIndex,
       "swL2PortStByteRx": swL2PortStByteRx,
       "swL2PortStByteTx": swL2PortStByteTx,
       "swL2PortStFrameRx": swL2PortStFrameRx,
       "swL2PortStFrameTx": swL2PortStFrameTx,
       "swL2PortStTotalBytesRx": swL2PortStTotalBytesRx,
       "swL2PortStTotalFramesRx": swL2PortStTotalFramesRx,
       "swL2PortStBroadcastFramesRx": swL2PortStBroadcastFramesRx,
       "swL2PortStMulticastFramesRx": swL2PortStMulticastFramesRx,
       "swL2PortStCRCError": swL2PortStCRCError,
       "swL2PortStOversizeFrames": swL2PortStOversizeFrames,
       "swL2PortStFragments": swL2PortStFragments,
       "swL2PortStJabber": swL2PortStJabber,
       "swL2PortStCollision": swL2PortStCollision,
       "swL2PortStLateCollision": swL2PortStLateCollision,
       "swL2PortStFrames-64-bytes": swL2PortStFrames_64_bytes,
       "swL2PortStFrames-65-127-bytes": swL2PortStFrames_65_127_bytes,
       "swL2PortStFrames-128-255-bytes": swL2PortStFrames_128_255_bytes,
       "swL2PortStFrames-256-511-bytes": swL2PortStFrames_256_511_bytes,
       "swL2PortStFrames-512-1023-bytes": swL2PortStFrames_512_1023_bytes,
       "swL2PortStFrames-1024-1536-bytes": swL2PortStFrames_1024_1536_bytes,
       "swL2PortStFramesDroppedFrames": swL2PortStFramesDroppedFrames,
       "swL2PortStMulticastFramesTx": swL2PortStMulticastFramesTx,
       "swL2PortStBroadcastFramesTx": swL2PortStBroadcastFramesTx,
       "swL2PortStUndersizeFrames": swL2PortStUndersizeFrames,
       "swPortSniff": swPortSniff,
       "swSniffCtrlTable": swSniffCtrlTable,
       "swSniffCtrlEntry": swSniffCtrlEntry,
       "swSniffIndex": swSniffIndex,
       "swSniffSourcePort": swSniffSourcePort,
       "swSniffTargetPort": swSniffTargetPort,
       "swSniffState": swSniffState,
       "swPortTrunk": swPortTrunk,
       "swPortTrunkCtrlTable": swPortTrunkCtrlTable,
       "swPortTrunkCtrlEntry": swPortTrunkCtrlEntry,
       "swPortTrunkCtrlIndex": swPortTrunkCtrlIndex,
       "swPortTrunkCtrlAnchorPort": swPortTrunkCtrlAnchorPort,
       "swPortTrunkCtrlMasterPort": swPortTrunkCtrlMasterPort,
       "swPortTrunkCtrlName": swPortTrunkCtrlName,
       "swPortTrunkCtrlMember": swPortTrunkCtrlMember,
       "swPortTrunkCtrlState": swPortTrunkCtrlState,
       "swPortTrunkMemberTable": swPortTrunkMemberTable,
       "swPortTrunkMemberEntry": swPortTrunkMemberEntry,
       "swPortTrunkMemberIndex": swPortTrunkMemberIndex,
       "swPortTrunkMemberUnitIndex": swPortTrunkMemberUnitIndex,
       "swPortTrunkMemberModuleIndex": swPortTrunkMemberModuleIndex,
       "swPortTrunkMemberPortIndex": swPortTrunkMemberPortIndex,
       "swIGMP": swIGMP,
       "swIGMPCtrl": swIGMPCtrl,
       "swIGMPAdminState": swIGMPAdminState,
       "swIGMPTimeout": swIGMPTimeout,
       "swIGMPInfoTable": swIGMPInfoTable,
       "swIGMPInfoEntry": swIGMPInfoEntry,
       "swIGMPInfoIndex": swIGMPInfoIndex,
       "swIGMPInfoVid": swIGMPInfoVid,
       "swIGMPInfoQueryCount": swIGMPInfoQueryCount,
       "swIGMPInfoTxQueryCount": swIGMPInfoTxQueryCount,
       "swIGMPTable": swIGMPTable,
       "swIGMPEntry": swIGMPEntry,
       "swIGMPVid": swIGMPVid,
       "swIGMPGroupIpAddr": swIGMPGroupIpAddr,
       "swIGMPGroupMacAddr": swIGMPGroupMacAddr,
       "swIGMPPortMap": swIGMPPortMap,
       "swIGMPIpGroupReportCount": swIGMPIpGroupReportCount,
       "swIGMPCtrlTable": swIGMPCtrlTable,
       "swIGMPCtrlEntry": swIGMPCtrlEntry,
       "swIGMPCtrlIndex": swIGMPCtrlIndex,
       "swIGMPCtrlVid": swIGMPCtrlVid,
       "swIGMPCtrlTimer": swIGMPCtrlTimer,
       "swIGMPCtrlState": swIGMPCtrlState,
       "swVlan": swVlan,
       "swVlanCtrl": swVlanCtrl,
       "swVlanCtrlMode": swVlanCtrlMode,
       "swVlanInfoStatus": swVlanInfoStatus,
       "swVlanSnmpPortVlan": swVlanSnmpPortVlan,
       "swMacBaseVlan": swMacBaseVlan,
       "swMacBaseVlanInfo": swMacBaseVlanInfo,
       "swMacBaseVlanMaxNum": swMacBaseVlanMaxNum,
       "swMacBaseVlanAddrMaxNum": swMacBaseVlanAddrMaxNum,
       "swMacBaseVlanCtrlTable": swMacBaseVlanCtrlTable,
       "swMacBaseVlanCtrlEntry": swMacBaseVlanCtrlEntry,
       "swMacBaseVlanDesc": swMacBaseVlanDesc,
       "swMacBaseVlanMacMember": swMacBaseVlanMacMember,
       "swMacBaseVlanCtrlState": swMacBaseVlanCtrlState,
       "swMacBaseVlanAddrTable": swMacBaseVlanAddrTable,
       "swMacBaseVlanAddrEntry": swMacBaseVlanAddrEntry,
       "swMacBaseVlanAddr": swMacBaseVlanAddr,
       "swMacBaseVlanAddrVlanDesc": swMacBaseVlanAddrVlanDesc,
       "swMacBaseVlanAddrState": swMacBaseVlanAddrState,
       "swMacBaseVlanAddrStatus": swMacBaseVlanAddrStatus,
       "swPortBaseVlan": swPortBaseVlan,
       "swPortBaseVlanTotalNum": swPortBaseVlanTotalNum,
       "swPortBaseVlanDefaultVlanTable": swPortBaseVlanDefaultVlanTable,
       "swPortBaseVlanDefaultVlanEntry": swPortBaseVlanDefaultVlanEntry,
       "swPortBaseVlanDefaultPvid": swPortBaseVlanDefaultPvid,
       "swPortBaseVlanDefaultDesc": swPortBaseVlanDefaultDesc,
       "swPortBaseVlanDefaultPortList": swPortBaseVlanDefaultPortList,
       "swPortBaseVlanDefaultPortNumber": swPortBaseVlanDefaultPortNumber,
       "swPortBaseVlanConfigTable": swPortBaseVlanConfigTable,
       "swPortBaseVlanConfigEntry": swPortBaseVlanConfigEntry,
       "swPortBaseVlanConfigPvid": swPortBaseVlanConfigPvid,
       "swPortBaseVlanConfigDesc": swPortBaseVlanConfigDesc,
       "swPortBaseVlanConfigPortList": swPortBaseVlanConfigPortList,
       "swPortBaseVlanConfigPortNumber": swPortBaseVlanConfigPortNumber,
       "pBridgeMIBObjects": pBridgeMIBObjects,
       "dot1dExtBase": dot1dExtBase,
       "dot1dDeviceCapabilities": dot1dDeviceCapabilities,
       "dot1dTrafficClassesEnabled": dot1dTrafficClassesEnabled,
       "dot1dGmrpStatus": dot1dGmrpStatus,
       "dot1dPortCapabilitiesTable": dot1dPortCapabilitiesTable,
       "dot1dPortCapabilitiesEntry": dot1dPortCapabilitiesEntry,
       "dot1dPortCapabilities": dot1dPortCapabilities,
       "dot1dPriority": dot1dPriority,
       "dot1dPortPriorityTable": dot1dPortPriorityTable,
       "dot1dPortPriorityEntry": dot1dPortPriorityEntry,
       "dot1dPortNumTrafficClasses": dot1dPortNumTrafficClasses,
       "dot1dGarp": dot1dGarp,
       "dot1dPortGarpTable": dot1dPortGarpTable,
       "dot1dPortGarpEntry": dot1dPortGarpEntry,
       "dot1dPortGarpJoinTime": dot1dPortGarpJoinTime,
       "dot1dPortGarpLeaveTime": dot1dPortGarpLeaveTime,
       "dot1dPortGarpLeaveAllTime": dot1dPortGarpLeaveAllTime,
       "dot1dGmrp": dot1dGmrp,
       "dot1dPortGmrpTable": dot1dPortGmrpTable,
       "dot1dPortGmrpEntry": dot1dPortGmrpEntry,
       "dot1dPortGmrpStatus": dot1dPortGmrpStatus,
       "dot1dPortGmrpFailedRegistrations": dot1dPortGmrpFailedRegistrations,
       "dot1dPortGmrpLastPduOrigin": dot1dPortGmrpLastPduOrigin,
       "qBridgeMIBObjects": qBridgeMIBObjects,
       "dot1qBase": dot1qBase,
       "dot1qVlanVersionNumber": dot1qVlanVersionNumber,
       "dot1qMaxVlanId": dot1qMaxVlanId,
       "dot1qMaxSupportedVlans": dot1qMaxSupportedVlans,
       "dot1qNumVlans": dot1qNumVlans,
       "dot1qGvrpStatus": dot1qGvrpStatus,
       "dot1qTp": dot1qTp,
       "dot1qFdbTable": dot1qFdbTable,
       "dot1qFdbEntry": dot1qFdbEntry,
       "dot1qFdbId": dot1qFdbId,
       "dot1qFdbDynamicCount": dot1qFdbDynamicCount,
       "dot1qTpFdbTable": dot1qTpFdbTable,
       "dot1qTpFdbEntry": dot1qTpFdbEntry,
       "dot1qTpFdbAddress": dot1qTpFdbAddress,
       "dot1qTpFdbPort": dot1qTpFdbPort,
       "dot1qTpFdbStatus": dot1qTpFdbStatus,
       "dot1qTpGroupTable": dot1qTpGroupTable,
       "dot1qTpGroupEntry": dot1qTpGroupEntry,
       "dot1qTpGroupAddress": dot1qTpGroupAddress,
       "dot1qTpGroupEgressPorts": dot1qTpGroupEgressPorts,
       "dot1qTpGroupLearnt": dot1qTpGroupLearnt,
       "dot1qStatic": dot1qStatic,
       "dot1qStaticMulticastTable": dot1qStaticMulticastTable,
       "dot1qStaticMulticastEntry": dot1qStaticMulticastEntry,
       "dot1qStaticMulticastAddress": dot1qStaticMulticastAddress,
       "dot1qStaticMulticastReceivePort": dot1qStaticMulticastReceivePort,
       "dot1qStaticMulticastStaticEgressPorts": dot1qStaticMulticastStaticEgressPorts,
       "dot1qStaticMulticastForbiddenEgressPorts": dot1qStaticMulticastForbiddenEgressPorts,
       "dot1qStaticMulticastStatus": dot1qStaticMulticastStatus,
       "dot1qVlan": dot1qVlan,
       "dot1qVlanNumDeletes": dot1qVlanNumDeletes,
       "dot1qVlanCurrentTable": dot1qVlanCurrentTable,
       "dot1qVlanCurrentEntry": dot1qVlanCurrentEntry,
       "dot1qVlanTimeMark": dot1qVlanTimeMark,
       "dot1qVlanIndex": dot1qVlanIndex,
       "dot1qVlanFdbId": dot1qVlanFdbId,
       "dot1qVlanCurrentEgressPorts": dot1qVlanCurrentEgressPorts,
       "dot1qVlanCurrentUntaggedPorts": dot1qVlanCurrentUntaggedPorts,
       "dot1qVlanStatus": dot1qVlanStatus,
       "dot1qVlanCreationTime": dot1qVlanCreationTime,
       "dot1qVlanStaticTable": dot1qVlanStaticTable,
       "dot1qVlanStaticEntry": dot1qVlanStaticEntry,
       "dot1qVlanStaticName": dot1qVlanStaticName,
       "dot1qVlanStaticEgressPorts": dot1qVlanStaticEgressPorts,
       "dot1qVlanForbiddenEgressPorts": dot1qVlanForbiddenEgressPorts,
       "dot1qVlanStaticUntaggedPorts": dot1qVlanStaticUntaggedPorts,
       "dot1qVlanStaticRowState": dot1qVlanStaticRowState,
       "dot1qPortVlanTable": dot1qPortVlanTable,
       "dot1qPortVlanEntry": dot1qPortVlanEntry,
       "dot1qPvid": dot1qPvid,
       "dot1qPortIngressFiltering": dot1qPortIngressFiltering,
       "dot1qPortGvrpStatus": dot1qPortGvrpStatus,
       "dot1qPortGvrpFailedRegistrations": dot1qPortGvrpFailedRegistrations,
       "dot1qPortGvrpLastPduOrigin": dot1qPortGvrpLastPduOrigin,
       "swFDB": swFDB,
       "swFdbStaticTable": swFdbStaticTable,
       "swFdbStaticEntry": swFdbStaticEntry,
       "swFdbStaticVid": swFdbStaticVid,
       "swFdbStaticAddress": swFdbStaticAddress,
       "swFdbStaticPortMap": swFdbStaticPortMap,
       "swFdbStaticJoinIGMPSnooping": swFdbStaticJoinIGMPSnooping,
       "swFdbStaticState": swFdbStaticState,
       "swFdbStaticStatus": swFdbStaticStatus,
       "swFdbStaticMemberTable": swFdbStaticMemberTable,
       "swFdbStaticMemberEntry": swFdbStaticMemberEntry,
       "swFdbStaticMemberVid": swFdbStaticMemberVid,
       "swFdbStaticMemberAddress": swFdbStaticMemberAddress,
       "swFdbStaticMemberUnitIndex": swFdbStaticMemberUnitIndex,
       "swFdbStaticMemberModuleIndex": swFdbStaticMemberModuleIndex,
       "swFdbStaticMemberPortIndex": swFdbStaticMemberPortIndex,
       "swFdbFilterTable": swFdbFilterTable,
       "swFdbFilterEntry": swFdbFilterEntry,
       "swFdbFilterVid": swFdbFilterVid,
       "swFdbFilterAddress": swFdbFilterAddress,
       "swFdbFilterState": swFdbFilterState,
       "endOfMIB": endOfMIB}
)
