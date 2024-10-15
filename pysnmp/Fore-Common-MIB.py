# SNMP MIB module (Fore-Common-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Common-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:29 2024
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

fore = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326)
)


# Types definitions



class SpansAddress(OctetString):
    """Custom type SpansAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class AtmAddress(OctetString):
    """Custom type AtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(20, 20),
    )





class NsapPrefix(OctetString):
    """Custom type NsapPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )





class NsapAddr(OctetString):
    """Custom type NsapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )





class TransitNetwork(DisplayString):
    """Custom type TransitNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )





class TrapNumber(Integer32):
    """Custom type TrapNumber based on Integer32"""




class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )





class AtmSigProtocol(Integer32):
    """Custom type AtmSigProtocol based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("fsig", 10),
          ("ipCtl", 12),
          ("mpls", 11),
          ("oam", 6),
          ("oam-ctl", 13),
          ("other", 1),
          ("pvc", 4),
          ("q2931", 3),
          ("rcc", 9),
          ("spans", 2),
          ("spvc", 5),
          ("spvcPnni", 8),
          ("spvcSpans", 7))
    )





class GeneralState(Integer32):
    """Custom type GeneralState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("normal", 1))
    )





class IntegerBitString(Integer32):
    """Custom type IntegerBitString based on Integer32"""




class ConnectionType(Integer32):
    """Custom type ConnectionType based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Admin_ObjectIdentity = ObjectIdentity
admin = _Admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1)
)
_Operations_ObjectIdentity = ObjectIdentity
operations = _Operations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 1)
)
_SnmpErrors_ObjectIdentity = ObjectIdentity
snmpErrors = _SnmpErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 2)
)
_SnmpTrapDest_ObjectIdentity = ObjectIdentity
snmpTrapDest = _SnmpTrapDest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 3)
)
_SnmpAccess_ObjectIdentity = ObjectIdentity
snmpAccess = _SnmpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 4)
)
_Assembly_ObjectIdentity = ObjectIdentity
assembly = _Assembly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 5)
)
_FileXfr_ObjectIdentity = ObjectIdentity
fileXfr = _FileXfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 6)
)
_RmonExtensions_ObjectIdentity = ObjectIdentity
rmonExtensions = _RmonExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 7)
)
_PreDot1qVlanMIB_ObjectIdentity = ObjectIdentity
preDot1qVlanMIB = _PreDot1qVlanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 8)
)
_SnmpTrapLog_ObjectIdentity = ObjectIdentity
snmpTrapLog = _SnmpTrapLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 9)
)
_Ilmisnmp_ObjectIdentity = ObjectIdentity
ilmisnmp = _Ilmisnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 10)
)
_EntityExtensionMIB_ObjectIdentity = ObjectIdentity
entityExtensionMIB = _EntityExtensionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 11)
)
_IlmiRegistry_ObjectIdentity = ObjectIdentity
ilmiRegistry = _IlmiRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 14)
)
_ForeIfExtension_ObjectIdentity = ObjectIdentity
foreIfExtension = _ForeIfExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 15)
)
_FrameInternetworking_ObjectIdentity = ObjectIdentity
frameInternetworking = _FrameInternetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 16)
)
_IfExtensions_ObjectIdentity = ObjectIdentity
ifExtensions = _IfExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 17)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2)
)
_AtmAdapter_ObjectIdentity = ObjectIdentity
atmAdapter = _AtmAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1)
)
_AtmSwitch_ObjectIdentity = ObjectIdentity
atmSwitch = _AtmSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1)
)
_Asx_ObjectIdentity = ObjectIdentity
asx = _Asx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2)
)
_Asxd_ObjectIdentity = ObjectIdentity
asxd = _Asxd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1)
)
_Asx200wg_ObjectIdentity = ObjectIdentity
asx200wg = _Asx200wg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 4)
)
_Asx200bx_ObjectIdentity = ObjectIdentity
asx200bx = _Asx200bx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 5)
)
_Asx200bxe_ObjectIdentity = ObjectIdentity
asx200bxe = _Asx200bxe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 6)
)
_Cabletron9A000_ObjectIdentity = ObjectIdentity
cabletron9A000 = _Cabletron9A000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 7)
)
_Asx1000_ObjectIdentity = ObjectIdentity
asx1000 = _Asx1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 8)
)
_Le155_ObjectIdentity = ObjectIdentity
le155 = _Le155_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 9)
)
_Sfcs200wg_ObjectIdentity = ObjectIdentity
sfcs200wg = _Sfcs200wg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 10)
)
_Sfcs200bx_ObjectIdentity = ObjectIdentity
sfcs200bx = _Sfcs200bx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 11)
)
_Sfcs1000_ObjectIdentity = ObjectIdentity
sfcs1000 = _Sfcs1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 12)
)
_Tnx210_ObjectIdentity = ObjectIdentity
tnx210 = _Tnx210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 15)
)
_Tnx1100_ObjectIdentity = ObjectIdentity
tnx1100 = _Tnx1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 16)
)
_Asx1200_ObjectIdentity = ObjectIdentity
asx1200 = _Asx1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 17)
)
_Asx4000_ObjectIdentity = ObjectIdentity
asx4000 = _Asx4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 18)
)
_Le25_ObjectIdentity = ObjectIdentity
le25 = _Le25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 19)
)
_Esx3000_ObjectIdentity = ObjectIdentity
esx3000 = _Esx3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 20)
)
_Tnx1100b_ObjectIdentity = ObjectIdentity
tnx1100b = _Tnx1100b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 21)
)
_Asx150_ObjectIdentity = ObjectIdentity
asx150 = _Asx150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 22)
)
_Bxr48000_ObjectIdentity = ObjectIdentity
bxr48000 = _Bxr48000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 24)
)
_Asx4000m_ObjectIdentity = ObjectIdentity
asx4000m = _Asx4000m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 25)
)
_AxhIp_ObjectIdentity = ObjectIdentity
axhIp = _AxhIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 26)
)
_AxhSig_ObjectIdentity = ObjectIdentity
axhSig = _AxhSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 27)
)
_EtherSwitch_ObjectIdentity = ObjectIdentity
etherSwitch = _EtherSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 3)
)
_AtmAccess_ObjectIdentity = ObjectIdentity
atmAccess = _AtmAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 5)
)
_HubSwitchRouter_ObjectIdentity = ObjectIdentity
hubSwitchRouter = _HubSwitchRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6)
)
_Ipoa_ObjectIdentity = ObjectIdentity
ipoa = _Ipoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 7)
)
_StackSwitch_ObjectIdentity = ObjectIdentity
stackSwitch = _StackSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 10)
)
_SwitchRouter_ObjectIdentity = ObjectIdentity
switchRouter = _SwitchRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 15)
)
_ForeExperiment_ObjectIdentity = ObjectIdentity
foreExperiment = _ForeExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Common-MIB",
    **{"SpansAddress": SpansAddress,
       "AtmAddress": AtmAddress,
       "NsapPrefix": NsapPrefix,
       "NsapAddr": NsapAddr,
       "TransitNetwork": TransitNetwork,
       "TrapNumber": TrapNumber,
       "EntryStatus": EntryStatus,
       "AtmSigProtocol": AtmSigProtocol,
       "GeneralState": GeneralState,
       "IntegerBitString": IntegerBitString,
       "ConnectionType": ConnectionType,
       "fore": fore,
       "admin": admin,
       "operations": operations,
       "snmpErrors": snmpErrors,
       "snmpTrapDest": snmpTrapDest,
       "snmpAccess": snmpAccess,
       "assembly": assembly,
       "fileXfr": fileXfr,
       "rmonExtensions": rmonExtensions,
       "preDot1qVlanMIB": preDot1qVlanMIB,
       "snmpTrapLog": snmpTrapLog,
       "ilmisnmp": ilmisnmp,
       "entityExtensionMIB": entityExtensionMIB,
       "ilmiRegistry": ilmiRegistry,
       "foreIfExtension": foreIfExtension,
       "frameInternetworking": frameInternetworking,
       "ifExtensions": ifExtensions,
       "systems": systems,
       "atmAdapter": atmAdapter,
       "atmSwitch": atmSwitch,
       "hardware": hardware,
       "asx": asx,
       "software": software,
       "asxd": asxd,
       "asx200wg": asx200wg,
       "asx200bx": asx200bx,
       "asx200bxe": asx200bxe,
       "cabletron9A000": cabletron9A000,
       "asx1000": asx1000,
       "le155": le155,
       "sfcs200wg": sfcs200wg,
       "sfcs200bx": sfcs200bx,
       "sfcs1000": sfcs1000,
       "tnx210": tnx210,
       "tnx1100": tnx1100,
       "asx1200": asx1200,
       "asx4000": asx4000,
       "le25": le25,
       "esx3000": esx3000,
       "tnx1100b": tnx1100b,
       "asx150": asx150,
       "bxr48000": bxr48000,
       "asx4000m": asx4000m,
       "axhIp": axhIp,
       "axhSig": axhSig,
       "etherSwitch": etherSwitch,
       "atmAccess": atmAccess,
       "hubSwitchRouter": hubSwitchRouter,
       "ipoa": ipoa,
       "stackSwitch": stackSwitch,
       "switchRouter": switchRouter,
       "foreExperiment": foreExperiment}
)
