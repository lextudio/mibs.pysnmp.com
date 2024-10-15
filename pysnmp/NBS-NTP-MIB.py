# SNMP MIB module (NBS-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:52 2024
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

(nbsCmmcNtpGrp,) = mibBuilder.importSymbols(
    "NBS-CMMC-MIB",
    "nbsCmmcNtpGrp")

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

nbsNtpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _NbsNtpEnable_Type(Integer32):
    """Custom type nbsNtpEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("notSupported", 1),
          ("yes", 3))
    )


_NbsNtpEnable_Type.__name__ = "Integer32"
_NbsNtpEnable_Object = MibScalar
nbsNtpEnable = _NbsNtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 9, 1, 1),
    _NbsNtpEnable_Type()
)
nbsNtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsNtpEnable.setStatus("current")
_NbsNtpServerTableSize_Type = Integer32
_NbsNtpServerTableSize_Object = MibScalar
nbsNtpServerTableSize = _NbsNtpServerTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 9, 1, 2),
    _NbsNtpServerTableSize_Type()
)
nbsNtpServerTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsNtpServerTableSize.setStatus("current")
_NbsNtpServerTable_Object = MibTable
nbsNtpServerTable = _NbsNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 9, 1, 3)
)
if mibBuilder.loadTexts:
    nbsNtpServerTable.setStatus("current")
_NbsNtpServerEntry_Object = MibTableRow
nbsNtpServerEntry = _NbsNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 9, 1, 3, 1)
)
nbsNtpServerEntry.setIndexNames(
    (0, "NBS-NTP-MIB", "nbsNtpServerIpAddr"),
)
if mibBuilder.loadTexts:
    nbsNtpServerEntry.setStatus("current")
_NbsNtpServerIpAddr_Type = IpAddress
_NbsNtpServerIpAddr_Object = MibTableColumn
nbsNtpServerIpAddr = _NbsNtpServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 9, 1, 3, 1, 1),
    _NbsNtpServerIpAddr_Type()
)
nbsNtpServerIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsNtpServerIpAddr.setStatus("current")


class _NbsNtpServerStatus_Type(Integer32):
    """Custom type nbsNtpServerStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("invalid", 1))
    )


_NbsNtpServerStatus_Type.__name__ = "Integer32"
_NbsNtpServerStatus_Object = MibTableColumn
nbsNtpServerStatus = _NbsNtpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 9, 1, 3, 1, 2),
    _NbsNtpServerStatus_Type()
)
nbsNtpServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsNtpServerStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-NTP-MIB",
    **{"nbsNtpMib": nbsNtpMib,
       "nbsNtpEnable": nbsNtpEnable,
       "nbsNtpServerTableSize": nbsNtpServerTableSize,
       "nbsNtpServerTable": nbsNtpServerTable,
       "nbsNtpServerEntry": nbsNtpServerEntry,
       "nbsNtpServerIpAddr": nbsNtpServerIpAddr,
       "nbsNtpServerStatus": nbsNtpServerStatus}
)
