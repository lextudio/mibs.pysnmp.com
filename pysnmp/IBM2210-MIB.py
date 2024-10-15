# SNMP MIB module (IBM2210-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM2210-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:43 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(proElsSubSysEventMsg,
 proElsTrapEvent,
 proElsTrapSeqs,
 proElsTrapSubSystem) = mibBuilder.importSymbols(
    "PROTEON-MIB",
    "proElsSubSysEventMsg",
    "proElsTrapEvent",
    "proElsTrapSeqs",
    "proElsTrapSubSystem")

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

_Proteon_ObjectIdentity = ObjectIdentity
proteon = _Proteon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1)
)
_ProXfaceGenericTable_Object = MibTable
proXfaceGenericTable = _ProXfaceGenericTable_Object(
    (1, 3, 6, 1, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    proXfaceGenericTable.setStatus("mandatory")
_ProXfaceGenericEntry_Object = MibTableRow
proXfaceGenericEntry = _ProXfaceGenericEntry_Object(
    (1, 3, 6, 1, 4, 1, 1, 2, 1)
)
proXfaceGenericEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    proXfaceGenericEntry.setStatus("mandatory")


class _ProXfaceGenericType_Type(Integer32):
    """Custom type proXfaceGenericType based on Integer32"""
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
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64)
        )
    )
    namedValues = NamedValues(
        *(("appnl", 60),
          ("atcomsl", 24),
          ("atm", 48),
          ("atmpmpls", 63),
          ("atmvirt", 59),
          ("atr", 19),
          ("ceth", 25),
          ("chaos", 4),
          ("com2", 10),
          ("com4", 11),
          ("csl", 26),
          ("escon", 49),
          ("eth100", 64),
          ("fddi", 20),
          ("gwslc", 16),
          ("hssi", 42),
          ("hyper", 14),
          ("ieth", 8),
          ("isdnpri", 50),
          ("m1822", 6),
          ("mp", 62),
          ("nseth", 33),
          ("nwescon", 58),
          ("omn", 12),
          ("pawrs232", 57),
          ("pawv36", 56),
          ("pawx21", 55),
          ("peth", 9),
          ("pn10", 2),
          ("pn16", 23),
          ("pn4", 13),
          ("pn80", 3),
          ("pqsx", 18),
          ("qsl", 37),
          ("qslch", 40),
          ("quic4mdm", 53),
          ("quic4wan", 51),
          ("quic8mdm", 54),
          ("quic8wan", 52),
          ("quicbisdn", 46),
          ("quiceth", 43),
          ("quicsl", 45),
          ("quictkr", 44),
          ("scc", 7),
          ("sdlcrly", 32),
          ("seth", 27),
          ("srbtnl", 31),
          ("srlyatc2", 29),
          ("srlycsl", 30),
          ("srlygwsl", 28),
          ("tsl", 39),
          ("v25bis", 41),
          ("v34", 61),
          ("vcom4", 22),
          ("vi", 1),
          ("vlane", 21),
          ("vlic", 47),
          ("wdeth", 15),
          ("x25", 17),
          ("x25atc2", 34),
          ("x25csl", 35),
          ("x25dcsl", 36),
          ("xeth", 5),
          ("ydcisdn", 38))
    )


_ProXfaceGenericType_Type.__name__ = "Integer32"
_ProXfaceGenericType_Object = MibTableColumn
proXfaceGenericType = _ProXfaceGenericType_Object(
    (1, 3, 6, 1, 4, 1, 1, 2, 1, 1),
    _ProXfaceGenericType_Type()
)
proXfaceGenericType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proXfaceGenericType.setStatus("mandatory")
_ProXfaceGenericCSR_Type = Integer32
_ProXfaceGenericCSR_Object = MibTableColumn
proXfaceGenericCSR = _ProXfaceGenericCSR_Object(
    (1, 3, 6, 1, 4, 1, 1, 2, 1, 2),
    _ProXfaceGenericCSR_Type()
)
proXfaceGenericCSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proXfaceGenericCSR.setStatus("mandatory")
_ProXfaceGenericIntVec_Type = Integer32
_ProXfaceGenericIntVec_Object = MibTableColumn
proXfaceGenericIntVec = _ProXfaceGenericIntVec_Object(
    (1, 3, 6, 1, 4, 1, 1, 2, 1, 3),
    _ProXfaceGenericIntVec_Type()
)
proXfaceGenericIntVec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proXfaceGenericIntVec.setStatus("mandatory")
_ProXfaceGenericMaintInt_Type = Integer32
_ProXfaceGenericMaintInt_Object = MibTableColumn
proXfaceGenericMaintInt = _ProXfaceGenericMaintInt_Object(
    (1, 3, 6, 1, 4, 1, 1, 2, 1, 4),
    _ProXfaceGenericMaintInt_Type()
)
proXfaceGenericMaintInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proXfaceGenericMaintInt.setStatus("mandatory")
_ProXfaceGenericMaintLim_Type = Integer32
_ProXfaceGenericMaintLim_Object = MibTableColumn
proXfaceGenericMaintLim = _ProXfaceGenericMaintLim_Object(
    (1, 3, 6, 1, 4, 1, 1, 2, 1, 5),
    _ProXfaceGenericMaintLim_Type()
)
proXfaceGenericMaintLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proXfaceGenericMaintLim.setStatus("mandatory")
_ProXfaceGenericNextTest_Type = Integer32
_ProXfaceGenericNextTest_Object = MibTableColumn
proXfaceGenericNextTest = _ProXfaceGenericNextTest_Object(
    (1, 3, 6, 1, 4, 1, 1, 2, 1, 6),
    _ProXfaceGenericNextTest_Type()
)
proXfaceGenericNextTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proXfaceGenericNextTest.setStatus("mandatory")
_ProXfaceGenericNextMaint_Type = Integer32
_ProXfaceGenericNextMaint_Object = MibTableColumn
proXfaceGenericNextMaint = _ProXfaceGenericNextMaint_Object(
    (1, 3, 6, 1, 4, 1, 1, 2, 1, 7),
    _ProXfaceGenericNextMaint_Type()
)
proXfaceGenericNextMaint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proXfaceGenericNextMaint.setStatus("mandatory")
_ProXfaceGenericMaintCnt_Type = Counter32
_ProXfaceGenericMaintCnt_Object = MibTableColumn
proXfaceGenericMaintCnt = _ProXfaceGenericMaintCnt_Object(
    (1, 3, 6, 1, 4, 1, 1, 2, 1, 8),
    _ProXfaceGenericMaintCnt_Type()
)
proXfaceGenericMaintCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proXfaceGenericMaintCnt.setStatus("mandatory")
_ProXfaceGenericMaintFails_Type = Counter32
_ProXfaceGenericMaintFails_Object = MibTableColumn
proXfaceGenericMaintFails = _ProXfaceGenericMaintFails_Object(
    (1, 3, 6, 1, 4, 1, 1, 2, 1, 9),
    _ProXfaceGenericMaintFails_Type()
)
proXfaceGenericMaintFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proXfaceGenericMaintFails.setStatus("mandatory")
_ProXfaceGenericTestPasses_Type = Counter32
_ProXfaceGenericTestPasses_Object = MibTableColumn
proXfaceGenericTestPasses = _ProXfaceGenericTestPasses_Object(
    (1, 3, 6, 1, 4, 1, 1, 2, 1, 10),
    _ProXfaceGenericTestPasses_Type()
)
proXfaceGenericTestPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proXfaceGenericTestPasses.setStatus("mandatory")
_ProXfaceGenericTestFails_Type = Counter32
_ProXfaceGenericTestFails_Object = MibTableColumn
proXfaceGenericTestFails = _ProXfaceGenericTestFails_Object(
    (1, 3, 6, 1, 4, 1, 1, 2, 1, 11),
    _ProXfaceGenericTestFails_Type()
)
proXfaceGenericTestFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proXfaceGenericTestFails.setStatus("mandatory")
_ProXfaceGenericModuleId_Type = Integer32
_ProXfaceGenericModuleId_Object = MibTableColumn
proXfaceGenericModuleId = _ProXfaceGenericModuleId_Object(
    (1, 3, 6, 1, 4, 1, 1, 2, 1, 12),
    _ProXfaceGenericModuleId_Type()
)
proXfaceGenericModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proXfaceGenericModuleId.setStatus("mandatory")
_Proto_ObjectIdentity = ObjectIdentity
proto = _Proto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 3)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 3, 1)
)
_Proip_ObjectIdentity = ObjectIdentity
proip = _Proip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 3, 2)
)
_Defgw_ObjectIdentity = ObjectIdentity
defgw = _Defgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 3, 2, 1)
)
_ProProtoIpDefGwAddress_Type = IpAddress
_ProProtoIpDefGwAddress_Object = MibScalar
proProtoIpDefGwAddress = _ProProtoIpDefGwAddress_Object(
    (1, 3, 6, 1, 4, 1, 1, 3, 2, 1, 1),
    _ProProtoIpDefGwAddress_Type()
)
proProtoIpDefGwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proProtoIpDefGwAddress.setStatus("mandatory")
_ProProtoIpDefGwCost_Type = Integer32
_ProProtoIpDefGwCost_Object = MibScalar
proProtoIpDefGwCost = _ProProtoIpDefGwCost_Object(
    (1, 3, 6, 1, 4, 1, 1, 3, 2, 1, 2),
    _ProProtoIpDefGwCost_Type()
)
proProtoIpDefGwCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proProtoIpDefGwCost.setStatus("mandatory")
_ProProtoIpDefGwAge_Type = Integer32
_ProProtoIpDefGwAge_Object = MibScalar
proProtoIpDefGwAge = _ProProtoIpDefGwAge_Object(
    (1, 3, 6, 1, 4, 1, 1, 3, 2, 1, 3),
    _ProProtoIpDefGwAge_Type()
)
proProtoIpDefGwAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proProtoIpDefGwAge.setStatus("mandatory")
_PDot3ChipSets_ObjectIdentity = ObjectIdentity
pDot3ChipSets = _PDot3ChipSets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 5)
)
_PDot3ChipMC68EN360_ObjectIdentity = ObjectIdentity
pDot3ChipMC68EN360 = _PDot3ChipMC68EN360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 5, 1)
)
_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm2210_ObjectIdentity = ObjectIdentity
ibm2210 = _Ibm2210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 72)
)
_Ibm2210admin_ObjectIdentity = ObjectIdentity
ibm2210admin = _Ibm2210admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 72, 1)
)
_Ibm2210system_ObjectIdentity = ObjectIdentity
ibm2210system = _Ibm2210system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 72, 2)
)
_Ibm2210hardware_ObjectIdentity = ObjectIdentity
ibm2210hardware = _Ibm2210hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 72, 3)
)
_Ibm2210hardwareinfo_ObjectIdentity = ObjectIdentity
ibm2210hardwareinfo = _Ibm2210hardwareinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 72, 3, 1)
)
_IbmServiceGenericTable_Object = MibTable
ibmServiceGenericTable = _IbmServiceGenericTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 72, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ibmServiceGenericTable.setStatus("mandatory")
_IbmServiceGenericEntry_Object = MibTableRow
ibmServiceGenericEntry = _IbmServiceGenericEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 72, 3, 1, 1, 1)
)
ibmServiceGenericEntry.setIndexNames(
    (0, "IBM2210-MIB", "ibmServiceGenericPort"),
)
if mibBuilder.loadTexts:
    ibmServiceGenericEntry.setStatus("mandatory")
_IbmServiceGenericPort_Type = Integer32
_IbmServiceGenericPort_Object = MibTableColumn
ibmServiceGenericPort = _IbmServiceGenericPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 72, 3, 1, 1, 1, 1),
    _IbmServiceGenericPort_Type()
)
ibmServiceGenericPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServiceGenericPort.setStatus("mandatory")
_IbmServiceGenericBaurdrate_Type = Integer32
_IbmServiceGenericBaurdrate_Object = MibTableColumn
ibmServiceGenericBaurdrate = _IbmServiceGenericBaurdrate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 72, 3, 1, 1, 1, 2),
    _IbmServiceGenericBaurdrate_Type()
)
ibmServiceGenericBaurdrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServiceGenericBaurdrate.setStatus("mandatory")


class _IbmServiceGenericType_Type(Integer32):
    """Custom type ibmServiceGenericType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eia232", 1),
          ("modem", 2),
          ("nocard", 3))
    )


_IbmServiceGenericType_Type.__name__ = "Integer32"
_IbmServiceGenericType_Object = MibTableColumn
ibmServiceGenericType = _IbmServiceGenericType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 72, 3, 1, 1, 1, 3),
    _IbmServiceGenericType_Type()
)
ibmServiceGenericType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServiceGenericType.setStatus("mandatory")
_Ibm2210routing_ObjectIdentity = ObjectIdentity
ibm2210routing = _Ibm2210routing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 72, 4)
)
_Ibm2210switching_ObjectIdentity = ObjectIdentity
ibm2210switching = _Ibm2210switching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 72, 5)
)

# Managed Objects groups


# Notification objects

ibmElsTrapV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 72, 0, 1)
)
ibmElsTrapV1.setObjects(
      *(("PROTEON-MIB", "proElsTrapSeqs"),
        ("PROTEON-MIB", "proElsTrapSubSystem"),
        ("PROTEON-MIB", "proElsTrapEvent"))
)
if mibBuilder.loadTexts:
    ibmElsTrapV1.setStatus(
        ""
    )

ibmElsTrapV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 72, 0, 2)
)
ibmElsTrapV2.setObjects(
    ("PROTEON-MIB", "proElsSubSysEventMsg")
)
if mibBuilder.loadTexts:
    ibmElsTrapV2.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM2210-MIB",
    **{"proteon": proteon,
       "proXfaceGenericTable": proXfaceGenericTable,
       "proXfaceGenericEntry": proXfaceGenericEntry,
       "proXfaceGenericType": proXfaceGenericType,
       "proXfaceGenericCSR": proXfaceGenericCSR,
       "proXfaceGenericIntVec": proXfaceGenericIntVec,
       "proXfaceGenericMaintInt": proXfaceGenericMaintInt,
       "proXfaceGenericMaintLim": proXfaceGenericMaintLim,
       "proXfaceGenericNextTest": proXfaceGenericNextTest,
       "proXfaceGenericNextMaint": proXfaceGenericNextMaint,
       "proXfaceGenericMaintCnt": proXfaceGenericMaintCnt,
       "proXfaceGenericMaintFails": proXfaceGenericMaintFails,
       "proXfaceGenericTestPasses": proXfaceGenericTestPasses,
       "proXfaceGenericTestFails": proXfaceGenericTestFails,
       "proXfaceGenericModuleId": proXfaceGenericModuleId,
       "proto": proto,
       "general": general,
       "proip": proip,
       "defgw": defgw,
       "proProtoIpDefGwAddress": proProtoIpDefGwAddress,
       "proProtoIpDefGwCost": proProtoIpDefGwCost,
       "proProtoIpDefGwAge": proProtoIpDefGwAge,
       "pDot3ChipSets": pDot3ChipSets,
       "pDot3ChipMC68EN360": pDot3ChipMC68EN360,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "ibm2210": ibm2210,
       "ibmElsTrapV1": ibmElsTrapV1,
       "ibmElsTrapV2": ibmElsTrapV2,
       "ibm2210admin": ibm2210admin,
       "ibm2210system": ibm2210system,
       "ibm2210hardware": ibm2210hardware,
       "ibm2210hardwareinfo": ibm2210hardwareinfo,
       "ibmServiceGenericTable": ibmServiceGenericTable,
       "ibmServiceGenericEntry": ibmServiceGenericEntry,
       "ibmServiceGenericPort": ibmServiceGenericPort,
       "ibmServiceGenericBaurdrate": ibmServiceGenericBaurdrate,
       "ibmServiceGenericType": ibmServiceGenericType,
       "ibm2210routing": ibm2210routing,
       "ibm2210switching": ibm2210switching}
)
