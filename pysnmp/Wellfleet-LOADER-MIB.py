# SNMP MIB module (Wellfleet-LOADER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-LOADER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:37 2024
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

(wfSoftwareConfig,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfSoftwareConfig")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfProtocols_ObjectIdentity = ObjectIdentity
wfProtocols = _WfProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1)
)
_WfIPROTOLoad_Type = Counter32
_WfIPROTOLoad_Object = MibScalar
wfIPROTOLoad = _WfIPROTOLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 1),
    _WfIPROTOLoad_Type()
)
wfIPROTOLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIPROTOLoad.setStatus("mandatory")
_WfDECNETLoad_Type = Counter32
_WfDECNETLoad_Object = MibScalar
wfDECNETLoad = _WfDECNETLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 2),
    _WfDECNETLoad_Type()
)
wfDECNETLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDECNETLoad.setStatus("mandatory")
_WfATLoad_Type = Counter32
_WfATLoad_Object = MibScalar
wfATLoad = _WfATLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 3),
    _WfATLoad_Type()
)
wfATLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfATLoad.setStatus("mandatory")
_WfXNSLoad_Type = Counter32
_WfXNSLoad_Object = MibScalar
wfXNSLoad = _WfXNSLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 4),
    _WfXNSLoad_Type()
)
wfXNSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfXNSLoad.setStatus("mandatory")
_WfIPXLoad_Type = Counter32
_WfIPXLoad_Object = MibScalar
wfIPXLoad = _WfIPXLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 5),
    _WfIPXLoad_Type()
)
wfIPXLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIPXLoad.setStatus("mandatory")
_WfOSILoad_Type = Counter32
_WfOSILoad_Object = MibScalar
wfOSILoad = _WfOSILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 6),
    _WfOSILoad_Type()
)
wfOSILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOSILoad.setStatus("mandatory")
_WfX25DTELoad_Type = Counter32
_WfX25DTELoad_Object = MibScalar
wfX25DTELoad = _WfX25DTELoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 7),
    _WfX25DTELoad_Type()
)
wfX25DTELoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25DTELoad.setStatus("mandatory")
_WfX25DCELoad_Type = Counter32
_WfX25DCELoad_Object = MibScalar
wfX25DCELoad = _WfX25DCELoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 8),
    _WfX25DCELoad_Type()
)
wfX25DCELoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25DCELoad.setStatus("mandatory")
_WfVINESLoad_Type = Counter32
_WfVINESLoad_Object = MibScalar
wfVINESLoad = _WfVINESLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 9),
    _WfVINESLoad_Type()
)
wfVINESLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVINESLoad.setStatus("mandatory")
_WfFRLoad_Type = Counter32
_WfFRLoad_Object = MibScalar
wfFRLoad = _WfFRLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 10),
    _WfFRLoad_Type()
)
wfFRLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFRLoad.setStatus("mandatory")
_WfRARPLoad_Type = Counter32
_WfRARPLoad_Object = MibScalar
wfRARPLoad = _WfRARPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 11),
    _WfRARPLoad_Type()
)
wfRARPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRARPLoad.setStatus("mandatory")
_WfATMLoad_Type = Counter32
_WfATMLoad_Object = MibScalar
wfATMLoad = _WfATMLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 12),
    _WfATMLoad_Type()
)
wfATMLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfATMLoad.setStatus("mandatory")
_WfDLSLoad_Type = Counter32
_WfDLSLoad_Object = MibScalar
wfDLSLoad = _WfDLSLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 13),
    _WfDLSLoad_Type()
)
wfDLSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDLSLoad.setStatus("mandatory")
_WfLNMLoad_Type = Counter32
_WfLNMLoad_Object = MibScalar
wfLNMLoad = _WfLNMLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 14),
    _WfLNMLoad_Type()
)
wfLNMLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLNMLoad.setStatus("mandatory")
_WfTelnetLoad_Type = Counter32
_WfTelnetLoad_Object = MibScalar
wfTelnetLoad = _WfTelnetLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 15),
    _WfTelnetLoad_Type()
)
wfTelnetLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetLoad.setStatus("mandatory")
_WfTFTPLoad_Type = Counter32
_WfTFTPLoad_Object = MibScalar
wfTFTPLoad = _WfTFTPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 16),
    _WfTFTPLoad_Type()
)
wfTFTPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTFTPLoad.setStatus("mandatory")
_WfSNMPLoad_Type = Counter32
_WfSNMPLoad_Object = MibScalar
wfSNMPLoad = _WfSNMPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 17),
    _WfSNMPLoad_Type()
)
wfSNMPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSNMPLoad.setStatus("mandatory")
_WfTCPLoad_Type = Counter32
_WfTCPLoad_Object = MibScalar
wfTCPLoad = _WfTCPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 18),
    _WfTCPLoad_Type()
)
wfTCPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTCPLoad.setStatus("mandatory")
_WfBGPLoad_Type = Counter32
_WfBGPLoad_Object = MibScalar
wfBGPLoad = _WfBGPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 19),
    _WfBGPLoad_Type()
)
wfBGPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBGPLoad.setStatus("mandatory")
_WfEGPLoad_Type = Counter32
_WfEGPLoad_Object = MibScalar
wfEGPLoad = _WfEGPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 20),
    _WfEGPLoad_Type()
)
wfEGPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfEGPLoad.setStatus("mandatory")
_WfOSPFLoad_Type = Counter32
_WfOSPFLoad_Object = MibScalar
wfOSPFLoad = _WfOSPFLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 21),
    _WfOSPFLoad_Type()
)
wfOSPFLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOSPFLoad.setStatus("mandatory")
_WfWPROXYLoad_Type = Counter32
_WfWPROXYLoad_Object = MibScalar
wfWPROXYLoad = _WfWPROXYLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 22),
    _WfWPROXYLoad_Type()
)
wfWPROXYLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWPROXYLoad.setStatus("mandatory")
_WfLLC2Load_Type = Counter32
_WfLLC2Load_Object = MibScalar
wfLLC2Load = _WfLLC2Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 23),
    _WfLLC2Load_Type()
)
wfLLC2Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLLC2Load.setStatus("mandatory")
_WfSMDSLoad_Type = Counter32
_WfSMDSLoad_Object = MibScalar
wfSMDSLoad = _WfSMDSLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 24),
    _WfSMDSLoad_Type()
)
wfSMDSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSMDSLoad.setStatus("mandatory")
_WfPPPLoad_Type = Counter32
_WfPPPLoad_Object = MibScalar
wfPPPLoad = _WfPPPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 25),
    _WfPPPLoad_Type()
)
wfPPPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPPPLoad.setStatus("mandatory")
_WfPktCaptureLoad_Type = Counter32
_WfPktCaptureLoad_Object = MibScalar
wfPktCaptureLoad = _WfPktCaptureLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 26),
    _WfPktCaptureLoad_Type()
)
wfPktCaptureLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureLoad.setStatus("mandatory")
_WfFRSWCNGCLoad_Type = Counter32
_WfFRSWCNGCLoad_Object = MibScalar
wfFRSWCNGCLoad = _WfFRSWCNGCLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 27),
    _WfFRSWCNGCLoad_Type()
)
wfFRSWCNGCLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFRSWCNGCLoad.setStatus("mandatory")
_WfSWPROXYLoad_Type = Counter32
_WfSWPROXYLoad_Object = MibScalar
wfSWPROXYLoad = _WfSWPROXYLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 28),
    _WfSWPROXYLoad_Type()
)
wfSWPROXYLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSWPROXYLoad.setStatus("mandatory")
_WfFRSWLoad_Type = Counter32
_WfFRSWLoad_Object = MibScalar
wfFRSWLoad = _WfFRSWLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 29),
    _WfFRSWLoad_Type()
)
wfFRSWLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFRSWLoad.setStatus("mandatory")
_WfSWSMDSLoad_Type = Counter32
_WfSWSMDSLoad_Object = MibScalar
wfSWSMDSLoad = _WfSWSMDSLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 30),
    _WfSWSMDSLoad_Type()
)
wfSWSMDSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSWSMDSLoad.setStatus("mandatory")
_WfNBASELoad_Type = Counter32
_WfNBASELoad_Object = MibScalar
wfNBASELoad = _WfNBASELoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 31),
    _WfNBASELoad_Type()
)
wfNBASELoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNBASELoad.setStatus("mandatory")
_WfSDLCLoad_Type = Counter32
_WfSDLCLoad_Object = MibScalar
wfSDLCLoad = _WfSDLCLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 32),
    _WfSDLCLoad_Type()
)
wfSDLCLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSDLCLoad.setStatus("mandatory")
_WfTNCLoad_Type = Counter32
_WfTNCLoad_Object = MibScalar
wfTNCLoad = _WfTNCLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 33),
    _WfTNCLoad_Type()
)
wfTNCLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTNCLoad.setStatus("mandatory")
_WfLAPBLoad_Type = Counter32
_WfLAPBLoad_Object = MibScalar
wfLAPBLoad = _WfLAPBLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 34),
    _WfLAPBLoad_Type()
)
wfLAPBLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLAPBLoad.setStatus("mandatory")
_WfDebugLoad_Type = Counter32
_WfDebugLoad_Object = MibScalar
wfDebugLoad = _WfDebugLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 35),
    _WfDebugLoad_Type()
)
wfDebugLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDebugLoad.setStatus("mandatory")
_WfNBIPLoad_Type = Counter32
_WfNBIPLoad_Object = MibScalar
wfNBIPLoad = _WfNBIPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 36),
    _WfNBIPLoad_Type()
)
wfNBIPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNBIPLoad.setStatus("mandatory")
_WfATMCsLoad_Type = Counter32
_WfATMCsLoad_Object = MibScalar
wfATMCsLoad = _WfATMCsLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 37),
    _WfATMCsLoad_Type()
)
wfATMCsLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfATMCsLoad.setStatus("mandatory")
_WfDvmrpLoad_Type = Counter32
_WfDvmrpLoad_Object = MibScalar
wfDvmrpLoad = _WfDvmrpLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 38),
    _WfDvmrpLoad_Type()
)
wfDvmrpLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpLoad.setStatus("mandatory")
_WfIgmpLoad_Type = Counter32
_WfIgmpLoad_Object = MibScalar
wfIgmpLoad = _WfIgmpLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 39),
    _WfIgmpLoad_Type()
)
wfIgmpLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIgmpLoad.setStatus("mandatory")
_WfISDNLoad_Type = Counter32
_WfISDNLoad_Object = MibScalar
wfISDNLoad = _WfISDNLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 40),
    _WfISDNLoad_Type()
)
wfISDNLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfISDNLoad.setStatus("mandatory")
_WfLMLoad_Type = Counter32
_WfLMLoad_Object = MibScalar
wfLMLoad = _WfLMLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 41),
    _WfLMLoad_Type()
)
wfLMLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLMLoad.setStatus("mandatory")
_WfPingLoad_Type = Counter32
_WfPingLoad_Object = MibScalar
wfPingLoad = _WfPingLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 42),
    _WfPingLoad_Type()
)
wfPingLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingLoad.setStatus("mandatory")
_WfAPPNCpLoad_Type = Counter32
_WfAPPNCpLoad_Object = MibScalar
wfAPPNCpLoad = _WfAPPNCpLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 43),
    _WfAPPNCpLoad_Type()
)
wfAPPNCpLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAPPNCpLoad.setStatus("mandatory")
_WfAPPNLsLoad_Type = Counter32
_WfAPPNLsLoad_Object = MibScalar
wfAPPNLsLoad = _WfAPPNLsLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 44),
    _WfAPPNLsLoad_Type()
)
wfAPPNLsLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAPPNLsLoad.setStatus("mandatory")
_WfWcpLoad_Type = Counter32
_WfWcpLoad_Object = MibScalar
wfWcpLoad = _WfWcpLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 45),
    _WfWcpLoad_Type()
)
wfWcpLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpLoad.setStatus("mandatory")
_WfFTPLoad_Type = Counter32
_WfFTPLoad_Object = MibScalar
wfFTPLoad = _WfFTPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 46),
    _WfFTPLoad_Type()
)
wfFTPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFTPLoad.setStatus("mandatory")
_WfARPLoad_Type = Counter32
_WfARPLoad_Object = MibScalar
wfARPLoad = _WfARPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 47),
    _WfARPLoad_Type()
)
wfARPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfARPLoad.setStatus("mandatory")
_WfSYSLLoad_Type = Counter32
_WfSYSLLoad_Object = MibScalar
wfSYSLLoad = _WfSYSLLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 48),
    _WfSYSLLoad_Type()
)
wfSYSLLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSYSLLoad.setStatus("mandatory")
_WfBGPRSLoad_Type = Counter32
_WfBGPRSLoad_Object = MibScalar
wfBGPRSLoad = _WfBGPRSLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 49),
    _WfBGPRSLoad_Type()
)
wfBGPRSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBGPRSLoad.setStatus("mandatory")
_WfATMLeLoad_Type = Counter32
_WfATMLeLoad_Object = MibScalar
wfATMLeLoad = _WfATMLeLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 50),
    _WfATMLeLoad_Type()
)
wfATMLeLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfATMLeLoad.setStatus("mandatory")
_WfCRMLoad_Type = Counter32
_WfCRMLoad_Object = MibScalar
wfCRMLoad = _WfCRMLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 51),
    _WfCRMLoad_Type()
)
wfCRMLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCRMLoad.setStatus("mandatory")
_WfIPEXLoad_Type = Counter32
_WfIPEXLoad_Object = MibScalar
wfIPEXLoad = _WfIPEXLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 52),
    _WfIPEXLoad_Type()
)
wfIPEXLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIPEXLoad.setStatus("mandatory")
_WfSt2Load_Type = Counter32
_WfSt2Load_Object = MibScalar
wfSt2Load = _WfSt2Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 53),
    _WfSt2Load_Type()
)
wfSt2Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2Load.setStatus("mandatory")
_WfNLSPLoad_Type = Counter32
_WfNLSPLoad_Object = MibScalar
wfNLSPLoad = _WfNLSPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 54),
    _WfNLSPLoad_Type()
)
wfNLSPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNLSPLoad.setStatus("mandatory")
_WfSTATSLoad_Type = Counter32
_WfSTATSLoad_Object = MibScalar
wfSTATSLoad = _WfSTATSLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 55),
    _WfSTATSLoad_Type()
)
wfSTATSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSTATSLoad.setStatus("mandatory")
_WfNPTLoad_Type = Counter32
_WfNPTLoad_Object = MibScalar
wfNPTLoad = _WfNPTLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 56),
    _WfNPTLoad_Type()
)
wfNPTLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNPTLoad.setStatus("mandatory")
_WfRREDUNDLoad_Type = Counter32
_WfRREDUNDLoad_Object = MibScalar
wfRREDUNDLoad = _WfRREDUNDLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 57),
    _WfRREDUNDLoad_Type()
)
wfRREDUNDLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRREDUNDLoad.setStatus("mandatory")
_WfATMSigLoad_Type = Counter32
_WfATMSigLoad_Object = MibScalar
wfATMSigLoad = _WfATMSigLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 58),
    _WfATMSigLoad_Type()
)
wfATMSigLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfATMSigLoad.setStatus("mandatory")
_WfIPv6Load_Type = Counter32
_WfIPv6Load_Object = MibScalar
wfIPv6Load = _WfIPv6Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 59),
    _WfIPv6Load_Type()
)
wfIPv6Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIPv6Load.setStatus("mandatory")
_WfBOTLoad_Type = Counter32
_WfBOTLoad_Object = MibScalar
wfBOTLoad = _WfBOTLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 60),
    _WfBOTLoad_Type()
)
wfBOTLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBOTLoad.setStatus("mandatory")
_WfPimLoad_Type = Counter32
_WfPimLoad_Object = MibScalar
wfPimLoad = _WfPimLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 61),
    _WfPimLoad_Type()
)
wfPimLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPimLoad.setStatus("mandatory")
_WfLBCLoad_Type = Counter32
_WfLBCLoad_Object = MibScalar
wfLBCLoad = _WfLBCLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 62),
    _WfLBCLoad_Type()
)
wfLBCLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLBCLoad.setStatus("mandatory")
_WfATMMcsLoad_Type = Counter32
_WfATMMcsLoad_Object = MibScalar
wfATMMcsLoad = _WfATMMcsLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 63),
    _WfATMMcsLoad_Type()
)
wfATMMcsLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfATMMcsLoad.setStatus("mandatory")
_WfATMAsmLoad_Type = Counter32
_WfATMAsmLoad_Object = MibScalar
wfATMAsmLoad = _WfATMAsmLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 64),
    _WfATMAsmLoad_Type()
)
wfATMAsmLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfATMAsmLoad.setStatus("mandatory")
_WfCPMLoad_Type = Counter32
_WfCPMLoad_Object = MibScalar
wfCPMLoad = _WfCPMLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 65),
    _WfCPMLoad_Type()
)
wfCPMLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCPMLoad.setStatus("mandatory")
_WfBAYSIGLoad_Type = Counter32
_WfBAYSIGLoad_Object = MibScalar
wfBAYSIGLoad = _WfBAYSIGLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 66),
    _WfBAYSIGLoad_Type()
)
wfBAYSIGLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBAYSIGLoad.setStatus("mandatory")
_WfScmIpcLoad_Type = Counter32
_WfScmIpcLoad_Object = MibScalar
wfScmIpcLoad = _WfScmIpcLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 67),
    _WfScmIpcLoad_Type()
)
wfScmIpcLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfScmIpcLoad.setStatus("mandatory")
_WfNTPLoad_Type = Counter32
_WfNTPLoad_Object = MibScalar
wfNTPLoad = _WfNTPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 68),
    _WfNTPLoad_Type()
)
wfNTPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNTPLoad.setStatus("mandatory")
_WfRADIUSLoad_Type = Counter32
_WfRADIUSLoad_Object = MibScalar
wfRADIUSLoad = _WfRADIUSLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 69),
    _WfRADIUSLoad_Type()
)
wfRADIUSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRADIUSLoad.setStatus("mandatory")
_WfRCMDSLoad_Type = Counter32
_WfRCMDSLoad_Object = MibScalar
wfRCMDSLoad = _WfRCMDSLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 70),
    _WfRCMDSLoad_Type()
)
wfRCMDSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRCMDSLoad.setStatus("mandatory")
_WfDNSLoad_Type = Counter32
_WfDNSLoad_Object = MibScalar
wfDNSLoad = _WfDNSLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 71),
    _WfDNSLoad_Type()
)
wfDNSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDNSLoad.setStatus("mandatory")
_WfWepLoad_Type = Counter32
_WfWepLoad_Object = MibScalar
wfWepLoad = _WfWepLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 72),
    _WfWepLoad_Type()
)
wfWepLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWepLoad.setStatus("mandatory")
_WfRipv6Load_Type = Counter32
_WfRipv6Load_Object = MibScalar
wfRipv6Load = _WfRipv6Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 73),
    _WfRipv6Load_Type()
)
wfRipv6Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6Load.setStatus("mandatory")
_WfMOSPFLoad_Type = Counter32
_WfMOSPFLoad_Object = MibScalar
wfMOSPFLoad = _WfMOSPFLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 74),
    _WfMOSPFLoad_Type()
)
wfMOSPFLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMOSPFLoad.setStatus("mandatory")
_WfRSVPLoad_Type = Counter32
_WfRSVPLoad_Object = MibScalar
wfRSVPLoad = _WfRSVPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 75),
    _WfRSVPLoad_Type()
)
wfRSVPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRSVPLoad.setStatus("mandatory")
_WfIpSwitchLoad_Type = Counter32
_WfIpSwitchLoad_Object = MibScalar
wfIpSwitchLoad = _WfIpSwitchLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 76),
    _WfIpSwitchLoad_Type()
)
wfIpSwitchLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSwitchLoad.setStatus("mandatory")
_WfPortMtxLoad_Type = Counter32
_WfPortMtxLoad_Object = MibScalar
wfPortMtxLoad = _WfPortMtxLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 77),
    _WfPortMtxLoad_Type()
)
wfPortMtxLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPortMtxLoad.setStatus("mandatory")
_WfConvStrLoad_Type = Counter32
_WfConvStrLoad_Object = MibScalar
wfConvStrLoad = _WfConvStrLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 78),
    _WfConvStrLoad_Type()
)
wfConvStrLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfConvStrLoad.setStatus("mandatory")
_WfS5ChasLoad_Type = Counter32
_WfS5ChasLoad_Object = MibScalar
wfS5ChasLoad = _WfS5ChasLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 79),
    _WfS5ChasLoad_Type()
)
wfS5ChasLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfS5ChasLoad.setStatus("mandatory")
_WfFRSVCLoad_Type = Counter32
_WfFRSVCLoad_Object = MibScalar
wfFRSVCLoad = _WfFRSVCLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 80),
    _WfFRSVCLoad_Type()
)
wfFRSVCLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFRSVCLoad.setStatus("mandatory")
_WfAOTLoad_Type = Counter32
_WfAOTLoad_Object = MibScalar
wfAOTLoad = _WfAOTLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 81),
    _WfAOTLoad_Type()
)
wfAOTLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAOTLoad.setStatus("mandatory")
_WfNATLoad_Type = Counter32
_WfNATLoad_Object = MibScalar
wfNATLoad = _WfNATLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 82),
    _WfNATLoad_Type()
)
wfNATLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNATLoad.setStatus("mandatory")
_WfFRPTLoad_Type = Counter32
_WfFRPTLoad_Object = MibScalar
wfFRPTLoad = _WfFRPTLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 83),
    _WfFRPTLoad_Type()
)
wfFRPTLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFRPTLoad.setStatus("mandatory")
_WfHttpSrvLoad_Type = Counter32
_WfHttpSrvLoad_Object = MibScalar
wfHttpSrvLoad = _WfHttpSrvLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 84),
    _WfHttpSrvLoad_Type()
)
wfHttpSrvLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHttpSrvLoad.setStatus("mandatory")
_WfStacLZSLoad_Type = Counter32
_WfStacLZSLoad_Object = MibScalar
wfStacLZSLoad = _WfStacLZSLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 85),
    _WfStacLZSLoad_Type()
)
wfStacLZSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStacLZSLoad.setStatus("mandatory")
_WfASRLoad_Type = Counter32
_WfASRLoad_Object = MibScalar
wfASRLoad = _WfASRLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 86),
    _WfASRLoad_Type()
)
wfASRLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfASRLoad.setStatus("mandatory")
_WfNHRPLoad_Type = Counter32
_WfNHRPLoad_Object = MibScalar
wfNHRPLoad = _WfNHRPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 87),
    _WfNHRPLoad_Type()
)
wfNHRPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNHRPLoad.setStatus("mandatory")
_WfAHBLoad_Type = Counter32
_WfAHBLoad_Object = MibScalar
wfAHBLoad = _WfAHBLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 88),
    _WfAHBLoad_Type()
)
wfAHBLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAHBLoad.setStatus("mandatory")
_WfL2TPLoad_Type = Counter32
_WfL2TPLoad_Object = MibScalar
wfL2TPLoad = _WfL2TPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 89),
    _WfL2TPLoad_Type()
)
wfL2TPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPLoad.setStatus("mandatory")
_WfISDBLoad_Type = Counter32
_WfISDBLoad_Object = MibScalar
wfISDBLoad = _WfISDBLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 90),
    _WfISDBLoad_Type()
)
wfISDBLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfISDBLoad.setStatus("mandatory")
_WfVCCTLoad_Type = Counter32
_WfVCCTLoad_Object = MibScalar
wfVCCTLoad = _WfVCCTLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 91),
    _WfVCCTLoad_Type()
)
wfVCCTLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVCCTLoad.setStatus("mandatory")
_WfMpsLoad_Type = Counter32
_WfMpsLoad_Object = MibScalar
wfMpsLoad = _WfMpsLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 92),
    _WfMpsLoad_Type()
)
wfMpsLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMpsLoad.setStatus("mandatory")
_WfTAG1QLoad_Type = Counter32
_WfTAG1QLoad_Object = MibScalar
wfTAG1QLoad = _WfTAG1QLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 93),
    _WfTAG1QLoad_Type()
)
wfTAG1QLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTAG1QLoad.setStatus("mandatory")
_WfMpcLoad_Type = Counter32
_WfMpcLoad_Object = MibScalar
wfMpcLoad = _WfMpcLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 94),
    _WfMpcLoad_Type()
)
wfMpcLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMpcLoad.setStatus("mandatory")
_WfDVSLoad_Type = Counter32
_WfDVSLoad_Object = MibScalar
wfDVSLoad = _WfDVSLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 95),
    _WfDVSLoad_Type()
)
wfDVSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDVSLoad.setStatus("mandatory")
_WfVRRPLoad_Type = Counter32
_WfVRRPLoad_Object = MibScalar
wfVRRPLoad = _WfVRRPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 96),
    _WfVRRPLoad_Type()
)
wfVRRPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVRRPLoad.setStatus("mandatory")
_WfDHCPLoad_Type = Counter32
_WfDHCPLoad_Object = MibScalar
wfDHCPLoad = _WfDHCPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 97),
    _WfDHCPLoad_Type()
)
wfDHCPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDHCPLoad.setStatus("mandatory")
_WfCAPILoad_Type = Counter32
_WfCAPILoad_Object = MibScalar
wfCAPILoad = _WfCAPILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 98),
    _WfCAPILoad_Type()
)
wfCAPILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCAPILoad.setStatus("mandatory")
_WfIPSECLoad_Type = Counter32
_WfIPSECLoad_Object = MibScalar
wfIPSECLoad = _WfIPSECLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 99),
    _WfIPSECLoad_Type()
)
wfIPSECLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIPSECLoad.setStatus("mandatory")
_WfMplsLdpLoad_Type = Counter32
_WfMplsLdpLoad_Object = MibScalar
wfMplsLdpLoad = _WfMplsLdpLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 100),
    _WfMplsLdpLoad_Type()
)
wfMplsLdpLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpLoad.setStatus("mandatory")
_WfMplsMlmLoad_Type = Counter32
_WfMplsMlmLoad_Object = MibScalar
wfMplsMlmLoad = _WfMplsMlmLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 101),
    _WfMplsMlmLoad_Type()
)
wfMplsMlmLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsMlmLoad.setStatus("mandatory")
_WfBacPktGenLoad_Type = Counter32
_WfBacPktGenLoad_Object = MibScalar
wfBacPktGenLoad = _WfBacPktGenLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 102),
    _WfBacPktGenLoad_Type()
)
wfBacPktGenLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenLoad.setStatus("mandatory")
_WfIISISLoad_Type = Counter32
_WfIISISLoad_Object = MibScalar
wfIISISLoad = _WfIISISLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 103),
    _WfIISISLoad_Type()
)
wfIISISLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIISISLoad.setStatus("mandatory")
_WfCopsCLoad_Type = Counter32
_WfCopsCLoad_Object = MibScalar
wfCopsCLoad = _WfCopsCLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 104),
    _WfCopsCLoad_Type()
)
wfCopsCLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsCLoad.setStatus("mandatory")
_WfDiffServLoad_Type = Counter32
_WfDiffServLoad_Object = MibScalar
wfDiffServLoad = _WfDiffServLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 105),
    _WfDiffServLoad_Type()
)
wfDiffServLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDiffServLoad.setStatus("mandatory")
_WfIKELoad_Type = Counter32
_WfIKELoad_Object = MibScalar
wfIKELoad = _WfIKELoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 106),
    _WfIKELoad_Type()
)
wfIKELoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIKELoad.setStatus("mandatory")
_WfDsqmsProxyLoad_Type = Counter32
_WfDsqmsProxyLoad_Object = MibScalar
wfDsqmsProxyLoad = _WfDsqmsProxyLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 107),
    _WfDsqmsProxyLoad_Type()
)
wfDsqmsProxyLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsqmsProxyLoad.setStatus("mandatory")
_WfLinkModules_ObjectIdentity = ObjectIdentity
wfLinkModules = _WfLinkModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2)
)
_WfENETIILoad_Type = Counter32
_WfENETIILoad_Object = MibScalar
wfENETIILoad = _WfENETIILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 1),
    _WfENETIILoad_Type()
)
wfENETIILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfENETIILoad.setStatus("mandatory")
_WfQENETLoad_Type = Counter32
_WfQENETLoad_Object = MibScalar
wfQENETLoad = _WfQENETLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 2),
    _WfQENETLoad_Type()
)
wfQENETLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQENETLoad.setStatus("mandatory")
_WfFDDILoad_Type = Counter32
_WfFDDILoad_Object = MibScalar
wfFDDILoad = _WfFDDILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 3),
    _WfFDDILoad_Type()
)
wfFDDILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDILoad.setStatus("mandatory")
_WfDSDELoad_Type = Counter32
_WfDSDELoad_Object = MibScalar
wfDSDELoad = _WfDSDELoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 4),
    _WfDSDELoad_Type()
)
wfDSDELoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDSDELoad.setStatus("mandatory")
_WfDSDEIILoad_Type = Counter32
_WfDSDEIILoad_Object = MibScalar
wfDSDEIILoad = _WfDSDEIILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 5),
    _WfDSDEIILoad_Type()
)
wfDSDEIILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDSDEIILoad.setStatus("mandatory")
_WfQSYNCLoad_Type = Counter32
_WfQSYNCLoad_Object = MibScalar
wfQSYNCLoad = _WfQSYNCLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 6),
    _WfQSYNCLoad_Type()
)
wfQSYNCLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQSYNCLoad.setStatus("mandatory")
_WfDTLoad_Type = Counter32
_WfDTLoad_Object = MibScalar
wfDTLoad = _WfDTLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 7),
    _WfDTLoad_Type()
)
wfDTLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDTLoad.setStatus("mandatory")
_WfDSTLoad_Type = Counter32
_WfDSTLoad_Object = MibScalar
wfDSTLoad = _WfDSTLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 8),
    _WfDSTLoad_Type()
)
wfDSTLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDSTLoad.setStatus("mandatory")
_WfT1IILoad_Type = Counter32
_WfT1IILoad_Object = MibScalar
wfT1IILoad = _WfT1IILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 9),
    _WfT1IILoad_Type()
)
wfT1IILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1IILoad.setStatus("mandatory")
_WfE1IILoad_Type = Counter32
_WfE1IILoad_Object = MibScalar
wfE1IILoad = _WfE1IILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 10),
    _WfE1IILoad_Type()
)
wfE1IILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfE1IILoad.setStatus("mandatory")
_WfHSSILoad_Type = Counter32
_WfHSSILoad_Object = MibScalar
wfHSSILoad = _WfHSSILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 11),
    _WfHSSILoad_Type()
)
wfHSSILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHSSILoad.setStatus("mandatory")
_WfFNSDSELoad_Type = Counter32
_WfFNSDSELoad_Object = MibScalar
wfFNSDSELoad = _WfFNSDSELoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 12),
    _WfFNSDSELoad_Type()
)
wfFNSDSELoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFNSDSELoad.setStatus("mandatory")
_WfFNSDSDTLoad_Type = Counter32
_WfFNSDSDTLoad_Object = MibScalar
wfFNSDSDTLoad = _WfFNSDSDTLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 13),
    _WfFNSDSDTLoad_Type()
)
wfFNSDSDTLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFNSDSDTLoad.setStatus("mandatory")
_WfMCT1Load_Type = Counter32
_WfMCT1Load_Object = MibScalar
wfMCT1Load = _WfMCT1Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 14),
    _WfMCT1Load_Type()
)
wfMCT1Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMCT1Load.setStatus("mandatory")
_WfANLoad_Type = Counter32
_WfANLoad_Object = MibScalar
wfANLoad = _WfANLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 15),
    _WfANLoad_Type()
)
wfANLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfANLoad.setStatus("mandatory")
_WfFNSDSETLoad_Type = Counter32
_WfFNSDSETLoad_Object = MibScalar
wfFNSDSETLoad = _WfFNSDSETLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 16),
    _WfFNSDSETLoad_Type()
)
wfFNSDSETLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFNSDSETLoad.setStatus("mandatory")
_WfMCT1E1Load_Type = Counter32
_WfMCT1E1Load_Object = MibScalar
wfMCT1E1Load = _WfMCT1E1Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 17),
    _WfMCT1E1Load_Type()
)
wfMCT1E1Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMCT1E1Load.setStatus("mandatory")
_WfEFDDILoad_Type = Counter32
_WfEFDDILoad_Object = MibScalar
wfEFDDILoad = _WfEFDDILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 18),
    _WfEFDDILoad_Type()
)
wfEFDDILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfEFDDILoad.setStatus("mandatory")
_WfHLSLoad_Type = Counter32
_WfHLSLoad_Object = MibScalar
wfHLSLoad = _WfHLSLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 19),
    _WfHLSLoad_Type()
)
wfHLSLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHLSLoad.setStatus("mandatory")
_WfChipcomLoad_Type = Counter32
_WfChipcomLoad_Object = MibScalar
wfChipcomLoad = _WfChipcomLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 20),
    _WfChipcomLoad_Type()
)
wfChipcomLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfChipcomLoad.setStatus("mandatory")
_WfAtmcLoad_Type = Counter32
_WfAtmcLoad_Object = MibScalar
wfAtmcLoad = _WfAtmcLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 21),
    _WfAtmcLoad_Type()
)
wfAtmcLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmcLoad.setStatus("mandatory")
_WfHDWANLMLoad_Type = Counter32
_WfHDWANLMLoad_Object = MibScalar
wfHDWANLMLoad = _WfHDWANLMLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 22),
    _WfHDWANLMLoad_Type()
)
wfHDWANLMLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHDWANLMLoad.setStatus("mandatory")
_WfDE100Load_Type = Counter32
_WfDE100Load_Object = MibScalar
wfDE100Load = _WfDE100Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 23),
    _WfDE100Load_Type()
)
wfDE100Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDE100Load.setStatus("mandatory")
_WfAtmc5000Load_Type = Counter32
_WfAtmc5000Load_Object = MibScalar
wfAtmc5000Load = _WfAtmc5000Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 24),
    _WfAtmc5000Load_Type()
)
wfAtmc5000Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmc5000Load.setStatus("mandatory")
_WfArnLoad_Type = Counter32
_WfArnLoad_Object = MibScalar
wfArnLoad = _WfArnLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 25),
    _WfArnLoad_Type()
)
wfArnLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfArnLoad.setStatus("mandatory")
_WfFntsLoad_Type = Counter32
_WfFntsLoad_Object = MibScalar
wfFntsLoad = _WfFntsLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 26),
    _WfFntsLoad_Type()
)
wfFntsLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFntsLoad.setStatus("mandatory")
_WfSQE100Load_Type = Counter32
_WfSQE100Load_Object = MibScalar
wfSQE100Load = _WfSQE100Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 27),
    _WfSQE100Load_Type()
)
wfSQE100Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSQE100Load.setStatus("mandatory")
_WfGigEnetLoad_Type = Counter32
_WfGigEnetLoad_Object = MibScalar
wfGigEnetLoad = _WfGigEnetLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 28),
    _WfGigEnetLoad_Type()
)
wfGigEnetLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfGigEnetLoad.setStatus("mandatory")
_WfFBRLoad_Type = Counter32
_WfFBRLoad_Object = MibScalar
wfFBRLoad = _WfFBRLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 29),
    _WfFBRLoad_Type()
)
wfFBRLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFBRLoad.setStatus("mandatory")
_WfDrivers_ObjectIdentity = ObjectIdentity
wfDrivers = _WfDrivers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3)
)
_WfLANCELoad_Type = Counter32
_WfLANCELoad_Object = MibScalar
wfLANCELoad = _WfLANCELoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 1),
    _WfLANCELoad_Type()
)
wfLANCELoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLANCELoad.setStatus("mandatory")
_WfILACCLoad_Type = Counter32
_WfILACCLoad_Object = MibScalar
wfILACCLoad = _WfILACCLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 2),
    _WfILACCLoad_Type()
)
wfILACCLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfILACCLoad.setStatus("mandatory")
_WfFSILoad_Type = Counter32
_WfFSILoad_Object = MibScalar
wfFSILoad = _WfFSILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 3),
    _WfFSILoad_Type()
)
wfFSILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFSILoad.setStatus("mandatory")
_WfTMS380Load_Type = Counter32
_WfTMS380Load_Object = MibScalar
wfTMS380Load = _WfTMS380Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 4),
    _WfTMS380Load_Type()
)
wfTMS380Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTMS380Load.setStatus("mandatory")
_WfMK5025Load_Type = Counter32
_WfMK5025Load_Object = MibScalar
wfMK5025Load = _WfMK5025Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 5),
    _WfMK5025Load_Type()
)
wfMK5025Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMK5025Load.setStatus("mandatory")
_WfDS2180Load_Type = Counter32
_WfDS2180Load_Object = MibScalar
wfDS2180Load = _WfDS2180Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 6),
    _WfDS2180Load_Type()
)
wfDS2180Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDS2180Load.setStatus("mandatory")
_WfDS2181Load_Type = Counter32
_WfDS2181Load_Object = MibScalar
wfDS2181Load = _WfDS2181Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 7),
    _WfDS2181Load_Type()
)
wfDS2181Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDS2181Load.setStatus("mandatory")
_WfDEFALoad_Type = Counter32
_WfDEFALoad_Object = MibScalar
wfDEFALoad = _WfDEFALoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 8),
    _WfDEFALoad_Type()
)
wfDEFALoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDEFALoad.setStatus("mandatory")
_WfAMZ8530Load_Type = Counter32
_WfAMZ8530Load_Object = MibScalar
wfAMZ8530Load = _WfAMZ8530Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 9),
    _WfAMZ8530Load_Type()
)
wfAMZ8530Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAMZ8530Load.setStatus("mandatory")
_WfHSSIFSILoad_Type = Counter32
_WfHSSIFSILoad_Object = MibScalar
wfHSSIFSILoad = _WfHSSIFSILoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 10),
    _WfHSSIFSILoad_Type()
)
wfHSSIFSILoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHSSIFSILoad.setStatus("mandatory")
_WfMUNICHT1Load_Type = Counter32
_WfMUNICHT1Load_Object = MibScalar
wfMUNICHT1Load = _WfMUNICHT1Load_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 11),
    _WfMUNICHT1Load_Type()
)
wfMUNICHT1Load.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMUNICHT1Load.setStatus("mandatory")
_WfQsccSyncLoad_Type = Counter32
_WfQsccSyncLoad_Object = MibScalar
wfQsccSyncLoad = _WfQsccSyncLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 12),
    _WfQsccSyncLoad_Type()
)
wfQsccSyncLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQsccSyncLoad.setStatus("mandatory")
_WfQsccEnetLoad_Type = Counter32
_WfQsccEnetLoad_Object = MibScalar
wfQsccEnetLoad = _WfQsccEnetLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 13),
    _WfQsccEnetLoad_Type()
)
wfQsccEnetLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQsccEnetLoad.setStatus("mandatory")
_WfMunichLoad_Type = Counter32
_WfMunichLoad_Object = MibScalar
wfMunichLoad = _WfMunichLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 14),
    _WfMunichLoad_Type()
)
wfMunichLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMunichLoad.setStatus("mandatory")
_WfHilanceLoad_Type = Counter32
_WfHilanceLoad_Object = MibScalar
wfHilanceLoad = _WfHilanceLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 15),
    _WfHilanceLoad_Type()
)
wfHilanceLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHilanceLoad.setStatus("mandatory")
_WfAtmAlcLoad_Type = Counter32
_WfAtmAlcLoad_Object = MibScalar
wfAtmAlcLoad = _WfAtmAlcLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 16),
    _WfAtmAlcLoad_Type()
)
wfAtmAlcLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmAlcLoad.setStatus("mandatory")
_WfRptrLoad_Type = Counter32
_WfRptrLoad_Object = MibScalar
wfRptrLoad = _WfRptrLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 17),
    _WfRptrLoad_Type()
)
wfRptrLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRptrLoad.setStatus("mandatory")
_WfIsacLoad_Type = Counter32
_WfIsacLoad_Object = MibScalar
wfIsacLoad = _WfIsacLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 18),
    _WfIsacLoad_Type()
)
wfIsacLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsacLoad.setStatus("mandatory")
_WfAtmizerLoad_Type = Counter32
_WfAtmizerLoad_Object = MibScalar
wfAtmizerLoad = _WfAtmizerLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 19),
    _WfAtmizerLoad_Type()
)
wfAtmizerLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmizerLoad.setStatus("mandatory")
_WfNSC100MLoad_Type = Counter32
_WfNSC100MLoad_Object = MibScalar
wfNSC100MLoad = _WfNSC100MLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 20),
    _WfNSC100MLoad_Type()
)
wfNSC100MLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNSC100MLoad.setStatus("mandatory")
_WfDCMMWLoad_Type = Counter32
_WfDCMMWLoad_Object = MibScalar
wfDCMMWLoad = _WfDCMMWLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 21),
    _WfDCMMWLoad_Type()
)
wfDCMMWLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDCMMWLoad.setStatus("mandatory")
_WfHwCompLoad_Type = Counter32
_WfHwCompLoad_Object = MibScalar
wfHwCompLoad = _WfHwCompLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 22),
    _WfHwCompLoad_Type()
)
wfHwCompLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHwCompLoad.setStatus("mandatory")
_WfRAEsaLoad_Type = Counter32
_WfRAEsaLoad_Object = MibScalar
wfRAEsaLoad = _WfRAEsaLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 23),
    _WfRAEsaLoad_Type()
)
wfRAEsaLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRAEsaLoad.setStatus("mandatory")
_WfFntsAtmLoad_Type = Counter32
_WfFntsAtmLoad_Object = MibScalar
wfFntsAtmLoad = _WfFntsAtmLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 24),
    _WfFntsAtmLoad_Type()
)
wfFntsAtmLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFntsAtmLoad.setStatus("mandatory")
_WfRMONStatLoad_Type = Counter32
_WfRMONStatLoad_Object = MibScalar
wfRMONStatLoad = _WfRMONStatLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 25),
    _WfRMONStatLoad_Type()
)
wfRMONStatLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRMONStatLoad.setStatus("mandatory")
_WfSEEQ100MLoad_Type = Counter32
_WfSEEQ100MLoad_Object = MibScalar
wfSEEQ100MLoad = _WfSEEQ100MLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 26),
    _WfSEEQ100MLoad_Type()
)
wfSEEQ100MLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSEEQ100MLoad.setStatus("mandatory")
_WfSeeqGigLoad_Type = Counter32
_WfSeeqGigLoad_Object = MibScalar
wfSeeqGigLoad = _WfSeeqGigLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 27),
    _WfSeeqGigLoad_Type()
)
wfSeeqGigLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSeeqGigLoad.setStatus("mandatory")
_WfPQ2EnetLoad_Type = Counter32
_WfPQ2EnetLoad_Object = MibScalar
wfPQ2EnetLoad = _WfPQ2EnetLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 28),
    _WfPQ2EnetLoad_Type()
)
wfPQ2EnetLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPQ2EnetLoad.setStatus("mandatory")
_WfTdmManagerLoad_Type = Counter32
_WfTdmManagerLoad_Object = MibScalar
wfTdmManagerLoad = _WfTdmManagerLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 29),
    _WfTdmManagerLoad_Type()
)
wfTdmManagerLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTdmManagerLoad.setStatus("mandatory")
_WfPQ2DsyncLoad_Type = Counter32
_WfPQ2DsyncLoad_Object = MibScalar
wfPQ2DsyncLoad = _WfPQ2DsyncLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 30),
    _WfPQ2DsyncLoad_Type()
)
wfPQ2DsyncLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPQ2DsyncLoad.setStatus("mandatory")
_WfVoIPLoad_Type = Counter32
_WfVoIPLoad_Object = MibScalar
wfVoIPLoad = _WfVoIPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 31),
    _WfVoIPLoad_Type()
)
wfVoIPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVoIPLoad.setStatus("mandatory")
_WfQsccVoIPLoad_Type = Counter32
_WfQsccVoIPLoad_Object = MibScalar
wfQsccVoIPLoad = _WfQsccVoIPLoad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 32),
    _WfQsccVoIPLoad_Type()
)
wfQsccVoIPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfQsccVoIPLoad.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-LOADER-MIB",
    **{"wfProtocols": wfProtocols,
       "wfIPROTOLoad": wfIPROTOLoad,
       "wfDECNETLoad": wfDECNETLoad,
       "wfATLoad": wfATLoad,
       "wfXNSLoad": wfXNSLoad,
       "wfIPXLoad": wfIPXLoad,
       "wfOSILoad": wfOSILoad,
       "wfX25DTELoad": wfX25DTELoad,
       "wfX25DCELoad": wfX25DCELoad,
       "wfVINESLoad": wfVINESLoad,
       "wfFRLoad": wfFRLoad,
       "wfRARPLoad": wfRARPLoad,
       "wfATMLoad": wfATMLoad,
       "wfDLSLoad": wfDLSLoad,
       "wfLNMLoad": wfLNMLoad,
       "wfTelnetLoad": wfTelnetLoad,
       "wfTFTPLoad": wfTFTPLoad,
       "wfSNMPLoad": wfSNMPLoad,
       "wfTCPLoad": wfTCPLoad,
       "wfBGPLoad": wfBGPLoad,
       "wfEGPLoad": wfEGPLoad,
       "wfOSPFLoad": wfOSPFLoad,
       "wfWPROXYLoad": wfWPROXYLoad,
       "wfLLC2Load": wfLLC2Load,
       "wfSMDSLoad": wfSMDSLoad,
       "wfPPPLoad": wfPPPLoad,
       "wfPktCaptureLoad": wfPktCaptureLoad,
       "wfFRSWCNGCLoad": wfFRSWCNGCLoad,
       "wfSWPROXYLoad": wfSWPROXYLoad,
       "wfFRSWLoad": wfFRSWLoad,
       "wfSWSMDSLoad": wfSWSMDSLoad,
       "wfNBASELoad": wfNBASELoad,
       "wfSDLCLoad": wfSDLCLoad,
       "wfTNCLoad": wfTNCLoad,
       "wfLAPBLoad": wfLAPBLoad,
       "wfDebugLoad": wfDebugLoad,
       "wfNBIPLoad": wfNBIPLoad,
       "wfATMCsLoad": wfATMCsLoad,
       "wfDvmrpLoad": wfDvmrpLoad,
       "wfIgmpLoad": wfIgmpLoad,
       "wfISDNLoad": wfISDNLoad,
       "wfLMLoad": wfLMLoad,
       "wfPingLoad": wfPingLoad,
       "wfAPPNCpLoad": wfAPPNCpLoad,
       "wfAPPNLsLoad": wfAPPNLsLoad,
       "wfWcpLoad": wfWcpLoad,
       "wfFTPLoad": wfFTPLoad,
       "wfARPLoad": wfARPLoad,
       "wfSYSLLoad": wfSYSLLoad,
       "wfBGPRSLoad": wfBGPRSLoad,
       "wfATMLeLoad": wfATMLeLoad,
       "wfCRMLoad": wfCRMLoad,
       "wfIPEXLoad": wfIPEXLoad,
       "wfSt2Load": wfSt2Load,
       "wfNLSPLoad": wfNLSPLoad,
       "wfSTATSLoad": wfSTATSLoad,
       "wfNPTLoad": wfNPTLoad,
       "wfRREDUNDLoad": wfRREDUNDLoad,
       "wfATMSigLoad": wfATMSigLoad,
       "wfIPv6Load": wfIPv6Load,
       "wfBOTLoad": wfBOTLoad,
       "wfPimLoad": wfPimLoad,
       "wfLBCLoad": wfLBCLoad,
       "wfATMMcsLoad": wfATMMcsLoad,
       "wfATMAsmLoad": wfATMAsmLoad,
       "wfCPMLoad": wfCPMLoad,
       "wfBAYSIGLoad": wfBAYSIGLoad,
       "wfScmIpcLoad": wfScmIpcLoad,
       "wfNTPLoad": wfNTPLoad,
       "wfRADIUSLoad": wfRADIUSLoad,
       "wfRCMDSLoad": wfRCMDSLoad,
       "wfDNSLoad": wfDNSLoad,
       "wfWepLoad": wfWepLoad,
       "wfRipv6Load": wfRipv6Load,
       "wfMOSPFLoad": wfMOSPFLoad,
       "wfRSVPLoad": wfRSVPLoad,
       "wfIpSwitchLoad": wfIpSwitchLoad,
       "wfPortMtxLoad": wfPortMtxLoad,
       "wfConvStrLoad": wfConvStrLoad,
       "wfS5ChasLoad": wfS5ChasLoad,
       "wfFRSVCLoad": wfFRSVCLoad,
       "wfAOTLoad": wfAOTLoad,
       "wfNATLoad": wfNATLoad,
       "wfFRPTLoad": wfFRPTLoad,
       "wfHttpSrvLoad": wfHttpSrvLoad,
       "wfStacLZSLoad": wfStacLZSLoad,
       "wfASRLoad": wfASRLoad,
       "wfNHRPLoad": wfNHRPLoad,
       "wfAHBLoad": wfAHBLoad,
       "wfL2TPLoad": wfL2TPLoad,
       "wfISDBLoad": wfISDBLoad,
       "wfVCCTLoad": wfVCCTLoad,
       "wfMpsLoad": wfMpsLoad,
       "wfTAG1QLoad": wfTAG1QLoad,
       "wfMpcLoad": wfMpcLoad,
       "wfDVSLoad": wfDVSLoad,
       "wfVRRPLoad": wfVRRPLoad,
       "wfDHCPLoad": wfDHCPLoad,
       "wfCAPILoad": wfCAPILoad,
       "wfIPSECLoad": wfIPSECLoad,
       "wfMplsLdpLoad": wfMplsLdpLoad,
       "wfMplsMlmLoad": wfMplsMlmLoad,
       "wfBacPktGenLoad": wfBacPktGenLoad,
       "wfIISISLoad": wfIISISLoad,
       "wfCopsCLoad": wfCopsCLoad,
       "wfDiffServLoad": wfDiffServLoad,
       "wfIKELoad": wfIKELoad,
       "wfDsqmsProxyLoad": wfDsqmsProxyLoad,
       "wfLinkModules": wfLinkModules,
       "wfENETIILoad": wfENETIILoad,
       "wfQENETLoad": wfQENETLoad,
       "wfFDDILoad": wfFDDILoad,
       "wfDSDELoad": wfDSDELoad,
       "wfDSDEIILoad": wfDSDEIILoad,
       "wfQSYNCLoad": wfQSYNCLoad,
       "wfDTLoad": wfDTLoad,
       "wfDSTLoad": wfDSTLoad,
       "wfT1IILoad": wfT1IILoad,
       "wfE1IILoad": wfE1IILoad,
       "wfHSSILoad": wfHSSILoad,
       "wfFNSDSELoad": wfFNSDSELoad,
       "wfFNSDSDTLoad": wfFNSDSDTLoad,
       "wfMCT1Load": wfMCT1Load,
       "wfANLoad": wfANLoad,
       "wfFNSDSETLoad": wfFNSDSETLoad,
       "wfMCT1E1Load": wfMCT1E1Load,
       "wfEFDDILoad": wfEFDDILoad,
       "wfHLSLoad": wfHLSLoad,
       "wfChipcomLoad": wfChipcomLoad,
       "wfAtmcLoad": wfAtmcLoad,
       "wfHDWANLMLoad": wfHDWANLMLoad,
       "wfDE100Load": wfDE100Load,
       "wfAtmc5000Load": wfAtmc5000Load,
       "wfArnLoad": wfArnLoad,
       "wfFntsLoad": wfFntsLoad,
       "wfSQE100Load": wfSQE100Load,
       "wfGigEnetLoad": wfGigEnetLoad,
       "wfFBRLoad": wfFBRLoad,
       "wfDrivers": wfDrivers,
       "wfLANCELoad": wfLANCELoad,
       "wfILACCLoad": wfILACCLoad,
       "wfFSILoad": wfFSILoad,
       "wfTMS380Load": wfTMS380Load,
       "wfMK5025Load": wfMK5025Load,
       "wfDS2180Load": wfDS2180Load,
       "wfDS2181Load": wfDS2181Load,
       "wfDEFALoad": wfDEFALoad,
       "wfAMZ8530Load": wfAMZ8530Load,
       "wfHSSIFSILoad": wfHSSIFSILoad,
       "wfMUNICHT1Load": wfMUNICHT1Load,
       "wfQsccSyncLoad": wfQsccSyncLoad,
       "wfQsccEnetLoad": wfQsccEnetLoad,
       "wfMunichLoad": wfMunichLoad,
       "wfHilanceLoad": wfHilanceLoad,
       "wfAtmAlcLoad": wfAtmAlcLoad,
       "wfRptrLoad": wfRptrLoad,
       "wfIsacLoad": wfIsacLoad,
       "wfAtmizerLoad": wfAtmizerLoad,
       "wfNSC100MLoad": wfNSC100MLoad,
       "wfDCMMWLoad": wfDCMMWLoad,
       "wfHwCompLoad": wfHwCompLoad,
       "wfRAEsaLoad": wfRAEsaLoad,
       "wfFntsAtmLoad": wfFntsAtmLoad,
       "wfRMONStatLoad": wfRMONStatLoad,
       "wfSEEQ100MLoad": wfSEEQ100MLoad,
       "wfSeeqGigLoad": wfSeeqGigLoad,
       "wfPQ2EnetLoad": wfPQ2EnetLoad,
       "wfTdmManagerLoad": wfTdmManagerLoad,
       "wfPQ2DsyncLoad": wfPQ2DsyncLoad,
       "wfVoIPLoad": wfVoIPLoad,
       "wfQsccVoIPLoad": wfQsccVoIPLoad}
)
