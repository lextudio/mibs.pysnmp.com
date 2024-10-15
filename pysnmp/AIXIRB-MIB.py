# SNMP MIB module (AIXIRB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIXIRB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:27 2024
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

aiXirb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSystemOID_ObjectIdentity = ObjectIdentity
aiSystemOID = _AiSystemOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2)
)
_AiSLC2_ObjectIdentity = ObjectIdentity
aiSLC2 = _AiSLC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16)
)
_AiXirbSystem_ObjectIdentity = ObjectIdentity
aiXirbSystem = _AiXirbSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 1)
)
_AiXirbTcp_ObjectIdentity = ObjectIdentity
aiXirbTcp = _AiXirbTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 2)
)


class _AiXirbTcpWindowSize_Type(Integer32):
    """Custom type aiXirbTcpWindowSize based on Integer32"""
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
        *(("ws1024", 3),
          ("ws200", 1),
          ("ws2048", 4),
          ("ws512", 2))
    )


_AiXirbTcpWindowSize_Type.__name__ = "Integer32"
_AiXirbTcpWindowSize_Object = MibScalar
aiXirbTcpWindowSize = _AiXirbTcpWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 2, 1),
    _AiXirbTcpWindowSize_Type()
)
aiXirbTcpWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiXirbTcpWindowSize.setStatus("current")


class _AiXirbTcpSendAhead_Type(Integer32):
    """Custom type aiXirbTcpSendAhead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AiXirbTcpSendAhead_Type.__name__ = "Integer32"
_AiXirbTcpSendAhead_Object = MibScalar
aiXirbTcpSendAhead = _AiXirbTcpSendAhead_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 2, 2),
    _AiXirbTcpSendAhead_Type()
)
aiXirbTcpSendAhead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiXirbTcpSendAhead.setStatus("current")
_AiXirbX25_ObjectIdentity = ObjectIdentity
aiXirbX25 = _AiXirbX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 3)
)


class _AiXirbBx25CallDown_Type(Integer32):
    """Custom type aiXirbBx25CallDown based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiXirbBx25CallDown_Type.__name__ = "Integer32"
_AiXirbBx25CallDown_Object = MibScalar
aiXirbBx25CallDown = _AiXirbBx25CallDown_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 3, 1),
    _AiXirbBx25CallDown_Type()
)
aiXirbBx25CallDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiXirbBx25CallDown.setStatus("current")


class _AiXirbBx25DMlock_Type(Integer32):
    """Custom type aiXirbBx25DMlock based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 6000000),
    )


_AiXirbBx25DMlock_Type.__name__ = "Integer32"
_AiXirbBx25DMlock_Object = MibScalar
aiXirbBx25DMlock = _AiXirbBx25DMlock_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 3, 2),
    _AiXirbBx25DMlock_Type()
)
aiXirbBx25DMlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiXirbBx25DMlock.setStatus("current")


class _AiXirbBx25LinkUp_Type(Integer32):
    """Custom type aiXirbBx25LinkUp based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 6000000),
    )


_AiXirbBx25LinkUp_Type.__name__ = "Integer32"
_AiXirbBx25LinkUp_Object = MibScalar
aiXirbBx25LinkUp = _AiXirbBx25LinkUp_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 3, 3),
    _AiXirbBx25LinkUp_Type()
)
aiXirbBx25LinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiXirbBx25LinkUp.setStatus("current")
_AiXirbCpuStats_ObjectIdentity = ObjectIdentity
aiXirbCpuStats = _AiXirbCpuStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 4)
)


class _AiXirbCpuStatsCurrent_Type(Integer32):
    """Custom type aiXirbCpuStatsCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AiXirbCpuStatsCurrent_Type.__name__ = "Integer32"
_AiXirbCpuStatsCurrent_Object = MibScalar
aiXirbCpuStatsCurrent = _AiXirbCpuStatsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 4, 1),
    _AiXirbCpuStatsCurrent_Type()
)
aiXirbCpuStatsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiXirbCpuStatsCurrent.setStatus("current")


class _AiXirbCpuStatsMax_Type(Integer32):
    """Custom type aiXirbCpuStatsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AiXirbCpuStatsMax_Type.__name__ = "Integer32"
_AiXirbCpuStatsMax_Object = MibScalar
aiXirbCpuStatsMax = _AiXirbCpuStatsMax_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 4, 2),
    _AiXirbCpuStatsMax_Type()
)
aiXirbCpuStatsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiXirbCpuStatsMax.setStatus("current")


class _AiXirbCpuStatsReset_Type(Integer32):
    """Custom type aiXirbCpuStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_AiXirbCpuStatsReset_Type.__name__ = "Integer32"
_AiXirbCpuStatsReset_Object = MibScalar
aiXirbCpuStatsReset = _AiXirbCpuStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 4, 3),
    _AiXirbCpuStatsReset_Type()
)
aiXirbCpuStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiXirbCpuStatsReset.setStatus("current")
_AiXirbEthernet_ObjectIdentity = ObjectIdentity
aiXirbEthernet = _AiXirbEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 5)
)


class _AiXirbPpc10BaseT_Type(Integer32):
    """Custom type aiXirbPpc10BaseT based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AiXirbPpc10BaseT_Type.__name__ = "Integer32"
_AiXirbPpc10BaseT_Object = MibScalar
aiXirbPpc10BaseT = _AiXirbPpc10BaseT_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 5, 1),
    _AiXirbPpc10BaseT_Type()
)
aiXirbPpc10BaseT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiXirbPpc10BaseT.setStatus("current")


class _AiXirb10BaseTDuplex_Type(Integer32):
    """Custom type aiXirb10BaseTDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_AiXirb10BaseTDuplex_Type.__name__ = "Integer32"
_AiXirb10BaseTDuplex_Object = MibScalar
aiXirb10BaseTDuplex = _AiXirb10BaseTDuplex_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 5, 5, 2),
    _AiXirb10BaseTDuplex_Type()
)
aiXirb10BaseTDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiXirb10BaseTDuplex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIXIRB-MIB",
    **{"aii": aii,
       "aiSystemOID": aiSystemOID,
       "aiSLC2": aiSLC2,
       "aiXirb": aiXirb,
       "aiXirbSystem": aiXirbSystem,
       "aiXirbTcp": aiXirbTcp,
       "aiXirbTcpWindowSize": aiXirbTcpWindowSize,
       "aiXirbTcpSendAhead": aiXirbTcpSendAhead,
       "aiXirbX25": aiXirbX25,
       "aiXirbBx25CallDown": aiXirbBx25CallDown,
       "aiXirbBx25DMlock": aiXirbBx25DMlock,
       "aiXirbBx25LinkUp": aiXirbBx25LinkUp,
       "aiXirbCpuStats": aiXirbCpuStats,
       "aiXirbCpuStatsCurrent": aiXirbCpuStatsCurrent,
       "aiXirbCpuStatsMax": aiXirbCpuStatsMax,
       "aiXirbCpuStatsReset": aiXirbCpuStatsReset,
       "aiXirbEthernet": aiXirbEthernet,
       "aiXirbPpc10BaseT": aiXirbPpc10BaseT,
       "aiXirb10BaseTDuplex": aiXirb10BaseTDuplex}
)
