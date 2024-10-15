# SNMP MIB module (XMSERVD-PERF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XMSERVD-PERF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:45 2024
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
 internet,
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
    "internet",
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

_Directory_ObjectIdentity = ObjectIdentity
directory = _Directory_ObjectIdentity(
    (1, 3, 6, 1, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmAgents_ObjectIdentity = ObjectIdentity
ibmAgents = _IbmAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3)
)
_Aix_ObjectIdentity = ObjectIdentity
aix = _Aix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1)
)
_AixRT_ObjectIdentity = ObjectIdentity
aixRT = _AixRT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 1)
)
_AixRISC6000_ObjectIdentity = ObjectIdentity
aixRISC6000 = _AixRISC6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2)
)
_Risc6000agents_ObjectIdentity = ObjectIdentity
risc6000agents = _Risc6000agents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 1)
)
_Risc6000snmpd_ObjectIdentity = ObjectIdentity
risc6000snmpd = _Risc6000snmpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 1, 1)
)
_Risc6000gated_ObjectIdentity = ObjectIdentity
risc6000gated = _Risc6000gated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 1, 2)
)
_Risc6000xmservd_ObjectIdentity = ObjectIdentity
risc6000xmservd = _Risc6000xmservd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 1, 3)
)
_Risc6000ibm7318_ObjectIdentity = ObjectIdentity
risc6000ibm7318 = _Risc6000ibm7318_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 1, 4)
)
_Risc6000clsmuxpd_ObjectIdentity = ObjectIdentity
risc6000clsmuxpd = _Risc6000clsmuxpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 1, 5)
)
_Risc6000private_ObjectIdentity = ObjectIdentity
risc6000private = _Risc6000private_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2)
)
_Risc6000samples_ObjectIdentity = ObjectIdentity
risc6000samples = _Risc6000samples_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 1)
)
_Risc6000sampleAgents_ObjectIdentity = ObjectIdentity
risc6000sampleAgents = _Risc6000sampleAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 1, 1)
)
_Risc6000perf_ObjectIdentity = ObjectIdentity
risc6000perf = _Risc6000perf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2)
)
_Xmd_ObjectIdentity = ObjectIdentity
xmd = _Xmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1)
)
_XmdCPU_ObjectIdentity = ObjectIdentity
xmdCPU = _XmdCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 1)
)
_XmdCPUGluser_Type = Integer32
_XmdCPUGluser_Object = MibScalar
xmdCPUGluser = _XmdCPUGluser_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 1, 101),
    _XmdCPUGluser_Type()
)
xmdCPUGluser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdCPUGluser.setStatus("mandatory")
_XmdCPUGlkern_Type = Integer32
_XmdCPUGlkern_Object = MibScalar
xmdCPUGlkern = _XmdCPUGlkern_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 1, 102),
    _XmdCPUGlkern_Type()
)
xmdCPUGlkern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdCPUGlkern.setStatus("mandatory")
_XmdCPUGlwait_Type = Integer32
_XmdCPUGlwait_Object = MibScalar
xmdCPUGlwait = _XmdCPUGlwait_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 1, 103),
    _XmdCPUGlwait_Type()
)
xmdCPUGlwait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdCPUGlwait.setStatus("mandatory")
_XmdCPUGlidle_Type = Integer32
_XmdCPUGlidle_Object = MibScalar
xmdCPUGlidle = _XmdCPUGlidle_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 1, 104),
    _XmdCPUGlidle_Type()
)
xmdCPUGlidle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdCPUGlidle.setStatus("mandatory")
_XmdCPUGluticks_Type = Counter32
_XmdCPUGluticks_Object = MibScalar
xmdCPUGluticks = _XmdCPUGluticks_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 1, 121),
    _XmdCPUGluticks_Type()
)
xmdCPUGluticks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdCPUGluticks.setStatus("mandatory")
_XmdCPUGlkticks_Type = Counter32
_XmdCPUGlkticks_Object = MibScalar
xmdCPUGlkticks = _XmdCPUGlkticks_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 1, 122),
    _XmdCPUGlkticks_Type()
)
xmdCPUGlkticks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdCPUGlkticks.setStatus("mandatory")
_XmdCPUGlwticks_Type = Counter32
_XmdCPUGlwticks_Object = MibScalar
xmdCPUGlwticks = _XmdCPUGlwticks_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 1, 123),
    _XmdCPUGlwticks_Type()
)
xmdCPUGlwticks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdCPUGlwticks.setStatus("mandatory")
_XmdCPUGliticks_Type = Counter32
_XmdCPUGliticks_Object = MibScalar
xmdCPUGliticks = _XmdCPUGliticks_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 1, 124),
    _XmdCPUGliticks_Type()
)
xmdCPUGliticks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdCPUGliticks.setStatus("mandatory")
_XmdMem_ObjectIdentity = ObjectIdentity
xmdMem = _XmdMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2)
)
_XmdMemReal_ObjectIdentity = ObjectIdentity
xmdMemReal = _XmdMemReal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1)
)
_XmdMemRealSize_Type = Integer32
_XmdMemRealSize_Object = MibScalar
xmdMemRealSize = _XmdMemRealSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 1),
    _XmdMemRealSize_Type()
)
xmdMemRealSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealSize.setStatus("mandatory")
_XmdMemRealNumfrb_Type = Integer32
_XmdMemRealNumfrb_Object = MibScalar
xmdMemRealNumfrb = _XmdMemRealNumfrb_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 2),
    _XmdMemRealNumfrb_Type()
)
xmdMemRealNumfrb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealNumfrb.setStatus("mandatory")
_XmdMemRealNoncomp_Type = Integer32
_XmdMemRealNoncomp_Object = MibScalar
xmdMemRealNoncomp = _XmdMemRealNoncomp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 3),
    _XmdMemRealNoncomp_Type()
)
xmdMemRealNoncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealNoncomp.setStatus("mandatory")
_XmdMemRealComp_Type = Integer32
_XmdMemRealComp_Object = MibScalar
xmdMemRealComp = _XmdMemRealComp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 4),
    _XmdMemRealComp_Type()
)
xmdMemRealComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealComp.setStatus("mandatory")
_XmdMemRealNumlocal_Type = Integer32
_XmdMemRealNumlocal_Object = MibScalar
xmdMemRealNumlocal = _XmdMemRealNumlocal_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 5),
    _XmdMemRealNumlocal_Type()
)
xmdMemRealNumlocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealNumlocal.setStatus("mandatory")
_XmdMemRealNumclient_Type = Integer32
_XmdMemRealNumclient_Object = MibScalar
xmdMemRealNumclient = _XmdMemRealNumclient_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 6),
    _XmdMemRealNumclient_Type()
)
xmdMemRealNumclient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealNumclient.setStatus("mandatory")
_XmdMemRealMaxclient_Type = Integer32
_XmdMemRealMaxclient_Object = MibScalar
xmdMemRealMaxclient = _XmdMemRealMaxclient_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 7),
    _XmdMemRealMaxclient_Type()
)
xmdMemRealMaxclient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealMaxclient.setStatus("mandatory")
_XmdMemRealPdecay_Type = Integer32
_XmdMemRealPdecay_Object = MibScalar
xmdMemRealPdecay = _XmdMemRealPdecay_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 8),
    _XmdMemRealPdecay_Type()
)
xmdMemRealPdecay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealPdecay.setStatus("mandatory")
_XmdMemRealSysrepag_Type = Integer32
_XmdMemRealSysrepag_Object = MibScalar
xmdMemRealSysrepag = _XmdMemRealSysrepag_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 9),
    _XmdMemRealSysrepag_Type()
)
xmdMemRealSysrepag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealSysrepag.setStatus("mandatory")
_XmdMemRealEfree_Type = Integer32
_XmdMemRealEfree_Object = MibScalar
xmdMemRealEfree = _XmdMemRealEfree_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 10),
    _XmdMemRealEfree_Type()
)
xmdMemRealEfree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealEfree.setStatus("mandatory")
_XmdMemRealEpinned_Type = Integer32
_XmdMemRealEpinned_Object = MibScalar
xmdMemRealEpinned = _XmdMemRealEpinned_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 11),
    _XmdMemRealEpinned_Type()
)
xmdMemRealEpinned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealEpinned.setStatus("mandatory")
_XmdMemRealEcomp_Type = Integer32
_XmdMemRealEcomp_Object = MibScalar
xmdMemRealEcomp = _XmdMemRealEcomp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 12),
    _XmdMemRealEcomp_Type()
)
xmdMemRealEcomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealEcomp.setStatus("mandatory")
_XmdMemRealEnoncomp_Type = Integer32
_XmdMemRealEnoncomp_Object = MibScalar
xmdMemRealEnoncomp = _XmdMemRealEnoncomp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 13),
    _XmdMemRealEnoncomp_Type()
)
xmdMemRealEnoncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealEnoncomp.setStatus("mandatory")
_XmdMemRealElocal_Type = Integer32
_XmdMemRealElocal_Object = MibScalar
xmdMemRealElocal = _XmdMemRealElocal_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 14),
    _XmdMemRealElocal_Type()
)
xmdMemRealElocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealElocal.setStatus("mandatory")
_XmdMemRealEclnt_Type = Integer32
_XmdMemRealEclnt_Object = MibScalar
xmdMemRealEclnt = _XmdMemRealEclnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 15),
    _XmdMemRealEclnt_Type()
)
xmdMemRealEclnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealEclnt.setStatus("mandatory")
_XmdMemRealWseguse_Type = Integer32
_XmdMemRealWseguse_Object = MibScalar
xmdMemRealWseguse = _XmdMemRealWseguse_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 16),
    _XmdMemRealWseguse_Type()
)
xmdMemRealWseguse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealWseguse.setStatus("mandatory")
_XmdMemRealPseguse_Type = Integer32
_XmdMemRealPseguse_Object = MibScalar
xmdMemRealPseguse = _XmdMemRealPseguse_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 17),
    _XmdMemRealPseguse_Type()
)
xmdMemRealPseguse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealPseguse.setStatus("mandatory")
_XmdMemRealClseguse_Type = Integer32
_XmdMemRealClseguse_Object = MibScalar
xmdMemRealClseguse = _XmdMemRealClseguse_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 18),
    _XmdMemRealClseguse_Type()
)
xmdMemRealClseguse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealClseguse.setStatus("mandatory")
_XmdMemRealWsegpin_Type = Integer32
_XmdMemRealWsegpin_Object = MibScalar
xmdMemRealWsegpin = _XmdMemRealWsegpin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 19),
    _XmdMemRealWsegpin_Type()
)
xmdMemRealWsegpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealWsegpin.setStatus("mandatory")
_XmdMemRealPsegpin_Type = Integer32
_XmdMemRealPsegpin_Object = MibScalar
xmdMemRealPsegpin = _XmdMemRealPsegpin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 20),
    _XmdMemRealPsegpin_Type()
)
xmdMemRealPsegpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealPsegpin.setStatus("mandatory")
_XmdMemRealClsegpin_Type = Integer32
_XmdMemRealClsegpin_Object = MibScalar
xmdMemRealClsegpin = _XmdMemRealClsegpin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 21),
    _XmdMemRealClsegpin_Type()
)
xmdMemRealClsegpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemRealClsegpin.setStatus("mandatory")
_XmdMemVirt_ObjectIdentity = ObjectIdentity
xmdMemVirt = _XmdMemVirt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2)
)
_XmdMemVirtPagein_Type = Counter32
_XmdMemVirtPagein_Object = MibScalar
xmdMemVirtPagein = _XmdMemVirtPagein_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 1),
    _XmdMemVirtPagein_Type()
)
xmdMemVirtPagein.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtPagein.setStatus("mandatory")
_XmdMemVirtPageout_Type = Counter32
_XmdMemVirtPageout_Object = MibScalar
xmdMemVirtPageout = _XmdMemVirtPageout_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 2),
    _XmdMemVirtPageout_Type()
)
xmdMemVirtPageout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtPageout.setStatus("mandatory")
_XmdMemVirtPgspgin_Type = Counter32
_XmdMemVirtPgspgin_Object = MibScalar
xmdMemVirtPgspgin = _XmdMemVirtPgspgin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 3),
    _XmdMemVirtPgspgin_Type()
)
xmdMemVirtPgspgin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtPgspgin.setStatus("mandatory")
_XmdMemVirtPgspgout_Type = Counter32
_XmdMemVirtPgspgout_Object = MibScalar
xmdMemVirtPgspgout = _XmdMemVirtPgspgout_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 4),
    _XmdMemVirtPgspgout_Type()
)
xmdMemVirtPgspgout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtPgspgout.setStatus("mandatory")
_XmdMemVirtSio_Type = Counter32
_XmdMemVirtSio_Object = MibScalar
xmdMemVirtSio = _XmdMemVirtSio_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 5),
    _XmdMemVirtSio_Type()
)
xmdMemVirtSio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtSio.setStatus("mandatory")
_XmdMemVirtIodone_Type = Counter32
_XmdMemVirtIodone_Object = MibScalar
xmdMemVirtIodone = _XmdMemVirtIodone_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 6),
    _XmdMemVirtIodone_Type()
)
xmdMemVirtIodone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtIodone.setStatus("mandatory")
_XmdMemVirtZerofill_Type = Counter32
_XmdMemVirtZerofill_Object = MibScalar
xmdMemVirtZerofill = _XmdMemVirtZerofill_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 7),
    _XmdMemVirtZerofill_Type()
)
xmdMemVirtZerofill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtZerofill.setStatus("mandatory")
_XmdMemVirtPagexct_Type = Counter32
_XmdMemVirtPagexct_Object = MibScalar
xmdMemVirtPagexct = _XmdMemVirtPagexct_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 8),
    _XmdMemVirtPagexct_Type()
)
xmdMemVirtPagexct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtPagexct.setStatus("mandatory")
_XmdMemVirtPgrclm_Type = Counter32
_XmdMemVirtPgrclm_Object = MibScalar
xmdMemVirtPgrclm = _XmdMemVirtPgrclm_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 9),
    _XmdMemVirtPgrclm_Type()
)
xmdMemVirtPgrclm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtPgrclm.setStatus("mandatory")
_XmdMemVirtLockexct_Type = Counter32
_XmdMemVirtLockexct_Object = MibScalar
xmdMemVirtLockexct = _XmdMemVirtLockexct_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 10),
    _XmdMemVirtLockexct_Type()
)
xmdMemVirtLockexct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtLockexct.setStatus("mandatory")
_XmdMemVirtBacktrk_Type = Counter32
_XmdMemVirtBacktrk_Object = MibScalar
xmdMemVirtBacktrk = _XmdMemVirtBacktrk_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 11),
    _XmdMemVirtBacktrk_Type()
)
xmdMemVirtBacktrk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtBacktrk.setStatus("mandatory")
_XmdMemVirtExfill_Type = Counter32
_XmdMemVirtExfill_Object = MibScalar
xmdMemVirtExfill = _XmdMemVirtExfill_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 12),
    _XmdMemVirtExfill_Type()
)
xmdMemVirtExfill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtExfill.setStatus("mandatory")
_XmdMemVirtScan_Type = Counter32
_XmdMemVirtScan_Object = MibScalar
xmdMemVirtScan = _XmdMemVirtScan_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 13),
    _XmdMemVirtScan_Type()
)
xmdMemVirtScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtScan.setStatus("mandatory")
_XmdMemVirtCycle_Type = Counter32
_XmdMemVirtCycle_Object = MibScalar
xmdMemVirtCycle = _XmdMemVirtCycle_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 14),
    _XmdMemVirtCycle_Type()
)
xmdMemVirtCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtCycle.setStatus("mandatory")
_XmdMemVirtSteal_Type = Counter32
_XmdMemVirtSteal_Object = MibScalar
xmdMemVirtSteal = _XmdMemVirtSteal_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 15),
    _XmdMemVirtSteal_Type()
)
xmdMemVirtSteal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtSteal.setStatus("mandatory")
_XmdMemVirtFreewt_Type = Counter32
_XmdMemVirtFreewt_Object = MibScalar
xmdMemVirtFreewt = _XmdMemVirtFreewt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 16),
    _XmdMemVirtFreewt_Type()
)
xmdMemVirtFreewt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtFreewt.setStatus("mandatory")
_XmdMemVirtExtendwt_Type = Counter32
_XmdMemVirtExtendwt_Object = MibScalar
xmdMemVirtExtendwt = _XmdMemVirtExtendwt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 17),
    _XmdMemVirtExtendwt_Type()
)
xmdMemVirtExtendwt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtExtendwt.setStatus("mandatory")
_XmdMemVirtPendiowt_Type = Counter32
_XmdMemVirtPendiowt_Object = MibScalar
xmdMemVirtPendiowt = _XmdMemVirtPendiowt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 18),
    _XmdMemVirtPendiowt_Type()
)
xmdMemVirtPendiowt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtPendiowt.setStatus("mandatory")
_XmdMemVirtPfavail_Type = Integer32
_XmdMemVirtPfavail_Object = MibScalar
xmdMemVirtPfavail = _XmdMemVirtPfavail_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 19),
    _XmdMemVirtPfavail_Type()
)
xmdMemVirtPfavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtPfavail.setStatus("mandatory")
_XmdMemVirtWcomrepag_Type = Integer32
_XmdMemVirtWcomrepag_Object = MibScalar
xmdMemVirtWcomrepag = _XmdMemVirtWcomrepag_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 20),
    _XmdMemVirtWcomrepag_Type()
)
xmdMemVirtWcomrepag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtWcomrepag.setStatus("mandatory")
_XmdMemVirtWncomrepag_Type = Integer32
_XmdMemVirtWncomrepag_Object = MibScalar
xmdMemVirtWncomrepag = _XmdMemVirtWncomrepag_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 21),
    _XmdMemVirtWncomrepag_Type()
)
xmdMemVirtWncomrepag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtWncomrepag.setStatus("mandatory")
_XmdMemVirtComrepag_Type = Counter32
_XmdMemVirtComrepag_Object = MibScalar
xmdMemVirtComrepag = _XmdMemVirtComrepag_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 22),
    _XmdMemVirtComrepag_Type()
)
xmdMemVirtComrepag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtComrepag.setStatus("mandatory")
_XmdMemVirtEcomrepag_Type = Integer32
_XmdMemVirtEcomrepag_Object = MibScalar
xmdMemVirtEcomrepag = _XmdMemVirtEcomrepag_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 23),
    _XmdMemVirtEcomrepag_Type()
)
xmdMemVirtEcomrepag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtEcomrepag.setStatus("mandatory")
_XmdMemVirtNcomrepag_Type = Counter32
_XmdMemVirtNcomrepag_Object = MibScalar
xmdMemVirtNcomrepag = _XmdMemVirtNcomrepag_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 24),
    _XmdMemVirtNcomrepag_Type()
)
xmdMemVirtNcomrepag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtNcomrepag.setStatus("mandatory")
_XmdMemVirtEncomrepag_Type = Integer32
_XmdMemVirtEncomrepag_Object = MibScalar
xmdMemVirtEncomrepag = _XmdMemVirtEncomrepag_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 25),
    _XmdMemVirtEncomrepag_Type()
)
xmdMemVirtEncomrepag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtEncomrepag.setStatus("mandatory")
_XmdMemVirtComrepl_Type = Counter32
_XmdMemVirtComrepl_Object = MibScalar
xmdMemVirtComrepl = _XmdMemVirtComrepl_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 26),
    _XmdMemVirtComrepl_Type()
)
xmdMemVirtComrepl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtComrepl.setStatus("mandatory")
_XmdMemVirtEcomrepl_Type = Integer32
_XmdMemVirtEcomrepl_Object = MibScalar
xmdMemVirtEcomrepl = _XmdMemVirtEcomrepl_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 27),
    _XmdMemVirtEcomrepl_Type()
)
xmdMemVirtEcomrepl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtEcomrepl.setStatus("mandatory")
_XmdMemVirtNcomrepl_Type = Counter32
_XmdMemVirtNcomrepl_Object = MibScalar
xmdMemVirtNcomrepl = _XmdMemVirtNcomrepl_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 28),
    _XmdMemVirtNcomrepl_Type()
)
xmdMemVirtNcomrepl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtNcomrepl.setStatus("mandatory")
_XmdMemVirtEncomrepl_Type = Integer32
_XmdMemVirtEncomrepl_Object = MibScalar
xmdMemVirtEncomrepl = _XmdMemVirtEncomrepl_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 29),
    _XmdMemVirtEncomrepl_Type()
)
xmdMemVirtEncomrepl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtEncomrepl.setStatus("mandatory")
_XmdMemVirtTotpends_Type = Integer32
_XmdMemVirtTotpends_Object = MibScalar
xmdMemVirtTotpends = _XmdMemVirtTotpends_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 30),
    _XmdMemVirtTotpends_Type()
)
xmdMemVirtTotpends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtTotpends.setStatus("mandatory")
_XmdMemVirtCompends_Type = Integer32
_XmdMemVirtCompends_Object = MibScalar
xmdMemVirtCompends = _XmdMemVirtCompends_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 31),
    _XmdMemVirtCompends_Type()
)
xmdMemVirtCompends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtCompends.setStatus("mandatory")
_XmdMemVirtNcompends_Type = Integer32
_XmdMemVirtNcompends_Object = MibScalar
xmdMemVirtNcompends = _XmdMemVirtNcompends_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 32),
    _XmdMemVirtNcompends_Type()
)
xmdMemVirtNcompends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtNcompends.setStatus("mandatory")
_XmdMemVirtCltpends_Type = Integer32
_XmdMemVirtCltpends_Object = MibScalar
xmdMemVirtCltpends = _XmdMemVirtCltpends_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 33),
    _XmdMemVirtCltpends_Type()
)
xmdMemVirtCltpends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtCltpends.setStatus("mandatory")
_XmdMemVirtNpswarn_Type = Integer32
_XmdMemVirtNpswarn_Object = MibScalar
xmdMemVirtNpswarn = _XmdMemVirtNpswarn_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 34),
    _XmdMemVirtNpswarn_Type()
)
xmdMemVirtNpswarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtNpswarn.setStatus("mandatory")
_XmdMemVirtNpskill_Type = Integer32
_XmdMemVirtNpskill_Object = MibScalar
xmdMemVirtNpskill = _XmdMemVirtNpskill_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 35),
    _XmdMemVirtNpskill_Type()
)
xmdMemVirtNpskill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtNpskill.setStatus("mandatory")
_XmdMemVirtMaxfree_Type = Integer32
_XmdMemVirtMaxfree_Object = MibScalar
xmdMemVirtMaxfree = _XmdMemVirtMaxfree_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 36),
    _XmdMemVirtMaxfree_Type()
)
xmdMemVirtMaxfree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtMaxfree.setStatus("mandatory")
_XmdMemVirtMinfree_Type = Integer32
_XmdMemVirtMinfree_Object = MibScalar
xmdMemVirtMinfree = _XmdMemVirtMinfree_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 37),
    _XmdMemVirtMinfree_Type()
)
xmdMemVirtMinfree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtMinfree.setStatus("mandatory")
_XmdMemVirtMinperm_Type = Integer32
_XmdMemVirtMinperm_Object = MibScalar
xmdMemVirtMinperm = _XmdMemVirtMinperm_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 38),
    _XmdMemVirtMinperm_Type()
)
xmdMemVirtMinperm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtMinperm.setStatus("mandatory")
_XmdMemVirtMaxpgahead_Type = Integer32
_XmdMemVirtMaxpgahead_Object = MibScalar
xmdMemVirtMaxpgahead = _XmdMemVirtMaxpgahead_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 39),
    _XmdMemVirtMaxpgahead_Type()
)
xmdMemVirtMaxpgahead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtMaxpgahead.setStatus("mandatory")
_XmdMemVirtMinpgahead_Type = Integer32
_XmdMemVirtMinpgahead_Object = MibScalar
xmdMemVirtMinpgahead = _XmdMemVirtMinpgahead_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 40),
    _XmdMemVirtMinpgahead_Type()
)
xmdMemVirtMinpgahead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtMinpgahead.setStatus("mandatory")
_XmdMemVirtMaxpout_Type = Integer32
_XmdMemVirtMaxpout_Object = MibScalar
xmdMemVirtMaxpout = _XmdMemVirtMaxpout_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 41),
    _XmdMemVirtMaxpout_Type()
)
xmdMemVirtMaxpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtMaxpout.setStatus("mandatory")
_XmdMemVirtMinpout_Type = Integer32
_XmdMemVirtMinpout_Object = MibScalar
xmdMemVirtMinpout = _XmdMemVirtMinpout_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 2, 42),
    _XmdMemVirtMinpout_Type()
)
xmdMemVirtMinpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemVirtMinpout.setStatus("mandatory")
_XmdMemKmem_Object = MibTable
xmdMemKmem = _XmdMemKmem_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    xmdMemKmem.setStatus("mandatory")
_XmdMemKmemEntry_Object = MibTableRow
xmdMemKmemEntry = _XmdMemKmemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    xmdMemKmemEntry.setStatus("mandatory")
_XmdMemKmemIndex_Type = Integer32
_XmdMemKmemIndex_Object = MibTableColumn
xmdMemKmemIndex = _XmdMemKmemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 4, 1, 1),
    _XmdMemKmemIndex_Type()
)
xmdMemKmemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemKmemIndex.setStatus("mandatory")
_XmdMemKmemInstName_Type = DisplayString
_XmdMemKmemInstName_Object = MibTableColumn
xmdMemKmemInstName = _XmdMemKmemInstName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 4, 1, 2),
    _XmdMemKmemInstName_Type()
)
xmdMemKmemInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemKmemInstName.setStatus("mandatory")
_XmdMemKmemInuse_Type = Integer32
_XmdMemKmemInuse_Object = MibTableColumn
xmdMemKmemInuse = _XmdMemKmemInuse_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 4, 1, 3),
    _XmdMemKmemInuse_Type()
)
xmdMemKmemInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemKmemInuse.setStatus("mandatory")
_XmdMemKmemCalls_Type = Counter32
_XmdMemKmemCalls_Object = MibTableColumn
xmdMemKmemCalls = _XmdMemKmemCalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 4, 1, 4),
    _XmdMemKmemCalls_Type()
)
xmdMemKmemCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemKmemCalls.setStatus("mandatory")
_XmdMemKmemFailures_Type = Counter32
_XmdMemKmemFailures_Object = MibTableColumn
xmdMemKmemFailures = _XmdMemKmemFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 4, 1, 5),
    _XmdMemKmemFailures_Type()
)
xmdMemKmemFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemKmemFailures.setStatus("mandatory")
_XmdMemKmemMemuse_Type = Integer32
_XmdMemKmemMemuse_Object = MibTableColumn
xmdMemKmemMemuse = _XmdMemKmemMemuse_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 4, 1, 6),
    _XmdMemKmemMemuse_Type()
)
xmdMemKmemMemuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemKmemMemuse.setStatus("mandatory")
_XmdMemKmemMemmax_Type = Integer32
_XmdMemKmemMemmax_Object = MibTableColumn
xmdMemKmemMemmax = _XmdMemKmemMemmax_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 4, 1, 7),
    _XmdMemKmemMemmax_Type()
)
xmdMemKmemMemmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemKmemMemmax.setStatus("mandatory")
_XmdMemKmemBlocks_Type = Counter32
_XmdMemKmemBlocks_Object = MibTableColumn
xmdMemKmemBlocks = _XmdMemKmemBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 2, 4, 1, 8),
    _XmdMemKmemBlocks_Type()
)
xmdMemKmemBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdMemKmemBlocks.setStatus("mandatory")
_XmdPagSp_Object = MibTable
xmdPagSp = _XmdPagSp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    xmdPagSp.setStatus("mandatory")
_XmdPagSpEntry_Object = MibTableRow
xmdPagSpEntry = _XmdPagSpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    xmdPagSpEntry.setStatus("mandatory")
_XmdPagSpIndex_Type = Integer32
_XmdPagSpIndex_Object = MibTableColumn
xmdPagSpIndex = _XmdPagSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 3, 1, 1),
    _XmdPagSpIndex_Type()
)
xmdPagSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdPagSpIndex.setStatus("mandatory")
_XmdPagSpInstName_Type = DisplayString
_XmdPagSpInstName_Object = MibTableColumn
xmdPagSpInstName = _XmdPagSpInstName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 3, 1, 2),
    _XmdPagSpInstName_Type()
)
xmdPagSpInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdPagSpInstName.setStatus("mandatory")
_XmdPagSpSize_Type = Integer32
_XmdPagSpSize_Object = MibTableColumn
xmdPagSpSize = _XmdPagSpSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 3, 1, 3),
    _XmdPagSpSize_Type()
)
xmdPagSpSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdPagSpSize.setStatus("mandatory")
_XmdPagSpEfree_Type = Integer32
_XmdPagSpEfree_Object = MibTableColumn
xmdPagSpEfree = _XmdPagSpEfree_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 3, 1, 4),
    _XmdPagSpEfree_Type()
)
xmdPagSpEfree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdPagSpEfree.setStatus("mandatory")
_XmdPagSpIocnt_Type = Integer32
_XmdPagSpIocnt_Object = MibTableColumn
xmdPagSpIocnt = _XmdPagSpIocnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 3, 1, 5),
    _XmdPagSpIocnt_Type()
)
xmdPagSpIocnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdPagSpIocnt.setStatus("mandatory")
_XmdPagSpTotalsize_Type = Integer32
_XmdPagSpTotalsize_Object = MibScalar
xmdPagSpTotalsize = _XmdPagSpTotalsize_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 3, 11),
    _XmdPagSpTotalsize_Type()
)
xmdPagSpTotalsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdPagSpTotalsize.setStatus("mandatory")
_XmdPagSpTotalfree_Type = Integer32
_XmdPagSpTotalfree_Object = MibScalar
xmdPagSpTotalfree = _XmdPagSpTotalfree_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 3, 12),
    _XmdPagSpTotalfree_Type()
)
xmdPagSpTotalfree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdPagSpTotalfree.setStatus("mandatory")
_XmdPagSpEtotalfree_Type = Integer32
_XmdPagSpEtotalfree_Object = MibScalar
xmdPagSpEtotalfree = _XmdPagSpEtotalfree_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 3, 13),
    _XmdPagSpEtotalfree_Type()
)
xmdPagSpEtotalfree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdPagSpEtotalfree.setStatus("mandatory")
_XmdPagSpEtotalused_Type = Integer32
_XmdPagSpEtotalused_Object = MibScalar
xmdPagSpEtotalused = _XmdPagSpEtotalused_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 3, 14),
    _XmdPagSpEtotalused_Type()
)
xmdPagSpEtotalused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdPagSpEtotalused.setStatus("mandatory")
_XmdPagSpPgspgin_Type = Counter32
_XmdPagSpPgspgin_Object = MibScalar
xmdPagSpPgspgin = _XmdPagSpPgspgin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 3, 15),
    _XmdPagSpPgspgin_Type()
)
xmdPagSpPgspgin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdPagSpPgspgin.setStatus("mandatory")
_XmdPagSpPgspgout_Type = Counter32
_XmdPagSpPgspgout_Object = MibScalar
xmdPagSpPgspgout = _XmdPagSpPgspgout_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 3, 16),
    _XmdPagSpPgspgout_Type()
)
xmdPagSpPgspgout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdPagSpPgspgout.setStatus("mandatory")
_XmdDisk_Object = MibTable
xmdDisk = _XmdDisk_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    xmdDisk.setStatus("mandatory")
_XmdDiskEntry_Object = MibTableRow
xmdDiskEntry = _XmdDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    xmdDiskEntry.setStatus("mandatory")
_XmdDiskIndex_Type = Integer32
_XmdDiskIndex_Object = MibTableColumn
xmdDiskIndex = _XmdDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 4, 1, 1),
    _XmdDiskIndex_Type()
)
xmdDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdDiskIndex.setStatus("mandatory")
_XmdDiskInstName_Type = DisplayString
_XmdDiskInstName_Object = MibTableColumn
xmdDiskInstName = _XmdDiskInstName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 4, 1, 2),
    _XmdDiskInstName_Type()
)
xmdDiskInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdDiskInstName.setStatus("mandatory")
_XmdDiskBusy_Type = Counter32
_XmdDiskBusy_Object = MibTableColumn
xmdDiskBusy = _XmdDiskBusy_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 4, 1, 3),
    _XmdDiskBusy_Type()
)
xmdDiskBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdDiskBusy.setStatus("mandatory")
_XmdDiskXfer_Type = Counter32
_XmdDiskXfer_Object = MibTableColumn
xmdDiskXfer = _XmdDiskXfer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 4, 1, 4),
    _XmdDiskXfer_Type()
)
xmdDiskXfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdDiskXfer.setStatus("mandatory")
_XmdDiskRblk_Type = Counter32
_XmdDiskRblk_Object = MibTableColumn
xmdDiskRblk = _XmdDiskRblk_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 4, 1, 5),
    _XmdDiskRblk_Type()
)
xmdDiskRblk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdDiskRblk.setStatus("mandatory")
_XmdDiskWblk_Type = Counter32
_XmdDiskWblk_Object = MibTableColumn
xmdDiskWblk = _XmdDiskWblk_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 4, 1, 6),
    _XmdDiskWblk_Type()
)
xmdDiskWblk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdDiskWblk.setStatus("mandatory")
_XmdLAN_Object = MibTable
xmdLAN = _XmdLAN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    xmdLAN.setStatus("mandatory")
_XmdLANEntry_Object = MibTableRow
xmdLANEntry = _XmdLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    xmdLANEntry.setStatus("mandatory")
_XmdLANIndex_Type = Integer32
_XmdLANIndex_Object = MibTableColumn
xmdLANIndex = _XmdLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 1),
    _XmdLANIndex_Type()
)
xmdLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANIndex.setStatus("mandatory")
_XmdLANInstName_Type = DisplayString
_XmdLANInstName_Object = MibTableColumn
xmdLANInstName = _XmdLANInstName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 2),
    _XmdLANInstName_Type()
)
xmdLANInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANInstName.setStatus("mandatory")
_XmdLANBytesout_Type = Counter32
_XmdLANBytesout_Object = MibTableColumn
xmdLANBytesout = _XmdLANBytesout_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 3),
    _XmdLANBytesout_Type()
)
xmdLANBytesout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANBytesout.setStatus("mandatory")
_XmdLANKbytesout_Type = Counter32
_XmdLANKbytesout_Object = MibTableColumn
xmdLANKbytesout = _XmdLANKbytesout_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 4),
    _XmdLANKbytesout_Type()
)
xmdLANKbytesout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANKbytesout.setStatus("mandatory")
_XmdLANBytesin_Type = Counter32
_XmdLANBytesin_Object = MibTableColumn
xmdLANBytesin = _XmdLANBytesin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 5),
    _XmdLANBytesin_Type()
)
xmdLANBytesin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANBytesin.setStatus("mandatory")
_XmdLANKbytesin_Type = Counter32
_XmdLANKbytesin_Object = MibTableColumn
xmdLANKbytesin = _XmdLANKbytesin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 6),
    _XmdLANKbytesin_Type()
)
xmdLANKbytesin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANKbytesin.setStatus("mandatory")
_XmdLANFramesout_Type = Counter32
_XmdLANFramesout_Object = MibTableColumn
xmdLANFramesout = _XmdLANFramesout_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 7),
    _XmdLANFramesout_Type()
)
xmdLANFramesout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANFramesout.setStatus("mandatory")
_XmdLANFramesin_Type = Counter32
_XmdLANFramesin_Object = MibTableColumn
xmdLANFramesin = _XmdLANFramesin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 8),
    _XmdLANFramesin_Type()
)
xmdLANFramesin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANFramesin.setStatus("mandatory")
_XmdLANXmiterrors_Type = Counter32
_XmdLANXmiterrors_Object = MibTableColumn
xmdLANXmiterrors = _XmdLANXmiterrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 9),
    _XmdLANXmiterrors_Type()
)
xmdLANXmiterrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANXmiterrors.setStatus("mandatory")
_XmdLANRcverrors_Type = Counter32
_XmdLANRcverrors_Object = MibTableColumn
xmdLANRcverrors = _XmdLANRcverrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 10),
    _XmdLANRcverrors_Type()
)
xmdLANRcverrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANRcverrors.setStatus("mandatory")
_XmdLANIbadpacks_Type = Counter32
_XmdLANIbadpacks_Object = MibTableColumn
xmdLANIbadpacks = _XmdLANIbadpacks_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 11),
    _XmdLANIbadpacks_Type()
)
xmdLANIbadpacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANIbadpacks.setStatus("mandatory")
_XmdLANXmitque_Type = Integer32
_XmdLANXmitque_Object = MibTableColumn
xmdLANXmitque = _XmdLANXmitque_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 12),
    _XmdLANXmitque_Type()
)
xmdLANXmitque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANXmitque.setStatus("mandatory")
_XmdLANHighxmitq_Type = Integer32
_XmdLANHighxmitq_Object = MibTableColumn
xmdLANHighxmitq = _XmdLANHighxmitq_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 13),
    _XmdLANHighxmitq_Type()
)
xmdLANHighxmitq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANHighxmitq.setStatus("mandatory")
_XmdLANRecvintr_Type = Counter32
_XmdLANRecvintr_Object = MibTableColumn
xmdLANRecvintr = _XmdLANRecvintr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 14),
    _XmdLANRecvintr_Type()
)
xmdLANRecvintr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANRecvintr.setStatus("mandatory")
_XmdLANXmitintr_Type = Counter32
_XmdLANXmitintr_Object = MibTableColumn
xmdLANXmitintr = _XmdLANXmitintr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 15),
    _XmdLANXmitintr_Type()
)
xmdLANXmitintr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANXmitintr.setStatus("mandatory")
_XmdLANXmitovfl_Type = Counter32
_XmdLANXmitovfl_Object = MibTableColumn
xmdLANXmitovfl = _XmdLANXmitovfl_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 16),
    _XmdLANXmitovfl_Type()
)
xmdLANXmitovfl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANXmitovfl.setStatus("mandatory")
_XmdLANXmitdrops_Type = Counter32
_XmdLANXmitdrops_Object = MibTableColumn
xmdLANXmitdrops = _XmdLANXmitdrops_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 17),
    _XmdLANXmitdrops_Type()
)
xmdLANXmitdrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANXmitdrops.setStatus("mandatory")
_XmdLANRecvdrops_Type = Counter32
_XmdLANRecvdrops_Object = MibTableColumn
xmdLANRecvdrops = _XmdLANRecvdrops_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 5, 1, 18),
    _XmdLANRecvdrops_Type()
)
xmdLANRecvdrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdLANRecvdrops.setStatus("mandatory")
_XmdProc_Object = MibTable
xmdProc = _XmdProc_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    xmdProc.setStatus("mandatory")
_XmdProcEntry_Object = MibTableRow
xmdProcEntry = _XmdProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    xmdProcEntry.setStatus("mandatory")
_XmdProcIndex_Type = Integer32
_XmdProcIndex_Object = MibTableColumn
xmdProcIndex = _XmdProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 1),
    _XmdProcIndex_Type()
)
xmdProcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcIndex.setStatus("mandatory")
_XmdProcInstName_Type = DisplayString
_XmdProcInstName_Object = MibTableColumn
xmdProcInstName = _XmdProcInstName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 2),
    _XmdProcInstName_Type()
)
xmdProcInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcInstName.setStatus("mandatory")
_XmdProcNice_Type = Integer32
_XmdProcNice_Object = MibTableColumn
xmdProcNice = _XmdProcNice_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 3),
    _XmdProcNice_Type()
)
xmdProcNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcNice.setStatus("mandatory")
_XmdProcRepage_Type = Counter32
_XmdProcRepage_Object = MibTableColumn
xmdProcRepage = _XmdProcRepage_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 4),
    _XmdProcRepage_Type()
)
xmdProcRepage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcRepage.setStatus("mandatory")
_XmdProcMajflt_Type = Counter32
_XmdProcMajflt_Object = MibTableColumn
xmdProcMajflt = _XmdProcMajflt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 5),
    _XmdProcMajflt_Type()
)
xmdProcMajflt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcMajflt.setStatus("mandatory")
_XmdProcMinflt_Type = Counter32
_XmdProcMinflt_Object = MibTableColumn
xmdProcMinflt = _XmdProcMinflt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 6),
    _XmdProcMinflt_Type()
)
xmdProcMinflt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcMinflt.setStatus("mandatory")
_XmdProcCpums_Type = Counter32
_XmdProcCpums_Object = MibTableColumn
xmdProcCpums = _XmdProcCpums_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 7),
    _XmdProcCpums_Type()
)
xmdProcCpums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcCpums.setStatus("mandatory")
_XmdProcCpuacc_Type = Integer32
_XmdProcCpuacc_Object = MibTableColumn
xmdProcCpuacc = _XmdProcCpuacc_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 8),
    _XmdProcCpuacc_Type()
)
xmdProcCpuacc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcCpuacc.setStatus("mandatory")
_XmdProcCpupct_Type = Integer32
_XmdProcCpupct_Object = MibTableColumn
xmdProcCpupct = _XmdProcCpupct_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 9),
    _XmdProcCpupct_Type()
)
xmdProcCpupct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcCpupct.setStatus("mandatory")
_XmdProcUsercpu_Type = Counter32
_XmdProcUsercpu_Object = MibTableColumn
xmdProcUsercpu = _XmdProcUsercpu_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 10),
    _XmdProcUsercpu_Type()
)
xmdProcUsercpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcUsercpu.setStatus("mandatory")
_XmdProcKerncpu_Type = Counter32
_XmdProcKerncpu_Object = MibTableColumn
xmdProcKerncpu = _XmdProcKerncpu_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 11),
    _XmdProcKerncpu_Type()
)
xmdProcKerncpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcKerncpu.setStatus("mandatory")
_XmdProcWorkmem_Type = Integer32
_XmdProcWorkmem_Object = MibTableColumn
xmdProcWorkmem = _XmdProcWorkmem_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 12),
    _XmdProcWorkmem_Type()
)
xmdProcWorkmem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcWorkmem.setStatus("mandatory")
_XmdProcCodemem_Type = Integer32
_XmdProcCodemem_Object = MibTableColumn
xmdProcCodemem = _XmdProcCodemem_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 13),
    _XmdProcCodemem_Type()
)
xmdProcCodemem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcCodemem.setStatus("mandatory")
_XmdProcPagsp_Type = Integer32
_XmdProcPagsp_Object = MibTableColumn
xmdProcPagsp = _XmdProcPagsp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 14),
    _XmdProcPagsp_Type()
)
xmdProcPagsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcPagsp.setStatus("mandatory")
_XmdProcNsignals_Type = Counter32
_XmdProcNsignals_Object = MibTableColumn
xmdProcNsignals = _XmdProcNsignals_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 15),
    _XmdProcNsignals_Type()
)
xmdProcNsignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcNsignals.setStatus("mandatory")
_XmdProcNvcsw_Type = Counter32
_XmdProcNvcsw_Object = MibTableColumn
xmdProcNvcsw = _XmdProcNvcsw_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 16),
    _XmdProcNvcsw_Type()
)
xmdProcNvcsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcNvcsw.setStatus("mandatory")
_XmdProcTsize_Type = Integer32
_XmdProcTsize_Object = MibTableColumn
xmdProcTsize = _XmdProcTsize_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 17),
    _XmdProcTsize_Type()
)
xmdProcTsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcTsize.setStatus("mandatory")
_XmdProcMaxrss_Type = Integer32
_XmdProcMaxrss_Object = MibTableColumn
xmdProcMaxrss = _XmdProcMaxrss_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 1, 18),
    _XmdProcMaxrss_Type()
)
xmdProcMaxrss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcMaxrss.setStatus("mandatory")
_XmdProcPswitch_Type = Counter32
_XmdProcPswitch_Object = MibScalar
xmdProcPswitch = _XmdProcPswitch_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 11),
    _XmdProcPswitch_Type()
)
xmdProcPswitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcPswitch.setStatus("mandatory")
_XmdProcRunque_Type = Integer32
_XmdProcRunque_Object = MibScalar
xmdProcRunque = _XmdProcRunque_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 12),
    _XmdProcRunque_Type()
)
xmdProcRunque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcRunque.setStatus("mandatory")
_XmdProcRunocc_Type = Integer32
_XmdProcRunocc_Object = MibScalar
xmdProcRunocc = _XmdProcRunocc_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 13),
    _XmdProcRunocc_Type()
)
xmdProcRunocc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcRunocc.setStatus("mandatory")
_XmdProcSwpque_Type = Integer32
_XmdProcSwpque_Object = MibScalar
xmdProcSwpque = _XmdProcSwpque_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 14),
    _XmdProcSwpque_Type()
)
xmdProcSwpque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcSwpque.setStatus("mandatory")
_XmdProcSwpocc_Type = Integer32
_XmdProcSwpocc_Object = MibScalar
xmdProcSwpocc = _XmdProcSwpocc_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 15),
    _XmdProcSwpocc_Type()
)
xmdProcSwpocc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcSwpocc.setStatus("mandatory")
_XmdProcKsched_Type = Counter32
_XmdProcKsched_Object = MibScalar
xmdProcKsched = _XmdProcKsched_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 16),
    _XmdProcKsched_Type()
)
xmdProcKsched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcKsched.setStatus("mandatory")
_XmdProcKexit_Type = Counter32
_XmdProcKexit_Object = MibScalar
xmdProcKexit = _XmdProcKexit_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 6, 17),
    _XmdProcKexit_Type()
)
xmdProcKexit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdProcKexit.setStatus("mandatory")
_XmdSyscall_ObjectIdentity = ObjectIdentity
xmdSyscall = _XmdSyscall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 7)
)
_XmdSyscallTotal_Type = Counter32
_XmdSyscallTotal_Object = MibScalar
xmdSyscallTotal = _XmdSyscallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 7, 1),
    _XmdSyscallTotal_Type()
)
xmdSyscallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSyscallTotal.setStatus("mandatory")
_XmdSyscallRead_Type = Counter32
_XmdSyscallRead_Object = MibScalar
xmdSyscallRead = _XmdSyscallRead_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 7, 2),
    _XmdSyscallRead_Type()
)
xmdSyscallRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSyscallRead.setStatus("mandatory")
_XmdSyscallWrite_Type = Counter32
_XmdSyscallWrite_Object = MibScalar
xmdSyscallWrite = _XmdSyscallWrite_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 7, 3),
    _XmdSyscallWrite_Type()
)
xmdSyscallWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSyscallWrite.setStatus("mandatory")
_XmdSyscallFork_Type = Counter32
_XmdSyscallFork_Object = MibScalar
xmdSyscallFork = _XmdSyscallFork_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 7, 4),
    _XmdSyscallFork_Type()
)
xmdSyscallFork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSyscallFork.setStatus("mandatory")
_XmdSyscallExec_Type = Counter32
_XmdSyscallExec_Object = MibScalar
xmdSyscallExec = _XmdSyscallExec_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 7, 5),
    _XmdSyscallExec_Type()
)
xmdSyscallExec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSyscallExec.setStatus("mandatory")
_XmdSysIO_ObjectIdentity = ObjectIdentity
xmdSysIO = _XmdSysIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8)
)
_XmdSysIOReadch_Type = Counter32
_XmdSysIOReadch_Object = MibScalar
xmdSysIOReadch = _XmdSysIOReadch_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8, 1),
    _XmdSysIOReadch_Type()
)
xmdSysIOReadch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSysIOReadch.setStatus("mandatory")
_XmdSysIOWritech_Type = Counter32
_XmdSysIOWritech_Object = MibScalar
xmdSysIOWritech = _XmdSysIOWritech_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8, 2),
    _XmdSysIOWritech_Type()
)
xmdSysIOWritech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSysIOWritech.setStatus("mandatory")
_XmdSysIOLbread_Type = Counter32
_XmdSysIOLbread_Object = MibScalar
xmdSysIOLbread = _XmdSysIOLbread_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8, 3),
    _XmdSysIOLbread_Type()
)
xmdSysIOLbread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSysIOLbread.setStatus("mandatory")
_XmdSysIOLbwrite_Type = Counter32
_XmdSysIOLbwrite_Object = MibScalar
xmdSysIOLbwrite = _XmdSysIOLbwrite_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8, 4),
    _XmdSysIOLbwrite_Type()
)
xmdSysIOLbwrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSysIOLbwrite.setStatus("mandatory")
_XmdSysIOBread_Type = Counter32
_XmdSysIOBread_Object = MibScalar
xmdSysIOBread = _XmdSysIOBread_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8, 5),
    _XmdSysIOBread_Type()
)
xmdSysIOBread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSysIOBread.setStatus("mandatory")
_XmdSysIOBwrite_Type = Counter32
_XmdSysIOBwrite_Object = MibScalar
xmdSysIOBwrite = _XmdSysIOBwrite_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8, 6),
    _XmdSysIOBwrite_Type()
)
xmdSysIOBwrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSysIOBwrite.setStatus("mandatory")
_XmdSysIOPhread_Type = Counter32
_XmdSysIOPhread_Object = MibScalar
xmdSysIOPhread = _XmdSysIOPhread_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8, 7),
    _XmdSysIOPhread_Type()
)
xmdSysIOPhread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSysIOPhread.setStatus("mandatory")
_XmdSysIOPhwrite_Type = Counter32
_XmdSysIOPhwrite_Object = MibScalar
xmdSysIOPhwrite = _XmdSysIOPhwrite_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8, 8),
    _XmdSysIOPhwrite_Type()
)
xmdSysIOPhwrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSysIOPhwrite.setStatus("mandatory")
_XmdSysIOTtyraw_Type = Counter32
_XmdSysIOTtyraw_Object = MibScalar
xmdSysIOTtyraw = _XmdSysIOTtyraw_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8, 9),
    _XmdSysIOTtyraw_Type()
)
xmdSysIOTtyraw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSysIOTtyraw.setStatus("mandatory")
_XmdSysIOTtycan_Type = Counter32
_XmdSysIOTtycan_Object = MibScalar
xmdSysIOTtycan = _XmdSysIOTtycan_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8, 10),
    _XmdSysIOTtycan_Type()
)
xmdSysIOTtycan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSysIOTtycan.setStatus("mandatory")
_XmdSysIOTtyout_Type = Counter32
_XmdSysIOTtyout_Object = MibScalar
xmdSysIOTtyout = _XmdSysIOTtyout_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8, 11),
    _XmdSysIOTtyout_Type()
)
xmdSysIOTtyout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSysIOTtyout.setStatus("mandatory")
_XmdSysIOReadchkb_Type = Counter32
_XmdSysIOReadchkb_Object = MibScalar
xmdSysIOReadchkb = _XmdSysIOReadchkb_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8, 12),
    _XmdSysIOReadchkb_Type()
)
xmdSysIOReadchkb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSysIOReadchkb.setStatus("mandatory")
_XmdSysIOWritechkb_Type = Counter32
_XmdSysIOWritechkb_Object = MibScalar
xmdSysIOWritechkb = _XmdSysIOWritechkb_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 8, 13),
    _XmdSysIOWritechkb_Type()
)
xmdSysIOWritechkb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSysIOWritechkb.setStatus("mandatory")
_XmdIPC_ObjectIdentity = ObjectIdentity
xmdIPC = _XmdIPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9)
)
_XmdIPCMsg_ObjectIdentity = ObjectIdentity
xmdIPCMsg = _XmdIPCMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 1)
)
_XmdIPCMsgMsgmax_Type = Integer32
_XmdIPCMsgMsgmax_Object = MibScalar
xmdIPCMsgMsgmax = _XmdIPCMsgMsgmax_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 1, 1),
    _XmdIPCMsgMsgmax_Type()
)
xmdIPCMsgMsgmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCMsgMsgmax.setStatus("mandatory")
_XmdIPCMsgQuemax_Type = Integer32
_XmdIPCMsgQuemax_Object = MibScalar
xmdIPCMsgQuemax = _XmdIPCMsgQuemax_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 1, 2),
    _XmdIPCMsgQuemax_Type()
)
xmdIPCMsgQuemax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCMsgQuemax.setStatus("mandatory")
_XmdIPCMsgQueids_Type = Integer32
_XmdIPCMsgQueids_Object = MibScalar
xmdIPCMsgQueids = _XmdIPCMsgQueids_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 1, 3),
    _XmdIPCMsgQueids_Type()
)
xmdIPCMsgQueids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCMsgQueids.setStatus("mandatory")
_XmdIPCMsgIdmax_Type = Integer32
_XmdIPCMsgIdmax_Object = MibScalar
xmdIPCMsgIdmax = _XmdIPCMsgIdmax_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 1, 4),
    _XmdIPCMsgIdmax_Type()
)
xmdIPCMsgIdmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCMsgIdmax.setStatus("mandatory")
_XmdIPCSem_ObjectIdentity = ObjectIdentity
xmdIPCSem = _XmdIPCSem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 2)
)
_XmdIPCSemSemids_Type = Integer32
_XmdIPCSemSemids_Object = MibScalar
xmdIPCSemSemids = _XmdIPCSemSemids_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 2, 1),
    _XmdIPCSemSemids_Type()
)
xmdIPCSemSemids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCSemSemids.setStatus("mandatory")
_XmdIPCSemMaxsems_Type = Integer32
_XmdIPCSemMaxsems_Object = MibScalar
xmdIPCSemMaxsems = _XmdIPCSemMaxsems_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 2, 2),
    _XmdIPCSemMaxsems_Type()
)
xmdIPCSemMaxsems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCSemMaxsems.setStatus("mandatory")
_XmdIPCSemMaxops_Type = Integer32
_XmdIPCSemMaxops_Object = MibScalar
xmdIPCSemMaxops = _XmdIPCSemMaxops_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 2, 3),
    _XmdIPCSemMaxops_Type()
)
xmdIPCSemMaxops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCSemMaxops.setStatus("mandatory")
_XmdIPCSemMaxundo_Type = Integer32
_XmdIPCSemMaxundo_Object = MibScalar
xmdIPCSemMaxundo = _XmdIPCSemMaxundo_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 2, 4),
    _XmdIPCSemMaxundo_Type()
)
xmdIPCSemMaxundo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCSemMaxundo.setStatus("mandatory")
_XmdIPCSemUndosiz_Type = Integer32
_XmdIPCSemUndosiz_Object = MibScalar
xmdIPCSemUndosiz = _XmdIPCSemUndosiz_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 2, 5),
    _XmdIPCSemUndosiz_Type()
)
xmdIPCSemUndosiz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCSemUndosiz.setStatus("mandatory")
_XmdIPCSemSemmaxv_Type = Integer32
_XmdIPCSemSemmaxv_Object = MibScalar
xmdIPCSemSemmaxv = _XmdIPCSemSemmaxv_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 2, 6),
    _XmdIPCSemSemmaxv_Type()
)
xmdIPCSemSemmaxv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCSemSemmaxv.setStatus("mandatory")
_XmdIPCSemSemmaxe_Type = Integer32
_XmdIPCSemSemmaxe_Object = MibScalar
xmdIPCSemSemmaxe = _XmdIPCSemSemmaxe_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 2, 7),
    _XmdIPCSemSemmaxe_Type()
)
xmdIPCSemSemmaxe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCSemSemmaxe.setStatus("mandatory")
_XmdIPCShm_ObjectIdentity = ObjectIdentity
xmdIPCShm = _XmdIPCShm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 3)
)
_XmdIPCShmShmmax_Type = Integer32
_XmdIPCShmShmmax_Object = MibScalar
xmdIPCShmShmmax = _XmdIPCShmShmmax_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 3, 1),
    _XmdIPCShmShmmax_Type()
)
xmdIPCShmShmmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCShmShmmax.setStatus("mandatory")
_XmdIPCShmShmmin_Type = Integer32
_XmdIPCShmShmmin_Object = MibScalar
xmdIPCShmShmmin = _XmdIPCShmShmmin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 3, 2),
    _XmdIPCShmShmmin_Type()
)
xmdIPCShmShmmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCShmShmmin.setStatus("mandatory")
_XmdIPCShmShmids_Type = Integer32
_XmdIPCShmShmids_Object = MibScalar
xmdIPCShmShmids = _XmdIPCShmShmids_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 3, 3),
    _XmdIPCShmShmids_Type()
)
xmdIPCShmShmids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCShmShmids.setStatus("mandatory")
_XmdIPCLocks_ObjectIdentity = ObjectIdentity
xmdIPCLocks = _XmdIPCLocks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 4)
)
_XmdIPCLocksNumrecs_Type = Integer32
_XmdIPCLocksNumrecs_Object = MibScalar
xmdIPCLocksNumrecs = _XmdIPCLocksNumrecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 4, 1),
    _XmdIPCLocksNumrecs_Type()
)
xmdIPCLocksNumrecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCLocksNumrecs.setStatus("mandatory")
_XmdIPCLocksRecsused_Type = Integer32
_XmdIPCLocksRecsused_Object = MibScalar
xmdIPCLocksRecsused = _XmdIPCLocksRecsused_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 4, 2),
    _XmdIPCLocksRecsused_Type()
)
xmdIPCLocksRecsused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCLocksRecsused.setStatus("mandatory")
_XmdIPCLocksOverrun_Type = Integer32
_XmdIPCLocksOverrun_Object = MibScalar
xmdIPCLocksOverrun = _XmdIPCLocksOverrun_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 4, 3),
    _XmdIPCLocksOverrun_Type()
)
xmdIPCLocksOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCLocksOverrun.setStatus("mandatory")
_XmdIPCLocksRecstot_Type = Integer32
_XmdIPCLocksRecstot_Object = MibScalar
xmdIPCLocksRecstot = _XmdIPCLocksRecstot_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 4, 4),
    _XmdIPCLocksRecstot_Type()
)
xmdIPCLocksRecstot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCLocksRecstot.setStatus("mandatory")
_XmdIPCLocksRecsync_Type = Integer32
_XmdIPCLocksRecsync_Object = MibScalar
xmdIPCLocksRecsync = _XmdIPCLocksRecsync_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 9, 4, 5),
    _XmdIPCLocksRecsync_Type()
)
xmdIPCLocksRecsync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPCLocksRecsync.setStatus("mandatory")
_XmdFS_Object = MibTable
xmdFS = _XmdFS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 10)
)
if mibBuilder.loadTexts:
    xmdFS.setStatus("mandatory")
_XmdFSEntry_Object = MibTableRow
xmdFSEntry = _XmdFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    xmdFSEntry.setStatus("mandatory")
_XmdFSIndex_Type = Integer32
_XmdFSIndex_Object = MibTableColumn
xmdFSIndex = _XmdFSIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 10, 1, 1),
    _XmdFSIndex_Type()
)
xmdFSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdFSIndex.setStatus("mandatory")
_XmdFSInstName_Type = DisplayString
_XmdFSInstName_Object = MibTableColumn
xmdFSInstName = _XmdFSInstName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 10, 1, 2),
    _XmdFSInstName_Type()
)
xmdFSInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdFSInstName.setStatus("mandatory")
_XmdFSFree_Type = Integer32
_XmdFSFree_Object = MibTableColumn
xmdFSFree = _XmdFSFree_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 10, 1, 3),
    _XmdFSFree_Type()
)
xmdFSFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdFSFree.setStatus("mandatory")
_XmdFSPpsize_Type = Integer32
_XmdFSPpsize_Object = MibTableColumn
xmdFSPpsize = _XmdFSPpsize_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 10, 1, 4),
    _XmdFSPpsize_Type()
)
xmdFSPpsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdFSPpsize.setStatus("mandatory")
_XmdFSLvcount_Type = Integer32
_XmdFSLvcount_Object = MibTableColumn
xmdFSLvcount = _XmdFSLvcount_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 10, 1, 5),
    _XmdFSLvcount_Type()
)
xmdFSLvcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdFSLvcount.setStatus("mandatory")
_XmdFSPvcount_Type = Integer32
_XmdFSPvcount_Object = MibTableColumn
xmdFSPvcount = _XmdFSPvcount_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 10, 1, 6),
    _XmdFSPvcount_Type()
)
xmdFSPvcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdFSPvcount.setStatus("mandatory")
_XmdFSIget_Type = Counter32
_XmdFSIget_Object = MibScalar
xmdFSIget = _XmdFSIget_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 10, 11),
    _XmdFSIget_Type()
)
xmdFSIget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdFSIget.setStatus("mandatory")
_XmdFSNamei_Type = Counter32
_XmdFSNamei_Object = MibScalar
xmdFSNamei = _XmdFSNamei_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 10, 12),
    _XmdFSNamei_Type()
)
xmdFSNamei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdFSNamei.setStatus("mandatory")
_XmdFSDirblk_Type = Counter32
_XmdFSDirblk_Object = MibScalar
xmdFSDirblk = _XmdFSDirblk_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 10, 13),
    _XmdFSDirblk_Type()
)
xmdFSDirblk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdFSDirblk.setStatus("mandatory")
_XmdIP_ObjectIdentity = ObjectIdentity
xmdIP = _XmdIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11)
)
_XmdIPRcvtotal_Type = Counter32
_XmdIPRcvtotal_Object = MibScalar
xmdIPRcvtotal = _XmdIPRcvtotal_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 1),
    _XmdIPRcvtotal_Type()
)
xmdIPRcvtotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPRcvtotal.setStatus("mandatory")
_XmdIPRcvfrag_Type = Counter32
_XmdIPRcvfrag_Object = MibScalar
xmdIPRcvfrag = _XmdIPRcvfrag_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 2),
    _XmdIPRcvfrag_Type()
)
xmdIPRcvfrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPRcvfrag.setStatus("mandatory")
_XmdIPForward_Type = Counter32
_XmdIPForward_Object = MibScalar
xmdIPForward = _XmdIPForward_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 3),
    _XmdIPForward_Type()
)
xmdIPForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPForward.setStatus("mandatory")
_XmdIPRcvdgrm_Type = Counter32
_XmdIPRcvdgrm_Object = MibScalar
xmdIPRcvdgrm = _XmdIPRcvdgrm_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 4),
    _XmdIPRcvdgrm_Type()
)
xmdIPRcvdgrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPRcvdgrm.setStatus("mandatory")
_XmdIPSnddgrm_Type = Counter32
_XmdIPSnddgrm_Object = MibScalar
xmdIPSnddgrm = _XmdIPSnddgrm_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 5),
    _XmdIPSnddgrm_Type()
)
xmdIPSnddgrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPSnddgrm.setStatus("mandatory")
_XmdIPReasmok_Type = Counter32
_XmdIPReasmok_Object = MibScalar
xmdIPReasmok = _XmdIPReasmok_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 6),
    _XmdIPReasmok_Type()
)
xmdIPReasmok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPReasmok.setStatus("mandatory")
_XmdIPFragok_Type = Counter32
_XmdIPFragok_Object = MibScalar
xmdIPFragok = _XmdIPFragok_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 7),
    _XmdIPFragok_Type()
)
xmdIPFragok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPFragok.setStatus("mandatory")
_XmdIPNetIF_Object = MibTable
xmdIPNetIF = _XmdIPNetIF_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10)
)
if mibBuilder.loadTexts:
    xmdIPNetIF.setStatus("mandatory")
_XmdIPNetIFEntry_Object = MibTableRow
xmdIPNetIFEntry = _XmdIPNetIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1)
)
if mibBuilder.loadTexts:
    xmdIPNetIFEntry.setStatus("mandatory")
_XmdIPNetIFIndex_Type = Integer32
_XmdIPNetIFIndex_Object = MibTableColumn
xmdIPNetIFIndex = _XmdIPNetIFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 1),
    _XmdIPNetIFIndex_Type()
)
xmdIPNetIFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFIndex.setStatus("mandatory")
_XmdIPNetIFInstName_Type = DisplayString
_XmdIPNetIFInstName_Object = MibTableColumn
xmdIPNetIFInstName = _XmdIPNetIFInstName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 2),
    _XmdIPNetIFInstName_Type()
)
xmdIPNetIFInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFInstName.setStatus("mandatory")
_XmdIPNetIFIpacket_Type = Counter32
_XmdIPNetIFIpacket_Object = MibTableColumn
xmdIPNetIFIpacket = _XmdIPNetIFIpacket_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 3),
    _XmdIPNetIFIpacket_Type()
)
xmdIPNetIFIpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFIpacket.setStatus("mandatory")
_XmdIPNetIFIoctet_Type = Counter32
_XmdIPNetIFIoctet_Object = MibTableColumn
xmdIPNetIFIoctet = _XmdIPNetIFIoctet_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 4),
    _XmdIPNetIFIoctet_Type()
)
xmdIPNetIFIoctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFIoctet.setStatus("mandatory")
_XmdIPNetIFIoctetkb_Type = Counter32
_XmdIPNetIFIoctetkb_Object = MibTableColumn
xmdIPNetIFIoctetkb = _XmdIPNetIFIoctetkb_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 5),
    _XmdIPNetIFIoctetkb_Type()
)
xmdIPNetIFIoctetkb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFIoctetkb.setStatus("mandatory")
_XmdIPNetIFIerror_Type = Counter32
_XmdIPNetIFIerror_Object = MibTableColumn
xmdIPNetIFIerror = _XmdIPNetIFIerror_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 6),
    _XmdIPNetIFIerror_Type()
)
xmdIPNetIFIerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFIerror.setStatus("mandatory")
_XmdIPNetIFImcastpkt_Type = Counter32
_XmdIPNetIFImcastpkt_Object = MibTableColumn
xmdIPNetIFImcastpkt = _XmdIPNetIFImcastpkt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 7),
    _XmdIPNetIFImcastpkt_Type()
)
xmdIPNetIFImcastpkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFImcastpkt.setStatus("mandatory")
_XmdIPNetIFIqdrop_Type = Counter32
_XmdIPNetIFIqdrop_Object = MibTableColumn
xmdIPNetIFIqdrop = _XmdIPNetIFIqdrop_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 8),
    _XmdIPNetIFIqdrop_Type()
)
xmdIPNetIFIqdrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFIqdrop.setStatus("mandatory")
_XmdIPNetIFIunknproto_Type = Counter32
_XmdIPNetIFIunknproto_Object = MibTableColumn
xmdIPNetIFIunknproto = _XmdIPNetIFIunknproto_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 9),
    _XmdIPNetIFIunknproto_Type()
)
xmdIPNetIFIunknproto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFIunknproto.setStatus("mandatory")
_XmdIPNetIFOpacket_Type = Counter32
_XmdIPNetIFOpacket_Object = MibTableColumn
xmdIPNetIFOpacket = _XmdIPNetIFOpacket_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 10),
    _XmdIPNetIFOpacket_Type()
)
xmdIPNetIFOpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFOpacket.setStatus("mandatory")
_XmdIPNetIFOoctet_Type = Counter32
_XmdIPNetIFOoctet_Object = MibTableColumn
xmdIPNetIFOoctet = _XmdIPNetIFOoctet_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 11),
    _XmdIPNetIFOoctet_Type()
)
xmdIPNetIFOoctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFOoctet.setStatus("mandatory")
_XmdIPNetIFOoctetkb_Type = Counter32
_XmdIPNetIFOoctetkb_Object = MibTableColumn
xmdIPNetIFOoctetkb = _XmdIPNetIFOoctetkb_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 12),
    _XmdIPNetIFOoctetkb_Type()
)
xmdIPNetIFOoctetkb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFOoctetkb.setStatus("mandatory")
_XmdIPNetIFOerror_Type = Counter32
_XmdIPNetIFOerror_Object = MibTableColumn
xmdIPNetIFOerror = _XmdIPNetIFOerror_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 13),
    _XmdIPNetIFOerror_Type()
)
xmdIPNetIFOerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFOerror.setStatus("mandatory")
_XmdIPNetIFOmcastpkt_Type = Counter32
_XmdIPNetIFOmcastpkt_Object = MibTableColumn
xmdIPNetIFOmcastpkt = _XmdIPNetIFOmcastpkt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 14),
    _XmdIPNetIFOmcastpkt_Type()
)
xmdIPNetIFOmcastpkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFOmcastpkt.setStatus("mandatory")
_XmdIPNetIFOquelen_Type = Integer32
_XmdIPNetIFOquelen_Object = MibTableColumn
xmdIPNetIFOquelen = _XmdIPNetIFOquelen_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 15),
    _XmdIPNetIFOquelen_Type()
)
xmdIPNetIFOquelen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFOquelen.setStatus("mandatory")
_XmdIPNetIFOquemax_Type = Integer32
_XmdIPNetIFOquemax_Object = MibTableColumn
xmdIPNetIFOquemax = _XmdIPNetIFOquemax_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 16),
    _XmdIPNetIFOquemax_Type()
)
xmdIPNetIFOquemax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFOquemax.setStatus("mandatory")
_XmdIPNetIFOdrops_Type = Counter32
_XmdIPNetIFOdrops_Object = MibTableColumn
xmdIPNetIFOdrops = _XmdIPNetIFOdrops_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 10, 1, 17),
    _XmdIPNetIFOdrops_Type()
)
xmdIPNetIFOdrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPNetIFOdrops.setStatus("mandatory")
_XmdIPRouting_ObjectIdentity = ObjectIdentity
xmdIPRouting = _XmdIPRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 11)
)
_XmdIPRoutingBadred_Type = Counter32
_XmdIPRoutingBadred_Object = MibScalar
xmdIPRoutingBadred = _XmdIPRoutingBadred_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 11, 1),
    _XmdIPRoutingBadred_Type()
)
xmdIPRoutingBadred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPRoutingBadred.setStatus("mandatory")
_XmdIPRoutingDynamic_Type = Counter32
_XmdIPRoutingDynamic_Object = MibScalar
xmdIPRoutingDynamic = _XmdIPRoutingDynamic_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 11, 2),
    _XmdIPRoutingDynamic_Type()
)
xmdIPRoutingDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPRoutingDynamic.setStatus("mandatory")
_XmdIPRoutingNewgate_Type = Counter32
_XmdIPRoutingNewgate_Object = MibScalar
xmdIPRoutingNewgate = _XmdIPRoutingNewgate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 11, 3),
    _XmdIPRoutingNewgate_Type()
)
xmdIPRoutingNewgate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPRoutingNewgate.setStatus("mandatory")
_XmdIPRoutingUnreach_Type = Counter32
_XmdIPRoutingUnreach_Object = MibScalar
xmdIPRoutingUnreach = _XmdIPRoutingUnreach_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 11, 4),
    _XmdIPRoutingUnreach_Type()
)
xmdIPRoutingUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPRoutingUnreach.setStatus("mandatory")
_XmdIPRoutingWildc_Type = Counter32
_XmdIPRoutingWildc_Object = MibScalar
xmdIPRoutingWildc = _XmdIPRoutingWildc_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 11, 11, 5),
    _XmdIPRoutingWildc_Type()
)
xmdIPRoutingWildc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdIPRoutingWildc.setStatus("mandatory")
_XmdTCP_ObjectIdentity = ObjectIdentity
xmdTCP = _XmdTCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12)
)
_XmdTCPConattmpt_Type = Counter32
_XmdTCPConattmpt_Object = MibScalar
xmdTCPConattmpt = _XmdTCPConattmpt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 1),
    _XmdTCPConattmpt_Type()
)
xmdTCPConattmpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPConattmpt.setStatus("mandatory")
_XmdTCPAccept_Type = Counter32
_XmdTCPAccept_Object = MibScalar
xmdTCPAccept = _XmdTCPAccept_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 2),
    _XmdTCPAccept_Type()
)
xmdTCPAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPAccept.setStatus("mandatory")
_XmdTCPConnects_Type = Counter32
_XmdTCPConnects_Object = MibScalar
xmdTCPConnects = _XmdTCPConnects_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 3),
    _XmdTCPConnects_Type()
)
xmdTCPConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPConnects.setStatus("mandatory")
_XmdTCPClose_Type = Counter32
_XmdTCPClose_Object = MibScalar
xmdTCPClose = _XmdTCPClose_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 4),
    _XmdTCPClose_Type()
)
xmdTCPClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPClose.setStatus("mandatory")
_XmdTCPSndtotal_Type = Counter32
_XmdTCPSndtotal_Object = MibScalar
xmdTCPSndtotal = _XmdTCPSndtotal_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 5),
    _XmdTCPSndtotal_Type()
)
xmdTCPSndtotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPSndtotal.setStatus("mandatory")
_XmdTCPSndpack_Type = Counter32
_XmdTCPSndpack_Object = MibScalar
xmdTCPSndpack = _XmdTCPSndpack_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 6),
    _XmdTCPSndpack_Type()
)
xmdTCPSndpack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPSndpack.setStatus("mandatory")
_XmdTCPSndbyte_Type = Counter32
_XmdTCPSndbyte_Object = MibScalar
xmdTCPSndbyte = _XmdTCPSndbyte_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 7),
    _XmdTCPSndbyte_Type()
)
xmdTCPSndbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPSndbyte.setStatus("mandatory")
_XmdTCPSndrexmitpack_Type = Counter32
_XmdTCPSndrexmitpack_Object = MibScalar
xmdTCPSndrexmitpack = _XmdTCPSndrexmitpack_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 8),
    _XmdTCPSndrexmitpack_Type()
)
xmdTCPSndrexmitpack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPSndrexmitpack.setStatus("mandatory")
_XmdTCPSndrexmitbyte_Type = Counter32
_XmdTCPSndrexmitbyte_Object = MibScalar
xmdTCPSndrexmitbyte = _XmdTCPSndrexmitbyte_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 9),
    _XmdTCPSndrexmitbyte_Type()
)
xmdTCPSndrexmitbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPSndrexmitbyte.setStatus("mandatory")
_XmdTCPSndack_Type = Counter32
_XmdTCPSndack_Object = MibScalar
xmdTCPSndack = _XmdTCPSndack_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 10),
    _XmdTCPSndack_Type()
)
xmdTCPSndack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPSndack.setStatus("mandatory")
_XmdTCPSndprobe_Type = Counter32
_XmdTCPSndprobe_Object = MibScalar
xmdTCPSndprobe = _XmdTCPSndprobe_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 11),
    _XmdTCPSndprobe_Type()
)
xmdTCPSndprobe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPSndprobe.setStatus("mandatory")
_XmdTCPSndurg_Type = Counter32
_XmdTCPSndurg_Object = MibScalar
xmdTCPSndurg = _XmdTCPSndurg_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 12),
    _XmdTCPSndurg_Type()
)
xmdTCPSndurg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPSndurg.setStatus("mandatory")
_XmdTCPSndwinup_Type = Counter32
_XmdTCPSndwinup_Object = MibScalar
xmdTCPSndwinup = _XmdTCPSndwinup_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 13),
    _XmdTCPSndwinup_Type()
)
xmdTCPSndwinup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPSndwinup.setStatus("mandatory")
_XmdTCPSndctrl_Type = Counter32
_XmdTCPSndctrl_Object = MibScalar
xmdTCPSndctrl = _XmdTCPSndctrl_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 14),
    _XmdTCPSndctrl_Type()
)
xmdTCPSndctrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPSndctrl.setStatus("mandatory")
_XmdTCPRcvtotal_Type = Counter32
_XmdTCPRcvtotal_Object = MibScalar
xmdTCPRcvtotal = _XmdTCPRcvtotal_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 15),
    _XmdTCPRcvtotal_Type()
)
xmdTCPRcvtotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvtotal.setStatus("mandatory")
_XmdTCPRcvpack_Type = Counter32
_XmdTCPRcvpack_Object = MibScalar
xmdTCPRcvpack = _XmdTCPRcvpack_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 16),
    _XmdTCPRcvpack_Type()
)
xmdTCPRcvpack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvpack.setStatus("mandatory")
_XmdTCPRcvbyte_Type = Counter32
_XmdTCPRcvbyte_Object = MibScalar
xmdTCPRcvbyte = _XmdTCPRcvbyte_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 17),
    _XmdTCPRcvbyte_Type()
)
xmdTCPRcvbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvbyte.setStatus("mandatory")
_XmdTCPRcvduppack_Type = Counter32
_XmdTCPRcvduppack_Object = MibScalar
xmdTCPRcvduppack = _XmdTCPRcvduppack_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 18),
    _XmdTCPRcvduppack_Type()
)
xmdTCPRcvduppack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvduppack.setStatus("mandatory")
_XmdTCPRcvdupbyte_Type = Counter32
_XmdTCPRcvdupbyte_Object = MibScalar
xmdTCPRcvdupbyte = _XmdTCPRcvdupbyte_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 19),
    _XmdTCPRcvdupbyte_Type()
)
xmdTCPRcvdupbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvdupbyte.setStatus("mandatory")
_XmdTCPRcvpartduppack_Type = Counter32
_XmdTCPRcvpartduppack_Object = MibScalar
xmdTCPRcvpartduppack = _XmdTCPRcvpartduppack_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 20),
    _XmdTCPRcvpartduppack_Type()
)
xmdTCPRcvpartduppack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvpartduppack.setStatus("mandatory")
_XmdTCPRcvpartdupbyte_Type = Counter32
_XmdTCPRcvpartdupbyte_Object = MibScalar
xmdTCPRcvpartdupbyte = _XmdTCPRcvpartdupbyte_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 21),
    _XmdTCPRcvpartdupbyte_Type()
)
xmdTCPRcvpartdupbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvpartdupbyte.setStatus("mandatory")
_XmdTCPRcvoopack_Type = Counter32
_XmdTCPRcvoopack_Object = MibScalar
xmdTCPRcvoopack = _XmdTCPRcvoopack_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 22),
    _XmdTCPRcvoopack_Type()
)
xmdTCPRcvoopack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvoopack.setStatus("mandatory")
_XmdTCPRcvoobyte_Type = Counter32
_XmdTCPRcvoobyte_Object = MibScalar
xmdTCPRcvoobyte = _XmdTCPRcvoobyte_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 23),
    _XmdTCPRcvoobyte_Type()
)
xmdTCPRcvoobyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvoobyte.setStatus("mandatory")
_XmdTCPRcvaftwinpack_Type = Counter32
_XmdTCPRcvaftwinpack_Object = MibScalar
xmdTCPRcvaftwinpack = _XmdTCPRcvaftwinpack_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 24),
    _XmdTCPRcvaftwinpack_Type()
)
xmdTCPRcvaftwinpack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvaftwinpack.setStatus("mandatory")
_XmdTCPRcvaftwinbyte_Type = Counter32
_XmdTCPRcvaftwinbyte_Object = MibScalar
xmdTCPRcvaftwinbyte = _XmdTCPRcvaftwinbyte_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 25),
    _XmdTCPRcvaftwinbyte_Type()
)
xmdTCPRcvaftwinbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvaftwinbyte.setStatus("mandatory")
_XmdTCPRcvwinprobe_Type = Counter32
_XmdTCPRcvwinprobe_Object = MibScalar
xmdTCPRcvwinprobe = _XmdTCPRcvwinprobe_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 26),
    _XmdTCPRcvwinprobe_Type()
)
xmdTCPRcvwinprobe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvwinprobe.setStatus("mandatory")
_XmdTCPRcvdupack_Type = Counter32
_XmdTCPRcvdupack_Object = MibScalar
xmdTCPRcvdupack = _XmdTCPRcvdupack_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 27),
    _XmdTCPRcvdupack_Type()
)
xmdTCPRcvdupack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvdupack.setStatus("mandatory")
_XmdTCPRcvackpack_Type = Counter32
_XmdTCPRcvackpack_Object = MibScalar
xmdTCPRcvackpack = _XmdTCPRcvackpack_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 28),
    _XmdTCPRcvackpack_Type()
)
xmdTCPRcvackpack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvackpack.setStatus("mandatory")
_XmdTCPRcvackbyte_Type = Counter32
_XmdTCPRcvackbyte_Object = MibScalar
xmdTCPRcvackbyte = _XmdTCPRcvackbyte_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 29),
    _XmdTCPRcvackbyte_Type()
)
xmdTCPRcvackbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvackbyte.setStatus("mandatory")
_XmdTCPRcvwinup_Type = Counter32
_XmdTCPRcvwinup_Object = MibScalar
xmdTCPRcvwinup = _XmdTCPRcvwinup_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 30),
    _XmdTCPRcvwinup_Type()
)
xmdTCPRcvwinup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvwinup.setStatus("mandatory")
_XmdTCPSndkbyte_Type = Counter32
_XmdTCPSndkbyte_Object = MibScalar
xmdTCPSndkbyte = _XmdTCPSndkbyte_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 44),
    _XmdTCPSndkbyte_Type()
)
xmdTCPSndkbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPSndkbyte.setStatus("mandatory")
_XmdTCPRcvkbyte_Type = Counter32
_XmdTCPRcvkbyte_Object = MibScalar
xmdTCPRcvkbyte = _XmdTCPRcvkbyte_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 12, 45),
    _XmdTCPRcvkbyte_Type()
)
xmdTCPRcvkbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdTCPRcvkbyte.setStatus("mandatory")
_XmdUDP_ObjectIdentity = ObjectIdentity
xmdUDP = _XmdUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 13)
)
_XmdUDPRcvdgrm_Type = Counter32
_XmdUDPRcvdgrm_Object = MibScalar
xmdUDPRcvdgrm = _XmdUDPRcvdgrm_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 13, 1),
    _XmdUDPRcvdgrm_Type()
)
xmdUDPRcvdgrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdUDPRcvdgrm.setStatus("mandatory")
_XmdUDPNoport_Type = Counter32
_XmdUDPNoport_Object = MibScalar
xmdUDPNoport = _XmdUDPNoport_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 13, 2),
    _XmdUDPNoport_Type()
)
xmdUDPNoport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdUDPNoport.setStatus("mandatory")
_XmdUDPFullsock_Type = Counter32
_XmdUDPFullsock_Object = MibScalar
xmdUDPFullsock = _XmdUDPFullsock_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 13, 3),
    _XmdUDPFullsock_Type()
)
xmdUDPFullsock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdUDPFullsock.setStatus("mandatory")
_XmdUDPSnddgrm_Type = Counter32
_XmdUDPSnddgrm_Object = MibScalar
xmdUDPSnddgrm = _XmdUDPSnddgrm_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 13, 4),
    _XmdUDPSnddgrm_Type()
)
xmdUDPSnddgrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdUDPSnddgrm.setStatus("mandatory")
_XmdUDPNoportbc_Type = Counter32
_XmdUDPNoportbc_Object = MibScalar
xmdUDPNoportbc = _XmdUDPNoportbc_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 13, 5),
    _XmdUDPNoportbc_Type()
)
xmdUDPNoportbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdUDPNoportbc.setStatus("mandatory")
_XmdUDPHdrops_Type = Counter32
_XmdUDPHdrops_Object = MibScalar
xmdUDPHdrops = _XmdUDPHdrops_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 13, 6),
    _XmdUDPHdrops_Type()
)
xmdUDPHdrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdUDPHdrops.setStatus("mandatory")
_XmdUDPBadsum_Type = Counter32
_XmdUDPBadsum_Object = MibScalar
xmdUDPBadsum = _XmdUDPBadsum_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 13, 7),
    _XmdUDPBadsum_Type()
)
xmdUDPBadsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdUDPBadsum.setStatus("mandatory")
_XmdUDPBadlen_Type = Counter32
_XmdUDPBadlen_Object = MibScalar
xmdUDPBadlen = _XmdUDPBadlen_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 13, 8),
    _XmdUDPBadlen_Type()
)
xmdUDPBadlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdUDPBadlen.setStatus("mandatory")
_XmdUDPCachmiss_Type = Counter32
_XmdUDPCachmiss_Object = MibScalar
xmdUDPCachmiss = _XmdUDPCachmiss_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 13, 9),
    _XmdUDPCachmiss_Type()
)
xmdUDPCachmiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdUDPCachmiss.setStatus("mandatory")
_XmdRTime_ObjectIdentity = ObjectIdentity
xmdRTime = _XmdRTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 14)
)
_XmdRTimeLAN_ObjectIdentity = ObjectIdentity
xmdRTimeLAN = _XmdRTimeLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 14, 1)
)
_XmdRTimeARM_ObjectIdentity = ObjectIdentity
xmdRTimeARM = _XmdRTimeARM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 14, 2)
)
_XmdRPC_ObjectIdentity = ObjectIdentity
xmdRPC = _XmdRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16)
)
_XmdRPCClntCo_ObjectIdentity = ObjectIdentity
xmdRPCClntCo = _XmdRPCClntCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 1)
)
_XmdRPCClntCoCalls_Type = Counter32
_XmdRPCClntCoCalls_Object = MibScalar
xmdRPCClntCoCalls = _XmdRPCClntCoCalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 1, 1),
    _XmdRPCClntCoCalls_Type()
)
xmdRPCClntCoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntCoCalls.setStatus("mandatory")
_XmdRPCClntCoBadcalls_Type = Counter32
_XmdRPCClntCoBadcalls_Object = MibScalar
xmdRPCClntCoBadcalls = _XmdRPCClntCoBadcalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 1, 2),
    _XmdRPCClntCoBadcalls_Type()
)
xmdRPCClntCoBadcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntCoBadcalls.setStatus("mandatory")
_XmdRPCClntCoCantconn_Type = Counter32
_XmdRPCClntCoCantconn_Object = MibScalar
xmdRPCClntCoCantconn = _XmdRPCClntCoCantconn_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 1, 3),
    _XmdRPCClntCoCantconn_Type()
)
xmdRPCClntCoCantconn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntCoCantconn.setStatus("mandatory")
_XmdRPCClntCoBadxids_Type = Counter32
_XmdRPCClntCoBadxids_Object = MibScalar
xmdRPCClntCoBadxids = _XmdRPCClntCoBadxids_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 1, 4),
    _XmdRPCClntCoBadxids_Type()
)
xmdRPCClntCoBadxids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntCoBadxids.setStatus("mandatory")
_XmdRPCClntCoTimeouts_Type = Counter32
_XmdRPCClntCoTimeouts_Object = MibScalar
xmdRPCClntCoTimeouts = _XmdRPCClntCoTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 1, 5),
    _XmdRPCClntCoTimeouts_Type()
)
xmdRPCClntCoTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntCoTimeouts.setStatus("mandatory")
_XmdRPCClntCoNewcreds_Type = Counter32
_XmdRPCClntCoNewcreds_Object = MibScalar
xmdRPCClntCoNewcreds = _XmdRPCClntCoNewcreds_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 1, 6),
    _XmdRPCClntCoNewcreds_Type()
)
xmdRPCClntCoNewcreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntCoNewcreds.setStatus("mandatory")
_XmdRPCClntCoBadverfs_Type = Counter32
_XmdRPCClntCoBadverfs_Object = MibScalar
xmdRPCClntCoBadverfs = _XmdRPCClntCoBadverfs_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 1, 7),
    _XmdRPCClntCoBadverfs_Type()
)
xmdRPCClntCoBadverfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntCoBadverfs.setStatus("mandatory")
_XmdRPCClntCoTimers_Type = Counter32
_XmdRPCClntCoTimers_Object = MibScalar
xmdRPCClntCoTimers = _XmdRPCClntCoTimers_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 1, 8),
    _XmdRPCClntCoTimers_Type()
)
xmdRPCClntCoTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntCoTimers.setStatus("mandatory")
_XmdRPCClntCoNomem_Type = Counter32
_XmdRPCClntCoNomem_Object = MibScalar
xmdRPCClntCoNomem = _XmdRPCClntCoNomem_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 1, 9),
    _XmdRPCClntCoNomem_Type()
)
xmdRPCClntCoNomem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntCoNomem.setStatus("mandatory")
_XmdRPCClntCoInterrupts_Type = Counter32
_XmdRPCClntCoInterrupts_Object = MibScalar
xmdRPCClntCoInterrupts = _XmdRPCClntCoInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 1, 10),
    _XmdRPCClntCoInterrupts_Type()
)
xmdRPCClntCoInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntCoInterrupts.setStatus("mandatory")
_XmdRPCClntCl_ObjectIdentity = ObjectIdentity
xmdRPCClntCl = _XmdRPCClntCl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 2)
)
_XmdRPCClntClCalls_Type = Counter32
_XmdRPCClntClCalls_Object = MibScalar
xmdRPCClntClCalls = _XmdRPCClntClCalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 2, 1),
    _XmdRPCClntClCalls_Type()
)
xmdRPCClntClCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntClCalls.setStatus("mandatory")
_XmdRPCClntClBadcalls_Type = Counter32
_XmdRPCClntClBadcalls_Object = MibScalar
xmdRPCClntClBadcalls = _XmdRPCClntClBadcalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 2, 2),
    _XmdRPCClntClBadcalls_Type()
)
xmdRPCClntClBadcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntClBadcalls.setStatus("mandatory")
_XmdRPCClntClRetrans_Type = Counter32
_XmdRPCClntClRetrans_Object = MibScalar
xmdRPCClntClRetrans = _XmdRPCClntClRetrans_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 2, 3),
    _XmdRPCClntClRetrans_Type()
)
xmdRPCClntClRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntClRetrans.setStatus("mandatory")
_XmdRPCClntClBadxids_Type = Counter32
_XmdRPCClntClBadxids_Object = MibScalar
xmdRPCClntClBadxids = _XmdRPCClntClBadxids_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 2, 4),
    _XmdRPCClntClBadxids_Type()
)
xmdRPCClntClBadxids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntClBadxids.setStatus("mandatory")
_XmdRPCClntClTimeouts_Type = Counter32
_XmdRPCClntClTimeouts_Object = MibScalar
xmdRPCClntClTimeouts = _XmdRPCClntClTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 2, 5),
    _XmdRPCClntClTimeouts_Type()
)
xmdRPCClntClTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntClTimeouts.setStatus("mandatory")
_XmdRPCClntClNewcreds_Type = Counter32
_XmdRPCClntClNewcreds_Object = MibScalar
xmdRPCClntClNewcreds = _XmdRPCClntClNewcreds_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 2, 6),
    _XmdRPCClntClNewcreds_Type()
)
xmdRPCClntClNewcreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntClNewcreds.setStatus("mandatory")
_XmdRPCClntClBadverfs_Type = Counter32
_XmdRPCClntClBadverfs_Object = MibScalar
xmdRPCClntClBadverfs = _XmdRPCClntClBadverfs_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 2, 7),
    _XmdRPCClntClBadverfs_Type()
)
xmdRPCClntClBadverfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntClBadverfs.setStatus("mandatory")
_XmdRPCClntClTimers_Type = Counter32
_XmdRPCClntClTimers_Object = MibScalar
xmdRPCClntClTimers = _XmdRPCClntClTimers_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 2, 8),
    _XmdRPCClntClTimers_Type()
)
xmdRPCClntClTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntClTimers.setStatus("mandatory")
_XmdRPCClntClNomem_Type = Counter32
_XmdRPCClntClNomem_Object = MibScalar
xmdRPCClntClNomem = _XmdRPCClntClNomem_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 2, 9),
    _XmdRPCClntClNomem_Type()
)
xmdRPCClntClNomem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntClNomem.setStatus("mandatory")
_XmdRPCClntClCantsend_Type = Counter32
_XmdRPCClntClCantsend_Object = MibScalar
xmdRPCClntClCantsend = _XmdRPCClntClCantsend_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 2, 10),
    _XmdRPCClntClCantsend_Type()
)
xmdRPCClntClCantsend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCClntClCantsend.setStatus("mandatory")
_XmdRPCSvrCo_ObjectIdentity = ObjectIdentity
xmdRPCSvrCo = _XmdRPCSvrCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 3)
)
_XmdRPCSvrCoCalls_Type = Counter32
_XmdRPCSvrCoCalls_Object = MibScalar
xmdRPCSvrCoCalls = _XmdRPCSvrCoCalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 3, 1),
    _XmdRPCSvrCoCalls_Type()
)
xmdRPCSvrCoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrCoCalls.setStatus("mandatory")
_XmdRPCSvrCoBadcalls_Type = Counter32
_XmdRPCSvrCoBadcalls_Object = MibScalar
xmdRPCSvrCoBadcalls = _XmdRPCSvrCoBadcalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 3, 2),
    _XmdRPCSvrCoBadcalls_Type()
)
xmdRPCSvrCoBadcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrCoBadcalls.setStatus("mandatory")
_XmdRPCSvrCoNullrecv_Type = Counter32
_XmdRPCSvrCoNullrecv_Object = MibScalar
xmdRPCSvrCoNullrecv = _XmdRPCSvrCoNullrecv_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 3, 3),
    _XmdRPCSvrCoNullrecv_Type()
)
xmdRPCSvrCoNullrecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrCoNullrecv.setStatus("mandatory")
_XmdRPCSvrCoBadlen_Type = Counter32
_XmdRPCSvrCoBadlen_Object = MibScalar
xmdRPCSvrCoBadlen = _XmdRPCSvrCoBadlen_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 3, 4),
    _XmdRPCSvrCoBadlen_Type()
)
xmdRPCSvrCoBadlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrCoBadlen.setStatus("mandatory")
_XmdRPCSvrCoXdrcall_Type = Counter32
_XmdRPCSvrCoXdrcall_Object = MibScalar
xmdRPCSvrCoXdrcall = _XmdRPCSvrCoXdrcall_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 3, 5),
    _XmdRPCSvrCoXdrcall_Type()
)
xmdRPCSvrCoXdrcall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrCoXdrcall.setStatus("mandatory")
_XmdRPCSvrCoDupchecks_Type = Counter32
_XmdRPCSvrCoDupchecks_Object = MibScalar
xmdRPCSvrCoDupchecks = _XmdRPCSvrCoDupchecks_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 3, 6),
    _XmdRPCSvrCoDupchecks_Type()
)
xmdRPCSvrCoDupchecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrCoDupchecks.setStatus("mandatory")
_XmdRPCSvrCoDupreqs_Type = Counter32
_XmdRPCSvrCoDupreqs_Object = MibScalar
xmdRPCSvrCoDupreqs = _XmdRPCSvrCoDupreqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 3, 7),
    _XmdRPCSvrCoDupreqs_Type()
)
xmdRPCSvrCoDupreqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrCoDupreqs.setStatus("mandatory")
_XmdRPCSvrCl_ObjectIdentity = ObjectIdentity
xmdRPCSvrCl = _XmdRPCSvrCl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 4)
)
_XmdRPCSvrClCalls_Type = Counter32
_XmdRPCSvrClCalls_Object = MibScalar
xmdRPCSvrClCalls = _XmdRPCSvrClCalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 4, 1),
    _XmdRPCSvrClCalls_Type()
)
xmdRPCSvrClCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrClCalls.setStatus("mandatory")
_XmdRPCSvrClBadcalls_Type = Counter32
_XmdRPCSvrClBadcalls_Object = MibScalar
xmdRPCSvrClBadcalls = _XmdRPCSvrClBadcalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 4, 2),
    _XmdRPCSvrClBadcalls_Type()
)
xmdRPCSvrClBadcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrClBadcalls.setStatus("mandatory")
_XmdRPCSvrClNullrecv_Type = Counter32
_XmdRPCSvrClNullrecv_Object = MibScalar
xmdRPCSvrClNullrecv = _XmdRPCSvrClNullrecv_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 4, 3),
    _XmdRPCSvrClNullrecv_Type()
)
xmdRPCSvrClNullrecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrClNullrecv.setStatus("mandatory")
_XmdRPCSvrClBadlen_Type = Counter32
_XmdRPCSvrClBadlen_Object = MibScalar
xmdRPCSvrClBadlen = _XmdRPCSvrClBadlen_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 4, 4),
    _XmdRPCSvrClBadlen_Type()
)
xmdRPCSvrClBadlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrClBadlen.setStatus("mandatory")
_XmdRPCSvrClXdrcall_Type = Counter32
_XmdRPCSvrClXdrcall_Object = MibScalar
xmdRPCSvrClXdrcall = _XmdRPCSvrClXdrcall_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 4, 5),
    _XmdRPCSvrClXdrcall_Type()
)
xmdRPCSvrClXdrcall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrClXdrcall.setStatus("mandatory")
_XmdRPCSvrClDupchecks_Type = Counter32
_XmdRPCSvrClDupchecks_Object = MibScalar
xmdRPCSvrClDupchecks = _XmdRPCSvrClDupchecks_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 4, 6),
    _XmdRPCSvrClDupchecks_Type()
)
xmdRPCSvrClDupchecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrClDupchecks.setStatus("mandatory")
_XmdRPCSvrClDupreqs_Type = Counter32
_XmdRPCSvrClDupreqs_Object = MibScalar
xmdRPCSvrClDupreqs = _XmdRPCSvrClDupreqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 16, 4, 7),
    _XmdRPCSvrClDupreqs_Type()
)
xmdRPCSvrClDupreqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdRPCSvrClDupreqs.setStatus("mandatory")
_XmdNFS_ObjectIdentity = ObjectIdentity
xmdNFS = _XmdNFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17)
)
_XmdNFSClient_ObjectIdentity = ObjectIdentity
xmdNFSClient = _XmdNFSClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 1)
)
_XmdNFSClientCalls_Type = Counter32
_XmdNFSClientCalls_Object = MibScalar
xmdNFSClientCalls = _XmdNFSClientCalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 1, 1),
    _XmdNFSClientCalls_Type()
)
xmdNFSClientCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSClientCalls.setStatus("mandatory")
_XmdNFSClientBadcalls_Type = Counter32
_XmdNFSClientBadcalls_Object = MibScalar
xmdNFSClientBadcalls = _XmdNFSClientBadcalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 1, 2),
    _XmdNFSClientBadcalls_Type()
)
xmdNFSClientBadcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSClientBadcalls.setStatus("mandatory")
_XmdNFSServer_ObjectIdentity = ObjectIdentity
xmdNFSServer = _XmdNFSServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 2)
)
_XmdNFSServerCalls_Type = Counter32
_XmdNFSServerCalls_Object = MibScalar
xmdNFSServerCalls = _XmdNFSServerCalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 2, 1),
    _XmdNFSServerCalls_Type()
)
xmdNFSServerCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSServerCalls.setStatus("mandatory")
_XmdNFSServerBadcalls_Type = Counter32
_XmdNFSServerBadcalls_Object = MibScalar
xmdNFSServerBadcalls = _XmdNFSServerBadcalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 2, 2),
    _XmdNFSServerBadcalls_Type()
)
xmdNFSServerBadcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSServerBadcalls.setStatus("mandatory")
_XmdNFSV2Clnt_ObjectIdentity = ObjectIdentity
xmdNFSV2Clnt = _XmdNFSV2Clnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3)
)
_XmdNFSV2ClntNull_Type = Counter32
_XmdNFSV2ClntNull_Object = MibScalar
xmdNFSV2ClntNull = _XmdNFSV2ClntNull_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 1),
    _XmdNFSV2ClntNull_Type()
)
xmdNFSV2ClntNull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntNull.setStatus("mandatory")
_XmdNFSV2ClntGetattr_Type = Counter32
_XmdNFSV2ClntGetattr_Object = MibScalar
xmdNFSV2ClntGetattr = _XmdNFSV2ClntGetattr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 2),
    _XmdNFSV2ClntGetattr_Type()
)
xmdNFSV2ClntGetattr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntGetattr.setStatus("mandatory")
_XmdNFSV2ClntSetattr_Type = Counter32
_XmdNFSV2ClntSetattr_Object = MibScalar
xmdNFSV2ClntSetattr = _XmdNFSV2ClntSetattr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 3),
    _XmdNFSV2ClntSetattr_Type()
)
xmdNFSV2ClntSetattr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntSetattr.setStatus("mandatory")
_XmdNFSV2ClntRoot_Type = Counter32
_XmdNFSV2ClntRoot_Object = MibScalar
xmdNFSV2ClntRoot = _XmdNFSV2ClntRoot_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 4),
    _XmdNFSV2ClntRoot_Type()
)
xmdNFSV2ClntRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntRoot.setStatus("mandatory")
_XmdNFSV2ClntLookup_Type = Counter32
_XmdNFSV2ClntLookup_Object = MibScalar
xmdNFSV2ClntLookup = _XmdNFSV2ClntLookup_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 5),
    _XmdNFSV2ClntLookup_Type()
)
xmdNFSV2ClntLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntLookup.setStatus("mandatory")
_XmdNFSV2ClntReadlink_Type = Counter32
_XmdNFSV2ClntReadlink_Object = MibScalar
xmdNFSV2ClntReadlink = _XmdNFSV2ClntReadlink_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 6),
    _XmdNFSV2ClntReadlink_Type()
)
xmdNFSV2ClntReadlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntReadlink.setStatus("mandatory")
_XmdNFSV2ClntRead_Type = Counter32
_XmdNFSV2ClntRead_Object = MibScalar
xmdNFSV2ClntRead = _XmdNFSV2ClntRead_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 7),
    _XmdNFSV2ClntRead_Type()
)
xmdNFSV2ClntRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntRead.setStatus("mandatory")
_XmdNFSV2ClntWrcache_Type = Counter32
_XmdNFSV2ClntWrcache_Object = MibScalar
xmdNFSV2ClntWrcache = _XmdNFSV2ClntWrcache_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 8),
    _XmdNFSV2ClntWrcache_Type()
)
xmdNFSV2ClntWrcache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntWrcache.setStatus("mandatory")
_XmdNFSV2ClntWrite_Type = Counter32
_XmdNFSV2ClntWrite_Object = MibScalar
xmdNFSV2ClntWrite = _XmdNFSV2ClntWrite_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 9),
    _XmdNFSV2ClntWrite_Type()
)
xmdNFSV2ClntWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntWrite.setStatus("mandatory")
_XmdNFSV2ClntCreate_Type = Counter32
_XmdNFSV2ClntCreate_Object = MibScalar
xmdNFSV2ClntCreate = _XmdNFSV2ClntCreate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 10),
    _XmdNFSV2ClntCreate_Type()
)
xmdNFSV2ClntCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntCreate.setStatus("mandatory")
_XmdNFSV2ClntRemove_Type = Counter32
_XmdNFSV2ClntRemove_Object = MibScalar
xmdNFSV2ClntRemove = _XmdNFSV2ClntRemove_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 11),
    _XmdNFSV2ClntRemove_Type()
)
xmdNFSV2ClntRemove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntRemove.setStatus("mandatory")
_XmdNFSV2ClntRename_Type = Counter32
_XmdNFSV2ClntRename_Object = MibScalar
xmdNFSV2ClntRename = _XmdNFSV2ClntRename_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 12),
    _XmdNFSV2ClntRename_Type()
)
xmdNFSV2ClntRename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntRename.setStatus("mandatory")
_XmdNFSV2ClntLink_Type = Counter32
_XmdNFSV2ClntLink_Object = MibScalar
xmdNFSV2ClntLink = _XmdNFSV2ClntLink_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 13),
    _XmdNFSV2ClntLink_Type()
)
xmdNFSV2ClntLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntLink.setStatus("mandatory")
_XmdNFSV2ClntSymlink_Type = Counter32
_XmdNFSV2ClntSymlink_Object = MibScalar
xmdNFSV2ClntSymlink = _XmdNFSV2ClntSymlink_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 14),
    _XmdNFSV2ClntSymlink_Type()
)
xmdNFSV2ClntSymlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntSymlink.setStatus("mandatory")
_XmdNFSV2ClntMkdir_Type = Counter32
_XmdNFSV2ClntMkdir_Object = MibScalar
xmdNFSV2ClntMkdir = _XmdNFSV2ClntMkdir_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 15),
    _XmdNFSV2ClntMkdir_Type()
)
xmdNFSV2ClntMkdir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntMkdir.setStatus("mandatory")
_XmdNFSV2ClntRmdir_Type = Counter32
_XmdNFSV2ClntRmdir_Object = MibScalar
xmdNFSV2ClntRmdir = _XmdNFSV2ClntRmdir_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 16),
    _XmdNFSV2ClntRmdir_Type()
)
xmdNFSV2ClntRmdir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntRmdir.setStatus("mandatory")
_XmdNFSV2ClntReaddir_Type = Counter32
_XmdNFSV2ClntReaddir_Object = MibScalar
xmdNFSV2ClntReaddir = _XmdNFSV2ClntReaddir_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 17),
    _XmdNFSV2ClntReaddir_Type()
)
xmdNFSV2ClntReaddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntReaddir.setStatus("mandatory")
_XmdNFSV2ClntStatfs_Type = Counter32
_XmdNFSV2ClntStatfs_Object = MibScalar
xmdNFSV2ClntStatfs = _XmdNFSV2ClntStatfs_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 3, 18),
    _XmdNFSV2ClntStatfs_Type()
)
xmdNFSV2ClntStatfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2ClntStatfs.setStatus("mandatory")
_XmdNFSV2Svr_ObjectIdentity = ObjectIdentity
xmdNFSV2Svr = _XmdNFSV2Svr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4)
)
_XmdNFSV2SvrNull_Type = Counter32
_XmdNFSV2SvrNull_Object = MibScalar
xmdNFSV2SvrNull = _XmdNFSV2SvrNull_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 1),
    _XmdNFSV2SvrNull_Type()
)
xmdNFSV2SvrNull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrNull.setStatus("mandatory")
_XmdNFSV2SvrGetattr_Type = Counter32
_XmdNFSV2SvrGetattr_Object = MibScalar
xmdNFSV2SvrGetattr = _XmdNFSV2SvrGetattr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 2),
    _XmdNFSV2SvrGetattr_Type()
)
xmdNFSV2SvrGetattr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrGetattr.setStatus("mandatory")
_XmdNFSV2SvrSetattr_Type = Counter32
_XmdNFSV2SvrSetattr_Object = MibScalar
xmdNFSV2SvrSetattr = _XmdNFSV2SvrSetattr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 3),
    _XmdNFSV2SvrSetattr_Type()
)
xmdNFSV2SvrSetattr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrSetattr.setStatus("mandatory")
_XmdNFSV2SvrRoot_Type = Counter32
_XmdNFSV2SvrRoot_Object = MibScalar
xmdNFSV2SvrRoot = _XmdNFSV2SvrRoot_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 4),
    _XmdNFSV2SvrRoot_Type()
)
xmdNFSV2SvrRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrRoot.setStatus("mandatory")
_XmdNFSV2SvrLookup_Type = Counter32
_XmdNFSV2SvrLookup_Object = MibScalar
xmdNFSV2SvrLookup = _XmdNFSV2SvrLookup_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 5),
    _XmdNFSV2SvrLookup_Type()
)
xmdNFSV2SvrLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrLookup.setStatus("mandatory")
_XmdNFSV2SvrReadlink_Type = Counter32
_XmdNFSV2SvrReadlink_Object = MibScalar
xmdNFSV2SvrReadlink = _XmdNFSV2SvrReadlink_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 6),
    _XmdNFSV2SvrReadlink_Type()
)
xmdNFSV2SvrReadlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrReadlink.setStatus("mandatory")
_XmdNFSV2SvrRead_Type = Counter32
_XmdNFSV2SvrRead_Object = MibScalar
xmdNFSV2SvrRead = _XmdNFSV2SvrRead_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 7),
    _XmdNFSV2SvrRead_Type()
)
xmdNFSV2SvrRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrRead.setStatus("mandatory")
_XmdNFSV2SvrWrcache_Type = Counter32
_XmdNFSV2SvrWrcache_Object = MibScalar
xmdNFSV2SvrWrcache = _XmdNFSV2SvrWrcache_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 8),
    _XmdNFSV2SvrWrcache_Type()
)
xmdNFSV2SvrWrcache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrWrcache.setStatus("mandatory")
_XmdNFSV2SvrWrite_Type = Counter32
_XmdNFSV2SvrWrite_Object = MibScalar
xmdNFSV2SvrWrite = _XmdNFSV2SvrWrite_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 9),
    _XmdNFSV2SvrWrite_Type()
)
xmdNFSV2SvrWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrWrite.setStatus("mandatory")
_XmdNFSV2SvrCreate_Type = Counter32
_XmdNFSV2SvrCreate_Object = MibScalar
xmdNFSV2SvrCreate = _XmdNFSV2SvrCreate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 10),
    _XmdNFSV2SvrCreate_Type()
)
xmdNFSV2SvrCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrCreate.setStatus("mandatory")
_XmdNFSV2SvrRemove_Type = Counter32
_XmdNFSV2SvrRemove_Object = MibScalar
xmdNFSV2SvrRemove = _XmdNFSV2SvrRemove_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 11),
    _XmdNFSV2SvrRemove_Type()
)
xmdNFSV2SvrRemove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrRemove.setStatus("mandatory")
_XmdNFSV2SvrRename_Type = Counter32
_XmdNFSV2SvrRename_Object = MibScalar
xmdNFSV2SvrRename = _XmdNFSV2SvrRename_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 12),
    _XmdNFSV2SvrRename_Type()
)
xmdNFSV2SvrRename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrRename.setStatus("mandatory")
_XmdNFSV2SvrLink_Type = Counter32
_XmdNFSV2SvrLink_Object = MibScalar
xmdNFSV2SvrLink = _XmdNFSV2SvrLink_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 13),
    _XmdNFSV2SvrLink_Type()
)
xmdNFSV2SvrLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrLink.setStatus("mandatory")
_XmdNFSV2SvrSymlink_Type = Counter32
_XmdNFSV2SvrSymlink_Object = MibScalar
xmdNFSV2SvrSymlink = _XmdNFSV2SvrSymlink_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 14),
    _XmdNFSV2SvrSymlink_Type()
)
xmdNFSV2SvrSymlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrSymlink.setStatus("mandatory")
_XmdNFSV2SvrMkdir_Type = Counter32
_XmdNFSV2SvrMkdir_Object = MibScalar
xmdNFSV2SvrMkdir = _XmdNFSV2SvrMkdir_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 15),
    _XmdNFSV2SvrMkdir_Type()
)
xmdNFSV2SvrMkdir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrMkdir.setStatus("mandatory")
_XmdNFSV2SvrRmdir_Type = Counter32
_XmdNFSV2SvrRmdir_Object = MibScalar
xmdNFSV2SvrRmdir = _XmdNFSV2SvrRmdir_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 16),
    _XmdNFSV2SvrRmdir_Type()
)
xmdNFSV2SvrRmdir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrRmdir.setStatus("mandatory")
_XmdNFSV2SvrReaddir_Type = Counter32
_XmdNFSV2SvrReaddir_Object = MibScalar
xmdNFSV2SvrReaddir = _XmdNFSV2SvrReaddir_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 17),
    _XmdNFSV2SvrReaddir_Type()
)
xmdNFSV2SvrReaddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrReaddir.setStatus("mandatory")
_XmdNFSV2SvrStatfs_Type = Counter32
_XmdNFSV2SvrStatfs_Object = MibScalar
xmdNFSV2SvrStatfs = _XmdNFSV2SvrStatfs_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 4, 18),
    _XmdNFSV2SvrStatfs_Type()
)
xmdNFSV2SvrStatfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV2SvrStatfs.setStatus("mandatory")
_XmdNFSV3Clnt_ObjectIdentity = ObjectIdentity
xmdNFSV3Clnt = _XmdNFSV3Clnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5)
)
_XmdNFSV3ClntNull_Type = Counter32
_XmdNFSV3ClntNull_Object = MibScalar
xmdNFSV3ClntNull = _XmdNFSV3ClntNull_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 1),
    _XmdNFSV3ClntNull_Type()
)
xmdNFSV3ClntNull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntNull.setStatus("mandatory")
_XmdNFSV3ClntGetattr_Type = Counter32
_XmdNFSV3ClntGetattr_Object = MibScalar
xmdNFSV3ClntGetattr = _XmdNFSV3ClntGetattr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 2),
    _XmdNFSV3ClntGetattr_Type()
)
xmdNFSV3ClntGetattr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntGetattr.setStatus("mandatory")
_XmdNFSV3ClntSetattr_Type = Counter32
_XmdNFSV3ClntSetattr_Object = MibScalar
xmdNFSV3ClntSetattr = _XmdNFSV3ClntSetattr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 3),
    _XmdNFSV3ClntSetattr_Type()
)
xmdNFSV3ClntSetattr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntSetattr.setStatus("mandatory")
_XmdNFSV3ClntLookup_Type = Counter32
_XmdNFSV3ClntLookup_Object = MibScalar
xmdNFSV3ClntLookup = _XmdNFSV3ClntLookup_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 4),
    _XmdNFSV3ClntLookup_Type()
)
xmdNFSV3ClntLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntLookup.setStatus("mandatory")
_XmdNFSV3ClntAccess_Type = Counter32
_XmdNFSV3ClntAccess_Object = MibScalar
xmdNFSV3ClntAccess = _XmdNFSV3ClntAccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 5),
    _XmdNFSV3ClntAccess_Type()
)
xmdNFSV3ClntAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntAccess.setStatus("mandatory")
_XmdNFSV3ClntReadlink_Type = Counter32
_XmdNFSV3ClntReadlink_Object = MibScalar
xmdNFSV3ClntReadlink = _XmdNFSV3ClntReadlink_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 6),
    _XmdNFSV3ClntReadlink_Type()
)
xmdNFSV3ClntReadlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntReadlink.setStatus("mandatory")
_XmdNFSV3ClntRead_Type = Counter32
_XmdNFSV3ClntRead_Object = MibScalar
xmdNFSV3ClntRead = _XmdNFSV3ClntRead_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 7),
    _XmdNFSV3ClntRead_Type()
)
xmdNFSV3ClntRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntRead.setStatus("mandatory")
_XmdNFSV3ClntWrite_Type = Counter32
_XmdNFSV3ClntWrite_Object = MibScalar
xmdNFSV3ClntWrite = _XmdNFSV3ClntWrite_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 8),
    _XmdNFSV3ClntWrite_Type()
)
xmdNFSV3ClntWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntWrite.setStatus("mandatory")
_XmdNFSV3ClntCreate_Type = Counter32
_XmdNFSV3ClntCreate_Object = MibScalar
xmdNFSV3ClntCreate = _XmdNFSV3ClntCreate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 9),
    _XmdNFSV3ClntCreate_Type()
)
xmdNFSV3ClntCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntCreate.setStatus("mandatory")
_XmdNFSV3ClntSymlink_Type = Counter32
_XmdNFSV3ClntSymlink_Object = MibScalar
xmdNFSV3ClntSymlink = _XmdNFSV3ClntSymlink_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 10),
    _XmdNFSV3ClntSymlink_Type()
)
xmdNFSV3ClntSymlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntSymlink.setStatus("mandatory")
_XmdNFSV3ClntMknod_Type = Counter32
_XmdNFSV3ClntMknod_Object = MibScalar
xmdNFSV3ClntMknod = _XmdNFSV3ClntMknod_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 11),
    _XmdNFSV3ClntMknod_Type()
)
xmdNFSV3ClntMknod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntMknod.setStatus("mandatory")
_XmdNFSV3ClntRemove_Type = Counter32
_XmdNFSV3ClntRemove_Object = MibScalar
xmdNFSV3ClntRemove = _XmdNFSV3ClntRemove_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 12),
    _XmdNFSV3ClntRemove_Type()
)
xmdNFSV3ClntRemove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntRemove.setStatus("mandatory")
_XmdNFSV3ClntRmdir_Type = Counter32
_XmdNFSV3ClntRmdir_Object = MibScalar
xmdNFSV3ClntRmdir = _XmdNFSV3ClntRmdir_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 13),
    _XmdNFSV3ClntRmdir_Type()
)
xmdNFSV3ClntRmdir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntRmdir.setStatus("mandatory")
_XmdNFSV3ClntMkdir_Type = Counter32
_XmdNFSV3ClntMkdir_Object = MibScalar
xmdNFSV3ClntMkdir = _XmdNFSV3ClntMkdir_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 14),
    _XmdNFSV3ClntMkdir_Type()
)
xmdNFSV3ClntMkdir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntMkdir.setStatus("mandatory")
_XmdNFSV3ClntRename_Type = Counter32
_XmdNFSV3ClntRename_Object = MibScalar
xmdNFSV3ClntRename = _XmdNFSV3ClntRename_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 15),
    _XmdNFSV3ClntRename_Type()
)
xmdNFSV3ClntRename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntRename.setStatus("mandatory")
_XmdNFSV3ClntLink_Type = Counter32
_XmdNFSV3ClntLink_Object = MibScalar
xmdNFSV3ClntLink = _XmdNFSV3ClntLink_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 16),
    _XmdNFSV3ClntLink_Type()
)
xmdNFSV3ClntLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntLink.setStatus("mandatory")
_XmdNFSV3ClntReaddir_Type = Counter32
_XmdNFSV3ClntReaddir_Object = MibScalar
xmdNFSV3ClntReaddir = _XmdNFSV3ClntReaddir_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 17),
    _XmdNFSV3ClntReaddir_Type()
)
xmdNFSV3ClntReaddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntReaddir.setStatus("mandatory")
_XmdNFSV3ClntReaddir_plus_Type = Counter32
_XmdNFSV3ClntReaddir_plus_Object = MibScalar
xmdNFSV3ClntReaddir_plus = _XmdNFSV3ClntReaddir_plus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 18),
    _XmdNFSV3ClntReaddir_plus_Type()
)
xmdNFSV3ClntReaddir_plus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntReaddir_plus.setStatus("mandatory")
_XmdNFSV3ClntFsstat_Type = Counter32
_XmdNFSV3ClntFsstat_Object = MibScalar
xmdNFSV3ClntFsstat = _XmdNFSV3ClntFsstat_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 19),
    _XmdNFSV3ClntFsstat_Type()
)
xmdNFSV3ClntFsstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntFsstat.setStatus("mandatory")
_XmdNFSV3ClntFsinfo_Type = Counter32
_XmdNFSV3ClntFsinfo_Object = MibScalar
xmdNFSV3ClntFsinfo = _XmdNFSV3ClntFsinfo_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 20),
    _XmdNFSV3ClntFsinfo_Type()
)
xmdNFSV3ClntFsinfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntFsinfo.setStatus("mandatory")
_XmdNFSV3ClntPathconf_Type = Counter32
_XmdNFSV3ClntPathconf_Object = MibScalar
xmdNFSV3ClntPathconf = _XmdNFSV3ClntPathconf_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 21),
    _XmdNFSV3ClntPathconf_Type()
)
xmdNFSV3ClntPathconf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntPathconf.setStatus("mandatory")
_XmdNFSV3ClntCommit_Type = Counter32
_XmdNFSV3ClntCommit_Object = MibScalar
xmdNFSV3ClntCommit = _XmdNFSV3ClntCommit_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 5, 22),
    _XmdNFSV3ClntCommit_Type()
)
xmdNFSV3ClntCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3ClntCommit.setStatus("mandatory")
_XmdNFSV3Svr_ObjectIdentity = ObjectIdentity
xmdNFSV3Svr = _XmdNFSV3Svr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6)
)
_XmdNFSV3SvrNull_Type = Counter32
_XmdNFSV3SvrNull_Object = MibScalar
xmdNFSV3SvrNull = _XmdNFSV3SvrNull_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 1),
    _XmdNFSV3SvrNull_Type()
)
xmdNFSV3SvrNull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrNull.setStatus("mandatory")
_XmdNFSV3SvrGetattr_Type = Counter32
_XmdNFSV3SvrGetattr_Object = MibScalar
xmdNFSV3SvrGetattr = _XmdNFSV3SvrGetattr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 2),
    _XmdNFSV3SvrGetattr_Type()
)
xmdNFSV3SvrGetattr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrGetattr.setStatus("mandatory")
_XmdNFSV3SvrSetattr_Type = Counter32
_XmdNFSV3SvrSetattr_Object = MibScalar
xmdNFSV3SvrSetattr = _XmdNFSV3SvrSetattr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 3),
    _XmdNFSV3SvrSetattr_Type()
)
xmdNFSV3SvrSetattr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrSetattr.setStatus("mandatory")
_XmdNFSV3SvrLookup_Type = Counter32
_XmdNFSV3SvrLookup_Object = MibScalar
xmdNFSV3SvrLookup = _XmdNFSV3SvrLookup_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 4),
    _XmdNFSV3SvrLookup_Type()
)
xmdNFSV3SvrLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrLookup.setStatus("mandatory")
_XmdNFSV3SvrAccess_Type = Counter32
_XmdNFSV3SvrAccess_Object = MibScalar
xmdNFSV3SvrAccess = _XmdNFSV3SvrAccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 5),
    _XmdNFSV3SvrAccess_Type()
)
xmdNFSV3SvrAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrAccess.setStatus("mandatory")
_XmdNFSV3SvrReadlink_Type = Counter32
_XmdNFSV3SvrReadlink_Object = MibScalar
xmdNFSV3SvrReadlink = _XmdNFSV3SvrReadlink_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 6),
    _XmdNFSV3SvrReadlink_Type()
)
xmdNFSV3SvrReadlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrReadlink.setStatus("mandatory")
_XmdNFSV3SvrRead_Type = Counter32
_XmdNFSV3SvrRead_Object = MibScalar
xmdNFSV3SvrRead = _XmdNFSV3SvrRead_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 7),
    _XmdNFSV3SvrRead_Type()
)
xmdNFSV3SvrRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrRead.setStatus("mandatory")
_XmdNFSV3SvrWrite_Type = Counter32
_XmdNFSV3SvrWrite_Object = MibScalar
xmdNFSV3SvrWrite = _XmdNFSV3SvrWrite_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 8),
    _XmdNFSV3SvrWrite_Type()
)
xmdNFSV3SvrWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrWrite.setStatus("mandatory")
_XmdNFSV3SvrCreate_Type = Counter32
_XmdNFSV3SvrCreate_Object = MibScalar
xmdNFSV3SvrCreate = _XmdNFSV3SvrCreate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 9),
    _XmdNFSV3SvrCreate_Type()
)
xmdNFSV3SvrCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrCreate.setStatus("mandatory")
_XmdNFSV3SvrMkdir_Type = Counter32
_XmdNFSV3SvrMkdir_Object = MibScalar
xmdNFSV3SvrMkdir = _XmdNFSV3SvrMkdir_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 10),
    _XmdNFSV3SvrMkdir_Type()
)
xmdNFSV3SvrMkdir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrMkdir.setStatus("mandatory")
_XmdNFSV3SvrSymlink_Type = Counter32
_XmdNFSV3SvrSymlink_Object = MibScalar
xmdNFSV3SvrSymlink = _XmdNFSV3SvrSymlink_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 11),
    _XmdNFSV3SvrSymlink_Type()
)
xmdNFSV3SvrSymlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrSymlink.setStatus("mandatory")
_XmdNFSV3SvrMknod_Type = Counter32
_XmdNFSV3SvrMknod_Object = MibScalar
xmdNFSV3SvrMknod = _XmdNFSV3SvrMknod_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 12),
    _XmdNFSV3SvrMknod_Type()
)
xmdNFSV3SvrMknod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrMknod.setStatus("mandatory")
_XmdNFSV3SvrRemove_Type = Counter32
_XmdNFSV3SvrRemove_Object = MibScalar
xmdNFSV3SvrRemove = _XmdNFSV3SvrRemove_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 13),
    _XmdNFSV3SvrRemove_Type()
)
xmdNFSV3SvrRemove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrRemove.setStatus("mandatory")
_XmdNFSV3SvrRmdir_Type = Counter32
_XmdNFSV3SvrRmdir_Object = MibScalar
xmdNFSV3SvrRmdir = _XmdNFSV3SvrRmdir_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 14),
    _XmdNFSV3SvrRmdir_Type()
)
xmdNFSV3SvrRmdir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrRmdir.setStatus("mandatory")
_XmdNFSV3SvrRename_Type = Counter32
_XmdNFSV3SvrRename_Object = MibScalar
xmdNFSV3SvrRename = _XmdNFSV3SvrRename_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 15),
    _XmdNFSV3SvrRename_Type()
)
xmdNFSV3SvrRename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrRename.setStatus("mandatory")
_XmdNFSV3SvrLink_Type = Counter32
_XmdNFSV3SvrLink_Object = MibScalar
xmdNFSV3SvrLink = _XmdNFSV3SvrLink_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 16),
    _XmdNFSV3SvrLink_Type()
)
xmdNFSV3SvrLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrLink.setStatus("mandatory")
_XmdNFSV3SvrReaddir_Type = Counter32
_XmdNFSV3SvrReaddir_Object = MibScalar
xmdNFSV3SvrReaddir = _XmdNFSV3SvrReaddir_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 17),
    _XmdNFSV3SvrReaddir_Type()
)
xmdNFSV3SvrReaddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrReaddir.setStatus("mandatory")
_XmdNFSV3SvrReaddir_plus_Type = Counter32
_XmdNFSV3SvrReaddir_plus_Object = MibScalar
xmdNFSV3SvrReaddir_plus = _XmdNFSV3SvrReaddir_plus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 18),
    _XmdNFSV3SvrReaddir_plus_Type()
)
xmdNFSV3SvrReaddir_plus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrReaddir_plus.setStatus("mandatory")
_XmdNFSV3SvrFsstat_Type = Counter32
_XmdNFSV3SvrFsstat_Object = MibScalar
xmdNFSV3SvrFsstat = _XmdNFSV3SvrFsstat_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 19),
    _XmdNFSV3SvrFsstat_Type()
)
xmdNFSV3SvrFsstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrFsstat.setStatus("mandatory")
_XmdNFSV3SvrFsinfo_Type = Counter32
_XmdNFSV3SvrFsinfo_Object = MibScalar
xmdNFSV3SvrFsinfo = _XmdNFSV3SvrFsinfo_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 20),
    _XmdNFSV3SvrFsinfo_Type()
)
xmdNFSV3SvrFsinfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrFsinfo.setStatus("mandatory")
_XmdNFSV3SvrPathconf_Type = Counter32
_XmdNFSV3SvrPathconf_Object = MibScalar
xmdNFSV3SvrPathconf = _XmdNFSV3SvrPathconf_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 21),
    _XmdNFSV3SvrPathconf_Type()
)
xmdNFSV3SvrPathconf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrPathconf.setStatus("mandatory")
_XmdNFSV3SvrCommit_Type = Counter32
_XmdNFSV3SvrCommit_Object = MibScalar
xmdNFSV3SvrCommit = _XmdNFSV3SvrCommit_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 17, 6, 22),
    _XmdNFSV3SvrCommit_Type()
)
xmdNFSV3SvrCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdNFSV3SvrCommit.setStatus("mandatory")
_XmdDCE_ObjectIdentity = ObjectIdentity
xmdDCE = _XmdDCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 28)
)
_XmdSpmi_ObjectIdentity = ObjectIdentity
xmdSpmi = _XmdSpmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 98)
)
_XmdSpmiUsers_Type = Integer32
_XmdSpmiUsers_Object = MibScalar
xmdSpmiUsers = _XmdSpmiUsers_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 98, 1),
    _XmdSpmiUsers_Type()
)
xmdSpmiUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSpmiUsers.setStatus("mandatory")
_XmdSpmiStatsets_Type = Integer32
_XmdSpmiStatsets_Object = MibScalar
xmdSpmiStatsets = _XmdSpmiStatsets_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 98, 2),
    _XmdSpmiStatsets_Type()
)
xmdSpmiStatsets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSpmiStatsets.setStatus("mandatory")
_XmdSpmiDdscount_Type = Integer32
_XmdSpmiDdscount_Object = MibScalar
xmdSpmiDdscount = _XmdSpmiDdscount_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 98, 3),
    _XmdSpmiDdscount_Type()
)
xmdSpmiDdscount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSpmiDdscount.setStatus("mandatory")
_XmdSpmiConsumers_Type = Integer32
_XmdSpmiConsumers_Object = MibScalar
xmdSpmiConsumers = _XmdSpmiConsumers_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 98, 4),
    _XmdSpmiConsumers_Type()
)
xmdSpmiConsumers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSpmiConsumers.setStatus("mandatory")
_XmdSpmiComused_Type = Integer32
_XmdSpmiComused_Object = MibScalar
xmdSpmiComused = _XmdSpmiComused_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 98, 5),
    _XmdSpmiComused_Type()
)
xmdSpmiComused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSpmiComused.setStatus("mandatory")
_XmdSpmiHotsets_Type = Integer32
_XmdSpmiHotsets_Object = MibScalar
xmdSpmiHotsets = _XmdSpmiHotsets_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 98, 6),
    _XmdSpmiHotsets_Type()
)
xmdSpmiHotsets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmdSpmiHotsets.setStatus("mandatory")
_XmdDDS_ObjectIdentity = ObjectIdentity
xmdDDS = _XmdDDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 2, 2, 1, 99)
)
_Risc6000public_ObjectIdentity = ObjectIdentity
risc6000public = _Risc6000public_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 2, 3)
)
_Aix370_ObjectIdentity = ObjectIdentity
aix370 = _Aix370_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 3)
)
_AixPS2_ObjectIdentity = ObjectIdentity
aixPS2 = _AixPS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 1, 4)
)
_Mvs_ObjectIdentity = ObjectIdentity
mvs = _Mvs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 2)
)
_Mvs370_ObjectIdentity = ObjectIdentity
mvs370 = _Mvs370_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 2, 1)
)
_Vm_ObjectIdentity = ObjectIdentity
vm = _Vm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 3)
)
_Vm370_ObjectIdentity = ObjectIdentity
vm370 = _Vm370_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 3, 1)
)
_Os2_ObjectIdentity = ObjectIdentity
os2 = _Os2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 4)
)
_Ps2PS2_ObjectIdentity = ObjectIdentity
ps2PS2 = _Ps2PS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 4, 1)
)
_Os400_ObjectIdentity = ObjectIdentity
os400 = _Os400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 5)
)
_Os400as400_ObjectIdentity = ObjectIdentity
os400as400 = _Os400as400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 5, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XMSERVD-PERF-MIB",
    **{"directory": directory,
       "mgmt": mgmt,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "ibm": ibm,
       "ibmAgents": ibmAgents,
       "aix": aix,
       "aixRT": aixRT,
       "aixRISC6000": aixRISC6000,
       "risc6000agents": risc6000agents,
       "risc6000snmpd": risc6000snmpd,
       "risc6000gated": risc6000gated,
       "risc6000xmservd": risc6000xmservd,
       "risc6000ibm7318": risc6000ibm7318,
       "risc6000clsmuxpd": risc6000clsmuxpd,
       "risc6000private": risc6000private,
       "risc6000samples": risc6000samples,
       "risc6000sampleAgents": risc6000sampleAgents,
       "risc6000perf": risc6000perf,
       "xmd": xmd,
       "xmdCPU": xmdCPU,
       "xmdCPUGluser": xmdCPUGluser,
       "xmdCPUGlkern": xmdCPUGlkern,
       "xmdCPUGlwait": xmdCPUGlwait,
       "xmdCPUGlidle": xmdCPUGlidle,
       "xmdCPUGluticks": xmdCPUGluticks,
       "xmdCPUGlkticks": xmdCPUGlkticks,
       "xmdCPUGlwticks": xmdCPUGlwticks,
       "xmdCPUGliticks": xmdCPUGliticks,
       "xmdMem": xmdMem,
       "xmdMemReal": xmdMemReal,
       "xmdMemRealSize": xmdMemRealSize,
       "xmdMemRealNumfrb": xmdMemRealNumfrb,
       "xmdMemRealNoncomp": xmdMemRealNoncomp,
       "xmdMemRealComp": xmdMemRealComp,
       "xmdMemRealNumlocal": xmdMemRealNumlocal,
       "xmdMemRealNumclient": xmdMemRealNumclient,
       "xmdMemRealMaxclient": xmdMemRealMaxclient,
       "xmdMemRealPdecay": xmdMemRealPdecay,
       "xmdMemRealSysrepag": xmdMemRealSysrepag,
       "xmdMemRealEfree": xmdMemRealEfree,
       "xmdMemRealEpinned": xmdMemRealEpinned,
       "xmdMemRealEcomp": xmdMemRealEcomp,
       "xmdMemRealEnoncomp": xmdMemRealEnoncomp,
       "xmdMemRealElocal": xmdMemRealElocal,
       "xmdMemRealEclnt": xmdMemRealEclnt,
       "xmdMemRealWseguse": xmdMemRealWseguse,
       "xmdMemRealPseguse": xmdMemRealPseguse,
       "xmdMemRealClseguse": xmdMemRealClseguse,
       "xmdMemRealWsegpin": xmdMemRealWsegpin,
       "xmdMemRealPsegpin": xmdMemRealPsegpin,
       "xmdMemRealClsegpin": xmdMemRealClsegpin,
       "xmdMemVirt": xmdMemVirt,
       "xmdMemVirtPagein": xmdMemVirtPagein,
       "xmdMemVirtPageout": xmdMemVirtPageout,
       "xmdMemVirtPgspgin": xmdMemVirtPgspgin,
       "xmdMemVirtPgspgout": xmdMemVirtPgspgout,
       "xmdMemVirtSio": xmdMemVirtSio,
       "xmdMemVirtIodone": xmdMemVirtIodone,
       "xmdMemVirtZerofill": xmdMemVirtZerofill,
       "xmdMemVirtPagexct": xmdMemVirtPagexct,
       "xmdMemVirtPgrclm": xmdMemVirtPgrclm,
       "xmdMemVirtLockexct": xmdMemVirtLockexct,
       "xmdMemVirtBacktrk": xmdMemVirtBacktrk,
       "xmdMemVirtExfill": xmdMemVirtExfill,
       "xmdMemVirtScan": xmdMemVirtScan,
       "xmdMemVirtCycle": xmdMemVirtCycle,
       "xmdMemVirtSteal": xmdMemVirtSteal,
       "xmdMemVirtFreewt": xmdMemVirtFreewt,
       "xmdMemVirtExtendwt": xmdMemVirtExtendwt,
       "xmdMemVirtPendiowt": xmdMemVirtPendiowt,
       "xmdMemVirtPfavail": xmdMemVirtPfavail,
       "xmdMemVirtWcomrepag": xmdMemVirtWcomrepag,
       "xmdMemVirtWncomrepag": xmdMemVirtWncomrepag,
       "xmdMemVirtComrepag": xmdMemVirtComrepag,
       "xmdMemVirtEcomrepag": xmdMemVirtEcomrepag,
       "xmdMemVirtNcomrepag": xmdMemVirtNcomrepag,
       "xmdMemVirtEncomrepag": xmdMemVirtEncomrepag,
       "xmdMemVirtComrepl": xmdMemVirtComrepl,
       "xmdMemVirtEcomrepl": xmdMemVirtEcomrepl,
       "xmdMemVirtNcomrepl": xmdMemVirtNcomrepl,
       "xmdMemVirtEncomrepl": xmdMemVirtEncomrepl,
       "xmdMemVirtTotpends": xmdMemVirtTotpends,
       "xmdMemVirtCompends": xmdMemVirtCompends,
       "xmdMemVirtNcompends": xmdMemVirtNcompends,
       "xmdMemVirtCltpends": xmdMemVirtCltpends,
       "xmdMemVirtNpswarn": xmdMemVirtNpswarn,
       "xmdMemVirtNpskill": xmdMemVirtNpskill,
       "xmdMemVirtMaxfree": xmdMemVirtMaxfree,
       "xmdMemVirtMinfree": xmdMemVirtMinfree,
       "xmdMemVirtMinperm": xmdMemVirtMinperm,
       "xmdMemVirtMaxpgahead": xmdMemVirtMaxpgahead,
       "xmdMemVirtMinpgahead": xmdMemVirtMinpgahead,
       "xmdMemVirtMaxpout": xmdMemVirtMaxpout,
       "xmdMemVirtMinpout": xmdMemVirtMinpout,
       "xmdMemKmem": xmdMemKmem,
       "xmdMemKmemEntry": xmdMemKmemEntry,
       "xmdMemKmemIndex": xmdMemKmemIndex,
       "xmdMemKmemInstName": xmdMemKmemInstName,
       "xmdMemKmemInuse": xmdMemKmemInuse,
       "xmdMemKmemCalls": xmdMemKmemCalls,
       "xmdMemKmemFailures": xmdMemKmemFailures,
       "xmdMemKmemMemuse": xmdMemKmemMemuse,
       "xmdMemKmemMemmax": xmdMemKmemMemmax,
       "xmdMemKmemBlocks": xmdMemKmemBlocks,
       "xmdPagSp": xmdPagSp,
       "xmdPagSpEntry": xmdPagSpEntry,
       "xmdPagSpIndex": xmdPagSpIndex,
       "xmdPagSpInstName": xmdPagSpInstName,
       "xmdPagSpSize": xmdPagSpSize,
       "xmdPagSpEfree": xmdPagSpEfree,
       "xmdPagSpIocnt": xmdPagSpIocnt,
       "xmdPagSpTotalsize": xmdPagSpTotalsize,
       "xmdPagSpTotalfree": xmdPagSpTotalfree,
       "xmdPagSpEtotalfree": xmdPagSpEtotalfree,
       "xmdPagSpEtotalused": xmdPagSpEtotalused,
       "xmdPagSpPgspgin": xmdPagSpPgspgin,
       "xmdPagSpPgspgout": xmdPagSpPgspgout,
       "xmdDisk": xmdDisk,
       "xmdDiskEntry": xmdDiskEntry,
       "xmdDiskIndex": xmdDiskIndex,
       "xmdDiskInstName": xmdDiskInstName,
       "xmdDiskBusy": xmdDiskBusy,
       "xmdDiskXfer": xmdDiskXfer,
       "xmdDiskRblk": xmdDiskRblk,
       "xmdDiskWblk": xmdDiskWblk,
       "xmdLAN": xmdLAN,
       "xmdLANEntry": xmdLANEntry,
       "xmdLANIndex": xmdLANIndex,
       "xmdLANInstName": xmdLANInstName,
       "xmdLANBytesout": xmdLANBytesout,
       "xmdLANKbytesout": xmdLANKbytesout,
       "xmdLANBytesin": xmdLANBytesin,
       "xmdLANKbytesin": xmdLANKbytesin,
       "xmdLANFramesout": xmdLANFramesout,
       "xmdLANFramesin": xmdLANFramesin,
       "xmdLANXmiterrors": xmdLANXmiterrors,
       "xmdLANRcverrors": xmdLANRcverrors,
       "xmdLANIbadpacks": xmdLANIbadpacks,
       "xmdLANXmitque": xmdLANXmitque,
       "xmdLANHighxmitq": xmdLANHighxmitq,
       "xmdLANRecvintr": xmdLANRecvintr,
       "xmdLANXmitintr": xmdLANXmitintr,
       "xmdLANXmitovfl": xmdLANXmitovfl,
       "xmdLANXmitdrops": xmdLANXmitdrops,
       "xmdLANRecvdrops": xmdLANRecvdrops,
       "xmdProc": xmdProc,
       "xmdProcEntry": xmdProcEntry,
       "xmdProcIndex": xmdProcIndex,
       "xmdProcInstName": xmdProcInstName,
       "xmdProcNice": xmdProcNice,
       "xmdProcRepage": xmdProcRepage,
       "xmdProcMajflt": xmdProcMajflt,
       "xmdProcMinflt": xmdProcMinflt,
       "xmdProcCpums": xmdProcCpums,
       "xmdProcCpuacc": xmdProcCpuacc,
       "xmdProcCpupct": xmdProcCpupct,
       "xmdProcUsercpu": xmdProcUsercpu,
       "xmdProcKerncpu": xmdProcKerncpu,
       "xmdProcWorkmem": xmdProcWorkmem,
       "xmdProcCodemem": xmdProcCodemem,
       "xmdProcPagsp": xmdProcPagsp,
       "xmdProcNsignals": xmdProcNsignals,
       "xmdProcNvcsw": xmdProcNvcsw,
       "xmdProcTsize": xmdProcTsize,
       "xmdProcMaxrss": xmdProcMaxrss,
       "xmdProcPswitch": xmdProcPswitch,
       "xmdProcRunque": xmdProcRunque,
       "xmdProcRunocc": xmdProcRunocc,
       "xmdProcSwpque": xmdProcSwpque,
       "xmdProcSwpocc": xmdProcSwpocc,
       "xmdProcKsched": xmdProcKsched,
       "xmdProcKexit": xmdProcKexit,
       "xmdSyscall": xmdSyscall,
       "xmdSyscallTotal": xmdSyscallTotal,
       "xmdSyscallRead": xmdSyscallRead,
       "xmdSyscallWrite": xmdSyscallWrite,
       "xmdSyscallFork": xmdSyscallFork,
       "xmdSyscallExec": xmdSyscallExec,
       "xmdSysIO": xmdSysIO,
       "xmdSysIOReadch": xmdSysIOReadch,
       "xmdSysIOWritech": xmdSysIOWritech,
       "xmdSysIOLbread": xmdSysIOLbread,
       "xmdSysIOLbwrite": xmdSysIOLbwrite,
       "xmdSysIOBread": xmdSysIOBread,
       "xmdSysIOBwrite": xmdSysIOBwrite,
       "xmdSysIOPhread": xmdSysIOPhread,
       "xmdSysIOPhwrite": xmdSysIOPhwrite,
       "xmdSysIOTtyraw": xmdSysIOTtyraw,
       "xmdSysIOTtycan": xmdSysIOTtycan,
       "xmdSysIOTtyout": xmdSysIOTtyout,
       "xmdSysIOReadchkb": xmdSysIOReadchkb,
       "xmdSysIOWritechkb": xmdSysIOWritechkb,
       "xmdIPC": xmdIPC,
       "xmdIPCMsg": xmdIPCMsg,
       "xmdIPCMsgMsgmax": xmdIPCMsgMsgmax,
       "xmdIPCMsgQuemax": xmdIPCMsgQuemax,
       "xmdIPCMsgQueids": xmdIPCMsgQueids,
       "xmdIPCMsgIdmax": xmdIPCMsgIdmax,
       "xmdIPCSem": xmdIPCSem,
       "xmdIPCSemSemids": xmdIPCSemSemids,
       "xmdIPCSemMaxsems": xmdIPCSemMaxsems,
       "xmdIPCSemMaxops": xmdIPCSemMaxops,
       "xmdIPCSemMaxundo": xmdIPCSemMaxundo,
       "xmdIPCSemUndosiz": xmdIPCSemUndosiz,
       "xmdIPCSemSemmaxv": xmdIPCSemSemmaxv,
       "xmdIPCSemSemmaxe": xmdIPCSemSemmaxe,
       "xmdIPCShm": xmdIPCShm,
       "xmdIPCShmShmmax": xmdIPCShmShmmax,
       "xmdIPCShmShmmin": xmdIPCShmShmmin,
       "xmdIPCShmShmids": xmdIPCShmShmids,
       "xmdIPCLocks": xmdIPCLocks,
       "xmdIPCLocksNumrecs": xmdIPCLocksNumrecs,
       "xmdIPCLocksRecsused": xmdIPCLocksRecsused,
       "xmdIPCLocksOverrun": xmdIPCLocksOverrun,
       "xmdIPCLocksRecstot": xmdIPCLocksRecstot,
       "xmdIPCLocksRecsync": xmdIPCLocksRecsync,
       "xmdFS": xmdFS,
       "xmdFSEntry": xmdFSEntry,
       "xmdFSIndex": xmdFSIndex,
       "xmdFSInstName": xmdFSInstName,
       "xmdFSFree": xmdFSFree,
       "xmdFSPpsize": xmdFSPpsize,
       "xmdFSLvcount": xmdFSLvcount,
       "xmdFSPvcount": xmdFSPvcount,
       "xmdFSIget": xmdFSIget,
       "xmdFSNamei": xmdFSNamei,
       "xmdFSDirblk": xmdFSDirblk,
       "xmdIP": xmdIP,
       "xmdIPRcvtotal": xmdIPRcvtotal,
       "xmdIPRcvfrag": xmdIPRcvfrag,
       "xmdIPForward": xmdIPForward,
       "xmdIPRcvdgrm": xmdIPRcvdgrm,
       "xmdIPSnddgrm": xmdIPSnddgrm,
       "xmdIPReasmok": xmdIPReasmok,
       "xmdIPFragok": xmdIPFragok,
       "xmdIPNetIF": xmdIPNetIF,
       "xmdIPNetIFEntry": xmdIPNetIFEntry,
       "xmdIPNetIFIndex": xmdIPNetIFIndex,
       "xmdIPNetIFInstName": xmdIPNetIFInstName,
       "xmdIPNetIFIpacket": xmdIPNetIFIpacket,
       "xmdIPNetIFIoctet": xmdIPNetIFIoctet,
       "xmdIPNetIFIoctetkb": xmdIPNetIFIoctetkb,
       "xmdIPNetIFIerror": xmdIPNetIFIerror,
       "xmdIPNetIFImcastpkt": xmdIPNetIFImcastpkt,
       "xmdIPNetIFIqdrop": xmdIPNetIFIqdrop,
       "xmdIPNetIFIunknproto": xmdIPNetIFIunknproto,
       "xmdIPNetIFOpacket": xmdIPNetIFOpacket,
       "xmdIPNetIFOoctet": xmdIPNetIFOoctet,
       "xmdIPNetIFOoctetkb": xmdIPNetIFOoctetkb,
       "xmdIPNetIFOerror": xmdIPNetIFOerror,
       "xmdIPNetIFOmcastpkt": xmdIPNetIFOmcastpkt,
       "xmdIPNetIFOquelen": xmdIPNetIFOquelen,
       "xmdIPNetIFOquemax": xmdIPNetIFOquemax,
       "xmdIPNetIFOdrops": xmdIPNetIFOdrops,
       "xmdIPRouting": xmdIPRouting,
       "xmdIPRoutingBadred": xmdIPRoutingBadred,
       "xmdIPRoutingDynamic": xmdIPRoutingDynamic,
       "xmdIPRoutingNewgate": xmdIPRoutingNewgate,
       "xmdIPRoutingUnreach": xmdIPRoutingUnreach,
       "xmdIPRoutingWildc": xmdIPRoutingWildc,
       "xmdTCP": xmdTCP,
       "xmdTCPConattmpt": xmdTCPConattmpt,
       "xmdTCPAccept": xmdTCPAccept,
       "xmdTCPConnects": xmdTCPConnects,
       "xmdTCPClose": xmdTCPClose,
       "xmdTCPSndtotal": xmdTCPSndtotal,
       "xmdTCPSndpack": xmdTCPSndpack,
       "xmdTCPSndbyte": xmdTCPSndbyte,
       "xmdTCPSndrexmitpack": xmdTCPSndrexmitpack,
       "xmdTCPSndrexmitbyte": xmdTCPSndrexmitbyte,
       "xmdTCPSndack": xmdTCPSndack,
       "xmdTCPSndprobe": xmdTCPSndprobe,
       "xmdTCPSndurg": xmdTCPSndurg,
       "xmdTCPSndwinup": xmdTCPSndwinup,
       "xmdTCPSndctrl": xmdTCPSndctrl,
       "xmdTCPRcvtotal": xmdTCPRcvtotal,
       "xmdTCPRcvpack": xmdTCPRcvpack,
       "xmdTCPRcvbyte": xmdTCPRcvbyte,
       "xmdTCPRcvduppack": xmdTCPRcvduppack,
       "xmdTCPRcvdupbyte": xmdTCPRcvdupbyte,
       "xmdTCPRcvpartduppack": xmdTCPRcvpartduppack,
       "xmdTCPRcvpartdupbyte": xmdTCPRcvpartdupbyte,
       "xmdTCPRcvoopack": xmdTCPRcvoopack,
       "xmdTCPRcvoobyte": xmdTCPRcvoobyte,
       "xmdTCPRcvaftwinpack": xmdTCPRcvaftwinpack,
       "xmdTCPRcvaftwinbyte": xmdTCPRcvaftwinbyte,
       "xmdTCPRcvwinprobe": xmdTCPRcvwinprobe,
       "xmdTCPRcvdupack": xmdTCPRcvdupack,
       "xmdTCPRcvackpack": xmdTCPRcvackpack,
       "xmdTCPRcvackbyte": xmdTCPRcvackbyte,
       "xmdTCPRcvwinup": xmdTCPRcvwinup,
       "xmdTCPSndkbyte": xmdTCPSndkbyte,
       "xmdTCPRcvkbyte": xmdTCPRcvkbyte,
       "xmdUDP": xmdUDP,
       "xmdUDPRcvdgrm": xmdUDPRcvdgrm,
       "xmdUDPNoport": xmdUDPNoport,
       "xmdUDPFullsock": xmdUDPFullsock,
       "xmdUDPSnddgrm": xmdUDPSnddgrm,
       "xmdUDPNoportbc": xmdUDPNoportbc,
       "xmdUDPHdrops": xmdUDPHdrops,
       "xmdUDPBadsum": xmdUDPBadsum,
       "xmdUDPBadlen": xmdUDPBadlen,
       "xmdUDPCachmiss": xmdUDPCachmiss,
       "xmdRTime": xmdRTime,
       "xmdRTimeLAN": xmdRTimeLAN,
       "xmdRTimeARM": xmdRTimeARM,
       "xmdRPC": xmdRPC,
       "xmdRPCClntCo": xmdRPCClntCo,
       "xmdRPCClntCoCalls": xmdRPCClntCoCalls,
       "xmdRPCClntCoBadcalls": xmdRPCClntCoBadcalls,
       "xmdRPCClntCoCantconn": xmdRPCClntCoCantconn,
       "xmdRPCClntCoBadxids": xmdRPCClntCoBadxids,
       "xmdRPCClntCoTimeouts": xmdRPCClntCoTimeouts,
       "xmdRPCClntCoNewcreds": xmdRPCClntCoNewcreds,
       "xmdRPCClntCoBadverfs": xmdRPCClntCoBadverfs,
       "xmdRPCClntCoTimers": xmdRPCClntCoTimers,
       "xmdRPCClntCoNomem": xmdRPCClntCoNomem,
       "xmdRPCClntCoInterrupts": xmdRPCClntCoInterrupts,
       "xmdRPCClntCl": xmdRPCClntCl,
       "xmdRPCClntClCalls": xmdRPCClntClCalls,
       "xmdRPCClntClBadcalls": xmdRPCClntClBadcalls,
       "xmdRPCClntClRetrans": xmdRPCClntClRetrans,
       "xmdRPCClntClBadxids": xmdRPCClntClBadxids,
       "xmdRPCClntClTimeouts": xmdRPCClntClTimeouts,
       "xmdRPCClntClNewcreds": xmdRPCClntClNewcreds,
       "xmdRPCClntClBadverfs": xmdRPCClntClBadverfs,
       "xmdRPCClntClTimers": xmdRPCClntClTimers,
       "xmdRPCClntClNomem": xmdRPCClntClNomem,
       "xmdRPCClntClCantsend": xmdRPCClntClCantsend,
       "xmdRPCSvrCo": xmdRPCSvrCo,
       "xmdRPCSvrCoCalls": xmdRPCSvrCoCalls,
       "xmdRPCSvrCoBadcalls": xmdRPCSvrCoBadcalls,
       "xmdRPCSvrCoNullrecv": xmdRPCSvrCoNullrecv,
       "xmdRPCSvrCoBadlen": xmdRPCSvrCoBadlen,
       "xmdRPCSvrCoXdrcall": xmdRPCSvrCoXdrcall,
       "xmdRPCSvrCoDupchecks": xmdRPCSvrCoDupchecks,
       "xmdRPCSvrCoDupreqs": xmdRPCSvrCoDupreqs,
       "xmdRPCSvrCl": xmdRPCSvrCl,
       "xmdRPCSvrClCalls": xmdRPCSvrClCalls,
       "xmdRPCSvrClBadcalls": xmdRPCSvrClBadcalls,
       "xmdRPCSvrClNullrecv": xmdRPCSvrClNullrecv,
       "xmdRPCSvrClBadlen": xmdRPCSvrClBadlen,
       "xmdRPCSvrClXdrcall": xmdRPCSvrClXdrcall,
       "xmdRPCSvrClDupchecks": xmdRPCSvrClDupchecks,
       "xmdRPCSvrClDupreqs": xmdRPCSvrClDupreqs,
       "xmdNFS": xmdNFS,
       "xmdNFSClient": xmdNFSClient,
       "xmdNFSClientCalls": xmdNFSClientCalls,
       "xmdNFSClientBadcalls": xmdNFSClientBadcalls,
       "xmdNFSServer": xmdNFSServer,
       "xmdNFSServerCalls": xmdNFSServerCalls,
       "xmdNFSServerBadcalls": xmdNFSServerBadcalls,
       "xmdNFSV2Clnt": xmdNFSV2Clnt,
       "xmdNFSV2ClntNull": xmdNFSV2ClntNull,
       "xmdNFSV2ClntGetattr": xmdNFSV2ClntGetattr,
       "xmdNFSV2ClntSetattr": xmdNFSV2ClntSetattr,
       "xmdNFSV2ClntRoot": xmdNFSV2ClntRoot,
       "xmdNFSV2ClntLookup": xmdNFSV2ClntLookup,
       "xmdNFSV2ClntReadlink": xmdNFSV2ClntReadlink,
       "xmdNFSV2ClntRead": xmdNFSV2ClntRead,
       "xmdNFSV2ClntWrcache": xmdNFSV2ClntWrcache,
       "xmdNFSV2ClntWrite": xmdNFSV2ClntWrite,
       "xmdNFSV2ClntCreate": xmdNFSV2ClntCreate,
       "xmdNFSV2ClntRemove": xmdNFSV2ClntRemove,
       "xmdNFSV2ClntRename": xmdNFSV2ClntRename,
       "xmdNFSV2ClntLink": xmdNFSV2ClntLink,
       "xmdNFSV2ClntSymlink": xmdNFSV2ClntSymlink,
       "xmdNFSV2ClntMkdir": xmdNFSV2ClntMkdir,
       "xmdNFSV2ClntRmdir": xmdNFSV2ClntRmdir,
       "xmdNFSV2ClntReaddir": xmdNFSV2ClntReaddir,
       "xmdNFSV2ClntStatfs": xmdNFSV2ClntStatfs,
       "xmdNFSV2Svr": xmdNFSV2Svr,
       "xmdNFSV2SvrNull": xmdNFSV2SvrNull,
       "xmdNFSV2SvrGetattr": xmdNFSV2SvrGetattr,
       "xmdNFSV2SvrSetattr": xmdNFSV2SvrSetattr,
       "xmdNFSV2SvrRoot": xmdNFSV2SvrRoot,
       "xmdNFSV2SvrLookup": xmdNFSV2SvrLookup,
       "xmdNFSV2SvrReadlink": xmdNFSV2SvrReadlink,
       "xmdNFSV2SvrRead": xmdNFSV2SvrRead,
       "xmdNFSV2SvrWrcache": xmdNFSV2SvrWrcache,
       "xmdNFSV2SvrWrite": xmdNFSV2SvrWrite,
       "xmdNFSV2SvrCreate": xmdNFSV2SvrCreate,
       "xmdNFSV2SvrRemove": xmdNFSV2SvrRemove,
       "xmdNFSV2SvrRename": xmdNFSV2SvrRename,
       "xmdNFSV2SvrLink": xmdNFSV2SvrLink,
       "xmdNFSV2SvrSymlink": xmdNFSV2SvrSymlink,
       "xmdNFSV2SvrMkdir": xmdNFSV2SvrMkdir,
       "xmdNFSV2SvrRmdir": xmdNFSV2SvrRmdir,
       "xmdNFSV2SvrReaddir": xmdNFSV2SvrReaddir,
       "xmdNFSV2SvrStatfs": xmdNFSV2SvrStatfs,
       "xmdNFSV3Clnt": xmdNFSV3Clnt,
       "xmdNFSV3ClntNull": xmdNFSV3ClntNull,
       "xmdNFSV3ClntGetattr": xmdNFSV3ClntGetattr,
       "xmdNFSV3ClntSetattr": xmdNFSV3ClntSetattr,
       "xmdNFSV3ClntLookup": xmdNFSV3ClntLookup,
       "xmdNFSV3ClntAccess": xmdNFSV3ClntAccess,
       "xmdNFSV3ClntReadlink": xmdNFSV3ClntReadlink,
       "xmdNFSV3ClntRead": xmdNFSV3ClntRead,
       "xmdNFSV3ClntWrite": xmdNFSV3ClntWrite,
       "xmdNFSV3ClntCreate": xmdNFSV3ClntCreate,
       "xmdNFSV3ClntSymlink": xmdNFSV3ClntSymlink,
       "xmdNFSV3ClntMknod": xmdNFSV3ClntMknod,
       "xmdNFSV3ClntRemove": xmdNFSV3ClntRemove,
       "xmdNFSV3ClntRmdir": xmdNFSV3ClntRmdir,
       "xmdNFSV3ClntMkdir": xmdNFSV3ClntMkdir,
       "xmdNFSV3ClntRename": xmdNFSV3ClntRename,
       "xmdNFSV3ClntLink": xmdNFSV3ClntLink,
       "xmdNFSV3ClntReaddir": xmdNFSV3ClntReaddir,
       "xmdNFSV3ClntReaddir-plus": xmdNFSV3ClntReaddir_plus,
       "xmdNFSV3ClntFsstat": xmdNFSV3ClntFsstat,
       "xmdNFSV3ClntFsinfo": xmdNFSV3ClntFsinfo,
       "xmdNFSV3ClntPathconf": xmdNFSV3ClntPathconf,
       "xmdNFSV3ClntCommit": xmdNFSV3ClntCommit,
       "xmdNFSV3Svr": xmdNFSV3Svr,
       "xmdNFSV3SvrNull": xmdNFSV3SvrNull,
       "xmdNFSV3SvrGetattr": xmdNFSV3SvrGetattr,
       "xmdNFSV3SvrSetattr": xmdNFSV3SvrSetattr,
       "xmdNFSV3SvrLookup": xmdNFSV3SvrLookup,
       "xmdNFSV3SvrAccess": xmdNFSV3SvrAccess,
       "xmdNFSV3SvrReadlink": xmdNFSV3SvrReadlink,
       "xmdNFSV3SvrRead": xmdNFSV3SvrRead,
       "xmdNFSV3SvrWrite": xmdNFSV3SvrWrite,
       "xmdNFSV3SvrCreate": xmdNFSV3SvrCreate,
       "xmdNFSV3SvrMkdir": xmdNFSV3SvrMkdir,
       "xmdNFSV3SvrSymlink": xmdNFSV3SvrSymlink,
       "xmdNFSV3SvrMknod": xmdNFSV3SvrMknod,
       "xmdNFSV3SvrRemove": xmdNFSV3SvrRemove,
       "xmdNFSV3SvrRmdir": xmdNFSV3SvrRmdir,
       "xmdNFSV3SvrRename": xmdNFSV3SvrRename,
       "xmdNFSV3SvrLink": xmdNFSV3SvrLink,
       "xmdNFSV3SvrReaddir": xmdNFSV3SvrReaddir,
       "xmdNFSV3SvrReaddir-plus": xmdNFSV3SvrReaddir_plus,
       "xmdNFSV3SvrFsstat": xmdNFSV3SvrFsstat,
       "xmdNFSV3SvrFsinfo": xmdNFSV3SvrFsinfo,
       "xmdNFSV3SvrPathconf": xmdNFSV3SvrPathconf,
       "xmdNFSV3SvrCommit": xmdNFSV3SvrCommit,
       "xmdDCE": xmdDCE,
       "xmdSpmi": xmdSpmi,
       "xmdSpmiUsers": xmdSpmiUsers,
       "xmdSpmiStatsets": xmdSpmiStatsets,
       "xmdSpmiDdscount": xmdSpmiDdscount,
       "xmdSpmiConsumers": xmdSpmiConsumers,
       "xmdSpmiComused": xmdSpmiComused,
       "xmdSpmiHotsets": xmdSpmiHotsets,
       "xmdDDS": xmdDDS,
       "risc6000public": risc6000public,
       "aix370": aix370,
       "aixPS2": aixPS2,
       "mvs": mvs,
       "mvs370": mvs370,
       "vm": vm,
       "vm370": vm370,
       "os2": os2,
       "ps2PS2": ps2PS2,
       "os400": os400,
       "os400as400": os400as400}
)
