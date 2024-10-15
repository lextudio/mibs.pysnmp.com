# SNMP MIB module (ZhoneMasterAgent-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZhoneMasterAgent-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:20 2024
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

(zhoneMasterAgent,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneMasterAgent",
    "zhoneModules")


# MODULE-IDENTITY

zhoneMasterAgentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 10)
)
zhoneMasterAgentMIB.setRevisions(
        ("2000-09-12 11:16",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _MaRequestPort_Type(Integer32):
    """Custom type maRequestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MaRequestPort_Type.__name__ = "Integer32"
_MaRequestPort_Object = MibScalar
maRequestPort = _MaRequestPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 7, 1),
    _MaRequestPort_Type()
)
maRequestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maRequestPort.setStatus("current")


class _MaTrapPort_Type(Integer32):
    """Custom type maTrapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MaTrapPort_Type.__name__ = "Integer32"
_MaTrapPort_Object = MibScalar
maTrapPort = _MaTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 7, 2),
    _MaTrapPort_Type()
)
maTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maTrapPort.setStatus("current")
_MaPerfSaRequests_Type = Counter32
_MaPerfSaRequests_Object = MibScalar
maPerfSaRequests = _MaPerfSaRequests_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 7, 3),
    _MaPerfSaRequests_Type()
)
maPerfSaRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPerfSaRequests.setStatus("current")
_MaPerfSaResponses_Type = Counter32
_MaPerfSaResponses_Object = MibScalar
maPerfSaResponses = _MaPerfSaResponses_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 7, 4),
    _MaPerfSaResponses_Type()
)
maPerfSaResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPerfSaResponses.setStatus("current")
_MaPerfSnmpErrors_Type = Counter32
_MaPerfSnmpErrors_Object = MibScalar
maPerfSnmpErrors = _MaPerfSnmpErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 7, 5),
    _MaPerfSnmpErrors_Type()
)
maPerfSnmpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPerfSnmpErrors.setStatus("current")
_MaPerfSaTimeouts_Type = Counter32
_MaPerfSaTimeouts_Object = MibScalar
maPerfSaTimeouts = _MaPerfSaTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 7, 6),
    _MaPerfSaTimeouts_Type()
)
maPerfSaTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPerfSaTimeouts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZhoneMasterAgent-MIB",
    **{"maRequestPort": maRequestPort,
       "maTrapPort": maTrapPort,
       "maPerfSaRequests": maPerfSaRequests,
       "maPerfSaResponses": maPerfSaResponses,
       "maPerfSnmpErrors": maPerfSnmpErrors,
       "maPerfSaTimeouts": maPerfSaTimeouts,
       "zhoneMasterAgentMIB": zhoneMasterAgentMIB}
)
