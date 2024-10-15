# SNMP MIB module (CHEETAH-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHEETAH-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:42 2024
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

(fltCurCfgIndx,
 fltCurCfgPortIndx,
 fltCurCfgSrcIp,
 slbCurCfgRealServerIndex,
 slbCurCfgRealServerIpAddr,
 slbCurCfgRealServerName,
 slbCurCfgVirtServiceRealPort) = mibBuilder.importSymbols(
    "ALTEON-CHEETAH-LAYER4-MIB",
    "fltCurCfgIndx",
    "fltCurCfgPortIndx",
    "fltCurCfgSrcIp",
    "slbCurCfgRealServerIndex",
    "slbCurCfgRealServerIpAddr",
    "slbCurCfgRealServerName",
    "slbCurCfgVirtServiceRealPort")

(ipCurCfgGwAddr,
 ipCurCfgGwIndex,
 vrrpCurCfgIfIndx,
 vrrpCurCfgIfPasswd,
 vrrpCurCfgVirtRtrAddr,
 vrrpCurCfgVirtRtrIndx) = mibBuilder.importSymbols(
    "ALTEON-CHEETAH-NETWORK-MIB",
    "ipCurCfgGwAddr",
    "ipCurCfgGwIndex",
    "vrrpCurCfgIfIndx",
    "vrrpCurCfgIfPasswd",
    "vrrpCurCfgVirtRtrAddr",
    "vrrpCurCfgVirtRtrIndx")

(aws_switch,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "aws-switch")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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

_AltTraps_ObjectIdentity = ObjectIdentity
altTraps = _AltTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7)
)


class _AltSwTrapDisplayString_Type(DisplayString):
    """Custom type altSwTrapDisplayString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AltSwTrapDisplayString_Type.__name__ = "DisplayString"
_AltSwTrapDisplayString_Object = MibScalar
altSwTrapDisplayString = _AltSwTrapDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 1000),
    _AltSwTrapDisplayString_Type()
)
altSwTrapDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altSwTrapDisplayString.setStatus("mandatory")
_AltSwTrapRate_Type = Integer32
_AltSwTrapRate_Object = MibScalar
altSwTrapRate = _AltSwTrapRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 1001),
    _AltSwTrapRate_Type()
)
altSwTrapRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altSwTrapRate.setStatus("mandatory")

# Managed Objects groups


# Notification objects

altSwPrimaryPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 1)
)
if mibBuilder.loadTexts:
    altSwPrimaryPowerSupplyFailure.setStatus(
        ""
    )

altSwDefGwUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 2)
)
altSwDefGwUp.setObjects(
      *(("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwIndex"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDefGwUp.setStatus(
        ""
    )

altSwDefGwDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 3)
)
altSwDefGwDown.setObjects(
      *(("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwIndex"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDefGwDown.setStatus(
        ""
    )

altSwDefGwInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 4)
)
altSwDefGwInService.setObjects(
      *(("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwIndex"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDefGwInService.setStatus(
        ""
    )

altSwDefGwNotInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 5)
)
altSwDefGwNotInService.setObjects(
      *(("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwIndex"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDefGwNotInService.setStatus(
        ""
    )

altSwSlbRealServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 6)
)
altSwSlbRealServerUp.setObjects(
      *(("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerUp.setStatus(
        ""
    )

altSwSlbRealServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 7)
)
altSwSlbRealServerDown.setObjects(
      *(("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerDown.setStatus(
        ""
    )

altSwSlbRealServerMaxConnReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 8)
)
altSwSlbRealServerMaxConnReached.setObjects(
      *(("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerMaxConnReached.setStatus(
        ""
    )

altSwSlbBkupRealServerAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 9)
)
altSwSlbBkupRealServerAct.setObjects(
      *(("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupRealServerAct.setStatus(
        ""
    )

altSwSlbBkupRealServerDeact = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 10)
)
altSwSlbBkupRealServerDeact.setObjects(
      *(("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupRealServerDeact.setStatus(
        ""
    )

altSwSlbBkupRealServerActOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 11)
)
altSwSlbBkupRealServerActOverflow.setObjects(
      *(("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupRealServerActOverflow.setStatus(
        ""
    )

altSwSlbBkupRealServerDeactOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 12)
)
altSwSlbBkupRealServerDeactOverflow.setObjects(
      *(("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupRealServerDeactOverflow.setStatus(
        ""
    )

altSwfltFilterFired = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 13)
)
altSwfltFilterFired.setObjects(
      *(("ALTEON-CHEETAH-LAYER4-MIB", "fltCurCfgIndx"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "fltCurCfgPortIndx"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwfltFilterFired.setStatus(
        ""
    )

altSwSlbRealServerServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 14)
)
altSwSlbRealServerServiceUp.setObjects(
      *(("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgVirtServiceRealPort"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerServiceUp.setStatus(
        ""
    )

altSwSlbRealServerServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 15)
)
altSwSlbRealServerServiceDown.setObjects(
      *(("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerName"),
        ("ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgVirtServiceRealPort"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerServiceDown.setStatus(
        ""
    )

altSwVrrpNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 16)
)
altSwVrrpNewMaster.setObjects(
      *(("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwVrrpNewMaster.setStatus(
        ""
    )

altSwVrrpNewBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 17)
)
altSwVrrpNewBackup.setObjects(
      *(("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwVrrpNewBackup.setStatus(
        ""
    )

altSwVrrpAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 18)
)
altSwVrrpAuthFailure.setObjects(
      *(("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgIfIndx"),
        ("ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgIfPasswd"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwVrrpAuthFailure.setStatus(
        ""
    )

altSwLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 19)
)
altSwLoginFailure.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwLoginFailure.setStatus(
        ""
    )

altSwSlbSynAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 20)
)
altSwSlbSynAttack.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapRate"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbSynAttack.setStatus(
        ""
    )

altSwTcpHoldDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 21)
)
altSwTcpHoldDown.setObjects(
      *(("ALTEON-CHEETAH-LAYER4-MIB", "fltCurCfgSrcIp"),
        ("CHEETAH-TRAP-MIB", "altSwTrapRate"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwTcpHoldDown.setStatus(
        ""
    )

altSwTempExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 7, 0, 22)
)
altSwTempExceedThreshold.setObjects(
      *(("CHEETAH-TRAP-MIB", "altSwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwTempExceedThreshold.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHEETAH-TRAP-MIB",
    **{"altTraps": altTraps,
       "altSwPrimaryPowerSupplyFailure": altSwPrimaryPowerSupplyFailure,
       "altSwDefGwUp": altSwDefGwUp,
       "altSwDefGwDown": altSwDefGwDown,
       "altSwDefGwInService": altSwDefGwInService,
       "altSwDefGwNotInService": altSwDefGwNotInService,
       "altSwSlbRealServerUp": altSwSlbRealServerUp,
       "altSwSlbRealServerDown": altSwSlbRealServerDown,
       "altSwSlbRealServerMaxConnReached": altSwSlbRealServerMaxConnReached,
       "altSwSlbBkupRealServerAct": altSwSlbBkupRealServerAct,
       "altSwSlbBkupRealServerDeact": altSwSlbBkupRealServerDeact,
       "altSwSlbBkupRealServerActOverflow": altSwSlbBkupRealServerActOverflow,
       "altSwSlbBkupRealServerDeactOverflow": altSwSlbBkupRealServerDeactOverflow,
       "altSwfltFilterFired": altSwfltFilterFired,
       "altSwSlbRealServerServiceUp": altSwSlbRealServerServiceUp,
       "altSwSlbRealServerServiceDown": altSwSlbRealServerServiceDown,
       "altSwVrrpNewMaster": altSwVrrpNewMaster,
       "altSwVrrpNewBackup": altSwVrrpNewBackup,
       "altSwVrrpAuthFailure": altSwVrrpAuthFailure,
       "altSwLoginFailure": altSwLoginFailure,
       "altSwSlbSynAttack": altSwSlbSynAttack,
       "altSwTcpHoldDown": altSwTcpHoldDown,
       "altSwTempExceedThreshold": altSwTempExceedThreshold,
       "altSwTrapDisplayString": altSwTrapDisplayString,
       "altSwTrapRate": altSwTrapRate}
)
