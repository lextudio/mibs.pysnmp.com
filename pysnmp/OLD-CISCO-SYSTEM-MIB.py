# SNMP MIB module (OLD-CISCO-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLD-CISCO-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:26 2024
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

(local,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "local")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lsystem_ObjectIdentity = ObjectIdentity
lsystem = _Lsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 1)
)
_RomId_Type = DisplayString
_RomId_Object = MibScalar
romId = _RomId_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 1),
    _RomId_Type()
)
romId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    romId.setStatus("mandatory")
_WhyReload_Type = DisplayString
_WhyReload_Object = MibScalar
whyReload = _WhyReload_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 2),
    _WhyReload_Type()
)
whyReload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whyReload.setStatus("mandatory")
_HostName_Type = DisplayString
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 3),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("mandatory")
_DomainName_Type = DisplayString
_DomainName_Object = MibScalar
domainName = _DomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 4),
    _DomainName_Type()
)
domainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainName.setStatus("mandatory")
_AuthAddr_Type = IpAddress
_AuthAddr_Object = MibScalar
authAddr = _AuthAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 5),
    _AuthAddr_Type()
)
authAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authAddr.setStatus("mandatory")
_BootHost_Type = IpAddress
_BootHost_Object = MibScalar
bootHost = _BootHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 6),
    _BootHost_Type()
)
bootHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootHost.setStatus("mandatory")
_NetConfigAddr_Type = IpAddress
_NetConfigAddr_Object = MibScalar
netConfigAddr = _NetConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 48),
    _NetConfigAddr_Type()
)
netConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigAddr.setStatus("mandatory")
_NetConfigName_Type = DisplayString
_NetConfigName_Object = MibScalar
netConfigName = _NetConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 49),
    _NetConfigName_Type()
)
netConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigName.setStatus("mandatory")
_NetConfigSet_Type = DisplayString
_NetConfigSet_Object = MibScalar
netConfigSet = _NetConfigSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 50),
    _NetConfigSet_Type()
)
netConfigSet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    netConfigSet.setStatus("mandatory")
_HostConfigAddr_Type = IpAddress
_HostConfigAddr_Object = MibScalar
hostConfigAddr = _HostConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 51),
    _HostConfigAddr_Type()
)
hostConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostConfigAddr.setStatus("obsolete")
_HostConfigName_Type = DisplayString
_HostConfigName_Object = MibScalar
hostConfigName = _HostConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 52),
    _HostConfigName_Type()
)
hostConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostConfigName.setStatus("obsolete")
_HostConfigSet_Type = DisplayString
_HostConfigSet_Object = MibScalar
hostConfigSet = _HostConfigSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 53),
    _HostConfigSet_Type()
)
hostConfigSet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hostConfigSet.setStatus("obsolete")
_WriteMem_Type = Integer32
_WriteMem_Object = MibScalar
writeMem = _WriteMem_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 54),
    _WriteMem_Type()
)
writeMem.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    writeMem.setStatus("mandatory")
_WriteNet_Type = DisplayString
_WriteNet_Object = MibScalar
writeNet = _WriteNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 55),
    _WriteNet_Type()
)
writeNet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    writeNet.setStatus("mandatory")
_CiscoContactInfo_Type = DisplayString
_CiscoContactInfo_Object = MibScalar
ciscoContactInfo = _CiscoContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 61),
    _CiscoContactInfo_Type()
)
ciscoContactInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoContactInfo.setStatus("mandatory")
_NetConfigProto_Type = Integer32
_NetConfigProto_Object = MibScalar
netConfigProto = _NetConfigProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 70),
    _NetConfigProto_Type()
)
netConfigProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigProto.setStatus("mandatory")
_HostConfigProto_Type = Integer32
_HostConfigProto_Object = MibScalar
hostConfigProto = _HostConfigProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 71),
    _HostConfigProto_Type()
)
hostConfigProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostConfigProto.setStatus("mandatory")
_SysConfigAddr_Type = IpAddress
_SysConfigAddr_Object = MibScalar
sysConfigAddr = _SysConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 72),
    _SysConfigAddr_Type()
)
sysConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigAddr.setStatus("mandatory")
_SysConfigName_Type = DisplayString
_SysConfigName_Object = MibScalar
sysConfigName = _SysConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 73),
    _SysConfigName_Type()
)
sysConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigName.setStatus("mandatory")


class _SysConfigProto_Type(Integer32):
    """Custom type sysConfigProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 3),
          ("rom", 2),
          ("tftp", 1))
    )


_SysConfigProto_Type.__name__ = "Integer32"
_SysConfigProto_Object = MibScalar
sysConfigProto = _SysConfigProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 74),
    _SysConfigProto_Type()
)
sysConfigProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigProto.setStatus("mandatory")
_SysClearARP_Type = Integer32
_SysClearARP_Object = MibScalar
sysClearARP = _SysClearARP_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 75),
    _SysClearARP_Type()
)
sysClearARP.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sysClearARP.setStatus("mandatory")
_SysClearInt_Type = Integer32
_SysClearInt_Object = MibScalar
sysClearInt = _SysClearInt_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 76),
    _SysClearInt_Type()
)
sysClearInt.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sysClearInt.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-SYSTEM-MIB",
    **{"lsystem": lsystem,
       "romId": romId,
       "whyReload": whyReload,
       "hostName": hostName,
       "domainName": domainName,
       "authAddr": authAddr,
       "bootHost": bootHost,
       "netConfigAddr": netConfigAddr,
       "netConfigName": netConfigName,
       "netConfigSet": netConfigSet,
       "hostConfigAddr": hostConfigAddr,
       "hostConfigName": hostConfigName,
       "hostConfigSet": hostConfigSet,
       "writeMem": writeMem,
       "writeNet": writeNet,
       "ciscoContactInfo": ciscoContactInfo,
       "netConfigProto": netConfigProto,
       "hostConfigProto": hostConfigProto,
       "sysConfigAddr": sysConfigAddr,
       "sysConfigName": sysConfigName,
       "sysConfigProto": sysConfigProto,
       "sysClearARP": sysClearARP,
       "sysClearInt": sysClearInt}
)
