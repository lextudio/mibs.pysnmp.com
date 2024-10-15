# SNMP MIB module (ASCEND-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-FIREWALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:57 2024
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

(DisplayString,
 firewallGroup) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "DisplayString",
    "firewallGroup")

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

_FirewallStatus_ObjectIdentity = ObjectIdentity
firewallStatus = _FirewallStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 16, 1)
)
_FirewallControl_ObjectIdentity = ObjectIdentity
firewallControl = _FirewallControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 16, 2)
)
_FwallCtrlRuleName_Type = DisplayString
_FwallCtrlRuleName_Object = MibScalar
fwallCtrlRuleName = _FwallCtrlRuleName_Object(
    (1, 3, 6, 1, 4, 1, 529, 16, 2, 1),
    _FwallCtrlRuleName_Type()
)
fwallCtrlRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallCtrlRuleName.setStatus("mandatory")


class _FwallCtrlExecute_Type(Integer32):
    """Custom type fwallCtrlExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dis-rule", 3),
          ("enb-rule", 2),
          ("no-op", 1))
    )


_FwallCtrlExecute_Type.__name__ = "Integer32"
_FwallCtrlExecute_Object = MibScalar
fwallCtrlExecute = _FwallCtrlExecute_Object(
    (1, 3, 6, 1, 4, 1, 529, 16, 2, 2),
    _FwallCtrlExecute_Type()
)
fwallCtrlExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallCtrlExecute.setStatus("mandatory")


class _FwallCtrlTimeOut_Type(Integer32):
    """Custom type fwallCtrlTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FwallCtrlTimeOut_Type.__name__ = "Integer32"
_FwallCtrlTimeOut_Object = MibScalar
fwallCtrlTimeOut = _FwallCtrlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 529, 16, 2, 3),
    _FwallCtrlTimeOut_Type()
)
fwallCtrlTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallCtrlTimeOut.setStatus("mandatory")
_FwallCtrlExtAddr_Type = IpAddress
_FwallCtrlExtAddr_Object = MibScalar
fwallCtrlExtAddr = _FwallCtrlExtAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 16, 2, 4),
    _FwallCtrlExtAddr_Type()
)
fwallCtrlExtAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallCtrlExtAddr.setStatus("mandatory")
_FwallCtrlExtAddrMask_Type = IpAddress
_FwallCtrlExtAddrMask_Object = MibScalar
fwallCtrlExtAddrMask = _FwallCtrlExtAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 16, 2, 5),
    _FwallCtrlExtAddrMask_Type()
)
fwallCtrlExtAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallCtrlExtAddrMask.setStatus("mandatory")


class _FwallCtrlExtPort_Type(Integer32):
    """Custom type fwallCtrlExtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FwallCtrlExtPort_Type.__name__ = "Integer32"
_FwallCtrlExtPort_Object = MibScalar
fwallCtrlExtPort = _FwallCtrlExtPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 16, 2, 6),
    _FwallCtrlExtPort_Type()
)
fwallCtrlExtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallCtrlExtPort.setStatus("mandatory")


class _FwallCtrlExtPortMax_Type(Integer32):
    """Custom type fwallCtrlExtPortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FwallCtrlExtPortMax_Type.__name__ = "Integer32"
_FwallCtrlExtPortMax_Object = MibScalar
fwallCtrlExtPortMax = _FwallCtrlExtPortMax_Object(
    (1, 3, 6, 1, 4, 1, 529, 16, 2, 7),
    _FwallCtrlExtPortMax_Type()
)
fwallCtrlExtPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallCtrlExtPortMax.setStatus("mandatory")
_FwallCtrlIntAddr_Type = IpAddress
_FwallCtrlIntAddr_Object = MibScalar
fwallCtrlIntAddr = _FwallCtrlIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 16, 2, 8),
    _FwallCtrlIntAddr_Type()
)
fwallCtrlIntAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallCtrlIntAddr.setStatus("mandatory")
_FwallCtrlIntAddrMask_Type = IpAddress
_FwallCtrlIntAddrMask_Object = MibScalar
fwallCtrlIntAddrMask = _FwallCtrlIntAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 16, 2, 9),
    _FwallCtrlIntAddrMask_Type()
)
fwallCtrlIntAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallCtrlIntAddrMask.setStatus("mandatory")


class _FwallCtrlIntPort_Type(Integer32):
    """Custom type fwallCtrlIntPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FwallCtrlIntPort_Type.__name__ = "Integer32"
_FwallCtrlIntPort_Object = MibScalar
fwallCtrlIntPort = _FwallCtrlIntPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 16, 2, 10),
    _FwallCtrlIntPort_Type()
)
fwallCtrlIntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallCtrlIntPort.setStatus("mandatory")


class _FwallCtrlIntPortMax_Type(Integer32):
    """Custom type fwallCtrlIntPortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FwallCtrlIntPortMax_Type.__name__ = "Integer32"
_FwallCtrlIntPortMax_Object = MibScalar
fwallCtrlIntPortMax = _FwallCtrlIntPortMax_Object(
    (1, 3, 6, 1, 4, 1, 529, 16, 2, 11),
    _FwallCtrlIntPortMax_Type()
)
fwallCtrlIntPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallCtrlIntPortMax.setStatus("mandatory")
_FwallCtrlRoutAddr_Type = IpAddress
_FwallCtrlRoutAddr_Object = MibScalar
fwallCtrlRoutAddr = _FwallCtrlRoutAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 16, 2, 12),
    _FwallCtrlRoutAddr_Type()
)
fwallCtrlRoutAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallCtrlRoutAddr.setStatus("mandatory")
_FwallCtrlAddrOpts_Type = Integer32
_FwallCtrlAddrOpts_Object = MibScalar
fwallCtrlAddrOpts = _FwallCtrlAddrOpts_Object(
    (1, 3, 6, 1, 4, 1, 529, 16, 2, 13),
    _FwallCtrlAddrOpts_Type()
)
fwallCtrlAddrOpts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallCtrlAddrOpts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-FIREWALL-MIB",
    **{"firewallStatus": firewallStatus,
       "firewallControl": firewallControl,
       "fwallCtrlRuleName": fwallCtrlRuleName,
       "fwallCtrlExecute": fwallCtrlExecute,
       "fwallCtrlTimeOut": fwallCtrlTimeOut,
       "fwallCtrlExtAddr": fwallCtrlExtAddr,
       "fwallCtrlExtAddrMask": fwallCtrlExtAddrMask,
       "fwallCtrlExtPort": fwallCtrlExtPort,
       "fwallCtrlExtPortMax": fwallCtrlExtPortMax,
       "fwallCtrlIntAddr": fwallCtrlIntAddr,
       "fwallCtrlIntAddrMask": fwallCtrlIntAddrMask,
       "fwallCtrlIntPort": fwallCtrlIntPort,
       "fwallCtrlIntPortMax": fwallCtrlIntPortMax,
       "fwallCtrlRoutAddr": fwallCtrlRoutAddr,
       "fwallCtrlAddrOpts": fwallCtrlAddrOpts}
)
