# SNMP MIB module (CISCO-DMN-DSG-CA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-CA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:17 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ciscoDSGCA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 11)
)
ciscoDSGCA.setRevisions(
        ("2010-08-30 05:00",
         "2010-06-17 06:00",
         "2010-03-22 05:00",
         "2010-02-12 12:00",
         "2009-12-07 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ca_ObjectIdentity = ObjectIdentity
ca = _Ca_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 11, 1)
)


class _CaClearADP_Type(Integer32):
    """Custom type caClearADP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeOnly", 1),
          ("yes", 2))
    )


_CaClearADP_Type.__name__ = "Integer32"
_CaClearADP_Object = MibScalar
caClearADP = _CaClearADP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 11, 1, 1),
    _CaClearADP_Type()
)
caClearADP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caClearADP.setStatus("current")
_CaTable_ObjectIdentity = ObjectIdentity
caTable = _CaTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 11, 2)
)
_CaADPTable_Object = MibTable
caADPTable = _CaADPTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 11, 2, 1)
)
if mibBuilder.loadTexts:
    caADPTable.setStatus("current")
_CaADPEntry_Object = MibTableRow
caADPEntry = _CaADPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 11, 2, 1, 1)
)
caADPEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-CA-MIB", "caIndex"),
)
if mibBuilder.loadTexts:
    caADPEntry.setStatus("current")


class _CaIndex_Type(Integer32):
    """Custom type caIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CaIndex_Type.__name__ = "Integer32"
_CaIndex_Object = MibTableColumn
caIndex = _CaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 11, 2, 1, 1, 1),
    _CaIndex_Type()
)
caIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caIndex.setStatus("current")


class _CaUsrAddr_Type(DisplayString):
    """Custom type caUsrAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CaUsrAddr_Type.__name__ = "DisplayString"
_CaUsrAddr_Object = MibTableColumn
caUsrAddr = _CaUsrAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 11, 2, 1, 1, 2),
    _CaUsrAddr_Type()
)
caUsrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caUsrAddr.setStatus("current")


class _CaISEVer_Type(DisplayString):
    """Custom type caISEVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CaISEVer_Type.__name__ = "DisplayString"
_CaISEVer_Object = MibTableColumn
caISEVer = _CaISEVer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 11, 2, 1, 1, 3),
    _CaISEVer_Type()
)
caISEVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caISEVer.setStatus("current")


class _CaADPEncPass_Type(DisplayString):
    """Custom type caADPEncPass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CaADPEncPass_Type.__name__ = "DisplayString"
_CaADPEncPass_Object = MibTableColumn
caADPEncPass = _CaADPEncPass_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 11, 2, 1, 1, 4),
    _CaADPEncPass_Type()
)
caADPEncPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caADPEncPass.setStatus("current")


class _CaADPEncTotal_Type(DisplayString):
    """Custom type caADPEncTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CaADPEncTotal_Type.__name__ = "DisplayString"
_CaADPEncTotal_Object = MibTableColumn
caADPEncTotal = _CaADPEncTotal_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 11, 2, 1, 1, 5),
    _CaADPEncTotal_Type()
)
caADPEncTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caADPEncTotal.setStatus("current")


class _CaADPNonEncPass_Type(DisplayString):
    """Custom type caADPNonEncPass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CaADPNonEncPass_Type.__name__ = "DisplayString"
_CaADPNonEncPass_Object = MibTableColumn
caADPNonEncPass = _CaADPNonEncPass_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 11, 2, 1, 1, 6),
    _CaADPNonEncPass_Type()
)
caADPNonEncPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caADPNonEncPass.setStatus("current")


class _CaADPNonEncTotal_Type(DisplayString):
    """Custom type caADPNonEncTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CaADPNonEncTotal_Type.__name__ = "DisplayString"
_CaADPNonEncTotal_Object = MibTableColumn
caADPNonEncTotal = _CaADPNonEncTotal_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 11, 2, 1, 1, 7),
    _CaADPNonEncTotal_Type()
)
caADPNonEncTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caADPNonEncTotal.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-CA-MIB",
    **{"ciscoDSGCA": ciscoDSGCA,
       "ca": ca,
       "caClearADP": caClearADP,
       "caTable": caTable,
       "caADPTable": caADPTable,
       "caADPEntry": caADPEntry,
       "caIndex": caIndex,
       "caUsrAddr": caUsrAddr,
       "caISEVer": caISEVer,
       "caADPEncPass": caADPEncPass,
       "caADPEncTotal": caADPEncTotal,
       "caADPNonEncPass": caADPNonEncPass,
       "caADPNonEncTotal": caADPNonEncTotal}
)
