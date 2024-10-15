# SNMP MIB module (FORTINET-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORTINET-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:38 2024
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

(fortinet,
 fortinetTrap) = mibBuilder.importSymbols(
    "FORTINET-MIB",
    "fortinet",
    "fortinetTrap")

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

_FnTrapSysSn_Type = DisplayString
_FnTrapSysSn_Object = MibScalar
fnTrapSysSn = _FnTrapSysSn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 10, 1),
    _FnTrapSysSn_Type()
)
fnTrapSysSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnTrapSysSn.setStatus("mandatory")


class _FnTrapIfName_Type(DisplayString):
    """Custom type fnTrapIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnTrapIfName_Type.__name__ = "DisplayString"
_FnTrapIfName_Object = MibScalar
fnTrapIfName = _FnTrapIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 10, 2),
    _FnTrapIfName_Type()
)
fnTrapIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnTrapIfName.setStatus("mandatory")
_FnTrapIfIp_Type = IpAddress
_FnTrapIfIp_Object = MibScalar
fnTrapIfIp = _FnTrapIfIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 10, 3),
    _FnTrapIfIp_Type()
)
fnTrapIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnTrapIfIp.setStatus("mandatory")
_FnTrapIfNetmask_Type = IpAddress
_FnTrapIfNetmask_Object = MibScalar
fnTrapIfNetmask = _FnTrapIfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 10, 4),
    _FnTrapIfNetmask_Type()
)
fnTrapIfNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnTrapIfNetmask.setStatus("mandatory")


class _FnTrapType_Type(Integer32):
    """Custom type fnTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(51,
              52,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              301,
              401,
              402,
              501,
              502,
              601,
              901)
        )
    )
    namedValues = NamedValues(
        *(("auth-srv-unreachable", 301),
          ("cpu-usage-high", 101),
          ("disk-low", 103),
          ("ha-swtich", 106),
          ("hardware-problem", 107),
          ("interface-ip-change", 104),
          ("link-down", 52),
          ("link-up", 51),
          ("log-full", 901),
          ("memory-low", 102),
          ("port-scan-attack", 502),
          ("syn-flood-attack", 501),
          ("system-dead", 105),
          ("virus-detected", 601),
          ("vpn-tunnel-down", 402),
          ("vpn-tunnel-up", 401))
    )


_FnTrapType_Type.__name__ = "Integer32"
_FnTrapType_Object = MibScalar
fnTrapType = _FnTrapType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 10, 5),
    _FnTrapType_Type()
)
fnTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnTrapType.setStatus("mandatory")


class _FnTrapDesc_Type(DisplayString):
    """Custom type fnTrapDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnTrapDesc_Type.__name__ = "DisplayString"
_FnTrapDesc_Object = MibScalar
fnTrapDesc = _FnTrapDesc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 10, 6),
    _FnTrapDesc_Type()
)
fnTrapDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnTrapDesc.setStatus("mandatory")

# Managed Objects groups


# Notification objects

fnTrapColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 0)
)
if mibBuilder.loadTexts:
    fnTrapColdStart.setStatus(
        ""
    )

fnTrapSystemDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 10)
)
if mibBuilder.loadTexts:
    fnTrapSystemDown.setStatus(
        ""
    )

fnTrapAgentDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 11)
)
if mibBuilder.loadTexts:
    fnTrapAgentDown.setStatus(
        ""
    )

fnTrapAgentUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 12)
)
if mibBuilder.loadTexts:
    fnTrapAgentUp.setStatus(
        ""
    )

fnTrapInfChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 100)
)
fnTrapInfChg.setObjects(
      *(("FORTINET-TRAP-MIB", "fnTrapSysSn"),
        ("FORTINET-TRAP-MIB", "fnTrapIfName"),
        ("FORTINET-TRAP-MIB", "fnTrapIfNetmask"),
        ("FORTINET-TRAP-MIB", "fnTrapSysSn"))
)
if mibBuilder.loadTexts:
    fnTrapInfChg.setStatus(
        ""
    )

fnTrapSystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 101)
)
fnTrapSystem.setObjects(
      *(("FORTINET-TRAP-MIB", "fnTrapType"),
        ("FORTINET-TRAP-MIB", "fnTrapDesc"))
)
if mibBuilder.loadTexts:
    fnTrapSystem.setStatus(
        ""
    )

fnTrapFirewall = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 200)
)
fnTrapFirewall.setObjects(
      *(("FORTINET-TRAP-MIB", "fnTrapType"),
        ("FORTINET-TRAP-MIB", "fnTrapDesc"))
)
if mibBuilder.loadTexts:
    fnTrapFirewall.setStatus(
        ""
    )

fnTrapUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 300)
)
fnTrapUser.setObjects(
      *(("FORTINET-TRAP-MIB", "fnTrapType"),
        ("FORTINET-TRAP-MIB", "fnTrapDesc"))
)
if mibBuilder.loadTexts:
    fnTrapUser.setStatus(
        ""
    )

fnTrapVpn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 400)
)
fnTrapVpn.setObjects(
      *(("FORTINET-TRAP-MIB", "fnTrapType"),
        ("FORTINET-TRAP-MIB", "fnTrapDesc"))
)
if mibBuilder.loadTexts:
    fnTrapVpn.setStatus(
        ""
    )

fnTrapNids = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 500)
)
fnTrapNids.setObjects(
      *(("FORTINET-TRAP-MIB", "fnTrapType"),
        ("FORTINET-TRAP-MIB", "fnTrapDesc"))
)
if mibBuilder.loadTexts:
    fnTrapNids.setStatus(
        ""
    )

fnTrapAntiVirus = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 600)
)
fnTrapAntiVirus.setObjects(
      *(("FORTINET-TRAP-MIB", "fnTrapType"),
        ("FORTINET-TRAP-MIB", "fnTrapDesc"))
)
if mibBuilder.loadTexts:
    fnTrapAntiVirus.setStatus(
        ""
    )

fnTrapWebFilter = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 700)
)
fnTrapWebFilter.setObjects(
      *(("FORTINET-TRAP-MIB", "fnTrapType"),
        ("FORTINET-TRAP-MIB", "fnTrapDesc"))
)
if mibBuilder.loadTexts:
    fnTrapWebFilter.setStatus(
        ""
    )

fnTrapEmailFilter = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 800)
)
fnTrapEmailFilter.setObjects(
      *(("FORTINET-TRAP-MIB", "fnTrapType"),
        ("FORTINET-TRAP-MIB", "fnTrapDesc"))
)
if mibBuilder.loadTexts:
    fnTrapEmailFilter.setStatus(
        ""
    )

fnTrapLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 900)
)
fnTrapLog.setObjects(
      *(("FORTINET-TRAP-MIB", "fnTrapType"),
        ("FORTINET-TRAP-MIB", "fnTrapDesc"))
)
if mibBuilder.loadTexts:
    fnTrapLog.setStatus(
        ""
    )

fnTrapMisc = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 1000)
)
fnTrapMisc.setObjects(
      *(("FORTINET-TRAP-MIB", "fnTrapType"),
        ("FORTINET-TRAP-MIB", "fnTrapDesc"))
)
if mibBuilder.loadTexts:
    fnTrapMisc.setStatus(
        ""
    )

fnTrapDemoUpdateConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 10000)
)
fnTrapDemoUpdateConfig.setObjects(
      *(("FORTINET-TRAP-MIB", "fnTrapSysSn"),
        ("FORTINET-TRAP-MIB", "fnTrapIfName"),
        ("FORTINET-TRAP-MIB", "fnTrapIfNetmask"),
        ("FORTINET-TRAP-MIB", "fnTrapSysSn"))
)
if mibBuilder.loadTexts:
    fnTrapDemoUpdateConfig.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-TRAP-MIB",
    **{"fnTrapColdStart": fnTrapColdStart,
       "fnTrapSystemDown": fnTrapSystemDown,
       "fnTrapAgentDown": fnTrapAgentDown,
       "fnTrapAgentUp": fnTrapAgentUp,
       "fnTrapInfChg": fnTrapInfChg,
       "fnTrapSystem": fnTrapSystem,
       "fnTrapFirewall": fnTrapFirewall,
       "fnTrapUser": fnTrapUser,
       "fnTrapVpn": fnTrapVpn,
       "fnTrapNids": fnTrapNids,
       "fnTrapAntiVirus": fnTrapAntiVirus,
       "fnTrapWebFilter": fnTrapWebFilter,
       "fnTrapEmailFilter": fnTrapEmailFilter,
       "fnTrapLog": fnTrapLog,
       "fnTrapMisc": fnTrapMisc,
       "fnTrapDemoUpdateConfig": fnTrapDemoUpdateConfig,
       "fnTrapSysSn": fnTrapSysSn,
       "fnTrapIfName": fnTrapIfName,
       "fnTrapIfIp": fnTrapIfIp,
       "fnTrapIfNetmask": fnTrapIfNetmask,
       "fnTrapType": fnTrapType,
       "fnTrapDesc": fnTrapDesc}
)
