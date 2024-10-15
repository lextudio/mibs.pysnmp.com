# SNMP MIB module (AGILENT-ENTERPRISE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AGILENT-ENTERPRISE
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:58 2024
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

agilent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5053)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Reserved_ObjectIdentity = ObjectIdentity
reserved = _Reserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 0)
)
_AgilentDS_ObjectIdentity = ObjectIdentity
agilentDS = _AgilentDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 1)
)
_HpSmartInternet_ObjectIdentity = ObjectIdentity
hpSmartInternet = _HpSmartInternet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 1, 1)
)
_WebGuard_ObjectIdentity = ObjectIdentity
webGuard = _WebGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 1, 2)
)
_UxLDAP_ObjectIdentity = ObjectIdentity
uxLDAP = _UxLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 1, 3)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1)
)
_Iag_ObjectIdentity = ObjectIdentity
iag = _Iag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 1)
)
_Ing_ObjectIdentity = ObjectIdentity
ing = _Ing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 2)
)
_Osi_ObjectIdentity = ObjectIdentity
osi = _Osi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 2, 1)
)
_X400_ObjectIdentity = ObjectIdentity
x400 = _X400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 2, 1, 1)
)
_Ots_ObjectIdentity = ObjectIdentity
ots = _Ots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 2, 1, 2)
)
_Csg_ObjectIdentity = ObjectIdentity
csg = _Csg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 3)
)
_Nsml_ObjectIdentity = ObjectIdentity
nsml = _Nsml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 4)
)
_CommInfrastructure_ObjectIdentity = ObjectIdentity
commInfrastructure = _CommInfrastructure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 4, 1)
)
_Ino_ObjectIdentity = ObjectIdentity
ino = _Ino_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 5)
)
_Tmo_ObjectIdentity = ObjectIdentity
tmo = _Tmo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 6)
)
_Tmsd_ObjectIdentity = ObjectIdentity
tmsd = _Tmsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 6, 1)
)
_OvTraining_ObjectIdentity = ObjectIdentity
ovTraining = _OvTraining_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 7)
)
_Cmis_ObjectIdentity = ObjectIdentity
cmis = _Cmis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 7, 1)
)
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 7, 2)
)
_Issl_ObjectIdentity = ObjectIdentity
issl = _Issl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 1, 8)
)
_Auth_ObjectIdentity = ObjectIdentity
auth = _Auth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 1)
)
_ComputerSystem_ObjectIdentity = ObjectIdentity
computerSystem = _ComputerSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 1, 1)
)
_FileSystem_ObjectIdentity = ObjectIdentity
fileSystem = _FileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 1, 2)
)
_MpXLSystem_ObjectIdentity = ObjectIdentity
mpXLSystem = _MpXLSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 1, 3)
)
_Processes_ObjectIdentity = ObjectIdentity
processes = _Processes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 1, 4)
)
_Cluster_ObjectIdentity = ObjectIdentity
cluster = _Cluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 1, 5)
)
_McCluster_ObjectIdentity = ObjectIdentity
mcCluster = _McCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 1, 6)
)
_HpUDR_ObjectIdentity = ObjectIdentity
hpUDR = _HpUDR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 1, 7)
)
_Hpux_ObjectIdentity = ObjectIdentity
hpux = _Hpux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 2)
)
_HpuxGeneral_ObjectIdentity = ObjectIdentity
hpuxGeneral = _HpuxGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 2, 1)
)
_Hp9000s300_ObjectIdentity = ObjectIdentity
hp9000s300 = _Hp9000s300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 2, 2)
)
_Hp9000s800_ObjectIdentity = ObjectIdentity
hp9000s800 = _Hp9000s800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 2, 3)
)
_Hp9000s400_ObjectIdentity = ObjectIdentity
hp9000s400 = _Hp9000s400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 2, 4)
)
_Hp9000s700_ObjectIdentity = ObjectIdentity
hp9000s700 = _Hp9000s700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 2, 5)
)
_MpeV_ObjectIdentity = ObjectIdentity
mpeV = _MpeV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 3)
)
_MpeVGeneral_ObjectIdentity = ObjectIdentity
mpeVGeneral = _MpeVGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 3, 1)
)
_Hp3000s3x_ObjectIdentity = ObjectIdentity
hp3000s3x = _Hp3000s3x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 3, 2)
)
_Hp3000s4x_ObjectIdentity = ObjectIdentity
hp3000s4x = _Hp3000s4x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 3, 3)
)
_MpeXL_ObjectIdentity = ObjectIdentity
mpeXL = _MpeXL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 4)
)
_MpeXLGeneral_ObjectIdentity = ObjectIdentity
mpeXLGeneral = _MpeXLGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 4, 1)
)
_Hp3000s92x_ObjectIdentity = ObjectIdentity
hp3000s92x = _Hp3000s92x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 4, 2)
)
_Hp3000s93x_ObjectIdentity = ObjectIdentity
hp3000s93x = _Hp3000s93x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 4, 3)
)
_Hp3000s5x_ObjectIdentity = ObjectIdentity
hp3000s5x = _Hp3000s5x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 4, 4)
)
_Hp3000s6x_ObjectIdentity = ObjectIdentity
hp3000s6x = _Hp3000s6x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 4, 5)
)
_HpDOS_ObjectIdentity = ObjectIdentity
hpDOS = _HpDOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 5)
)
_HpOS2_ObjectIdentity = ObjectIdentity
hpOS2 = _HpOS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 6)
)
_NetElement_ObjectIdentity = ObjectIdentity
netElement = _NetElement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7)
)
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 1)
)
_Bridge1010_ObjectIdentity = ObjectIdentity
bridge1010 = _Bridge1010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 1, 1)
)
_BridgeRemote_ObjectIdentity = ObjectIdentity
bridgeRemote = _BridgeRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 1, 2)
)
_Eswitch_ObjectIdentity = ObjectIdentity
eswitch = _Eswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 1, 3)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 2)
)
_Dtc_ObjectIdentity = ObjectIdentity
dtc = _Dtc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 3)
)
_DtcGeneral_ObjectIdentity = ObjectIdentity
dtcGeneral = _DtcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 3, 1)
)
_Dtc48_ObjectIdentity = ObjectIdentity
dtc48 = _Dtc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 3, 2)
)
_Dtc16_ObjectIdentity = ObjectIdentity
dtc16 = _Dtc16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 3, 3)
)
_DtcTeb_ObjectIdentity = ObjectIdentity
dtcTeb = _DtcTeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 3, 4)
)
_Dtc72mx_ObjectIdentity = ObjectIdentity
dtc72mx = _Dtc72mx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 3, 5)
)
_Dtc16tn_ObjectIdentity = ObjectIdentity
dtc16tn = _Dtc16tn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 3, 6)
)
_Dtc16mx_ObjectIdentity = ObjectIdentity
dtc16mx = _Dtc16mx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 3, 7)
)
_Dtc16ix_ObjectIdentity = ObjectIdentity
dtc16ix = _Dtc16ix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 3, 8)
)
_Modem_ObjectIdentity = ObjectIdentity
modem = _Modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 4)
)
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 5)
)
_Ethertwist12A_ObjectIdentity = ObjectIdentity
ethertwist12A = _Ethertwist12A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 5, 1)
)
_Ethertwist12B_ObjectIdentity = ObjectIdentity
ethertwist12B = _Ethertwist12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 5, 2)
)
_FiberOptic_ObjectIdentity = ObjectIdentity
fiberOptic = _FiberOptic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 5, 3)
)
_Ethertwist48_ObjectIdentity = ObjectIdentity
ethertwist48 = _Ethertwist48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 5, 4)
)
_ThinLAN_ObjectIdentity = ObjectIdentity
thinLAN = _ThinLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 5, 5)
)
_Ethertwist24S_ObjectIdentity = ObjectIdentity
ethertwist24S = _Ethertwist24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 5, 6)
)
_HpHub7_ObjectIdentity = ObjectIdentity
hpHub7 = _HpHub7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 5, 7)
)
_HpHub8_ObjectIdentity = ObjectIdentity
hpHub8 = _HpHub8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 5, 8)
)
_HpHub9_ObjectIdentity = ObjectIdentity
hpHub9 = _HpHub9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 5, 9)
)
_HpFCHubA3724A_ObjectIdentity = ObjectIdentity
hpFCHubA3724A = _HpFCHubA3724A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 5, 10)
)
_HpFCHubD6976A_ObjectIdentity = ObjectIdentity
hpFCHubD6976A = _HpFCHubD6976A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 5, 11)
)
_Lanprobe_ObjectIdentity = ObjectIdentity
lanprobe = _Lanprobe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 6)
)
_Packetswitch_ObjectIdentity = ObjectIdentity
packetswitch = _Packetswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 7)
)
_Model45_ObjectIdentity = ObjectIdentity
model45 = _Model45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 7, 1)
)
_Model233x_ObjectIdentity = ObjectIdentity
model233x = _Model233x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 7, 2)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 8)
)
_RepeaterAgent_ObjectIdentity = ObjectIdentity
repeaterAgent = _RepeaterAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 8, 1)
)
_Advisor_ObjectIdentity = ObjectIdentity
advisor = _Advisor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 9)
)
_AdvisorGeneral_ObjectIdentity = ObjectIdentity
advisorGeneral = _AdvisorGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 9, 1)
)
_HpFCSwitch_ObjectIdentity = ObjectIdentity
hpFCSwitch = _HpFCSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 10)
)
_Polaris_ObjectIdentity = ObjectIdentity
polaris = _Polaris_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 10, 1)
)
_Nimbus_ObjectIdentity = ObjectIdentity
nimbus = _Nimbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 10, 2)
)
_HpFCSwitchA5420_ObjectIdentity = ObjectIdentity
hpFCSwitchA5420 = _HpFCSwitchA5420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 10, 3)
)
_HpEtherSwitch_ObjectIdentity = ObjectIdentity
hpEtherSwitch = _HpEtherSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 11)
)
_HpCableRouter_ObjectIdentity = ObjectIdentity
hpCableRouter = _HpCableRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 12)
)
_HpBSTS_ObjectIdentity = ObjectIdentity
hpBSTS = _HpBSTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 13)
)
_HpBSTS_OC3_ObjectIdentity = ObjectIdentity
hpBSTS_OC3 = _HpBSTS_OC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 13, 1)
)
_MANOXC_ObjectIdentity = ObjectIdentity
mANOXC = _MANOXC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 7, 14)
)
_Hp386_ObjectIdentity = ObjectIdentity
hp386 = _Hp386_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 8)
)
_NetPeripheral_ObjectIdentity = ObjectIdentity
netPeripheral = _NetPeripheral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9)
)
_NetPrinter_ObjectIdentity = ObjectIdentity
netPrinter = _NetPrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 1)
)
_NetPlotter_ObjectIdentity = ObjectIdentity
netPlotter = _NetPlotter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 2)
)
_HpXStation_ObjectIdentity = ObjectIdentity
hpXStation = _HpXStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 3)
)
_NetPML_ObjectIdentity = ObjectIdentity
netPML = _NetPML_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 4)
)
_NetPMLadmin_ObjectIdentity = ObjectIdentity
netPMLadmin = _NetPMLadmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 4, 1)
)
_NetPMLmgmt_ObjectIdentity = ObjectIdentity
netPMLmgmt = _NetPMLmgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 4, 2)
)
_NetScanner_ObjectIdentity = ObjectIdentity
netScanner = _NetScanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 5)
)
_NetMultiFn_ObjectIdentity = ObjectIdentity
netMultiFn = _NetMultiFn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 6)
)
_NetTape_ObjectIdentity = ObjectIdentity
netTape = _NetTape_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 7)
)
_NetCdRomServer_ObjectIdentity = ObjectIdentity
netCdRomServer = _NetCdRomServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 8)
)
_HpStorageSystem_ObjectIdentity = ObjectIdentity
hpStorageSystem = _HpStorageSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 9)
)
_HpNASServer_ObjectIdentity = ObjectIdentity
hpNASServer = _HpNASServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 10)
)
_HpWinTerm_ObjectIdentity = ObjectIdentity
hpWinTerm = _HpWinTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 11)
)
_HpNetworkStorage_ObjectIdentity = ObjectIdentity
hpNetworkStorage = _HpNetworkStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 9, 12)
)
_Hpsun_ObjectIdentity = ObjectIdentity
hpsun = _Hpsun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 10)
)
_Sparc_ObjectIdentity = ObjectIdentity
sparc = _Sparc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 10, 1)
)
_Sun4_ObjectIdentity = ObjectIdentity
sun4 = _Sun4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 10, 1, 1)
)
_Sun5_ObjectIdentity = ObjectIdentity
sun5 = _Sun5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 10, 1, 2)
)
_HpFX_ObjectIdentity = ObjectIdentity
hpFX = _HpFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 11)
)
_HpFXgeneral_ObjectIdentity = ObjectIdentity
hpFXgeneral = _HpFXgeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 11, 1)
)
_Hp9000s12xx_ObjectIdentity = ObjectIdentity
hp9000s12xx = _Hp9000s12xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 11, 2)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 12)
)
_FujistuXXX_ObjectIdentity = ObjectIdentity
fujistuXXX = _FujistuXXX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 12, 1)
)
_RelianceYYY_ObjectIdentity = ObjectIdentity
relianceYYY = _RelianceYYY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 12, 2)
)
_HpAtt_ObjectIdentity = ObjectIdentity
hpAtt = _HpAtt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 13)
)
_Gis_ObjectIdentity = ObjectIdentity
gis = _Gis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 13, 1)
)
_HpWinNT_ObjectIdentity = ObjectIdentity
hpWinNT = _HpWinNT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 3, 14)
)
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 4)
)
_Ieee8023Mac_ObjectIdentity = ObjectIdentity
ieee8023Mac = _Ieee8023Mac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 4, 1)
)
_Ieee8025_ObjectIdentity = ObjectIdentity
ieee8025 = _Ieee8025_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 4, 2)
)
_NpCard_ObjectIdentity = ObjectIdentity
npCard = _NpCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 4, 3)
)
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 4, 4)
)
_Serial_ObjectIdentity = ObjectIdentity
serial = _Serial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 4, 5)
)
_Net_ObjectIdentity = ObjectIdentity
net = _Net_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 4, 6)
)
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 4, 7)
)
_PvcMIB_ObjectIdentity = ObjectIdentity
pvcMIB = _PvcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 4, 8)
)
_VlanMIB_ObjectIdentity = ObjectIdentity
vlanMIB = _VlanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 4, 9)
)
_At_ObjectIdentity = ObjectIdentity
at = _At_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 5)
)
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 6)
)
_Icmp_ObjectIdentity = ObjectIdentity
icmp = _Icmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 7)
)
_Tcp_ObjectIdentity = ObjectIdentity
tcp = _Tcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 8)
)
_Udp_ObjectIdentity = ObjectIdentity
udp = _Udp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 9)
)
_Egp_ObjectIdentity = ObjectIdentity
egp = _Egp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 10)
)
_Cmot_ObjectIdentity = ObjectIdentity
cmot = _Cmot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 11)
)
_Tansmission_ObjectIdentity = ObjectIdentity
tansmission = _Tansmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 12)
)
_Snmp_hp_ObjectIdentity = ObjectIdentity
snmp_hp = _Snmp_hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 13)
)
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 13, 1)
)
_SnmpdConf_ObjectIdentity = ObjectIdentity
snmpdConf = _SnmpdConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 13, 2)
)
_SnmpdAgent_ObjectIdentity = ObjectIdentity
snmpdAgent = _SnmpdAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 13, 3)
)
_Authfail_ObjectIdentity = ObjectIdentity
authfail = _Authfail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 13, 4)
)
_Community_ObjectIdentity = ObjectIdentity
community = _Community_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 13, 5)
)
_Icf_ObjectIdentity = ObjectIdentity
icf = _Icf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 14)
)
_IcfCommon_ObjectIdentity = ObjectIdentity
icfCommon = _IcfCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 14, 1)
)
_IcfHub_ObjectIdentity = ObjectIdentity
icfHub = _IcfHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 14, 2)
)
_IcfBridge_ObjectIdentity = ObjectIdentity
icfBridge = _IcfBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 14, 3)
)
_IcfEswitch_ObjectIdentity = ObjectIdentity
icfEswitch = _IcfEswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 14, 6)
)
_Slip_ObjectIdentity = ObjectIdentity
slip = _Slip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 15)
)
_SamplingProbe_ObjectIdentity = ObjectIdentity
samplingProbe = _SamplingProbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 16)
)
_OpenView_ObjectIdentity = ObjectIdentity
openView = _OpenView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17)
)
_HpOpenView_ObjectIdentity = ObjectIdentity
hpOpenView = _HpOpenView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17, 1)
)
_OpenViewTrapVars_ObjectIdentity = ObjectIdentity
openViewTrapVars = _OpenViewTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17, 2)
)
_OpenViewForWin_ObjectIdentity = ObjectIdentity
openViewForWin = _OpenViewForWin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17, 3)
)
_HpOVDistribStation_ObjectIdentity = ObjectIdentity
hpOVDistribStation = _HpOVDistribStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17, 4)
)
_HpOVSNMPSecurity_ObjectIdentity = ObjectIdentity
hpOVSNMPSecurity = _HpOVSNMPSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17, 5)
)
_HpOVEventMIB_ObjectIdentity = ObjectIdentity
hpOVEventMIB = _HpOVEventMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17, 6)
)
_HpOVExpose_ObjectIdentity = ObjectIdentity
hpOVExpose = _HpOVExpose_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17, 7)
)
_HpOVExposeTraps_ObjectIdentity = ObjectIdentity
hpOVExposeTraps = _HpOVExposeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17, 7, 0)
)
_HpOVDTAdmin_ObjectIdentity = ObjectIdentity
hpOVDTAdmin = _HpOVDTAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17, 8)
)
_HpOVUserDefnEvents_ObjectIdentity = ObjectIdentity
hpOVUserDefnEvents = _HpOVUserDefnEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17, 9)
)
_HpOVNodeSentry_ObjectIdentity = ObjectIdentity
hpOVNodeSentry = _HpOVNodeSentry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17, 10)
)
_HpOVSanManager_ObjectIdentity = ObjectIdentity
hpOVSanManager = _HpOVSanManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17, 11)
)
_HpOVPolicyExpert_ObjectIdentity = ObjectIdentity
hpOVPolicyExpert = _HpOVPolicyExpert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 17, 12)
)
_Unknown18_ObjectIdentity = ObjectIdentity
unknown18 = _Unknown18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 18)
)
_Unknown19_ObjectIdentity = ObjectIdentity
unknown19 = _Unknown19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 19)
)
_Ieee8022_ObjectIdentity = ObjectIdentity
ieee8022 = _Ieee8022_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 20)
)
_Nmpacketswitch_ObjectIdentity = ObjectIdentity
nmpacketswitch = _Nmpacketswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 21)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 21, 1)
)
_Proxy_ObjectIdentity = ObjectIdentity
proxy = _Proxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 21, 2)
)
_M45_ObjectIdentity = ObjectIdentity
m45 = _M45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 21, 3)
)
_Hp233x_ObjectIdentity = ObjectIdentity
hp233x = _Hp233x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 21, 4)
)
_HpNSA_ObjectIdentity = ObjectIdentity
hpNSA = _HpNSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 23)
)
_SwitchManager_ObjectIdentity = ObjectIdentity
switchManager = _SwitchManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 24)
)
_NetmonProxy_ObjectIdentity = ObjectIdentity
netmonProxy = _NetmonProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 25)
)
_HpUPS_ObjectIdentity = ObjectIdentity
hpUPS = _HpUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 26)
)
_HpStorageAssistant_ObjectIdentity = ObjectIdentity
hpStorageAssistant = _HpStorageAssistant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 27)
)
_AgilentEase_ObjectIdentity = ObjectIdentity
agilentEase = _AgilentEase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 28)
)
_InNetElem_ObjectIdentity = ObjectIdentity
inNetElem = _InNetElem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 29)
)
_AgilentNTDFaultMgt_ObjectIdentity = ObjectIdentity
agilentNTDFaultMgt = _AgilentNTDFaultMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 30)
)
_HpFibreChannel_ObjectIdentity = ObjectIdentity
hpFibreChannel = _HpFibreChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 31)
)
_HpRSM_ObjectIdentity = ObjectIdentity
hpRSM = _HpRSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 32)
)
_HpBMP_ObjectIdentity = ObjectIdentity
hpBMP = _HpBMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 33)
)
_HpMediaStream_ObjectIdentity = ObjectIdentity
hpMediaStream = _HpMediaStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 34)
)
_HpDMC_ObjectIdentity = ObjectIdentity
hpDMC = _HpDMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 35)
)
_AgilentWebMgt_ObjectIdentity = ObjectIdentity
agilentWebMgt = _AgilentWebMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 36)
)
_HpisdnAcc_ObjectIdentity = ObjectIdentity
hpisdnAcc = _HpisdnAcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 37)
)
_HpQuickBurst_ObjectIdentity = ObjectIdentity
hpQuickBurst = _HpQuickBurst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 38)
)
_HpOEMF_ObjectIdentity = ObjectIdentity
hpOEMF = _HpOEMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 39)
)
_HpUPSMgt_ObjectIdentity = ObjectIdentity
hpUPSMgt = _HpUPSMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 40)
)
_HpObsolete41_ObjectIdentity = ObjectIdentity
hpObsolete41 = _HpObsolete41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 41)
)
_AgilentFirehunter_ObjectIdentity = ObjectIdentity
agilentFirehunter = _AgilentFirehunter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 42)
)
_AgilentRFTS_ObjectIdentity = ObjectIdentity
agilentRFTS = _AgilentRFTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 43)
)
_Access7_ObjectIdentity = ObjectIdentity
access7 = _Access7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 44)
)
_BroadbandProbeChassis_ObjectIdentity = ObjectIdentity
broadbandProbeChassis = _BroadbandProbeChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 2, 45)
)
_AgilentMPG_ObjectIdentity = ObjectIdentity
agilentMPG = _AgilentMPG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 3)
)
_AgilentIT_ObjectIdentity = ObjectIdentity
agilentIT = _AgilentIT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 4)
)
_AgilentSysMgt_ObjectIdentity = ObjectIdentity
agilentSysMgt = _AgilentSysMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 5)
)
_HpDesktopPC_ObjectIdentity = ObjectIdentity
hpDesktopPC = _HpDesktopPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 5, 1)
)
_HpMobilePC_ObjectIdentity = ObjectIdentity
hpMobilePC = _HpMobilePC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 5, 2)
)
_Unused_ObjectIdentity = ObjectIdentity
unused = _Unused_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 5, 3)
)
_HpUXSysMgt_ObjectIdentity = ObjectIdentity
hpUXSysMgt = _HpUXSysMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 5, 4)
)
_HpIgniteUX_ObjectIdentity = ObjectIdentity
hpIgniteUX = _HpIgniteUX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 5, 4, 1)
)
_AgilentRemotePCMgt_ObjectIdentity = ObjectIdentity
agilentRemotePCMgt = _AgilentRemotePCMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 5, 5)
)
_HpChai_ObjectIdentity = ObjectIdentity
hpChai = _HpChai_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 5, 6)
)
_HpChina_ObjectIdentity = ObjectIdentity
hpChina = _HpChina_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 6)
)
_HpInternetApps_ObjectIdentity = ObjectIdentity
hpInternetApps = _HpInternetApps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 7)
)
_HpFrontOffice_ObjectIdentity = ObjectIdentity
hpFrontOffice = _HpFrontOffice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 7, 1)
)
_HpMalaysia_ObjectIdentity = ObjectIdentity
hpMalaysia = _HpMalaysia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 8)
)
_HpTaiwan_ObjectIdentity = ObjectIdentity
hpTaiwan = _HpTaiwan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5053, 9)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AGILENT-ENTERPRISE",
    **{"agilent": agilent,
       "reserved": reserved,
       "agilentDS": agilentDS,
       "hpSmartInternet": hpSmartInternet,
       "webGuard": webGuard,
       "uxLDAP": uxLDAP,
       "nm": nm,
       "experimental": experimental,
       "iag": iag,
       "ing": ing,
       "osi": osi,
       "x400": x400,
       "ots": ots,
       "csg": csg,
       "nsml": nsml,
       "commInfrastructure": commInfrastructure,
       "ino": ino,
       "tmo": tmo,
       "tmsd": tmsd,
       "ovTraining": ovTraining,
       "cmis": cmis,
       "snmp": snmp,
       "issl": issl,
       "auth": auth,
       "system": system,
       "general": general,
       "computerSystem": computerSystem,
       "fileSystem": fileSystem,
       "mpXLSystem": mpXLSystem,
       "processes": processes,
       "cluster": cluster,
       "mcCluster": mcCluster,
       "hpUDR": hpUDR,
       "hpux": hpux,
       "hpuxGeneral": hpuxGeneral,
       "hp9000s300": hp9000s300,
       "hp9000s800": hp9000s800,
       "hp9000s400": hp9000s400,
       "hp9000s700": hp9000s700,
       "mpeV": mpeV,
       "mpeVGeneral": mpeVGeneral,
       "hp3000s3x": hp3000s3x,
       "hp3000s4x": hp3000s4x,
       "mpeXL": mpeXL,
       "mpeXLGeneral": mpeXLGeneral,
       "hp3000s92x": hp3000s92x,
       "hp3000s93x": hp3000s93x,
       "hp3000s5x": hp3000s5x,
       "hp3000s6x": hp3000s6x,
       "hpDOS": hpDOS,
       "hpOS2": hpOS2,
       "netElement": netElement,
       "bridge": bridge,
       "bridge1010": bridge1010,
       "bridgeRemote": bridgeRemote,
       "eswitch": eswitch,
       "router": router,
       "dtc": dtc,
       "dtcGeneral": dtcGeneral,
       "dtc48": dtc48,
       "dtc16": dtc16,
       "dtcTeb": dtcTeb,
       "dtc72mx": dtc72mx,
       "dtc16tn": dtc16tn,
       "dtc16mx": dtc16mx,
       "dtc16ix": dtc16ix,
       "modem": modem,
       "hub": hub,
       "ethertwist12A": ethertwist12A,
       "ethertwist12B": ethertwist12B,
       "fiberOptic": fiberOptic,
       "ethertwist48": ethertwist48,
       "thinLAN": thinLAN,
       "ethertwist24S": ethertwist24S,
       "hpHub7": hpHub7,
       "hpHub8": hpHub8,
       "hpHub9": hpHub9,
       "hpFCHubA3724A": hpFCHubA3724A,
       "hpFCHubD6976A": hpFCHubD6976A,
       "lanprobe": lanprobe,
       "packetswitch": packetswitch,
       "model45": model45,
       "model233x": model233x,
       "chassis": chassis,
       "repeaterAgent": repeaterAgent,
       "advisor": advisor,
       "advisorGeneral": advisorGeneral,
       "hpFCSwitch": hpFCSwitch,
       "polaris": polaris,
       "nimbus": nimbus,
       "hpFCSwitchA5420": hpFCSwitchA5420,
       "hpEtherSwitch": hpEtherSwitch,
       "hpCableRouter": hpCableRouter,
       "hpBSTS": hpBSTS,
       "hpBSTS-OC3": hpBSTS_OC3,
       "mANOXC": mANOXC,
       "hp386": hp386,
       "netPeripheral": netPeripheral,
       "netPrinter": netPrinter,
       "netPlotter": netPlotter,
       "hpXStation": hpXStation,
       "netPML": netPML,
       "netPMLadmin": netPMLadmin,
       "netPMLmgmt": netPMLmgmt,
       "netScanner": netScanner,
       "netMultiFn": netMultiFn,
       "netTape": netTape,
       "netCdRomServer": netCdRomServer,
       "hpStorageSystem": hpStorageSystem,
       "hpNASServer": hpNASServer,
       "hpWinTerm": hpWinTerm,
       "hpNetworkStorage": hpNetworkStorage,
       "hpsun": hpsun,
       "sparc": sparc,
       "sun4": sun4,
       "sun5": sun5,
       "hpFX": hpFX,
       "hpFXgeneral": hpFXgeneral,
       "hp9000s12xx": hp9000s12xx,
       "switch": switch,
       "fujistuXXX": fujistuXXX,
       "relianceYYY": relianceYYY,
       "hpAtt": hpAtt,
       "gis": gis,
       "hpWinNT": hpWinNT,
       "interface": interface,
       "ieee8023Mac": ieee8023Mac,
       "ieee8025": ieee8025,
       "npCard": npCard,
       "ethernet": ethernet,
       "serial": serial,
       "net": net,
       "tokenRing": tokenRing,
       "pvcMIB": pvcMIB,
       "vlanMIB": vlanMIB,
       "at": at,
       "ip": ip,
       "icmp": icmp,
       "tcp": tcp,
       "udp": udp,
       "egp": egp,
       "cmot": cmot,
       "tansmission": tansmission,
       "snmp-hp": snmp_hp,
       "trap": trap,
       "snmpdConf": snmpdConf,
       "snmpdAgent": snmpdAgent,
       "authfail": authfail,
       "community": community,
       "icf": icf,
       "icfCommon": icfCommon,
       "icfHub": icfHub,
       "icfBridge": icfBridge,
       "icfEswitch": icfEswitch,
       "slip": slip,
       "samplingProbe": samplingProbe,
       "openView": openView,
       "hpOpenView": hpOpenView,
       "openViewTrapVars": openViewTrapVars,
       "openViewForWin": openViewForWin,
       "hpOVDistribStation": hpOVDistribStation,
       "hpOVSNMPSecurity": hpOVSNMPSecurity,
       "hpOVEventMIB": hpOVEventMIB,
       "hpOVExpose": hpOVExpose,
       "hpOVExposeTraps": hpOVExposeTraps,
       "hpOVDTAdmin": hpOVDTAdmin,
       "hpOVUserDefnEvents": hpOVUserDefnEvents,
       "hpOVNodeSentry": hpOVNodeSentry,
       "hpOVSanManager": hpOVSanManager,
       "hpOVPolicyExpert": hpOVPolicyExpert,
       "unknown18": unknown18,
       "unknown19": unknown19,
       "ieee8022": ieee8022,
       "nmpacketswitch": nmpacketswitch,
       "common": common,
       "proxy": proxy,
       "m45": m45,
       "hp233x": hp233x,
       "hpNSA": hpNSA,
       "switchManager": switchManager,
       "netmonProxy": netmonProxy,
       "hpUPS": hpUPS,
       "hpStorageAssistant": hpStorageAssistant,
       "agilentEase": agilentEase,
       "inNetElem": inNetElem,
       "agilentNTDFaultMgt": agilentNTDFaultMgt,
       "hpFibreChannel": hpFibreChannel,
       "hpRSM": hpRSM,
       "hpBMP": hpBMP,
       "hpMediaStream": hpMediaStream,
       "hpDMC": hpDMC,
       "agilentWebMgt": agilentWebMgt,
       "hpisdnAcc": hpisdnAcc,
       "hpQuickBurst": hpQuickBurst,
       "hpOEMF": hpOEMF,
       "hpUPSMgt": hpUPSMgt,
       "hpObsolete41": hpObsolete41,
       "agilentFirehunter": agilentFirehunter,
       "agilentRFTS": agilentRFTS,
       "access7": access7,
       "broadbandProbeChassis": broadbandProbeChassis,
       "agilentMPG": agilentMPG,
       "agilentIT": agilentIT,
       "agilentSysMgt": agilentSysMgt,
       "hpDesktopPC": hpDesktopPC,
       "hpMobilePC": hpMobilePC,
       "unused": unused,
       "hpUXSysMgt": hpUXSysMgt,
       "hpIgniteUX": hpIgniteUX,
       "agilentRemotePCMgt": agilentRemotePCMgt,
       "hpChai": hpChai,
       "hpChina": hpChina,
       "hpInternetApps": hpInternetApps,
       "hpFrontOffice": hpFrontOffice,
       "hpMalaysia": hpMalaysia,
       "hpTaiwan": hpTaiwan}
)
